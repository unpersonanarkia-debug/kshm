from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from pathlib import Path
import json
import io
import csv
import logging

logger = logging.getLogger("kshm-research")

app = FastAPI(
    title="KSHM Research API",
    version="1.2.0",
    description="Research Edition – mtDNA & Y-DNA haploryhmädata (JSON-pohjainen)",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tuotannossa: ["https://kshm.fi"]
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────
# PYDANTIC SCHEMAT
# ─────────────────────────────────────────────

class AncientSample(BaseModel):
    sample_id: str
    date_bp: int
    date_bp_uncertainty: int
    region: str
    country: str
    site: str
    culture: str
    snp_quality: str
    coverage: Optional[float] = None
    source: str
    doi: str

class GeographicDensity(BaseModel):
    region: str
    country_code: str
    frequency_percent: float
    sample_size: int
    data_source: str

class PhylogeneticPlacement(BaseModel):
    haplogroup_full: str
    parent: str
    lineage_type: str
    defining_snps: List[str]
    phylotree_build: str
    yfull_version: Optional[str] = None

class ConfidenceModel(BaseModel):
    tmrca_estimate_bp: int
    tmrca_min_bp: int
    tmrca_max_bp: int
    tmrca_confidence_interval: str
    tmrca_method: str
    geographic_origin_confidence: str
    sample_bias_note: str
    overall_uncertainty_percent: int

class ChangelogEntry(BaseModel):
    version: str
    date: str
    changes: List[str]

class Source(BaseModel):
    authors: str
    year: int
    title: str
    journal: str
    doi: str
    relevance: str

class ResearchReport(BaseModel):
    haplogroup: str
    haplogroup_normalized: str
    lineage_type: str
    defining_snps: List[str]
    phylotree_build: str
    phylogenetic_placement: PhylogeneticPlacement
    confidence_model: ConfidenceModel
    ancient_samples: List[AncientSample]
    ancient_sample_count: int
    geographic_distribution: List[GeographicDensity]
    methodology_notes: str
    limitations: List[str]
    bibliography: List[Source]
    changelog: List[ChangelogEntry]
    data_version: str
    generated_by: str
    generated_at: str


# ─────────────────────────────────────────────
# TIETOKANTALATAUS JSON-TIEDOSTOISTA
# ─────────────────────────────────────────────

DATA_DIR = Path(__file__).parent.parent / "data" / "haplogroups"

def _load_all() -> dict[str, ResearchReport]:
    """
    Lataa kaikki JSON-tiedostot data/haplogroups/-hakemistosta käynnistyksessä.
    Rakentaa hakutaulukon: kanoninen nimi + kaikki aliases → sama objekti.
    """
    db: dict[str, ResearchReport] = {}

    if not DATA_DIR.exists():
        logger.warning(f"Data-hakemistoa ei löydy: {DATA_DIR}")
        return db

    for path in DATA_DIR.glob("*.json"):
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))

            # ancient_sample_count lasketaan automaattisesti jos puuttuu
            if "ancient_sample_count" not in raw:
                raw["ancient_sample_count"] = len(raw.get("ancient_samples", []))

            # generated_at asetetaan latauksessa
            raw.setdefault("generated_at", datetime.utcnow().isoformat() + "Z")

            report = ResearchReport(**raw)

            # Kanoninen avain (tiedostonimi ilman .json, isot kirjaimet)
            canonical = path.stem.upper()
            db[canonical] = report

            # Lisää aliases hakutaulukkoon
            for alias in raw.get("aliases", []):
                db[alias.upper()] = report

            logger.info(f"Ladattu: {canonical} ({len(raw.get('ancient_samples', []))} näytettä)")

        except Exception as e:
            logger.error(f"Virhe tiedostossa {path.name}: {e}")

    logger.info(f"Tietokanta ladattu: {len(set(db.values()))} haploryhmää, {len(db)} hakuavainta")
    return db


# Ladataan kerran käynnistyksessä
HAPLOGROUP_DB: dict[str, ResearchReport] = _load_all()


def lookup(haplogroup: str) -> Optional[ResearchReport]:
    """Case-insensitive haku – etsii ensin tarkalla, sitten isoilla kirjaimilla."""
    key = haplogroup.strip()
    return HAPLOGROUP_DB.get(key) or HAPLOGROUP_DB.get(key.upper())


def refresh_db():
    """Lataa tietokannan uudelleen ilman palvelimen uudelleenkäynnistystä."""
    global HAPLOGROUP_DB
    HAPLOGROUP_DB = _load_all()


def now() -> str:
    return datetime.utcnow().isoformat() + "Z"


# ─────────────────────────────────────────────
# ENDPOINTIT
# ─────────────────────────────────────────────

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": app.version,
        "haplogroups_loaded": len(set(HAPLOGROUP_DB.values())),
        "data_dir": str(DATA_DIR),
        "timestamp": now(),
    }


