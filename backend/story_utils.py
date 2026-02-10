from typing import Dict, List, Optional
from i18n_utils import get_text, build_intro, build_label
from datetime import datetime

# -----------------------------
# Päärajapinta
# -----------------------------

def generate_story(
    haplogroup_data: Dict,
    lang: str = "en",
    tone: str = "chronological",
    region: str = "global",
    user_name: Optional[str] = None,
    notes: Optional[str] = None,
) -> Dict[str, str]:
    """
    Tuottaa koko haploryhmäraportin osiot rakenteellisessa muodossa.
    Palauttaa sanakirjan, jossa osiot ovat nimettyjä tekstikokonaisuuksia.
    """

    story = {}

    # 1) Otsikko ja johdanto
    story["intro"] = build_intro(lang, tone, region).format(haplogroup=haplogroup_data.get("haplogroup", ""))
    if user_name:
        story["intro"] = personalize_intro(story["intro"], user_name, lang)

    # 2) Yleiskuvaus
    story["overview"] = build_overview(haplogroup_data, lang, tone, region)

    # 3) Kronologinen aikajana
    story["timeline"] = build_chronological_timeline(haplogroup_data, lang, tone, region)

    # 4) Maantieteellinen levinneisyys
    story["distribution"] = build_geographic_distribution(haplogroup_data, lang, tone, region)

    # 5) Muinaiset näytteet
    story["ancient_samples"] = build_ancient_samples_section(haplogroup_data, lang, tone, region)

    # 6) Kulttuuriset kontekstit
    story["cultural_contexts"] = build_cultural_contexts(haplogroup_data, lang, tone, region)

    # 7) Tieteellinen tulkinta
    story["scientific_interpretation"] = build_scientific_interpretation(haplogroup_data, lang, tone, region)

    # 😎 Lähteet
    story["sources"] = build_sources_section(haplogroup_data, lang)

    # 9) Yksityisyys
    story["privacy_notice"] = get_text("privacy_notice", lang)

    # 10) Käyttäjän muistiinpanot
    if notes:
        story["user_notes"] = format_user_notes(notes, lang)

    # 11) Metadata
    story["metadata"] = build_metadata(haplogroup_data, lang, tone, region)

    return story


# -----------------------------
# Osioiden rakentajat
# -----------------------------

def build_overview(data: Dict, lang: str, tone: str, region: str) -> str:
    title = build_label("haplogroup_title", lang).format(haplogroup=data.get("haplogroup", ""))
    description = data.get("description") or get_text("description_intro", lang, tone, region)

    lineage_type = data.get("lineage_type", "")
    time_depth = data.get("time_depth", "")
    regions = ", ".join(data.get("regions", []))

    lines = [
        title,
        "",
        description,
    ]

    if lineage_type:
        lines.append(f"{get_text('lineage_type_label', lang)}: {lineage_type}")
    if time_depth:
        lines.append(f"{build_label('time_depth_label', lang)}: {time_depth}")
    if regions:
        lines.append(f"{build_label('regions_label', lang)}: {regions}")

    return "\n".join(lines).strip()


def build_chronological_timeline(data: Dict, lang: str, tone: str, region: str) -> str:
    title = get_text("timeline_title", lang, tone, region) or "Chronological timeline"
    intro = get_text("section_intro", lang, tone, region)

    events = data.get("timeline", []) or infer_timeline_from_samples(data)

    if not events:
        return f"{title}\n\n{get_text('no_timeline_data', lang, tone, region)}"

    lines = [title, "", intro, ""]

    for event in sorted(events, key=lambda e: e.get("date", "")):
        lines.append(format_timeline_event(event, lang))

    return "\n".join(lines).strip()


def build_geographic_distribution(data: Dict, lang: str, tone: str, region: str) -> str:
    title = build_label("regions_label", lang)
    intro = get_text("distribution_intro", lang, tone, region)

    regions = data.get("regions", [])
    regional_profiles = data.get("regional_profiles", [])

    lines = [title, "", intro, ""]

    if regions:
        lines.append(get_text("regions_list_intro", lang, tone, region) + ":")
        for r in regions:
            lines.append(f"• {r}")

    if regional_profiles:
        lines.append("")
        lines.append(get_text("regional_profiles_intro", lang, tone, region))
        for profile in regional_profiles:
            lines.append(format_regional_profile(profile, lang))

    return "\n".join(lines).strip()


def build_ancient_samples_section(data: Dict, lang: str, tone: str, region: str) -> str:
    title = build_label("ancient_samples_label", lang)
    intro = get_text("ancient_samples_intro", lang, tone, region)

    samples = data.get("ancient_samples", [])

    lines = [title, "", intro, ""]

    if not samples:
        lines.append(get_text("no_ancient_samples", lang, tone, region))
        return "\n".join(lines).strip()

    for sample in samples:
        lines.append(format_ancient_sample(sample, lang))

    return "\n".join(lines).strip()


