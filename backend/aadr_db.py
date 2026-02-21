"""
aadr_db.py — Allen Ancient DNA Resource (AADR) integraatio
KSHM-projekti

Tukee sekä AADR v54.1 että v62.0 (ja myöhemmät versiot automaattisesti).
Sarakerakenne havaitaan automaattisesti — ei kiinteitä sarakeindeksejä.

Parsii .anno-tiedoston ja tarjoaa:
  get_nearest_samples(haplogroup, n, lineage)  → n lähintä aDNA-näytettä
  get_oldest_sample(haplogroup, lineage)        → vanhin tunnettu näyte
  get_samples_by_region(haplogroup, country)    → aluesuodatus
  get_clade_tree_samples(prefix, lineage)       → koko kladipuun näytteet
  get_sample_count(haplogroup, lineage)         → näytemäärä
  list_available_clades(lineage)                → kaikki kladit järjestettyinä

v62 vs v54.1 pääerot:
  - Näytteitä: 21 945 (v62) vs 9 253 (v54.1)
  - Y-DNA: 8 516 (v62) vs 507 (v54.1)  ← 17x enemmän
  - Y-sarakkeet eri nimillä (havaitaan automaattisesti)
  - Date-sarake: eri pitkä nimi (havaitaan automaattisesti)

Ympäristömuuttujat:
  AADR_ANNO_PATH  — polku .anno-tiedostoon (oletus: v62_0_HO_public.anno)

Käyttö:
  from aadr_db import get_nearest_samples
  samples = get_nearest_samples("U5b1", n=5)
  samples = get_nearest_samples("N-L550", n=10, lineage="y")
"""

from __future__ import annotations
import csv
import os
import logging
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Tiedostopolku — v62 ensisijainen, v54.1 varavaihto
# ---------------------------------------------------------------------------

DEFAULT_ANNO_PATH = os.getenv("AADR_ANNO_PATH", "v62_0_HO_public.anno")

# ---------------------------------------------------------------------------
# Sarakenimi-kandidaatit (v54.1 ja v62 käyttävät eri nimiä)
# ---------------------------------------------------------------------------

_MT_COLS = [
    "mtDNA haplogroup if >2x or published",
    "mtDNA haplogroup",
]
_Y_TERM_COLS = [
    # v62
    "Y haplogroup in terminal mutation notation automatically called based on Yfull with the software described in Lazaridis et al. Science 2022",
    # v54.1
    "Y haplogroup (manual curation in terminal mutation format)",
    "Y haplogroup in terminal mutation notation",
]
_Y_ISOGG_COLS = [
    # v62 (extra space intentional — matches actual header)
    "Y haplogroup  in ISOGG v15.73 notation automatically called based on Yfull with the software described in Lazaridis et al. Science 2022",
    # v54.1
    "Y haplogroup (manual curation in ISOGG format)",
    "Y haplogroup in ISOGG format",
]
_Y_MANUAL_COLS = [
    "Y haplogroup manually called if different from automatic",
    "Y haplogroup (manual override)",
]
_DATE_COLS = [
    "Date mean in BP in years before 1950 CE [OxCal mu for a direct radiocarbon date, and average of range for a contextual date]",
    "Date mean in BP",
]
_ID_COLS      = ["Genetic ID", "Genetic_ID"]
_GRP_COLS     = ["Group ID", "Group_ID"]
_LOC_COLS     = ["Locality", "Site"]
_CTR_COLS     = ["Political Entity", "Country"]
_LAT_COLS     = ["Lat.", "Lat", "Latitude"]
_LON_COLS     = ["Long.", "Long", "Longitude"]
_PUB_COLS     = ["Publication abbreviation", "Publication", "Reference"]


def _find_col(fieldnames: List[str], candidates: List[str]) -> Optional[str]:
    fn_set = set(fieldnames)
    for c in candidates:
        if c in fn_set:
            return c
    # Osittainen täsmäys varmuuden vuoksi
    for c in candidates:
        for fn in fieldnames:
            if c.lower() in fn.lower():
                return fn
    return None


# ---------------------------------------------------------------------------
# Manuaaliset lisäykset
# ---------------------------------------------------------------------------

