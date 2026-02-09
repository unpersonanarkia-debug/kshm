# data_utils.py

import requests
from typing import Dict, List


# ------------------------------
# Core interface
# ------------------------------

def fetch_full_haplogroup_data(haplogroup: str) -> Dict:
    """
    Yhdistää useista lähteistä haploryhmädataa ja palauttaa yhtenäisen rakenteen.
    Lisäksi liittää globaalin archeogenetiikan raakadata- ja analyysiverkoston.
    """
    haplogroup = haplogroup.upper().strip()

    data: Dict = {
        "haplogroup": haplogroup,
        "lineage_type": detect_lineage_type(haplogroup),
        "description": "",
        "regions": [],
        "ancient_samples": [],
        "time_depth": "",
        "sources": [],
        "raw_data_providers": [],
        "analysis_tools": [],
    }

    # Länsimaiset lähteet
    data = merge_data(data, fetch_from_yfull(haplogroup))
    data = merge_data(data, fetch_from_familytreedna(haplogroup))
    data = merge_data(data, fetch_from_haplogrep(haplogroup))
    data = merge_data(data, fetch_from_eupedia(haplogroup))
    data = merge_data(data, fetch_from_geni(haplogroup))

    # Arkeogeneettiset tietokannat
    data = merge_data(data, fetch_from_ancientdna_info(haplogroup))
    data = merge_data(data, fetch_from_european_nucleotide_archive(haplogroup))

    # Venäläiset ja Euraasian lähteet
    data = merge_data(data, fetch_from_russian_academic_sources(haplogroup))
    data = merge_data(data, fetch_from_eurasian_archaeogenetics(haplogroup))

    # Kiinalaiset ja Itä-Aasian lähteet
    data = merge_data(data, fetch_from_chinese_genomic_databases(haplogroup))
    data = merge_data(data, fetch_from_korean_genomics(haplogroup))
    data = merge_data(data, fetch_from_japanese_genomics(haplogroup))

    # Globaalit kaupalliset raakadata-lähteet
    data = merge_data(data, fetch_raw_data_providers(haplogroup))

    # Globaalit analyysityökalut
    data = merge_data(data, fetch_analysis_tools(haplogroup))

    # Lopullinen siistiminen
    data["regions"] = sorted(set(data.get("regions", [])))
    data["sources"] = sorted(set(data.get("sources", [])))
    data["raw_data_providers"] = unique_by_key(data.get("raw_data_providers", []), "name")
    data["analysis_tools"] = unique_by_key(data.get("analysis_tools", []), "name")

    return data


# ------------------------------
# Utility functions
# ------------------------------

def merge_data(base: Dict, new: Dict) -> Dict:
    if not new:
        return base

    base["description"] += " " + new.get("description", "")

    base.setdefault("regions", []).extend(new.get("regions", []))
    base.setdefault("ancient_samples", []).extend(new.get("ancient_samples", []))
    base.setdefault("sources", []).extend(new.get("sources", []))

    base.setdefault("raw_data_providers", []).extend(new.get("raw_data_providers", []))
    base.setdefault("analysis_tools", []).extend(new.get("analysis_tools", []))

    if not base.get("time_depth") and new.get("time_depth"):
        base["time_depth"] = new.get("time_depth")

    return base


def detect_lineage_type(haplogroup: str) -> str:
    if haplogroup.startswith("Y"):
        return "Y-DNA"
    elif haplogroup.startswith(("MT", "H", "U", "J", "K", "T", "W", "I", "X", "V")):
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


# ------------------------------
# Western / global databases
# ------------------------------

def fetch_from_yfull(haplogroup: str) -> Dict:
    return {
        "description": f"YFull-arkistot sisältävät useita haarautumia haploryhmästä {haplogroup} ja kalibroituja fylogeneettisiä puita erityisesti Y-DNA- ja mtDNA-linjoille.",
        "regions": ["Eurooppa", "Lähi-itä", "Keski-Aasia"],
        "ancient_samples": [],
        "time_depth": "20 000–50 000 vuotta",
        "sources": ["yfull.com"],
    }


