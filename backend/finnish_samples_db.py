"""
finnish_samples_db.py — Suomi-fokus muinaisnäytetietokanta
KSHM-projekti

Yhdistää kolme datalähdettä:
  1. AADR v54.1 (.anno) — globaali perusta, Fennoskandia-näytteet
  2. media-4.xlsx (S4a) — 4 302 täyttä mitogenomia, 96 suomalaista
  3. RTF-käsinkerätty — Tuukkala (TU) + Eura/Luistari (JK), 110 näytettä

Kohteet ja aikakaudet:
  Levänluhta      300–800 jaa.    Rautakausi / merovingi (saamelaisyhteys)
  Luistari        600–1200 jaa.   Merovingi / viikinkiaika / ristiretki
  Tuukkala        1200–1400 jaa.  Ristiretki / keskiaika
  Hollola         1050–1300 jaa.  Ristiretki
  Pälkäne         1200–1700 jaa.  Ristiretki / keskiaika / uusi aika
  Porvoo          1300–1700 jaa.  Myöhäiskeskiaika / uusi aika
  Renko           1500–1800 jaa.  Myöhäiskeskiaika / uusi aika
  Turku           1550–1650 jaa.  Uusi aika
  Hamina          1700–1800 jaa.  Uusi aika

Julkaisut:
  Wessman et al. 2023 — Tuukkala, Luistari, Hollola, Levänluhta
  Lamnidis et al. 2018 — Levänluhta (JK-tunnukset)
  Klunk et al. 2019 — Levänluhta (DA-tunnukset)
  AADR v54.1 — globaali tausta

Käyttö:
  from finnish_samples_db import get_finnish_samples, get_site_samples
  samples = get_finnish_samples("U5b1b1a1")
  site    = get_site_samples("Levänluhta")
"""

from __future__ import annotations
import csv
import os
import re
import logging
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Tiedostopolut — ylikirjoitettavissa ympäristömuuttujilla
# ---------------------------------------------------------------------------

DEFAULT_XLSX_PATH = os.getenv("KSHM_XLSX_PATH",  "media-4.xlsx")
DEFAULT_ANNO_PATH = os.getenv("AADR_ANNO_PATH",   "v54_1_p1_1240K_public.anno")
DEFAULT_RTF_PATH  = os.getenv("KSHM_RTF_PATH",    
    "Muinaisnäyteluettelo-Tuukkala-Eura-Luistari-mtDNA-Haploryhmät.rtf")

# ---------------------------------------------------------------------------
# Kohdetiedot — koordinaatit ja kulttuurikonteksti
# ---------------------------------------------------------------------------

