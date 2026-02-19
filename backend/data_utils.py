import requests
from typing import Dict, List, Optional
import re
import json
import logging

logger = logging.getLogger(__name__)

# ------------------------------
# Lineage type detection
# ------------------------------

# Y-DNA haplogroup root letters (ISOGG-standardin mukaan)
_Y_DNA_ROOTS = frozenset("ABCDEFGHIJKLMNOPQRST")

# mtDNA haplogroup root letters
_MT_DNA_ROOTS = frozenset([
    "L", "M", "N",          # makrohaplogrupit
    "A", "B", "C", "D",     # Aasia / Amerikat
    "E", "F", "G",           # Aasia
    "H", "HV",               # Eurooppa
    "I", "J", "K",           # Eurooppa / Lähi-itä
    "P", "Q", "R",           # Oseania / Etelä-Aasia
    "T", "U", "V", "W", "X", "Y", "Z",  # Eurooppa / Aasia
])

# Eksplisiittinen Y-DNA-etuliitteiden lista — nämä ovat yksiselitteisesti Y-DNA:ta
# vaikka niiden juurikirjain löytyy myös mtDNA:sta
_Y_DNA_EXPLICIT_PREFIXES = (
    "A0", "A00", "A1", "A2", "A3",
    "B2", "B4",
    "C1", "C2", "C3",
    "DE", "D1", "D2",
    "E1", "E2",
    "F1", "F2",
    "G1", "G2",
    # H1/H2 poistettu — konfliktoi mtDNA:n kanssa
    "I1", "I2",
    # J1/J2 poistettu — J1/J2 on sekä Y-DNA (J1a, J2a) että mtDNA (J1c, J2b)
    # ilman kolmatta kirjainta/numeroa ei voida erottaa → ambiguous
    # K1/K2 poistettu — konfliktoi mtDNA:n kanssa
    "L1",
    # M1 poistettu — konfliktoi mtDNA:n kanssa
    "N1", "N2",
    "O1", "O2",
    "P1",
    "Q1",
    "R1", "R2",
    "S1",
    # T1 poistettu — konfliktoi mtDNA:n kanssa
)

# mtDNA-etuliitteet — tarkistetaan VASTA Y-DNA-tarkistuksen jälkeen
_MT_DNA_EXPLICIT_PREFIXES = (
    "MT-", "MTDNA",
    "L0", "L1", "L2", "L3", "L4", "L5", "L6",
    "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9",
    "HV0", "HV1", "HV2",
    "H1", "H2", "H3", "H4", "H5", "H6", "H7",
    "U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8",
    "K1", "K2",
    "T1", "T2",
    "X2",
)


def detect_lineage_type(haplogroup: str) -> str:
    """
    Tunnistaa haploryhmän linjatypin (Y-DNA / mtDNA / ambiguous).

    Logiikka (järjestys on tärkeä — Y-DNA tarkistetaan ennen mtDNA):
    1. Alkaa MT- tai MTDNA- → yksiselitteisesti mtDNA
    2. Alkaa Y-kirjaimella → Y-DNA
    3. Eksplisiittiset Y-DNA-etuliitteet → Y-DNA  (tarkistetaan ENNEN mtDNA)
    4. Eksplisiittiset mtDNA-etuliitteet → mtDNA
    5. Yksittäiskirjaimet joita käytetään vain mtDNA:ssa → mtDNA
    6. Muut → "ambiguous" (ei arvata väärin)

    Huom: J1/J2 ovat Y-DNA:ta (ISOGG), H1-H7 ovat mtDNA:ta.
    Kontekstiriippuvaiset tapaukset (esim. pelkkä "A", "N") → ambiguous.
    """
    hg = haplogroup.upper().strip()
    if not hg:
        return "ambiguous"

    # 1. Selkeät MT-etuliitteet
    if hg.startswith("MT-") or hg.startswith("MTDNA"):
        return "mtDNA"

    # 2. Y-kirjaimella alkavat
    if hg.startswith("Y"):
        return "Y-DNA"

    # 3. Eksplisiittiset Y-DNA-etuliitteet (ENNEN mtDNA-tarkistusta)
    for prefix in _Y_DNA_EXPLICIT_PREFIXES:
        if hg.startswith(prefix):
            return "Y-DNA"

    # 4. Eksplisiittiset mtDNA-etuliitteet
    for prefix in _MT_DNA_EXPLICIT_PREFIXES:
        if hg.startswith(prefix):
            return "mtDNA"

    # 5. Yksittäiskirjaimet jotka ovat yksiselitteisesti mtDNA-käytössä
    #    (ei esiinny Y-DNA-puussa juuritasolla)
    mtdna_only_singles = {"V", "W", "X"}
    if hg[0] in mtdna_only_singles:
        return "mtDNA"

    # 6. Epäselvä — ei arvata
    return "ambiguous"