@app.get("/api/research/search")
async def search_haplogroups(
    lineage:     Optional[str] = Query(None, description="mtDNA tai Y-DNA"),
    region:      Optional[str] = Query(None, description="Alue tai maa, esim. 'Ireland'"),
    snp_quality: Optional[str] = Query(None, description="High / Medium / Low"),
    min_date_bp: Optional[int] = Query(None, description="Vanhin hyväksytty näyte (BP)"),
    max_date_bp: Optional[int] = Query(None, description="Nuorin hyväksytty näyte (BP)"),
):
    """
    Hae haploryhmäraportteja suodattimilla.

      /api/research/search?lineage=mtDNA&region=Ireland
      /api/research/search?snp_quality=High&max_date_bp=3000
      /api/research/search?min_date_bp=5000&max_date_bp=10000
    """
    results = []

    for report in set(HAPLOGROUP_DB.values()):

        if lineage and report.lineage_type.lower() != lineage.lower():
            continue

        if region:
            r = region.lower()
            in_samples = any(
                r in s.region.lower() or r in s.country.lower()
                for s in report.ancient_samples
            )
            in_dist = any(r in g.region.lower() for g in report.geographic_distribution)
            if not in_samples and not in_dist:
                continue

        if snp_quality:
            if not any(
                s.snp_quality.lower() == snp_quality.lower()
                for s in report.ancient_samples
            ):
                continue

        if min_date_bp or max_date_bp:
            matching = [
                s for s in report.ancient_samples
                if (min_date_bp is None or s.date_bp >= min_date_bp)
                and (max_date_bp is None or s.date_bp <= max_date_bp)
            ]
            if not matching:
                continue

        results.append({
            "haplogroup":           report.haplogroup,
            "lineage_type":         report.lineage_type,
            "ancient_sample_count": report.ancient_sample_count,
            "tmrca_estimate_bp":    report.confidence_model.tmrca_estimate_bp,
            "tmrca_min_bp":         report.confidence_model.tmrca_min_bp,
            "tmrca_max_bp":         report.confidence_model.tmrca_max_bp,
            "data_version":         report.data_version,
        })

    return {
        "query": {
            "lineage": lineage, "region": region,
            "snp_quality": snp_quality,
            "min_date_bp": min_date_bp, "max_date_bp": max_date_bp,
        },
        "result_count": len(results),
        "results": results,
    }


@app.get("/api/research/{haplogroup}", response_model=ResearchReport)
async def get_research_report(haplogroup: str):
    """Täysi tutkimusraportti – Research Edition PDF:n ja dashboardin datalähde."""
    report = lookup(haplogroup)
    if not report:
        available = sorted(set(r.haplogroup for r in HAPLOGROUP_DB.values()))
        raise HTTPException(
            status_code=404,
            detail=f"Haploryhmää '{haplogroup}' ei löydy. Saatavilla: {available}"
        )
    report.generated_at = now()
    return report


@app.get("/api/research/{haplogroup}/samples")
async def get_ancient_samples(haplogroup: str):
    """Pelkät muinaisnäytteet – dashboardin taulukkoa varten."""
    report = lookup(haplogroup)
    if not report:
        raise HTTPException(status_code=404, detail="Haploryhmää ei löydy.")
    return {
        "haplogroup":   report.haplogroup,
        "sample_count": report.ancient_sample_count,
        "samples":      [s.model_dump() for s in report.ancient_samples],
    }


@app.get("/api/research/{haplogroup}/phylogeny")
async def get_phylogeny(haplogroup: str):
    """Fylogeneettinen sijoitus – dashboardin puunäkymää varten."""
    report = lookup(haplogroup)
    if not report:
        raise HTTPException(status_code=404, detail="Haploryhmää ei löydy.")
    return report.phylogenetic_placement.model_dump()


@app.get("/api/research/{haplogroup}/export")
async def export_data(
    haplogroup: str,
    format: str = Query("json", enum=["json", "csv"])
):
    """Exportoi muinaisnäytteet CSV:nä tai täysi raportti JSON:na."""
    report = lookup(haplogroup)
    if not report:
        raise HTTPException(status_code=404, detail="Haploryhmää ei löydy.")

    if format == "csv":
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=[
            "sample_id", "date_bp", "date_bp_uncertainty",
            "region", "country", "site", "culture",
            "snp_quality", "coverage", "source", "doi"
        ])
        writer.writeheader()
        for s in report.ancient_samples:
            writer.writerow(s.model_dump())
        return Response(
            content=output.getvalue(),
            media_type="text/csv",
            headers={
                "Content-Disposition":
                    f"attachment; filename={haplogroup}_ancient_samples.csv"
            }
        )

    report.generated_at = now()
    return report.model_dump()


@app.post("/api/research/reload")
async def reload_database():
    """
    Lataa JSON-tiedostot uudelleen ilman palvelimen uudelleenkäynnistystä.
    Käytä kun lisäät uuden haploryhmän data/haplogroups/-hakemistoon.
    HUOM: Suojaa tämä autentikoinnilla tuotannossa.
    """
    refresh_db()
    return {
        "status": "reloaded",
        "haplogroups_loaded": len(set(HAPLOGROUP_DB.values())),
        "timestamp": now(),
    }


# ─────────────────────────────────────────────
# KÄYNNISTYS
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
