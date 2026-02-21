"""
basal_markers.py — KSHM "sateenvarjo-selitykset" haploryhmille

Ongelma jonka tämä ratkaisee:
  Jotkut haploryhmät ovat niin laajoja tai erityisiä, että pelkkä
  kladitieto ilman kontekstuaalista johdantoa on harhaanjohtava tai
  vaatii erillisen selityksen ennen episodinarratiivia.

  Esimerkkejä:
    - N-M46 (Tat): Suomen ~60% Y-DNA, mutta "N1a1a1a1a4" kertoo käyttäjälle hyvin vähän
    - U-kokonaan: makrohaploryhmä josta H, V, K kaikki polveutuvat
    - HV0/V: refugio-yhteys jonka logiikka pitää avata
    - K: näyttää omalta haploryhmältä mutta on U8b:n juonne
    - mtDNA I ja J: helposti sekoitetaan Y-DNA I ja J -haploryhmiin

Rakenne per merkintä:
  {
    "id":              str,   # haploryhmätunniste (lyhyin yksilöivä)
    "lineage":         str,   # "mtDNA" | "Y-DNA" | "both"
    "parent":          str,   # yläkladi (esim. U8 → U)
    "children_note":   str,   # lyhyt kuvaus tärkeimmistä alakladeista
    "origin_region":   str,   # syntysijainti
    "origin_date_bce": int,   # arvioitu syntymisaika (negatiivinen = BCE)
    "tmrca_note":      str,   # TMRCA-selitys (YFull/ISOGG)
    "finland_relevance": str, # miksi tämä on relevantti KSHM:n Suomi-fokuksessa
    "narrative_hook":  str,   # tarina-aloitusvirke story_utils.py:lle (fi)
    "disambiguation":  str,   # varoitus sekaannusvaarasta (jos tarpeen)
    "references":      List[str],
  }

Hakufunktiot:
  get_basal_context(haplogroup)  → Dict | None
  is_basal(haplogroup)           → bool
  get_parent_context(haplogroup) → Dict | None  (yläkladin selitys)
"""

from __future__ import annotations
from typing import Dict, List, Optional


# ---------------------------------------------------------------------------
# Päärekisteri
# ---------------------------------------------------------------------------

BASAL_MARKERS: Dict[str, Dict] = {}


# ---------------------------------------------------------------------------
# mtDNA — U-makrohaploryhmä ja sen haarat
# ---------------------------------------------------------------------------

BASAL_MARKERS["U"] = {
    "id":              "U",
    "lineage":         "mtDNA",
    "parent":          "R",
    "children_note":   "U1–U8 + K (U8b-juonne). U5 on Euroopan vanhin tunnettu linja.",
    "origin_region":   "Lähi-itä / Lounais-Aasia",
    "origin_date_bce": -55000,
    "tmrca_note":      "TMRCA ~55 000 BCE (YFull mtDNA). Yksi ensimmäisistä Out-of-Africa -linjoista.",
    "finland_relevance": (
        "U on suomalaisen mtDNA-maiseman kattohaploryhmä. "
        "U5 (metsästäjä-keräilijät), U4 (itäinen WHG), K (EEF-neoliitti) "
        "ja U2 ovat kaikki sen haarat. Suomalaisessa väestössä U-haarat "
        "kattavat arviolta 30–40 % kaikista äitilinjoista."
    ),
    "narrative_hook": (
        "Kaikki U-haaran äitilinjat — U5:n jääkautiset metsästäjät, "
        "K:n neoliittiset viljelijät, U4:n arovaeltajat — juontuvat "
        "yhdestä naisesta joka eli Lounais-Aasiassa yli 55 000 vuotta sitten."
    ),
    "disambiguation":  None,
    "references": [
        "Torroni et al. 2001. Am. J. Hum. Genet. 69:1178–1190",
        "Soares et al. 2009. Am. J. Hum. Genet. 84:740–759",
        "YFull mtDNA tree v3.x — U node",
    ],
}

BASAL_MARKERS["U5"] = {
    "id":              "U5",
    "lineage":         "mtDNA",
    "parent":          "U",
    "children_note":   "U5a (itä/pohjoinen) ja U5b (länsi/refugio). U5b1 on vanhin Euroopassa dokumentoitu.",
    "origin_region":   "Eurooppa (tai sitä edeltävä siirtymä Lähi-idästä Eurooppaan)",
    "origin_date_bce": -45000,
    "tmrca_note":      "TMRCA ~45 000 BCE. Ranis-luolan (Saksa) näyte on tähän mennessä vanhin todistettu U5b1.",
    "finland_relevance": (
        "U5 on Euroopan mesoliittisten metsästäjä-keräilijöiden (WHG, SHG, EHG) "
        "dominoiva linja. Suomessa U5-haarat ovat erityisen yleisiä, koska "
        "mesoliittinen väestö säilyi Fennoskandian pohjoisosissa pidempään kuin "
        "Keski-Euroopassa. U5a1d ja U5b1b1 ovat yleisiä Suomessa ja Virossa."
    ),
    "narrative_hook": (
        "Noin 45 000 vuotta sitten — kauan ennen jääkauden pahimpia aikoja — "
        "yksi nainen kulki Eurooppaan. Hänen äitilinjansa, U5b1, löydettiin "
        "Ranis-luolasta Saksasta. Se on vanhin tunnettu eurooppalainen äitilinja. "
        "Sinun linjasi on tämän naisen suora perillinen."
    ),
    "disambiguation":  None,
    "references": [
        "Pearce et al. 2024. Nature — Ranis Cave, earliest modern Europeans",
        "Welker et al. 2024. Nature — Ilsenhöhle proteomics",
        "Fu et al. 2016. Nature 534:200–205 — Upper Palaeolithic European genomes",
        "Skoglund et al. 2014. Science 344:747–750",
    ],
}