# ------------------------------
# Structured description fragments
# ------------------------------

# description_fragments tallennetaan rakenteisena datana tekstin sijaan.
# Näin story_utils.py voi hakea oikean käännöksen i18n-järjestelmästä.
#
# Rakenne:
# {
#   "key": str,          # i18n-avain
#   "source": str,       # lähteen tunniste (loggausta varten)
#   "params": Dict,      # format()-parametrit käännösmalliin
# }

DescriptionFragment = Dict  # {"key": str, "source": str, "params": Dict}


def make_fragment(key: str, source: str, **params) -> DescriptionFragment:
    """Luo rakenteisen description_fragment-objektin."""
    return {"key": key, "source": source, "params": params}


# ------------------------------
# Reliability scoring
# ------------------------------

# Staattinen pisteytys per lähdefunktio — ei merkkijonoheuristiikkaa
SOURCE_RELIABILITY_SCORES: Dict[str, int] = {
    # Akateemiset (korkein luottamus)
    "pubmed.ncbi.nlm.nih.gov": 10,
    "ebi.ac.uk/ena": 10,
    "Russian Academy of Sciences": 10,
    "Nature Eurasia": 10,

    # Erikoistuneet genomitietokannat
    "yfull.com": 8,
    "isogg.org": 8,
    "haplogrep.i-med.ac.at": 8,
    "RIKEN": 8,
    "cngb.org": 7,
    "bgi.com": 7,
    "Korean Genome Project": 7,
    "Japanese Genome Database": 7,

    # Kaupalliset mutta luotettavat
    "familytreedna.com": 6,
    "ancientdna.info": 6,
    "AncestryDNA": 5,
    "FamilyTreeDNA": 5,
    "MyHeritage": 5,
    "Nebula Genomics": 5,
    "Living DNA": 5,
    "Sequencing.com": 4,
    "Genomelink": 4,

    # Hakemistot ja yhteisöt
    "eupedia.com": 4,
    "geni.com": 3,
    "eLIBRARY.RU": 4,

    # Analyysityökalut
    "MyTrueAncestry": 4,
    "GEDmatch": 4,
    "Genoplot": 4,
    "Illustrative DNA": 4,

    # Alueelliset journaalit (matala prioriteetti — ei peer-review-varmistusta)
    "Middle Eastern Archaeogenetics Journals": 3,
    "South Asian Archaeogenetics Journals": 3,
    "SE Asian Archaeogenetics Journals": 3,
    "African Archaeogenetics Journals": 3,
    "North African Archaeogenetics Journals": 3,
    "Sub-Saharan Archaeogenetics Journals": 3,
    "Native American Archaeogenetics Journals": 3,
    "South American Archaeogenetics Journals": 3,
    "Caribbean Archaeogenetics Journals": 3,
    "Arctic Archaeogenetics Journals": 3,
    "Australian Archaeogenetics Journals": 3,
    "Polynesian Archaeogenetics Journals": 3,
    "Melanesian Archaeogenetics Journals": 3,
    "Micronesian Archaeogenetics Journals": 3,
    "New Zealand Archaeogenetics Journals": 3,
    "Indian Ocean Archaeogenetics Journals": 3,
    "North Atlantic Archaeogenetics Journals": 3,
}

_DEFAULT_SOURCE_SCORE = 2  # tuntematon lähde


def calculate_reliability(new_data: Dict) -> int:
    """
    Laskee luotettavuuspisteet staattisen pisteytyslistan perusteella.
    Jokainen lähde lasketaan vain kerran (deduplikoitu kutsukohtaisesti).
    """
    score = 0
    for source in new_data.get("sources", []):
        score += SOURCE_RELIABILITY_SCORES.get(source, _DEFAULT_SOURCE_SCORE)
    return score


