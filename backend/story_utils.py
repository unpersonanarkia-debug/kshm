# story_utils.py

from typing import Dict, List, Optional
from datetime import datetime


# ===============================
# Entry point
# ===============================

def generate_story(
    haplo_data: Dict,
    user_name: str,
    style: str = "chronological",
    language: str = "fi",
    notes: Optional[str] = None
) -> str:
    """
    Luo haploryhmään perustuvan arkeogeneettisen kertomuksen.
    Kerrontatyyli voi olla: chronological, scientific, narrative, documentary, poetic.
    """

    style = style.lower()

    if style == "scientific":
        return generate_scientific_story(haplo_data, user_name, language, notes)
    elif style == "narrative":
        return generate_narrative_story(haplo_data, user_name, language, notes)
    elif style == "documentary":
        return generate_documentary_story(haplo_data, user_name, language, notes)
    elif style == "poetic":
        return generate_poetic_story(haplo_data, user_name, language, notes)
    else:
        return generate_chronological_story(haplo_data, user_name, language, notes)


# ===============================
# Core: Chronological archaeogenetic story
# ===============================

def generate_chronological_story(
    haplo_data: Dict,
    user_name: str,
    language: str = "fi",
    notes: Optional[str] = None
) -> str:
    """
    Rakentaa kronologisen kertomuksen arkeologisten löytöjen ja populaatioliikkeiden mukaan.
    """

    haplogroup = haplo_data.get("haplogroup", "tuntematon haploryhmä")
    lineage_type = haplo_data.get("lineage_type", "")
    regions = haplo_data.get("regions", [])
    ancient_samples = haplo_data.get("ancient_samples", [])
    time_depth = haplo_data.get("time_depth", "")
    regional_profiles = haplo_data.get("regional_profiles", [])

    story_sections: List[str] = []

    story_sections.append(build_intro_section(haplogroup, lineage_type, user_name, time_depth, language))

    story_sections.append(build_origins_section(haplogroup, regions, ancient_samples, language))

    story_sections.append(build_migration_section(haplogroup, regions, ancient_samples, language))

    story_sections.append(build_cultural_section(haplogroup, regional_profiles, language))

    story_sections.append(build_modern_distribution_section(haplogroup, regions, language))

    story_sections.append(build_conclusion_section(haplogroup, user_name, language))

    if notes:
        story_sections.append(build_user_notes_section(notes, language))

    return "\n\n".join(story_sections)


# ===============================
# Alternative narrative styles
# ===============================

def generate_scientific_story(haplo_data: Dict, user_name: str, language: str, notes: Optional[str]) -> str:
    haplogroup = haplo_data.get("haplogroup", "tuntematon haploryhmä")
    lineage_type = haplo_data.get("lineage_type", "")
    regions = haplo_data.get("regions", [])
    time_depth = haplo_data.get("time_depth", "")

    text = (
        f"Arkeogeneettinen analyysi haploryhmästä {haplogroup} ({lineage_type}) osoittaa sen "
        f"syvän aikajänteen, joka ulottuu {time_depth} taakse. Tämä raportti kokoaa yhteen "
        f"useista akateemisista ja geneettisistä lähteistä peräisin olevan datan, jonka avulla "
        f"voidaan rekonstruoida haploryhmän esi-isien liikkeet, populaatiorakenteet ja "
        f"maantieteelliset jakautumat.\n\n"
        f"Analyysin kohteena ovat erityisesti seuraavat alueet: {', '.join(regions)}. "
        f"Näiltä alueilta peräisin olevat muinaisnäytteet ja nykyväestön geneettinen variaatio "
        f"osoittavat haploryhmän liittyneen useisiin merkittäviin kulttuurisiin ja "
        f"demografisiin murrosvaiheisiin."
    )

    if notes:
        text += f"\n\nLisähuomiot: {notes}"

    return text