MANUAL_ADDITIONS: List[Dict] = [
    {
        "id": "Ranis-GH4-manual", "group": "Germany_Ranis_45000BP",
        "location": "Ranis Cave (Ilsenhöhle), Thuringia", "country": "Germany",
        "lat": 50.65, "lon": 11.57, "date_bce": -43050,
        "publication": "Pearce2024Nature / Welker2024Nature",
        "mt": "U5b1", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Vanhimpia anatomisesti moderneja eurooppalaisia. U5b1 >45 000 BCE.",
        "source": "manual",
    },
    {
        "id": "Ust_Ishim-manual", "group": "Russia_UstIshim_43000BP",
        "location": "Ust'-Ishim, Siberia", "country": "Russia",
        "lat": 57.71, "lon": 71.36, "date_bce": -43070,
        "publication": "Fu et al. 2014",
        "mt": "R", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Vanhin täysin sekvensoitu moderni ihminen. R* = kaikkien ei-afrikkalaisten mtDNA-linjojen katto.",
        "source": "media4_S4b",
    },
    {
        "id": "Kostenki14-manual", "group": "Russia_Kostenki_35000BP",
        "location": "Kostenki, Voronezh Oblast", "country": "Russia",
        "lat": 51.39, "lon": 39.06, "date_bce": -35523,
        "publication": "Seguin-Orlando et al. 2014",
        "mt": "U2", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Vanhin tunnettu U-haaran näyte.",
        "source": "media4_S4b",
    },
    {
        "id": "Sunghir1-manual", "group": "Russia_Sunghir_30000BP",
        "location": "Sunghir, Vladimir Oblast", "country": "Russia",
        "lat": 56.19, "lon": 40.53, "date_bce": -30872,
        "publication": "Sikora et al. 2017",
        "mt": "U8c", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Vanhin U8-haaran näyte. U8c on K:n (U8b) sisarhaara.",
        "source": "media4_S4b",
    },
    {
        "id": "KremsWA3-manual", "group": "Austria_Krems_29000BP",
        "location": "Krems-Wachtberg", "country": "Austria",
        "lat": 48.41, "lon": 15.60, "date_bce": -29020,
        "publication": "Fu et al. 2016",
        "mt": "U5", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Vanhin U5 Keski-Euroopasta. Gravettilainen kulttuuri.",
        "source": "media4_S4b",
    },
    {
        "id": "Paglicci133-manual", "group": "Italy_Paglicci_27000BP",
        "location": "Grotta Paglicci, Apulia", "country": "Italy",
        "lat": 41.63, "lon": 15.53, "date_bce": -26750,
        "publication": "Posth et al. 2016; Fu et al. 2016",
        "mt": "U8c", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "U8c Italiasta ~27 000 BCE — U8-linjan laajuus Gravettilaisena aikana.",
        "source": "media4_S4b",
    },
    {
        "id": "ElMiron-manual", "group": "Spain_ElMiron_17000BP",
        "location": "El Miron Cave, Cantabria", "country": "Spain",
        "lat": 43.22, "lon": -3.57, "date_bce": -16770,
        "publication": "Fu et al. 2016",
        "mt": "U5b", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "U5b Franco-Kantabrian refugiosta ~17 000 BCE.",
        "source": "media4_S4b",
    },
    {
        "id": "Paglicci71-manual", "group": "Italy_Paglicci_17000BP",
        "location": "Grotta Paglicci, Apulia", "country": "Italy",
        "lat": 41.63, "lon": 15.53, "date_bce": -16635,
        "publication": "Posth et al. 2016",
        "mt": "U5b2b", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Vanhin U5b2b.",
        "source": "media4_S4b",
    },
    {
        "id": "HohleFels49-manual", "group": "Germany_HohleFels_14000BP",
        "location": "Hohle Fels, Swabian Alb", "country": "Germany",
        "lat": 48.37, "lon": 9.75, "date_bce": -13959,
        "publication": "Posth et al. 2016; Fu et al. 2016",
        "mt": "U8a", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Magdaleniaaninen U8a — U8-linja selvisi jääkauden maksimin yli.",
        "source": "media4_S4b",
    },
    {
        "id": "Oberkassel998-manual", "group": "Germany_Oberkassel_12000BP",
        "location": "Oberkassel, Düsseldorf", "country": "Germany",
        "lat": 51.22, "lon": 6.77, "date_bce": -12070,
        "publication": "Fu et al. 2013b",
        "mt": "U5b1", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "U5b1+16189+16192T! — lähisukulainen suomalaiselle U5b1b1-linjalle.",
        "source": "media4_S4b",
    },
    {
        "id": "Villabruna-manual", "group": "Italy_Villabruna_12000BP",
        "location": "Villabruna, Veneto", "country": "Italy",
        "lat": 46.02, "lon": 11.89, "date_bce": -12030,
        "publication": "Fu et al. 2016",
        "mt": "U5b2b", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Epigravettilainen U5b2b Pohjois-Italiasta.",
        "source": "media4_S4b",
    },
    {
        "id": "Bichon-manual", "group": "Switzerland_Bichon_11500BP",
        "location": "La Bichonne Cave, Jura", "country": "Switzerland",
        "lat": 47.10, "lon": 6.90, "date_bce": -11550,
        "publication": "Jones et al. 2015",
        "mt": "U5b1h", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Mesolittiinen WHG, U5b1 Alppien pohjoispuolelta.",
        "source": "media4_S4b",
    },
    {
        "id": "Motala309-manual", "group": "Sweden_Motala_7700BP",
        "location": "Kanaljorden, Motala", "country": "Sweden",
        "lat": 58.53, "lon": 15.03, "date_bce": -5715,
        "publication": "Mittnik et al. 2018",
        "mt": "U5a2d", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Skandinaavinen SHG. U5a2d yleinen Motalan kohteessa.",
        "source": "media4_S4b",
    },
    {
        "id": "Motala363-manual", "group": "Sweden_Motala_7700BP",
        "location": "Kanaljorden, Motala", "country": "Sweden",
        "lat": 58.53, "lon": 15.03, "date_bce": -5618,
        "publication": "Mittnik et al. 2018",
        "mt": "U5a1", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Toinen Motalan SHG — U5a1 Skandinaviassa ~5 600 BCE.",
        "source": "media4_S4b",
    },
    # -----------------------------------------------------------------------
    # Kilinc et al. 2023, Current Biology — Altai-Sayanin ja Kamchatkan
    # uudet genoomit. DOI: 10.1016/j.cub.2022.11.062
    # Julkaisu: "Middle Holocene Siberian genomes reveal highly connected
    #            gene pools throughout North Asia"
    #
    # Narratiivinen merkitys KSHM:lle:
    #   U2e1b (FRS001, Altai ~5 400 BCE) kuuluu samaan EHG-lähiklädiin kuin
    #   varhaisimmat itäiset metsästäjä-keräilijät — silta Läntisestä Siperiasta
    #   Euroopan U2e-linjoihin. ANE-komponentti (Ancient North Eurasian) on sama
    #   populaatiopohja jonka kautta myöhemmin R1a/R1b+N-Tat kantajat kulkivat
    #   Suomeen pronssikaudella.
    # -----------------------------------------------------------------------
    {
        "id": "FRS001-manual", "group": "Altai_7500BP",
        "location": "Frolovskiy, Altai-Sayan", "country": "Russia",
        "lat": 53.337, "lon": 83.93, "date_bce": -5434,
        "publication": "Kilinc et al. 2023. Curr. Biol. doi:10.1016/j.cub.2022.11.062",
        "mt": "U2e1b", "y": "CT", "y_isogg": None, "y_manual": None,
        "notes": (
            "Altai ~7 500 BP (5 478–5 390 cal BCE). Y-CT = basaalinen klade ennen Q/R-haarautumaa. "
            "U2e1b kuuluu EHG-sukuiseen U2e-linjaan — silta Länsi-Siperia↔Eurooppa. "
            "Ryhmä edustaa aiemmin tuntematonta ANE+Paleo-Siperialainen sekoitusta."
        ),
        "source": "Kilinc2023",
    },
    {
        "id": "FRS002-manual", "group": "Altai_7500BP",
        "location": "Frolovskiy, Altai-Sayan", "country": "Russia",
        "lat": 53.337, "lon": 83.93, "date_bce": -5434,
        "publication": "Kilinc et al. 2023. Curr. Biol. doi:10.1016/j.cub.2022.11.062",
        "mt": "C", "y": "Q1a1", "y_isogg": "Q1a1", "y_manual": None,
        "notes": (
            "Altai ~7 500 BP. Q1a1 Y-DNA — uralilaisten ja alkuperäisamerikkalaisten "
            "isälinja. Q1a1 dokumentoitu Altailla jo ~5 400 BCE. mtDNA C: tyypillinen "
            "Siperia/Itä-Aasia-haplotyyppi."
        ),
        "source": "Kilinc2023",
    },
    {
        "id": "NVR001-manual", "group": "Altai_6500BP",
        "location": "Novorybinskiy, Altai-Sayan", "country": "Russia",
        "lat": 53.371, "lon": 83.92, "date_bce": -4252,
        "publication": "Kilinc et al. 2023. Curr. Biol. doi:10.1016/j.cub.2022.11.062",
        "mt": "D4j", "y": "Q1a1", "y_isogg": "Q1a1", "y_manual": None,
        "notes": "Altai ~6 500 BP. Q1a1 jatkuu — sama Y-linja 1 000 vuotta myöhemmin. D4j mtDNA.",
        "source": "Kilinc2023",
    },
    {
        "id": "TZB001-manual", "group": "Altai_5500BP",
        "location": "Tzebotarevo, Altai-Sayan", "country": "Russia",
        "lat": 53.269, "lon": 83.811, "date_bce": -3423,
        "publication": "Kilinc et al. 2023. Curr. Biol. doi:10.1016/j.cub.2022.11.062",
        "mt": "C4+152", "y": "C2b1", "y_isogg": "C2b1", "y_manual": None,
        "notes": "Altai ~5 500 BP. C2b1 Y-DNA (Mongolia/Siperia). Altai-populaation siirtymä kohti ANA-komponentin laskua.",
        "source": "Kilinc2023",
    },
    {
        "id": "TZB002-manual", "group": "Altai_5500BP",
        "location": "Tzebotarevo, Altai-Sayan", "country": "Russia",
        "lat": 53.269, "lon": 83.811, "date_bce": -3895,
        "publication": "Kilinc et al. 2023. Curr. Biol. doi:10.1016/j.cub.2022.11.062",
        "mt": "R1b", "y": "C2b", "y_isogg": "C2b", "y_manual": None,
        "notes": "Altai ~5 500 BP. C2b Y + R1b mtDNA — epätavallinen yhdistelmä samasta kohteesta kuin TZB001.",
        "source": "Kilinc2023",
    },
    {
        "id": "NIZ001-manual", "group": "Nizhnetytkesken_6500BP",
        "location": "Nizhnetytkesken, Altai-Sayan", "country": "Russia",
        "lat": 51.1997, "lon": 86.0733, "date_bce": -4391,
        "publication": "Kilinc et al. 2023. Curr. Biol. doi:10.1016/j.cub.2022.11.062",
        "mt": "A", "y": "C2b1a1", "y_isogg": "C2b1a1", "y_manual": None,
        "notes": (
            "Altai-Sayan ~6 500 BP, Katun-joen laakso. C2b1a1 + mtDNA A — korkea ANA-komponentti, "
            "PCA-avaruudessa lähempänä Baikal EN-populaatiota kuin Altai_HG-ryhmää. "
            "Osoittaa Altai-alueen geneettisen monimuotoisuuden jo Holoseenikaudella."
        ),
        "source": "Kilinc2023",
    },
    {
        "id": "LetuchayaMysh-manual", "group": "LetuchayaMysh_7000BP",
        "location": "Letuchaya Mysh (Bat Cave), Primorsky Krai", "country": "Russia",
        "lat": 42.999, "lon": 133.095, "date_bce": -4832,
        "publication": "Kilinc et al. 2023. Curr. Biol. doi:10.1016/j.cub.2022.11.062",
        "mt": "D4b1a2a", "y": "C2b", "y_isogg": "C2b", "y_manual": None,
        "notes": (
            "Venäjän Kaukoidän rannikko ~7 000 BP (4 935–4 729 cal BCE). "
            "C2b + D4b1a2a — korkea ANA-komponentti, silta Amur-alueen populaatioihin. "
            "Maantieteellisesti äärimmäinen läntinen piste ANA-ankkurille."
        ),
        "source": "Kilinc2023",
    },
    {
        "id": "KMT001-manual", "group": "Kamchatka_400BP",
        "location": "Kamchatka Peninsula (Ust-Khayryuzovo area)", "country": "Russia",
        "lat": 55.461, "lon": 159.68, "date_bce": 304,
        "publication": "Kilinc et al. 2023. Curr. Biol. doi:10.1016/j.cub.2022.11.062",
        "mt": "G1b", "y": None, "y_isogg": None, "y_manual": None,
        "notes": "Kamchatka ~500 BP, naispuolinen. G1b mtDNA — Siperian alkuperäiskansojen haplotyyppi.",
        "source": "Kilinc2023",
    },
    {
        "id": "KMT002-manual", "group": "Kamchatka_400BP",
        "location": "Kamchatka Peninsula (Ust-Khayryuzovo area)", "country": "Russia",
        "lat": 55.461, "lon": 159.68, "date_bce": 372,
        "publication": "Kilinc et al. 2023. Curr. Biol. doi:10.1016/j.cub.2022.11.062",
        "mt": "G1b", "y": "Q1a1", "y_isogg": "Q1a1", "y_manual": None,
        "notes": (
            "Kamchatka ~500 BP. Q1a1 + G1b — samat haplogroups kuin Altai_7500BP/FRS002 "
            "~6 000 vuotta myöhemmin. Jatkuvuus Q1a1-linjassa läpi Pohjois-Aasian."
        ),
        "source": "Kilinc2023",
    },
    {
        "id": "KMT003-manual", "group": "Kamchatka_400BP",
        "location": "Kamchatka Peninsula (Ust-Khayryuzovo area)", "country": "Russia",
        "lat": 55.461, "lon": 159.68, "date_bce": 832,
        "publication": "Kilinc et al. 2023. Curr. Biol. doi:10.1016/j.cub.2022.11.062",
        "mt": "G1b", "y": "Q1a1", "y_isogg": "Q1a1", "y_manual": None,
        "notes": "Kamchatka ~1 100 BP. Q1a1 + G1b — kolmas Q1a1-näyte Kamchatkalta.",
        "source": "Kilinc2023",
    },
]


