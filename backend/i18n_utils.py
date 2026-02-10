from typing import Dict, Optional

# ----------------------------------
# Konfiguraatio
# ----------------------------------

SUPPORTED_LANGUAGES = ["fi", "en", "sv", "de"]
DEFAULT_LANG = "en"
SUPPORTED_TONES = ["academic", "narrative", "popular"]
DEFAULT_TONE = "academic"


# ----------------------------------
# Käännökset ja tekstipohjat
# ----------------------------------

TRANSLATIONS: Dict[str, Dict[str, Dict[str, str]]] = {

    # -------------------------------
    # Yleiset otsikot
    # -------------------------------

    "haplogroup_title": {
        "academic": {
            "fi": "Haploryhmä {haplogroup}",
            "en": "Haplogroup {haplogroup}",
            "sv": "Haplogrupp {haplogroup}",
            "de": "Haplogruppe {haplogroup}",
        },
        "narrative": {
            "fi": "Tarina haploryhmästä {haplogroup}",
            "en": "The Story of Haplogroup {haplogroup}",
            "sv": "Berättelsen om haplogrupp {haplogroup}",
            "de": "Die Geschichte der Haplogruppe {haplogroup}",
        },
        "popular": {
            "fi": "Sinun haploryhmäsi: {haplogroup}",
            "en": "Your Haplogroup: {haplogroup}",
            "sv": "Din haplogrupp: {haplogroup}",
            "de": "Ihre Haplogruppe: {haplogroup}",
        },
    },

    "description_intro": {
        "academic": {
            "fi": "Tieteellinen yleiskuva haploryhmästä.",
            "en": "Scientific overview of the haplogroup.",
            "sv": "Vetenskaplig översikt av haplogruppen.",
            "de": "Wissenschaftlicher Überblick über die Haplogruppe.",
        },
        "narrative": {
            "fi": "Tämä on tarina ihmisistä, jotka kantoivat tätä haploryhmää vuosituhansien ajan.",
            "en": "This is the story of people who carried this haplogroup across millennia.",
            "sv": "Detta är berättelsen om människor som bar denna haplogrupp genom årtusenden.",
            "de": "Dies ist die Geschichte der Menschen, die diese Haplogruppe über Jahrtausende trugen.",
        },
        "popular": {
            "fi": "Lyhyt ja helposti ymmärrettävä yhteenveto haploryhmästäsi.",
            "en": "A short and easy-to-understand summary of your haplogroup.",
            "sv": "En kort och lättförståelig sammanfattning av din haplogrupp.",
            "de": "Eine kurze und leicht verständliche Zusammenfassung Ihrer Haplogruppe.",
        },
    },

    "regions_label": {
        "academic": {
            "fi": "Maantieteellinen levinneisyys",
            "en": "Geographic distribution",
            "sv": "Geografisk spridning",
            "de": "Geografische Verbreitung",
        },
        "narrative": {
            "fi": "Matka halki maanosien",
            "en": "A journey across continents",
            "sv": "En resa över kontinenter",
            "de": "Eine Reise über Kontinente",
        },
        "popular": {
            "fi": "Missä tätä haploryhmää tavataan",
            "en": "Where this haplogroup is found",
            "sv": "Var denna haplogrupp finns",
            "de": "Wo diese Haplogruppe vorkommt",
        },
    },

    "time_depth_label": {
        "academic": {
            "fi": "Ajallinen syvyys",
            "en": "Time depth",
            "sv": "Tidsdjup",
            "de": "Zeitliche Tiefe",
        },
        "narrative": {
            "fi": "Aikamatka menneisyyteen",
            "en": "A journey back in time",
            "sv": "En resa tillbaka i tiden",
            "de": "Eine Reise in die Vergangenheit",
        },
        "popular": {
            "fi": "Kuinka vanha tämä haploryhmä on",
            "en": "How old this haplogroup is",
            "sv": "Hur gammal denna haplogrupp är",
            "de": "Wie alt diese Haplogruppe ist",
        },
    },

    "ancient_samples_label": {
        "academic": {
            "fi": "Muinaisnäytteet",
            "en": "Ancient samples",
            "sv": "Fornprover",
            "de": "Antike Proben",
        },
        "narrative": {
            "fi": "Muinaiset jäljet ihmisistä",
            "en": "Ancient traces of people",
            "sv": "Fornspår av människor",
            "de": "Antike Spuren von Menschen",
        },
        "popular": {
            "fi": "Vanhimmat löydöt",
            "en": "Oldest findings",
            "sv": "Äldsta fynden",
            "de": "Älteste Funde",
        },
    },

    "sources_label": {
        "academic": {
            "fi": "Lähteet",
            "en": "Sources",
            "sv": "Källor",
            "de": "Quellen",
        },
        "narrative": {
            "fi": "Tutkimukset ja kertomukset",
            "en": "Studies and narratives",
            "sv": "Studier och berättelser",
            "de": "Studien und Erzählungen",
        },
        "popular": {
            "fi": "Mistä tieto on peräisin",
            "en": "Where this information comes from",
            "sv": "Var informationen kommer ifrån",
            "de": "Woher diese Informationen stammen",
        },
    },

    # -------------------------------
    # PDF-tekstit
    # -------------------------------

    "pdf_title": {
        "academic": {
            "fi": "Haploryhmäraportti: {haplogroup}",
            "en": "Haplogroup Report: {haplogroup}",
            "sv": "Haplogruppsrapport: {haplogroup}",
            "de": "Haplogruppenbericht: {haplogroup}",
        },
        "narrative": {
            "fi": "Sukulinjan tarina: {haplogroup}",
            "en": "The Story of Your Lineage: {haplogroup}",
            "sv": "Berättelsen om din släktlinje: {haplogroup}",
            "de": "Die Geschichte Ihrer Abstammung: {haplogroup}",
        },
        "popular": {
            "fi": "Sinun haploryhmäraporttisi: {haplogroup}",
            "en": "Your Haplogroup Report: {haplogroup}",
            "sv": "Din haplogruppsrapport: {haplogroup}",
            "de": "Ihr Haplogruppenbericht: {haplogroup}",
        },
    },

    "pdf_footer": {
        "academic": {
            "fi": "Luotu automaattisesti arkeogeneettisestä tietokannasta.",
            "en": "Automatically generated from archaeogenetic databases.",
            "sv": "Automatiskt genererad från arkeogenetiska databaser.",
            "de": "Automatisch generiert aus archäogenetischen Datenbanken.",
        },
        "narrative": {
            "fi": "Luotu menneisyyden tarinoita varten.",
            "en": "Created to tell stories of the past.",
            "sv": "Skapad för att berätta det förflutnas historier.",
            "de": "Erstellt, um Geschichten der Vergangenheit zu erzählen.",
        },
        "popular": {
            "fi": "Raportti on luotu automaattisesti.",
            "en": "This report was generated automatically.",
            "sv": "Denna rapport skapades automatiskt.",
            "de": "Dieser Bericht wurde automatisch erstellt.",
        },
    },

    # -------------------------------
    # Sähköposti
    # -------------------------------

    "email_subject": {
        "academic": {
            "fi": "Haploryhmäraportti – {haplogroup}",
            "en": "Haplogroup Report – {haplogroup}",
            "sv": "Haplogruppsrapport – {haplogroup}",
            "de": "Haplogruppenbericht – {haplogroup}",
        },
        "narrative": {
            "fi": "Tarina sukulinjastasi – {haplogroup}",
            "en": "The Story of Your Lineage – {haplogroup}",
            "sv": "Berättelsen om din släktlinje – {haplogroup}",
            "de": "Die Geschichte Ihrer Abstammung – {haplogroup}",
        },
        "popular": {
            "fi": "Sinun haploryhmäraporttisi – {haplogroup}",
            "en": "Your Haplogroup Report – {haplogroup}",
            "sv": "Din haplogruppsrapport – {haplogroup}",
            "de": "Ihr Haplogruppenbericht – {haplogroup}",
        },
    },

    "email_body_text": {
        "academic": {
            "fi": "Hei {user_name},\n\nLiitteenä on tieteellinen haploryhmäraporttisi ({haplogroup}).\n\nYstävällisin terveisin,\nKadonneen Sukuhistorian Metsästäjä",
            "en": "Hello {user_name},\n\nAttached is your scientific haplogroup report ({haplogroup}).\n\nKind regards,\nKadonneen Sukuhistorian Metsästäjä",
            "sv": "Hej {user_name},\n\nBifogat finns din vetenskapliga haplogruppsrapport ({haplogroup}).\n\nVänliga hälsningar,\nKadonneen Sukuhistorian Metsästäjä",
            "de": "Hallo {user_name},\n\nIm Anhang finden Sie Ihren wissenschaftlichen Haplogruppenbericht ({haplogroup}).\n\nMit freundlichen Grüßen,\nKadonneen Sukuhistorian Metsästäjä",
        },
        "narrative": {
            "fi": "Hei {user_name},\n\nLiitteenä on sukulinjasi tarina haploryhmästä {haplogroup}.\n\nLämpimin terveisin,\nKadonneen Sukuhistorian Metsästäjä",
            "en": "Hello {user_name},\n\nAttached is the story of your lineage through haplogroup {haplogroup}.\n\nWarm regards,\nKadonneen Sukuhistorian Metsästäjä",
            "sv": "Hej {user_name},\n\nBifogat finns berättelsen om din släktlinje genom haplogrupp {haplogroup}.\n\nVänliga hälsningar,\nKadonneen Sukuhistorian Metsästäjä",
            "de": "Hallo {user_name},\n\nIm Anhang finden Sie die Geschichte Ihrer Abstammung über Haplogruppe {haplogroup}.\n\nMit freundlichen Grüßen,\nKadonneen Sukuhistorian Metsästäjä",
        },
        "popular": {
            "fi": "Hei {user_name},\n\nTässä on henkilökohtainen haploryhmäraporttisi ({haplogroup}).\n\nTerveisin,\nKadonneen Sukuhistorian Metsästäjä",
            "en": "Hello {user_name},\n\nHere is your personal haplogroup report ({haplogroup}).\n\nBest regards,\nKadonneen Sukuhistorian Metsästäjä",
            "sv": "Hej {user_name},\n\nHär är din personliga haplogruppsrapport ({haplogroup}).\n\nVänliga hälsningar,\nKadonneen Sukuhistorian Metsästäjä",
            "de": "Hallo {user_name},\n\nHier ist Ihr persönlicher Haplogruppenbericht ({haplogroup}).\n\nMit freundlichen Grüßen,\nKadonneen Sukuhistorian Metsästäjä",
        },
    },

    "email_body_html": {
        "academic": {
            "fi": "<p>Hei {user_name},</p><p>Liitteenä on tieteellinen haploryhmäraporttisi (<strong>{haplogroup}</strong>).</p><p>Ystävällisin terveisin,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
            "en": "<p>Hello {user_name},</p><p>Attached is your scientific haplogroup report (<strong>{haplogroup}</strong>).</p><p>Kind regards,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
            "sv": "<p>Hej {user_name},</p><p>Bifogat finns din vetenskapliga haplogruppsrapport (<strong>{haplogroup}</strong>).</p><p>Vänliga hälsningar,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
            "de": "<p>Hallo {user_name},</p><p>Im Anhang finden Sie Ihren wissenschaftlichen Haplogruppenbericht (<strong>{haplogroup}</strong>).</p><p>Mit freundlichen Grüßen,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
        },
        "narrative": {
            "fi": "<p>Hei {user_name},</p><p>Liitteenä on sukulinjasi tarina haploryhmästä <strong>{haplogroup}</strong>.</p><p>Lämpimin terveisin,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
            "en": "<p>Hello {user_name},</p><p>Attached is the story of your lineage through haplogroup <strong>{haplogroup}</strong>.</p><p>Warm regards,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
            "sv": "<p>Hej {user_name},</p><p>Bifogat finns berättelsen om din släktlinje genom haplogrupp <strong>{haplogroup}</strong>.</p><p>Vänliga hälsningar,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
            "de": "<p>Hallo {user_name},</p><p>Im Anhang finden Sie die Geschichte Ihrer Abstammung über Haplogruppe <strong>{haplogroup}</strong>.</p><p>Mit freundlichen Grüßen,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
        },
        "popular": {
            "fi": "<p>Hei {user_name},</p><p>Tässä on henkilökohtainen haploryhmäraporttisi (<strong>{haplogroup}</strong>).</p><p>Terveisin,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
            "en": "<p>Hello {user_name},</p><p>Here is your personal haplogroup report (<strong>{haplogroup}</strong>).</p><p>Best regards,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
            "sv": "<p>Hej {user_name},</p><p>Här är din personliga haplogruppsrapport (<strong>{haplogroup}</strong>).</p><p>Vänliga hälsningar,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
            "de": "<p>Hallo {user_name},</p><p>Hier ist Ihr persönlicher Haplogruppenbericht (<strong>{haplogroup}</strong>).</p><p>Mit freundlichen Grüßen,<br><strong>Kadonneen Sukuhistorian Metsästäjä</strong></p>",
        },
    },

    # -------------------------------
    # Virheilmoitukset ja käyttö
    # -------------------------------

    "error_invalid_haplogroup": {
        "academic": {
            "fi": "Virheellinen haploryhmämuoto: {haplogroup}",
            "en": "Invalid haplogroup format: {haplogroup}",
            "sv": "Ogiltigt haplogruppsformat: {haplogroup}",
            "de": "Ungültiges Haplogruppenformat: {haplogroup}",
        },
        "narrative": {
            "fi": "Annettu haploryhmä ei vastaa tunnettuja muotoja: {haplogroup}",
            "en": "The given haplogroup does not match known formats: {haplogroup}",
            "sv": "Den angivna haplogruppen matchar inte kända format: {haplogroup}",
            "de": "Die angegebene Haplogruppe entspricht keinen bekannten Formaten: {haplogroup}",
        },
        "popular": {
            "fi": "Tämä ei näytä oikealta haploryhmältä: {haplogroup}",
            "en": "This doesn’t look like a valid haplogroup: {haplogroup}",
            "sv": "Detta ser inte ut som en giltig haplogrupp: {haplogroup}",
            "de": "Dies sieht nicht wie eine gültige Haplogruppe aus: {haplogroup}",
        },
    },

    "error_internal": {
        "academic": {
            "fi": "Sisäinen järjestelmävirhe.",
            "en": "Internal system error.",
            "sv": "Internt systemfel.",
            "de": "Interner Systemfehler.",
        },
        "narrative": {
            "fi": "Järjestelmässä tapahtui odottamaton virhe.",
            "en": "An unexpected error occurred in the system.",
            "sv": "Ett oväntat fel inträffade i systemet.",
            "de": "Im System ist ein unerwarteter Fehler aufgetreten.",
        },
        "popular": {
            "fi": "Jokin meni pieleen. Yritä uudelleen.",
            "en": "Something went wrong. Please try again.",
            "sv": "Något gick fel. Försök igen.",
            "de": "Etwas ist schiefgelaufen. Bitte versuchen Sie es erneut.",
        },
    },
}