# ------------------------------
# Core interface
# ------------------------------

def fetch_full_haplogroup_data(haplogroup: str) -> Dict:
    """
    Yhdistää globaalisti useista lähteistä haploryhmädataa ja palauttaa
    yhtenäisen arkeogeneettisen tietorakenteen.
    Tämä moduuli EI muodosta käyttäjätekstiä – vain raakadataa ja faktarakenteita.
    """
    haplogroup = haplogroup.upper().strip()
    if not re.match(r'^[A-Z0-9-]+$', haplogroup):
        raise ValueError(f"Virheellinen haploryhmä: {haplogroup}")

    data: Dict = {
        "haplogroup": haplogroup,
        "lineage_type": detect_lineage_type(haplogroup),
        "description_fragments": [],   # List[DescriptionFragment]
        "regions": [],
        "ancient_samples": [],
        "time_depth": "",
        "sources": [],
        "raw_data_providers": [],
        "analysis_tools": [],
        "regional_profiles": [],
        "reliability_score": 0,
        "privacy_notice": "Never share your raw DNA data without informed consent.",
    }

    source_funcs = [
        # Länsi / globaali
        fetch_from_yfull,
        fetch_from_familytreedna,
        fetch_from_haplogrep,
        fetch_from_eupedia,
        fetch_from_geni,
        fetch_from_isogg,

        # Arkeogenetiikka / arkistot
        fetch_from_ancientdna_info,
        fetch_from_european_nucleotide_archive,
        fetch_from_pubmed,

        # Euraasia
        fetch_from_russian_academic_sources,
        fetch_from_eurasian_archaeogenetics,
        fetch_from_middle_east_archaeogenetics,
        fetch_from_south_asian_archaeogenetics,

        # Itä-Aasia
        fetch_from_chinese_genomic_databases,
        fetch_from_korean_genomics,
        fetch_from_japanese_genomics,
        fetch_from_southeast_asian_archaeogenetics,

        # Afrikka
        fetch_from_african_archaeogenetics,
        fetch_from_north_african_archaeogenetics,
        fetch_from_subsaharan_archaeogenetics,

        # Amerikat
        fetch_from_native_american_archaeogenetics,
        fetch_from_south_american_archaeogenetics,
        fetch_from_caribbean_archaeogenetics,
        fetch_from_arctic_archaeogenetics,

        # Oseania & saaristot
        fetch_from_australian_archaeogenetics,
        fetch_from_polynesian_archaeogenetics,
        fetch_from_melanesian_archaeogenetics,
        fetch_from_micronesian_archaeogenetics,
        fetch_from_new_zealand_archaeogenetics,
        fetch_from_indian_ocean_islands,
        fetch_from_north_atlantic_islands,

        # Raakadata & analyysimoottorit
        fetch_raw_data_providers,
        fetch_analysis_tools,
    ]

    for source_func in source_funcs:
        try:
            new_data = source_func(haplogroup)
            data = merge_data(data, new_data)
            data["reliability_score"] += calculate_reliability(new_data)
        except Exception as e:
            logger.warning(f"Virhe lähteessä {source_func.__name__}: {e}")

    # Integraatio: ancient_samples_db
    # Kutsutaan source_funcs-loopin jälkeen — kureertu tietokanta, ei verkkohaku.
    # Deduplikointi ID:n perusteella suojaa tuplilta jos muut lähteet
    # lisäävät saman näytteen (esim. ancientdna_info).
    try:
        from ancient_samples_db import get_samples_for_haplogroup
        db_samples = get_samples_for_haplogroup(haplogroup)
        if db_samples:
            data["ancient_samples"] = _merge_ancient_samples_by_id(
                data["ancient_samples"], db_samples
            )
            logger.info(
                f"ancient_samples_db: {len(db_samples)} näytettä haploryhmälle {haplogroup}"
            )
    except ImportError:
        logger.warning("ancient_samples_db ei ole saatavilla — ohitetaan")
    except Exception as e:
        logger.warning(f"Virhe ancient_samples_db-haussa ({haplogroup}): {e}")

    # Final cleanup
    data["regions"] = sorted(set(data.get("regions", [])))
    data["sources"] = sorted(set(data.get("sources", [])))
    data["raw_data_providers"] = unique_by_key(data.get("raw_data_providers", []), "name")
    data["analysis_tools"] = unique_by_key(data.get("analysis_tools", []), "name")
    data["regional_profiles"] = unique_by_key(data.get("regional_profiles", []), "region")

    # Deduploi fragmentit avaimen + parametrien perusteella
    seen_fragments: set = set()
    deduped: List[DescriptionFragment] = []
    for frag in data["description_fragments"]:
        frag_id = (frag.get("key"), json.dumps(frag.get("params", {}), sort_keys=True))
        if frag_id not in seen_fragments:
            seen_fragments.add(frag_id)
            deduped.append(frag)
    data["description_fragments"] = deduped

    data["reliability_score"] = min(100, data["reliability_score"])

    return data