BASAL_MARKERS["U8"] = {
    "id":              "U8",
    "lineage":         "mtDNA",
    "parent":          "U",
    "children_note":   "U8a (harvinainen Lähi-itä), U8b → K (K1, K2). K on U8b:n ainoa laajalle levinnyt haara.",
    "origin_region":   "Lähi-itä",
    "origin_date_bce": -40000,
    "tmrca_note":      "U8 itsessään harvinainen. K (U8b) on käytännössä kaikki mitä U8:sta on jäljellä.",
    "finland_relevance": (
        "U8 ei suoraan esiinny Suomessa, mutta sen juonne K on yleinen. "
        "K1a erityisesti on Anatolian neoliittisten viljelijöiden (EEF) merkkilinja "
        "joka tuli Eurooppaan ~8 000–7 000 eaa."
    ),
    "narrative_hook": (
        "K-haploryhmä näyttää omalta, mutta se on U8b:n juonne — "
        "osa samaa U-perhettä kuin U5:n jääkautiset metsästäjät. "
        "Reitti kulki Lähi-idästä Anatoliaan ja sieltä Eurooppaan neoliitissa."
    ),
    "disambiguation":  None,
    "references": [
        "Behar et al. 2008. Am. J. Hum. Genet. 82:1130–1140",
        "Soares et al. 2009. Am. J. Hum. Genet. 84:740–759",
    ],
}

BASAL_MARKERS["K"] = {
    "id":              "K",
    "lineage":         "mtDNA",
    "parent":          "U8",
    "children_note":   "K1 (K1a, K1b, K1c) ja K2 (K2a, K2b). K1a on ylivoimaisesti yleisin.",
    "origin_region":   "Lähi-itä / Anatolia",
    "origin_date_bce": -22000,
    "tmrca_note":      "K TMRCA ~22 000 BCE (YFull). K1a laajeni voimakkaasti neoliittisen ekspansion myötä.",
    "finland_relevance": (
        "K, erityisesti K1a ja K1a+195, on yleinen Euroopan neoliittisten "
        "viljelijöiden (EEF) jälkeläisissä. Suomessa K esiintyy kohtalaisen "
        "usein, erityisesti lounaassa missä EEF-komponentti on vahvempi. "
        "K2a on vanhempi linja, jonka vanhin näyte on Iranin Belt Cave ~10 000 BCE."
    ),
    "narrative_hook": (
        "K näyttää ensisilmäyksellä erilliseltä haploryhmältä, mutta se on "
        "U8b:n tytärhaara — sukulainen U5:n jääkautisille metsästäjille. "
        "K:n kantajat olivat Anatolian ja Levanttin varhaiset viljelijät, "
        "jotka toivat maanviljelyn Eurooppaan noin 8 000 vuotta sitten."
    ),
    "disambiguation": (
        "K on mtDNA-haploryhmä. Älä sekoita Y-DNA-haploryhmiin. "
        "Myös: K1a+195-merkintä tarkoittaa lisämutaatiota position 195:ssä — "
        "se ei ole erillinen haploryhmä vaan K1a:n alatunnus."
    ),
    "references": [
        "Behar et al. 2008. Am. J. Hum. Genet. 82:1130–1140",
        "Lazaridis et al. 2016. Nature 536:419–424",
        "Mathieson et al. 2015. Nature 522:197–202",
    ],
}

# ---------------------------------------------------------------------------
# mtDNA — HV-makrohaploryhmä, H, V, HV0
# ---------------------------------------------------------------------------

BASAL_MARKERS["HV"] = {
    "id":              "HV",
    "lineage":         "mtDNA",
    "parent":          "R",
    "children_note":   "H (Euroopan yleisin), V (refugio-linja), HV0 (H:n ja V:n esiaste).",
    "origin_region":   "Lähi-itä",
    "origin_date_bce": -25000,
    "tmrca_note":      "HV TMRCA ~25 000 BCE. H erosi omaksi haarakseen ~20 000 BCE.",
    "finland_relevance": (
        "HV itsessään harvinainen Suomessa, mutta sen tyttäret H ja V ovat "
        "erittäin yleisiä. H on Euroopan yleisin mtDNA-haploryhmä (~40–50 % "
        "väestöstä), V on erityisen yleinen Saameilla (~60 %) ja Pohjois-Euroopassa."
    ),
    "narrative_hook": (
        "Lähi-idässä noin 25 000 vuotta sitten syntyi linja josta "
        "kehittyivät Euroopan kaksi yleisintä äitilinjaa: H, jota kantaa "
        "joka toinen eurooppalainen, ja V, joka on Saameilla erityisen yleinen."
    ),
    "disambiguation":  None,
    "references": [
        "Torroni et al. 2006. Curr. Biol. 16:781–785",
        "Soares et al. 2009. Am. J. Hum. Genet. 84:740–759",
    ],
}

