# pdf_utils.py

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
import os
from typing import Optional


# ===============================
# Main entry point
# ===============================

def generate_pdf(
    story_text: str,
    filename: str,
    title: str = "Arkeogeneettinen raportti",
    subtitle: Optional[str] = None,
    logo_path: Optional[str] = None,
    output_dir: str = "generated_pdfs"
) -> str:
    """
    Luo PDF-tiedoston annetusta tekstistä.

    :param story_text: Valmis tarina tai raporttiteksti
    :param filename: Lopullinen tiedostonimi (esim. H1_T16189C_Matti_Meikäläinen.pdf)
    :param title: Raportin pääotsikko
    :param subtitle: Alaotsikko (esim. haploryhmä)
    :param logo_path: Polku logo-kuvaan (valinnainen)
    :param output_dir: Hakemisto, johon PDF tallennetaan
    :return: Täysi polku luotuun PDF-tiedostoon
    """

    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    doc = SimpleDocTemplate(
        filepath,
        pagesize=A4,
        rightMargin=2.5 * cm,
        leftMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm
    )

    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="TitleStyle",
        fontSize=24,
        leading=30,
        alignment=TA_CENTER,
        textColor=HexColor("#6B4E16"),
        spaceAfter=24
    ))

    styles.add(ParagraphStyle(
        name="SubtitleStyle",
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        textColor=HexColor("#8A6A2F"),
        spaceAfter=18
    ))

    styles.add(ParagraphStyle(
        name="BodyStyle",
        fontSize=11.5,
        leading=16,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    ))

    styles.add(ParagraphStyle(
        name="SectionHeader",
        fontSize=14,
        leading=18,
        textColor=HexColor("#5C3A0F"),
        spaceBefore=18,
        spaceAfter=10,
        fontName="Helvetica-Bold"
    ))

    elements = []

    # Logo
    if logo_path and os.path.exists(logo_path):
        img = Image(logo_path, width=6 * cm, height=6 * cm)
        img.hAlign = "CENTER"
        elements.append(img)
        elements.append(Spacer(1, 18))

    # Title
    elements.append(Paragraph(title, styles["TitleStyle"]))

    if subtitle:
        elements.append(Paragraph(subtitle, styles["SubtitleStyle"]))

    elements.append(Spacer(1, 24))

    # Story content parsing
    paragraphs = parse_story_text(story_text)

    for p in paragraphs:
        if p.startswith("### "):
            elements.append(Paragraph(p.replace("### ", ""), styles["SectionHeader"]))
        else:
            elements.append(Paragraph(p, styles["BodyStyle"]))

        elements.append(Spacer(1, 10))

    doc.build(elements)

    return filepath


# ===============================
# Helpers
# ===============================

def parse_story_text(story_text: str) -> list:
    """
    Pilkkoo tekstin kappaleiksi ja tunnistaa otsikot.
    Otsikkoformaatti: "### Otsikko"
    """
    lines = story_text.split("\n")
    paragraphs = []
    buffer = ""

    for line in lines:
        line = line.strip()
        if not line:
            if buffer:
                paragraphs.append(buffer)
                buffer = ""
        elif line.startswith("### "):
            if buffer:
                paragraphs.append(buffer)
                buffer = ""
            paragraphs.append(line)
        else:
            buffer += (" " if buffer else "") + line

    if buffer:
        paragraphs.append(buffer)

    return paragraphs
