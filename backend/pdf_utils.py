# pdf_utils.py
# KSHM – Archaeogenetic Bloodline Book PDF Engine

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak,
    Table,
    TableStyle,
    ListFlowable,
    ListItem,
    KeepTogether
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.platypus.doctemplate import Indenter
import os


# =========================================================
# TYPOGRAPHY REGISTRATION
# =========================================================

def register_fonts(font_path="fonts"):
    """
    Register custom fonts if available.
    Falls back safely if not found.
    """

    try:
        pdfmetrics.registerFont(
            TTFont("Playfair", os.path.join(font_path, "PlayfairDisplay-Regular.ttf"))
        )
        pdfmetrics.registerFont(
            TTFont("Playfair-Italic", os.path.join(font_path, "PlayfairDisplay-Italic.ttf"))
        )
        pdfmetrics.registerFont(
            TTFont("Lora", os.path.join(font_path, "Lora-Regular.ttf"))
        )
    except Exception:
        # Fallback to built-in fonts
        pass


# =========================================================
# COLOR SYSTEM (Sepia theme)
# =========================================================

SEPIA_BG = colors.HexColor("#f4ecdf")
SEPIA_TEXT = colors.HexColor("#2e2a24")
SEPIA_ACCENT = colors.HexColor("#6e4f2c")


# =========================================================
# STYLE SYSTEM
# =========================================================

def get_styles():
    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="TitlePlayfair",
            fontName="Playfair",
            fontSize=26,
            leading=32,
            textColor=SEPIA_TEXT,
            alignment=TA_CENTER,
            spaceAfter=20,
        )
    )

    styles.add(
        ParagraphStyle(
            name="Subtitle",
            fontName="Playfair-Italic",
            fontSize=16,
            leading=22,
            textColor=SEPIA_ACCENT,
            alignment=TA_CENTER,
            spaceAfter=40,
        )
    )

    styles.add(
        ParagraphStyle(
            name="HeadingChapter",
            fontName="Playfair",
            fontSize=20,
            leading=26,
            textColor=SEPIA_TEXT,
            spaceBefore=30,
            spaceAfter=15,
        )
    )

    styles.add(
        ParagraphStyle(
            name="HeadingSection",
            fontName="Playfair-Italic",
            fontSize=15,
            leading=20,
            textColor=SEPIA_ACCENT,
            spaceBefore=20,
            spaceAfter=10,
        )
    )

    styles.add(
        ParagraphStyle(
            name="BodyLora",
            fontName="Lora",
            fontSize=12,
            leading=18,
            textColor=SEPIA_TEXT,
            spaceAfter=12,
        )
    )

    styles.add(
        ParagraphStyle(
            name="Caption",
            fontName="Lora",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#6b5e4a"),
            alignment=TA_CENTER,
            spaceAfter=20,
        )
    )

    return styles


# =========================================================
# PAGE TEMPLATE (Margins & Footer)
# =========================================================

def add_page_number(canvas, doc):
    page_num_text = f"{doc.page}"
    canvas.setFont("Lora", 9)
    canvas.setFillColor(SEPIA_ACCENT)
    canvas.drawRightString(19.5 * cm, 1.5 * cm, page_num_text)


# =========================================================
# MAIN PDF GENERATOR CLASS
# =========================================================

class BloodlinePDF:

    def __init__(self, output_path):
        register_fonts()
        self.styles = get_styles()
        self.doc = BaseDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=2.5 * cm,
            leftMargin=2.5 * cm,
            topMargin=2.5 * cm,
            bottomMargin=2.5 * cm,
        )

        frame = Frame(
            self.doc.leftMargin,
            self.doc.bottomMargin,
            self.doc.width,
            self.doc.height - 1 * cm,
            id="normal"
        )

        template = PageTemplate(id="test", frames=frame, onPage=add_page_number)
        self.doc.addPageTemplates([template])

        self.story = []

    # -----------------------------------------------------
    # COVER PAGE
    # -----------------------------------------------------

    def add_cover(self, title, subtitle, slogan):
        self.story.append(Spacer(1, 6 * cm))
        self.story.append(Paragraph(title, self.styles["TitlePlayfair"]))
        self.story.append(Paragraph(subtitle, self.styles["Subtitle"]))
        self.story.append(Spacer(1, 2 * cm))
        self.story.append(Paragraph(f"<i>{slogan}</i>", self.styles["Caption"]))
        self.story.append(PageBreak())

    # -----------------------------------------------------
    # TABLE OF CONTENTS
    # -----------------------------------------------------

    def add_table_of_contents(self):
        self.story.append(Paragraph("Sisällysluettelo", self.styles["HeadingChapter"]))
        toc = TableOfContents()
        toc.levelStyles = [
            self.styles["BodyLora"],
        ]
        self.story.append(toc)
        self.story.append(PageBreak())

    # -----------------------------------------------------
    # CHAPTER
    # -----------------------------------------------------

    def add_chapter(self, title):
        self.story.append(Paragraph(title, self.styles["HeadingChapter"]))
        self.story.append(Spacer(1, 12))

    # -----------------------------------------------------
    # SECTION
    # -----------------------------------------------------

    def add_section(self, title):
        self.story.append(Paragraph(title, self.styles["HeadingSection"]))

    # -----------------------------------------------------
    # PARAGRAPH
    # -----------------------------------------------------

    def add_paragraph(self, text):
        self.story.append(Paragraph(text, self.styles["BodyLora"]))

    # -----------------------------------------------------
    # IMAGE WITH CAPTION
    # -----------------------------------------------------

    def add_image(self, image_path, caption=None, width=14 * cm):
        if os.path.exists(image_path):
            img = Image(image_path, width=width, preserveAspectRatio=True)
            self.story.append(Spacer(1, 20))
            self.story.append(img)
            if caption:
                self.story.append(Paragraph(caption, self.styles["Caption"]))
            self.story.append(Spacer(1, 10))

    # -----------------------------------------------------
    # PAGE BREAK
    # -----------------------------------------------------

    def page_break(self):
        self.story.append(PageBreak())

    # -----------------------------------------------------
    # BUILD PDF
    # -----------------------------------------------------

    def build(self):
        self.doc.build(self.story)
