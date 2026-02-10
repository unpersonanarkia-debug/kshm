from typing import Dict, Optional

# -----------------------------
# Konfiguraatio
# -----------------------------

SUPPORTED_LANGUAGES = ["fi", "en", "sv", "de", "es", "fr", "ru", "zh", "ar"]
DEFAULT_LANG = "en"
DEFAULT_TONE = "chronological"  # academic | narrative | chronological | popular
DEFAULT_REGION = "global"

# -----------------------------
# Yleiset tekstipohjat
# -----------------------------

BASE_TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "haplogroup_title": {
        "fi": "Haploryhmä {haplogroup}",
        "en": "Haplogroup {haplogroup}",
        "sv": "Haplogrupp {haplogroup}",
        "de": "Haplogruppe {haplogroup}",
        "es": "Haplogrupo {haplogroup}",
        "fr": "Haplogroupe {haplogroup}",
        "ru": "Гаплогруппа {haplogroup}",
        "zh": "单倍群 {haplogroup}",
        "ar": "السلالة الجينية {haplogroup}",
    },
    "intro_overview": {
        "fi": "Tämä raportti esittelee haploryhmäsi arkeogeneettisen historian perustuen muinais-DNA-löytöihin, kulttuureihin ja väestöliikkeisiin.",
        "en": "This report presents the archaeogenetic history of your haplogroup based on ancient DNA findings, cultures, and population movements.",
        "sv": "Denna rapport presenterar den arkeogenetiska historien för din haplogrupp baserat på forntida DNA-fynd, kulturer och befolkningsrörelser.",
        "de": "Dieser Bericht präsentiert die archäogenetische Geschichte Ihrer Haplogruppe basierend auf alten DNA-Funden, Kulturen und Bevölkerungsbewegungen.",
        "es": "Este informe presenta la historia arqueogenética de su haplogrupo basada en hallazgos de ADN antiguo, culturas y movimientos poblacionales.",
        "fr": "Ce rapport présente l’histoire archéogénétique de votre haplogroupe basée sur des découvertes d’ADN ancien, des cultures et des mouvements de population.",
        "ru": "Этот отчет представляет археогенетическую историю вашей гаплогруппы на основе данных древней ДНК, культур и миграций.",
        "zh": "本报告基于古DNA发现、文化与人口迁移，呈现您的单倍群的考古遗传学历史。",
        "ar": "يعرض هذا التقرير التاريخ الجيني الأثري لسلالتك الجينية استنادًا إلى اكتشافات الحمض النووي القديم والثقافات وحركات السكان.",
    },
    "regions_label": {
        "fi": "Maantieteellinen levinneisyys",
        "en": "Geographic distribution",
        "sv": "Geografisk spridning",
        "de": "Geografische Verbreitung",
        "es": "Distribución geográfica",
        "fr": "Répartition géographique",
        "ru": "Географическое распространение",
        "zh": "地理分布",
        "ar": "التوزيع الجغرافي",
    },
    "ancient_samples_label": {
        "fi": "Muinaiset DNA-näytteet",
        "en": "Ancient DNA samples",
        "sv": "Forntida DNA-prover",
        "de": "Alte DNA-Proben",
        "es": "Muestras de ADN antiguo",
        "fr": "Échantillons d’ADN ancien",
        "ru": "Образцы древней ДНК",
        "zh": "古代DNA样本",
        "ar": "عينات الحمض النووي القديم",
    },
    "time_depth_label": {
        "fi": "Aikasyvyys",
        "en": "Time depth",
        "sv": "Tidsdjup",
        "de": "Zeitliche Tiefe",
        "es": "Profundidad temporal",
        "fr": "Profondeur temporelle",
        "ru": "Временная глубина",
        "zh": "时间深度",
        "ar": "العمق الزمني",
    },
    "sources_label": {
        "fi": "Lähteet",
        "en": "Sources",
        "sv": "Källor",
        "de": "Quellen",
        "es": "Fuentes",
        "fr": "Sources",
        "ru": "Источники",
        "zh": "来源",
        "ar": "المصادر",
    },
    "privacy_notice": {
        "fi": "Huomio: Tämä raportti ei sisällä henkilökohtaisia DNA-tietoja, vain haploryhmään perustuvaa väestöhistoriallista analyysia.",
        "en": "Note: This report does not contain personal DNA data, only population-level haplogroup analysis.",
        "sv": "Obs: Denna rapport innehåller inte personliga DNA-data, endast befolkningsbaserad haplogruppsanalys.",
        "de": "Hinweis: Dieser Bericht enthält keine persönlichen DNA-Daten, sondern nur eine populationsbasierte Haplogruppenanalyse.",
        "es": "Nota: Este informe no contiene datos personales de ADN, solo análisis poblacionales de haplogrupos.",
        "fr": "Remarque : Ce rapport ne contient pas de données ADN personnelles, uniquement une analyse de haplogroupes à l’échelle de la population.",
        "ru": "Примечание: В этом отчете нет персональных данных ДНК, только анализ на уровне популяций.",
        "zh": "注意：本报告不包含个人DNA数据，仅提供群体层面的单倍群分析。",
        "ar": "ملاحظة: لا يحتوي هذا التقرير على بيانات DNA شخصية، بل على تحليل سكاني قائم على السلالة الجينية فقط.",
    },
}

