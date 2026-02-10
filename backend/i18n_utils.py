from typing import Dict, List, Optional


SUPPORTED_LANGUAGES = [
    "fi", "en", "sv", "de", "fr", "es", "pt", "it", "ru", "zh", "ja", "ko",
    "ar", "he", "hi", "bn", "tr", "fa", "ur",
    "sw", "am", "yo", "zu",
    "id", "ms", "th", "vi", "tl",
    "pl", "cs", "sk", "hu", "ro", "bg", "el",
    "nl", "da", "no",
    "et", "lv", "lt",
    "is", "ga",
    "sr", "hr", "sl",
    "uk", "ka", "hy",
    "mn", "kk", "uz",
    "ta", "te", "kn", "ml",
    "ne", "si",
    "my", "km", "lo",
    "haw", "mi", "sm",
    "es-mx", "pt-br"
]


def get_supported_languages() -> List[str]:
    return SUPPORTED_LANGUAGES


def get_default_language() -> str:
    return "en"


def get_language_name(lang_code: str) -> str:
    names = {
        "fi": "Suomi", "en": "English", "sv": "Svenska", "de": "Deutsch",
        "fr": "Français", "es": "Español", "pt": "Português", "it": "Italiano",
        "ru": "Русский", "zh": "中文", "ja": "日本語", "ko": "한국어",
        "ar": "العربية", "he": "עברית", "hi": "हिन्दी", "bn": "বাংলা",
        "tr": "Türkçe", "fa": "فارسی", "ur": "اردو",
        "sw": "Kiswahili", "am": "አማርኛ", "yo": "Yorùbá", "zu": "isiZulu",
        "id": "Bahasa Indonesia", "ms": "Bahasa Melayu", "th": "ไทย",
        "vi": "Tiếng Việt", "tl": "Tagalog",
        "pl": "Polski", "cs": "Čeština", "sk": "Slovenčina", "hu": "Magyar",
        "ro": "Română", "bg": "Български", "el": "Ελληνικά",
        "nl": "Nederlands", "da": "Dansk", "no": "Norsk",
        "et": "Eesti", "lv": "Latviešu", "lt": "Lietuvių",
        "is": "Íslenska", "ga": "Gaeilge",
        "sr": "Српски", "hr": "Hrvatski", "sl": "Slovenščina",
        "uk": "Українська", "ka": "ქართული", "hy": "Հայերեն",
        "mn": "Монгол", "kk": "Қазақ", "uz": "Oʻzbek",
        "ta": "தமிழ்", "te": "తెలుగు", "kn": "ಕನ್ನಡ", "ml": "മലയാളം",
        "ne": "नेपाली", "si": "සිංහල",
        "my": "မြန်မာ", "km": "ខ្មែរ", "lo": "ລາວ",
        "haw": "ʻŌlelo Hawaiʻi", "mi": "Māori", "sm": "Gagana Samoa",
        "es-mx": "Español (México)", "pt-br": "Português (Brasil)"
    }
    return names.get(lang_code, lang_code)


