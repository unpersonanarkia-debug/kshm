import os
import smtplib
import ssl
from email.message import EmailMessage
from typing import Optional, Dict

from i18n_utils import get_translation


# -----------------------------
# SMTP-asetukset
# -----------------------------

SMTP_SERVER = os.getenv("SMTP_SERVER", "mail.kshm.fi")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_EMAIL = os.getenv("SMTP_EMAIL", "raportit@kshm.fi")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SENDER_NAME = os.getenv("SENDER_NAME", "Kadonneen Sukuhistorian Metsästäjä")


# -----------------------------
# Sisäinen lähetysfunktion ydin
# -----------------------------

def _send_email_message(msg: EmailMessage) -> bool:
    """
    Lähettää valmiin EmailMessage-olion SMTP:n kautta.
    """
    if not SMTP_EMAIL or not SMTP_PASSWORD:
        raise RuntimeError("SMTP_EMAIL tai SMTP_PASSWORD puuttuu ympäristömuuttujista.")

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Sähköpostin lähetys epäonnistui: {e}")
        return False


# -----------------------------
# Rungon rakentajat
# -----------------------------

def build_email_subject(haplogroup: str, lang: str) -> str:
    return get_translation(lang, "email_subject").format(haplogroup=haplogroup)


def build_email_body_text(
    haplogroup: str,
    lang: str,
    user_name: Optional[str] = None,
    is_dual: bool = False,
    mt_haplogroup: Optional[str] = None,
) -> str:
    key = "email_body_text_dual" if is_dual else "email_body_text"
    return get_translation(lang, key).format(
        haplogroup=haplogroup,
        mt_haplogroup=mt_haplogroup or "",
        user_name=user_name or "",
    )


def build_email_body_html(
    haplogroup: str,
    lang: str,
    user_name: Optional[str] = None,
    is_dual: bool = False,
    mt_haplogroup: Optional[str] = None,
) -> str:
    key = "email_body_html_dual" if is_dual else "email_body_html"
    return get_translation(lang, key).format(
        haplogroup=haplogroup,
        mt_haplogroup=mt_haplogroup or "",
        user_name=user_name or "",
    )


# -----------------------------
# Julkinen API
# -----------------------------

def send_email_with_pdf(
    to_email: str,
    pdf_path: str,
    haplogroup: str,
    lang: str = "fi",
    user_name: Optional[str] = None,
    is_dual: bool = False,
    mt_haplogroup: Optional[str] = None,
) -> bool:
    """
    Lähettää sähköpostin PDF-liitteellä käyttäjälle.
    Tukee myös kaksoishaploryhmäraporttia (Y-DNA + mtDNA).
    """

    subject = build_email_subject(haplogroup, lang)
    body_text = build_email_body_text(
        haplogroup, lang, user_name, is_dual=is_dual, mt_haplogroup=mt_haplogroup
    )
    body_html = build_email_body_html(
        haplogroup, lang, user_name, is_dual=is_dual, mt_haplogroup=mt_haplogroup
    )

    msg = EmailMessage()
    msg["From"] = f"{SENDER_NAME} <{SMTP_EMAIL}>"
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.set_content(body_text)
    msg.add_alternative(body_html, subtype="html")

    # Liitä PDF
    with open(pdf_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(pdf_path)

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename=file_name,
    )

    return _send_email_message(msg)


# -----------------------------
# Korkeamman tason integraatiot
# -----------------------------

def send_story_email_from_haplogroup(
    to_email: str,
    haplogroup: str,
    pdf_path: str,
    lang: str = "fi",
    tone: str = "academic",
    user_name: Optional[str] = None,
) -> bool:
    """
    Luo tarinan, PDF:n ja lähettää sähköpostin yhdellä kutsulla.
    """
    from story_utils import generate_story_from_haplogroup
    from pdf_utils import generate_pdf

    story = generate_story_from_haplogroup(haplogroup, lang=lang, tone=tone)
    generate_pdf(story, filename=pdf_path, lang=lang)

    return send_email_with_pdf(
        to_email=to_email,
        pdf_path=pdf_path,
        haplogroup=haplogroup,
        lang=lang,
        user_name=user_name,
    )


def send_dual_story_email_from_haplogroups(
    to_email: str,
    y_haplogroup: str,
    mt_haplogroup: str,
    pdf_path: str,
    lang: str = "fi",
    tone: str = "academic",
    user_name: Optional[str] = None,
) -> bool:
    """
    Luo yhdistetyn Y-DNA + mtDNA -tarinan, PDF:n ja lähettää sähköpostin.
    """

    from story_utils import generate_dual_story_from_haplogroups
    from pdf_utils import generate_pdf

    story = generate_dual_story_from_haplogroups(y_haplogroup, mt_haplogroup, lang=lang, tone=tone)
    generate_pdf(story, filename=pdf_path, lang=lang)

    return send_email_with_pdf(
        to_email=to_email,
        pdf_path=pdf_path,
        haplogroup=y_haplogroup,
        lang=lang,
        user_name=user_name,
        is_dual=True,
        mt_haplogroup=mt_haplogroup,
    )