BASAL_MARKERS["HV0"] = {
    "id":              "HV0",
    "lineage":         "mtDNA",
    "parent":          "HV",
    "children_note":   "HV0a, HV0+195, HV0e — kaikki johtavat V-haaraan tai ovat sen sisarlinjoja.",
    "origin_region":   "Iberian niemimaa / Länsi-Eurooppa",
    "origin_date_bce": -16000,
    "tmrca_note":      "HV0 syntyi todennäköisesti Franco-Cantabrian refugiossa ~16 000–12 000 BCE.",
    "finland_relevance": (
        "HV0 on V-haploryhmän välitön esiaste. V on erityisen yleinen "
        "Saameilla (~60 %), baskeilta ja Skandinaviassa. HV0a on dokumentoitu "
        "useissa Skandinavian mesoliittisissa ja neoliittisissa näytteissä."
    ),
    "narrative_hook": (
        "Jääkauden loppupuolella, kun jäätiköt alkoivat vetäytyä, "
        "Franco-Cantabrian refugiossa syntyi linja josta tuli "
        "Pohjois-Euroopan merkkilinja: HV0 → V. "
        "Saamelaisilla se on tänä päivänä yleisin äitilinja."
    ),
    "disambiguation":  None,
    "references": [
        "Torroni et al. 2001. Am. J. Hum. Genet. 69:1178–1190",
        "Malmström et al. 2009. Curr. Biol. 19:1758–1762",
    ],
}

BASAL_MARKERS["V"] = {
    "id":              "V",
    "lineage":         "mtDNA",
    "parent":          "HV0",
    "children_note":   "V7 (Skandinavia), V1–V6, V15–V22. V on harvinaisempi kuin H mutta erittäin spesifi Pohjois-Euroopassa.",
    "origin_region":   "Iberian niemimaa / Skandinavia",
    "origin_date_bce": -12000,
    "tmrca_note":      "V TMRCA ~12 000 BCE. Levisi refugiosta Skandinaviaan jääkauden jälkeen.",
    "finland_relevance": (
        "V on erityisen merkittävä saamelaisessa geneettisessä perimässä (~60 %). "
        "Suomalaisessa väestössä V on kohtalainen (~4–8 %). "
        "Se on Pohjois-Euroopan mesoliittisen alkuperäisväestön merkkilinja, "
        "joka säilyi pohjoisen refugioalueilla myös neoliittisen muuton aikana."
    ),
    "narrative_hook": (
        "V on Pohjolan äitilinja. Se syntyi jääkauden jälkeen, kulki "
        "Pyreneiden vuoristosta pohjoiseen ja jäi lopulta Fennoskandiaan — "
        "erityisesti saamelaisiin, joilla se on tänä päivänä lähes "
        "joka toisen naisen äitilinja."
    ),
    "disambiguation":  None,
    "references": [
        "Torroni et al. 2001. Am. J. Hum. Genet. 69:1178–1190",
        "Saag et al. 2019. Curr. Biol. 29:3445–3456",
        "Lamnidis et al. 2018. Nature Comm. 9:5018",
    ],
}

# ---------------------------------------------------------------------------
# mtDNA — W
# ---------------------------------------------------------------------------

BASAL_MARKERS["W"] = {
    "id":              "W",
    "lineage":         "mtDNA",
    "parent":          "N",
    "children_note":   "W1 (W1c, W1+119), W3 (W3a1, W3b), W5, W6 (W6a). W3a1 on erityisen yleinen Keski-Aasiassa.",
    "origin_region":   "Lähi-itä / Lounais-Aasia",
    "origin_date_bce": -25000,
    "tmrca_note":      "W TMRCA ~25 000 BCE. Leviää Eurooppaan neoliittisten aaltojen mukana.",
    "finland_relevance": (
        "W on Euroopassa harvinaisempi kuin H tai U, mutta esiintyy "
        "säännöllisesti Itä-Euroopassa ja Baltiassa. Suomessa W on pieni "
        "mutta dokumentoitu komponentti, erityisesti kaakkoisessa Suomessa. "
        "W1+119 on vanhimpia W-linjoja, dokumentoitu jo Turkin neoliitissa ~6 300 BCE."
    ),
    "narrative_hook": (
        "W-haploryhmä kulki pitkän matkan: Lähi-idästä Anatolian läpi "
        "Keski-Aasiaan ja sieltä takaisin länteen neoliittisten aaltojen "
        "ja myöhempien arovaeltajien mukana. Se on harvinainen mutta "
        "kertoo kaukaisista yhteyksistä."
    ),
    "disambiguation":  None,
    "references": [
        "Soares et al. 2009. Am. J. Hum. Genet. 84:740–759",
        "Haak et al. 2015. Nature 522:207–211",
    ],
}

# ---------------------------------------------------------------------------
# mtDNA — N makrohaploryhmä
# ---------------------------------------------------------------------------

BASAL_MARKERS["N"] = {
    "id":              "N",
    "lineage":         "mtDNA",
    "parent":          "L3",
    "children_note":   (
        "N on jättimäinen makrohaploryhmä: sisältää R (→ U, H, V, T, J, K, B, P), "
        "A, W, X, I, N1, N9 ja muita. Lähes kaikki ei-afrikkalaiset mtDNA-linjat "
        "ovat joko N:n tai M:n haarat."
    ),
    "origin_region":   "Lähi-itä / Arabian niemimaa",
    "origin_date_bce": -70000,
    "tmrca_note":      "N TMRCA ~70 000–65 000 BCE. Out-of-Africa -ekspansion ydinlinja.",
    "finland_relevance": (
        "N itsessään ei esiinny suoraan — se on niin basaali taso että "
        "käytännössä jokainen eurooppalainen äitilinja (H, U, T, J, K, V, W...) "
        "on N:n jälkeläinen. Kontekstiselitys tarpeen jos haploryhmäraportissa "
        "lukee pelkkä 'N' (tarkoittaa usein N1-alakladeja kuten N1a)."
    ),
    "narrative_hook": (
        "N on niin vanha linja, ettei sen 'tarina' ole yhden paikan tarina — "
        "se on itse Out-of-Africa-ekspansio. Noin 70 000 vuotta sitten "
        "pieni joukko ihmisiä lähti Afrikasta. Heidän mukanaan lähti linja "
        "josta kehittyi käytännössä kaikki eurooppalainen, aasialainen "
        "ja alkuperäisamerikkalainen äitiperimä."
    ),
    "disambiguation": (
        "Pelkkä 'N' haploryhmäraportissa voi tarkoittaa: (1) makrohaploryhmä N "
        "jota ei ole tarkemmin luokiteltu, tai (2) N1-alakladi (varhaiset EEF-viljelijät). "
        "Tarkista konteksti — N1a on täysin eri tarina kuin 'kaikki N-haarat'."
    ),
    "references": [
        "Soares et al. 2009. Am. J. Hum. Genet. 84:740–759",
        "Behar et al. 2012. PLoS ONE 7:e52905",
    ],
}

