import os
import smtplib
from email.message import EmailMessage
from typing import Optional
from i18n_utils import get_translation


# -----------------------------
# SMTP-asetukset
# -----------------------------

SMTP_SERVER = os.getenv("SMTP_SERVER", "mail.kshm.fi")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SENDER_NAME = os.getenv("SENDER_NAME", "Kadonneen Sukuhistorian Metsästäjä")


# -----------------------------
# Pääfunktio
# -----------------------------

def send_email_with_pdf(
    to_email: str,
    pdf_path: str,
    haplogroup: str,
    lang: str = "fi",
    user_name: Optional[str] = None,
) -> None:
    """
    Lähettää sähköpostin PDF-liitteellä käyttäjälle.
    """

    if not SMTP_EMAIL or not SMTP_PASSWORD:
        raise RuntimeError("SMTP_EMAIL tai SMTP_PASSWORD ei ole asetettu ympäristömuuttujissa.")

    subject = get_translation(lang, "email_subject").format(haplogroup=haplogroup)

    body_text = get_translation(lang, "email_body_text").format(
        haplogroup=haplogroup,
        user_name=user_name or "",
    )

    body_html = get_translation(lang, "email_body_html").format(
        haplogroup=haplogroup,
        user_name=user_name or "",
    )

    msg = EmailMessage()
    msg["From"] = f"{SENDER_NAME} <{SMTP_EMAIL}>"
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.set_content(body_text)
    msg.add_alternative(body_html, subtype="html")

    # Liite
    with open(pdf_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(pdf_path)

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename=file_name,
    )

    # Lähetys
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)
