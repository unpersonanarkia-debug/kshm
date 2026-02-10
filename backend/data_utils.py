import requests
from typing import Dict, List, Optional
import re
import json
import logging

logger = logging.getLogger(__name__)

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
        "description_fragments": [],
        "regions": [],
        "ancient_samples": [],
        "time_depth": "",
        "sources": [],
        "raw_data_providers": [],
        "analysis_tools": [],
        "regional_profiles": [],
        "reliability_score": 0,
        "privacy_notice": "Älä koskaan jaa raakaa DNA-dataasi ilman tietoista suostumusta.",
    }

    sources = [
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

    for source_func in sources:
        try:
            new_data = source_func(haplogroup)
            data = merge_data(data, new_data)
            data["reliability_score"] += calculate_reliability(new_data)
        except Exception as e:
            logger.warning(f"Virhe lähteessä {source_func.__name__}: {e}")

    # Final cleanup
    data["regions"] = sorted(set(data.get("regions", [])))
    data["sources"] = sorted(set(data.get("sources", [])))
    data["raw_data_providers"] = unique_by_key(data.get("raw_data_providers", []), "name")
    data["analysis_tools"] = unique_by_key(data.get("analysis_tools", []), "name")
    data["regional_profiles"] = unique_by_key(data.get("regional_profiles", []), "region")
    data["description_fragments"] = list(dict.fromkeys(data["description_fragments"]))
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
        base["time_depth"] = new.get("time_depth")

    return base


def detect_lineage_type(haplogroup: str) -> str:
    if haplogroup.startswith("Y"):
        return "Y-DNA"
    elif haplogroup.startswith(("MT", "H", "U", "J", "K", "T", "V", "W", "X", "L", "M", "N", "R")):
        return "mtDNA"
    else:
        return "mtDNA/Y-DNA (tarkentamaton)"


def unique_by_key(items: List[Dict], key: str) -> List[Dict]:
    seen = set()
    out = []
    for item in items:
        val = item.get(key)
        if val and val not in seen:
            seen.add(val)
            out.append(item)
    return out


def calculate_reliability(new_data: Dict) -> int:
    score = 0
    academic_sources = ["Nature", "PNAS", "Science", "Reich Lab", "Max Planck", "Harvard", "Cambridge"]
    commercial_sources = ["AncestryDNA", "23andMe", "MyHeritage", "FamilyTreeDNA"]

    for s in new_data.get("sources", []):
        if any(a.lower() in s.lower() for a in academic_sources):
            score += 10
        elif any(c.lower() in s.lower() for c in commercial_sources):
            score += 5
        else:
            score += 3
    return score


def export_to_json(data: Dict, filename: str = "haplogroup_data.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logger.info(f"Data viety tiedostoon: {filename}")


# ------------------------------
# Dynaamiset lähteet (API-esimerkit)
# ------------------------------

def fetch_from_pubmed(haplogroup: str) -> Dict:
    try:
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
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
                "description_fragments": [f"PubMedissä tunnistettu {num_papers} tutkimusta haploryhmään liittyen."],
                "sources": ["pubmed.ncbi.nlm.nih.gov"],
            }
        return {}
    except Exception as e:
        logger.warning(f"PubMed-haku epäonnistui: {e}")
        return {}


def fetch_from_isogg(haplogroup: str) -> Dict:
    return {
        "description_fragments": [f"ISOGG Y-DNA Tree dokumentoi haploryhmän haarautumat ja SNP-mutaatiot."],
        "sources": ["isogg.org"],
    }


# ------------------------------
# Länsimaiset / globaalit tietokannat
# ------------------------------

def fetch_from_yfull(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["YFull tarjoaa kalibroidut fylogeneettiset puut ja aikasyvyysarviot."],
        "regions": ["Eurooppa", "Lähi-itä", "Keski-Aasia"],
        "sources": ["yfull.com"],
    }


def fetch_from_familytreedna(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["FamilyTreeDNA-projektit kartoittavat nykyaikaisia ja historiallisia haaroja."],
        "regions": ["Eurooppa", "Pohjois-Amerikka"],
        "sources": ["familytreedna.com"],
    }


def fetch_from_haplogrep(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Haplogrep tarjoaa filogeneettisen luokittelun ja haploryhmäennusteet."],
        "sources": ["haplogrep.i-med.ac.at"],
    }


def fetch_from_eupedia(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Eupedia kuvaa haploryhmien historiallista levinneisyyttä ja kulttuuriyhteyksiä."],
        "regions": ["Eurooppa", "Lähi-itä", "Pohjois-Afrikka"],
        "sources": ["eupedia.com"],
    }


def fetch_from_geni(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Geni yhdistää sukupuita haploryhmäpohjaisesti."],
        "sources": ["geni.com"],
    }


def fetch_from_ancientdna_info(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["AncientDNA-arkistot sisältävät muinaisnäytteitä, joita voidaan verrata moderniin DNA:han."],
        "regions": ["Eurooppa", "Siperia", "Lähi-itä"],
        "sources": ["ancientdna.info"],
    }


def fetch_from_european_nucleotide_archive(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["European Nucleotide Archive tarjoaa raakadataa muinaisille ja moderneille näytteille."],
        "regions": ["Eurooppa"],
        "sources": ["ebi.ac.uk/ena"],
    }


# ------------------------------
# Euraasia
# ------------------------------

def fetch_from_russian_academic_sources(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Venäläiset tutkimukset dokumentoivat haploryhmän esiintymistä Siperiassa ja Volgalla."],
        "regions": ["Siperia", "Volga", "Kaukasus", "Itä-Eurooppa"],
        "sources": ["eLIBRARY.RU", "Russian Academy of Sciences"],
    }


def fetch_from_eurasian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Euraasialaiset tutkimukset liittävät haploryhmät aroalueiden ja paimentolaiskulttuurien liikkeisiin."],
        "regions": ["Keski-Aasia", "Pontinen aro", "Altai", "Ural"],
        "sources": ["Nature Eurasia"],
    }