def generate_narrative_story(haplo_data: Dict, user_name: str, language: str, notes: Optional[str]) -> str:
    haplogroup = haplo_data.get("haplogroup", "tuntematon haploryhmä")
    regions = haplo_data.get("regions", [])
    time_depth = haplo_data.get("time_depth", "")

    text = (
        f"{user_name}, haploryhmäsi {haplogroup} ei ole vain geneettinen merkintä – "
        f"se on pitkä kertomus ihmisistä, jotka kulkivat halki mantereiden, "
        f"etsivät uusia asuinpaikkoja ja loivat kulttuureja kauan ennen kirjallista historiaa.\n\n"
        f"Tämä tarina alkaa ajasta, jolloin ihmiskunta vielä vaelsi varhaisissa yhteisöissä, "
        f"{time_depth} sitten. Sukulinjasi kulki alueiden kuten {', '.join(regions)} kautta, "
        f"jättäen jälkensä muinaisiin yhteisöihin ja lopulta nykypäivään – sinuun."
    )

    if notes:
        text += f"\n\n{notes}"

    return text


def generate_documentary_story(haplo_data: Dict, user_name: str, language: str, notes: Optional[str]) -> str:
    haplogroup = haplo_data.get("haplogroup", "tuntematon haploryhmä")
    regions = haplo_data.get("regions", [])
    time_depth = haplo_data.get("time_depth", "")

    text = (
        f"Dokumentaarinen katsaus haploryhmään {haplogroup} ({user_name}).\n\n"
        f"Tutkimus osoittaa, että haploryhmän juuret ulottuvat {time_depth} taakse. "
        f"Muinais-DNA-näytteet ja nykyväestön geneettinen data osoittavat haploryhmän "
        f"esiintymistä erityisesti seuraavilla alueilla: {', '.join(regions)}.\n\n"
        f"Nämä löydöt mahdollistavat yksityiskohtaisen rekonstruktion haploryhmän "
        f"populaatiohistoriasta, kulttuurisista yhteyksistä ja leviämisreiteistä."
    )

    if notes:
        text += f"\n\nLisäkommentit: {notes}"

    return text


def generate_poetic_story(haplo_data: Dict, user_name: str, language: str, notes: Optional[str]) -> str:
    haplogroup = haplo_data.get("haplogroup", "tuntematon haploryhmä")
    regions = haplo_data.get("regions", [])
    time_depth = haplo_data.get("time_depth", "")

    text = (
        f"Sinun veressäsi kulkee muinainen virta — haploryhmä {haplogroup}.\n"
        f"Se syntyi {time_depth} sitten, kaukana varhaisissa ihmisyhteisöissä,\n"
        f"ja kulki halki maiden: {', '.join(regions)}.\n\n"
        f"Jokainen askel, jokainen siirtymä, jokainen koti,\n"
        f"on piirtynyt sinuun, {user_name},\n"
        f"niin kuin kartta, jota kannat mukanasi."
    )

    if notes:
        text += f"\n\n{notes}"

    return text


# ===============================
# Section builders (chronological core)
# ===============================

def build_intro_section(haplogroup: str, lineage_type: str, user_name: str, time_depth: str, language: str) -> str:
    return (
        f"📜 **Arkeogeneettinen kertomus haploryhmästä {haplogroup}**\n\n"
        f"Tämä raportti käsittelee haploryhmää {haplogroup} ({lineage_type}) ja sen "
        f"arkeogeneettistä historiaa. Sukulinjasi juuret ulottuvat jopa {time_depth} taakse, "
        f"ja se kytkeytyy ihmiskunnan varhaisimpien populaatioiden liikkeisiin.\n\n"
        f"Raportti on laadittu käyttäen useita kansainvälisiä arkeogeneettisiä ja "
        f"genomisia lähteitä, ja se esitetään kronologisena kokonaisuutena, "
        f"perustuen todettuihin muinais-DNA-löytöihin ja väestöhistoriallisiin malleihin."
    )


