"""
KSHM Research Edition – FastAPI endpoint v1.1.0
/api/research/{haplogroup}

Lisätty v1.1.0:
  - GET /api/research/search?lineage=mtDNA&region=Ireland
  - ConfidenceModel: tmrca_min_bp + tmrca_max_bp (numeeriset rajat dashboardia varten)
  - Changelog-kenttä kaikkiin raportteihin
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import io
import csv

app = FastAPI(
    title="KSHM Research API",
    version="1.1.0",
    description="Research Edition – mtDNA & Y-DNA haploryhmädata",
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
    snp_quality: str                  # "High" / "Medium" / "Low"
    coverage: Optional[float] = None
    source: str
    doi: str


class GeographicDensity(BaseModel):
    region: str
    country_code: str                 # ISO 3166-1 alpha-2
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
    tmrca_min_bp: int                 # alaraja – dashboard piirtää janan tästä...
    tmrca_max_bp: int                 # yläraja – ...tähän
    tmrca_confidence_interval: str    # ihmisluettava teksti (säilytetty)
    tmrca_method: str
    geographic_origin_confidence: str
    sample_bias_note: str
    overall_uncertainty_percent: int


class ChangelogEntry(BaseModel):
    version: str
    date: str                         # ISO date "2026-02-18"
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
# APUFUNKTIO
# ─────────────────────────────────────────────

def now() -> str:
    return datetime.utcnow().isoformat() + "Z"


# ─────────────────────────────────────────────
# DATA – H1-T16189C!
# ─────────────────────────────────────────────

H1_T16189C_DATA = ResearchReport(
    haplogroup="H1-T16189C!",
    haplogroup_normalized="H1",
    lineage_type="mtDNA",
    defining_snps=["T16189C"],
    phylotree_build="PhyloTree Build 17",

    phylogenetic_placement=PhylogeneticPlacement(
        haplogroup_full="H1-T16189C!",
        parent="H1",
        lineage_type="mtDNA",
        defining_snps=["T16189C"],
        phylotree_build="PhyloTree Build 17",
        yfull_version=None
    ),

    confidence_model=ConfidenceModel(
        tmrca_estimate_bp=13000,
        tmrca_min_bp=11000,
        tmrca_max_bp=15000,
        tmrca_confidence_interval="11000–15000 BP",
        tmrca_method="Bayesian molecular clock (BEAST 2.x, HKY+Γ, 10M MCMC)",
        geographic_origin_confidence="Moderate",
        sample_bias_note=(
            "Akateemiset näytteet painottuvat Länsi- ja Keski-Eurooppaan. "
            "Itä-Euroopan, Lähi-idän ja Pohjois-Afrikan edustus on aliedustettu. "
            "Kuluttajatietokantadata (FTDNA, 23andMe) ei ole kriittisesti validoitu."
        ),
        overall_uncertainty_percent=20
    ),

    ancient_samples=[
        AncientSample(
            sample_id="PN05",
            date_bp=5900, date_bp_uncertainty=140,
            region="County Clare, Munster", country="Ireland",
            site="Poulnabrone dolmen", culture="Neolithic megalithic",
            snp_quality="High", coverage=12.4,
            source="Cassidy et al. 2020",
            doi="10.1038/s41586-020-2378-6"
        ),
        AncientSample(
            sample_id="PCA0099",
            date_bp=1750, date_bp_uncertainty=80,
            region="Masłomęcz, Lublin Voivodeship", country="Poland",
            site="Masłomęcz cemetery",
            culture="Wielbark culture (Gothic migration period)",
            snp_quality="High", coverage=8.7,
            source="Stolarek et al. 2019",
            doi="10.1038/s41598-019-51029-0"
        ),
        AncientSample(
            sample_id="VK51",
            date_bp=1000, date_bp_uncertainty=100,
            region="Gotland", country="Sweden",
            site="Kopparsvik cemetery", culture="Viking Age",
            snp_quality="High", coverage=15.2,
            source="Margaryan et al. 2020",
            doi="10.1038/s41586-020-2688-8"
        ),
        AncientSample(
            sample_id="VK50",
            date_bp=1000, date_bp_uncertainty=100,
            region="Gotland", country="Sweden",
            site="Kopparsvik cemetery", culture="Viking Age",
            snp_quality="Medium", coverage=6.1,
            source="Margaryan et al. 2020",
            doi="10.1038/s41586-020-2688-8"
        ),
        AncientSample(
            sample_id="Barcin_N",
            date_bp=8200, date_bp_uncertainty=300,
            region="Marmara region", country="Turkey",
            site="Barcın Höyük",
            culture="Anatolian Neolithic (PPNB)",
            snp_quality="Medium", coverage=4.3,
            source="Kılınç et al. 2016",
            doi="10.1016/j.cub.2016.07.057"
        ),
    ],
    ancient_sample_count=5,

    geographic_distribution=[
        GeographicDensity(region="Finland", country_code="FI",
                          frequency_percent=12.29, sample_size=441,
                          data_source="consumer_db (FTDNA 2026)"),
        GeographicDensity(region="Ireland", country_code="IE",
                          frequency_percent=9.8, sample_size=612,
                          data_source="consumer_db"),
        GeographicDensity(region="United Kingdom", country_code="GB",
                          frequency_percent=8.4, sample_size=2100,
                          data_source="consumer_db"),
        GeographicDensity(region="Sweden", country_code="SE",
                          frequency_percent=7.2, sample_size=880,
                          data_source="consumer_db"),
        GeographicDensity(region="Norway", country_code="NO",
                          frequency_percent=6.9, sample_size=540,
                          data_source="consumer_db"),
        GeographicDensity(region="Morocco (Anti-Atlas, Amazigh)",
                          country_code="MA",
                          frequency_percent=1.0, sample_size=120,
                          data_source="academic"),
    ],

    methodology_notes=(
        "Haploryhmämääritys perustuu PhyloTree Build 17 -luokitukseen. "
        "Muinaisnäytteet haettu Allen Ancient DNA Resource (AADR) v54.1 "
        "sekä primaarijulkaistuista supplementaaritiedostoista. "
        "Haploryhmämatchaus: täsmällinen SNP-tarkistus (T16189C positiivinen). "
        "TMRCA: BEAST 2.6, HKY+Γ substituutiomalli, 10M MCMC iteraatiota."
    ),

    limitations=[
        "TMRCA-epävarmuus ±20% johtuen molekyylipumpun kalibraatiohaasteista.",
        "Pohjois-Afrikan ja Lähi-idän näytteet aliedustettu akateemisissa tietokannoissa.",
        "Kuluttajadatan haplogroup-määritykset eivät ole yhtä tarkkoja kuin WGS-sekvensointi.",
        "VK50: matalan kattavuuden näyte (6.1x) – tulkinnoissa huomioitava.",
        "Modernin jakauman data heijastaa palveluita käyttävää väestöä, ei koko väestöä.",
    ],

    bibliography=[
        Source(authors="Cassidy, L.M. et al.", year=2020,
               title="A dynastic elite in monumental Neolithic society",
               journal="Nature", doi="10.1038/s41586-020-2378-6",
               relevance="Poulnabrone PN05, H1-T16189C! tunnistus"),
        Source(authors="Stolarek, I. et al.", year=2019,
               title="Ancient DNA from Wielbark culture reveals complex population history",
               journal="Scientific Reports", doi="10.1038/s41598-019-51029-0",
               relevance="Masłomęcz PCA0099, goottien vaellusvaihe"),
        Source(authors="Margaryan, A. et al.", year=2020,
               title="Population genomics of the Viking world",
               journal="Nature", doi="10.1038/s41586-020-2688-8",
               relevance="Kopparsvik VK50/VK51, viikinkiajan Gotlanti"),
        Source(authors="Kılınç, G.M. et al.", year=2016,
               title="The demographic development of the first farmers in Anatolia",
               journal="Current Biology", doi="10.1016/j.cub.2016.07.057",
               relevance="Anatolian Neolithic EEF H1-kantajat"),
        Source(authors="Achilli, A. et al.", year=2004,
               title="The molecular dissection of mtDNA haplogroup H confirms that "
                      "the Franco-Cantabrian glacial refuge was a major source for "
                      "the European gene pool",
               journal="American Journal of Human Genetics",
               doi="10.1086/425590",
               relevance="H1 refugio-perusta, Franco-Cantabria"),
        Source(authors="Haak, W. et al.", year=2015,
               title="Massive migration from the steppe was a source for "
                      "Indo-European languages in Europe",
               journal="Nature", doi="10.1038/nature14317",
               relevance="EEF-jatkumo Anatolia → Länsi-Eurooppa"),
        Source(authors="Rito, T. et al.", year=2013,
               title="Phylogeography of mtDNA haplogroup H",
               journal="European Journal of Human Genetics",
               doi="10.1038/ejhg.2013.54",
               relevance="H1-alalinjat, refugio → neoliittinen leviäminen"),
    ],

    changelog=[
        ChangelogEntry(
            version="1.0.0",
            date="2026-02-01",
            changes=[
                "Ensijulkaisu: 5 muinaisnäytettä, 7 lähdettä.",
                "Endpointit: /api/research/{haplogroup}, /samples, /export.",
            ]
        ),
        ChangelogEntry(
            version="1.1.0",
            date="2026-02-18",
            changes=[
                "Lisätty tmrca_min_bp ja tmrca_max_bp – dashboardin aikajanajanaa varten.",
                "Lisätty changelog-kenttä kaikkiin raportteihin.",
                "Lisätty /api/research/search -endpoint (lineage, region, snp_quality, aikaväli).",
            ]
        ),
    ],

    data_version="1.1.0",
    generated_by="KSHM Research Engine v1.1.0",
    generated_at=now()
)


# ─────────────────────────────────────────────
# TIETOKANTA
# ─────────────────────────────────────────────

HAPLOGROUP_DB: dict[str, ResearchReport] = {
    "H1-T16189C!": H1_T16189C_DATA,
    "H1":          H1_T16189C_DATA,
}

def lookup(haplogroup: str) -> Optional[ResearchReport]:
    key = haplogroup.strip()
    return (
        HAPLOGROUP_DB.get(key)
        or HAPLOGROUP_DB.get(key.upper())
        or HAPLOGROUP_DB.get(key.lower())
    )


# ─────────────────────────────────────────────
# ENDPOINTIT
# ─────────────────────────────────────────────

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": app.version,
        "haplogroups_available": len(HAPLOGROUP_DB),
        "timestamp": now()
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

    Esimerkkejä:
      /api/research/search?lineage=mtDNA&region=Ireland
      /api/research/search?snp_quality=High&max_date_bp=3000
      /api/research/search?min_date_bp=5000&max_date_bp=10000
    """
    results = []

    for report in set(HAPLOGROUP_DB.values()):   # deduplicate aliaksista

        if lineage and report.lineage_type.lower() != lineage.lower():
            continue

        if region:
            r = region.lower()
            in_samples = any(
                r in s.region.lower() or r in s.country.lower()
                for s in report.ancient_samples
            )
            in_distribution = any(
                r in g.region.lower() for g in report.geographic_distribution
            )
            if not in_samples and not in_distribution:
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
            "haplogroup":          report.haplogroup,
            "lineage_type":        report.lineage_type,
            "ancient_sample_count": report.ancient_sample_count,
            "tmrca_estimate_bp":   report.confidence_model.tmrca_estimate_bp,
            "tmrca_min_bp":        report.confidence_model.tmrca_min_bp,
            "tmrca_max_bp":        report.confidence_model.tmrca_max_bp,
            "data_version":        report.data_version,
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
        raise HTTPException(
            status_code=404,
            detail=f"Haploryhmää '{haplogroup}' ei löydy. "
                   f"Saatavilla: {list(HAPLOGROUP_DB.keys())}"
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


# ─────────────────────────────────────────────
# KÄYNNISTYS
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