# ---------------------------------------------------------------------------
# Sarakekartta — havaitaan kerran tiedostoa avattaessa
# ---------------------------------------------------------------------------

class _ColMap:
    __slots__ = (
        "id", "group", "loc", "country", "lat", "lon",
        "pub", "date", "mt", "y_term", "y_isogg", "y_manual", "version",
    )

    def __init__(self, fieldnames: List[str]):
        def fc(cands): return _find_col(fieldnames, cands)
        self.id       = fc(_ID_COLS)
        self.group    = fc(_GRP_COLS)
        self.loc      = fc(_LOC_COLS)
        self.country  = fc(_CTR_COLS)
        self.lat      = fc(_LAT_COLS)
        self.lon      = fc(_LON_COLS)
        self.pub      = fc(_PUB_COLS)
        self.date     = fc(_DATE_COLS)
        self.mt       = fc(_MT_COLS)
        self.y_term   = fc(_Y_TERM_COLS)
        self.y_isogg  = fc(_Y_ISOGG_COLS)
        self.y_manual = fc(_Y_MANUAL_COLS)
        self.version  = "v62" if (self.y_term and "Lazaridis" in (self.y_term or "")) else "v54"

    def g(self, row: Dict, attr: str) -> str:
        col = getattr(self, attr, None)
        return row.get(col, "").strip() if col else ""