SITE_METADATA: Dict[str, Dict] = {
    "Levänluhta": {
        "lat": 63.02, "lon": 22.95,
        "municipality": "Isokyrö",
        "period": "300–800 jaa.",
        "culture": "Rautakausi / merovingi",
        "significance": (
            "Levänluhta on ainutlaatuinen suovesihauta Etelä-Pohjanmaalla. "
            "Lähes 100 yksilön jäännökset löydettiin 1800-luvulla ojitustöissä. "
            "DNA-analyysi osoitti, että osa kantajista on geneettisesti lähempänä "
            "nykyisiä saamelaisia kuin suomalaisia — poikkeuksellinen löytö. "
            "U5b1b1-linjat ovat erityisen edustettuina."
        ),
        "publication": "Lamnidis et al. 2018; Klunk et al. 2019; Wessman et al. 2023",
    },
    "Luistari": {
        "lat": 61.12, "lon": 22.08,
        "municipality": "Eura",
        "period": "600–1200 jaa.",
        "culture": "Merovingi / viikinkiaika / ristiretki",
        "significance": (
            "Euran Luistari on yksi Suomen merkittävimmistä rautakauden "
            "hautausmaista — yli 1 300 hautaa. Löydöt ovat poikkeuksellisen "
            "rikkaita: koruja, aseita, tekstiilejä. mtDNA-profiili on "
            "monipuolinen ja edustaa länsisuomalaista rautakauden väestöä."
        ),
        "publication": "Wessman et al. 2023",
    },
    "Tuukkala": {
        "lat": 61.70, "lon": 27.27,
        "municipality": "Mikkeli",
        "period": "1200–1400 jaa.",
        "culture": "Ristiretki / varhaishistoriallinen",
        "significance": (
            "Tuukkalan ristiretki- ja varhaiskeskiaikainen hautausmaa Mikkelissä. "
            "Näytteet edustavat Suur-Savon varhaista kristillistä väestöä. "
            "H-haploryhmät ovat hallitsevia — neoliittinen EEF-komponentti vahva."
        ),
        "publication": "Wessman et al. 2023",
    },
    "Hollola": {
        "lat": 60.99, "lon": 25.51,
        "municipality": "Hollola",
        "period": "1050–1300 jaa.",
        "culture": "Ristiretki",
        "significance": (
            "Hollolan ristiretkiaikainen kirkkomaa edustaa Päijät-Hämeen "
            "varhaista kristillistä väestöä. U4-linjat poikkeuksellisen yleisiä "
            "— viittaa itäiseen vaikutukseen."
        ),
        "publication": "Wessman et al. 2023",
    },
    "Pälkäne": {
        "lat": 61.33, "lon": 24.28,
        "municipality": "Pälkäne",
        "period": "1200–1700 jaa.",
        "culture": "Ristiretki / keskiaika / uusi aika",
        "significance": "Pirkanmaan pitkä jatkumo ristiretkiajalta uuteen aikaan.",
        "publication": "Wessman et al. 2023",
    },
    "Porvoo": {
        "lat": 60.39, "lon": 25.66,
        "municipality": "Porvoo",
        "period": "1300–1700 jaa.",
        "culture": "Myöhäiskeskiaika / uusi aika",
        "significance": (
            "Porvoon kaupunkikirkkohautausmaa edustaa eteläsuomalaista "
            "kaupunkiväestöä — monipuolinen haploryhmäprofiili."
        ),
        "publication": "Wessman et al. 2023",
    },
    "Renko": {
        "lat": 60.88, "lon": 24.28,
        "municipality": "Hämeenlinna",
        "period": "1500–1800 jaa.",
        "culture": "Myöhäiskeskiaika / uusi aika",
        "significance": "Kanta-Hämeen maaseutuväestö myöhäiseltä ajalta.",
        "publication": "Wessman et al. 2023",
    },
    "Turku": {
        "lat": 60.45, "lon": 22.27,
        "municipality": "Turku",
        "period": "1550–1650 jaa.",
        "culture": "Uusi aika",
        "significance": "Turun kaupunkiväestö 1500–1600-luvulta.",
        "publication": "Wessman et al. 2023",
    },
    "Hamina": {
        "lat": 60.57, "lon": 27.20,
        "municipality": "Hamina",
        "period": "1700–1800 jaa.",
        "culture": "Uusi aika",
        "significance": (
            "Haminan hautausmaa 1700–1800-luvulta. C4a1a1 (Aasian linja) "
            "poikkeuksellinen löytö — viittaa Venäjältä tai Aasiasta saapuneisiin."
        ),
        "publication": "Wessman et al. 2023",
    },
}

# JK-tunnusten kontekstitieto
JK_SITE_MAP = {
    # Lamnidis et al. 2018 (Nature Comm.) — Levänluhta
    "JK1927": "Levänluhta",
    "JK1930": "Levänluhta",
    "JK1932": "Levänluhta",
    "JK1938": "Levänluhta",
    "JK1941": "Levänluhta",
    "JK1945": "Levänluhta",
    "JK1946": "Levänluhta",
    "JK1947": "Levänluhta",
    "JK1948": "Levänluhta",
    "JK1950": "Levänluhta",
    "JK1952": "Levänluhta",
    "JK1953": "Levänluhta",
    "JK1954": "Levänluhta",
    "JK1959": "Levänluhta",
    "JK1960": "Levänluhta",
    "JK1961": "Levänluhta",
    "JK1962": "Levänluhta",
    "JK1963": "Levänluhta",
    "JK1964": "Levänluhta",
    "JK1965": "Levänluhta",
    "JK1966": "Levänluhta",
    "JK1967": "Levänluhta",
    "JK1968": "Levänluhta",
    "JK1969": "Levänluhta",
    "JK1970": "Levänluhta",
    "JK2065": "Levänluhta",
    "JK2066": "Levänluhta",
    "JK2067": "Levänluhta",
    # Wessman et al. 2023 — Euran Luistari
    "JK2285": "Luistari",
    "JK2286": "Luistari",
    "JK2288": "Luistari",
    "JK2289": "Luistari",
    "JK2290": "Luistari",
}

# TU = Tuukkala
def _tu_site(sample_id: str) -> str:
    return "Tuukkala" if sample_id.startswith("TU") else "Unknown"


