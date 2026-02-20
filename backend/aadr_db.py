"""
aadr_db.py — Allen Ancient DNA Resource (AADR) v54.1 integraatio
KSHM-projekti

Parsii AADR .anno-tiedoston ja tarjoaa:
  - get_nearest_samples(haplogroup, n) → lähimmät aDNA-näytteet kronologisesti
  - get_oldest_sample(haplogroup)      → vanhin tunnettu näyte kladissa
  - get_samples_by_region(haplogroup, country) → aluesuodatus
  - haplogroup_prefix_search(hg)       → etuliitehaku koko indeksistä

Käyttö:
  from aadr_db import get_nearest_samples
  samples = get_nearest_samples("U5b1", n=5)

HUOM: Ranis-luolan U5b1 (~45 000 BCE) ei ole vielä v54.1:ssä.
      Se lisätään MANUAL_ADDITIONS-dictiin alla.
"""

from __future__ import annotations
import csv
import os
import logging
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Vakiot
# ---------------------------------------------------------------------------

# Oletettu sijainti — voidaan ylikirjoittaa ympäristömuuttujalla
DEFAULT_ANNO_PATH = os.getenv(
    "AADR_ANNO_PATH",
    "v54_1_p1_1240K_public.anno"
)

# Sarakkeiden nimet (v54.1)
_COL_ID       = "Genetic ID"
_COL_GROUP    = "Group ID"
_COL_LOC      = "Locality"
_COL_COUNTRY  = "Political Entity"
_COL_LAT      = "Lat."
_COL_LON      = "Long."
_COL_PUB      = "Publication"
_COL_MT       = "mtDNA haplogroup if >2x or published"
_COL_Y_TERM   = "Y haplogroup (manual curation in terminal mutation format)"
_COL_Y_ISOGG  = "Y haplogroup (manual curation in ISOGG format)"

# ---------------------------------------------------------------------------
# Manuaaliset lisäykset — julkaisut jotka eivät vielä ole v54.1:ssä
# ---------------------------------------------------------------------------

MANUAL_ADDITIONS: List[Dict] = [
    {
        # Conard et al. 2024, Nature — Ranis-luola, Saksa
        # GünzenhauserHöhle / Ilsenhöhle, vanhimmat anatomisesti modernit eurooppalaiset
        "id":          "Ranis-GH4-manual",
        "group":       "Germany_Ranis_45000BP",
        "location":    "Ranis Cave (Ilsenhöhle), Thuringia",
        "country":     "Germany",
        "lat":         50.65,
        "lon":         11.57,
        "date_bce":    -43050,   # ~45 000 BP
        "publication": "Pearce2024Nature / Welker2024Nature",
        "mt":          "U5b1",
        "y":           None,
        "lineage_fit": "mtDNA",
        "notes":       "Vanhimpia anatomisesti moderneja eurooppalaisia. U5b1 ankkuroi linjan >45 000 vuotta sitten.",
        "source":      "manual",
    },
]


# ---------------------------------------------------------------------------
# Tyypit
# ---------------------------------------------------------------------------

AADRSample = Dict  # ks. _parse_row


# ---------------------------------------------------------------------------
# Parseri
# ---------------------------------------------------------------------------

def _bp_to_bce(bp_str: str) -> Optional[int]:
    """Muuntaa BP-arvon (vuotta ennen 1950) BCE-vuodeksi."""
    try:
        return round(1950 - float(bp_str))
    except (ValueError, TypeError):
        return None


def _parse_row(row: Dict, cols: List[str]) -> Optional[AADRSample]:
    """
    Parsii yhden .anno-rivin AADRSample-dictiksi.
    Palauttaa None jos mt tai y puuttuu kokonaan.
    """
    mt = row.get(_COL_MT, "").strip()
    y  = row.get(_COL_Y_TERM, "").strip()
    y_isogg = row.get(_COL_Y_ISOGG, "").strip()

    # Normalisoi tyhjät arvot
    mt = None if (not mt or mt == ".." or mt.startswith("n/a") or mt == "Neanderthal") else mt
    y  = None if (not y  or y  == ".." or y.startswith("n/a")) else y
    y_isogg = None if (not y_isogg or y_isogg == "..") else y_isogg

    if mt is None and y is None:
        return None

    try:
        lat = float(row.get(_COL_LAT, "").strip())
        lon = float(row.get(_COL_LON, "").strip())
    except (ValueError, TypeError):
        lat, lon = None, None

    date_col = next((c for c in cols if "Date mean" in c), None)
    bce = _bp_to_bce(row.get(date_col, "")) if date_col else None

    return {
        "id":          row.get(_COL_ID, "").strip(),
        "group":       row.get(_COL_GROUP, "").strip(),
        "location":    row.get(_COL_LOC, "").strip(),
        "country":     row.get(_COL_COUNTRY, "").strip(),
        "lat":         lat,
        "lon":         lon,
        "date_bce":    bce,
        "publication": row.get(_COL_PUB, "").strip(),
        "mt":          mt,
        "y":           y,
        "y_isogg":     y_isogg,
        "source":      "aadr_v54",
    }


