# i18n_utils.py

from typing import Dict

SUPPORTED_LANGUAGES = {
    "fi": "Suomi",
    "en": "English",
    "sv": "Svenska",
    "de": "Deutsch",
    "fr": "Français",
    "es": "Español",
    "pt": "Português",
    "it": "Italiano",
}

DEFAULT_LANGUAGE = "fi"

TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "fi": {
        "report_title": "Arkeogeneettinen haploryhmäraportti",
        "intro": "Hei {name}, tässä on henkilökohtainen raporttisi haploryhmästä {haplogroup}.",
        "sections.origin": "Alkuperä ja leviämishistoria",
        "sections.samples": "Muinaiset näytteet",
        "sections.regions": "Maantieteellinen levinneisyys",
        "sections.time_depth": "Ajoitus ja ikä",
        "sections.tools": "Analyysityökalut",
        "sections.raw_data": "Raakadatan lähteet",
        "email.subject": "Henkilökohtainen haploryhmäraporttisi",
        "email.body": "Hei {name},\n\nLiitteenä on henkilökohtainen arkeogeneettinen raporttisi haploryhmästä {haplogroup}.\n\nYstävällisin terveisin,\nKadonneen Sukuhistorian Metsästäjä",
    },
    "en": {
        "report_title": "Archaeogenetic Haplogroup Report",
        "intro": "Hello {name}, here is your personalized report for haplogroup {haplogroup}.",
        "sections.origin": "Origins and Migration History",
        "sections.samples": "Ancient Samples",
        "sections.regions": "Geographic Distribution",
        "sections.time_depth": "Chronology and Age",
        "sections.tools": "Analysis Tools",
        "sections.raw_data": "Raw Data Providers",
        "email.subject": "Your Personal Haplogroup Report",
        "email.body": "Hello {name},\n\nAttached is your personal archaeogenetic report for haplogroup {haplogroup}.\n\nBest regards,\nThe Lost Ancestry Hunter",
    },
    "es": {
        "report_title": "Informe Arqueogenético del Haplogrupo",
        "intro": "Hola {name}, aquí está tu informe personalizado del haplogrupo {haplogroup}.",
        "sections.origin": "Origen e historia de migración",
        "sections.samples": "Muestras antiguas",
        "sections.regions": "Distribución geográfica",
        "sections.time_depth": "Cronología y antigüedad",
        "sections.tools": "Herramientas de análisis",
        "sections.raw_data": "Proveedores de datos en bruto",
        "email.subject": "Tu informe personal de haplogrupo",
        "email.body": "Hola {name},\n\nAdjunto encontrarás tu informe arqueogenético personal del haplogrupo {haplogroup}.\n\nSaludos cordiales,\nEl Cazador de la Historia Perdida",
    },
    # Lisää kieliä helposti tähän
}


def get_supported_languages():
    return SUPPORTED_LANGUAGES


def translate(key: str, lang: str = DEFAULT_LANGUAGE, **kwargs) -> str:
    lang = lang if lang in TRANSLATIONS else DEFAULT_LANGUAGE
    text = TRANSLATIONS.get(lang, {}).get(key)

    if not text:
        # fallback englantiin
        text = TRANSLATIONS.get("en", {}).get(key, key)

    try:
        return text.format(**kwargs)
    except Exception:
        return text