# -----------------------------
# Kerrontatyylit (tone layer)
# -----------------------------

TONE_VARIANTS: Dict[str, Dict[str, Dict[str, str]]] = {
    "academic": {
        "section_intro": {
            "fi": "Seuraava osio esittää tieteellisen yhteenvedon arkeogeneettisestä aineistosta.",
            "en": "The following section presents a scientific summary of the archaeogenetic evidence.",
            "sv": "Följande avsnitt presenterar en vetenskaplig sammanfattning av det arkeogenetiska materialet.",
            "de": "Der folgende Abschnitt präsentiert eine wissenschaftliche Zusammenfassung der archäogenetischen Evidenz.",
            "es": "La siguiente sección presenta un resumen científico de la evidencia arqueogenética.",
            "fr": "La section suivante présente un résumé scientifique des données archéogénétiques.",
            "ru": "Следующий раздел представляет научное резюме археогенетических данных.",
            "zh": "以下部分提供考古遗传学证据的科学总结。",
            "ar": "يقدم القسم التالي ملخصًا علميًا للأدلة الجينية الأثرية.",
        }
    },
    "narrative": {
        "section_intro": {
            "fi": "Seuraava osio kertoo tarinan ihmisistä, jotka kantoivat tätä haploryhmää halki aikojen.",
            "en": "The following section tells the story of the people who carried this haplogroup across time.",
            "sv": "Följande avsnitt berättar historien om människorna som bar denna haplogrupp genom tiderna.",
            "de": "Der folgende Abschnitt erzählt die Geschichte der Menschen, die diese Haplogruppe durch die Zeit trugen.",
            "es": "La siguiente sección cuenta la historia de las personas que portaron este haplogrupo a través del tiempo.",
            "fr": "La section suivante raconte l’histoire des personnes qui ont porté cet haplogroupe à travers le temps.",
            "ru": "Следующий раздел рассказывает историю людей, носивших эту гаплогруппу сквозь времена.",
            "zh": "以下部分讲述了携带该单倍群的人们穿越时间的故事。",
            "ar": "يسرد القسم التالي قصة الأشخاص الذين حملوا هذه السلالة عبر العصور.",
        }
    },
    "chronological": {
        "section_intro": {
            "fi": "Seuraava osio esittää kronologisen katsauksen haploryhmän arkeologisiin löytöihin ja liikkeisiin.",
            "en": "The following section presents a chronological overview of archaeological findings and movements of the haplogroup.",
            "sv": "Följande avsnitt ger en kronologisk översikt över haplogruppens arkeologiska fynd och rörelser.",
            "de": "Der folgende Abschnitt bietet eine chronologische Übersicht über archäologische Funde und Bewegungen der Haplogruppe.",
            "es": "La siguiente sección presenta una visión cronológica de los hallazgos arqueológicos y movimientos del haplogrupo.",
            "fr": "La section suivante présente un aperçu chronologique des découvertes archéologiques et des déplacements du haplogroupe.",
            "ru": "Следующий раздел представляет хронологический обзор археологических находок и перемещений гаплогруппы.",
            "zh": "以下部分按时间顺序概述该单倍群的考古发现和迁移。",
            "ar": "يعرض القسم التالي نظرة زمنية على الاكتشافات الأثرية وتحركات السلالة.",
        }
    },
    "popular": {
        "section_intro": {
            "fi": "Seuraava osio kertoo ymmärrettävästi ja kiinnostavasti haploryhmäsi matkasta.",
            "en": "The following section explains your haplogroup’s journey in an accessible and engaging way.",
            "sv": "Följande avsnitt förklarar din haplogrupps resa på ett lättförståeligt och engagerande sätt.",
            "de": "Der folgende Abschnitt erklärt die Reise Ihrer Haplogruppe auf verständliche und ansprechende Weise.",
            "es": "La siguiente sección explica el viaje de su haplogrupo de forma accesible e interesante.",
            "fr": "La section suivante explique le parcours de votre haplogroupe de manière accessible et captivante.",
            "ru": "Следующий раздел доступно и увлекательно объясняет путь вашей гаплогруппы.",
            "zh": "以下部分以通俗易懂且引人入胜的方式讲述您的单倍群旅程。",
            "ar": "يشرح القسم التالي رحلة سلالتك الجينية بأسلوب مبسط وجذاب.",
        }
    },
}