BASAL_MARKERS["N1a"] = {
    "id":              "N1a",
    "lineage":         "mtDNA",
    "parent":          "N1",
    "children_note":   "N1a1 (LBK-kulttuuri), N1a1a1, N1a1a1a-alakladit. N1a1a1a2 on Keski-Euroopan neoliitissa yleisin.",
    "origin_region":   "Lähi-itä / Anatolia",
    "origin_date_bce": -10000,
    "tmrca_note":      "N1a TMRCA ~10 000 BCE. Levisi Eurooppaan LBK-kulttuurin mukana ~5 500–4 900 BCE.",
    "finland_relevance": (
        "N1a on eurooppalaisen neoliittisen ekspansion (EEF) yksi merkkilinjoista. "
        "Haak et al. 2010 osoitti sen olevan erityisen yleinen LBK-kulttuurin "
        "varhaisissa näytteissä Keski-Euroopassa. Suomessa harvinainen, "
        "mutta kertoo neoliittisesta komponentista jos esiintyy."
    ),
    "narrative_hook": (
        "N1a:n kantajat olivat Euroopan ensimmäisiä viljelijöitä — "
        "he saapuivat Anatoliasta noin 5 500 eaa. ja rakensivat "
        "LBK-kulttuurin kylät Reinin ja Tonavan laaksoihin. "
        "Heidän äitilinjansa dokumentoidaan jo Çatalhöyükistä."
    ),
    "disambiguation":  None,
    "references": [
        "Haak et al. 2010. Science 329:101–104",
        "Lazaridis et al. 2014. Nature 513:409–413",
        "Mathieson et al. 2015. Nature 522:197–202",
    ],
}

# ---------------------------------------------------------------------------
# mtDNA — I ja J (sekaannusvaara)
# ---------------------------------------------------------------------------

BASAL_MARKERS["I"] = {
    "id":              "I",
    "lineage":         "mtDNA",
    "parent":          "N",
    "children_note":   "I1–I7. I4a on yleisin Euroopan pronssikauden näytteissä.",
    "origin_region":   "Lähi-itä",
    "origin_date_bce": -30000,
    "tmrca_note":      "I TMRCA ~30 000 BCE. Harvinainen — alle 2 % eurooppalaisista.",
    "finland_relevance": (
        "mtDNA I on harvinainen Suomessa. Esiintyy satunnaisesti erityisesti "
        "pronssikauden ja rautakauden konteksteissa. I4a on yleinen "
        "Corded Ware / Steppe-peräisissä näytteissä."
    ),
    "narrative_hook": (
        "I on harvinainen merkki kaukaisesta Lähi-idän yhteydestä. "
        "Se kulkeutui Eurooppaan todennäköisesti arojen kautta, "
        "ei neoliittisessa maanviljelijäaallossa."
    ),
    "disambiguation": (
        "TÄRKEÄÄ: mtDNA haplogroup I on täysin eri kuin Y-DNA haplogroup I (I1, I2). "
        "Y-DNA I1 on yleinen skandinaavinen miesten linja (~30 % Suomessa). "
        "mtDNA I on harvinainen naisten äitilinja. Nämä eivät liity toisiinsa millään tavoin."
    ),
    "references": [
        "Soares et al. 2009. Am. J. Hum. Genet. 84:740–759",
        "Haak et al. 2015. Nature 522:207–211",
    ],
}

BASAL_MARKERS["J"] = {
    "id":              "J",
    "lineage":         "mtDNA",
    "parent":          "JT",
    "children_note":   "J1 (J1c yleisin Euroopassa), J2. J1c on erityisen yleinen neoliittisissa EEF-näytteissä.",
    "origin_region":   "Lähi-itä",
    "origin_date_bce": -40000,
    "tmrca_note":      "J TMRCA ~40 000 BCE. J1c levisi Eurooppaan neoliittisten viljelijöiden mukana.",
    "finland_relevance": (
        "mtDNA J, erityisesti J1c, on yleinen neoliittisen EEF-komponentin "
        "merkkilinja. Suomessa kohtalainen, erityisesti länsirannikolla "
        "ja lounaassa. J1c1 ja J1c3 ovat yleisimmät alakladit."
    ),
    "narrative_hook": (
        "J on Lähi-idän neoliittinen linja, joka saapui Eurooppaan "
        "maanviljelijöiden mukana. J1c:n kantajat kasvattivat "
        "einkorn-vehnää Çatalhöyükissä ennen kuin heidän jälkeläisensä "
        "rakensivat Stonehengea."
    ),
    "disambiguation": (
        "TÄRKEÄÄ: mtDNA haplogroup J on täysin eri kuin Y-DNA haplogroup J (J1, J2). "
        "Y-DNA J on Lähi-idän miesten linja. mtDNA J on naisten äitilinja. "
        "Molemmat ovat Lähi-itäistä alkuperää, mutta ne eivät liity toisiinsa suoraan."
    ),
    "references": [
        "Soares et al. 2009. Am. J. Hum. Genet. 84:740–759",
        "Lazaridis et al. 2016. Nature 536:419–424",
    ],
}