def fetch_from_familytreedna(haplogroup: str) -> Dict:
    return {
        "description": f"FamilyTreeDNA-projektit dokumentoivat haploryhmän {haplogroup} nykyaikaisia ja historiallisia haaroja (Y-DNA, mtDNA, autosomaali).",
        "regions": ["Eurooppa", "Pohjois-Amerikka"],
        "ancient_samples": [],
        "sources": ["familytreedna.com"],
    }


def fetch_from_haplogrep(haplogroup: str) -> Dict:
    return {
        "description": f"Haplogrep tarjoaa filogeneettisen luokituksen ja todennäköisyyspohjaisen haploryhmäarvion haploryhmälle {haplogroup}.",
        "regions": [],
        "ancient_samples": [],
        "sources": ["haplogrep.i-med.ac.at"],
    }


def fetch_from_eupedia(haplogroup: str) -> Dict:
    return {
        "description": f"Eupedia kuvaa haploryhmän {haplogroup} historiallista levinneisyyttä, kulttuuriyhteyksiä ja modernia frekvenssijakaumaa.",
        "regions": ["Eurooppa", "Lähi-itä", "Pohjois-Afrikka"],
        "ancient_samples": [],
        "sources": ["eupedia.com"],
    }


def fetch_from_geni(haplogroup: str) -> Dict:
    return {
        "description": f"Geni-verkosto yhdistää sukupuita haploryhmään {haplogroup} ja mahdollistaa sukujen linjojen visuaalisen tarkastelun.",
        "regions": [],
        "ancient_samples": [],
        "sources": ["geni.com"],
    }


def fetch_from_ancientdna_info(haplogroup: str) -> Dict:
    return {
        "description": f"AncientDNA- ja muut arkeogenetiikkatietokannat sisältävät muinaisnäytteitä haploryhmästä {haplogroup}, joita voidaan verrata moderniin DNA:han.",
        "regions": ["Eurooppa", "Siperia", "Lähi-itä"],
        "ancient_samples": [],
        "sources": ["ancientdna.info"],
    }


def fetch_from_european_nucleotide_archive(haplogroup: str) -> Dict:
    return {
        "description": f"European Nucleotide Archive tarjoaa raakadataa (BAM/VCF) muinaisille ja moderneille näytteille, joista haploryhmä {haplogroup} voidaan rekonstruoida.",
        "regions": ["Eurooppa"],
        "ancient_samples": [],
        "sources": ["ebi.ac.uk/ena"],
    }


# ------------------------------
# Russian / Eurasian sources
# ------------------------------

def fetch_from_russian_academic_sources(haplogroup: str) -> Dict:
    return {
        "description": f"Venäläiset arkeogeneettiset tutkimukset dokumentoivat haploryhmän {haplogroup} esiintymistä Siperiassa, Volgan alueella ja Kaukasuksella.",
        "regions": ["Siperia", "Volga", "Kaukasus", "Itä-Eurooppa"],
        "ancient_samples": [],
        "sources": ["eLIBRARY.RU", "Russian Academy of Sciences"],
    }


def fetch_from_eurasian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Euraasialaiset tutkimukset osoittavat haploryhmän {haplogroup} yhteyksiä aroalueiden ja varhaisten paimentolaiskulttuurien välillä.",
        "regions": ["Keski-Aasia", "Pontinen aro", "Altai", "Ural"],
        "ancient_samples": [],
        "sources": ["Nature Eurasia", "Russian Archaeogenetics Journals"],
    }


# ------------------------------
# East Asian sources
# ------------------------------