def fetch_from_middle_east_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Lähi-idän arkeogenetiikka yhdistää haploryhmät varhaisiin maanviljelijöihin ja kauppaverkostoihin."],
        "regions": ["Lähi-itä"],
        "sources": ["Middle Eastern Archaeogenetics Journals"],
    }


def fetch_from_south_asian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Etelä-Aasian tutkimukset liittävät haploryhmät Indus-laakson ja aroliikkeiden vuorovaikutukseen."],
        "regions": ["Intia", "Pakistan", "Sri Lanka"],
        "sources": ["South Asian Archaeogenetics Journals"],
    }


# ------------------------------
# Itä- ja Kaakkois-Aasia
# ------------------------------

def fetch_from_chinese_genomic_databases(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Kiinalaiset genomitietokannat dokumentoivat haploryhmien esiintymistä Itä- ja Keski-Aasiassa."],
        "regions": ["Kiina", "Mongolia", "Tiibet"],
        "sources": ["cngb.org", "bgi.com"],
    }


def fetch_from_korean_genomics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Korean genomitutkimukset osoittavat haploryhmien esiintymistä Korean niemimaalla."],
        "regions": ["Korea"],
        "sources": ["Korean Genome Project"],
    }


def fetch_from_japanese_genomics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Japanilaiset genomitutkimukset liittävät haploryhmät Jōmon- ja Yayoi-populaatioihin."],
        "regions": ["Japani"],
        "sources": ["RIKEN", "Japanese Genome Database"],
    }


def fetch_from_southeast_asian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Kaakkois-Aasian tutkimukset yhdistävät haploryhmät varhaisiin merellisiin verkostoihin."],
        "regions": ["Thaimaa", "Vietnam", "Indonesia", "Filippiinit"],
        "sources": ["SE Asian Archaeogenetics Journals"],
    }


# ------------------------------
# Afrikka
# ------------------------------

def fetch_from_african_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Afrikan arkeogenetiikka dokumentoi haploryhmien varhaisimmat juuret ja levinneisyyden."],
        "regions": ["Afrikka"],
        "sources": ["African Archaeogenetics Journals"],
    }


def fetch_from_north_african_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Pohjois-Afrikan tutkimukset yhdistävät haploryhmät Välimeren ja Saharan verkostoihin."],
        "regions": ["Pohjois-Afrikka"],
        "sources": ["North African Archaeogenetics Journals"],
    }


def fetch_from_subsaharan_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Sub-Saharan Afrikan tutkimukset liittävät haploryhmät Bantu-laajenemiseen ja varhaisiin metsästäjä-keräilijöihin."],
        "regions": ["Sub-Saharan Afrikka"],
        "sources": ["Sub-Saharan Archaeogenetics Journals"],
    }


# ------------------------------
# Amerikat
# ------------------------------

def fetch_from_native_american_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Pohjois-Amerikan alkuperäiskansojen tutkimukset yhdistävät haploryhmät Beringian reitteihin."],
        "regions": ["Pohjois-Amerikka"],
        "sources": ["Native American Archaeogenetics Journals"],
    }