# ------------------------------
# Utility functions
# ------------------------------

def merge_data(base: Dict, new: Dict) -> Dict:
    if not new:
        return base

    base.setdefault("description_fragments", []).extend(new.get("description_fragments", []))
    base.setdefault("regions", []).extend(new.get("regions", []))
    base.setdefault("ancient_samples", []).extend(new.get("ancient_samples", []))
    base.setdefault("sources", []).extend(new.get("sources", []))
    base.setdefault("raw_data_providers", []).extend(new.get("raw_data_providers", []))
    base.setdefault("analysis_tools", []).extend(new.get("analysis_tools", []))
    base.setdefault("regional_profiles", []).extend(new.get("regional_profiles", []))

    if not base.get("time_depth") and new.get("time_depth"):
        base["time_depth"] = new["time_depth"]

    return base


def unique_by_key(items: List[Dict], key: str) -> List[Dict]:
    seen = set()
    out = []
    for item in items:
        val = item.get(key)
        if val and val not in seen:
            seen.add(val)
            out.append(item)
    return out


def _merge_ancient_samples_by_id(
    existing: List[Dict], incoming: List[Dict]
) -> List[Dict]:
    """
    Yhdistää kaksi ancient_samples-listaa deduplikoiden ID:n perusteella.
    Prioriteetti: existing voittaa — jo olemassa oleva data säilyy.
    incoming-näytteet lisätään perään jos ID:tä ei vielä ole.
    """
    existing_ids = {s.get("id") for s in existing if s.get("id")}
    merged = list(existing)
    for sample in incoming:
        if sample.get("id") not in existing_ids:
            merged.append(sample)
            existing_ids.add(sample.get("id"))
    return merged


def export_to_json(data: Dict, filename: str = "haplogroup_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logger.info(f"Data viety tiedostoon: {filename}")


def render_fragments(fragments: List[DescriptionFragment], lang: str = "en") -> List[str]:
    """
    Muuntaa rakenteelliset fragmentit lokalisoiduiksi tekstimerkkijonoiksi.
    Kutsutaan story_utils.py:stä — ei data_utils.py:stä.

    Tarvitsee i18n_utils.get_text() -funktion.
    Lazy import välttää sirkkulaarisen riippuvuuden.
    """
    try:
        from i18n_utils import get_text
    except ImportError:
        # Fallback: palauta avain jos i18n ei ole saatavilla
        return [f["key"] for f in fragments]

    result = []
    for frag in fragments:
        try:
            text = get_text(frag["key"], lang=lang, **frag.get("params", {}))
            result.append(text)
        except (KeyError, TypeError) as e:
            logger.warning(f"Fragment render failed for key '{frag.get('key')}': {e}")
            result.append(frag.get("key", ""))
    return result


# ------------------------------
# Dynaamiset lähteet
# ------------------------------

def fetch_from_pubmed(haplogroup: str) -> Dict:
    try:
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": f"{haplogroup} haplogroup ancient DNA",
            "retmode": "xml",
        }
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            count_match = re.search(r'<Count>(\d+)</Count>', response.text)
            num_papers = int(count_match.group(1)) if count_match else 0
            return {
                "description_fragments": [
                    make_fragment("source_pubmed_count", "pubmed", haplogroup=haplogroup, count=num_papers)
                ],
                "sources": ["pubmed.ncbi.nlm.nih.gov"],
            }
        return {}
    except Exception as e:
        logger.warning(f"PubMed-haku epäonnistui: {e}")
        return {}