# ---------------------------------------------------------------------------
# Arvot joita ei pidetä oikeina haploryhmänä
# ---------------------------------------------------------------------------

def _clean(v: str) -> Optional[str]:
    """Palauttaa None jos arvo ei ole käyttökelpoinen haploryhmä."""
    if not v:
        return None
    s = v.strip()
    if not s:
        return None
    sl = s.lower()
    # Kaikki tyhjää/puuttuvaa tarkoittavat arvot
    if sl in ("..", "na", "n/a", "no", "not published in paper", "neanderthal"):
        return None
    if sl.startswith("n/a"):          # "n/a (female)", "n/a (<2x)", jne.
        return None
    if sl.startswith("neanderthal"):
        return None
    # v54.1-spesifiset roskat
    if sl in ("na", "not published", ""):
        return None
    return s


def _bp_to_bce(bp: str) -> Optional[int]:
    try:
        return round(1950 - float(bp))
    except (ValueError, TypeError):
        return None


# ---------------------------------------------------------------------------
# Parseri
# ---------------------------------------------------------------------------

def _parse_row(row: Dict, cm: _ColMap) -> Optional[Dict]:
    mt       = _clean(cm.g(row, "mt"))
    y_term   = _clean(cm.g(row, "y_term"))
    y_isogg  = _clean(cm.g(row, "y_isogg"))
    y_manual = _clean(cm.g(row, "y_manual"))

    # v54.1: terminaali usein tyhjä, ISOGG:ssä arvo → käytä ISOGG y_best:nä
    # v62:  terminaali (esim. "N-L550") > manuaalinen override > ISOGG
    y_best = y_manual or y_term or y_isogg

    if mt is None and y_best is None and y_isogg is None:
        return None

    try:
        lat = float(cm.g(row, "lat"))
        lon = float(cm.g(row, "lon"))
    except (ValueError, TypeError):
        lat, lon = None, None

    return {
        "id":          cm.g(row, "id"),
        "group":       cm.g(row, "group"),
        "location":    cm.g(row, "loc"),
        "country":     cm.g(row, "country"),
        "lat":         lat,
        "lon":         lon,
        "date_bce":    _bp_to_bce(cm.g(row, "date")),
        "publication": cm.g(row, "pub"),
        "mt":          mt,
        "y":           y_best,
        "y_isogg":     y_isogg,
        "y_manual":    y_manual,
        "source":      cm.version,
    }