# ---------------------------------------------------------------------------
# Y-DNA — N-M46 / Tat (Suomen tärkein)
# ---------------------------------------------------------------------------
#
# NIMIHISTORIA — N-haploryhmässä on tapahtunut enemmän uudelleennimeämisiä
# kuin missään muussa Y-DNA-haploryhmässä. Tässä täydellinen aikajana:
#
# ISOGG 2006:  N3          (M46/Tat-klade)
#              N3a         (M178, Eurooppa+Siperia)
#              N3a1        (P21, Itä-Eurooppa)
# ISOGG 2008:  N1c         (M46/Tat, "formerly N3")
#              N1c1        (M178, "formerly N3a")
#              N1c1a       (P21, "formerly N3a1")
# ISOGG 2011:  N1c1        (M178 — päähaara säilyy)
#              N1c1 + L550 löydetty (Länsi-Suomi/Skandinavia)
# ISOGG 2015:  N1c1        (M178 — sama)
#              N1c1a1      (L708 — Eurooppa-haara)
# ISOGG 2017:  N1a1        (M46 — SUURI NIMIUUDISTUS)
#              N1a1a       (M178)
#              N1a1a1      (L392)
#              N1a1a1a     (L1026 — eurooppalais-siperialainen)
#              N1a1a1a1    (CTS2929/VL29 — Länsi-Eurooppa/Baltia/Suomi)
# ISOGG 2018+: N1a1        (M46, virallinen nimitys säilyy)
#              N1a1a1a1a   (CTS2929/VL29)
#              N1a1a1a1a1  (L550 — Länsi-Suomi, Skandinavia, Baltia)
#              N1a1a1a1a2  (Z1936 — Itä-Suomi, Karjala, Volgalaiset)
#
# ERITYINEN VAARA: Julkaisut ennen 2017 käyttävät N1c tai N1c1.
# Julkaisut 2017+ käyttävät N1a1. MOLEMMAT tarkoittavat samaa kladia.
# N3 on VAIN löydettävissä ennen 2008 julkaistuissa papereissa.
# ---------------------------------------------------------------------------

# Suomi-spesifiset alaklaadinimet (ISOGG 2018+):
#
#  N1a1a1a (L1026)       — koko eurooppalainen+siperialainen haara
#  N1a1a1a1 (VL29/CTS2929) — Länsi-Eurooppa, Baltia, Suomi, NW-Venäjä
#    ├── N1a1a1a1a1 (L550) — "Länsi-Suomi + Skandinavia + Baltia"
#    │     ├── N1a1a1a1a1a1 (M2783) — Liettua, Latvia (Baltti-haara)
#    │     └── N1a1a1a1a1a2 (Y4706) — Suomi, Skandinavia (Fennoskandiahaara)
#    └── N1a1a1a1a2 (Z1936/CTS10082) — "Itä-Suomi, Karjala, Komi, Volga"
#          └── N1a1a1a1a2a1 (Z1925) — Savon/Karjalan haara, myös Lappi
#  N1a1a1a2 (B211) — Udmurtit, Komit, Mansit (Uralin itäpuoli)
#
# Eupedian vanha nimistö (edelleen laajalti käytössä):
#  N1c1a1a1a1 = N1a1a1a1a1 (L550)   Länsi-Suomi
#  N1c1a1a1a2 = N1a1a1a1a2 (Z1936)  Itä-Suomi/Karjala
#  N1c1a1a1a1a1 = M2783              Baltit
#  N1c1a1a1a1a2 = Y4706              Fennoskandialaiset
# ---------------------------------------------------------------------------

