from typing import Dict, List, Optional
from i18n_utils import get_text
from data_utils import fetch_full_haplogroup_data


# ----------------------------
# Core story generator
# ----------------------------

def generate_story(haplogroup_data: Dict, lang: str = "en", tone: str = "academic") -> Dict:
    """
    Rakentaa kronologisen, kulttuuritietoisen ja arkeogeneettisen kertomuksen haploryhmästä.
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

    # Tunnetut historialliset henkilöt
    story["sections"].append(build_famous_people_section(haplogroup_data, lang, style))

    # Hotspotit / poikkeavat esiintymiskeskittymät
    story["sections"].append(build_hotspots_section(haplogroup_data, lang, style))

    # Aluekohtaiset profiilit
    story["sections"].extend(build_regional_profiles(haplogroup_data, lang, style))

    # Nykyinen levinneisyys
    story["sections"].append(build_modern_distribution(haplogroup_data, lang, style))

    # Lähteet ja luotettavuus
    story["sections"].append(build_sources_section(haplogroup_data, lang, style))

    # Laillisuus & yksityisyys
    story["sections"].append(build_legal_section(haplogroup_data, lang, style))

    # Ero perinteiseen sukututkimukseen
    story["sections"].append(build_genealogy_comparison_section(haplogroup_data, lang, style))

    # Juuret & aarre -loppuhuipennus
    story["sections"].append(build_heritage_section(haplogroup_data, lang, style))

    return story


# ----------------------------
# Dual haplogroup generator (Y-DNA + mtDNA)
# ----------------------------

def generate_dual_haplogroup_story(
    y_haplogroup: str,
    mt_haplogroup: str,
    lang: str = "en",
    tone: str = "academic"
) -> Dict:
    """
    Rakentaa kahden haploryhmän (Y-DNA + mtDNA) yhdistetyn tarinan:
    sisältää molempien kertomukset, niiden historialliset kohtaamiset
    sekä symbolisen rakkaustarinan lopuksi.
    """
    y_data = fetch_full_haplogroup_data(y_haplogroup)
    mt_data = fetch_full_haplogroup_data(mt_haplogroup)

    style = get_style_profile(lang=lang, tone=tone)

    story = {
        "title": get_text("dual_story_title", lang, y=y_haplogroup, mt=mt_haplogroup),
        "subtitle": get_text("dual_story_subtitle", lang),
        "sections": [],
        "metadata": {
            "y_haplogroup": y_haplogroup,
            "mt_haplogroup": mt_haplogroup,
        },
    }

    # Y-DNA tarina
    story["sections"].append({
        "id": "y_story",
        "title": get_text("section_y_story_title", lang, haplogroup=y_haplogroup),
        "content": generate_story(y_data, lang, tone)["sections"],
    })

    # mtDNA tarina
    story["sections"].append({
        "id": "mt_story",
        "title": get_text("section_mt_story_title", lang, haplogroup=mt_haplogroup),
        "content": generate_story(mt_data, lang, tone)["sections"],
    })

    # Historialliset kohtaamiset
    story["sections"].append(build_dual_encounters_section(y_data, mt_data, lang, style))

    # Symbolinen rakkaustarina
    story["sections"].append(build_dual_love_story_section(y_data, mt_data, lang, style))

    # Loppuhuipennus
    story["sections"].append(build_dual_heritage_section(y_data, mt_data, lang, style))

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


def build_famous_people_section(data: Dict, lang: str, style: Dict) -> Dict:
    """
    Tunnetut historialliset henkilöt, jos sellaisia tunnetaan haploryhmästä.
    """
    people = data.get("famous_people", [])
    if not people:
        content = get_text("no_famous_people_available", lang)
    else:
        lines = []
        for person in people:
            lines.append(style["famous_person_entry"].format(
                name=person.get("name"),
                era=person.get("era"),
                region=person.get("region"),
                significance=person.get("significance"),
            ))
        content = "\n\n".join(lines)

    return {
        "id": "famous_people",
        "title": get_text("section_famous_people_title", lang),
        "content": content,
    }


def build_hotspots_section(data: Dict, lang: str, style: Dict) -> Dict:
    """
    Poikkeavat tai erityisen merkittävät esiintymiskeskittymät ("hotspots").
    """
    hotspots = data.get("hotspots", [])
    if not hotspots:
        content = get_text("no_hotspots_available", lang)
    else:
        lines = []
        for hotspot in hotspots:
            lines.append(style["hotspot_entry"].format(
                location=hotspot.get("location"),
                period=hotspot.get("period"),
                description=hotspot.get("description"),
                significance=hotspot.get("significance"),
            ))
        content = "\n\n".join(lines)

    return {
        "id": "hotspots",
        "title": get_text("section_hotspots_title", lang),
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


def build_legal_section(data: Dict, lang: str, style: Dict) -> Dict:
    """
    Laillisuus, vastuuvapaus, yksityisyys.
    """
    return {
        "id": "legal",
        "title": get_text("section_legal_title", lang),
        "content": style["legal_section"].format(),
    }


def build_genealogy_comparison_section(data: Dict, lang: str, style: Dict) -> Dict:
    """
    Selittää eron arkeogeneettisen haploryhmätarinan ja perinteisen sukututkimuksen välillä.
    """
    return {
        "id": "genealogy_comparison",
        "title": get_text("section_genealogy_comparison_title", lang),
        "content": style["genealogy_comparison_section"].format(),
    }


def build_heritage_section(data: Dict, lang: str, style: Dict) -> Dict:
    """
    Loppuhuipennus: juuret, aarre, merkityksellisyys tilaajalle.
    """
    return {
        "id": "heritage",
        "title": get_text("section_heritage_title", lang),
        "content": style["heritage_section"].format(
            haplogroup=data.get("haplogroup"),
        ),
    }


# ----------------------------
# Dual haplogroup sections
# ----------------------------

def build_dual_encounters_section(y_data: Dict, mt_data: Dict, lang: str, style: Dict) -> Dict:
    """
    Kuvaa historialliset kohtaamiset alueilla ja kulttuureissa,
    joissa molemmat haploryhmät ovat olleet läsnä.
    """
    y_regions = set(y_data.get("regions", []))
    mt_regions = set(mt_data.get("regions", []))
    shared_regions = sorted(y_regions.intersection(mt_regions))

    content = style["dual_encounters_section"].format(
        y=y_data.get("haplogroup"),
        mt=mt_data.get("haplogroup"),
        regions=", ".join(shared_regions) if shared_regions else get_text("no_shared_regions", lang),
    )

    return {
        "id": "dual_encounters",
        "title": get_text("section_dual_encounters_title", lang),
        "content": content,
    }


def build_dual_love_story_section(y_data: Dict, mt_data: Dict, lang: str, style: Dict) -> Dict:
    """
    Symbolinen rakkaustarina Y-DNA:n ja mtDNA:n kohtaamisesta historian kuluessa.
    """
    content = style["dual_love_story_section"].format(
        y=y_data.get("haplogroup"),
        mt=mt_data.get("haplogroup"),
    )

    return {
        "id": "dual_love_story",
        "title": get_text("section_dual_love_story_title", lang),
        "content": content,
    }


def build_dual_heritage_section(y_data: Dict, mt_data: Dict, lang: str, style: Dict) -> Dict:
    """
    Yhdistetty perintö: tilaajan kahden linjan merkitys ja syvyys.
    """
    content = style["dual_heritage_section"].format(
        y=y_data.get("haplogroup"),
        mt=mt_data.get("haplogroup"),
    )

    return {
        "id": "dual_heritage",
        "title": get_text("section_dual_heritage_title", lang),
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


def generate_dual_story_from_haplogroups(
    y_haplogroup: str,
    mt_haplogroup: str,
    lang: str = "en",
    tone: str = "academic"
) -> Dict:
    """
    Julkinen API kahden haploryhmän yhdistetylle tarinalle.
    """
    return generate_dual_haplogroup_story(y_haplogroup, mt_haplogroup, lang, tone)