def get_cultural_context(lang_code: str) -> str:
    """
    Palauttaa kulttuurisen viitekehyksen kuvaustekstin
    (käytetään tarinan sävyn ja metaforien muokkaukseen).
    """
    contexts = {
        "fi": "Luontosuhde, sukujuuret, maantieteellinen jatkuvuus",
        "en": "Exploration, ancestry, migration, discovery",
        "sv": "Historia, släktskap, nordisk identitet",
        "de": "Geschichte, Abstammung, kulturelle Entwicklung",
        "fr": "Héritage, civilisation, continuité humaine",
        "es": "Linaje, mestizaje, herencia cultural",
        "pt": "Ancestralidade, miscigenação, jornada histórica",
        "it": "Origini, civiltà, continuità culturale",
        "ru": "Родословная, цивилизация, историческое движение",
        "zh": "祖先、文明演进、族群迁徙",
        "ja": "祖先、伝統、歴史の連続性",
        "ko": "조상, 문화적 계승, 인류 이동",
        "ar": "الأنساب، الحضارة، الامتداد التاريخي",
        "he": "שורשים, מורשת, המשכיות היסטורית",
        "hi": "वंश, परंपरा, ऐतिहासिक प्रवाह",
        "bn": "বংশধারা, সংস্কৃতি, মানব ইতিহাস",
        "tr": "Soy, medeniyet, tarihsel süreklilik",
        "fa": "نسب، تمدن، پیوستگی تاریخی",
        "ur": "نسب، تہذیب، تاریخی تسلسل",
        "sw": "Ukoo, urithi wa kitamaduni, historia ya binadamu",
        "am": "ዘር፣ ባህል፣ ታሪካዊ ቀጥታ",
        "yo": "Ìtàn ìran, àṣà, ìtẹ̀síwájú ènìyàn",
        "zu": "Umsuka, amasiko, ukuqhubeka komlando",
        "id": "Asal-usul, peradaban, kesinambungan sejarah",
        "ms": "Keturunan, tamadun, kesinambungan sejarah",
        "th": "บรรพชน อารยธรรม ความต่อเนื่องทางประวัติศาสตร์",
        "vi": "Tổ tiên, văn minh, dòng chảy lịch sử",
        "tl": "Pinagmulan, kultura, kasaysayan ng sangkatauhan",
        "pl": "Pochodzenie, cywilizacja, ciągłość dziejowa",
        "cs": "Původ, civilizace, historická kontinuita",
        "sk": "Pôvod, civilizácia, historická kontinuita",
        "hu": "Származás, civilizáció, történelmi folytonosság",
        "ro": "Origini, civilizație, continuitate istorică",
        "bg": "Произход, цивилизация, историческа приемственост",
        "el": "Καταγωγή, πολιτισμός, ιστορική συνέχεια",
        "nl": "Afkomst, beschaving, historische continuïteit",
        "da": "Oprindelse, civilisation, historisk kontinuitet",
        "no": "Opprinnelse, sivilisasjon, historisk kontinuitet",
        "et": "Päritolu, tsivilisatsioon, ajalooline järjepidevus",
        "lv": "Izcelsme, civilizācija, vēsturiskā nepārtrauktība",
        "lt": "Kilmė, civilizacija, istorinė tęstinumas",
        "is": "Uppruni, siðmenning, söguleg samfella",
        "ga": "Bunús, sibhialtacht, leanúnachas stairiúil",
        "sr": "Порекло, цивилизација, историјски континуитет",
        "hr": "Podrijetlo, civilizacija, povijesni kontinuitet",
        "sl": "Izvor, civilizacija, zgodovinska kontinuiteta",
        "uk": "Походження, цивілізація, історична тяглість",
        "ka": "წარმოშობა, ცივილიზაცია, ისტორიული უწყვეტობა",
        "hy": "Ծագում, քաղաքակրթություն, պատմական շարունակություն",
        "mn": "Угсаа, соёл иргэншил, түүхэн үргэлжлэл",
        "kk": "Тегі, өркениет, тарихи сабақтастық",
        "uz": "Kelib chiqish, sivilizatsiya, tarixiy davomiylik",
        "ta": "மூலம், நாகரிகம், வரலாற்றுத் தொடர்ச்சி",
        "te": "వంశావళి, నాగరికత, చారిత్రక కొనసాగింపు",
        "kn": "ಮೂಲ, ನಾಗರಿಕತೆ, ಐತಿಹಾಸಿಕ ನಿರಂತರತೆ",
        "ml": "ഉത്ഭവം, സംസ്കാരം, ചരിത്രപരമായ തുടർച്ച",
        "ne": "वंश, सभ्यता, ऐतिहासिक निरन्तरता",
        "si": "වංශය, සivilization, ඉතිහාසමය සන්තානය",
        "my": "မျိုးရိုး, ယဉ်ကျေးမှု, သမိုင်းဆက်စပ်မှု",
        "km": "វង្ស, អរិយធម៌, ភាពបន្តប្រវត្តិសាស្ត្រ",
        "lo": "ສາຍເລືອດ, ອາລະຍະທຳ, ຄວາມຕໍ່ເນື່ອງທາງປະຫວັດສາດ",
        "haw": "Kumu, moʻomeheu, ka hoʻomau o ka moʻokūʻauhau",
        "mi": "Tīpuna, ahurea, rere tonu o te hītori",
        "sm": "Tupuaga, aganuʻu, faasoloaga faasolopito",
        "es-mx": "Raíces, mestizaje, herencia histórica",
        "pt-br": "Ancestralidade, diversidade, continuidade histórica",
    }
    return contexts.get(lang_code, contexts.get("en"))