BASAL_MARKERS["N-M46"] = {
    "id":              "N-M46",
    "lineage":         "Y-DNA",
    "parent":          "N-M231",
    "children_note":   (
        "Kaksi päähaaraa: (1) N1a1a1 (L392) — Siperia, Mongolia, Jakutia; "
        "(2) N1a1a1a (L1026) — Eurooppa + Länsi-Siperia. "
        "Eurooppalainen haara jakautuu edelleen: "
        "N1a1a1a1a1 (L550) = Länsi-Suomi + Skandinavia + Baltia, "
        "N1a1a1a1a2 (Z1936) = Itä-Suomi + Karjala + Volgalaiset."
    ),
    "origin_region":   "Koillis-Aasia / Siperia (Baikal-alue)",
    "origin_date_bce": -16000,
    "tmrca_note":      (
        "Tat-mutaatio (M46/P105) syntyi arviolta 16 000–14 000 BCE Koillis-Aasiassa. "
        "Vanhimmat aDNA-näytteet ovat Trans-Baikalista (~6 000–8 000 BCE). "
        "Eurooppalainen haara (L1026) erosi ~8 000 BCE, "
        "VL29-haara ~3 600 BCE (Kiukainen-kulttuurin aika), "
        "L550-haara (Suomi/Skandinavia) ja Z1936-haara (Itä-Suomi) "
        "erosivat toisistaan ~2 600 BCE."
    ),
    "finland_relevance": (
        "N-Tat on Suomen ylivoimaisesti yleisin Y-DNA-haploryhmä (~60 %). "
        "Saag et al. 2019 osoitti: Siperialaista autosomaalia DNA:ta ja "
        "Y-haploryhmä N1c puuttuivat pronssikaudelta Virosta — ne saapuivat "
        "vasta rautakaudella (~500 BCE). Tämä ankkuroi N-Tatin Suomeen "
        "historiallisesti myöhäiseen ajankohtaan, ei Kivikautiseen asutukseen. "
        "Suomalaiselle linjalle tyypilliset haarat: "
        "L550 (Länsi-Suomi, Eura, Turku) ja Z1936/Z1925 (Savo, Karjala, Lappi). "
        "Uralilaisten kielten korrelaatio N-Tatin kanssa on vahva mutta "
        "ei täydellinen — haploryhmä levisi nopeammin kuin kielet."
    ),
    "narrative_hook": (
        "Noin 14 000 vuotta sitten Siperiassa syntyi mutaatio — Tat. "
        "Se on pieni muutos Y-kromosomissa, mutta sen kantajat vaelsivat "
        "länteen ja pohjoiseen niin menestyksekkäästi, että tänä päivänä "
        "kuusi kymmenestä suomalaisesta miehestä kantaa sitä. "
        "Samaa linjaa kantavat myös virolaiset, saamelaisten suuri osa, "
        "ja se korreloi suomenkielisyyden kanssa vahvemmin kuin "
        "mikään muu tunnistettu Y-DNA-merkki Euroopassa."
    ),
    "disambiguation": (
        "NIMIKAOS: N-M46-klade on nimetty uudelleen useita kertoja. "
        "N3 = N1c = N1c1 = N1a1 — kaikki tarkoittavat samaa Tat-mutaation määrittelemää kladia. "
        "Aikajana: N3 (ISOGG ≤2006) → N1c/N1c1 (ISOGG 2008–2016) → N1a1 (ISOGG 2017+). "
        "VAROITUS 1: N3 on VAIN vanha nimi N-Tat:ille — ÄLÄ sekoita mtDNA:n N3:een "
        "(joka on aivan eri linja, esiintyy vain Valko-Venäjällä). "
        "VAROITUS 2: N1c tarkoittaa eri asiaa mtDNA:ssa (harvinainen mtDNA-haploryhmä) "
        "kuin Y-DNA:ssa (= N-Tat). Aina tarkistettava konteksti. "
        "VAROITUS 3: N1a1 Y-DNA:ssa ≠ N1a mtDNA:ssa. "
        "N1a mtDNA = LBK-viljelijöiden haploryhmä (Anatoliasta). "
        "N1a1 Y-DNA = Tat/M46 (Siperiasta). Täysin eri linjat."
    ),
    # Suomi-spesififit alaklaadialiaset — molemmat nimistöt
    "subclades_finland": {
        "L550":  {
            "isogg_new": "N1a1a1a1a1",
            "isogg_old": "N1c1a1a1a1",
            "distribution": "Länsi-Suomi, Skandinavia, Baltia",
            "note": "Etelä-Baltian haara (M2783) ja Fennoskandian haara (Y4706) erosivat ~2 600 BCE",
        },
        "Z1936": {
            "isogg_new": "N1a1a1a1a2",
            "isogg_old": "N1c1a1a1a2",
            "distribution": "Itä-Suomi, Karjala, Komi, Volga-tatarit",
            "note": "Z1925-alahaara tyypillinen Savolle, Karjalalle ja Lapille",
        },
        "VL29":  {
            "isogg_new": "N1a1a1a1a",
            "isogg_old": "N1c1a1a1",
            "distribution": "koko Fennoskandia+Baltia+NW-Venäjä",
            "note": "Kattaa L550 + Z1936 — vanhin yhteinen eurooppalainen haara, ~3 600 BCE",
        },
        "L1026": {
            "isogg_new": "N1a1a1a",
            "isogg_old": "N1c1a1a",
            "distribution": "Eurooppa + Länsi-Siperia",
            "note": "Uralin ylitys ~4 000 BCE — haarautui Euroopan puolelle",
        },
    },
    "references": [
        "Rootsi et al. 2007. Eur. J. Hum. Genet. 15:204–211",
        "Ilumäe et al. 2016. Am. J. Hum. Genet. 99:163–173 (non-trivial phylogeography)",
        "Lamnidis et al. 2018. Nature Comm. 9:5018 (Levänluhta, Kola)",
        "Saag et al. 2019. Curr. Biol. 29:3445–3456 (N-Tat saapuu rautakaudella)",
        "Tambets et al. 2018. Curr. Biol. 28:2277–2283 (Suomen geneettiset rajat)",
        "ISOGG 2008 N-tree (N3→N1c muutos)",
        "ISOGG 2018 N-tree (N1c→N1a1 muutos)",
    ],
}

# ---------------------------------------------------------------------------
# N-M46 ALIAS-TAULUKKO — kaikki historialliset nimet
# ---------------------------------------------------------------------------
# Periaate: kaikki alle listatut ovat VAIN Y-DNA N-Tat -kladin nimiä.
# mtDNA:n sekaannusten välttämiseksi N1a1 EI ole alias täällä
# (N1a mtDNA = LBK-viljelijät, täysin eri linja).