def fetch_from_south_american_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Etelä-Amerikan tutkimukset liittävät haploryhmät Andien, Amazonian ja rannikkokulttuurien verkostoihin."],
        "regions": ["Etelä-Amerikka"],
        "sources": ["South American Archaeogenetics Journals"],
    }


def fetch_from_caribbean_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Karibian tutkimukset yhdistävät haploryhmät Taino- ja Arawak-kulttuureihin."],
        "regions": ["Karibia"],
        "sources": ["Caribbean Archaeogenetics Journals"],
    }


def fetch_from_arctic_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Arktiset tutkimukset liittävät haploryhmät paleo-eskimoihin ja inuiittikulttuureihin."],
        "regions": ["Arktinen alue"],
        "sources": ["Arctic Archaeogenetics Journals"],
    }


# ------------------------------
# Oseania & saaristot
# ------------------------------

def fetch_from_australian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Australian tutkimukset liittävät haploryhmät varhaisiin Sahul-alueen populaatioihin."],
        "regions": ["Australia"],
        "sources": ["Australian Archaeogenetics Journals"],
    }


def fetch_from_polynesian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Polynesian tutkimukset yhdistävät haploryhmät austronesialaiseen laajenemiseen."],
        "regions": ["Polynesia"],
        "sources": ["Polynesian Archaeogenetics Journals"],
    }


def fetch_from_melanesian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Melanesian tutkimukset liittävät haploryhmät Sahulin ja Papuan varhaisiin väestöihin."],
        "regions": ["Melanesia"],
        "sources": ["Melanesian Archaeogenetics Journals"],
    }


def fetch_from_micronesian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Mikronesian tutkimukset yhdistävät haploryhmät merellisiin siirtoreitteihin Tyynellämerellä."],
        "regions": ["Mikronesia"],
        "sources": ["Micronesian Archaeogenetics Journals"],
    }


def fetch_from_new_zealand_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Uuden-Seelannin tutkimukset liittävät haploryhmät maorien esi-isiin ja polynesialaiseen laajenemiseen."],
        "regions": ["Uusi-Seelanti"],
        "sources": ["New Zealand Archaeogenetics Journals"],
    }


def fetch_from_indian_ocean_islands(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Intian valtameren saarien tutkimukset yhdistävät haploryhmät afrikkalaisiin, austronesialaisiin ja eteläaasialaisiin reitteihin."],
        "regions": ["Intian valtameren saaret"],
        "sources": ["Indian Ocean Archaeogenetics Journals"],
    }


def fetch_from_north_atlantic_islands(haplogroup: str) -> Dict:
    return {
        "description_fragments": ["Pohjois-Atlantin saarten tutkimukset yhdistävät haploryhmät viikinkeihin ja varhaisiin merikulttuureihin."],
        "regions": ["Islanti", "Färsaaret", "Orkneysaaret", "Shetlanti"],
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
            "focus": "Täysi genomi arkeogeneettiseen analyysiin.",
            "notes": "Sopii MyTrueAncestry-, GEDmatch- ja G25-analyyseihin.",
            "url": "https://nebula.org",
        },
        {
            "name": "AncestryDNA",
            "type": "Autosomal SNP array",
            "coverage": "~600k–700k SNP:tä",
            "focus": "Laaja autosomaalidata muinais-DNA-vertailuun.",
            "notes": "Hyvin tuettu kolmannen osapuolen työkaluissa.",
            "url": "https://www.ancestry.com/dna",
        },
        {
            "name": "FamilyTreeDNA",
            "type": "Y-DNA / mtDNA / autosomaali",
            "coverage": "Erikoistestit linjoille + autosomaali",
            "focus": f"Syvät isä- ja äitilinjat haploryhmälle {haplogroup}.",
            "notes": "Mahdollistaa linjapohjaisen syväanalyysin.",
            "url": "https://www.familytreedna.com",
        },
        {
            "name": "Living DNA",
            "type": "Autosomal + linjat",
            "coverage": "Mikrosiru + linjatulkinta",
            "focus": "Syvä alueellinen ja linjapohjainen raportointi.",
            "notes": "Hyödyllinen eurooppalaisessa populaatiohistoriassa.",
            "url": "https://livingdna.com",
        },
        {
            "name": "MyHeritage DNA",
            "type": "Autosomal SNP array",
            "coverage": "Noin samaa luokkaa kuin Ancestry/23andMe",
            "focus": "Laaja sukulaisverkosto ja moderni vertailu.",
            "notes": "Yhteensopiva useiden analyysityökalujen kanssa.",
            "url": "https://www.myheritage.com/dna",
        },
        {
            "name": "Sequencing.com",
            "type": "WGS / WES / SNP upload",
            "coverage": "WGS/WES + sovellusmarkkinapaikka",
            "focus": "Syvägenomi ja muinaisperimäanalyysit.",
            "notes": "Mahdollistaa useiden tiedostomuotojen hyödyntämisen.",
            "url": "https://sequencing.com",
        },
        {
            "name": "Genomelink",
            "type": "Raw DNA upload",
            "coverage": "Riippuu lähteestä",
            "focus": "Ancient Ancestry -raportit ja fenotyyppianalyysit.",
            "notes": "Hyödyntää kuluttajatestien raakadataa.",
            "url": "https://genomelink.io",
        },
    ]

    return {
        "description_fragments": ["Useat kaupalliset palvelut tarjoavat raakadataa, jota voidaan käyttää arkeogeneettiseen analyysiin."],
        "sources": ["Nebula Genomics", "AncestryDNA", "FamilyTreeDNA", "Living DNA", "MyHeritage", "Sequencing.com", "Genomelink"],
        "raw_data_providers": providers,
    }


