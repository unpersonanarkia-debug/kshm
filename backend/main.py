from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from data_utils import fetch_full_haplogroup_data
from story_utils import generate_story_html
from pdf_utils import generate_pdf
from email_utils import send_email_with_pdf

app = FastAPI(title="Kadonneen Sukuhistorian Metsästäjä API")

# 🔐 CORS (salli frontendin yhteydet)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tuotannossa rajaa domainiin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "KSHM backend running"}


@app.post("/api/order_report")
async def order_report(request: Request):
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Virheellinen JSON-data")

    name = data.get("name")
    email = data.get("email")
    haplo = data.get("haplogroup")
    notes = data.get("notes", "")

    if not name or not email or not haplo:
        raise HTTPException(status_code=422, detail="Nimi, sähköposti ja haploryhmä vaaditaan")

    # 🧬 Hae arkeogeneettinen data
    haplo_data = fetch_full_haplogroup_data(haplo)

    if not haplo_data:
        raise HTTPException(status_code=404, detail="Haploryhmää ei löydetty")

    # 📖 Luo tarina (haploryhmäkohtainen tyyli)
    story_html = generate_story_html(haplo_data, user_name=name, notes=notes)

    # 📄 Luo PDF
    safe_name = name.replace(" ", "").replace("/", "")
    pdf_filename = f"{haplo}_{safe_name}.pdf"
    pdf_path = generate_pdf(story_html, filename=pdf_filename)

    # ✉️ Lähetä sähköposti
    send_email_with_pdf(
        recipient=email,
        haplogroup=haplo,
        story_html=story_html,
        pdf_path=pdf_path,
        user_name=name
    )

    return JSONResponse({"message": "Raportti tilattu onnistuneesti."})
