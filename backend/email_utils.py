# email_utils.py

import smtplib
import os
from email.message import EmailMessage
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


def send_email_with_pdf(
    to_email: str,
    haplogroup: str,
    story_text: str,
    pdf_path: str,
    user_name: Optional[str] = None
):
    """
    Lähettää PDF-raportin liitteenä käyttäjälle.
    """

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    from_email = os.getenv("FROM_EMAIL", smtp_user)

    if not all([smtp_host, smtp_user, smtp_password]):
        raise RuntimeError("SMTP-asetuksia puuttuu ympäristömuuttujista.")

    msg = EmailMessage()
    msg["Subject"] = f"Raporttisi: Haploryhmä {haplogroup}"
    msg["From"] = f"Kadonneen Sukuhistorian Metsästäjä <{from_email}>"
    msg["To"] = to_email

    greeting_name = user_name or "sinä"

    text_content = f"""
Hei {greeting_name},

Raporttisi haploryhmästä {haplogroup} on valmis!

Liitteenä löydät PDF-kirjan, joka kertoo arkeogeneettisen tarinan
verilinjastasi — muinaisista ihmisistä, kulttuureista ja vaelluksista
aina nykypäivään saakka.

Jos sinulla on kysyttävää tai haluat jatkoraportteja,
ota rohkeasti yhteyttä: info@kshm.fi

Seikkailuterveisin,
Kadonneen Sukuhistorian Metsästäjä
"""

    html_content = f"""
    <html>
      <body style="font-family: Georgia, serif; background-color: #fdfaf3; color: #3b2f1a;">
        <div style="max-width: 600px; margin: auto; padding: 24px; border: 1px solid #e0cda9;">
          <h2 style="color: #6b4e16;">Hei {greeting_name},</h2>
          <p>
            Raporttisi haploryhmästä <strong>{haplogroup}</strong> on valmis!
          </p>
          <p>
            Liitteenä löydät PDF-kirjan, joka kertoo arkeogeneettisen tarinan
            verilinjastasi — muinaisista ihmisistä, kulttuureista ja vaelluksista
            aina nykypäivään saakka.
          </p>
          <p>
            Jos sinulla on kysyttävää tai haluat jatkoraportteja,
            ota rohkeasti yhteyttä:
            <a href="mailto:info@kshm.fi">info@kshm.fi</a>
          </p>
          <p style="margin-top: 32px;">
            Seikkailuterveisin,<br>
            <strong>Kadonneen Sukuhistorian Metsästäjä</strong>
          </p>
        </div>
      </body>
    </html>
    """

    msg.set_content(text_content)
    msg.add_alternative(html_content, subtype="html")

    # Attach PDF
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    filename = os.path.basename(pdf_path)
    msg.add_attachment(
        pdf_data,
        maintype="application",
        subtype="pdf",
        filename=filename
    )

    # Send email
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
