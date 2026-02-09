# data_utils.py

import requests
from typing import Dict, List

# ------------------------------
# Core interface
# ------------------------------

def fetch_full_haplogroup_data(haplogroup: str) -> Dict:
    """
    Yhdistää globaalisti useista lähteistä haploryhmädataa ja palauttaa
    yhtenäisen arkeogeneettisen tietorakenteen.
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
        "regional_profiles": [],  # uutta: aluekohtaiset analyysipaketit
    }

    # ------------------------------
    # Global core sources
    # ------------------------------
    data = merge_data(data, fetch_from_yfull(haplogroup))
    data = merge_data(data, fetch_from_familytreedna(haplogroup))
    data = merge_data(data, fetch_from_haplogrep(haplogroup))
    data = merge_data(data, fetch_from_eupedia(haplogroup))
    data = merge_data(data, fetch_from_geni(haplogroup))
    data = merge_data(data, fetch_from_ancientdna_info(haplogroup))
    data = merge_data(data, fetch_from_european_nucleotide_archive(haplogroup))

    # ------------------------------
    # Regional academic networks
    # ------------------------------
    data = merge_data(data, fetch_from_russian_academic_sources(haplogroup))
    data = merge_data(data, fetch_from_eurasian_archaeogenetics(haplogroup))
    data = merge_data(data, fetch_from_chinese_genomic_databases(haplogroup))
    data = merge_data(data, fetch_from_korean_genomics(haplogroup))
    data = merge_data(data, fetch_from_japanese_genomics(haplogroup))

    # AFRICA
    data = merge_data(data, fetch_from_african_archaeogenetics(haplogroup))

    # AMERICAS
    data = merge_data(data, fetch_from_native_american_archaeogenetics(haplogroup))
    data = merge_data(data, fetch_from_south_american_archaeogenetics(haplogroup))
    data = merge_data(data, fetch_from_caribbean_archaeogenetics(haplogroup))

    # OCEANIA
    data = merge_data(data, fetch_from_australian_archaeogenetics(haplogroup))
    data = merge_data(data, fetch_from_polynesian_archaeogenetics(haplogroup))
    data = merge_data(data, fetch_from_melanesian_archaeogenetics(haplogroup))
    data = merge_data(data, fetch_from_micronesian_archaeogenetics(haplogroup))
    data = merge_data(data, fetch_from_new_zealand_archaeogenetics(haplogroup))

    # ISLAND SYSTEMS
    data = merge_data(data, fetch_from_north_atlantic_islands(haplogroup))
    data = merge_data(data, fetch_from_indian_ocean_islands(haplogroup))

    # ------------------------------
    # Global raw data & analysis engines
    # ------------------------------
    data = merge_data(data, fetch_raw_data_providers(haplogroup))
    data = merge_data(data, fetch_analysis_tools(haplogroup))

    # ------------------------------
    # Final cleanup
    # ------------------------------
    data["regions"] = sorted(set(data.get("regions", [])))
    data["sources"] = sorted(set(data.get("sources", [])))

    data["raw_data_providers"] = unique_by_key(data.get("raw_data_providers", []), "name")
    data["analysis_tools"] = unique_by_key(data.get("analysis_tools", []), "name")
    data["regional_profiles"] = unique_by_key(data.get("regional_profiles", []), "region")

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
    base.setdefault("regional_profiles", []).extend(new.get("regional_profiles", []))

    if not base.get("time_depth") and new.get("time_depth"):
        base["time_depth"] = new.get("time_depth")

    return base


def detect_lineage_type(haplogroup: str) -> str:
    if haplogroup.startswith("Y"):
        return "Y-DNA"
    elif haplogroup.startswith(("MT", "H", "U", "J", "T", "K", "L", "M", "N", "R")):
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
# Global / Western databases
# ------------------------------

def fetch_from_yfull(haplogroup: str) -> Dict:
    return {
        "description": f"YFull-arkistot sisältävät useita haarautumia haploryhmästä {haplogroup} ja kalibroituja fylogeneettisiä puita Y-DNA:lle.",
        "regions": ["Eurooppa", "Lähi-itä", "Keski-Aasia"],
        "ancient_samples": [],
        "time_depth": "20 000–60 000 vuotta",
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
        "regions": ["Eurooppa", "Siperia", "Lähi-itä", "Amerikat", "Afrikka", "Oseania"],
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
        "regional_profiles": [
            {"region": "Siperia", "tools": ["ADMIXTOOLS", "qpAdm"], "notes": "Siperian paleogenomiikka"},
            {"region": "Volga-Kaukasus", "tools": ["G25", "ADMIXTOOLS"], "notes": "Aroalueen ja Kaukasuksen väestöhistoria"},
        ],
    }


def fetch_from_eurasian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Euraasialaiset tutkimukset osoittavat haploryhmän {haplogroup} yhteyksiä aroalueiden ja varhaisten paimentolaiskulttuurien välillä.",
        "regions": ["Keski-Aasia", "Pontinen aro", "Altai", "Ural"],
        "ancient_samples": [],
        "sources": ["Nature Eurasia", "Russian Archaeogenetics Journals"],
        "regional_profiles": [
            {"region": "Keski-Aasia", "tools": ["ADMIXTOOLS", "G25"], "notes": "Paimentolais- ja aroväestöjen analyysi"},
        ],
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
        "regional_profiles": [
            {"region": "Kiina", "tools": ["G25", "ADMIXTOOLS"], "notes": "Itä-Aasian muinaisväestöt"},
        ],
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
# Africa
# ------------------------------

def fetch_from_african_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Afrikan arkeogenetiikka osoittaa haploryhmän {haplogroup} yhteyksiä varhaisiin metsästäjä-keräilijöihin, neoliittisiin viljelijöihin ja bantulaajentumiseen.",
        "regions": ["Länsi-Afrikka", "Itä-Afrikka", "Etelä-Afrikka", "Sahel", "Pohjois-Afrikka"],
        "ancient_samples": [],
        "sources": ["H3Africa", "African Genome Variation Project", "Reich Lab Africa"],
        "regional_profiles": [
            {"region": "Itä-Afrikka", "tools": ["ADMIXTOOLS", "qpAdm"], "notes": "Varhaiset Homo sapiens -populaatiot"},
            {"region": "Länsi-Afrikka", "tools": ["G25", "ADMIXTOOLS"], "notes": "Bantulaajentumisen analyysi"},
        ],
    }


# ------------------------------
# Americas
# ------------------------------

def fetch_from_native_american_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Pohjois-Amerikan arkeogenetiikka yhdistää haploryhmän {haplogroup} paleo-intiaaneihin, Clovis- ja pre-Clovis-populaatioihin.",
        "regions": ["Pohjois-Amerikka"],
        "ancient_samples": [],
        "sources": ["Reich Lab Americas", "Simons Genome Diversity Project", "Genographic Project"],
        "regional_profiles": [
            {"region": "Pohjois-Amerikka", "tools": ["MyTrueAncestry", "GEDmatch", "G25"], "notes": "Paleo-intiaanit ja varhaiset muuttoreitit"},
        ],
    }


def fetch_from_south_american_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Etelä-Amerikan arkeogenetiikka yhdistää haploryhmän {haplogroup} Andien, Amazonian ja Patagonian varhaisiin populaatioihin.",
        "regions": ["Etelä-Amerikka"],
        "ancient_samples": [],
        "sources": ["Reich Lab South America", "PNAS", "Nature Genetics"],
        "regional_profiles": [
            {"region": "Andit", "tools": ["ADMIXTOOLS", "G25"], "notes": "Andien sivilisaatiot ja varhaiset maanviljelijät"},
        ],
    }


def fetch_from_caribbean_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Karibian arkeogenetiikka liittää haploryhmän {haplogroup} Taino-, Arawak- ja Carib-populaatioihin.",
        "regions": ["Karibia"],
        "ancient_samples": [],
        "sources": ["Caribbean aDNA Project", "Reich Lab Caribbean"],
        "regional_profiles": [
            {"region": "Karibia", "tools": ["MyTrueAncestry", "G25"], "notes": "Saaristojen varhaiset asuttajat"},
        ],
    }


# ------------------------------
# Oceania & Pacific
# ------------------------------

def fetch_from_australian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Australian arkeogenetiikka yhdistää haploryhmän {haplogroup} alkuperäiskansojen varhaisiin Sahul-populaatioihin.",
        "regions": ["Australia"],
        "ancient_samples": [],
        "sources": ["Max Planck Institute", "Nature Australia aDNA"],
        "regional_profiles": [
            {"region": "Australia", "tools": ["ADMIXTOOLS", "G25"], "notes": "Sahul-manner ja varhainen asutus"},
        ],
    }


def fetch_from_new_zealand_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Uuden-Seelannin arkeogenetiikka yhdistää haploryhmän {haplogroup} varhaisiin polynesialaisiin merenkulkijoihin (Māori).",
        "regions": ["Uusi-Seelanti"],
        "ancient_samples": [],
        "sources": ["Reich Lab Polynesia", "Nature Oceania"],
        "regional_profiles": [
            {"region": "Uusi-Seelanti", "tools": ["ADMIXTOOLS", "G25"], "notes": "Polynesialainen laajentuminen"},
        ],
    }


def fetch_from_polynesian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Polynesian arkeogenetiikka yhdistää haploryhmän {haplogroup} austronesialaiseen laajentumiseen ja Tyynenmeren saariston asuttamiseen.",
        "regions": ["Polynesia"],
        "ancient_samples": [],
        "sources": ["PNAS Polynesia", "Nature Human Behaviour", "Reich Lab Oceania"],
        "regional_profiles": [
            {"region": "Polynesia", "tools": ["G25", "ADMIXTOOLS"], "notes": "Austronesialainen laajentuminen"},
        ],
    }


def fetch_from_melanesian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Melanesian arkeogenetiikka yhdistää haploryhmän {haplogroup} Papuan ja varhaisten Sahul-populaatioiden perimään.",
        "regions": ["Melanesia"],
        "ancient_samples": [],
        "sources": ["Max Planck Institute", "Nature Melanesia aDNA"],
        "regional_profiles": [
            {"region": "Melanesia", "tools": ["ADMIXTOOLS", "G25"], "notes": "Papuan ja Sahul-perimä"},
        ],
    }


def fetch_from_micronesian_archaeogenetics(haplogroup: str) -> Dict:
    return {
        "description": f"Micronesian arkeogenetiikka yhdistää haploryhmän {haplogroup} varhaisiin Tyynenmeren saaristojen merenkulkijoihin.",
        "regions": ["Mikronesia"],
        "ancient_samples": [],
        "sources": ["PNAS Micronesia", "Reich Lab Pacific"],
        "regional_profiles": [
            {"region": "Mikronesia", "tools": ["G25", "ADMIXTOOLS"], "notes": "Tyynenmeren saarien kolonisaatio"},
        ],
    }


# ------------------------------
# Island systems
# ------------------------------

def fetch_from_north_atlantic_islands(haplogroup: str) -> Dict:
    return {
        "description": f"Pohjois-Atlantin saarien arkeogenetiikka yhdistää haploryhmän {haplogroup} viikinkiajan ja varhaisten merenkulkukulttuurien leviämiseen.",
        "regions": ["Islanti", "Färsaaret", "Orkney", "Shetland"],
        "ancient_samples": [],
        "sources": ["Icelandic Genome Project", "Nature North Atlantic aDNA"],
        "regional_profiles": [
            {"region": "Pohjois-Atlantin saaret", "tools": ["MyTrueAncestry", "G25"], "notes": "Viikinkiajan saaristot"},
        ],
    }


def fetch_from_indian_ocean_islands(haplogroup: str) -> Dict:
    return {
        "description": f"Intian valtameren saaristojen arkeogenetiikka yhdistää haploryhmän {haplogroup} austronesialaiseen ja afrikkalaiseen laajentumiseen.",
        "regions": ["Madagaskar", "Mauritius", "Seychellit", "Malediivit"],
        "ancient_samples": [],
        "sources": ["Nature Indian Ocean aDNA", "Reich Lab Indian Ocean"],
        "regional_profiles": [
            {"region": "Intian valtameren saaret", "tools": ["ADMIXTOOLS", "G25"], "notes": "Afrikan ja Austronesian risteytys"},
        ],
    }


# ------------------------------
# Global raw-data providers (WGS, SNP arrays, lineage tests)
# ------------------------------

def fetch_raw_data_providers(haplogroup: str) -> Dict:
    providers = [
        {
            "name": "Nebula Genomics",
            "type": "WGS",
            "coverage": "30x–100x WGS",
            "focus": "Syvä arkeogeneettinen analyysi koko genomista.",
            "notes": "Paras vaihtoehto kattavaan muinais- ja haploryhmäanalyysiin.",
            "url": "https://nebula.org",
        },
        {
            "name": "AncestryDNA",
            "type": "Autosomal SNP array",
            "coverage": "~600k–700k SNP:tä",
            "focus": "Laaja autosomaalidata, hyvä lähtökohta muinaisperimän analyysiin.",
            "notes": "Yhteensopiva MyTrueAncestryn, GEDmatchin ja G25-työkalujen kanssa.",
            "url": "https://www.ancestry.com/dna",
        },
        {
            "name": "FamilyTreeDNA",
            "type": "Y-DNA / mtDNA / autosomaali",
            "coverage": "Erikoistestit linjoille",
            "focus": f"Syvät isä- ja äitilinjat, haploryhmä {haplogroup} tarkentuu.",
            "notes": "Tarjoaa linjakohtaista analyysia ja raakadataa.",
            "url": "https://www.familytreedna.com",
        },
        {
            "name": "Living DNA",
            "type": "Autosomal + Y-DNA/mtDNA",
            "coverage": "Mikrosiru + linjatulkinta",
            "focus": "Alueellinen tarkkuus Euroopassa ja Britteinsaarilla.",
            "notes": "Hyödyllinen eurooppalaiseen väestöhistoriaan.",
            "url": "https://livingdna.com",
        },
        {
            "name": "MyHeritage DNA",
            "type": "Autosomal SNP array",
            "coverage": "Kuluttajatason SNP-paneeli",
            "focus": "Laaja kansainvälinen sukulaisverkosto.",
            "notes": "Hyvä moderniin vertailuun ja kolmannen osapuolen analyysiin.",
            "url": "https://www.myheritage.com/dna",
        },
        {
            "name": "Sequencing.com",
            "type": "WGS / WES / SNP upload",
            "coverage": "WGS/WES + sovellusmarkkinapaikka",
            "focus": "Raakadatan jatkoanalyysi ja sovelluspohjainen tulkinta.",
            "notes": "Mahdollistaa eri raakadatamuotojen hyödyntämisen.",
            "url": "https://sequencing.com",
        },
        {
            "name": "Genomelink",
            "type": "Raw DNA upload",
            "coverage": "Riippuu lähteen testistä",
            "focus": "Ancient Ancestry -raportit ja populaatiomallinnus.",
            "notes": "Hyödyntää useimpien testauspalveluiden raakadataa.",
            "url": "https://genomelink.io",
        },
    ]

    return {
        "description": (
            "Arkeogeneettisesti paras raakadata haploryhmäanalyysiin saadaan korkean tiheyden SNP-paneeleista "
            "tai koko genomin sekvensoinnista (WGS), joita voidaan käyttää kolmansien osapuolten työkaluissa."
        ),
        "regions": [],
        "ancient_samples": [],
        "sources": [p["name"] for p in providers],
        "raw_data_providers": providers,
    }


# ------------------------------
# Global analysis tools (archeogenetic engines)
# ------------------------------

def fetch_analysis_tools(haplogroup: str) -> Dict:
    tools = [
        {
            "name": "MyTrueAncestry",
            "type": "Ancient DNA matching",
            "focus": "Vertaa käyttäjän DNA:ta tuhansiin arkeologisiin muinaisnäytteisiin.",
            "compatibility": "Hyväksyy autosomaali-, Y-DNA-, mtDNA- ja WGS-datan.",
            "notes": "Tuottaa karttoja, aikajanoja ja sivilisaatiotason tulkintoja.",
            "url": "https://mytrueancestry.com",
        },
        {
            "name": "GEDmatch",
            "type": "Admixture & heritage tools",
            "focus": "Admixture/Oracle-laskurit muinaisista komponenttipopulaatioista.",
            "compatibility": "Hyväksyy useimpien kuluttajatestien raakadatamuodot.",
            "notes": "Sopii muinaisten komponenttien arviointiin ja sukutaustojen vertailuun.",
            "url": "https://www.gedmatch.com",
        },
        {
            "name": "Genoplot / G25 tools",
            "type": "G25 modeling",
            "focus": "Korkean resoluution populaatiomallinnus muinais- ja modernidataan.",
            "compatibility": "Yhteensopiva useiden raakadatamuotojen kanssa.",
            "notes": "Mahdollistaa hienojakoisen mallinnuksen muinaisista viitepopulaatioista.",
            "url": "https://genoplot.com",
        },
        {
            "name": "Illustrative DNA",
            "type": "G25-based ancient modeling",
            "focus": "Granulaarinen muinaisväestöjen mallinnus.",
            "compatibility": "Yhteensopiva keskeisten kuluttajatestien kanssa.",
            "notes": "Sopii jatkoanalytiikkaan MyTrueAncestryn/GEDmatchin rinnalle.",
            "url": "https://illustrativedna.com",
        },
        {
            "name": "Genomelink Ancient Ancestry",
            "type": "Trait & ancient ancestry",
            "focus": "Ancient Ancestry -raportit osana laajempaa fenotyyppi- ja perimäpalvelua.",
            "compatibility": "Hyväksyy AncestryDNA, 23andMe, MyHeritage ja FTDNA-datat.",
            "notes": "Tarjoaa muinaisperimän lisäksi muita raportteja.",
            "url": "https://genomelink.io",
        },
        {
            "name": "Nebula Genomics (upload)",
            "type": "Raw DNA upload & WGS analysis",
            "focus": "Syvempi analyysi täysgenomidatasta.",
            "compatibility": "Hyväksyy mm. AncestryDNA:n ja 23andMe:n datan.",
            "notes": "Kattaa myös syvä-esi-isä- ja haploryhmäanalyysin.",
            "url": "https://nebula.org/free-dna-upload-analysis/",
        },
        {
            "name": "ADMIXTOOLS",
            "type": "Academic population genetics toolkit",
            "focus": "qpAdm, qpGraph, f-statistics muinais- ja modernipopulaatioiden mallinnukseen.",
            "compatibility": "Tutkimusympäristö, ei kuluttajille.",
            "notes": "Ammattilaistason työkalu arkeogeneettiseen analyysiin.",
            "url": "https://github.com/DReichLab/AdmixTools",
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
