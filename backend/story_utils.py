from typing import Dict, List
from i18n_utils import get_text, get_style_profile
from data_utils import fetch_full_haplogroup_data


def generate_story(haplogroup_data: Dict, lang: str = "en", tone: str = "academic") -> Dict:
    """
    Rakentaa kronologisen, arkeogeneettisen kertomuksen haploryhmästä.
    Palauttaa rakenteellisen tarinapaketin, jota pdf_utils ja email_utils voivat käyttää.
    """
    style = get_style_profile(lang=lang, tone=tone)

    story = {
        "title": build_title(haplogroup_data, lang),
        "subtitle": build_subtitle(haplogroup_data, lang),
        "sections": [],
        "metadata": {
            "haplogroup": haplogroup_data.get("haplogroup"),
            "lineage_type": haplogroup_data.get("lineage_type"),
            "regions": haplogroup_data.get("regions", []),
            "time_depth": haplogroup_data.get("time_depth"),
            "reliability_score": haplogroup_data.get("reliability_score"),
        },
    }

    # Johdanto
    story["sections"].append(build_introduction(haplogroup_data, lang, style))

    # Kronologinen kulku muinaisista löydöistä
    story["sections"].append(build_chronological_migration(haplogroup_data, lang, style))

    # Kulttuurit ja yhteydet
    story["sections"].append(build_cultural_context(haplogroup_data, lang, style))

    # Aluekohtaiset profiilit
    story["sections"].extend(build_regional_profiles(haplogroup_data, lang, style))

    # Nykyinen levinneisyys
    story["sections"].append(build_modern_distribution(haplogroup_data, lang, style))

    # Lähteet ja luotettavuus
    story["sections"].append(build_sources_section(haplogroup_data, lang, style))

    return story


# ----------------------------
# Section builders
# ----------------------------

def build_title(data: Dict, lang: str) -> str:
    return get_text("story_title", lang, haplogroup=data.get("haplogroup"))


def build_subtitle(data: Dict, lang: str) -> str:
    lineage_type = data.get("lineage_type", "unknown")
    return get_text("story_subtitle", lang, lineage_type=lineage_type)


def build_introduction(data: Dict, lang: str, style: Dict) -> Dict:
    return {
        "id": "introduction",
        "title": get_text("section_introduction_title", lang),
        "content": style["introduction"].format(
            haplogroup=data.get("haplogroup"),
            time_depth=data.get("time_depth", get_text("unknown_time_depth", lang)),
            regions=", ".join(data.get("regions", [])),
        ),
    }


def build_chronological_migration(data: Dict, lang: str, style: Dict) -> Dict:
    ancient_samples = data.get("ancient_samples", [])
    if not ancient_samples:
        content = get_text("no_ancient_samples_available", lang)
    else:
        lines = []
        for sample in sorted(ancient_samples, key=lambda x: x.get("date", 0)):
            lines.append(format_sample_entry(sample, lang, style))
        content = "\n\n".join(lines)

    return {
        "id": "chronological_migration",
        "title": get_text("section_chronological_title", lang),
        "content": content,
    }


def build_cultural_context(data: Dict, lang: str, style: Dict) -> Dict:
    cultures = data.get("cultures", [])
    if not cultures:
        content = get_text("no_cultural_data_available", lang)
    else:
        lines = []
        for culture in cultures:
            lines.append(style["culture_entry"].format(
                culture=culture.get("name"),
                period=culture.get("period"),
                region=culture.get("region"),
                description=culture.get("description", ""),
            ))
        content = "\n\n".join(lines)

    return {
        "id": "cultural_context",
        "title": get_text("section_cultural_title", lang),
        "content": content,
    }


def build_regional_profiles(data: Dict, lang: str, style: Dict) -> List[Dict]:
    profiles = data.get("regional_profiles", [])
    sections = []

    for profile in profiles:
        sections.append({
            "id": f"region_{profile.get('region', '').lower().replace(' ', '_')}",
            "title": get_text("section_region_title", lang, region=profile.get("region")),
            "content": style["regional_profile"].format(
                region=profile.get("region"),
                time_span=profile.get("time_span", ""),
                key_finds=", ".join(profile.get("key_finds", [])),
                cultures=", ".join(profile.get("cultures", [])),
                description=profile.get("description", ""),
            ),
        })

    return sections


def build_modern_distribution(data: Dict, lang: str, style: Dict) -> Dict:
    regions = data.get("regions", [])
    content = style["modern_distribution"].format(
        regions=", ".join(regions) if regions else get_text("no_regions_available", lang)
    )

    return {
        "id": "modern_distribution",
        "title": get_text("section_modern_distribution_title", lang),
        "content": content,
    }


def build_sources_section(data: Dict, lang: str, style: Dict) -> Dict:
    sources = data.get("sources", [])
    providers = data.get("raw_data_providers", [])
    tools = data.get("analysis_tools", [])
    reliability = data.get("reliability_score", 0)

    content = style["sources_section"].format(
        sources=", ".join(sources),
        providers=", ".join([p.get("name") for p in providers]),
        tools=", ".join([t.get("name") for t in tools]),
        reliability=reliability,
    )

    return {
        "id": "sources",
        "title": get_text("section_sources_title", lang),
        "content": content,
    }


# ----------------------------
# Helpers
# ----------------------------

def format_sample_entry(sample: Dict, lang: str, style: Dict) -> str:
    """
    Muotoilee yksittäisen muinaisnäytteen tarinaelementiksi.
    """
    return style["sample_entry"].format(
        sample_id=sample.get("id", get_text("unknown_sample", lang)),
        date=sample.get("date", get_text("unknown_date", lang)),
        location=sample.get("location", get_text("unknown_location", lang)),
        culture=sample.get("culture", get_text("unknown_culture", lang)),
        context=sample.get("context", ""),
    )


# ----------------------------
# Public API
# ----------------------------

def generate_story_from_haplogroup(haplogroup: str, lang: str = "en", tone: str = "academic") -> Dict:
    """
    Yhdistää data_utils + story_utils ja palauttaa valmiin tarinapaketin.
    """
    data = fetch_full_haplogroup_data(haplogroup)
    return generate_story(data, lang=lang, tone=tone)