# ---------------------------------------------------------------------------
# Parseri: xlsx
# ---------------------------------------------------------------------------

def _parse_xlsx(xlsx_path: str) -> List[Dict]:
    """Parsii media-4.xlsx S4a-taulukosta Suomi+Fennoskandia-näytteet."""
    try:
        import openpyxl
    except ImportError:
        logger.warning("openpyxl ei ole asennettu — xlsx ohitetaan")
        return []

    try:
        wb = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True)
    except FileNotFoundError:
        logger.warning(f"xlsx ei löydy: {xlsx_path}")
        return []

    ws = wb["S4a pop database"]
    rows = list(ws.iter_rows(values_only=True))
    headers = rows[1]

    TARGET_COUNTRIES = {
        "Finland", "Estonia", "Latvia", "Lithuania",
        "Sweden", "Norway", "Denmark",
    }

    samples = []
    for row in rows[2:]:
        if not any(row):
            continue
        s = dict(zip(headers, row))
        country = str(s.get("Country", "") or "")
        location = str(s.get("Location", "") or "")
        if not any(c in country or c in location for c in TARGET_COUNTRIES):
            continue

        mt = str(s.get("mtDNA haplogroup", "") or "").strip()
        if not mt or mt in ("None", "?"):
            continue

        # Päättele kohdenimi sijainnista
        loc_str = str(s.get("Location", "") or "").strip()
        site = _guess_site(loc_str, str(s.get("Other ID", "") or ""))

        # Päivämäärä: muunna "300-800 AD" → keskiarvo CE
        date_str = str(s.get("Date", "") or "").strip()
        date_ce = _parse_date_ce(date_str)

        meta = SITE_METADATA.get(site, {})
        samples.append({
            "id":          str(s.get("Other ID", "") or "").strip() or str(s.get("GenBank ID", "") or ""),
            "site":        site,
            "location":    loc_str,
            "municipality": meta.get("municipality", ""),
            "country":     country,
            "lat":         meta.get("lat"),
            "lon":         meta.get("lon"),
            "date_str":    date_str,
            "date_ce":     date_ce,
            "culture":     str(s.get("Culture or age", "") or "").strip(),
            "mt":          mt,
            "publication": str(s.get("Reference", "") or "").strip(),
            "source":      "xlsx_media4",
        })

    wb.close()
    return samples


def _guess_site(location: str, sample_id: str) -> str:
    """Päättelee arkeologisen kohteen sijainnin tai näyte-ID:n perusteella."""
    import re as _re
    loc = location.lower()

    # Täsmällinen sanamatch (vältetään Turlojiske → Tuukkala -virhe)
    for site in SITE_METADATA:
        pattern = r'\b' + _re.escape(site.lower()) + r'\b'
        if _re.search(pattern, loc):
            return site

    sid = sample_id.upper()
    if sid in JK_SITE_MAP:
        return JK_SITE_MAP[sid]
    # TU-prefix = Tuukkala vain jos ID on muotoa TU\d+
    if _re.match(r'^TU\d+$', sid):
        return "Tuukkala"
    return location or "Unknown"


def _parse_date_ce(date_str: str) -> Optional[int]:
    """
    Muuntaa päivämäärämerkkijonon CE-vuodeksi (negatiivinen = BCE).
    Esimerkkejä:
      "300-800 AD"       → 550
      "1200–1400 AD"     → 1300
      "540-380 BC"       → -460
      "39160-36550 BC"   → -37855
    """
    if not date_str:
        return None
    # Etsi numerot
    nums = re.findall(r'\d+', date_str.replace(',', ''))
    if not nums:
        return None
    vals = [int(n) for n in nums[:2]]
    avg = sum(vals) // len(vals)
    if "BC" in date_str.upper():
        return -avg
    return avg


# ---------------------------------------------------------------------------
# Parseri: RTF
# ---------------------------------------------------------------------------