def _y_index_keys(y_term: Optional[str], y_isogg: Optional[str], y_manual: Optional[str] = None) -> List[str]:
    """
    Tuottaa Y-DNA-avaimet indeksointia varten.
    Indeksoidaan SEKÄ terminaali (N-L550) ETTÄ ISOGG (N1a1a1a1a1a1a)
    jotta molemmat hakutavat toimivat.
    """
    keys = []
    for v in (y_manual, y_term, y_isogg):
        if v:
            clean = v.rstrip("~").strip()
            if clean and clean not in keys:
                keys.append(clean)
    return keys


# ---------------------------------------------------------------------------
# Singleton-indeksi
# ---------------------------------------------------------------------------

class _AADRIndex:
    def __init__(self):
        self._by_mt:  Dict[str, List[Dict]] = defaultdict(list)
        self._by_y:   Dict[str, List[Dict]] = defaultdict(list)
        self._loaded  = False
        self._path:   Optional[str] = None
        self._version = "unknown"

    def _load(self, anno_path: str) -> None:
        if self._loaded and self._path == anno_path:
            return

        logger.info(f"Ladataan AADR: {anno_path}")
        by_mt: Dict[str, List] = defaultdict(list)
        by_y:  Dict[str, List] = defaultdict(list)

        try:
            with open(anno_path, encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter="\t")
                cm = _ColMap(list(reader.fieldnames or []))
                self._version = cm.version
                logger.info(f"  Versio: {cm.version} | Y-terminaali: {(cm.y_term or '')[:60]}")

                for row in reader:
                    s = _parse_row(row, cm)
                    if s is None:
                        continue
                    if s["mt"]:
                        by_mt[s["mt"]].append(s)
                    for key in _y_index_keys(s.get("y"), s.get("y_isogg"), s.get("y_manual")):
                        by_y[key].append(s)

        except FileNotFoundError:
            logger.warning(f"Tiedostoa ei löydy: {anno_path}")

        # Manuaaliset lisäykset
        for s in MANUAL_ADDITIONS:
            if s.get("mt"):
                by_mt[s["mt"]].append(s)
            for key in _y_index_keys(s.get("y"), s.get("y_isogg"), s.get("y_manual")):
                by_y[key].append(s)

        self._by_mt  = by_mt
        self._by_y   = by_y
        self._loaded = True
        self._path   = anno_path

        n_mt = sum(len(v) for v in by_mt.values())
        n_y  = sum(len(v) for v in by_y.values())
        logger.info(f"Ladattu: {n_mt} mtDNA-merkintää, {n_y} Y-DNA-merkintää")

    def get_mt(self, p: str) -> Dict[str, List[Dict]]:
        self._load(p); return self._by_mt

    def get_y(self, p: str) -> Dict[str, List[Dict]]:
        self._load(p); return self._by_y

    @property
    def version(self) -> str:
        return self._version


