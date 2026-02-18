from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import uuid
import os
import logging

from data_utils import fetch_full_haplogroup_data
from story_utils import generate_story_from_haplogroup
from pdf_utils import generate_pdf_from_story
from email_utils import send_email_with_pdf

# ─────────────────────────────────────────────
# App setup  (app ENSIN, router JÄLKEEN)
# ─────────────────────────────────────────────

app = FastAPI(
    title="Kadonneen Sukuhistorian Metsästäjä API",
    description="API haploryhmäpohjaisten arkeogeneettisten raporttien tilaamiseen.",
    version="1.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tuotannossa: ["https://kshm.fi"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Research API router – lisätään app:n luomisen jälkeen
from backend.research_api import app as research_app
from fastapi import APIRouter

# Kopioidaan research_api:n routet tähän app:iin prefix-free
for route in research_app.routes:
    app.routes.append(route)

# ─────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kshm-backend")

# ─────────────────────────────────────────────
# Models
# ─────────────────────────────────────────────

class OrderRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    email: EmailStr
    haplogroup: str = Field(..., min_length=1, max_length=64)
    haplogroup_y: Optional[str] = Field(None, min_length=1, max_length=64)
    notes: Optional[str] = Field(None, max_length=2000)
    language: Optional[str] = Field("fi", max_length=8)
    tone: Optional[str] = Field("academic", max_length=32)


class OrderResponse(BaseModel):
    message: str
    order_id: str


# ─────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "version": app.version}


@app.post("/api/order_report", response_model=OrderResponse)
async def order_report(order: OrderRequest):
    try:
        logger.info(f"New report order: {order.haplogroup} for {order.email}")

        # 1. Fetch haplogroup data (mtDNA)
        haplo_data_mt = fetch_full_haplogroup_data(order.haplogroup)
        if not haplo_data_mt or "error" in haplo_data_mt:
            raise HTTPException(
                status_code=404,
                detail=f"Haploryhmälle {order.haplogroup} ei löytynyt tietoja."
            )

        # 2. Fetch Y-DNA jos annettu
        haplo_data_y = None
        if order.haplogroup_y:
            haplo_data_y = fetch_full_haplogroup_data(order.haplogroup_y)
            if not haplo_data_y or "error" in haplo_data_y:
                raise HTTPException(
                    status_code=404,
                    detail=f"Haploryhmälle {order.haplogroup_y} ei löytynyt tietoja."
                )

        # 3. Generoi tarinat
        story_mt = generate_story_from_haplogroup(
            haplogroup=order.haplogroup,
            lang=order.language,
            tone=order.tone,
        )

        story_y = None
        if haplo_data_y:
            story_y = generate_story_from_haplogroup(
                haplogroup=order.haplogroup_y,
                lang=order.language,
                tone=order.tone,
            )

        # 4. Generoi PDF
        order_id = str(uuid.uuid4())[:8]
        safe_name = order.name.replace(" ", "").replace("/", "")
        filename = f"{order.haplogroup}_{safe_name}_{order_id}.pdf"
        output_dir = "generated_reports"
        os.makedirs(output_dir, exist_ok=True)
        pdf_path = os.path.join(output_dir, filename)

        generate_pdf_from_story(
            story_mt=story_mt,
            story_y=story_y,
            output_path=pdf_path,
            user_name=order.name,
            notes=order.notes,
            lang=order.language,
        )

        # 5. Lähetä sähköposti
        send_email_with_pdf(
            to_email=order.email,
            pdf_path=pdf_path,
            haplogroup=order.haplogroup,
            lang=order.language,
            user_name=order.name,
        )

        logger.info(f"Report sent successfully: {pdf_path}")

        return OrderResponse(
            message="Raportti luotu ja lähetetty onnistuneesti.",
            order_id=order_id
        )

    except HTTPException:
        raise

    except Exception as e:
        logger.exception("Unexpected error while processing order")
        raise HTTPException(
            status_code=500,
            detail="Palvelimella tapahtui virhe raporttia luotaessa."
        )


@app.get("/api/debug/haplogroup/{haplogroup}")
async def debug_haplogroup(haplogroup: str):
    """Raakadata haploryhmästä – vain kehityskäyttöön."""
    try:
        data = fetch_full_haplogroup_data(haplogroup)
        if not data:
            raise HTTPException(status_code=404, detail="Haploryhmää ei löytynyt.")
        return JSONResponse(data)
    except Exception as e:
        logger.exception("Error fetching haplogroup data")
        raise HTTPException(status_code=500, detail="Virhe tietojen haussa.")


# ─────────────────────────────────────────────
# Käynnistys
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