# Vanhat ISOGG-nimet (2006–2016) — kaikki = N-Tat
BASAL_MARKERS["N3"]       = BASAL_MARKERS["N-M46"]   # ISOGG ≤2006
BASAL_MARKERS["N1c"]      = BASAL_MARKERS["N-M46"]   # ISOGG 2008–2016
BASAL_MARKERS["N1c1"]     = BASAL_MARKERS["N-M46"]   # ISOGG 2008–2016 (M178)
BASAL_MARKERS["N-TAT"]    = BASAL_MARKERS["N-M46"]   # SNP-nimi (synonyymi M46)
BASAL_MARKERS["N-Tat"]    = BASAL_MARKERS["N-M46"]   # sama, eri kirjoitusasu
BASAL_MARKERS["N-P105"]   = BASAL_MARKERS["N-M46"]   # SNP-synonyymi (P105 = M46)
BASAL_MARKERS["N-M178"]   = BASAL_MARKERS["N-M46"]   # M178 = N1c1 = N1a1a

# Uudet ISOGG-nimet (2017+)
# N1a1 EI lisätä aliakseksi — mtDNA-konflikti (ks. yllä)
# Käytetään SNP-pohjaisia nimiä jotka ovat yksiselitteisiä
BASAL_MARKERS["N-L1026"]  = BASAL_MARKERS["N-M46"]   # eurooppalainen päähaara
BASAL_MARKERS["N-VL29"]   = BASAL_MARKERS["N-M46"]   # Baltia+Suomi+NW-Venäjä
BASAL_MARKERS["N-L550"]   = BASAL_MARKERS["N-M46"]   # Länsi-Suomi+Skandinavia
BASAL_MARKERS["N-Z1936"]  = BASAL_MARKERS["N-M46"]   # Itä-Suomi+Karjala+Volga

# Eupedian nimistö (edelleen laajalti käytössä blogeissa/foorumeilla)
BASAL_MARKERS["N1c1a1a1a1"]  = BASAL_MARKERS["N-M46"]   # = L550
BASAL_MARKERS["N1c1a1a1a2"]  = BASAL_MARKERS["N-M46"]   # = Z1936
BASAL_MARKERS["N1c1a1a"]     = BASAL_MARKERS["N-M46"]   # = L1026

# ---------------------------------------------------------------------------
# Y-DNA — I1 (Skandinaavinen)
# ---------------------------------------------------------------------------

BASAL_MARKERS["I1"] = {
    "id":              "I1",
    "lineage":         "Y-DNA",
    "parent":          "I",
    "children_note":   "I1-M253. Alahaarat: I1a1 (Pohjoismaat), I1a2 (Norja/Islanti), I1a3 (Länsi-Eurooppa).",
    "origin_region":   "Skandinavia / Pohjois-Eurooppa",
    "origin_date_bce": -5000,
    "tmrca_note":      "I1 TMRCA ~5 000 BCE (YFull). Jyrkkä pullonkaula — kaikki nykyiset I1-miehet polveutuvat hyvin pienestä joukosta.",
    "finland_relevance": (
        "I1 on Suomen toiseksi yleisin Y-haploryhmä (~30 %). "
        "Se liittyy Skandinavian mesoliittisiin metsästäjä-keräilijöihin "
        "mutta nykymuodossaan edustaa viikinkiaikaista ja sitä edeltävää "
        "pohjoisgermanista populaatiota. Suomessa I1 saapui todennäköisesti "
        "sekä Scandinavian-suuntaisesta muuttoaallosta että viikinkiyhteyksiä pitkin."
    ),
    "narrative_hook": (
        "I1-linja kulki jääkauden yli pohjoisen refugioissa, "
        "nousi Skandinavian hallitsevaksi Y-DNA-linjaksi ja kulki "
        "viikinkiajan purjeiden mukana Islantiin, Normandiaan ja Suomeen. "
        "Se on Pohjoismaan miehen linja — metsästäjältä viikingille."
    ),
    "disambiguation": (
        "I1 on Y-DNA-haploryhmä (miesten isälinja). "
        "mtDNA haplogroup I (naisten äitilinja) on täysin eri asia. "
        "Sekaannus on yleinen — varmista konteksti."
    ),
    "references": [
        "Rootsi et al. 2004. Eur. J. Hum. Genet. 12:945–950",
        "Margaryan et al. 2020. Nature 585:390–396",
        "Skoglund et al. 2014. Science 344:747–750",
    ],
}

# ---------------------------------------------------------------------------
# Y-DNA — R1a
# ---------------------------------------------------------------------------

BASAL_MARKERS["R1a"] = {
    "id":              "R1a",
    "lineage":         "Y-DNA",
    "parent":          "R1",
    "children_note":   "R1a-M417: Z283 (Eurooppa), Z93 (Etelä-Aasia/Keski-Aasia). Suomessa Z283-haara.",
    "origin_region":   "Euraasian aro / Pontic-Kaspian aro",
    "origin_date_bce": -6000,
    "tmrca_note":      "R1a TMRCA ~6 000 BCE. Räjähdysmäinen kasvu ~3 000 BCE Yamnaya/Corded Ware -ekspansiossa.",
    "finland_relevance": (
        "R1a on Suomessa ~5–7 %. Se saapui Corded Ware -kulttuurin mukana "
        "noin 2 900–2 400 BCE ja edustaa protoindoeurooppalaista "
        "Steppe-komponenttia. R1a-Z283 on eurooppalainen haara, "
        "R1a-Z93 on Etelä- ja Keski-Aasian haara."
    ),
    "narrative_hook": (
        "R1a on protoindoeurooppalaisten aroihmisten linja. "
        "Noin 5 000 vuotta sitten Pontis-Kaspian aroilta lähti "
        "massiivinen muuttoaalto länteen ja itään — hevosten selässä, "
        "vaunujen rataisilla. R1a levisi Irlannista Intian niemimaan "
        "kärjelle saakka samassa sukupolvessa."
    ),
    "disambiguation":  None,
    "references": [
        "Haak et al. 2015. Nature 522:207–211",
        "Allentoft et al. 2015. Nature 522:167–172",
        "Anthony 2007. The Horse, the Wheel and Language",
    ],
}