_INDEX = _AADRIndex()


# ---------------------------------------------------------------------------
# N-Tat nimikaos — alias-taulukko
# ---------------------------------------------------------------------------

_N_TAT_ALIASES: Dict[str, str] = {
    # SNP-pohjaiset
    "N-M46": "N-M46",   "N-TAT": "N-M46",   "N-TAT": "N-M46",
    "N-P105": "N-M46",  "N-M178": "N-M46",
    # Vanhat ISOGG-nimet
    "N3": "N-M46",      "N1C": "N-M46",     "N1C1": "N-M46",
    # Eurooppalaiset SNP-nimet
    "N-L1026": "N-L1026",
    "N-VL29":  "N-L1026",
    "N-L550":  "N-L550",
    "N-Z1936": "N-Z1936",
    "N-Z1925": "N-Z1936",
    # Eupedian vanhat ISOGG-nimet
    "N1C1A1A1A1": "N-L550",
    "N1C1A1A1A2": "N-Z1936",
    "N1C1A1A": "N-L1026",
}


def _resolve(hg: str, lineage: str) -> str:
    if lineage == "y":
        return _N_TAT_ALIASES.get(hg.upper().strip(), hg)
    return hg


# ---------------------------------------------------------------------------
# Hakuapurit
# ---------------------------------------------------------------------------