def _parse_rtf(rtf_path: str) -> List[Dict]:
    """Parsii RTF-muisnäyteluettelon TU/JK-näytteet."""
    try:
        with open(rtf_path, "rb") as f:
            raw = f.read().decode("latin-1")
    except FileNotFoundError:
        logger.warning(f"RTF ei löydy: {rtf_path}")
        return []

    # Dekoodaa RTF
    raw = re.sub(r"\\'([0-9a-fA-F]{2})",
                 lambda m: bytes.fromhex(m.group(1)).decode("latin-1"), raw)
    raw = re.sub(r"\\[a-zA-Z]+\-?\d*\s?", " ", raw)
    raw = re.sub(r"[{}\\]", " ", raw)

    pairs = re.findall(r"(TU\d+|JK\d+)\s+([A-Za-z][A-Za-z0-9+@\*\']+)", raw)

    # Deduplikoi — viimeinen esiintymä voittaa (tarkempi kladi)
    seen: Dict[str, str] = {}
    for sid, hg in pairs:
        seen[sid] = hg

    samples = []
    for sid, mt in seen.items():
        site = JK_SITE_MAP.get(sid, _tu_site(sid))
        meta = SITE_METADATA.get(site, {})
        samples.append({
            "id":          sid,
            "site":        site,
            "location":    meta.get("municipality", site),
            "municipality": meta.get("municipality", ""),
            "country":     "Finland",
            "lat":         meta.get("lat"),
            "lon":         meta.get("lon"),
            "date_str":    meta.get("period", ""),
            "date_ce":     _period_to_midpoint(meta.get("period", "")),
            "culture":     meta.get("culture", ""),
            "mt":          mt,
            "publication": meta.get("publication", ""),
            "source":      "rtf_manual",
        })

    return samples


def _period_to_midpoint(period: str) -> Optional[int]:
    """Muuntaa "300–800 jaa." → 550."""
    nums = re.findall(r'\d+', period)
    if len(nums) >= 2:
        return (int(nums[0]) + int(nums[1])) // 2
    return None


# ---------------------------------------------------------------------------
# Indeksi — singleton
# ---------------------------------------------------------------------------

class _FinnishIndex:
    def __init__(self):
        self._by_mt:   Dict[str, List[Dict]] = defaultdict(list)
        self._by_site: Dict[str, List[Dict]] = defaultdict(list)
        self._all:     List[Dict] = []
        self._loaded = False

    def _load(self,
              xlsx_path: str = DEFAULT_XLSX_PATH,
              rtf_path:  str = DEFAULT_RTF_PATH) -> None:
        if self._loaded:
            return

        logger.info("Ladataan Finnish samples DB...")
        all_samples: List[Dict] = []

        # 1. xlsx
        xlsx_samples = _parse_xlsx(xlsx_path)
        all_samples.extend(xlsx_samples)
        logger.info(f"  xlsx: {len(xlsx_samples)} näytettä")

        # 2. RTF — lisää vain ne joita xlsx:ssä ei ole (deduplikoi ID:llä)
        xlsx_ids = {s["id"] for s in xlsx_samples}
        rtf_samples = _parse_rtf(rtf_path)
        new_rtf = [s for s in rtf_samples if s["id"] not in xlsx_ids]
        all_samples.extend(new_rtf)
        logger.info(f"  RTF (uudet): {len(new_rtf)} näytettä")

        # Indeksoi
        by_mt:   Dict[str, List[Dict]] = defaultdict(list)
        by_site: Dict[str, List[Dict]] = defaultdict(list)
        seen_ids: set = set()

        for s in all_samples:
            # Deduplikoi ID:llä
            if s["id"] in seen_ids:
                continue
            seen_ids.add(s["id"])

            mt = s.get("mt", "")
            if mt:
                by_mt[mt].append(s)
            site = s.get("site", "")
            if site:
                by_site[site].append(s)

        self._by_mt   = by_mt
        self._by_site = by_site
        self._all     = list({s["id"]: s for s in all_samples}.values())
        self._loaded  = True

        logger.info(f"Finnish DB ladattu: {len(self._all)} uniikkia näytettä, "
                    f"{len(by_mt)} haploryhmää, {len(by_site)} kohdetta")

    def get_by_mt(self)   -> Dict[str, List[Dict]]: self._load(); return self._by_mt
    def get_by_site(self) -> Dict[str, List[Dict]]: self._load(); return self._by_site
    def get_all(self)     -> List[Dict]:             self._load(); return self._all


_INDEX = _FinnishIndex()


# ---------------------------------------------------------------------------
# Etuliitehaku
# ---------------------------------------------------------------------------

