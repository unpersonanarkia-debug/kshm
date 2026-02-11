# KSHM Copilot Instructions

## Project Overview

**Kadonneen Sukuhistorian Metsästäjä (KSHM)** is an archaeogenetic report generator that transforms user haplogroups (mtDNA and Y-DNA) into personalized, scientifically-grounded historical narratives. The system fetches haplogroup data from 15+ international sources, synthesizes findings into chronological stories, and delivers them as PDF reports via email.

## Architecture

KSHM follows a clean **5-stage pipeline** architecture:

```
Order Request → Data Fetch → Story Generation → PDF Rendering → Email Delivery
```

### Core Components

- **`main.py`**: FastAPI application; exposes `/api/order_report` and `/api/debug/haplogroup/{haplogroup}` endpoints. Orchestrates the complete pipeline.
- **`data_utils.py`** (608 lines): Multi-source data aggregator. Calls 10+ external APIs (YFull, FamilyTreeDNA, Haplogrep, Eupedia, ancientdna.info, PubMed, EBI, etc.). Returns unified data structure with ancient samples, regions, time depth, and reliability scores. **Critical**: No story generation here—only structured fact collection.
- **`story_utils.py`** (421 lines): Narrative builder. Receives haplogroup data and generates 7-part story structure (introduction, chronological migration, cultural context, famous people, hotspots, regional profiles, modern distribution). Respects language and tone settings.
- **`pdf_utils.py`** (259 lines): ReportLab-based PDF engine. Combines mtDNA and Y-DNA stories, applies typography, generates table of contents, handles multi-page layout.
- **`email_utils.py`** (190 lines): SMTP wrapper. Sends PDF via environment-configured mail server (default: `mail.kshm.fi`).
- **`i18n_utils.py`** (580 lines): Localization hub. Supports 50+ languages + tone profiles ("academic", "narrative", etc.). Controls all user-facing text and styling.

### Data Flow

1. **OrderRequest** validated by Pydantic (`name`, `email`, `haplogroup`, optional `haplogroup_y`, `language`, `tone`).
2. `fetch_full_haplogroup_data()` aggregates from multiple sources; normalizes into single schema with `ancient_samples` (list of findings), `regions`, `lineage_type`.
3. `generate_story_from_haplogroup()` builds narrative chapters; returns `story` dict with `title`, `sections` (each a content block).
4. `generate_pdf_from_story()` renders both mtDNA and Y-DNA sections; outputs to `generated_reports/` directory.
5. `send_email_with_pdf()` attaches PDF and sends.

## Critical Developer Patterns

### Error Handling
- **Validation first**: Haplogroup format validated with regex `^[A-Z0-9-]+$` at entry point.
- **Graceful fallbacks**: Missing Y-DNA doesn't block mtDNA report; partial data returns reliability score `< 1.0`.
- **HTTPException for API errors**: Use `status_code=404` for missing haplogroup, `500` for internal failures.

### Haplogroup Data Structure
When working with data returned from `fetch_full_haplogroup_data()`, expect:
```python
{
    "haplogroup": "H1",
    "lineage_type": "mtDNA",  # or "Y-DNA"
    "ancient_samples": [
        {"site": "Natufian", "age_bp": 12000, "date_range": "11500-12500 BP", "culture": "..."},
    ],
    "regions": ["Europe", "Levant"],
    "time_depth": "~12,500 years",
    "reliability_score": 0.92,
    "sources": ["YFull", "ancientdna.info"],
}
```

### Language & Tone Handling
- Always call `get_style_profile(lang, tone)` before building narrative sections.
- Supported languages: 50+ (fi, en, sv, de, fr, es, pt, ja, zh, ru, ar, etc.).
- Tone affects prose style: "academic" = citations+dates, "narrative" = storytelling elements.
- Never hardcode UI strings—use `get_text(key, lang, tone)` from `i18n_utils.py`.

### Environment Configuration
Required `.env` variables:
```
SMTP_SERVER=mail.kshm.fi
SMTP_PORT=587
SMTP_EMAIL=raportit@kshm.fi
SMTP_PASSWORD=<secret>
```
Use `os.getenv()` with sensible defaults for development.

## Testing & Debugging

### Quick Data Verification
Use the `/api/debug/haplogroup/{haplogroup}` endpoint to inspect raw aggregated data without generating a report:
```bash
curl http://localhost:8000/api/debug/haplogroup/H1 | jq .
```

### Local Workflow
1. Start backend: `cd backend && uvicorn main:app --reload`
2. Test with cURL or Postman:
   ```bash
   curl -X POST http://localhost:8000/api/order_report \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Test User",
       "email": "test@example.com",
       "haplogroup": "H1",
       "language": "en",
       "tone": "academic"
     }'
   ```
3. Check generated PDF in `backend/generated_reports/`.

### Common Issues
- **"Haploryhmälle X ei löytynyt tietoja"**: Data aggregation returned empty for that haplogroup. Check if source APIs are responding.
- **PDF generation timeout**: Large narratives with many ancient samples can be slow. Increase timeout or optimize `build_chronological_migration()`.
- **Email not sending**: Verify `.env` SMTP credentials and that `mail.kshm.fi` is reachable from deployment environment.

## Adding New Features

### Adding a New Data Source
1. Implement `fetch_from_newsource()` function in `data_utils.py`.
2. Add it to the `sources` list in `fetch_full_haplogroup_data()`.
3. Return data matching the unified schema (at minimum: `ancient_samples`, `regions`, `reliability_score`).

### Adding a New Language
1. Extend `SUPPORTED_LANGUAGES` in `i18n_utils.py`.
2. Add language name to `get_language_name()`.
3. Add full translation dict for all text keys (see existing structure in file).
4. Test with `/api/order_report` using `"language": "xx"`.

### Modifying Narrative Structure
Edit the `generate_story()` function in `story_utils.py`:
- Add new section with `build_<section_name>()` helper.
- Insert into `story["sections"]` list at desired position.
- Ensure section dict has `{"title": str, "content": str or list}` shape for PDF renderer.

## Dependencies & Deployment

- **Backend**: Python 3.9+, FastAPI 0.110.0, WeasyPrint/ReportLab for PDF, Jinja2 for templating.
- **External APIs**: 15+ sources (all via HTTP GET/requests); no authentication required for public endpoints.
- **Hosting**: Render, VPS, or any environment supporting Python + SMTP.

## Key Files to Know

| File | Purpose |
|------|---------|
| [backend/main.py](../backend/main.py) | API entry point & orchestrator |
| [backend/data_utils.py](../backend/data_utils.py) | Multi-source aggregation engine |
| [backend/story_utils.py](../backend/story_utils.py) | Narrative generation |
| [backend/pdf_utils.py](../backend/pdf_utils.py) | PDF rendering |
| [backend/i18n_utils.py](../backend/i18n_utils.py) | Localization & styling |
| [backend/email_utils.py](../backend/email_utils.py) | Email delivery |
| [README.md](../README.md) | Project vision & data sources |

---

**When in doubt**: The data layer (`data_utils`) must remain pure—no text generation. Stories (`story_utils`) transform data into narrative. PDFs and emails consume stories. Localization (`i18n_utils`) is consulted at every user-facing output point.