def fetch_from_isogg(haplogroup: str) -> Dict:
    return {
        "description_fragments": [
            make_fragment("source_isogg", "isogg", haplogroup=haplogroup)
        ],
        "sources": ["isogg.org"],
    }


# ------------------------------
# Länsimaiset / globaalit tietokannat
# ------------------------------

def fetch_from_yfull(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_yfull", "yfull", haplogroup=haplogroup)],
        "regions": ["Europe", "Middle East", "Central Asia"],
        "sources": ["yfull.com"],
    }


def fetch_from_familytreedna(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_familytreedna", "familytreedna", haplogroup=haplogroup)],
        "regions": ["Europe", "North America"],
        "sources": ["familytreedna.com"],
    }


def fetch_from_haplogrep(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_haplogrep", "haplogrep", haplogroup=haplogroup)],
        "sources": ["haplogrep.i-med.ac.at"],
    }


def fetch_from_eupedia(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_eupedia", "eupedia", haplogroup=haplogroup)],
        "regions": ["Europe", "Middle East", "North Africa"],
        "sources": ["eupedia.com"],
    }


def fetch_from_geni(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_geni", "geni", haplogroup=haplogroup)],
        "sources": ["geni.com"],
    }


def fetch_from_ancientdna_info(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_ancientdna_info", "ancientdna_info", haplogroup=haplogroup)],
        "regions": ["Europe", "Siberia", "Middle East"],
        "sources": ["ancientdna.info"],
    }


def fetch_from_european_nucleotide_archive(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_ena", "ena", haplogroup=haplogroup)],
        "regions": ["Europe"],
        "sources": ["ebi.ac.uk/ena"],
    }


# ------------------------------
# Euraasia
# ------------------------------

def fetch_from_russian_academic_sources(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_russian_academic", "russian_academic", haplogroup=haplogroup)],
        "regions": ["Siberia", "Volga", "Caucasus", "Eastern Europe"],
        "sources": ["eLIBRARY.RU", "Russian Academy of Sciences"],
    }


def fetch_from_eurasian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_eurasian_archaeogenetics", "eurasian_arch", haplogroup=haplogroup)],
        "regions": ["Central Asia", "Pontic Steppe", "Altai", "Ural"],
        "sources": ["Nature Eurasia"],
    }


def fetch_from_middle_east_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_middle_east_archaeogenetics", "middle_east_arch", haplogroup=haplogroup)],
        "regions": ["Middle East"],
        "sources": ["Middle Eastern Archaeogenetics Journals"],
    }


def fetch_from_south_asian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_south_asian_archaeogenetics", "south_asian_arch", haplogroup=haplogroup)],
        "regions": ["India", "Pakistan", "Sri Lanka"],
        "sources": ["South Asian Archaeogenetics Journals"],
    }


# ------------------------------
# Itä- ja Kaakkois-Aasia
# ------------------------------

def fetch_from_chinese_genomic_databases(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_chinese_genomics", "chinese_genomics", haplogroup=haplogroup)],
        "regions": ["China", "Mongolia", "Tibet"],
        "sources": ["cngb.org", "bgi.com"],
    }


def fetch_from_korean_genomics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_korean_genomics", "korean_genomics", haplogroup=haplogroup)],
        "regions": ["Korea"],
        "sources": ["Korean Genome Project"],
    }


def fetch_from_japanese_genomics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_japanese_genomics", "japanese_genomics", haplogroup=haplogroup)],
        "regions": ["Japan"],
        "sources": ["RIKEN", "Japanese Genome Database"],
    }


def fetch_from_southeast_asian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_southeast_asian_archaeogenetics", "sea_arch", haplogroup=haplogroup)],
        "regions": ["Thailand", "Vietnam", "Indonesia", "Philippines"],
        "sources": ["SE Asian Archaeogenetics Journals"],
    }


# ------------------------------
# Afrikka
# ------------------------------

def fetch_from_african_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_african_archaeogenetics", "african_arch", haplogroup=haplogroup)],
        "regions": ["Africa"],
        "sources": ["African Archaeogenetics Journals"],
    }


def fetch_from_north_african_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_north_african_archaeogenetics", "north_african_arch", haplogroup=haplogroup)],
        "regions": ["North Africa"],
        "sources": ["North African Archaeogenetics Journals"],
    }