def fetch_from_chinese_genomic_databases(haplogroup: str) -> Dict:
    return {
        "description": f"Kiinalaiset genomitietokannat (CNGB, BGI) dokumentoivat haploryhmän {haplogroup} esiintymistä Itä- ja Keski-Aasiassa.",
        "regions": ["Kiina", "Mongolia", "Tiibet"],
        "ancient_samples": [],
        "sources": ["cngb.org", "bgi.com"],
    }


def fetch_from_korean_genomics(haplogroup: str) -> Dict:
    return {
        "description": f"Korean genomitutkimukset osoittavat haploryhmän {haplogroup} esiintymistä Korean niemimaalla ja lähialueilla.",
        "regions": ["Korea"],
        "ancient_samples": [],
        "sources": ["Korean Genome Project"],
    }


def fetch_from_japanese_genomics(haplogroup: str) -> Dict:
    return {
        "description": f"Japanilaiset genomitutkimukset liittävät haploryhmän {haplogroup} varhaisiin Jōmon- ja Yayoi-populaatioihin.",
        "regions": ["Japani"],
        "ancient_samples": [],
        "sources": ["RIKEN", "Japanese Genome Database"],
    }


# ------------------------------
# Global raw-data providers
# ------------------------------

def fetch_raw_data_providers(haplogroup: str) -> Dict:
    providers = [
        {
            "name": "Nebula Genomics",
            "type": "WGS",
            "coverage": "30x–100x koko genomi",
            "focus": "Syvä arkeogeneettinen analyysi, kaikki SNP:t, Y-DNA ja mtDNA.",
            "notes": "Kultainen standardi arkeogenetiikkaan; yhteensopiva MyTrueAncestryn, GEDmatchin ja G25-analyysien kanssa.",
            "url": "https://nebula.org",
        },
        {
            "name": "AncestryDNA",
            "type": "Autosomal SNP array",
            "coverage": "~600k–700k SNP:tä",
            "focus": "Laaja autosomaalidata muinais-DNA-vertailuihin.",
            "notes": "Hyvin tuettu MyTrueAncestryssa, GEDmatchissa ja Genomelinkissä.",
            "url": "https://www.ancestry.com/dna",
        },
        {
            "name": "FamilyTreeDNA",
            "type": "Y-DNA / mtDNA / autosomaali",
            "coverage": "Erikoistestit Y- ja mtDNA-linjoille",
            "focus": f"Syvät isä- ja äitilinjat, haploryhmä {haplogroup} tarkentuu huomattavasti.",
            "notes": "Tarjoaa BAM/FASTA-tyylisiä tiedostoja jatkoanalyysiin.",
            "url": "https://www.familytreedna.com",
        },
        {
            "name": "Living DNA",
            "type": "Autosomal + Y-DNA/mtDNA",
            "coverage": "Mikrosiru + linjatulkinta",
            "focus": "Hyvä eurooppalaisen ja brittiläisen populaatiohistorian tarkasteluun.",
            "notes": "Hyödyllinen alueellisiin vertailuihin.",
            "url": "https://livingdna.com",
        },
        {
            "name": "MyHeritage DNA",
            "type": "Autosomal SNP array",
            "coverage": "Saman luokan kattavuus kuin Ancestry/23andMe",
            "focus": "Laaja kansainvälinen sukulaisverkosto.",
            "notes": "Yhteensopiva MyTrueAncestryn ja Genomelinkin kanssa.",
            "url": "https://www.myheritage.com/dna",
        },
        {
            "name": "Sequencing.com",
            "type": "WGS / WES / SNP upload",
            "coverage": "WGS/WES + sovellusmarkkinapaikka",
            "focus": "Mahdollistaa raakadatapohjaiset muinais-DNA-analyysit.",
            "notes": "Tukee VCF- ja BAM-muotoja.",
            "url": "https://sequencing.com",
        },
        {
            "name": "Genomelink",
            "type": "Raw DNA upload",
            "coverage": "Riippuu lähdetestistä",
            "focus": "Ancient Ancestry -raportit ja populaatiovertailut.",
            "notes": "Hyödyntää Ancestry/23andMe/MyHeritage/FTDNA-datat.",
            "url": "https://genomelink.io",
        },
    ]

    return {
        "description": (
            "Arkeogeneettisesti paras raakadata saadaan korkean tiheyden SNP-paneeleista "
            "tai koko genomin sekvensoinnista (WGS), joita voidaan käyttää kolmansien osapuolten työkaluissa."
        ),
        "regions": [],
        "ancient_samples": [],
        "sources": [p["name"] for p in providers],
        "raw_data_providers": providers,
    }