# ---------------------------------------------------------------------------
# Indeksi — ladataan kerran, käytetään monesti
# ---------------------------------------------------------------------------

class _AADRIndex:
    """
    Sisäinen singleton-indeksi. Ladataan laiskasti ensimmäisellä kutsulla.
    Indeksoi näytteet sekä mtDNA- että Y-DNA-haploryhmän mukaan.
    """

    def __init__(self):
        self._by_mt: Dict[str, List[AADRSample]] = defaultdict(list)
        self._by_y:  Dict[str, List[AADRSample]] = defaultdict(list)
        self._loaded = False
        self._anno_path: Optional[str] = None

    def _load(self, anno_path: str) -> None:
        if self._loaded and self._anno_path == anno_path:
            return

        logger.info(f"Ladataan AADR: {anno_path}")
        by_mt: Dict[str, List] = defaultdict(list)
        by_y:  Dict[str, List] = defaultdict(list)

        try:
            with open(anno_path, encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter="\t")
                cols = reader.fieldnames or []
                for row in reader:
                    sample = _parse_row(row, cols)
                    if sample is None:
                        continue
                    if sample["mt"]:
                        by_mt[sample["mt"]].append(sample)
                    if sample["y"]:
                        by_y[sample["y"]].append(sample)
        except FileNotFoundError:
            logger.warning(f"AADR-tiedostoa ei löydy: {anno_path}")

        # Lisää manuaaliset näytteet
        for s in MANUAL_ADDITIONS:
            if s.get("mt"):
                by_mt[s["mt"]].append(s)
            if s.get("y"):
                by_y[s["y"]].append(s)

        self._by_mt = by_mt
        self._by_y  = by_y
        self._loaded = True
        self._anno_path = anno_path

        total = sum(len(v) for v in by_mt.values())
        logger.info(f"AADR ladattu: {total} mtDNA-näytettä, {sum(len(v) for v in by_y.values())} Y-näytettä")

    def get_mt(self, anno_path: str) -> Dict[str, List[AADRSample]]:
        self._load(anno_path)
        return self._by_mt

    def get_y(self, anno_path: str) -> Dict[str, List[AADRSample]]:
        self._load(anno_path)
        return self._by_y


_INDEX = _AADRIndex()


# ---------------------------------------------------------------------------
# Etuliitehaku — löytää näytteet myös alakladeille
# ---------------------------------------------------------------------------

def _prefix_lookup(
    index: Dict[str, List[AADRSample]],
    haplogroup: str,
    min_prefix_len: int = 2,
) -> List[AADRSample]:
    """
    Etsii näytteet haploryhmälle etuliitehaulla.

    Prioriteetti: pisin täsmäävä avain voittaa (tarkempi kladi ensin),
    mutta myös kaikkien yläkladien näytteet palautetaan jos omia ei löydy.

    Esimerkki:
        "U5b1c2" → etsii: U5b1c2, U5b1c, U5b1, U5b, U5
        palauttaa ensimmäisen ei-tyhjän osuman pitkimmästä lyhyimpään
    """
    hg_up = haplogroup.upper().strip()

    # 1. Täsmällinen osuma
    for key, samples in index.items():
        if key.upper() == hg_up:
            return samples

    # 2. Pisin etuliiteosuma (tarkempi kladi = oma data)
    best_key = None
    best_len = 0
    for key in index:
        k = key.upper()
        if hg_up.startswith(k) and len(k) > best_len and len(k) >= min_prefix_len:
            best_key = key
            best_len = len(k)

    if best_key:
        return index[best_key]

    return []


def _all_prefix_matches(
    index: Dict[str, List[AADRSample]],
    haplogroup: str,
) -> List[AADRSample]:
    """
    Palauttaa KAIKKI näytteet joiden avain alkaa haplogroup-etuliitteellä.
    Käytetään kun haetaan koko kladipuun näytteitä (esim. kaikki U5).
    """
    hg_up = haplogroup.upper().strip()
    result = []
    seen_ids: set = set()
    for key, samples in index.items():
        if key.upper().startswith(hg_up):
            for s in samples:
                if s["id"] not in seen_ids:
                    result.append(s)
                    seen_ids.add(s["id"])
    return result


