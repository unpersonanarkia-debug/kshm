from weasyprint import HTML
import os
import tempfile
from datetime import datetime


def generate_pdf(html_content: str, filename: str) -> str:
    """
    Generoi PDF HTML-sisällöstä ja palauttaa tiedostopolun.
    """
    output_dir = "generated_pdfs"
    os.makedirs(output_dir, exist_ok=True)

    safe_filename = filename.replace(" ", "_").lower()
    file_path = os.path.join(output_dir, safe_filename)

    HTML(string=html_content).write_pdf(file_path)

    return file_path