# ----------------------------------
# API-funktiot
# ----------------------------------

def get_translation(
    lang: str,
    key: str,
    tone: str = DEFAULT_TONE,
    fallback_lang: Optional[str] = DEFAULT_LANG,
    **kwargs,
) -> str:
    """
    Palauttaa lokalisoidun ja sävytetyn tekstin.
    Automaattinen fallback ensisijaisesti englantiin.
    """
    lang = lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANG
    tone = tone if tone in SUPPORTED_TONES else DEFAULT_TONE

    entry = TRANSLATIONS.get(key, {})
    tone_entry = entry.get(tone, {})

    text = tone_entry.get(lang)

    if not text and fallback_lang:
        text = tone_entry.get(fallback_lang)

    if not text:
        text = key  # fallback viime kädessä avain

    if kwargs:
        try:
            return text.format(**kwargs)
        except KeyError:
            return text  # Palauta raakateksti jos muotoilu epäonnistuu

    return text


def is_language_supported(lang: str) -> bool:
    return lang in SUPPORTED_LANGUAGES


def is_tone_supported(tone: str) -> bool:
    return tone in SUPPORTED_TONES


def list_supported_languages() -> list:
    return SUPPORTED_LANGUAGES


def list_supported_tones() -> list:
    return SUPPORTED_TONES