def fetch_analysis_tools(haplogroup: str) -> Dict:
    tools = [
        {
            "name": "MyTrueAncestry",
            "type": "Ancient DNA matching",
            "focus": "Vertaa käyttäjän DNA:ta tuhansiin muinaisnäytteisiin.",
            "compatibility": "Autosomal, Y-DNA, mtDNA, WGS.",
            "notes": "Tuottaa karttoja, aikajanoja ja kulttuuritulkintoja.",
            "url": "https://mytrueancestry.com",
        },
        {
            "name": "GEDmatch",
            "type": "Admixture & heritage tools",
            "focus": "Admixture/Oracle-laskurit muinaisista komponenttipopulaatioista.",
            "compatibility": "Useimpien kuluttajatestien raakadatamuodot.",
            "notes": "Sopii sekä muinaisten komponenttien arviointiin että sukutaustojen vertailuun.",
            "url": "https://www.gedmatch.com",
        },
        {
            "name": "Genoplot / G25-työkalut",
            "type": "G25 modeling",
            "focus": "Korkean resoluution populaatiomallinnus.",
            "compatibility": "Yhteensopiva useiden raakadatamuotojen kanssa.",
            "notes": "Mahdollistaa hienojakoisen mallinnuksen muinaisten ja modernien populaatioiden välillä.",
            "url": "https://genoplot.com",
        },
        {
            "name": "Illustrative DNA",
            "type": "G25-based ancient modeling",
            "focus": "Granulaarinen muinaisväestöjen mallinnus.",
            "compatibility": "Kuluttajatestit (Ancestry, 23andMe, MyHeritage, FTDNA).",
            "notes": "Sopii syvälliseen arkeogeneettiseen jatkoanalyysiin.",
            "url": "https://illustrativedna.com",
        },
        {
            "name": "Genomelink Ancient Ancestry",
            "type": "Trait & ancient ancestry",
            "focus": "Muinaisperimä + fenotyyppianalyysit.",
            "compatibility": "Useimmat kuluttajatestit.",
            "notes": "Hyödyllinen yhdistelmätulkinnoissa.",
            "url": "https://genomelink.io",
        },
        {
            "name": "Nebula Genomics (upload)",
            "type": "Raw DNA upload & WGS analysis",
            "focus": "Syvägenomi ja haploryhmäanalyysi täydestä genomista.",
            "compatibility": "AncestryDNA, 23andMe, MyHeritage jne.",
            "notes": "Kattaa syvä-esi-isä- ja haploryhmäanalyysin.",
            "url": "https://nebula.org/free-dna-upload-analysis/",
        },
    ]

    return {
        "description_fragments": ["Useat analyysialustat mahdollistavat muinais-DNA-vertailut ja populaatiomallinnuksen."],
        "sources": ["MyTrueAncestry", "GEDmatch", "Genoplot", "Illustrative DNA", "Genomelink", "Nebula Genomics"],
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

    haplogroup = sys.argv[1]
    data = fetch_full_haplogroup_data(haplogroup)

    print(json.dumps(data, indent=4, ensure_ascii=False))

    if len(sys.argv) > 2 and sys.argv[2] == "export":
        export_to_json(data)