# ---------------------------------------------------------------------------
# Y-DNA — R1b
# ---------------------------------------------------------------------------

BASAL_MARKERS["R1b"] = {
    "id":              "R1b",
    "lineage":         "Y-DNA",
    "parent":          "R1",
    "children_note":   "R1b-M269 (Länsi-Eurooppa: L21, U106, DF27), R1b-V1636 (Kaukasus/Steppe).",
    "origin_region":   "Pontic-Kaspian aro / Kaukasus",
    "origin_date_bce": -8000,
    "tmrca_note":      "R1b TMRCA ~8 000 BCE. R1b-M269 räjähdysmäinen kasvu Bell Beaker -ekspansiossa ~2 750 BCE.",
    "finland_relevance": (
        "R1b on Suomessa harvinainen (~3 %). Se on kuitenkin Länsi-Euroopan "
        "yleisin Y-haploryhmä (Irlanti >80 %, Wales >75 %). "
        "Suomessa R1b edustaa pientä mutta selkeää länsieuropalaista yhteyttä, "
        "todennäköisesti pronssi- tai rautakaudelta."
    ),
    "narrative_hook": (
        "R1b on Bell Beaker -kulttuurin linja — sama väestö joka rakensi "
        "Stonehengen loppuun, valloitti Brittein saaret alle 500 vuodessa "
        "ja antoi sen asukkaille kelttiläiset kielet. "
        "Länsi-Euroopassa se on hallitseva linja, Suomessa harvinainen vieras."
    ),
    "disambiguation":  None,
    "references": [
        "Olalde et al. 2018. Nature 555:190–196",
        "Haak et al. 2015. Nature 522:207–211",
    ],
}


# ---------------------------------------------------------------------------
# Hakufunktiot
# ---------------------------------------------------------------------------

def get_basal_context(haplogroup: str) -> Optional[Dict]:
    """
    Palauttaa basal-kontekstin haploryhmälle.

    Hakujärjestys:
      1. Täsmällinen avain (case-insensitive)
      2. Pisin etuliiteosuma (esim. "N1a1a1" → "N1a")
      3. None jos ei löydy

    Esimerkkejä:
      get_basal_context("U5b1")       → U5-konteksti
      get_basal_context("N-M46")      → N-M46/Tat-konteksti
      get_basal_context("K1a4a1")     → K-konteksti
      get_basal_context("H1-T16189C") → None (H ei ole basaali tässä mielessä)
    """
    hg_up = haplogroup.upper().strip()

    # 1. Täsmällinen osuma
    for key, val in BASAL_MARKERS.items():
        if key.upper() == hg_up:
            return val

    # 2. Pisin etuliiteosuma
    best_key = None
    best_len = 0
    for key in BASAL_MARKERS:
        k = key.upper()
        if hg_up.startswith(k) and len(k) > best_len:
            best_key = key
            best_len = len(k)

    if best_key:
        return BASAL_MARKERS[best_key]

    return None


def is_basal(haplogroup: str) -> bool:
    """Palauttaa True jos haploryhmälle on basal-konteksti."""
    return get_basal_context(haplogroup) is not None


def get_parent_context(haplogroup: str) -> Optional[Dict]:
    """
    Palauttaa yläkladin basal-kontekstin.
    Hyödyllinen kun halutaan lisätä "mistä tämä haara tuli" -kappale.

    Esimerkki:
      get_parent_context("K1a4a1") → K-konteksti (K on basaali)
      → K-kontekstin parent "U8" → U8-konteksti
    """
    ctx = get_basal_context(haplogroup)
    if ctx and ctx.get("parent"):
        return get_basal_context(ctx["parent"])
    return None


def list_basal_haplogroups(lineage: Optional[str] = None) -> List[str]:
    """
    Palauttaa kaikki rekisteröidyt basal-haploryhmät.
    lineage: "mtDNA" | "Y-DNA" | None (kaikki)
    """
    result = []
    seen = set()
    for key, val in BASAL_MARKERS.items():
        real_id = val.get("id", key)
        if real_id in seen:
            continue
        if lineage is None or val.get("lineage") == lineage:
            result.append(real_id)
            seen.add(real_id)
    return sorted(result)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    hg = sys.argv[1] if len(sys.argv) > 1 else "N-M46"
    ctx = get_basal_context(hg)

    if ctx:
        print(f"\n=== Basal-konteksti: {hg} ===\n")
        print(f"  ID:              {ctx['id']}")
        print(f"  Linja:           {ctx['lineage']}")
        print(f"  Yläkladi:        {ctx.get('parent', '—')}")
        print(f"  Syntyalue:       {ctx['origin_region']}")
        print(f"  TMRCA (arv.):    {ctx['origin_date_bce']} BCE")
        print(f"  Suomi-relevanssi:{ctx['finland_relevance'][:120]}...")
        print(f"\n  Tarina-aloitus:\n  {ctx['narrative_hook']}")
        if ctx.get("disambiguation"):
            print(f"\n  ⚠ SEKAANNUSVAARA:\n  {ctx['disambiguation']}")
    else:
        print(f"Ei basal-kontekstia haploryhmälle: {hg}")
        print(f"Saatavilla: {list_basal_haplogroups()}")