def _prefix_lookup(index: Dict[str, List[Dict]], hg: str) -> List[Dict]:
    """Täsmällinen + pisin etuliiteosuma."""
    hg_u = hg.upper().rstrip("~")
    # Täsmällinen
    for key, samps in index.items():
        if key.upper().rstrip("~") == hg_u:
            return samps
    # Pisin etuliite
    best, best_len = None, 0
    for key in index:
        k = key.upper().rstrip("~")
        if hg_u.startswith(k) and len(k) > best_len and len(k) >= 2:
            best, best_len = key, len(k)
    return index[best] if best else []


def _all_prefix_matches(index: Dict[str, List[Dict]], hg: str) -> List[Dict]:
    """Kaikki näytteet koko kladipuulle."""
    hg_u = hg.upper().rstrip("~")
    seen: set = set()
    out = []
    for key, samps in index.items():
        if key.upper().rstrip("~").startswith(hg_u):
            for s in samps:
                if s["id"] not in seen:
                    out.append(s)
                    seen.add(s["id"])
    return out


def _dedup(samples: List[Dict]) -> List[Dict]:
    seen: set = set()
    out = []
    for s in samples:
        if s["id"] not in seen:
            out.append(s)
            seen.add(s["id"])
    return out


def _chrono(samples: List[Dict]) -> List[Dict]:
    dated   = sorted([s for s in samples if s.get("date_bce") is not None],
                     key=lambda x: x["date_bce"])
    undated = [s for s in samples if s.get("date_bce") is None]
    return dated + undated


def _no_modern(samples: List[Dict]) -> List[Dict]:
    """Suodata pois modernit referenssinäytteet (.DG päätteellä ja BP≈0)."""
    return [
        s for s in samples
        if not (
            s.get("date_bce") is not None
            and s["date_bce"] >= -10
            and s.get("group", "").endswith(".DG")
        )
    ]


# ---------------------------------------------------------------------------
# Julkinen API
# ---------------------------------------------------------------------------