def fetch_from_subsaharan_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_subsaharan_archaeogenetics", "subsaharan_arch", haplogroup=haplogroup)],
        "regions": ["Sub-Saharan Africa"],
        "sources": ["Sub-Saharan Archaeogenetics Journals"],
    }


# ------------------------------
# Amerikat
# ------------------------------

def fetch_from_native_american_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_native_american_archaeogenetics", "native_american_arch", haplogroup=haplogroup)],
        "regions": ["North America"],
        "sources": ["Native American Archaeogenetics Journals"],
    }


def fetch_from_south_american_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_south_american_archaeogenetics", "south_american_arch", haplogroup=haplogroup)],
        "regions": ["South America"],
        "sources": ["South American Archaeogenetics Journals"],
    }


def fetch_from_caribbean_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_caribbean_archaeogenetics", "caribbean_arch", haplogroup=haplogroup)],
        "regions": ["Caribbean"],
        "sources": ["Caribbean Archaeogenetics Journals"],
    }


def fetch_from_arctic_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_arctic_archaeogenetics", "arctic_arch", haplogroup=haplogroup)],
        "regions": ["Arctic"],
        "sources": ["Arctic Archaeogenetics Journals"],
    }


# ------------------------------
# Oseania & saaristot
# ------------------------------

def fetch_from_australian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_australian_archaeogenetics", "australian_arch", haplogroup=haplogroup)],
        "regions": ["Australia"],
        "sources": ["Australian Archaeogenetics Journals"],
    }


def fetch_from_polynesian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_polynesian_archaeogenetics", "polynesian_arch", haplogroup=haplogroup)],
        "regions": ["Polynesia"],
        "sources": ["Polynesian Archaeogenetics Journals"],
    }


def fetch_from_melanesian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_melanesian_archaeogenetics", "melanesian_arch", haplogroup=haplogroup)],
        "regions": ["Melanesia"],
        "sources": ["Melanesian Archaeogenetics Journals"],
    }


def fetch_from_micronesian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_micronesian_archaeogenetics", "micronesian_arch", haplogroup=haplogroup)],
        "regions": ["Micronesia"],
        "sources": ["Micronesian Archaeogenetics Journals"],
    }


def fetch_from_new_zealand_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_new_zealand_archaeogenetics", "nz_arch", haplogroup=haplogroup)],
        "regions": ["New Zealand"],
        "sources": ["New Zealand Archaeogenetics Journals"],
    }


def fetch_from_indian_ocean_islands(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_indian_ocean_islands", "indian_ocean_arch", haplogroup=haplogroup)],
        "regions": ["Indian Ocean Islands"],
        "sources": ["Indian Ocean Archaeogenetics Journals"],
    }


def fetch_from_north_atlantic_islands(haplogroup: str) -> Dict:
    return {
        "description_fragments": [make_fragment("source_north_atlantic_islands", "north_atlantic_arch", haplogroup=haplogroup)],
        "regions": ["Iceland", "Faroe Islands", "Orkney", "Shetland"],
        "sources": ["North Atlantic Archaeogenetics Journals"],
    }


# ------------------------------
# Raakadata & analyysimoottorit
# ------------------------------