# ---------------------------------------------------------------------------
# Julkinen API
# ---------------------------------------------------------------------------

def get_nearest_samples(
    haplogroup: str,
    n: int = 10,
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
    require_coordinates: bool = False,
) -> List[AADRSample]:
    """
    Palauttaa n lähintä aDNA-näytettä haploryhmälle kronologisessa järjestyksessä
    (vanhin ensin).

    Args:
        haplogroup:          Haploryhmä (esim. "U5b1", "H1-T16189C", "N1a1a1")
        n:                   Palautettavien näytteiden maksimimäärä
        lineage:             "mt" (mtDNA) tai "y" (Y-DNA)
        anno_path:           AADR .anno-tiedoston polku
        require_coordinates: Jos True, palauttaa vain näytteet joilla on koordinaatit

    Returns:
        Lista AADRSample-dicteistä, järjestettynä vanhimmasta uusimpaan.
        Tyhjä lista jos ei löydy.
    """
    index = _INDEX.get_mt(anno_path) if lineage == "mt" else _INDEX.get_y(anno_path)
    samples = _prefix_lookup(index, haplogroup)

    if require_coordinates:
        samples = [s for s in samples if s["lat"] is not None and s["lon"] is not None]

    # Järjestä: vanhin ensin, tunnistamaton päivämäärä loppuun
    dated = [s for s in samples if s["date_bce"] is not None]
    undated = [s for s in samples if s["date_bce"] is None]
    dated.sort(key=lambda x: x["date_bce"])

    return (dated + undated)[:n]


def get_oldest_sample(
    haplogroup: str,
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
) -> Optional[AADRSample]:
    """Palauttaa vanhimman tunnetun näytteen kladille."""
    samples = get_nearest_samples(haplogroup, n=1, lineage=lineage, anno_path=anno_path)
    return samples[0] if samples else None


def get_samples_by_region(
    haplogroup: str,
    country: str,
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
) -> List[AADRSample]:
    """
    Suodattaa näytteet maan perusteella.
    Hyödyllinen kun halutaan esim. kaikki Suomeen tai Balttiaan liittyvät näytteet.
    """
    index = _INDEX.get_mt(anno_path) if lineage == "mt" else _INDEX.get_y(anno_path)
    samples = _prefix_lookup(index, haplogroup)
    return [s for s in samples if country.lower() in s["country"].lower()]


def get_clade_tree_samples(
    haplogroup_prefix: str,
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
    max_total: int = 50,
) -> List[AADRSample]:
    """
    Palauttaa kaikki näytteet koko kladipuulle (esim. kaikki U5*).
    Käytetään kun rakennetaan liikereitti koko haaralle.
    Rajattu max_total näytteeseen, kronologisessa järjestyksessä.
    """
    index = _INDEX.get_mt(anno_path) if lineage == "mt" else _INDEX.get_y(anno_path)
    samples = _all_prefix_matches(index, haplogroup_prefix)
    dated = sorted([s for s in samples if s["date_bce"] is not None], key=lambda x: x["date_bce"])
    undated = [s for s in samples if s["date_bce"] is None]
    return (dated + undated)[:max_total]


def get_sample_count(
    haplogroup: str,
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
) -> int:
    """Palauttaa näytemäärän haploryhmälle."""
    index = _INDEX.get_mt(anno_path) if lineage == "mt" else _INDEX.get_y(anno_path)
    return len(_prefix_lookup(index, haplogroup))


def list_available_clades(
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
) -> List[Tuple[str, int]]:
    """
    Palauttaa kaikki indeksoidut kladit näytemäärän mukaan järjestettynä.
    Hyödyllinen debuggaukseen ja UI:n kladivalitsimeen.
    """
    index = _INDEX.get_mt(anno_path) if lineage == "mt" else _INDEX.get_y(anno_path)
    return sorted([(k, len(v)) for k, v in index.items()], key=lambda x: -x[1])


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    import json

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    hg   = sys.argv[1] if len(sys.argv) > 1 else "U5b1"
    lin  = sys.argv[2] if len(sys.argv) > 2 else "mt"
    path = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_ANNO_PATH

    samples = get_nearest_samples(hg, n=10, lineage=lin, anno_path=path)
    print(f"\nHaploryhmä: {hg} ({lin}) — {get_sample_count(hg, lin, path)} näytettä AADR:ssä\n")
    for s in samples:
        print(f"  [{s['date_bce']} BCE] {s['id']} — {s['location']}, {s['country']}")
        print(f"    mt:{s['mt']} | y:{s['y']} | julkaisu:{s['publication'][:60]}")
        print()