def get_nearest_samples(
    haplogroup: str,
    n: int = 10,
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
    require_coordinates: bool = False,
    exclude_modern: bool = True,
) -> List[Dict]:
    """
    Palauttaa n lähintä aDNA-näytettä haploryhmälle (vanhin ensin).

    Args:
        haplogroup:         Haploryhmä (esim. "U5b1", "N-L550", "N1a1a1a1a1")
        n:                  Maksimimäärä
        lineage:            "mt" tai "y"
        anno_path:          .anno-tiedoston polku
        require_coordinates Vain koordinaateilla varustetut näytteet
        exclude_modern:     Jätä pois .DG-päätteiset modernit referenssinäytteet
    """
    hg    = _resolve(haplogroup, lineage)
    index = _INDEX.get_mt(anno_path) if lineage == "mt" else _INDEX.get_y(anno_path)
    samps = _dedup(_prefix_lookup(index, hg))

    if require_coordinates:
        samps = [s for s in samps if s.get("lat") is not None]
    if exclude_modern:
        samps = _no_modern(samps)

    return _chrono(samps)[:n]


def get_oldest_sample(
    haplogroup: str,
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
) -> Optional[Dict]:
    """Vanhin tunnettu näyte kladille."""
    s = get_nearest_samples(haplogroup, n=1, lineage=lineage, anno_path=anno_path)
    return s[0] if s else None


def get_samples_by_region(
    haplogroup: str,
    country: str,
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
    n: int = 50,
) -> List[Dict]:
    """Suodattaa näytteet maan perusteella."""
    hg    = _resolve(haplogroup, lineage)
    index = _INDEX.get_mt(anno_path) if lineage == "mt" else _INDEX.get_y(anno_path)
    samps = _dedup(_prefix_lookup(index, hg))
    samps = [s for s in samps if country.lower() in s.get("country", "").lower()]
    return _chrono(samps)[:n]


def get_clade_tree_samples(
    haplogroup_prefix: str,
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
    max_total: int = 50,
    exclude_modern: bool = True,
) -> List[Dict]:
    """Kaikki näytteet koko kladipuulle (esim. kaikki U5*)."""
    hg    = _resolve(haplogroup_prefix, lineage)
    index = _INDEX.get_mt(anno_path) if lineage == "mt" else _INDEX.get_y(anno_path)
    samps = _dedup(_all_prefix_matches(index, hg))
    if exclude_modern:
        samps = _no_modern(samps)
    return _chrono(samps)[:max_total]


def get_sample_count(
    haplogroup: str,
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
) -> int:
    """Näytemäärä haploryhmälle."""
    hg    = _resolve(haplogroup, lineage)
    index = _INDEX.get_mt(anno_path) if lineage == "mt" else _INDEX.get_y(anno_path)
    return len(_dedup(_prefix_lookup(index, hg)))


def list_available_clades(
    lineage: str = "mt",
    anno_path: str = DEFAULT_ANNO_PATH,
    min_count: int = 1,
) -> List[Tuple[str, int]]:
    """Kaikki indeksoidut kladit näytemäärän mukaan."""
    index = _INDEX.get_mt(anno_path) if lineage == "mt" else _INDEX.get_y(anno_path)
    return sorted(
        [(k, len(v)) for k, v in index.items() if len(v) >= min_count],
        key=lambda x: -x[1],
    )


def get_aadr_version(anno_path: str = DEFAULT_ANNO_PATH) -> str:
    """Palauttaa havaitun AADR-version ('v62' tai 'v54')."""
    _INDEX._load(anno_path)
    return _INDEX.version


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    hg   = sys.argv[1] if len(sys.argv) > 1 else "U5b1"
    lin  = sys.argv[2] if len(sys.argv) > 2 else "mt"
    path = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_ANNO_PATH

    print(f"\n=== AADR-haku: {hg} ({lin}) ===")
    print(f"Versio: {get_aadr_version(path)}")
    print(f"Näytteitä: {get_sample_count(hg, lin, path)}\n")

    for s in get_nearest_samples(hg, n=10, lineage=lin, anno_path=path):
        bce = s["date_bce"]
        era = f"{-bce} BCE" if bce < 0 else f"{bce} CE"
        print(f"  [{era:>10}] {s['id']:25} {s['location']}, {s['country']}")
        if lin == "mt":
            print(f"             mt:{s['mt']}  pub:{s['publication'][:55]}")
        else:
            print(f"             Y:{s['y']} / ISOGG:{s.get('y_isogg','')}  pub:{s['publication'][:55]}")
        print()
