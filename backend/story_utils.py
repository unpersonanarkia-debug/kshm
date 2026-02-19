"""
story_utils.py — KSHM Narrative Engine

Rakentaa kronologisen, paikkakohtaisen arkeogeneettisen kertomuksen
haplogroup_data-rakenteesta. Tavoite: jokaisella osiolla on muoto

    PAIKKA  →  AIKA  →  HENKILÖ (muinaisnäyte)  →  TIETEELLINEN TODISTE

Tyyliviite: kshm.fi/case-h1-t16189c-01.html
Sävy: "Verilinjan seikkailu ajassa" — ei tieteellinen abstrakti vaan
elämyksellinen matka joka ankkuroituu vertaisarvioituihin lähteisiin.
"""

from __future__ import annotations

import logging
from typing import Dict, List, Optional

from i18n_utils import (
    get_style_profile,
    get_style_profile_template,
    get_text,
    format_sources_list,
)
from data_utils import (
    fetch_full_haplogroup_data,
    render_fragments,
    DescriptionFragment,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Tone constants — ohjaa tyyliprofiilin valintaa tulevaisuudessa
# ---------------------------------------------------------------------------

TONE_NARRATIVE  = "narrative"    # kuluttaja: elämyksellinen
TONE_ACADEMIC   = "academic"     # KOSH: vertaisarvioitu
TONE_ADVENTURE  = "adventure"    # premium: seikkailullinen (tuleva)

DEFAULT_TONE = TONE_NARRATIVE


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def generate_story_from_haplogroup(
    haplogroup: str,
    lang: str = "en",
    tone: str = DEFAULT_TONE,
) -> Dict:
    """
    Päärajapinta: hakee datan ja rakentaa tarinan yhdellä kutsulla.

        story = generate_story_from_haplogroup("H1-T16189C", lang="fi", tone="narrative")
    """
    data = fetch_full_haplogroup_data(haplogroup)
    return generate_story(data, lang=lang, tone=tone)


def generate_dual_story_from_haplogroups(
    y_haplogroup: str,
    mt_haplogroup: str,
    lang: str = "en",
    tone: str = DEFAULT_TONE,
) -> Dict:
    """Kahden linjan (Y-DNA + mtDNA) yhdistetty tarina."""
    return generate_dual_haplogroup_story(y_haplogroup, mt_haplogroup, lang, tone)


# ---------------------------------------------------------------------------
# Core story generator
# ---------------------------------------------------------------------------

def generate_story(
    haplogroup_data: Dict,
    lang: str = "en",
    tone: str = DEFAULT_TONE,
) -> Dict:
    """
    Rakentaa tarinapaketin haplogroup_data-rakenteesta.

    Palautusrakenne:
    {
        "title": str,
        "subtitle": str,
        "hook": str,           # Kohtaaminen-osio (sivun avaus)
        "sections": [...]      # kronologinen osiolista
        "metadata": {...}
    }
    """
    style = get_style_profile(lang=lang, tone=tone)
    hg    = haplogroup_data.get("haplogroup", "")

    story: Dict = {
        "title":    _build_title(haplogroup_data, lang),
        "subtitle": _build_subtitle(haplogroup_data, lang),
        "hook":     _build_hook(haplogroup_data, lang),
        "sections": [],
        "metadata": _build_metadata(haplogroup_data),
    }

    # ── Johdanto ────────────────────────────────────────────────────────────
    story["sections"].append(_build_introduction(haplogroup_data, lang, style))

    # ── Kronologinen matka muinaisista löydöistä ─────────────────────────────
    # Jokainen muinaisnäyte = oma osionsa (paikka + aika + todiste)
    story["sections"].extend(_build_chronological_episodes(haplogroup_data, lang, style))

    # ── Kulttuurikontekstit ─────────────────────────────────────────────────
    story["sections"].append(_build_cultural_context(haplogroup_data, lang, style))

    # ── Tunnetut historialliset henkilöt ────────────────────────────────────
    famous = _build_famous_people_section(haplogroup_data, lang, style)
    if famous:
        story["sections"].append(famous)

    # ── Hotspotit ───────────────────────────────────────────────────────────
    hotspots = _build_hotspots_section(haplogroup_data, lang, style)
    if hotspots:
        story["sections"].append(hotspots)

    # ── Aluekohtaiset profiilit ─────────────────────────────────────────────
    story["sections"].extend(_build_regional_profiles(haplogroup_data, lang, style))

    # ── Data source -fragmentit (i18n-renderöityinä) ─────────────────────────
    source_narrative = _build_source_narrative(haplogroup_data, lang)
    if source_narrative:
        story["sections"].append(source_narrative)

    # ── Nykyinen levinneisyys ───────────────────────────────────────────────
    story["sections"].append(_build_modern_distribution(haplogroup_data, lang, style))

    # ── Ero perinteiseen sukututkimukseen ───────────────────────────────────
    story["sections"].append(_build_genealogy_comparison(haplogroup_data, lang, style))

    # ── Lähteet ja luotettavuus ─────────────────────────────────────────────
    story["sections"].append(_build_sources_section(haplogroup_data, lang, style))

    # ── Lakipykälä + yksityisyys ────────────────────────────────────────────
    story["sections"].append(_build_legal_section(haplogroup_data, lang, style))

    # ── Loppuhuipennus ──────────────────────────────────────────────────────
    story["sections"].append(_build_heritage_section(haplogroup_data, lang, style))

    return story


# ---------------------------------------------------------------------------
# Dual haplogroup story
# ---------------------------------------------------------------------------

def generate_dual_haplogroup_story(
    y_haplogroup: str,
    mt_haplogroup: str,
    lang: str = "en",
    tone: str = DEFAULT_TONE,
) -> Dict:
    """
    Y-DNA + mtDNA yhdistetty tarina:
    – kummankin linjan oma kronologinen matka
    – historialliset kohtaamiset yhteisillä alueilla
    – symbolinen rakkaustarina
    – yhteinen perintö-loppuhuipennus
    """
    y_data  = fetch_full_haplogroup_data(y_haplogroup)
    mt_data = fetch_full_haplogroup_data(mt_haplogroup)
    style   = get_style_profile(lang=lang, tone=tone)

    story: Dict = {
        "title":    _safe_get_text("dual_story_title",    lang, y=y_haplogroup, mt=mt_haplogroup),
        "subtitle": _safe_get_text("dual_story_subtitle", lang),
        "sections": [],
        "metadata": {
            "y_haplogroup":  y_haplogroup,
            "mt_haplogroup": mt_haplogroup,
        },
    }

    # Y-DNA tarina omana kokonaisuutenaan
    story["sections"].append({
        "id":      "y_story",
        "title":   _safe_get_text("section_y_story_title", lang, haplogroup=y_haplogroup),
        "content": generate_story(y_data, lang, tone)["sections"],
        "type":    "nested_story",
    })

    # mtDNA tarina omana kokonaisuutenaan
    story["sections"].append({
        "id":      "mt_story",
        "title":   _safe_get_text("section_mt_story_title", lang, haplogroup=mt_haplogroup),
        "content": generate_story(mt_data, lang, tone)["sections"],
        "type":    "nested_story",
    })

    # Historialliset kohtaamiset yhteisillä alueilla
    story["sections"].append(_build_dual_encounters(y_data, mt_data, lang, style))

    # Symbolinen rakkaustarina
    story["sections"].append(_build_dual_love_story(y_data, mt_data, lang, style))

    # Yhteinen perintö
    story["sections"].append(_build_dual_heritage(y_data, mt_data, lang, style))

    return story


# ---------------------------------------------------------------------------
# Section builders — yksityiset
# ---------------------------------------------------------------------------

def _build_title(data: Dict, lang: str) -> str:
    hg = data.get("haplogroup", "")
    return _safe_get_text("story_title", lang, haplogroup=hg)


def _build_subtitle(data: Dict, lang: str) -> str:
    lineage_type = data.get("lineage_type", "unknown")
    return _safe_get_text("story_subtitle", lang, lineage_type=lineage_type)


def _build_hook(data: Dict, lang: str) -> str:
    """
    'Kohtaaminen'-tyyppinen avausteksti — emotionaalinen sisäänheittokoukku.
    Käytetään HTML/PDF-renderöinnissä sivun alussa ennen varsinaisia osioita.
    """
    hg = data.get("haplogroup", "")
    return _safe_get_text("story_hook", lang, haplogroup=hg)


def _build_metadata(data: Dict) -> Dict:
    return {
        "haplogroup":       data.get("haplogroup"),
        "lineage_type":     data.get("lineage_type"),
        "regions":          data.get("regions", []),
        "time_depth":       data.get("time_depth"),
        "reliability_score": data.get("reliability_score"),
        "source_count":     len(data.get("sources", [])),
    }


def _build_introduction(data: Dict, lang: str, style: Dict) -> Dict:
    """
    Johdanto: haplogroup + aikasyvyys + levinneisyys + metodologia.
    Vastaa sivun 'Johdanto'-osiota, jossa on myös 'Analyysin ydin' -faktalista.
    """
    hg         = data.get("haplogroup", "")
    time_depth = data.get("time_depth") or _safe_get_text("unknown_time_depth", lang)
    regions    = ", ".join(data.get("regions", []))

    try:
        intro_text = style["introduction"].format(
            haplogroup=hg,
            time_depth=time_depth,
            regions=regions,
        )
    except KeyError as e:
        logger.warning(f"introduction template missing key {e}, using fallback")
        intro_text = f"{hg} — {time_depth}"

    # Analyysin ydin -faktalista (rakenne, ei teksti)
    key_facts = {
        "haplogroup":    hg,
        "lineage_type":  data.get("lineage_type", ""),
        "time_depth":    time_depth,
        "methodology":   _safe_get_text("methodology_archaeogenetics", lang),
        "source_type":   _safe_get_text("source_type_peer_reviewed",   lang),
    }

    return {
        "id":        "introduction",
        "title":     _safe_get_text("section_introduction_title", lang),
        "content":   intro_text,
        "key_facts": key_facts,
        "type":      "introduction",
    }


def _build_chronological_episodes(data: Dict, lang: str, style: Dict) -> List[Dict]:
    """
    Jokainen muinaisnäyte = oma episodiosionsa.
    Rakenne:
      – otsikko = paikka (arkeologinen kohde)
      – content = narratiivinen kuvaus kontekstineen
      – evidence = tieteellinen todiste (näyte-ID, päiväys, lähde)

    Jos muinaisnäytteitä ei ole, palautetaan yksi 'ei dataa' -osio.
    """
    ancient_samples = data.get("ancient_samples", [])

    if not ancient_samples:
        return [{
            "id":      "chronological_migration",
            "title":   _safe_get_text("section_chronological_title", lang),
            "content": _safe_get_text("no_ancient_samples_available", lang),
            "type":    "chronological_empty",
        }]

    episodes: List[Dict] = []

    # Järjestetään vanhimmasta uusimpaan
    sorted_samples = sorted(
        ancient_samples,
        key=lambda s: _parse_date_for_sort(s.get("date", "0")),
    )

    for sample in sorted_samples:
        episode = _build_single_episode(sample, lang, style)
        episodes.append(episode)

    return episodes


def _build_single_episode(sample: Dict, lang: str, style: Dict) -> Dict:
    """
    Yksi muinaisnäyte → yksi episodiosio.

    Rakenne vastaa sivun osiota:
        🜂 OSA X — [ajanjakson nimi]
        # [Paikan nimi]
        [narratiivi + tieteellinen todiste]
    """
    sample_id  = sample.get("id", "")
    location   = sample.get("location", _safe_get_text("unknown_location", lang))
    date       = sample.get("date",     _safe_get_text("unknown_date",     lang))
    culture    = sample.get("culture",  _safe_get_text("unknown_culture",  lang))
    context    = sample.get("context",  "")
    era_label  = sample.get("era_label", "")   # esim. "Jääkauden selviytyjät"
    references = sample.get("references", [])  # akateemiset lähteet tälle näytteelle

    try:
        entry_text = style["sample_entry"].format(
            sample_id=sample_id,
            date=date,
            location=location,
            culture=culture,
            context=context,
        )
    except KeyError as e:
        logger.warning(f"sample_entry template missing key {e}")
        entry_text = f"{sample_id}: {location} ({date})"

    # Tieteellinen todiste-rakenne (renderöidään erikseen PDF:ssä)
    evidence = {
        "sample_id":  sample_id,
        "date":       date,
        "location":   location,
        "culture":    culture,
        "references": references,
    }

    return {
        "id":        f"episode_{sample_id.lower().replace(' ', '_').replace('/', '_')}",
        "title":     location,
        "era_label": era_label,
        "content":   entry_text,
        "narrative": context,   # rikkaampi narratiivi, jos data_utils tarjoaa sen
        "evidence":  evidence,
        "type":      "chronological_episode",
    }


def _build_cultural_context(data: Dict, lang: str, style: Dict) -> Dict:
    cultures = data.get("cultures", [])

    if not cultures:
        return {
            "id":      "cultural_context",
            "title":   _safe_get_text("section_cultural_title", lang),
            "content": _safe_get_text("no_cultural_data_available", lang),
            "type":    "cultural_empty",
        }

    lines = []
    for culture in cultures:
        try:
            line = style["culture_entry"].format(
                culture=culture.get("name", ""),
                period=culture.get("period", ""),
                region=culture.get("region", ""),
                description=culture.get("description", ""),
            )
            lines.append(line)
        except KeyError as e:
            logger.warning(f"culture_entry template missing key {e}")
            lines.append(culture.get("name", ""))

    return {
        "id":      "cultural_context",
        "title":   _safe_get_text("section_cultural_title", lang),
        "content": "\n\n".join(lines),
        "type":    "cultural_context",
    }


def _build_famous_people_section(data: Dict, lang: str, style: Dict) -> Optional[Dict]:
    people = data.get("famous_people", [])
    if not people:
        return None  # Ei renderöidä tyhjää osiota

    lines = []
    for person in people:
        try:
            lines.append(style["famous_person_entry"].format(
                name=person.get("name", ""),
                era=person.get("era", ""),
                region=person.get("region", ""),
                significance=person.get("significance", ""),
            ))
        except KeyError as e:
            logger.warning(f"famous_person_entry missing key {e}")
            lines.append(person.get("name", ""))

    return {
        "id":      "famous_people",
        "title":   _safe_get_text("section_famous_people_title", lang),
        "content": "\n\n".join(lines),
        "type":    "famous_people",
    }


def _build_hotspots_section(data: Dict, lang: str, style: Dict) -> Optional[Dict]:
    hotspots = data.get("hotspots", [])
    if not hotspots:
        return None  # Ei renderöidä tyhjää osiota

    lines = []
    for hotspot in hotspots:
        try:
            lines.append(style["hotspot_entry"].format(
                location=hotspot.get("location", ""),
                period=hotspot.get("period", ""),
                description=hotspot.get("description", ""),
                significance=hotspot.get("significance", ""),
            ))
        except KeyError as e:
            logger.warning(f"hotspot_entry missing key {e}")
            lines.append(hotspot.get("location", ""))

    return {
        "id":      "hotspots",
        "title":   _safe_get_text("section_hotspots_title", lang),
        "content": "\n\n".join(lines),
        "type":    "hotspots",
    }


def _build_regional_profiles(data: Dict, lang: str, style: Dict) -> List[Dict]:
    profiles = data.get("regional_profiles", [])
    sections = []

    for profile in profiles:
        region = profile.get("region", "")
        try:
            content = style["regional_profile"].format(
                region=region,
                time_span=profile.get("time_span", ""),
                key_finds=", ".join(profile.get("key_finds", [])),
                cultures=", ".join(profile.get("cultures", [])),
                description=profile.get("description", ""),
            )
        except KeyError as e:
            logger.warning(f"regional_profile template missing key {e}")
            content = region

        sections.append({
            "id":      f"region_{region.lower().replace(' ', '_')}",
            "title":   _safe_get_text("section_region_title", lang, region=region),
            "content": content,
            "type":    "regional_profile",
        })

    return sections


def _build_source_narrative(data: Dict, lang: str) -> Optional[Dict]:
    """
    Renderöi data_utils.py:n rakenteelliset description_fragments
    lokalisoituina teksteinä. Tämä on se kohta jossa i18n-pipeline
    sulkeutuu: fragmentit → käännetyt tekstit → narratiiviosio.
    """
    fragments: List[DescriptionFragment] = data.get("description_fragments", [])
    if not fragments:
        return None

    rendered = render_fragments(fragments, lang=lang)
    if not rendered:
        return None

    return {
        "id":      "source_narrative",
        "title":   _safe_get_text("section_source_narrative_title", lang),
        "content": "\n\n".join(rendered),
        "type":    "source_narrative",
    }


def _build_modern_distribution(data: Dict, lang: str, style: Dict) -> Dict:
    regions = data.get("regions", [])
    try:
        content = style["modern_distribution"].format(
            regions=format_sources_list(regions, lang=lang) if regions
                    else _safe_get_text("no_regions_available", lang)
        )
    except KeyError as e:
        logger.warning(f"modern_distribution template missing key {e}")
        content = ", ".join(regions)

    return {
        "id":      "modern_distribution",
        "title":   _safe_get_text("section_modern_distribution_title", lang),
        "content": content,
        "type":    "modern_distribution",
    }


def _build_genealogy_comparison(data: Dict, lang: str, style: Dict) -> Dict:
    try:
        content = style["genealogy_comparison_section"].format()
    except KeyError:
        content = _safe_get_text("no_genealogy_comparison_available", lang)

    return {
        "id":      "genealogy_comparison",
        "title":   _safe_get_text("section_genealogy_comparison_title", lang),
        "content": content,
        "type":    "genealogy_comparison",
    }


def _build_sources_section(data: Dict, lang: str, style: Dict) -> Dict:
    sources     = data.get("sources", [])
    providers   = data.get("raw_data_providers", [])
    tools       = data.get("analysis_tools", [])
    reliability = data.get("reliability_score", 0)

    try:
        content = style["sources_section"].format(
            sources=format_sources_list(sources, lang=lang),
            providers=", ".join(p.get("name", "") for p in providers),
            tools=", ".join(t.get("name", "") for t in tools),
            reliability=reliability,
        )
    except KeyError as e:
        logger.warning(f"sources_section template missing key {e}")
        content = format_sources_list(sources, lang=lang)

    return {
        "id":               "sources",
        "title":            _safe_get_text("section_sources_title", lang),
        "content":          content,
        "reliability_score": reliability,
        "source_list":      sources,
        "providers":        [p.get("name") for p in providers],
        "tools":            [t.get("name") for t in tools],
        "type":             "sources",
    }


def _build_legal_section(data: Dict, lang: str, style: Dict) -> Dict:
    try:
        content = style["legal_section"].format()
    except KeyError:
        content = ""

    return {
        "id":      "legal",
        "title":   _safe_get_text("section_legal_title", lang),
        "content": content,
        "type":    "legal",
    }


def _build_heritage_section(data: Dict, lang: str, style: Dict) -> Dict:
    hg = data.get("haplogroup", "")
    try:
        content = style["heritage_section"].format(haplogroup=hg)
    except KeyError as e:
        logger.warning(f"heritage_section template missing key {e}")
        content = hg

    return {
        "id":      "heritage",
        "title":   _safe_get_text("section_heritage_title", lang),
        "content": content,
        "type":    "heritage",
    }


# ---------------------------------------------------------------------------
# Dual section builders
# ---------------------------------------------------------------------------

def _build_dual_encounters(y_data: Dict, mt_data: Dict, lang: str, style: Dict) -> Dict:
    y_regions      = set(y_data.get("regions", []))
    mt_regions     = set(mt_data.get("regions", []))
    shared_regions = sorted(y_regions & mt_regions)

    try:
        content = style["dual_encounters_section"].format(
            y=y_data.get("haplogroup", ""),
            mt=mt_data.get("haplogroup", ""),
            regions=format_sources_list(shared_regions, lang=lang)
                    if shared_regions
                    else _safe_get_text("no_shared_regions", lang),
        )
    except KeyError as e:
        logger.warning(f"dual_encounters_section template missing key {e}")
        content = ""

    return {
        "id":             "dual_encounters",
        "title":          _safe_get_text("section_dual_encounters_title", lang),
        "content":        content,
        "shared_regions": shared_regions,
        "type":           "dual_encounters",
    }


def _build_dual_love_story(y_data: Dict, mt_data: Dict, lang: str, style: Dict) -> Dict:
    try:
        content = style["dual_love_story_section"].format(
            y=y_data.get("haplogroup", ""),
            mt=mt_data.get("haplogroup", ""),
        )
    except KeyError as e:
        logger.warning(f"dual_love_story_section template missing key {e}")
        content = ""

    return {
        "id":      "dual_love_story",
        "title":   _safe_get_text("section_dual_love_story_title", lang),
        "content": content,
        "type":    "dual_love_story",
    }


def _build_dual_heritage(y_data: Dict, mt_data: Dict, lang: str, style: Dict) -> Dict:
    try:
        content = style["dual_heritage_section"].format(
            y=y_data.get("haplogroup", ""),
            mt=mt_data.get("haplogroup", ""),
        )
    except KeyError as e:
        logger.warning(f"dual_heritage_section template missing key {e}")
        content = ""

    return {
        "id":      "dual_heritage",
        "title":   _safe_get_text("section_dual_heritage_title", lang),
        "content": content,
        "type":    "dual_heritage",
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _safe_get_text(key: str, lang: str, **kwargs) -> str:
    """
    get_text() kutsutaan suojattuna — jos käännösavain puuttuu,
    palautetaan avain itse virheen sijaan jotta renderöinti ei kaadu.
    """
    try:
        return get_text(key, lang=lang, **kwargs)
    except KeyError:
        logger.debug(f"Missing i18n key: '{key}' for lang '{lang}'")
        return key


def _parse_date_for_sort(date_str: str) -> int:
    """
    Muuntaa arkeologisen päivämäärän kokonaisluvuksi lajittelua varten.
    Tukee muotoja:
      "-26500"           → -26500
      "26500 BCE"        → -26500
      "3941-3661 BCE"    → -3941  (ottaa vanhemman pään)
      "8800–7000 eaa."   → -8800  (en-dash)
      "400 CE" / "400 JAA" → 400
      pelkkä kokonaisluku → sellaisenaan
    Negatiivinen arvo = BCE = vanhempi.
    """
    import re as _re
    s = str(date_str).strip().upper()
    # Normalisoi eri viivatyypit
    s = s.replace("–", "-").replace("—", "-").replace("–", "-").replace("—", "-")

    is_bce = any(tok in s for tok in ("BCE", "BC", "EAA", "V.T.", "V.KR."))
    is_ce  = any(tok in s for tok in ("CE", "AD", "JAA"))

    # Aikaväli "NNNN-NNNN …" → ota ensimmäinen (vanhempi) luku
    range_match = _re.match(r"^(\d+)-\d+", s)
    if range_match:
        s = range_match.group(1)

    digits = "".join(c for c in s if c.isdigit())
    try:
        val = int(digits) if digits else 0
    except ValueError:
        return 0

    if is_bce:
        return -val
    elif is_ce:
        return val
    else:
        # Suoraan negatiivisena annettu (esim. "-26500")
        if str(date_str).strip().startswith("-"):
            return -val
        return val


def render_story_as_text(story: Dict, lang: str = "en") -> str:
    """
    Kehittäjätyökalu: muuntaa tarinapaketin luettavaksi tekstiksi.
    Ei tarkoitettu tuotantokäyttöön — pdf_utils ja html_utils
    käyttävät rakennetta suoraan.
    """
    lines = []
    lines.append(f"# {story.get('title', '')}")
    lines.append(f"## {story.get('subtitle', '')}")

    hook = story.get("hook", "")
    if hook:
        lines.append(f"\n{hook}\n")

    for section in story.get("sections", []):
        s_type   = section.get("type", "")
        s_title  = section.get("title", "")
        s_content = section.get("content", "")

        if s_type == "nested_story":
            lines.append(f"\n## {s_title}")
            for sub in (s_content if isinstance(s_content, list) else []):
                lines.append(f"  ### {sub.get('title', '')}")
                lines.append(f"  {sub.get('content', '')[:200]}...")
        else:
            lines.append(f"\n### {s_title}")
            if s_content:
                lines.append(s_content[:500] + ("..." if len(s_content) > 500 else ""))

        # Tieteellinen todiste episodioissa
        evidence = section.get("evidence")
        if evidence and evidence.get("references"):
            refs = evidence["references"]
            lines.append(f"\n  Lähteet: {', '.join(refs)}")

    return "\n".join(lines)