def fetch_raw_data_providers(haplogroup: str) -> Dict:
    providers = [
        {
            "name": "Nebula Genomics",
            "type": "WGS",
            "coverage": "30x–100x WGS",
            "focus_key": "provider_focus_nebula",
            "notes_key": "provider_notes_nebula",
            "url": "https://nebula.org",
        },
        {
            "name": "AncestryDNA",
            "type": "Autosomal SNP array",
            "coverage": "~600k–700k SNPs",
            "focus_key": "provider_focus_ancestry",
            "notes_key": "provider_notes_ancestry",
            "url": "https://www.ancestry.com/dna",
        },
        {
            "name": "FamilyTreeDNA",
            "type": "Y-DNA / mtDNA / autosomal",
            "coverage": "Specialized lineage tests + autosomal",
            "focus_key": "provider_focus_ftdna",
            "notes_key": "provider_notes_ftdna",
            "url": "https://www.familytreedna.com",
        },
        {
            "name": "Living DNA",
            "type": "Autosomal + lineages",
            "coverage": "Microarray + lineage interpretation",
            "focus_key": "provider_focus_livingdna",
            "notes_key": "provider_notes_livingdna",
            "url": "https://livingdna.com",
        },
        {
            "name": "MyHeritage DNA",
            "type": "Autosomal SNP array",
            "coverage": "Comparable to Ancestry/23andMe",
            "focus_key": "provider_focus_myheritage",
            "notes_key": "provider_notes_myheritage",
            "url": "https://www.myheritage.com/dna",
        },
        {
            "name": "Sequencing.com",
            "type": "WGS / WES / SNP upload",
            "coverage": "WGS/WES + app marketplace",
            "focus_key": "provider_focus_sequencing",
            "notes_key": "provider_notes_sequencing",
            "url": "https://sequencing.com",
        },
        {
            "name": "Genomelink",
            "type": "Raw DNA upload",
            "coverage": "Depends on source",
            "focus_key": "provider_focus_genomelink",
            "notes_key": "provider_notes_genomelink",
            "url": "https://genomelink.io",
        },
    ]

    return {
        "description_fragments": [
            make_fragment("source_raw_data_providers", "raw_data_providers", haplogroup=haplogroup)
        ],
        "sources": [
            "Nebula Genomics", "AncestryDNA", "FamilyTreeDNA",
            "Living DNA", "MyHeritage", "Sequencing.com", "Genomelink",
        ],
        "raw_data_providers": providers,
    }


def fetch_analysis_tools(haplogroup: str) -> Dict:
    tools = [
        {
            "name": "MyTrueAncestry",
            "type": "Ancient DNA matching",
            "focus_key": "tool_focus_mytrueancestry",
            "compatibility": "Autosomal, Y-DNA, mtDNA, WGS",
            "notes_key": "tool_notes_mytrueancestry",
            "url": "https://mytrueancestry.com",
        },
        {
            "name": "GEDmatch",
            "type": "Admixture & heritage tools",
            "focus_key": "tool_focus_gedmatch",
            "compatibility": "Most consumer test raw data formats",
            "notes_key": "tool_notes_gedmatch",
            "url": "https://www.gedmatch.com",
        },
        {
            "name": "Genoplot / G25",
            "type": "G25 modeling",
            "focus_key": "tool_focus_genoplot",
            "compatibility": "Multiple raw data formats",
            "notes_key": "tool_notes_genoplot",
            "url": "https://genoplot.com",
        },
        {
            "name": "Illustrative DNA",
            "type": "G25-based ancient modeling",
            "focus_key": "tool_focus_illustrativedna",
            "compatibility": "Ancestry, 23andMe, MyHeritage, FTDNA",
            "notes_key": "tool_notes_illustrativedna",
            "url": "https://illustrativedna.com",
        },
        {
            "name": "Genomelink Ancient Ancestry",
            "type": "Trait & ancient ancestry",
            "focus_key": "tool_focus_genomelink_ancient",
            "compatibility": "Most consumer tests",
            "notes_key": "tool_notes_genomelink_ancient",
            "url": "https://genomelink.io",
        },
        {
            "name": "Nebula Genomics (upload)",
            "type": "Raw DNA upload & WGS analysis",
            "focus_key": "tool_focus_nebula_upload",
            "compatibility": "AncestryDNA, 23andMe, MyHeritage etc.",
            "notes_key": "tool_notes_nebula_upload",
            "url": "https://nebula.org/free-dna-upload-analysis/",
        },
    ]

    return {
        "description_fragments": [
            make_fragment("source_analysis_tools", "analysis_tools", haplogroup=haplogroup)
        ],
        "sources": [
            "MyTrueAncestry", "GEDmatch", "Genoplot",
            "Illustrative DNA", "Genomelink", "Nebula Genomics",
        ],
        "analysis_tools": tools,
    }


# ------------------------------
# CLI-käyttö (kehittäjille)
# ------------------------------

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Käyttö: python data_utils.py <haploryhmä> [export]")
        sys.exit(1)

    haplogroup_arg = sys.argv[1]
    result = fetch_full_haplogroup_data(haplogroup_arg)

    print(json.dumps(result, indent=4, ensure_ascii=False))

    if len(sys.argv) > 2 and sys.argv[2] == "export":
        export_to_json(result)