def build_origins_section(haplogroup: str, regions: List[str], ancient_samples: List[Dict], language: str) -> str:
    if ancient_samples:
        sample_text = "Muinaisnäytteet osoittavat varhaisia esiintymiä seuraavilla alueilla:\n"
        for s in ancient_samples:
            sample_text += f"- {s.get('location', 'tuntematon paikka')}, ajoitus: {s.get('date', 'tuntematon aika')}\n"
    else:
        sample_text = (
            "Vaikka suoria muinaisnäytteitä ei ole vielä liitetty yksiselitteisesti tähän haploryhmään, "
            "geneettinen mallinnus ja populaatiodynamiikka osoittavat sen varhaisimmat juuret seuraaville alueille:\n"
        )
        for region in regions[:5]:
            sample_text += f"- {region}\n"

    return (
        f"🧬 **Varhaisimmat juuret**\n\n"
        f"Haploryhmä {haplogroup} syntyi varhaisissa ihmisyhteisöissä, joiden sijainti voidaan "
        f"rekonstruoida geneettisten ja arkeologisten todisteiden perusteella.\n\n"
        f"{sample_text}"
    )


def build_migration_section(haplogroup: str, regions: List[str], ancient_samples: List[Dict], language: str) -> str:
    region_sequence = " → ".join(regions[:8]) if regions else "useiden alueiden kautta"

    return (
        f"🌍 **Leviämisreitit ja väestöliikkeet**\n\n"
        f"Haploryhmä {haplogroup} ei pysynyt paikallaan. Sen kantajat osallistuivat useisiin "
        f"merkittäviin väestöliikkeisiin, jotka muokkasivat maailman demografiaa.\n\n"
        f"Kronologisesti rekonstruoituna linja kulki seuraavaa reittiä:\n"
        f"{region_sequence}\n\n"
        f"Nämä liikkeet liittyivät muun muassa ilmastonmuutoksiin, teknologisiin murroksiin, "
        f"maanviljelyn syntyyn, paimentolaisuuteen ja merenkulun kehittymiseen."
    )


def build_cultural_section(haplogroup: str, regional_profiles: List[Dict], language: str) -> str:
    if not regional_profiles:
        return (
            f"🏺 **Kulttuuriset yhteydet**\n\n"
            f"Haploryhmän {haplogroup} kantajat osallistuivat useisiin tunnetuihin ja tuntemattomiin "
            f"kulttuurimuodostelmiin, vaikka yksityiskohtaisia aluekohtaisia profiileja ei ole vielä saatavilla."
        )

    culture_text = ""
    for profile in regional_profiles:
        culture_text += (
            f"- *{profile.get('region')}*: {profile.get('notes', '')}. "
            f"Käytetyt analyysimenetelmät: {', '.join(profile.get('tools', []))}.\n"
        )

    return (
        f"🏺 **Kulttuuriset ja arkeologiset yhteydet**\n\n"
        f"Haploryhmä {haplogroup} on yhdistetty useisiin alueellisiin kulttuureihin ja "
        f"arkeologisiin kokonaisuuksiin seuraavasti:\n\n"
        f"{culture_text}"
    )


def build_modern_distribution_section(haplogroup: str, regions: List[str], language: str) -> str:
    region_list = ", ".join(regions) if regions else "useilla eri mantereilla"

    return (
        f"🧭 **Nykyinen levinneisyys**\n\n"
        f"Tänä päivänä haploryhmää {haplogroup} esiintyy laajasti seuraavilla alueilla: "
        f"{region_list}.\n\n"
        f"Nykyaikaiset geenitutkimukset, kuluttajatestit ja akateemiset projektit "
        f"mahdollistavat yksityiskohtaisen vertailun muinais- ja nykyväestöjen välillä."
    )


def build_conclusion_section(haplogroup: str, user_name: str, language: str) -> str:
    return (
        f"🔚 **Yhteenveto**\n\n"
        f"Haploryhmä {haplogroup} edustaa yhtä monista ihmiskunnan pitkäkestoisista "
        f"sukulinjoista. Sen historia on kudelma vaelluksia, sopeutumista ja kulttuurista "
        f"jatkuvuutta.\n\n"
        f"Tämä raportti yhdistää sinut, {user_name}, osaksi tätä laajaa arkeogeneettistä "
        f"kertomusta — ei symbolisesti, vaan geneettisesti."
    )


def build_user_notes_section(notes: str, language: str) -> str:
    return (
        f"📝 **Käyttäjän lisähuomiot**\n\n"
        f"{notes}"
    )
