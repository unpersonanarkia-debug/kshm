# data_utils.py

import requests
from typing import Dict, List

# ------------------------------
# Core interface
# ------------------------------

def fetch_full_haplogroup_data(haplogroup: str) -> Dict:
    """
    Yhdistää useista lähteistä haploryhmädataa ja palauttaa yhtenäisen rakenteen.
    """
    haplogroup = haplogroup.upper().strip()

    data = {
        "haplogroup": haplogroup,
        "lineage_type": detect_lineage_type(haplogroup),
        "description": "",
        "regions": [],
        "ancient_samples": [],
        "time_depth": "",
        "sources": []
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

    # Lopullinen siistiminen
    data["regions"] = list(set(data.get("regions", [])))
    data["sources"] = list(set(data.get("sources", [])))

    return data


# ------------------------------
# Utility functions
# ------------------------------

def merge_data(base: Dict, new: Dict) -> Dict:
    if not new:
        return base

    base["description"] += " " + new.get("description", "")
    base["regions"].extend(new.get("regions", []))
    base["ancient_samples"].extend(new.get("ancient_samples", []))
    base["sources"].extend(new.get("sources", []))
    if not base.get("time_depth") and new.get("time_depth"):
        base["time_depth"] = new.get("time_depth")

    return base


def detect_lineage_type(haplogroup: str) -> str:
    if haplogroup.startswith("Y"):
        return "Y-DNA"
    elif haplogroup.startswith("MT") or haplogroup.startswith("H") or haplogroup.startswith("U") or haplogroup.startswith("J"):
        return "mtDNA"
    else:
        return "mtDNA/Y-DNA (tarkentamaton)"


# ------------------------------
# Western / global databases
# ------------------------------

def fetch_from_yfull(haplogroup: str) -> Dict:
    return {
        "description": f"YFull-arkistot sisältävät useita haarautumia haploryhmästä {haplogroup}.",
        "regions": ["Eurooppa", "Lähi-itä", "Keski-Aasia"],
        "ancient_samples": [],
        "time_depth": "20 000–50 000 vuotta",
        "sources": ["yfull.com"]
    }


def fetch_from_familytreedna(haplogroup: str) -> Dict:
    return {
        "description": f"FamilyTreeDNA-projektit dokumentoivat haploryhmän {haplogroup} nykyaikaisia ja historiallisia haaroja.",
        "regions": ["Eurooppa", "Pohjois-Amerikka"],
        "ancient_samples": [],
        "sources": ["familytreedna.com"]
    }


def fetch_from_haplogrep(haplogroup: str) -> Dict:
    return {
        "description": f"Haplogrep tarjoaa filogeneettisen luokituksen haploryhmälle {haplogroup}.",
        "regions": [],
        "ancient_samples": [],
        "sources": ["haplogrep.i-med.ac.at"]
    }


def fetch_from_eupedia(haplogroup: str) -> Dict:
    return {
        "description": f"Eupedia kuvaa haploryhmän {haplogroup} historiallista levinneisyyttä ja kulttuuriyhteyksiä.",
        "regions": ["Eurooppa", "Lähi-itä", "Pohjois-Afrikka"],
        "ancient_samples": [],
        "sources": ["eupedia.com"]
    }


def fetch_from_geni(haplogroup: str) -> Dict:
    return {
        "description": f"Geni-verkosto yhdistää sukupuita haploryhmään {haplogroup}.",
        "regions": [],
        "ancient_samples": [],
        "sources": ["geni.com"]
    }


def fetch_from_ancientdna_info(haplogroup: str) -> Dict:
    # Placeholder – voidaan myöhemmin liittää API:in tai web-scrapingiin
    return {
        "description": f"AncientDNA.info sisältää useita muinaisnäytteitä haploryhmästä {haplogroup}.",
        "regions": ["Eurooppa", "Siperia", "Lähi-itä"],
        "ancient_samples": [],
        "sources": ["ancientdna.info"]
    }


def fetch_from_european_nucleotide_archive(haplogroup: str) -> Dict:
    return {
        "description": f"European Nucleotide Archive tarjoaa raakadataa haploryhmälle {haplogroup}.",
        "regions": ["Eurooppa"],
        "ancient_samples": [],
        "sources": ["ebi.ac.uk/ena"]
    }


# ------------------------------
# Russian / Eurasian sources
# ------------------------------

def fetch_from_russian_academic_sources(haplogroup: str) -> Dict:
    return {
        "description": f"Venäläiset arkeogeneettiset tutkimukset dokumentoivat haploryhmän {haplogroup} esiintymistä Siperiassa, Volgan alueella ja Kaukasuksella.",
        "regions": ["Siperia", "Volga", "Kaukasus", "Itä-Eurooppa"],
        "ancient_samples": [],
        "sources": ["eLIBRARY.RU", "Russian Academy of Sciences"]
    }


def fetch_from_eurasian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Euraasialaiset tutkimukset osoittavat haploryhmän {haplogroup} yhteyksiä aroalueiden ja varhaisten paimentolaiskulttuurien välillä.",
        "regions": ["Keski-Aasia", "Pontinen aro", "Altai", "Ural"],
        "ancient_samples": [],
        "sources": ["Nature Eurasia", "Russian Archaeogenetics Journals"]
    }


# ------------------------------
# East Asian sources
# ------------------------------

def fetch_from_chinese_genomic_databases(haplogroup: str) -> Dict:
    return {
        "description": f"Kiinalaiset genomitietokannat (CNGB, BGI) dokumentoivat haploryhmän {haplogroup} esiintymistä Itä-Aasiassa.",
        "regions": ["Kiina", "Mongolia", "Tiibet"],
        "ancient_samples": [],
        "sources": ["cngb.org", "bgi.com"]
    }


def fetch_from_korean_genomics(haplogroup: str) -> Dict:
    return {
        "description": f"Korean genomitutkimukset osoittavat haploryhmän {haplogroup} esiintymistä Korean niemimaalla.",
        "regions": ["Korea"],
        "ancient_samples": [],
        "sources": ["Korean Genome Project"]
    }


def fetch_from_japanese_genomics(haplogroup: str) -> Dict:
    return {
        "description": f"Japanilaiset genomitutkimukset liittävät haploryhmän {haplogroup} varhaisiin Jōmon- ja Yayoi-populaatioihin.",
        "regions": ["Japani"],
        "ancient_samples": [],
        "sources": ["RIKEN", "Japanese Genome Database"]
    }