def build_cultural_contexts(data: Dict, lang: str, tone: str, region: str) -> str:
    title = get_text("cultural_contexts_title", lang, tone, region)
    intro = get_text("cultural_contexts_intro", lang, tone, region)

    cultures = data.get("cultures", []) or infer_cultures_from_regions(data)

    lines = [title, "", intro, ""]

    if not cultures:
        lines.append(get_text("no_cultural_contexts", lang, tone, region))
        return "\n".join(lines).strip()

    for culture in cultures:
        lines.append(format_culture(culture, lang))

    return "\n".join(lines).strip()


def build_scientific_interpretation(data: Dict, lang: str, tone: str, region: str) -> str:
    title = get_text("scientific_interpretation_title", lang, tone, region)
    intro = get_text("scientific_interpretation_intro", lang, tone, region)

    reliability = data.get("reliability_score")
    lineage_type = data.get("lineage_type")
    raw_providers = data.get("raw_data_providers", [])
    tools = data.get("analysis_tools", [])

    lines = [title, "", intro, ""]

    if reliability is not None:
        lines.append(get_text("reliability_score_label", lang, tone, region).format(score=reliability))

    if lineage_type:
        lines.append(get_text("lineage_type_statement", lang, tone, region).format(type=lineage_type))

    if raw_providers:
        lines.append("")
        lines.append(get_text("raw_data_providers_label", lang, tone, region))
        for p in raw_providers:
            lines.append(f"• {p.get('name')} ({p.get('url', '')})")

    if tools:
        lines.append("")
        lines.append(get_text("analysis_tools_label", lang, tone, region))
        for tool in tools:
            lines.append(f"• {tool.get('name')} ({tool.get('url', '')})")

    return "\n".join(lines).strip()


def build_sources_section(data: Dict, lang: str) -> str:
    title = build_label("sources_label", lang)
    sources = data.get("sources", [])

    lines = [title, ""]

    if not sources:
        lines.append(get_text("no_sources", lang))
        return "\n".join(lines).strip()

    for source in sources:
        lines.append(f"• {source}")

    return "\n".join(lines).strip()


# -----------------------------
# Apurakentajat
# -----------------------------

def personalize_intro(intro_text: str, user_name: str, lang: str) -> str:
    greeting = get_text("personal_greeting", lang).format(name=user_name)
    return f"{greeting}\n\n{intro_text}"


def format_timeline_event(event: Dict, lang: str) -> str:
    date = event.get("date", get_text("unknown_date", lang))
    location = event.get("location", get_text("unknown_location", lang))
    description = event.get("description", "")

    return f"• {date} — {location}: {description}"


def format_ancient_sample(sample: Dict, lang: str) -> str:
    name = sample.get("name", get_text("unknown_sample", lang))
    date = sample.get("date", get_text("unknown_date", lang))
    location = sample.get("location", get_text("unknown_location", lang))
    culture = sample.get("culture", "")
    publication = sample.get("publication", "")

    line = f"• {name} — {date}, {location}"
    if culture:
        line += f" ({culture})"
    if publication:
        line += f". {get_text('publication_label', lang)}: {publication}"
    return line


def format_regional_profile(profile: Dict, lang: str) -> str:
    region_name = profile.get("region", get_text("unknown_region", lang))
    summary = profile.get("summary", "")
    timeframe = profile.get("timeframe", "")

    line = f"• {region_name}"
    if timeframe:
        line += f" ({timeframe})"
    if summary:
        line += f": {summary}"
    return line


def format_culture(culture: Dict, lang: str) -> str:
    name = culture.get("name", get_text("unknown_culture", lang))
    timeframe = culture.get("timeframe", "")
    description = culture.get("description", "")

    line = f"• {name}"
    if timeframe:
        line += f" ({timeframe})"
    if description:
        line += f": {description}"
    return line


def format_user_notes(notes: str, lang: str) -> str:
    title = get_text("user_notes_label", lang)
    return f"{title}\n\n{notes}".strip()


def build_metadata(data: Dict, lang: str, tone: str, region: str) -> Dict:
    return {
        "haplogroup": data.get("haplogroup"),
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "language": lang,
        "tone": tone,
        "region": region,
        "reliability_score": data.get("reliability_score"),
        "sources_count": len(data.get("sources", [])),
    }


# -----------------------------
# Inferenssifunktiot (fallback)
# -----------------------------

def infer_timeline_from_samples(data: Dict) -> List[Dict]:
    """
    Jos aikajanaa ei ole suoraan annettu, rakennetaan se muinaisnäytteistä.
    """
    samples = data.get("ancient_samples", [])
    timeline = []
    for s in samples:
        timeline.append({
            "date": s.get("date"),
            "location": s.get("location"),
            "description": s.get("description") or s.get("culture") or "",
        })
    return timeline


def infer_cultures_from_regions(data: Dict) -> List[Dict]:
    """
    Jos kulttuureja ei ole eksplisiittisesti, rakennetaan ne alueista ja näytteistä.
    """
    cultures = []
    for sample in data.get("ancient_samples", []):
        culture = sample.get("culture")
        if culture:
            cultures.append({
                "name": culture,
                "timeframe": sample.get("date"),
                "description": "",
            })
    return cultures
