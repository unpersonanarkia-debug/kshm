"""
ancient_samples_db.py — Kureertu muinaisnäytetietokanta

Jokainen näyte vastaa yhtä episodiosiota KSHM-narratiivissa:
    🜂 OSA X — [era_label]
    # [location]
    [context-narratiivi] + [references]

Rakenne per näyte:
    {
        "id":          str,   # näyte-ID (esim. "PN05", "PCA0099")
        "location":    str,   # arkeologinen kohde
        "date":        str,   # "3941–3661 BCE" tai "-26500" tai "400 CE"
        "culture":     str,   # kulttuurinimi
        "era_label":   str,   # osion yläotsikko (osan nimi)
        "context":     str,   # narratiivinen kuvaus (fi — i18n tulossa)
        "references":  List[str],  # akateemiset lähteet
        "coordinates": Optional[Tuple[float, float]],  # (lat, lon) kartalle
        "image":       Optional[str],  # kuvan polku tai URL
        "lineage_fit": str,   # "mtDNA" | "Y-DNA" | "both"
    }

HAPLOGROUP_SAMPLES[haplogroup_prefix] = List[sample_dict]

Haploryhmäavain on lyhyin yksilöivä etuliite:
    "H1"       kattaa H1a, H1b, H1-T16189C jne.
    "H1-T16189C" ohittaa H1-oletuksen (tarkempi avain voittaa)
    "R1b"      kattaa R1b-M269, R1b-L21 jne.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Tyyppimääritelmät
# ---------------------------------------------------------------------------

AncientSample = Dict  # ks. docstring


# ---------------------------------------------------------------------------
# Päärekisteri
# ---------------------------------------------------------------------------

HAPLOGROUP_SAMPLES: Dict[str, List[AncientSample]] = {}


# ---------------------------------------------------------------------------
# H1 / H1-T16189C  — KSHM case-01 pohja
# Lähde: kshm.fi/case-h1-t16189c-01.html + vertaisarvioidut julkaisut
# ---------------------------------------------------------------------------

HAPLOGROUP_SAMPLES["H1-T16189C"] = [

    {
        "id":        "REFUGIO-H1",
        "location":  "Franco-Cantabrian refugio",
        "date":      "26500–19000 BCE",
        "culture":   "Upper Palaeolithic / Magdalenian",
        "era_label": "Jääkauden selviytyjät",
        "lineage_fit": "mtDNA",
        "coordinates": (43.3, -1.8),   # Kantabrian vuoret / Pyreneiden länsipää
        "image":     "images/altamira-bison.jpg",
        "context": (
            "Noin 26 500–19 000 vuotta sitten jäätikkö oli niellyt Skandinavian ja "
            "Keski-Euroopan. H1-äitilinjan varhaiset kantajat selvisivät jääkauden "
            "ankarimmista vuosituhansista Franco-Cantabrian refugiossa — Iberian "
            "niemimaan luoteisosassa ja Lounais-Ranskassa. He elivät liikkeessä: "
            "seurasivat riistaa, kalastivat jokia ja maalasivat seinille eläimiä "
            "Altamiran ja Lascaux'n luolissa. Kaksi sisarlinjaa erosi noin 10 000 "
            "vuotta sitten: pohjoinen sisar seurasi riistaa kohti Keski-Eurooppaa, "
            "eteläinen sisar jäi Maghrebiin. Pohjoisen sisaren jälkeläiset ovat "
            "H1-T16189C-linjan kantajat."
        ),
        "references": [
            "Achilli et al. 2004. Am. J. Hum. Genet. 75:910–918",
            "Pereira et al. 2005. J. Hum. Genet. 50:451–459",
            "Fregel et al. 2018. PNAS 115:6774–6779",
            "Torroni et al. 1998. Am. J. Hum. Genet. 62:1137–1152",
        ],
    },

    {
        "id":        "ANATOLIA-EEF",
        "location":  "Anatolian Neolithic — Çatalhöyük / Barcın Höyük",
        "date":      "8800–6500 BCE",
        "culture":   "Pre-Pottery Neolithic B (PPNB) / Early European Farmers (EEF)",
        "era_label": "Suuri vaellus — Anatolian neoliitti",
        "lineage_fit": "mtDNA",
        "coordinates": (37.7, 32.8),   # Çatalhöyük, Konya, Turkki
        "image":     "images/anatolia-neolithic.jpg",
        "context": (
            "Noin 8 800–7 000 eaa. Pre-Pottery Neolithic B -aika mullisti ihmiskunnan. "
            "Çatalhöyükissä 8 000 ihmistä asui tiheässä savikylässä, hautasivat "
            "vainajansa lattian alle ja kasvattivat einkorn-vehnää. Barcın "
            "Höyükissä 200 pyöreää taloa vierekkäin. Tänä aikana mitokondrio-DNA:ssa "
            "tapahtui T16189C-pistemutaatio position 16189:ssä — pieni muutos, "
            "joka tuli kantaa tuhansien vuosien ajan. Neoliittinen laajeneminen "
            "kuljetti tämän linjan kolmea reittiä länteen: Balkanin kautta "
            "Keski-Eurooppaan (LBK-kulttuuri), Välimerta pitkin Sardiniaan ja "
            "Iberiaan, sekä lopulta Atlantin fasadin kautta Irlantiin."
        ),
        "references": [
            "Kilinc et al. 2016. Curr. Biol. 26:2659–2666",
            "Mathieson et al. 2015. Nature 522:197–202",
            "Allentoft et al. 2015. Nature 522:167–172",
            "Baird et al. 2012. Anatolian Neolithic",
        ],
    },

    {
        "id":        "PN05",
        "location":  "Poulnabrone dolmen, County Clare, Ireland",
        "date":      "3941–3661 BCE",
        "culture":   "Neolithic Megalithic / Western European Farmers",
        "era_label": "Suuri vaellus — Megaliittinen Irlanti",
        "lineage_fit": "mtDNA",
        "coordinates": (53.046, -9.134),  # Poulnabrone, Burren
        "image":     "images/poulnabrone-dolmen.jpg",
        "context": (
            "Poulnabronen dolmen Burrenin karulla tasangolla on kolme metriä korkea "
            "porttirakennelma — 50 tonnia kiveä, jotka on pysynyt paikallaan lähes "
            "6 000 vuotta. Akseli on linjattu talvipäivänseisauksen suuntaan. "
            "Kammioon on haudattu 33 ihmistä rituaalisesti, luut järjestelty "
            "uudelleen sukupolvien aikana. Näyte PN05 — nainen, ajoitettu "
            "3941–3661 eaa. — kantaa täsmälleen H1-T16189C!-merkkiä. "
            "Ei kultaa, ei aseita; vain kiillotettu tuffikivikirves, piikiviä, "
            "luuriipuksia ja kvartsikiteitä. Muistaminen oli jatkuva teko."
        ),
        "references": [
            "Cassidy et al. 2016. PNAS 113:368–373",
            "McLaughlin et al. 2016. J. Archaeol. Sci.",
            "Schulting & Fibiger 2012. Skeletal Trauma in European Prehistory",
        ],
    },

    {
        "id":        "PCA0099",
        "location":  "Masłomęcz, eastern Poland — Wielbark culture cemetery",
        "date":      "200–375 CE",
        "culture":   "Wielbark / Gothic migration phase",
        "era_label": "Vaelluksen aika — Goottien liike",
        "lineage_fit": "mtDNA",
        "coordinates": (50.75, 23.45),   # Masłomęcz, Hrubieszów, Puola
        "image":     "images/maslomecz-wielbark-2.jpg",
        "context": (
            "Noin 1 750 vuotta sitten Rooman valtakunta natisi saumoistaan. "
            "Masłomęczin Wielbark-kulttuurin hautakenttä sisältää yli 200 hautaa "
            "— aseettomuus on systemaattista, kulttuurinen valinta. Kivirenkaat "
            "puhuvat samaa muistamisen geometriaa kuin Atlantin megaliitit. "
            "Hauta 99, näyte PCA0099: nainen, kantaa H1-T16189C!-merkkiä. "
            "Hän eli rajojen maailmassa — heimot vaihtoivat paikkoja, identiteetti "
            "oli liike. Vanhat jumalat kulkivat mukana uusille asuinsijoille."
        ),
        "references": [
            "Schroeder et al. 2018. PNAS 115:8005–8010",
            "Kokowski 2013. Wielbark Culture in eastern Poland",
            "Heather 1998. The Goths. Blackwell",
        ],
    },

    {
        "id":        "KOPPARSVIK-F",
        "location":  "Kopparsvik, Gotland, Sweden — Viking Age cemetery",
        "date":      "750–1050 CE",
        "culture":   "Viking Age / Gotlandic maritime culture",
        "era_label": "Meren solmukohta — Gotlanti",
        "lineage_fit": "mtDNA",
        "coordinates": (57.63, 18.29),   # Kopparsvik, Visby, Gotlanti
        "image":     "images/gotland-kopparsvik.jpg",
        "context": (
            "Itämeren sydämessä Gotlanti oli viikinkiajan kaupan solmukohta — hopea "
            "virtasi Bagdadista, tarinat Volgalta, ihmiset kaikkialta. "
            "Kopparsvikin hautausmaalla yli 500 hautaa, joissa näkyy kansainvälinen "
            "verkosto: pronssikoruja, dirhemejä, miekkoja. Yksi naishaudoista "
            "paljastaa H1-T16189C!-linjan. Tuo ketju ei katkennut Atlantilla eikä "
            "goottien vaelluksessa — se jatkui täälläkin, hopean ja purjeiden "
            "maailmassa, ja jatkuu edelleen."
        ),
        "references": [
            "Price et al. 2019. Nature 574:356–361",
            "Hedenstierna-Jonson et al. 2017. Am. J. Phys. Anthropol.",
            "Gustin 2004. Zwischen Vielfalt und Standardisierung. Gotland",
        ],
    },
]


# ---------------------------------------------------------------------------
# H1  — yleinen H1 (kaikki alahaarat ilman tarkempaa T16189C-merkkiä)
# ---------------------------------------------------------------------------

HAPLOGROUP_SAMPLES["H1"] = [

    {
        "id":        "OLALDE-H1-IB",
        "location":  "Chalcolithic Iberia — El Portalón, Spain",
        "date":      "3500–2500 BCE",
        "culture":   "Iberian Chalcolithic / Bell Beaker precursor",
        "era_label": "Kuparikausi — Iberia",
        "lineage_fit": "mtDNA",
        "coordinates": (42.36, -3.52),
        "context": (
            "Iberian niemimaan kuparikauden hautauksissa H1 on yksi yleisimmistä "
            "naisten mitokondriohaploryhmistä. El Portalónin luolahaudoissa "
            "nauriinhautauksissa H1-linjat jatkavat neoliittista EEF-väestöä, "
            "johon sekoittuu vähitellen aroelementin (Yamnaya) vaikutusta."
        ),
        "references": [
            "Olalde et al. 2015. PNAS 112:13757–13762",
            "Günther et al. 2015. PNAS 112:11917–11922",
        ],
    },

    {
        "id":        "HAAK-H1-LBK",
        "location":  "Linearbandkeramik sites, Central Europe",
        "date":      "5500–4900 BCE",
        "culture":   "Linear Pottery Culture (LBK) / Early European Farmers",
        "era_label": "Varhainen maanviljely — Keski-Eurooppa",
        "lineage_fit": "mtDNA",
        "coordinates": (50.0, 10.0),
        "context": (
            "LBK-kulttuuri (5 500–4 900 eaa.) oli neoliittisen laajenemisen "
            "etujoukkoa Keski-Euroopassa. Haak et al. 2015 osoittaa, että "
            "H1 oli vahvasti edustettu varhaisten eurooppalaisten maanviljelijöiden "
            "joukossa — nämä ovat Anatoliasta saapuneen väestön suorat jälkeläiset, "
            "jotka syrjäyttivät suurelta osin mesoliittiset metsästäjä-keräilijät."
        ),
        "references": [
            "Haak et al. 2015. Nature 522:207–211",
            "Mathieson et al. 2015. Nature 522:197–202",
        ],
    },
]


# ---------------------------------------------------------------------------
# R1b — yleisin Länsi-Euroopan Y-DNA-haploryhmä
# ---------------------------------------------------------------------------

HAPLOGROUP_SAMPLES["R1b"] = [

    {
        "id":        "YAMNAYA-R1b",
        "location":  "Pontic-Caspian Steppe — Yamnaya burials",
        "date":      "3300–2600 BCE",
        "culture":   "Yamnaya / Proto-Indo-European",
        "era_label": "Aroheimojen aikakausi — Pontinen aro",
        "lineage_fit": "Y-DNA",
        "coordinates": (48.0, 40.0),
        "context": (
            "Yamnaya-kulttuuri (3 300–2 600 eaa.) oli kuparikauden aroheimojen "
            "ekspansiivinen yhteisö Pontis-Kaspian arolla. Miehet haudattiin "
            "kurgaaneihin — maanpäällisiin hautakumpuihin — koristeinaan "
            "pronssiesineet, vaunujen rattaat ja kadomalla. R1b-M269 on "
            "Yamnaya-miesten dominoiva Y-haploryhmä. Noin 3 000 eaa. tämä "
            "väestö vaelsi länteen ja kuljetti mukanaan protoindoeurooppalaisen "
            "kielen protoformin, josta kehittyivät myöhemmin kelttiläiset, "
            "germaaniset ja romaaniset kielet."
        ),
        "references": [
            "Haak et al. 2015. Nature 522:207–211",
            "Mathieson et al. 2015. Nature 522:197–202",
            "Allentoft et al. 2015. Nature 522:167–172",
        ],
    },

    {
        "id":        "BELL-BEAKER-R1b",
        "location":  "Bell Beaker sites, Western Europe",
        "date":      "2750–2000 BCE",
        "culture":   "Bell Beaker / Corded Ware derived",
        "era_label": "Kellomaljat — Länsi-Eurooppa",
        "lineage_fit": "Y-DNA",
        "coordinates": (48.5, 2.5),
        "context": (
            "Bell Beaker -kulttuuri levisi 2 750–2 000 eaa. koko Länsi-Eurooppaan "
            "Iberiasta Brittein saarille ja Keski-Eurooppaan. Olalde et al. 2018 "
            "osoitti, että Brittein saarilla Bell Beaker korvasi geneettisesti "
            "lähes kokonaan aiemman megalittiväestön alle 500 vuodessa. "
            "R1b-M269 on Bell Beaker -miesten ylivoimainen Y-haploryhmä — "
            "nykyinen R1b-taajuus Irlannissa (>80%) ja Walesissa on suoraa "
            "perua tästä massiivisesta väestönvaihdosta."
        ),
        "references": [
            "Olalde et al. 2018. Nature 555:190–196",
            "Haak et al. 2015. Nature 522:207–211",
        ],
    },

    {
        "id":        "HALLSTATT-R1b",
        "location":  "Hallstatt salt mines, Austria",
        "date":      "800–450 BCE",
        "culture":   "Hallstatt / Early Iron Age Celts",
        "era_label": "Rautakauden kelttilaiset — Hallstatt",
        "lineage_fit": "Y-DNA",
        "coordinates": (47.56, 13.65),
        "context": (
            "Hallstattin suolakaivos Itävallassa on yksi Euroopan parhaiten "
            "säilyneistä rautakauden kohteista — orgaaninen materiaali on "
            "säilynyt vuosituhansien ajan suolassa. Kaivoksessa löydettyjen "
            "miesten DNA:ssa R1b on dominoiva. Hallstattin kulttuuri on "
            "varhaisimman dokumentoidun kelttiläisen väestön ydin; sen jälkeläiset "
            "levisivät La Tène -kulttuurin myötä Galliaan, Iberiaan, "
            "Brittein saarille ja Anatoliaan."
        ),
        "references": [
            "Kocher et al. 2021. Nature Ecology & Evolution",
            "Martiniano et al. 2017. eLife",
        ],
    },
]


# ---------------------------------------------------------------------------
# I1  — Skandinaavinen Y-DNA
# ---------------------------------------------------------------------------

HAPLOGROUP_SAMPLES["I1"] = [

    {
        "id":        "SKOGLUND-I1-SCAN",
        "location":  "Neolithic Scandinavia — Pitted Ware culture",
        "date":      "3200–2300 BCE",
        "culture":   "Pitted Ware / Scandinavian Hunter-Gatherers (SHG)",
        "era_label": "Skandinaavinen mesoliitti — metsästäjä-keräilijät",
        "lineage_fit": "Y-DNA",
        "coordinates": (57.5, 12.0),
        "context": (
            "Skandinavian mesoliittiset metsästäjä-keräilijät (SHG) olivat "
            "I-haploryhmän varhaisia kantajia. Pitted Ware -kulttuuri (3 200–2 300 "
            "eaa.) oli heidän myöhäinen edustajansa — he asuivat rannikolla, "
            "metsästivät hylkeitä ja kalastivat, ja vastustivat neoliittisen "
            "maanviljelyn leviämistä. I1 eriytyi myöhemmin skandinaaviseen "
            "haaraan, joka saavutti huippunsa viikinkiajalla ja levisi "
            "normannien mukana Brittein saarille, Normandiaan ja Sisiliaan."
        ),
        "references": [
            "Skoglund et al. 2014. Science 344:747–750",
            "Haak et al. 2015. Nature 522:207–211",
        ],
    },

    {
        "id":        "VIKING-I1-NORWAY",
        "location":  "Viking Age Norway — Oseberg ship burial",
        "date":      "800–1100 CE",
        "culture":   "Viking Age / Norse",
        "era_label": "Viikinkiaika — Norja",
        "lineage_fit": "Y-DNA",
        "coordinates": (59.38, 10.47),
        "context": (
            "Viikinkiajan Norjassa I1 on dominoiva miesten Y-haploryhmä. "
            "Osebergin laivahautaus (834 jaa.) on yksi hienoimmista löydöistä: "
            "kahden naisen hauta täynnä käsitöitä, tekstiilejä ja eläimiä — "
            "mutta miesten Y-DNA:sta I1 kertoo elossa olevien miesten linjasta. "
            "Viikinit levisivät I1:n kanssa Islantiin (874), Normanniaan (911), "
            "Sisiliaan (1072) ja Kyjeviin (860), kantaen mukanaan tätä "
            "arktisen metsästäjä-keräilijän muinaisen linjan."
        ),
        "references": [
            "Price et al. 2019. Nature 574:356–361",
            "Margaryan et al. 2020. Nature 585:390–396",
        ],
    },
]


# ---------------------------------------------------------------------------
# J2  — Lähi-idän / Välimeren Y-DNA
# ---------------------------------------------------------------------------

HAPLOGROUP_SAMPLES["J2"] = [

    {
        "id":        "PPNB-J2-LEVANT",
        "location":  "Pre-Pottery Neolithic B — Levant / Ain Ghazal",
        "date":      "8500–6000 BCE",
        "culture":   "PPNB / Early Levantine Farmers",
        "era_label": "Levanttilainen neoliitti — varhaiset viljelijät",
        "lineage_fit": "Y-DNA",
        "coordinates": (32.0, 36.0),
        "context": (
            "J2 on yksi Lähi-idän neoliittisen vallankumouksen keskeisistä "
            "Y-haploryhmistä. Ain Ghazalin kylässä (nykyinen Jordania) "
            "8 500–6 000 eaa. ihmiset rakensivat maailman ensimmäisiä suuria "
            "kyliä, hallitsivat eläinten domestikaation ja kehittivät "
            "saviastianvalmistuksen. J2 levisi neoliittisten viljelijöiden "
            "mukana Anatoliaan, Kreikkaan ja koko Välimeren piiriin — "
            "ja on tänään erityisen yleinen Sardiniassa, Etelä-Italiassa "
            "ja Kreikassa."
        ),
        "references": [
            "Lazaridis et al. 2016. Nature 536:419–424",
            "Mathieson et al. 2015. Nature 522:197–202",
        ],
    },
]


# ---------------------------------------------------------------------------
# N1c / N1a2  — Suomen / Baltian / Siperian Y-DNA
# ---------------------------------------------------------------------------

HAPLOGROUP_SAMPLES["N1"] = [

    {
        "id":        "ANCIENT-N1-SIBERIA",
        "location":  "Siberian Bronze Age — Andronovo complex",
        "date":      "2100–900 BCE",
        "culture":   "Andronovo / West Siberian forest-steppe",
        "era_label": "Siperian pronssikausi",
        "lineage_fit": "Y-DNA",
        "coordinates": (55.0, 73.0),
        "context": (
            "N1-haploryhmä on jäänne muinaisesta pohjoiseuraasialaisesta "
            "metsästäjä-keräilijäväestöstä. Andronovo-kompleksin itäisimmissä "
            "osissa N1 on edustettuna — nämä ovat esi-isä-populaatioita, "
            "joista uraalilaista kieltä puhuvat kansat (suomalaiset, estonialaiset, "
            "unkarilaiset) ovat polveutuneet. N1c leviää Siperiasta "
            "Fennoskandiaan pronssikaudella ja varhaisella rautakaudella, "
            "jättäen vahvan jäljen erityisesti Suomen, Viron ja Latvian "
            "miespuoliseen väestöön."
        ),
        "references": [
            "Mathieson et al. 2015. Nature 522:197–202",
            "Tambets et al. 2018. Curr. Biol. 28:2277–2283",
        ],
    },
]


# ---------------------------------------------------------------------------
# U5  — Euroopan mesoliittiset metsästäjä-keräilijät (mtDNA)
# ---------------------------------------------------------------------------

HAPLOGROUP_SAMPLES["U5"] = [

    {
        "id":        "LOSCHBOUR-U5",
        "location":  "Loschbour, Luxembourg",
        "date":      "8000–7000 BCE",
        "culture":   "Mesolithic Western Hunter-Gatherer (WHG)",
        "era_label": "Euroopan metsästäjä-keräilijät",
        "lineage_fit": "mtDNA",
        "coordinates": (49.78, 6.12),
        "context": (
            "Loschbour-mies (8 000–7 000 eaa.) on yksi parhaiten sekvensoiduista "
            "eurooppalaisista mesoliittisista ihmisistä. Hänen äitilinjansa U5 "
            "on vanhin tunnistettu eurooppalainen mtDNA-linja — se saapui "
            "Eurooppaan ensimmäisten Homo sapiens -aaltojen mukana yli 40 000 "
            "vuotta sitten. U5 oli Euroopan metsästäjä-keräilijöiden dominoiva "
            "linja ennen neoliittisten maanviljelijöiden saapumista, ja se "
            "on edelleen yleinen Skandinaviassa ja Pohjois-Euroopassa."
        ),
        "references": [
            "Lazaridis et al. 2014. Nature 513:409–413",
            "Skoglund et al. 2014. Science 344:747–750",
        ],
    },
]


# ---------------------------------------------------------------------------
# E1b1b  — Afrikka / Välimeri Y-DNA
# ---------------------------------------------------------------------------

HAPLOGROUP_SAMPLES["E1b1b"] = [

    {
        "id":        "ANCIENT-E1B-NORTH-AFRICA",
        "location":  "Taforalt cave, Morocco",
        "date":      "15000–12000 BCE",
        "culture":   "Iberomaurusian / North African Late Palaeolithic",
        "era_label": "Pohjois-Afrikan paleoliitti — Iberomaurusian",
        "lineage_fit": "Y-DNA",
        "coordinates": (34.8, -2.5),
        "context": (
            "Taforaltin luola Marokossa on yksi Pohjois-Afrikan tärkeimmistä "
            "paleoliittisista kohteista. E1b1b on dominoiva Y-haploryhmä "
            "Iberomaurusian-kulttuurissa (15 000–12 000 eaa.) — näistä miehistä "
            "polveutuvat nykyiset berberi- eli amazigh-kansat. E1b1b on myös "
            "laajalle levinnyt Itä-Afrikassa, Etiopiassa ja Välimeren piirissä, "
            "ja se on yleinen erityisesti Kreikassa, Sardiniassa ja Turkissa."
        ),
        "references": [
            "Fregel et al. 2018. PNAS 115:6774–6779",
            "van de Loosdrecht et al. 2018. Science 360:548–552",
        ],
    },
]


# ---------------------------------------------------------------------------
# Hakufunktiot
# ---------------------------------------------------------------------------

def get_samples_for_haplogroup(haplogroup: str) -> List[AncientSample]:
    """
    Palauttaa muinaisnäytteet haploryhmälle.
    Etsintäjärjestys (spesifisimmästä yleisimpään):
      1. Täsmällinen avain (esim. "H1-T16189C")
      2. Lyhin etuliitteeseensopiva avain (esim. "H1" → "H1-T16189C".startswith("H1") = True)
      3. Tyhjä lista

    Esimerkki:
        get_samples_for_haplogroup("H1-T16189C")  → H1-T16189C -näytteet (5 kpl)
        get_samples_for_haplogroup("H1a1")        → H1-näytteet (fallback)
        get_samples_for_haplogroup("R1b-M269")    → R1b-näytteet
        get_samples_for_haplogroup("R1b-L21")     → R1b-näytteet
    """
    hg = haplogroup.strip()
    hg_upper = hg.upper()

    # 1. Täsmällinen osuma (case-insensitive)
    for key in HAPLOGROUP_SAMPLES:
        if key.upper() == hg_upper:
            return HAPLOGROUP_SAMPLES[key]

    # 2. Etuliitehaku: valitaan pisin sopiva avain (tarkempi voittaa)
    best_key: Optional[str] = None
    best_len: int = 0
    for key in HAPLOGROUP_SAMPLES:
        key_upper = key.upper()
        if hg_upper.startswith(key_upper) and len(key_upper) > best_len:
            best_key = key
            best_len = len(key_upper)

    if best_key:
        return HAPLOGROUP_SAMPLES[best_key]

    return []


def get_sample_by_id(sample_id: str) -> Optional[AncientSample]:
    """Palauttaa yksittäisen näytteen ID:n perusteella."""
    for samples in HAPLOGROUP_SAMPLES.values():
        for s in samples:
            if s.get("id") == sample_id:
                return s
    return None


def list_supported_haplogroups() -> List[str]:
    """Palauttaa kaikki haplogroups joille on näytteitä."""
    return sorted(HAPLOGROUP_SAMPLES.keys())


def get_era_sequence(haplogroup: str) -> List[str]:
    """Palauttaa aikajärjestyksessä era_label-otsikot narratiivin lukujärjestystä varten."""
    samples = get_samples_for_haplogroup(haplogroup)
    seen = []
    for s in samples:
        era = s.get("era_label", "")
        if era and era not in seen:
            seen.append(era)
    return seen


# ---------------------------------------------------------------------------
# CLI-käyttö (kehittäjille)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys, json as _json

    hg = sys.argv[1] if len(sys.argv) > 1 else "H1-T16189C"
    samples = get_samples_for_haplogroup(hg)
    print(f"Haploryhmä: {hg} — {len(samples)} näytettä")
    print()
    for s in samples:
        print(f"  [{s['date']}] {s['id']} — {s['location']}")
        print(f"    Kulttuuri: {s['culture']}")
        print(f"    Era: {s['era_label']}")
        print(f"    Viitteet: {len(s['references'])} kpl")
        print()