def get_translation_templates() -> Dict[str, Dict[str, str]]:
    """
    Palauttaa kaikki käytettävät käännösmallit eri kielille.
    """
    return {
        "intro": {
            "fi": "Tämä raportti kertoo haploryhmäsi {haplogroup} arkeogeneettisen matkan läpi ihmiskunnan historian.",
            "en": "This report traces the archaeogenetic journey of your haplogroup {haplogroup} through human history.",
            "sv": "Denna rapport följer din haplogrupp {haplogroup} genom mänsklighetens arkeogenetiska historia.",
            "de": "Dieser Bericht verfolgt die archäogenetische Reise Ihrer Haplogruppe {haplogroup} durch die Menschheitsgeschichte.",
            "fr": "Ce rapport retrace le parcours archéogénétique de votre haplogroupe {haplogroup} à travers l’histoire humaine.",
            "es": "Este informe sigue el recorrido arqueogenético de tu haplogrupo {haplogroup} a lo largo de la historia humana.",
            "pt": "Este relatório acompanha a jornada arqueogenética do seu haplogrupo {haplogroup} ao longo da história humana.",
            "it": "Questo rapporto traccia il percorso archeogenetico del tuo aplogruppo {haplogroup} nella storia umana.",
            "ru": "Этот отчет прослеживает археогенетическое путешествие вашей гаплогруппы {haplogroup} в истории человечества.",
            "zh": "本报告追溯了您的单倍群 {haplogroup} 在人类历史中的考古遗传旅程。",
            "ja": "このレポートは、あなたのハプログループ {haplogroup} の人類史における考古遺伝学的旅路をたどります。",
            "ko": "이 보고서는 당신의 하플로그룹 {haplogroup}의 인류 역사 속 고고유전학적 여정을 추적합니다。",
            "ar": "يتتبع هذا التقرير الرحلة الأثرية الجينية لسلالتك {haplogroup} عبر تاريخ البشرية.",
            "he": "דוח זה עוקב אחר המסע הארכיאוגנטי של קבוצת ההפלוגרופ שלך {haplogroup} לאורך ההיסטוריה האנושית.",
            "hi": "यह रिपोर्ट आपके हैप्लोग्रुप {haplogroup} की मानव इतिहास में पुरातात्विक-आनुवंशिक यात्रा का अनुसरण करती है।",
            "bn": "এই প্রতিবেদনটি মানব ইতিহাসে আপনার হ্যাপলোগ্রুপ {haplogroup} এর আর্কিওজেনেটিক যাত্রা অনুসরণ করে।",
            "tr": "Bu rapor, haplogrubunuz {haplogroup}’un insanlık tarihindeki arkeogenetik yolculuğunu izler.",
            "fa": "این گزارش مسیر باستان‌ژنتیکی هاپلوگروه شما {haplogroup} را در تاریخ بشر دنبال می‌کند.",
            "ur": "یہ رپورٹ انسانی تاریخ میں آپ کے ہاپلوگروپ {haplogroup} کے آثارِ قدیمہ و جینیاتی سفر کو بیان کرتی ہے۔",
            "sw": "Ripoti hii inafuatilia safari ya kijenetiki ya kikundi chako cha {haplogroup} katika historia ya binadamu.",
            "am": "ይህ ሪፖርት የእርስዎን ሃፕሎግሩፕ {haplogroup} በሰው ታሪክ ውስጥ የአርኬዮጄኔቲክ ጉዞ ይከታተላል።",
            "yo": "Iroyin yii n tọpa irin-ajo arkeogenetic ti haplogroup rẹ {haplogroup} ninu itan eniyan.",
            "zu": "Lo mbiko ulandela uhambo lwezofuzo lomlando weqembu lakho le-{haplogroup}.",
            "id": "Laporan ini menelusuri perjalanan arkeogenetik haplogroup Anda {haplogroup} dalam sejarah manusia.",
            "ms": "Laporan ini menjejaki perjalanan arkeogenetik haplogroup anda {haplogroup} dalam sejarah manusia.",
            "th": "รายงานนี้ติดตามการเดินทางทางโบราณพันธุกรรมของแฮ็ปโลกรุ๊ป {haplogroup} ในประวัติศาสตร์มนุษย์",
            "vi": "Báo cáo này theo dõi hành trình khảo cổ di truyền của haplogroup {haplogroup} trong lịch sử loài người.",
            "tl": "Sinusubaybayan ng ulat na ito ang arkeohenetikong paglalakbay ng iyong haplogroup {haplogroup} sa kasaysayan ng tao.",
            "pl": "Raport ten śledzi archeogenetyczną podróż Twojej haplogrupy {haplogroup} w historii ludzkości.",
            "cs": "Tato zpráva sleduje archeogenetickou cestu vaší haploskupiny {haplogroup} dějinami lidstva.",
            "sk": "Táto správa sleduje archeogenetickú cestu vašej haploskupiny {haplogroup} dejinami ľudstva.",
            "hu": "Ez a jelentés nyomon követi a {haplogroup} haplocsoport archeogenetikai útját az emberiség történetében.",
            "ro": "Acest raport urmărește călătoria arheogenetică a haplogrupului tău {haplogroup} în istoria omenirii.",
            "bg": "Този доклад проследява археогенетичното пътешествие на вашата хаплогрупа {haplogroup} в човешката история.",
            "el": "Αυτή η αναφορά παρακολουθεί την αρχαιογονιδιακή πορεία της απλοομάδας σας {haplogroup} στην ανθρώπινη ιστορία.",
            "nl": "Dit rapport volgt de archeogenetische reis van uw haplogroep {haplogroup} door de menselijke geschiedenis.",
            "da": "Denne rapport følger den arkæogenetiske rejse for din haplogruppe {haplogroup} gennem menneskets historie.",
            "no": "Denne rapporten følger den arkeogenetiske reisen til din haplogruppe {haplogroup} gjennom menneskets historie.",
            "et": "See raport jälgib teie haplogrupi {haplogroup} arheogeneetilist teekonda inimkonna ajaloos.",
            "lv": "Šis ziņojums seko jūsu haplogrupas {haplogroup} arheogenētiskajam ceļojumam cilvēces vēsturē.",
            "lt": "Ši ataskaita seka jūsų haplogrupės {haplogroup} archeogenetinę kelionę žmonijos istorijoje.",
            "is": "Þessi skýrsla rekur arkeógenetíska ferð haplóhóps þíns {haplogroup} í gegnum mannkynssöguna.",
            "ga": "Leanann an tuarascáil seo turas ársa-ghéiniteach do haploghrúpa {haplogroup} trí stair an chine dhaonna.",
            "sr": "Овај извештај прати археогенетско путовање ваше хаплогрупе {haplogroup} кроз историју човечанства.",
            "hr": "Ovo izvješće prati arheogenetsko putovanje vaše haplogrupe {haplogroup} kroz ljudsku povijest.",
            "sl": "To poročilo sledi arheogenetskemu potovanju vaše haploskupine {haplogroup} skozi zgodovino človeštva.",
            "uk": "Цей звіт простежує археогенетичну подорож вашої гаплогрупи {haplogroup} в історії людства.",
            "ka": "ეს ანგარიში აკვირდება თქვენი ჰაპლოგრუპის {haplogroup} არქეოგენეტიკურ მოგზაურობას კაცობრიობის ისტორიაში.",
            "hy": "Այս զեկույցը հետևում է ձեր հապլոգրուպ {haplogroup} արխեոգենետիկական ճանապարհին մարդկության պատմության մեջ։",
            "mn": "Энэхүү тайлан нь таны {haplogroup} хаплогруппийн археогенетик аяллыг хүн төрөлхтний түүхэнд мөрдөнө.",
            "kk": "Бұл есеп сіздің {haplogroup} гаплогруппаның адамзат тарихындағы археогенетикалық жолын қадағалайды.",
            "uz": "Ushbu hisobot sizning {haplogroup} haplogruppingizning insoniyat tarixidagi arkeogenetik safarini kuzatadi.",
            "ta": "இந்த அறிக்கை உங்கள் ஹாப்லோகுழு {haplogroup} மனித வரலாற்றில் மேற்கொண்ட தொல்லியல் மரபணு பயணத்தைப் பின்தொடர்கிறது.",
            "te": "ఈ నివేదిక మీ హాప్లోగ్రూప్ {haplogroup} యొక్క మానవ చరిత్రలో పురావస్తు-జన్యు ప్రయాణాన్ని అనుసరిస్తుంది.",
            "kn": "ಈ ವರದಿ ನಿಮ್ಮ ಹ್ಯಾಪ್ಲೋಗ್ರೂಪ್ {haplogroup} ಮಾನವ ಇತಿಹಾಸದಲ್ಲಿ ನಡೆಸಿದ ಪುರಾತನ-ಜನ್ಯ ಪ್ರಯಾಣವನ್ನು ಅನುಸರಿಸುತ್ತದೆ.",
            "ml": "ഈ റിപ്പോർട്ട് നിങ്ങളുടെ ഹാപ്ലോഗ്രൂപ്പ് {haplogroup} മനുഷ്യചരിത്രത്തിലൂടെ നടത്തിയ പുരാതന-ജന്യ യാത്രയെ പിന്തുടരുന്നു.",
            "ne": "यो प्रतिवेदनले मानव इतिहासमा तपाईंको ह्याप्लोग्रुप {haplogroup} को पुरातात्त्विक-आनुवंशिक यात्रालाई पछ्याउँछ।",
            "si": "මෙම වාර්තාව ඔබගේ හැප්ලොගෘප් {haplogroup} මිනිස් ඉතිහාසය තුළ සිදු කළ පුරාවිද්‍යාත්මක-ජීව විද්‍යාත්මක ගමන අනుసరిస్తుంది.",
            "my": "ဤအစီရင်ခံစာသည် လူ့သမိုင်းအတွင်း သင့်၏ ဟပ်ပလိုဂရုပ် {haplogroup} ၏ အာခီယိုဂျင်နက်တစ်ခရီးကို ခြေရာခံပါသည်။",
            "km": "របាយការណ៍នេះតាមដានដំណើរអាក្សរពន្ធុវិទ្យារបស់ហាប់ឡូក្រុម {haplogroup} របស់អ្នកក្នុងប្រវត្តិសាស្ត្រមនុស្ស។",
            "lo": "ລາຍງານນີ້ຕິດຕາມການເດີນທາງທາງພັນທຸກຳບູຮານຂອງຮາບໂລກຣຸບ {haplogroup} ຂອງທ່ານໃນປະຫວັດສາດມະນຸດ.",
            "haw": "Hahai kēia hōʻike i ka huakaʻi arkeogenetic o kou haplogroup {haplogroup} ma ka moʻokūʻauhau kanaka.",
            "mi": "Ka whai tēnei pūrongo i te haerenga arkeogenetic o tō haplogroup {haplogroup} i roto i te hītori o te tangata.",
            "sm": "O lenei lipoti e tulituliloa le malaga arkeogenetic o lau haplogroup {haplogroup} i le talafaasolopito o tagata.",
            "es-mx": "Este informe sigue el recorrido arqueogenético de tu haplogrupo {haplogroup} a lo largo de la historia humana.",
            "pt-br": "Este relatório acompanha a jornada arqueogenética do seu haplogrupo {haplogroup} ao longo da história humana."
        },

        "sources_footer": {
            "fi": (
                "Tämä tarina perustuu lukuisiin arkeologisiin ja geneettisiin lähteisiin, kuten {sources}. "
                "Raakadatat ovat peräisin palveluista {providers}, ja käytetyt tutkimustyökalut sisältävät {tools}. "
                "Luotettavuusluokitus: {reliability}/100."
            ),
            "en": (
                "This journey is based on numerous archaeological and genetic sources, such as {sources}. "
                "Raw data originates from {providers}, and the research tools used include {tools}. "
                "Reliability score: {reliability}/100."
            ),
            "sv": (
                "Denna resa bygger på många arkeologiska och genetiska källor, såsom {sources}. "
                "Rådata kommer från {providers}, och använda forskningsverktyg inkluderar {tools}. "
                "Tillförlitlighetsbetyg: {reliability}/100."
            ),
            "de": (
                "Diese Reise basiert auf zahlreichen archäologischen und genetischen Quellen wie {sources}. "
                "Rohdaten stammen von {providers}, und verwendete Forschungstools umfassen {tools}. "
                "Zuverlässigkeitsbewertung: {reliability}/100."
            ),
            "fr": (
                "Ce parcours repose sur de nombreuses sources archéologiques et génétiques, telles que {sources}. "
                "Les données brutes proviennent de {providers}, et les outils de recherche utilisés incluent {tools}. "
                "Indice de fiabilité : {reliability}/100."
            ),
            "es": (
                "Este recorrido se basa en numerosas fuentes arqueológicas y genéticas, como {sources}. "
                "Los datos brutos provienen de {providers}, y las herramientas de investigación utilizadas incluyen {tools}. "
                "Calificación de fiabilidad: {reliability}/100."
            ),
            "pt": (
                "Esta jornada baseia-se em numerosas fontes arqueológicas e genéticas, como {sources}. "
                "Os dados brutos provêm de {providers}, e as ferramentas de pesquisa utilizadas incluem {tools}. "
                "Classificação de confiabilidade: {reliability}/100."
            ),
            "it": (
                "Questa avventura si basa su numerose fonti archeologiche e genetiche, come {sources}. "
                "I dati grezzi provengono da {providers}, e gli strumenti di ricerca utilizzati includono {tools}. "
                "Valutazione dell'affidabilità: {reliability}/100."
            ),
            "ru": (
                "Это приключение основано на многочисленных археологических и генетических источниках, таких как {sources}. "
                "Исходные данные поступают от {providers}, а используемые исследовательские инструменты включают {tools}. "
                "Оценка надежности: {reliability}/100."
            ),
            "zh": (
                "这场探险基于众多考古和遗传学来源，如 {sources}。"
                "原始数据来自 {providers}，使用的研究工具包括 {tools}。"
                "可靠性评级：{reliability}/100。"
            ),
            "ja": (
                "この冒険は、{sources} などの多数の考古学的および遺伝学的情報源に基づいています。"
                "生データは {providers} から提供され、使用された研究ツールには {tools} が含まれます。"
                "信頼性評価：{reliability}/100。"
            ),
            "ko": (
                "이 모험은 {sources}와 같은 수많은 고고학 및 유전학적 출처를 기반으로 합니다. "
                "원시 데이터는 {providers}에서 제공되었으며, 사용된 연구 도구에는 {tools}가 포함됩니다. "
                "신뢰도 등급: {reliability}/100."
            ),
            "ar": (
                "تستند هذه المغامرة إلى العديد من المصادر الأثرية والجينية، مثل {sources}. "
                "تأتي البيانات الخام من {providers}، وتشمل أدوات البحث المستخدمة {tools}. "
                "تصنيف الموثوقية: {reliability}/100."
            ),
            "he": (
                "הרפתקה זו מבוססת על מקורות ארכאולוגיים וגנטיים רבים, כגון {sources}. "
                "הנתונים הגולמיים מגיעים מ-{providers}, וכלי המחקר שבהם נעשה שימוש כוללים את {tools}. "
                "דירוג אמינות: {reliability}/100."
            ),
            "hi": (
                "यह यात्रा {sources} जैसे अनेक पुरातात्त्विक और आनुवंशिक स्रोतों पर आधारित है। "
                "कच्चा डेटा {providers} से प्राप्त होता है, और उपयोग किए गए अनुसंधान उपकरणों में {tools} शामिल हैं। "
                "विश्वसनीयता स्कोर: {reliability}/100."
            ),
            "bn": (
                "এই যাত্রাটি {sources} সহ বহু প্রত্নতাত্ত্বিক ও জেনেটিক উৎসের উপর ভিত্তি করে তৈরি। "
                "কাঁচা তথ্য এসেছে {providers} থেকে, এবং ব্যবহৃত গবেষণা সরঞ্জামগুলির মধ্যে রয়েছে {tools}। "
                "বিশ্বাসযোগ্যতার স্কোর: {reliability}/100."
            ),
            "tr": (
                "Bu yolculuk, {sources} gibi çok sayıda arkeolojik ve genetik kaynağa dayanmaktadır. "
                "Ham veriler {providers} kaynaklıdır ve kullanılan araştırma araçları arasında {tools} bulunmaktadır. "
                "Güvenilirlik puanı: {reliability}/100."
            ),
            "fa": (
                "این سفر بر پایه منابع متعدد باستان‌شناسی و ژنتیکی مانند {sources} استوار است. "
                "داده‌های خام از {providers} تأمین شده و ابزارهای پژوهشی استفاده‌شده شامل {tools} هستند. "
                "امتیاز اعتبار: {reliability}/100."
            ),
            "ur": (
                "یہ سفر {sources} جیسے متعدد آثارِ قدیمہ اور جینیاتی ذرائع پر مبنی ہے۔ "
                "خام ڈیٹا {providers} سے حاصل ہوا ہے، اور استعمال شدہ تحقیقی آلات میں {tools} شامل ہیں۔ "
                "اعتماد کی درجہ بندی: {reliability}/100."
            ),
            "sw": (
                "Safari hii inategemea vyanzo vingi vya akiolojia na kijeni, kama vile {sources}. "
                "Data ghafi hutoka kwa {providers}, na zana za utafiti zilizotumika ni pamoja na {tools}. "
                "Kiwango cha uaminifu: {reliability}/100."
            ),
            "am": (
                "ይህ ጉዞ {sources} ያሉ ብዙ የአርኬዮሎጂ እና የጄኔቲክ ምንጮችን መሰረት ያደርጋል። "
                "የሚጠቀሙት የመረጃ ምንጮች {providers} ናቸው፣ እና የተጠቀሱት የምርምር መሳሪያዎች {tools} ናቸው። "
                "የታመነነት ደረጃ: {reliability}/100."
            ),
            "yo": (
                "Ìrìnàjò yìí dá lórí ọ̀pọ̀ orísun arkeoloji àti jiini gẹ́gẹ́ bí {sources}. "
                "Àwọn data àkọ́kọ́ wa láti {providers}, àti àwọn irinṣẹ́ ìwádìí tí a lo ni {tools}. "
                "Ìdíyelé ìgbàgbọ́: {reliability}/100."
            ),
            "zu": (
                "Lolu hambo lusekelwe emithonjeni eminingi yezinto zakudala nezofuzo, njengokuthi {sources}. "
                "Idatha eluhlaza ivela ku {providers}, kanti amathuluzi ocwaningo asetshenzisiwe afaka {tools}. "
                "Isilinganiso sokuthembeka: {reliability}/100."
            ),
            "id": (
                "Perjalanan ini didasarkan pada berbagai sumber arkeologi dan genetik, seperti {sources}. "
                "Data mentah berasal dari {providers}, dan alat penelitian yang digunakan mencakup {tools}. "
                "Skor keandalan: {reliability}/100."
            ),
            "ms": (
                "Perjalanan ini berasaskan pelbagai sumber arkeologi dan genetik, seperti {sources}. "
                "Data mentah berasal dari {providers}, dan alat penyelidikan yang digunakan termasuk {tools}. "
                "Skor kebolehpercayaan: {reliability}/100."
            ),
            "th": (
                "การเดินทางนี้อ้างอิงจากแหล่งข้อมูลทางโบราณคดีและพันธุกรรมจำนวนมาก เช่น {sources} "
                "ข้อมูลดิบมาจาก {providers} และเครื่องมือวิจัยที่ใช้รวมถึง {tools} "
                "คะแนนความน่าเชื่อถือ: {reliability}/100"
            ),
            "vi": (
                "Hành trình này dựa trên nhiều nguồn khảo cổ và di truyền học như {sources}. "
                "Dữ liệu thô đến từ {providers}, và các công cụ nghiên cứu được sử dụng bao gồm {tools}. "
                "Điểm độ tin cậy: {reliability}/100."
            ),
            "tl": (
                "Ang paglalakbay na ito ay batay sa maraming mapagkukunang arkeolohikal at henetiko tulad ng {sources}. "
                "Ang hilaw na datos ay nagmula sa {providers}, at ang mga ginamit na kasangkapan sa pananaliksik ay kinabibilangan ng {tools}. "
                "Antas ng pagiging mapagkakatiwalaan: {reliability}/100."
            ),
            "pl": (
                "Ta podróż opiera się na licznych źródłach archeologicznych i genetycznych, takich jak {sources}. "
                "Dane surowe pochodzą z {providers}, a użyte narzędzia badawcze obejmują {tools}. "
                "Ocena wiarygodności: {reliability}/100."
            ),
            "cs": (
                "Tato cesta vychází z mnoha archeologických a genetických zdrojů, jako jsou {sources}. "
                "Surová data pocházejí z {providers} a použité výzkumné nástroje zahrnují {tools}. "
                "Hodnocení spolehlivosti: {reliability}/100."
            ),
            "sk": (
                "Táto cesta vychádza z mnohých archeologických a genetických zdrojov, ako sú {sources}. "
                "Surové údaje pochádzajú z {providers} a použité výskumné nástroje zahŕňajú {tools}. "
                "Hodnotenie spoľahlivosti: {reliability}/100."
            ),
            "hu": (
                "Ez az utazás számos régészeti és genetikai forráson alapul, mint például {sources}. "
                "A nyers adatok a {providers} forrásaiból származnak, és a használt kutatási eszközök közé tartozik {tools}. "
                "Megbízhatósági értékelés: {reliability}/100."
            ),
            "ro": (
                "Această călătorie se bazează pe numeroase surse arheologice și genetice, precum {sources}. "
                "Datele brute provin de la {providers}, iar instrumentele de cercetare utilizate includ {tools}. "
                "Scor de fiabilitate: {reliability}/100."
            ),
            "bg": (
                "Това пътешествие се основава на множество археологически и генетични източници, като {sources}. "
                "Суровите данни идват от {providers}, а използваните изследователски инструменти включват {tools}. "
                "Оценка на надеждност: {reliability}/100."
            ),
            "el": (
                "Αυτό το ταξίδι βασίζεται σε πολλές αρχαιολογικές και γενετικές πηγές, όπως {sources}. "
                "Τα ακατέργαστα δεδομένα προέρχονται από {providers}, και τα εργαλεία έρευνας που χρησιμοποιήθηκαν περιλαμβάνουν {tools}. "
                "Βαθμολογία αξιοπιστίας: {reliability}/100."
            ),
            "nl": (
                "Deze reis is gebaseerd op talrijke archeologische en genetische bronnen, zoals {sources}. "
                "Ruwe gegevens zijn afkomstig van {providers}, en de gebruikte onderzoekstools omvatten {tools}. "
                "Betrouwbaarheidsscore: {reliability}/100."
            ),
            "da": (
                "Denne rejse er baseret på mange arkæologiske og genetiske kilder, såsom {sources}. "
                "Rådata stammer fra {providers}, og anvendte forskningsværktøjer inkluderer {tools}. "
                "Pålidelighedsvurdering: {reliability}/100."
            ),
            "no": (
                "Denne reisen er basert på mange arkeologiske og genetiske kilder, som {sources}. "
                "Rådata kommer fra {providers}, og brukte forskningsverktøy inkluderer {tools}. "
                "Pålitelighetsvurdering: {reliability}/100."
            ),
            "et": (
                "See teekond põhineb paljudel arheoloogilistel ja geneetilistel allikatel, nagu {sources}. "
                "Toorandmed pärinevad {providers} ning kasutatud uurimisvahendid hõlmavad {tools}. "
                "Usaldusväärsuse hinne: {reliability}/100."
            ),
            "lv": (
                "Šis ceļojums balstās uz daudziem arheoloģiskiem un ģenētiskiem avotiem, piemēram, {sources}. "
                "Neapstrādātie dati nāk no {providers}, un izmantotie pētniecības rīki ietver {tools}. "
                "Uzticamības vērtējums: {reliability}/100."
            ),
            "lt": (
                "Ši kelionė remiasi daugybe archeologinių ir genetinių šaltinių, tokių kaip {sources}. "
                "Neapdoroti duomenys gaunami iš {providers}, o naudojami tyrimų įrankiai apima {tools}. "
                "Patikimumo įvertinimas: {reliability}/100."
            ),
            "is": (
                "Þessi ferð byggir á fjölmörgum fornleifafræðilegum og erfðafræðilegum heimildum, svo sem {sources}. "
                "Hrá gögn koma frá {providers}, og notuð rannsóknartæki fela í sér {tools}. "
                "Áreiðanleikamat: {reliability}/100."
            ),
            "ga": (
                "Tá an turas seo bunaithe ar go leor foinsí seandálaíochta agus géiniteacha, amhail {sources}. "
                "Tagann na sonraí amh ó {providers}, agus áirítear ar na huirlisí taighde a úsáideadh {tools}. "
                "Scór iontaofachta: {reliability}/100."
            ),
            "sr": (
                "Ово путовање заснива се на бројним археолошким и генетским изворима, као што су {sources}. "
                "Сирови подаци потичу од {providers}, а коришћени истраживачки алати укључују {tools}. "
                "Оцена поузданости: {reliability}/100."
            ),
            "hr": (
                "Ovo putovanje temelji se na brojnim arheološkim i genetskim izvorima, poput {sources}. "
                "Sirovi podaci dolaze iz {providers}, a korišteni istraživački alati uključuju {tools}. "
                "Ocjena pouzdanosti: {reliability}/100."
            ),
            "sl": (
                "To potovanje temelji na številnih arheoloških in genetskih virih, kot so {sources}. "
                "Surovi podatki izvirajo iz {providers}, uporabljena raziskovalna orodja pa vključujejo {tools}. "
                "Ocena zanesljivosti: {reliability}/100."
            ),
            "uk": (
                "Ця подорож базується на численних археологічних та генетичних джерелах, таких як {sources}. "
                "Сирі дані надходять з {providers}, а використані дослідницькі інструменти включають {tools}. "
                "Оцінка надійності: {reliability}/100."
            ),
            "ka": (
                "ეს მოგზაურობა ეფუძნება მრავალ არქეოლოგიურ და გენეტიკურ წყაროს, როგორიცაა {sources}. "
                "ნედლი მონაცემები მოდის {providers}-დან, ხოლო გამოყენებული კვლევითი ინსტრუმენტები მოიცავს {tools}. "
                "სანდოობის შეფასება: {reliability}/100."
            ),
            "hy": (
                "Այս ճանապարհորդությունը հիմնված է բազմաթիվ հնագիտական և գենետիկական աղբյուրների վրա, ինչպիսիք են {sources}։ "
                "Հում տվյալները ստացվում են {providers}-ից, իսկ օգտագործված հետազոտական գործիքները ներառում են {tools}։ "
                "Վստահելիության գնահատում՝ {reliability}/100։"
            ),
            "mn": (
                "Энэхүү аялал нь {sources} зэрэг олон археологийн болон генетикийн эх сурвалжид тулгуурладаг. "
                "Түүхий өгөгдөл нь {providers}-оос ирсэн бөгөөд ашигласан судалгааны хэрэгслүүдэд {tools} орно. "
                "Найдвартай байдлын үнэлгээ: {reliability}/100."
            ),
            "kk": (
                "Бұл сапар {sources} сияқты көптеген археологиялық және генетикалық дереккөздерге негізделген. "
                "Шикі деректер {providers}-тен алынған, ал қолданылған зерттеу құралдарына {tools} кіреді. "
                "Сенімділік бағасы: {reliability}/100."
            ),
            "uz": (
                "Ushbu sayohat {sources} kabi ko‘plab arxeologik va genetik manbalarga asoslanadi. "
                "Xom ma’lumotlar {providers}-dan olinadi va ishlatilgan tadqiqot vositalariga {tools} kiradi. "
                "Ishonchlilik bahosi: {reliability}/100."
            ),
            "ta": (
                "இந்தப் பயணம் {sources} போன்ற பல தொல்லியல் மற்றும் மரபணு ஆதாரங்களை அடிப்படையாகக் கொண்டது. "
                "மூலத் தரவுகள் {providers} இலிருந்து பெறப்பட்டவை, பயன்படுத்தப்பட்ட ஆராய்ச்சி கருவிகளில் {tools} அடங்கும். "
                "நம்பகத்தன்மை மதிப்பெண்: {reliability}/100."
            ),
            "te": (
                "ఈ ప్రయాణం {sources} వంటి అనేక పురావస్తు మరియు జన్యు మూలాలపై ఆధారపడి ఉంది. "
                "మూల డేటా {providers} నుండి వస్తుంది, మరియు ఉపయోగించిన పరిశోధనా సాధనాలలో {tools} ఉన్నాయి. "
                "నమ్మకత రేటింగ్: {reliability}/100."
            ),
            "kn": (
                "ಈ ಪ್ರಯಾಣವು {sources} ಎಂಬ ಅನೇಕ ಪುರಾತತ್ವ ಮತ್ತು ಜನ್ಯ ಮೂಲಗಳ ಮೇಲೆ ಆಧಾರಿತವಾಗಿದೆ. "
                "ಕಚ್ಚಾ ದತ್ತಾಂಶ {providers} ನಿಂದ ಬರುತ್ತದೆ, ಮತ್ತು ಬಳಸಲಾದ ಸಂಶೋಧನಾ ಸಾಧನಗಳಲ್ಲಿ {tools} ಸೇರಿವೆ. "
                "ವಿಶ್ವಾಸಾರ್ಹತೆ ಅಂಕ: {reliability}/100."
            ),
            "ml": (
                "ഈ യാത്ര {sources} പോലുള്ള നിരവധി പുരാവസ്തു-ജന്യ ഉറവിടങ്ങളെ അടിസ്ഥാനമാക്കിയുള്ളതാണ്. "
                "മൂല ഡാറ്റ {providers}യിൽ നിന്നാണ് ലഭിക്കുന്നത്, ഉപയോഗിച്ച ഗവേഷണ ഉപകരണങ്ങളിൽ {tools} ഉൾപ്പെടുന്നു. "
                "വിശ്വാസ്യത സ്കോർ: {reliability}/100."
            ),
            "ne": (
                "यो यात्रा {sources} जस्ता धेरै पुरातात्त्विक र आनुवंशिक स्रोतहरूमा आधारित छ। "
                "कच्चा डेटा {providers} बाट आएको हो, र प्रयोग गरिएका अनुसन्धान उपकरणहरूमा {tools} समावेश छन्। "
                "विश्वसनीयता स्कोर: {reliability}/100."
            ),
            "si": (
                "මෙම ගමන {sources} වැනි බොහෝ පුරාවිද්‍යාත්මක සහ ජීව විද්‍යාත්මක මූලාශ්‍ර මත පදනම් වේ. "
                "අමු දත්ත {providers} වෙතින් ලැබී 있으며, භාවිතා කරන ලද පර්යේෂණ උපකරණවලට {tools} ඇතුළත් වේ. "
                "විශ්වාසනීයතා ලකුණු: {reliability}/100."
            ),
            "my": (
                "ဤခရီးသည် {sources} ကဲ့သို့သော အများအပြားသော ရှေးဟောင်းနှင့် မျိုးဗီဇဆိုင်ရာ အရင်းအမြစ်များအပေါ် အခြေခံထားပါသည်။ "
                "မူရင်းဒေတာသည် {providers} မှ ရရှိလာပြီး အသုံးပြုထားသော သုတေသနကိရိယာများတွင် {tools} ပါဝင်ပါသည်။ "
                "ယုံကြည်မှုအဆင့်: {reliability}/100."
            ),
            "km": (
                "ដំណើរនេះផ្អែកលើប្រភពបុរាណវិទ្យា និងហ្សែនជាច្រើនដូចជា {sources}។ "
                "ទិន្នន័យដើមមកពី {providers} ហើយឧបករណ៍ស្រាវជ្រាវដែលបានប្រើរួមមាន {tools}។ "
                "ពិន្ទុភាពទុកចិត្ត: {reliability}/100."
            ),
            "lo": (
                "ການເດີນທາງນີ້ອີງຕາມແຫຼ່ງຂໍ້ມູນທາງບູຮານຄະດີແລະພັນທຸກຳຫຼາຍແຫຼ່ງ ເຊັ່ນ {sources}. "
                "ຂໍ້ມູນດິບມາຈາກ {providers} ແລະເຄື່ອງມືການຄົ້ນຄວ້າທີ່ໃຊ້ຮວມມີ {tools}. "
                "ຄະແນນຄວາມໜ້າເຊື່ອຖື: {reliability}/100."
            ),
            "haw": (
                "Ua hoʻokumu ʻia kēia huakaʻi ma luna o nā kumu ʻike archaeological a genetic he nui, e like me {sources}. "
                "Mai nā {providers} nā ʻike kumu, a pili pū nā mea hana noiʻi i hoʻohana ʻia i ka {tools}. "
                "Kikoʻī hilinaʻi: {reliability}/100."
            ),
            "mi": (
                "E hāngai ana tēnei haerenga ki ngā pūtake whaipara tangata me ngā pūtake ira maha, pērā i a {sources}. "
                "Nō {providers} ngā raraunga taketake, ā, ko ngā taputapu rangahau i whakamahia ko {tools}. "
                "Tatauranga whakawhirinaki: {reliability}/100."
            ),
            "sm": (
                "O lenei malaga e fa'avae i luga o le tele o punaoa o suʻesuʻega o toega ma le genetika, e pei o {sources}. "
                "O fa'amaumauga mata'utia e maua mai i {providers}, ma o meafaigaluega su'esu'e na fa'aaogaina e aofia ai {tools}. "
                "Fuainumera fa'atuatuaina: {reliability}/100."
            ),
            "es-mx": (
                "Este recorrido se basa en numerosas fuentes arqueológicas y genéticas, como {sources}. "
                "Los datos brutos provienen de {providers}, y las herramientas de investigación utilizadas incluyen {tools}. "
                "Calificación de fiabilidad: {reliability}/100."
            ),
            "pt-br": (
                "Esta jornada baseia-se em numerosas fontes arqueológicas e genéticas, como {sources}. "
                "Os dados brutos provêm de {providers}, e as ferramentas de pesquisa utilizadas incluem {tools}. "
                "Classificação de confiabilidade: {reliability}/100."
            )
        }
    }


def get_text(key: str, lang: Optional[str] = None, **kwargs) -> str:
    """
    Palauttaa käännöksen annetulle avaimelle ja kielelle.
    """
    templates = get_translation_templates()
    lang = lang or get_default_language()
    if key not in templates:
        raise KeyError(f"Translation key not found: {key}")

    translations = templates[key]
    template = translations.get(lang) or translations.get(get_default_language())

    try:
        return template.format(**kwargs)
    except KeyError as e:
        raise KeyError(f"Missing format argument {e} for key '{key}' in language '{lang}'")


def format_sources_list(sources: List[str], lang: Optional[str] = None) -> str:
    """
    Muotoilee lähdeluettelon kieli- ja kulttuurisensitiivisesti.
    """
    lang = lang or get_default_language()
    if not sources:
        return ""

    if lang in ["fi", "sv", "de", "nl"]:
        return ", ".join(sources)
    elif lang in ["en", "fr", "es", "pt", "it"]:
        return ", ".join(sources)
    elif lang in ["zh", "ja", "ko"]:
        return "、".join(sources)
    elif lang in ["ar", "he"]:
        return "، ".join(sources)
    else:
        return ", ".join(sources)
