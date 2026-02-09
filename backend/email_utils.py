import os
import smtplib
from email.message import EmailMessage
from typing import Optional

SMTP_SERVER = os.getenv("SMTP_SERVER", "mail.kshm.fi")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")


def send_email_with_pdf(
    to_email: str,
    haplogroup: str,
    html_body: str,
    pdf_path: str,
    user_name: Optional[str] = None
):
    if not SMTP_EMAIL or not SMTP_PASSWORD:
        raise RuntimeError("SMTP credentials not configured.")

    msg = EmailMessage()
    msg["From"] = f"Kadonneen Sukuhistorian Metsästäjä <{SMTP_EMAIL}>"
    msg["To"] = to_email
    msg["Subject"] = f"Haploryhmäraporttisi: {haplogroup}"

    text_body = f"""
Hei {user_name or ''},

Haploryhmäraporttisi ({haplogroup}) on valmis!

PDF on liitteenä tässä sähköpostissa.

Ystävällisin terveisin,
Kadonneen Sukuhistorian Metsästäjä
https://kshm.fi
"""
    msg.set_content(text_body.strip())

    msg.add_alternative(f"""
<html>
  <body style="font-family: Georgia, serif; background:#fdfaf3; padding:20px;">
    <div style="max-width:600px;margin:auto;background:#fff8ec;padding:30px;border-radius:12px;border:1px solid #d4a373;">
      <h2 style="color:#92400e;">Hei {user_name or ''},</h2>
      <p>Haploryhmäraporttisi <strong>{haplogroup}</strong> on valmis!</p>
      <p>PDF-raportti on liitteenä tässä sähköpostissa.</p>
      <p style="margin-top:30px;">Seikkailullisin terveisin,<br>
      <strong>Kadonneen Sukuhistorian Metsästäjä</strong><br>
      <a href="https://kshm.fi">kshm.fi</a></p>
    </div>
  </body>
</html>
""", subtype="html")

    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    msg.add_attachment(
        pdf_data,
        maintype="application",
        subtype="pdf",
        filename=os.path.basename(pdf_path)
    )

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)