# -----------------------------
# Alueellinen sävy (region layer)
# -----------------------------

REGIONAL_VARIANTS: Dict[str, Dict[str, Dict[str, str]]] = {
    "europe": {
        "region_focus": {
            "fi": "Eurooppalaisessa kontekstissa haploryhmä on liitetty erityisesti neoliittisiin ja pronssikautisiin kulttuureihin.",
            "en": "In a European context, this haplogroup is particularly associated with Neolithic and Bronze Age cultures.",
        }
    },
    "africa": {
        "region_focus": {
            "fi": "Afrikassa haploryhmä liittyy usein varhaisiin metsästäjä-keräilijä- ja paimentolaiskulttuureihin.",
            "en": "In Africa, this haplogroup is often associated with early hunter-gatherer and pastoralist cultures.",
        }
    },
    "asia": {
        "region_focus": {
            "fi": "Aasiassa haploryhmä esiintyy useissa varhaisissa maanviljely- ja vaelluskulttuureissa.",
            "en": "In Asia, this haplogroup appears in multiple early agricultural and migratory cultures.",
        }
    },
    "americas": {
        "region_focus": {
            "fi": "Amerikoissa haploryhmä liittyy varhaisiin muuttoliikkeisiin Beringian kautta ja myöhempiin alkuperäiskulttuureihin.",
            "en": "In the Americas, this haplogroup is associated with early migrations عبر Beringia and later Indigenous cultures.",
        }
    },
    "oceania": {
        "region_focus": {
            "fi": "Oseaniassa haploryhmä kytkeytyy merellisiin vaelluksiin ja Polynesian, Melanesian ja Mikronesian kulttuureihin.",
            "en": "In Oceania, this haplogroup is linked to maritime migrations and Polynesian, Melanesian, and Micronesian cultures.",
        }
    },
}

# -----------------------------
# Ydintoiminnot
# -----------------------------

def get_text(
    key: str,
    lang: str = DEFAULT_LANG,
    tone: str = DEFAULT_TONE,
    region: str = DEFAULT_REGION,
    **kwargs
) -> str:
    """
    Palauttaa lokalisoidun tekstin huomioiden kielen, kerrontatyylin ja alueellisen sävyn.
    Fallback-logiikka: lang → DEFAULT_LANG → avain.
    """
    lang = normalize_language(lang)
    tone = normalize_tone(tone)
    region = normalize_region(region)

    # 1) Alueellinen variantti (jos avain on siellä)
    regional_entry = REGIONAL_VARIANTS.get(region, {}).get(key)
    if regional_entry:
        text = regional_entry.get(lang) or regional_entry.get(DEFAULT_LANG)
        if text:
            return format_text(text, **kwargs)

    # 2) Kerrontatyylin variantti
    tone_entry = TONE_VARIANTS.get(tone, {}).get(key)
    if tone_entry:
        text = tone_entry.get(lang) or tone_entry.get(DEFAULT_LANG)
        if text:
            return format_text(text, **kwargs)

    # 3) Perusteksti
    base_entry = BASE_TRANSLATIONS.get(key, {})
    text = base_entry.get(lang) or base_entry.get(DEFAULT_LANG) or key

    return format_text(text, **kwargs)

# -----------------------------
# Normalisointi & apufunktiot
# -----------------------------

def normalize_language(lang: Optional[str]) -> str:
    if not lang:
        return DEFAULT_LANG
    lang = lang.lower()
    return lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANG

def normalize_tone(tone: Optional[str]) -> str:
    if not tone:
        return DEFAULT_TONE
    tone = tone.lower()
    return tone if tone in TONE_VARIANTS else DEFAULT_TONE

def normalize_region(region: Optional[str]) -> str:
    if not region:
        return DEFAULT_REGION
    region = region.lower()
    return region if region in REGIONAL_VARIANTS else DEFAULT_REGION

def format_text(text: str, **kwargs) -> str:
    try:
        return text.format(**kwargs) if kwargs else text
    except Exception:
        return text

# -----------------------------
# Korkeamman tason koostajat
# -----------------------------

def build_intro(lang: str = DEFAULT_LANG, tone: str = DEFAULT_TONE, region: str = DEFAULT_REGION) -> str:
    title = get_text("haplogroup_title", lang, tone, region, haplogroup="{haplogroup}")
    intro = get_text("intro_overview", lang, tone, region)
    section = get_text("section_intro", lang, tone, region)
    return f"{title}\n\n{intro}\n\n{section}"

def build_privacy_notice(lang: str = DEFAULT_LANG) -> str:
    return get_text("privacy_notice", lang)

def build_label(label_key: str, lang: str = DEFAULT_LANG) -> str:
    return get_text(label_key, lang)
