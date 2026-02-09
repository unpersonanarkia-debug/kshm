from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import uuid
import os
import logging

from data_utils import fetch_full_haplogroup_data
from story_utils import generate_story_html, generate_story_text
from pdf_utils import generate_pdf
from email_utils import send_email_with_pdf

# --------------------
# App setup
# --------------------

app = FastAPI(
    title="Kadonneen Sukuhistorian Metsästäjä API",
    description="API haploryhmäpohjaisten arkeogeneettisten raporttien tilaamiseen ja toimittamiseen.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # rajaa tuotannossa tarvittaessa
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# Logging
# --------------------

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kshm-backend")

# --------------------
# Models
# --------------------

class OrderRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    email: EmailStr
    haplogroup: str = Field(..., min_length=1, max_length=64)
    notes: Optional[str] = Field(None, max_length=2000)
    language: Optional[str] = Field("fi", max_length=8)


class OrderResponse(BaseModel):
    message: str
    order_id: str


# --------------------
# Routes
# --------------------

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}


@app.post("/api/order_report", response_model=OrderResponse)
async def order_report(order: OrderRequest):
    try:
        logger.info(f"New report order: {order.haplogroup} for {order.email}")

        # 1. Fetch haplogroup data
        haplo_data = fetch_full_haplogroup_data(order.haplogroup)

        if not haplo_data or "error" in haplo_data:
            raise HTTPException(
                status_code=404,
                detail=f"Haploryhmälle {order.haplogroup} ei löytynyt tietoja."
            )

        # 2. Generate story
        story_html = generate_story_html(
            haplo_data,
            user_name=order.name,
            notes=order.notes,
            language=order.language
        )

        story_text = generate_story_text(
            haplo_data,
            user_name=order.name,
            notes=order.notes,
            language=order.language
        )

        # 3. Generate PDF
        order_id = str(uuid.uuid4())[:8]
        safe_name = order.name.replace(" ", "").replace("/", "")
        filename = f"{order.haplogroup}_{safe_name}_{order_id}.pdf"
        output_dir = "generated_reports"
        os.makedirs(output_dir, exist_ok=True)
        pdf_path = os.path.join(output_dir, filename)

        generate_pdf(story_html, output_path=pdf_path)

        # 4. Send email with PDF
        send_email_with_pdf(
            to_email=order.email,
            haplogroup=order.haplogroup,
            story_text=story_text,
            pdf_path=pdf_path,
            user_name=order.name
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


# --------------------
# Optional: debug endpoint
# --------------------

@app.get("/api/debug/haplogroup/{haplogroup}")
async def debug_haplogroup(haplogroup: str):
    """
    Palauttaa raakadatan haploryhmästä ilman raportointia.
    Hyödyllinen testaamiseen ja kehitykseen.
    """
    try:
        data = fetch_full_haplogroup_data(haplogroup)
        if not data:
            raise HTTPException(status_code=404, detail="Haploryhmää ei löytynyt.")
        return JSONResponse(data)
    except Exception as e:
        logger.exception("Error fetching haplogroup data")
        raise HTTPException(status_code=500, detail="Virhe tietojen haussa.")