# ------------------------------
# Global analysis tools
# ------------------------------

def fetch_analysis_tools(haplogroup: str) -> Dict:
    tools = [
        {
            "name": "MyTrueAncestry",
            "type": "Ancient DNA matching",
            "focus": "Vertaa käyttäjän DNA:ta tuhansiin muinaisnäytteisiin (esim. viikingit, roomalaiset, asteekit).",
            "compatibility": "Hyväksyy autosomaali-, Y-DNA-, mtDNA- ja WGS-datan.",
            "notes": "Tuottaa karttoja, aikajanoja ja kulttuuritason tulkintoja.",
            "url": "https://mytrueancestry.com",
        },
        {
            "name": "GEDmatch",
            "type": "Admixture & heritage tools",
            "focus": "Admixture- ja Oracle-laskurit muinaisista populaatioista.",
            "compatibility": "Hyväksyy useimpien kuluttajatestien raakadatamuodot.",
            "notes": "Sopii komponenttien arviointiin ja sukutaustojen vertailuun.",
            "url": "https://www.gedmatch.com",
        },
        {
            "name": "Genoplot / G25-työkalut",
            "type": "G25 modeling",
            "focus": "Korkean resoluution populaatiomallinnus (G25).",
            "compatibility": "Yhteensopiva useiden raakadatamuotojen kanssa.",
            "notes": "Mahdollistaa hienojakoisen muinaisten ja modernien populaatioiden vertailun.",
            "url": "https://genoplot.com",
        },
        {
            "name": "Illustrative DNA",
            "type": "G25-based ancient modeling",
            "focus": "Granulaarinen muinaisväestöjen mallinnus (G25).",
            "compatibility": "Yhteensopiva keskeisten kuluttajatestien kanssa.",
            "notes": "Hyvä jatkoanalytiikkaan GEDmatchin ja MyTrueAncestryn rinnalle.",
            "url": "https://illustrativedna.com",
        },
        {
            "name": "Genomelink Ancient Ancestry",
            "type": "Trait & ancient ancestry",
            "focus": "Ancient Ancestry -raportit osana laajempaa fenotyyppipalvelua.",
            "compatibility": "Hyväksyy AncestryDNA, 23andMe, MyHeritage ja FTDNA-datat.",
            "notes": "Tarjoaa muinaisperimän lisäksi muita raportteja.",
            "url": "https://genomelink.io",
        },
        {
            "name": "Nebula Genomics (upload)",
            "type": "Raw DNA upload & WGS analysis",
            "focus": "Mahdollistaa syvän analyysin omasta tai ladatusta genomidatasta.",
            "compatibility": "Hyväksyy mm. AncestryDNA:n ja 23andMe:n datan.",
            "notes": "Kattaa syvä-esi-isä- ja haploryhmäanalyysin täydestä genomista.",
            "url": "https://nebula.org/free-dna-upload-analysis/",
        },
    ]

    return {
        "description": (
            "Useiden kolmannen osapuolen analyysialustojen avulla raakadata voidaan liittää muinais-DNA-"
            "viitepopulaatioihin, komponenttianalyyseihin ja G25-mallinnukseen."
        ),
        "regions": [],
        "ancient_samples": [],
        "sources": [t["name"] for t in tools],
        "analysis_tools": tools,
    }