def _prefix_lookup(index: Dict[str, List[Dict]], haplogroup: str) -> List[Dict]:
    """Pisin etuliiteosuma — sama logiikka kuin aadr_db.py:ssä."""
    hg_up = haplogroup.upper().strip()

    # Täsmällinen
    for key, samples in index.items():
        if key.upper() == hg_up:
            return samples

    # Pisin etuliite
    best_key, best_len = None, 0
    for key in index:
        k = key.upper()
        if hg_up.startswith(k) and len(k) > best_len:
            best_key, best_len = key, len(k)

    return index[best_key] if best_key else []


# ---------------------------------------------------------------------------
# Julkinen API
# ---------------------------------------------------------------------------

def get_finnish_samples(
    haplogroup: str,
    n: int = 20,
) -> List[Dict]:
    """
    Palauttaa suomalaiset muinaisnäytteet haploryhmälle kronologisessa järjestyksessä.

    Args:
        haplogroup: Haploryhmä (esim. "U5b1b1a1", "H1c", "K1a4a1b")
        n:          Maksimimäärä

    Returns:
        Lista näytteistä vanhimmasta uusimpaan.
    """
    index = _INDEX.get_by_mt()
    samples = _prefix_lookup(index, haplogroup)
    dated   = sorted([s for s in samples if s["date_ce"] is not None], key=lambda x: x["date_ce"])
    undated = [s for s in samples if s["date_ce"] is None]
    return (dated + undated)[:n]


def get_site_samples(
    site: str,
    haplogroup: Optional[str] = None,
) -> List[Dict]:
    """
    Palauttaa kohteen kaikki näytteet.
    Valinnaisesti suodattaa haploryhmän mukaan.

    Kohteet: Levänluhta, Luistari, Tuukkala, Hollola,
             Pälkäne, Porvoo, Renko, Turku, Hamina
    """
    index = _INDEX.get_by_site()
    samples = index.get(site, [])
    if haplogroup:
        hg_up = haplogroup.upper()
        samples = [s for s in samples if s.get("mt", "").upper().startswith(hg_up)]
    return sorted(samples, key=lambda x: x.get("date_ce") or 9999)


def get_site_metadata(site: str) -> Optional[Dict]:
    """Palauttaa kohteen metatiedot (koordinaatit, kuvaus, julkaisu)."""
    return SITE_METADATA.get(site)


def get_haplogroup_sites(haplogroup: str) -> List[Tuple[str, int]]:
    """
    Palauttaa kohteet joissa haploryhmä esiintyy, näytemäärän mukaan.
    Hyödyllinen narratiivin rakentamisessa: "tätä linjaa on löydetty X:stä ja Y:stä"
    """
    samples = get_finnish_samples(haplogroup, n=999)
    site_counts: Dict[str, int] = defaultdict(int)
    for s in samples:
        site_counts[s.get("site", "?")] += 1
    return sorted(site_counts.items(), key=lambda x: -x[1])


def list_sites() -> List[str]:
    """Palauttaa kaikki indeksoidut kohteet."""
    return sorted(_INDEX.get_by_site().keys())


def get_all_finnish_samples() -> List[Dict]:
    """Palauttaa kaikki näytteet."""
    return _INDEX.get_all()


def get_sample_count(haplogroup: str) -> int:
    """Palauttaa näytemäärän haploryhmälle."""
    return len(get_finnish_samples(haplogroup, n=9999))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    cmd = sys.argv[1] if len(sys.argv) > 1 else "stats"

    if cmd == "stats":
        all_s = get_all_finnish_samples()
        print(f"\nFinnish DB yhteensä: {len(all_s)} näytettä")
        print(f"\nKohteet:")
        for site in list_sites():
            n = len(get_site_samples(site))
            meta = get_site_metadata(site) or {}
            print(f"  {site:15} {n:3} näytettä  ({meta.get('period','')})")

    elif cmd == "hg":
        hg = sys.argv[2] if len(sys.argv) > 2 else "U5b1"
        samples = get_finnish_samples(hg)
        print(f"\n{hg}: {len(samples)} suomalaista näytettä\n")
        for s in samples:
            print(f"  [{s.get('date_ce','?'):>5} CE] {s['id']:25} {s['site']:12} {s['mt']}")

    elif cmd == "site":
        site = sys.argv[2] if len(sys.argv) > 2 else "Levänluhta"
        samples = get_site_samples(site)
        meta = get_site_metadata(site) or {}
        print(f"\n{site} ({meta.get('period','')}):")
        print(f"  {meta.get('significance','')}\n")
        for s in samples:
            print(f"  [{s.get('date_ce','?'):>5} CE] {s['id']:25} {s['mt']}")
