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
    return {
        "intro": {
            "fi": "Tämä raportti kertoo haploryhmäsi {haplogroup} arkeogeneettisen matkan läpi ihmiskunnan historian.",
            "en": "This report traces the archaeogenetic journey of your haplogroup {haplogroup} through human history.",
            "sv": "Denna rapport följer din haplogrupp {haplogroup} genom mänsklighetens arkeogenetiska historia.",
            "de": "Dieser Bericht verfolgt die archäogenetische Reise Ihrer Haplogruppe {haplogroup} durch die Menschheitsgeschichte.",
            "fr": "Ce rapport retrace le parcours archéogénétique de votre haplogroupe {haplogroup} à travers l'histoire humaine.",
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
            "tr": "Bu rapor, haplogrubunuz {haplogroup}'un insanlık tarihindeki arkeogenetik yolculuğunu izler.",
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
            "si": "මෙම වාර්තාව ඔබගේ හැප්ලොගෘප් {haplogroup} මිනිස් ඉතිහාසය තුළ සිදු කළ පුරාවිද්‍යාත්මක-ජීව විද්‍යාත්මක ගමන අනුගමනය කරයි.",
            "my": "ဤအစီရင်ခံစာသည် လူ့သမိုင်းအတွင်း သင့်၏ ဟပ်ပလိုဂရုပ် {haplogroup} ၏ အာခီယိုဂျင်နက်တစ်ခရီးကို ခြေရာခံပါသည်။",
            "km": "របាយការណ៍នេះតាមដានដំណើរអាក្សរពន្ធុវិទ្យារបស់ហាប់ឡូក្រុម {haplogroup} របស់អ្នកក្នុងប្រវត្តិសាស្ត្រមនុស្ស។",
            "lo": "ລາຍງານນີ້ຕິດຕາມການເດີນທາງທາງພັນທຸກຳບູຮານຂອງຮາບໂລກຣຸບ {haplogroup} ຂອງທ່ານໃນປະຫວັດສາດມະນຸດ.",
            "haw": "Hahai kēia hōʻike i ka huakaʻi arkeogenetic o kou haplogroup {haplogroup} ma ka moʻokūʻauhau kanaka.",
            "mi": "Ka whai tēnei pūrongo i te haerenga arkeogenetic o tō haplogroup {haplogroup} i roto i te hītori o te tangata.",
            "sm": "O lenei lipoti e tulituliloa le malaga arkeogenetic o lau haplogroup {haplogroup} i le talafaasolopito o tagata.",
            "es-mx": "Este informe sigue el recorrido arqueogenético de tu haplogrupo {haplogroup} a lo largo de la historia humana.",
            "pt-br": "Este relatório acompanha a jornada arqueogenética do seu haplogrupo {haplogroup} ao longo da história humana.",
        },
        "sources_footer": {
            "fi": ("Tämä tarina perustuu lukuisiin arkeologisiin ja geneettisiin lähteisiin, kuten {sources}. "
                   "Raakadatat ovat peräisin palveluista {providers}, ja käytetyt tutkimustyökalut sisältävät {tools}. "
                   "Luotettavuusluokitus: {reliability}/100."),
            "en": ("This journey is based on numerous archaeological and genetic sources, such as {sources}. "
                   "Raw data originates from {providers}, and the research tools used include {tools}. "
                   "Reliability score: {reliability}/100."),
            "sv": ("Denna resa bygger på många arkeologiska och genetiska källor, såsom {sources}. "
                   "Rådata kommer från {providers}, och använda forskningsverktyg inkluderar {tools}. "
                   "Tillförlitlighetsbetyg: {reliability}/100."),
            "de": ("Diese Reise basiert auf zahlreichen archäologischen und genetischen Quellen wie {sources}. "
                   "Rohdaten stammen von {providers}, und verwendete Forschungstools umfassen {tools}. "
                   "Zuverlässigkeitsbewertung: {reliability}/100."),
            "fr": ("Ce parcours repose sur de nombreuses sources archéologiques et génétiques, telles que {sources}. "
                   "Les données brutes proviennent de {providers}, et les outils de recherche utilisés incluent {tools}. "
                   "Indice de fiabilité : {reliability}/100."),
            "es": ("Este recorrido se basa en numerosas fuentes arqueológicas y genéticas, como {sources}. "
                   "Los datos brutos provienen de {providers}, y las herramientas de investigación utilizadas incluyen {tools}. "
                   "Calificación de fiabilidad: {reliability}/100."),
            "pt": ("Esta jornada baseia-se em numerosas fontes arqueológicas e genéticas, como {sources}. "
                   "Os dados brutos provêm de {providers}, e as ferramentas de pesquisa utilizadas incluem {tools}. "
                   "Classificação de confiabilidade: {reliability}/100."),
            "it": ("Questa avventura si basa su numerose fonti archeologiche e genetiche, come {sources}. "
                   "I dati grezzi provengono da {providers}, e gli strumenti di ricerca utilizzati includono {tools}. "
                   "Valutazione dell'affidabilità: {reliability}/100."),
            "ru": ("Это приключение основано на многочисленных археологических и генетических источниках, таких как {sources}. "
                   "Исходные данные поступают от {providers}, а используемые исследовательские инструменты включают {tools}. "
                   "Оценка надежности: {reliability}/100."),
            "zh": ("这场探险基于众多考古和遗传学来源，如 {sources}。原始数据来自 {providers}，使用的研究工具包括 {tools}。可靠性评级：{reliability}/100。"),
            "ja": ("この冒険は、{sources} などの多数の考古学的および遺伝学的情報源に基づいています。"
                   "生データは {providers} から提供され、使用された研究ツールには {tools} が含まれます。信頼性評価：{reliability}/100。"),
            "ko": ("이 모험은 {sources}와 같은 수많은 고고학 및 유전학적 출처를 기반으로 합니다. "
                   "원시 데이터는 {providers}에서 제공되었으며, 사용된 연구 도구에는 {tools}가 포함됩니다. 신뢰도 등급: {reliability}/100."),
            "ar": ("تستند هذه المغامرة إلى العديد من المصادر الأثرية والجينية، مثل {sources}. "
                   "تأتي البيانات الخام من {providers}، وتشمل أدوات البحث المستخدمة {tools}. تصنيف الموثوقية: {reliability}/100."),
            "he": ("הרפתקה זו מבוססת על מקורות ארכאולוגיים וגנטיים רבים, כגון {sources}. "
                   "הנתונים הגולמיים מגיעים מ-{providers}, וכלי המחקר שבהם נעשה שימוש כוללים את {tools}. דירוג אמינות: {reliability}/100."),
            "hi": ("यह यात्रा {sources} जैसे अनेक पुरातात्त्विक और आनुवंशिक स्रोतों पर आधारित है। "
                   "कच्चा डेटा {providers} से प्राप्त होता है, और उपयोग किए गए अनुसंधान उपकरणों में {tools} शामिल हैं। विश्वसनीयता स्कोर: {reliability}/100."),
            "bn": ("এই যাত্রাটি {sources} সহ বহু প্রত্নতাত্ত্বিক ও জেনেটিক উৎসের উপর ভিত্তি করে তৈরি। "
                   "কাঁচা তথ্য এসেছে {providers} থেকে, এবং ব্যবহৃত গবেষণা সরঞ্জামগুলির মধ্যে রয়েছে {tools}। বিশ্বাসযোগ্যতার স্কোর: {reliability}/100."),
            "tr": ("Bu yolculuk, {sources} gibi çok sayıda arkeolojik ve genetik kaynağa dayanmaktadır. "
                   "Ham veriler {providers} kaynaklıdır ve kullanılan araştırma araçları arasında {tools} bulunmaktadır. Güvenilirlik puanı: {reliability}/100."),
            "fa": ("این سفر بر پایه منابع متعدد باستان‌شناسی و ژنتیکی مانند {sources} استوار است. "
                   "داده‌های خام از {providers} تأمین شده و ابزارهای پژوهشی استفاده‌شده شامل {tools} هستند. امتیاز اعتبار: {reliability}/100."),
            "ur": ("یہ سفر {sources} جیسے متعدد آثارِ قدیمہ اور جینیاتی ذرائع پر مبنی ہے۔ "
                   "خام ڈیٹا {providers} سے حاصل ہوا ہے، اور استعمال شدہ تحقیقی آلات میں {tools} شامل ہیں۔ اعتماد کی درجہ بندی: {reliability}/100."),
            "sw": ("Safari hii inategemea vyanzo vingi vya akiolojia na kijeni, kama vile {sources}. "
                   "Data ghafi hutoka kwa {providers}, na zana za utafiti zilizotumika ni pamoja na {tools}. Kiwango cha uaminifu: {reliability}/100."),
            "am": ("ይህ ጉዞ {sources} ያሉ ብዙ የአርኬዮሎጂ እና የጄኔቲክ ምንጮችን መሰረት ያደርጋል። "
                   "የሚጠቀሙት የመረጃ ምንጮች {providers} ናቸው፣ እና የተጠቀሱት የምርምር መሳሪያዎች {tools} ናቸው። የታመነነት ደረጃ: {reliability}/100."),
            "yo": ("Ìrìnàjò yìí dá lórí ọ̀pọ̀ orísun arkeoloji àti jiini gẹ́gẹ́ bí {sources}. "
                   "Àwọn data àkọ́kọ́ wa láti {providers}, àti àwọn irinṣẹ́ ìwádìí tí a lo ni {tools}. Ìdíyelé ìgbàgbọ́: {reliability}/100."),
            "zu": ("Lolu hambo lusekelwe emithonjeni eminingi yezinto zakudala nezofuzo, njengokuthi {sources}. "
                   "Idatha eluhlaza ivela ku {providers}, kanti amathuluzi ocwaningo asetshenzisiwe afaka {tools}. Isilinganiso sokuthembeka: {reliability}/100."),
            "id": ("Perjalanan ini didasarkan pada berbagai sumber arkeologi dan genetik, seperti {sources}. "
                   "Data mentah berasal dari {providers}, dan alat penelitian yang digunakan mencakup {tools}. Skor keandalan: {reliability}/100."),
            "ms": ("Perjalanan ini berasaskan pelbagai sumber arkeologi dan genetik, seperti {sources}. "
                   "Data mentah berasal dari {providers}, dan alat penyelidikan yang digunakan termasuk {tools}. Skor kebolehpercayaan: {reliability}/100."),
            "th": ("การเดินทางนี้อ้างอิงจากแหล่งข้อมูลทางโบราณคดีและพันธุกรรมจำนวนมาก เช่น {sources} "
                   "ข้อมูลดิบมาจาก {providers} และเครื่องมือวิจัยที่ใช้รวมถึง {tools} คะแนนความน่าเชื่อถือ: {reliability}/100"),
            "vi": ("Hành trình này dựa trên nhiều nguồn khảo cổ và di truyền học như {sources}. "
                   "Dữ liệu thô đến từ {providers}, và các công cụ nghiên cứu được sử dụng bao gồm {tools}. Điểm độ tin cậy: {reliability}/100."),
            "tl": ("Ang paglalakbay na ito ay batay sa maraming mapagkukunang arkeolohikal at henetiko tulad ng {sources}. "
                   "Ang hilaw na datos ay nagmula sa {providers}, at ang mga ginamit na kasangkapan sa pananaliksik ay kinabibilangan ng {tools}. Antas ng pagiging mapagkakatiwalaan: {reliability}/100."),
            "pl": ("Ta podróż opiera się na licznych źródłach archeologicznych i genetycznych, takich jak {sources}. "
                   "Dane surowe pochodzą z {providers}, a użyte narzędzia badawcze obejmują {tools}. Ocena wiarygodności: {reliability}/100."),
            "cs": ("Tato cesta vychází z mnoha archeologických a genetických zdrojů, jako jsou {sources}. "
                   "Surová data pocházejí z {providers} a použité výzkumné nástroje zahrnují {tools}. Hodnocení spolehlivosti: {reliability}/100."),
            "sk": ("Táto cesta vychádza z mnohých archeologických a genetických zdrojov, ako sú {sources}. "
                   "Surové údaje pochádzajú z {providers} a použité výskumné nástroje zahŕňajú {tools}. Hodnotenie spoľahlivosti: {reliability}/100."),
            "hu": ("Ez az utazás számos régészeti és genetikai forráson alapul, mint például {sources}. "
                   "A nyers adatok a {providers} forrásaiból származnak, és a használt kutatási eszközök közé tartozik {tools}. Megbízhatósági értékelés: {reliability}/100."),
            "ro": ("Această călătorie se bazează pe numeroase surse arheologice și genetice, precum {sources}. "
                   "Datele brute provin de la {providers}, iar instrumentele de cercetare utilizate includ {tools}. Scor de fiabilitate: {reliability}/100."),
            "bg": ("Това пътешествие се основава на множество археологически и генетични източници, като {sources}. "
                   "Суровите данни идват от {providers}, а използваните изследователски инструменти включват {tools}. Оценка на надеждност: {reliability}/100."),
            "el": ("Αυτό το ταξίδι βασίζεται σε πολλές αρχαιολογικές και γενετικές πηγές, όπως {sources}. "
                   "Τα ακατέργαστα δεδομένα προέρχονται από {providers}, και τα εργαλεία έρευνας που χρησιμοποιήθηκαν περιλαμβάνουν {tools}. Βαθμολογία αξιοπιστίας: {reliability}/100."),
            "nl": ("Deze reis is gebaseerd op talrijke archeologische en genetische bronnen, zoals {sources}. "
                   "Ruwe gegevens zijn afkomstig van {providers}, en de gebruikte onderzoekstools omvatten {tools}. Betrouwbaarheidsscore: {reliability}/100."),
            "da": ("Denne rejse er baseret på mange arkæologiske og genetiske kilder, såsom {sources}. "
                   "Rådata stammer fra {providers}, og anvendte forskningsværktøjer inkluderer {tools}. Pålidelighedsvurdering: {reliability}/100."),
            "no": ("Denne reisen er basert på mange arkeologiske og genetiske kilder, som {sources}. "
                   "Rådata kommer fra {providers}, og brukte forskningsverktøy inkluderer {tools}. Pålitelighetsvurdering: {reliability}/100."),
            "et": ("See teekond põhineb paljudel arheoloogilistel ja geneetilistel allikatel, nagu {sources}. "
                   "Toorandmed pärinevad {providers} ning kasutatud uurimisvahendid hõlmavad {tools}. Usaldusväärsuse hinne: {reliability}/100."),
            "lv": ("Šis ceļojums balstās uz daudziem arheoloģiskiem un ģenētiskiem avotiem, piemēram, {sources}. "
                   "Neapstrādātie dati nāk no {providers}, un izmantotie pētniecības rīki ietver {tools}. Uzticamības vērtējums: {reliability}/100."),
            "lt": ("Ši kelionė remiasi daugybe archeologinių ir genetinių šaltinių, tokių kaip {sources}. "
                   "Neapdoroti duomenys gaunami iš {providers}, o naudojami tyrimų įrankiai apima {tools}. Patikimumo įvertinimas: {reliability}/100."),
            "is": ("Þessi ferð byggir á fjölmörgum fornleifafræðilegum og erfðafræðilegum heimildum, svo sem {sources}. "
                   "Hrá gögn koma frá {providers}, og notuð rannsóknartæki fela í sér {tools}. Áreiðanleikamat: {reliability}/100."),
            "ga": ("Tá an turas seo bunaithe ar go leor foinsí seandálaíochta agus géiniteacha, amhail {sources}. "
                   "Tagann na sonraí amh ó {providers}, agus áirítear ar na huirlisí taighde a úsáideadh {tools}. Scór iontaofachta: {reliability}/100."),
            "sr": ("Ово путовање заснива се на бројним археолошким и генетским изворима, као што су {sources}. "
                   "Сирови подаци потичу од {providers}, а коришћени истраживачки алати укључују {tools}. Оцена поузданости: {reliability}/100."),
            "hr": ("Ovo putovanje temelji se na brojnim arheološkim i genetskim izvorima, poput {sources}. "
                   "Sirovi podaci dolaze iz {providers}, a korišteni istraživački alati uključuju {tools}. Ocjena pouzdanosti: {reliability}/100."),
            "sl": ("To potovanje temelji na številnih arheoloških in genetskih virih, kot so {sources}. "
                   "Surovi podatki izvirajo iz {providers}, uporabljena raziskovalna orodja pa vključujejo {tools}. Ocena zanesljivosti: {reliability}/100."),
            "uk": ("Ця подорож базується на численних археологічних та генетичних джерелах, таких як {sources}. "
                   "Сирі дані надходять з {providers}, а використані дослідницькі інструменти включають {tools}. Оцінка надійності: {reliability}/100."),
            "ka": ("ეს მოგზაურობა ეფუძნება მრავალ არქეოლოგიურ და გენეტიკურ წყაროს, როგორიცაა {sources}. "
                   "ნედლი მონაცემები მოდის {providers}-დან, ხოლო გამოყენებული კვლევითი ინსტრუმენტები მოიცავს {tools}. სანდოობის შეფასება: {reliability}/100."),
            "hy": ("Այս ճանապարհորդությունը հիմնված է բազմաթիվ հնագիտական և գենետիկական աղբյուրների վրա, ինչպիսիք են {sources}։ "
                   "Հում տվյալները ստացվում են {providers}-ից, իսկ օգտագործված հետազոտական գործիքները ներառում են {tools}։ Վստահելիության գնահատում՝ {reliability}/100։"),
            "mn": ("Энэхүү аялал нь {sources} зэрэг олон археологийн болон генетикийн эх сурвалжид тулгуурладаг. "
                   "Түүхий өгөгдөл нь {providers}-оос ирсэн бөгөөд ашигласан судалгааны хэрэгслүүдэд {tools} орно. Найдвартай байдлын үнэлгээ: {reliability}/100."),
            "kk": ("Бұл сапар {sources} сияқты көптеген археологиялық және генетикалық дереккөздерге негізделген. "
                   "Шикі деректер {providers}-тен алынған, ал қолданылған зерттеу құралдарына {tools} кіреді. Сенімділік бағасы: {reliability}/100."),
            "uz": ("Ushbu sayohat {sources} kabi ko'plab arxeologik va genetik manbalarga asoslanadi. "
                   "Xom ma'lumotlar {providers}-dan olinadi va ishlatilgan tadqiqot vositalariga {tools} kiradi. Ishonchlilik bahosi: {reliability}/100."),
            "ta": ("இந்தப் பயணம் {sources} போன்ற பல தொல்லியல் மற்றும் மரபணு ஆதாரங்களை அடிப்படையாகக் கொண்டது. "
                   "மூலத் தரவுகள் {providers} இலிருந்து பெறப்பட்டவை, பயன்படுத்தப்பட்ட ஆராய்ச்சி கருவிகளில் {tools} அடங்கும். நம்பகத்தன்மை மதிப்பெண்: {reliability}/100."),
            "te": ("ఈ ప్రయాణం {sources} వంటి అనేక పురావస్తు మరియు జన్యు మూలాలపై ఆధారపడి ఉంది. "
                   "మూల డేటా {providers} నుండి వస్తుంది, మరియు ఉపయోగించిన పరిశోధనా సాధనాలలో {tools} ఉన్నాయి. నమ్మకత రేటింగ్: {reliability}/100."),
            "kn": ("ಈ ಪ್ರಯಾಣವು {sources} ಎಂಬ ಅನೇಕ ಪುರಾತತ್ವ ಮತ್ತು ಜನ್ಯ ಮೂಲಗಳ ಮೇಲೆ ಆಧಾರಿತವಾಗಿದೆ. "
                   "ಕಚ್ಚಾ ದತ್ತಾಂಶ {providers} ನಿಂದ ಬರುತ್ತದೆ, ಮತ್ತು ಬಳಸಲಾದ ಸಂಶೋಧನಾ ಸಾಧನಗಳಲ್ಲಿ {tools} ಸೇರಿವೆ. ವಿಶ್ವಾಸಾರ್ಹತೆ ಅಂಕ: {reliability}/100."),
            "ml": ("ഈ യാത്ര {sources} പോലുള്ള നിരവധി പുരാവസ്തു-ജന്യ ഉറവിടങ്ങളെ അടിസ്ഥാനമാക്കിയുള്ളതാണ്. "
                   "മൂല ഡാറ്റ {providers}യിൽ നിന്നാണ് ലഭിക്കുന്നത്, ഉപയോഗിച്ച ഗവേഷണ ഉപകരണങ്ങളിൽ {tools} ഉൾപ്പെടുന്നു. വിശ്വാസ്യത സ്കോർ: {reliability}/100."),
            "ne": ("यो यात्रा {sources} जस्ता धेरै पुरातात्त्विक र आनुवंशिक स्रोतहरूमा आधारित छ। "
                   "कच्चा डेटा {providers} बाट आएको हो, र प्रयोग गरिएका अनुसन्धान उपकरणहरूमा {tools} समावेश छन्। विश्वसनीयता स्कोर: {reliability}/100."),
            "si": ("මෙම ගමන {sources} වැනි බොහෝ පුරාවිද්‍යාත්මක සහ ජීව විද්‍යාත්මක මූලාශ්‍ර මත පදනම් වේ. "
                   "අමු දත්ත {providers} වෙතින් ලැබෙන අතර, භාවිතා කරන ලද පර්යේෂණ උපකරණවලට {tools} ඇතුළත් වේ. විශ්වාසනීයතා ලකුණු: {reliability}/100."),
            "my": ("ဤခရီးသည် {sources} ကဲ့သို့သော အများအပြားသော ရှေးဟောင်းနှင့် မျိုးဗီဇဆိုင်ရာ အရင်းအမြစ်များအပေါ် အခြေခံထားပါသည်။ "
                   "မူရင်းဒေတာသည် {providers} မှ ရရှိလာပြီး အသုံးပြုထားသော သုတေသနကိရိယာများတွင် {tools} ပါဝင်ပါသည်။ ယုံကြည်မှုအဆင့်: {reliability}/100."),
            "km": ("ដំណើរនេះផ្អែកលើប្រភពបុរាណវិទ្យា និងហ្សែនជាច្រើនដូចជា {sources}។ "
                   "ទិន្នន័យដើមមកពី {providers} ហើយឧបករណ៍ស្រាវជ្រាវដែលបានប្រើរួមមាន {tools}។ ពិន្ទុភាពទុកចិត្ត: {reliability}/100."),
            "lo": ("ການເດີນທາງນີ້ອີງຕາມແຫຼ່ງຂໍ້ມູນທາງບູຮານຄະດີແລະພັນທຸກຳຫຼາຍແຫຼ່ງ ເຊັ່ນ {sources}. "
                   "ຂໍ້ມູນດິບມາຈາກ {providers} ແລະເຄື່ອງມືການຄົ້ນຄວ້າທີ່ໃຊ້ຮວມມີ {tools}. ຄະແນນຄວາມໜ້າເຊື່ອຖື: {reliability}/100."),
            "haw": ("Ua hoʻokumu ʻia kēia huakaʻi ma luna o nā kumu ʻike archaeological a genetic he nui, e like me {sources}. "
                    "Mai nā {providers} nā ʻike kumu, a pili pū nā mea hana noiʻi i hoʻohana ʻia i ka {tools}. Kikoʻī hilinaʻi: {reliability}/100."),
            "mi": ("E hāngai ana tēnei haerenga ki ngā pūtake whaipara tangata me ngā pūtake ira maha, pērā i a {sources}. "
                   "Nō {providers} ngā raraunga taketake, ā, ko ngā taputapu rangahau i whakamahia ko {tools}. Tatauranga whakawhirinaki: {reliability}/100."),
            "sm": ("O lenei malaga e fa'avae i luga o le tele o punaoa o suʻesuʻega o toega ma le genetika, e pei o {sources}. "
                   "O fa'amaumauga mata'utia e maua mai i {providers}, ma o meafaigaluega su'esu'e na fa'aaogaina e aofia ai {tools}. Fuainumera fa'atuatuaina: {reliability}/100."),
            "es-mx": ("Este recorrido se basa en numerosas fuentes arqueológicas y genéticas, como {sources}. "
                      "Los datos brutos provienen de {providers}, y las herramientas de investigación utilizadas incluyen {tools}. Calificación de fiabilidad: {reliability}/100."),
            "pt-br": ("Esta jornada baseia-se em numerosas fontes arqueológicas e genéticas, como {sources}. "
                      "Os dados brutos provêm de {providers}, e as ferramentas de pesquisa utilizadas incluem {tools}. Classificação de confiabilidade: {reliability}/100."),
        }
    }


def get_text(key: str, lang: Optional[str] = None, **kwargs) -> str:
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


def get_translation(lang: Optional[str] = None, key: str = None, **kwargs) -> str:
    """Legacy function for backward compatibility with email_utils."""
    return get_text(key, lang, **kwargs)


# ---------------------------------------------------------------------------
# STYLE PROFILE TEMPLATES
# Rakenne: STYLE_PROFILE_TEMPLATES[section_key][lang_code] = template_string
# Fallback-ketju: haluttu kieli → "en" → first available
# ---------------------------------------------------------------------------

_DEFAULT_LANG = "en"

STYLE_PROFILE_TEMPLATES: Dict[str, Dict[str, str]] = {
    "introduction": {
        "fi": "Tämä on haploryhmän {haplogroup} tarina, joka ulottuu {time_depth} taakse. Levinneisyys: {regions}.",
        "en": "This is the story of haplogroup {haplogroup}, reaching back {time_depth}. Distribution: {regions}.",
        "sv": "Detta är berättelsen om haplogrupp {haplogroup}, som sträcker sig {time_depth} tillbaka. Utbredning: {regions}.",
        "de": "Dies ist die Geschichte der Haplogruppe {haplogroup}, die {time_depth} zurückreicht. Verbreitung: {regions}.",
        "fr": "Voici l'histoire de l'haplogroupe {haplogroup}, remontant à {time_depth}. Répartition : {regions}.",
        "es": "Esta es la historia del haplogrupo {haplogroup}, que se remonta {time_depth}. Distribución: {regions}.",
        "pt": "Esta é a história do haplogrupo {haplogroup}, que remonta {time_depth}. Distribuição: {regions}.",
        "it": "Questa è la storia dell'aplogruppo {haplogroup}, che risale a {time_depth}. Distribuzione: {regions}.",
        "ru": "Это история гаплогруппы {haplogroup}, уходящей на {time_depth} назад. Распространение: {regions}.",
        "zh": "这是单倍群 {haplogroup} 的故事，可追溯至 {time_depth} 前。分布地区：{regions}。",
        "ja": "これはハプログループ {haplogroup} の物語で、{time_depth} 前に遡ります。分布地域：{regions}。",
        "ko": "이것은 하플로그룹 {haplogroup}의 이야기로, {time_depth} 전으로 거슬러 올라갑니다. 분포: {regions}.",
        "ar": "هذه قصة المجموعة المتشعبة {haplogroup}، التي تمتد لـ {time_depth}. التوزيع: {regions}.",
        "he": "זוהי סיפורה של קבוצת ההפלוגרופ {haplogroup}, החוזרת לפני {time_depth}. התפוצה: {regions}.",
        "hi": "यह हैप्लोग्रुप {haplogroup} की कहानी है, जो {time_depth} पीछे जाती है। वितरण: {regions}।",
        "tr": "Bu, {time_depth} öncesine uzanan {haplogroup} haplogrubunun hikayesidir. Dağılım: {regions}.",
        "pl": "To historia haplohrupy {haplogroup}, sięgającej {time_depth} wstecz. Zasięg: {regions}.",
        "nl": "Dit is het verhaal van haplogroep {haplogroup}, dat teruggaat tot {time_depth}. Verspreiding: {regions}.",
        "da": "Dette er historien om haplogruppe {haplogroup}, der strækker sig {time_depth} tilbage. Udbredelse: {regions}.",
        "no": "Dette er historien om haplogruppe {haplogroup}, som strekker seg {time_depth} tilbake. Utbredelse: {regions}.",
        "uk": "Це історія гаплогрупи {haplogroup}, що сягає {time_depth} у минуле. Поширення: {regions}.",
    },
    "sample_entry": {
        "fi": "{sample_id}: {location} ({date}), kulttuuri {culture}",
        "en": "{sample_id}: {location} ({date}), culture {culture}",
        "sv": "{sample_id}: {location} ({date}), kultur {culture}",
        "de": "{sample_id}: {location} ({date}), Kultur {culture}",
        "fr": "{sample_id} : {location} ({date}), culture {culture}",
        "es": "{sample_id}: {location} ({date}), cultura {culture}",
        "pt": "{sample_id}: {location} ({date}), cultura {culture}",
        "it": "{sample_id}: {location} ({date}), cultura {culture}",
        "ru": "{sample_id}: {location} ({date}), культура {culture}",
        "zh": "{sample_id}：{location}（{date}），文化 {culture}",
        "ja": "{sample_id}：{location}（{date}）、文化 {culture}",
        "ko": "{sample_id}: {location} ({date}), 문화 {culture}",
        "ar": "{sample_id}: {location} ({date})، ثقافة {culture}",
        "he": "{sample_id}: {location} ({date}), תרבות {culture}",
        "hi": "{sample_id}: {location} ({date}), संस्कृति {culture}",
        "tr": "{sample_id}: {location} ({date}), kültür {culture}",
        "pl": "{sample_id}: {location} ({date}), kultura {culture}",
        "nl": "{sample_id}: {location} ({date}), cultuur {culture}",
        "uk": "{sample_id}: {location} ({date}), культура {culture}",
    },
    "famous_person_entry": {
        "fi": "{name} ({era}) - {significance}",
        "en": "{name} ({era}) – {significance}",
        "sv": "{name} ({era}) – {significance}",
        "de": "{name} ({era}) – {significance}",
        "fr": "{name} ({era}) – {significance}",
        "es": "{name} ({era}) – {significance}",
        "pt": "{name} ({era}) – {significance}",
        "it": "{name} ({era}) – {significance}",
        "ru": "{name} ({era}) — {significance}",
        "zh": "{name}（{era}）—— {significance}",
        "ja": "{name}（{era}）― {significance}",
        "ko": "{name} ({era}) – {significance}",
        "ar": "{name} ({era}) – {significance}",
        "he": "{name} ({era}) – {significance}",
        "hi": "{name} ({era}) – {significance}",
        "tr": "{name} ({era}) – {significance}",
        "pl": "{name} ({era}) – {significance}",
        "nl": "{name} ({era}) – {significance}",
        "uk": "{name} ({era}) — {significance}",
    },
    "hotspot_entry": {
        "fi": "{location} ({period}): {significance}",
        "en": "{location} ({period}): {significance}",
        "sv": "{location} ({period}): {significance}",
        "de": "{location} ({period}): {significance}",
        "fr": "{location} ({period}) : {significance}",
        "es": "{location} ({period}): {significance}",
        "pt": "{location} ({period}): {significance}",
        "it": "{location} ({period}): {significance}",
        "ru": "{location} ({period}): {significance}",
        "zh": "{location}（{period}）：{significance}",
        "ja": "{location}（{period}）：{significance}",
        "ko": "{location} ({period}): {significance}",
        "ar": "{location} ({period}): {significance}",
        "he": "{location} ({period}): {significance}",
        "hi": "{location} ({period}): {significance}",
        "tr": "{location} ({period}): {significance}",
        "pl": "{location} ({period}): {significance}",
        "nl": "{location} ({period}): {significance}",
        "uk": "{location} ({period}): {significance}",
    },
    "culture_entry": {
        "fi": "{culture} - {period} ({region})",
        "en": "{culture} – {period} ({region})",
        "sv": "{culture} – {period} ({region})",
        "de": "{culture} – {period} ({region})",
        "fr": "{culture} – {period} ({region})",
        "es": "{culture} – {period} ({region})",
        "pt": "{culture} – {period} ({region})",
        "it": "{culture} – {period} ({region})",
        "ru": "{culture} — {period} ({region})",
        "zh": "{culture} — {period}（{region}）",
        "ja": "{culture} — {period}（{region}）",
        "ko": "{culture} – {period} ({region})",
        "ar": "{culture} – {period} ({region})",
        "he": "{culture} – {period} ({region})",
        "hi": "{culture} – {period} ({region})",
        "tr": "{culture} – {period} ({region})",
        "pl": "{culture} – {period} ({region})",
        "nl": "{culture} – {period} ({region})",
        "uk": "{culture} — {period} ({region})",
    },
    "regional_profile": {
        "fi": "Alue {region}: {key_finds}, kulttuurit {cultures}",
        "en": "Region {region}: {key_finds}, cultures {cultures}",
        "sv": "Region {region}: {key_finds}, kulturer {cultures}",
        "de": "Region {region}: {key_finds}, Kulturen {cultures}",
        "fr": "Région {region} : {key_finds}, cultures {cultures}",
        "es": "Región {region}: {key_finds}, culturas {cultures}",
        "pt": "Região {region}: {key_finds}, culturas {cultures}",
        "it": "Regione {region}: {key_finds}, culture {cultures}",
        "ru": "Регион {region}: {key_finds}, культуры {cultures}",
        "zh": "地区 {region}：{key_finds}，文化 {cultures}",
        "ja": "地域 {region}：{key_finds}、文化 {cultures}",
        "ko": "지역 {region}: {key_finds}, 문화 {cultures}",
        "ar": "منطقة {region}: {key_finds}، ثقافات {cultures}",
        "he": "אזור {region}: {key_finds}, תרבויות {cultures}",
        "hi": "क्षेत्र {region}: {key_finds}, संस्कृतियाँ {cultures}",
        "tr": "Bölge {region}: {key_finds}, kültürler {cultures}",
        "pl": "Region {region}: {key_finds}, kultury {cultures}",
        "nl": "Regio {region}: {key_finds}, culturen {cultures}",
        "uk": "Регіон {region}: {key_finds}, культури {cultures}",
    },
    "modern_distribution": {
        "fi": "Nykyään levinneisyys: {regions}",
        "en": "Modern distribution: {regions}",
        "sv": "Modern utbredning: {regions}",
        "de": "Moderne Verbreitung: {regions}",
        "fr": "Répartition moderne : {regions}",
        "es": "Distribución moderna: {regions}",
        "pt": "Distribuição moderna: {regions}",
        "it": "Distribuzione moderna: {regions}",
        "ru": "Современное распространение: {regions}",
        "zh": "现代分布：{regions}",
        "ja": "現代の分布：{regions}",
        "ko": "현대 분포: {regions}",
        "ar": "التوزيع الحديث: {regions}",
        "he": "תפוצה מודרנית: {regions}",
        "hi": "आधुनिक वितरण: {regions}",
        "tr": "Modern dağılım: {regions}",
        "pl": "Współczesny zasięg: {regions}",
        "nl": "Moderne verspreiding: {regions}",
        "uk": "Сучасне поширення: {regions}",
    },
    "sources_section": {
        "fi": "Lähteet: {sources}. Tarjoajat: {providers}. Analyysityökalut: {tools}. Luotettavuus: {reliability}%",
        "en": "Sources: {sources}. Providers: {providers}. Analysis tools: {tools}. Reliability: {reliability}%",
        "sv": "Källor: {sources}. Leverantörer: {providers}. Analysverktyg: {tools}. Tillförlitlighet: {reliability}%",
        "de": "Quellen: {sources}. Anbieter: {providers}. Analysewerkzeuge: {tools}. Zuverlässigkeit: {reliability}%",
        "fr": "Sources : {sources}. Fournisseurs : {providers}. Outils d'analyse : {tools}. Fiabilité : {reliability}%",
        "es": "Fuentes: {sources}. Proveedores: {providers}. Herramientas de análisis: {tools}. Fiabilidad: {reliability}%",
        "pt": "Fontes: {sources}. Fornecedores: {providers}. Ferramentas de análise: {tools}. Confiabilidade: {reliability}%",
        "it": "Fonti: {sources}. Fornitori: {providers}. Strumenti di analisi: {tools}. Affidabilità: {reliability}%",
        "ru": "Источники: {sources}. Поставщики: {providers}. Инструменты анализа: {tools}. Надёжность: {reliability}%",
        "zh": "来源：{sources}。提供者：{providers}。分析工具：{tools}。可靠性：{reliability}%",
        "ja": "情報源：{sources}。提供者：{providers}。分析ツール：{tools}。信頼性：{reliability}%",
        "ko": "출처: {sources}. 제공자: {providers}. 분석 도구: {tools}. 신뢰도: {reliability}%",
        "ar": "المصادر: {sources}. المزودون: {providers}. أدوات التحليل: {tools}. الموثوقية: {reliability}%",
        "he": "מקורות: {sources}. ספקים: {providers}. כלי ניתוח: {tools}. אמינות: {reliability}%",
        "hi": "स्रोत: {sources}. प्रदाता: {providers}. विश्लेषण उपकरण: {tools}. विश्वसनीयता: {reliability}%",
        "tr": "Kaynaklar: {sources}. Sağlayıcılar: {providers}. Analiz araçları: {tools}. Güvenilirlik: {reliability}%",
        "pl": "Źródła: {sources}. Dostawcy: {providers}. Narzędzia analityczne: {tools}. Wiarygodność: {reliability}%",
        "nl": "Bronnen: {sources}. Aanbieders: {providers}. Analysetools: {tools}. Betrouwbaarheid: {reliability}%",
        "uk": "Джерела: {sources}. Постачальники: {providers}. Аналітичні інструменти: {tools}. Надійність: {reliability}%",
    },
    "legal_section": {
        "fi": "Vastuuvapaus: Tämä raportti perustuu tieteellisiin lähteisiin, mutta se ei ole oikeudellinen neuvonta.",
        "en": "Disclaimer: This report is based on scientific sources and does not constitute legal advice.",
        "sv": "Ansvarsfriskrivning: Denna rapport baseras på vetenskapliga källor och utgör inte juridisk rådgivning.",
        "de": "Haftungsausschluss: Dieser Bericht basiert auf wissenschaftlichen Quellen und stellt keine Rechtsberatung dar.",
        "fr": "Avertissement : Ce rapport est basé sur des sources scientifiques et ne constitue pas un conseil juridique.",
        "es": "Aviso legal: Este informe se basa en fuentes científicas y no constituye asesoramiento jurídico.",
        "pt": "Aviso legal: Este relatório baseia-se em fontes científicas e não constitui aconselhamento jurídico.",
        "it": "Avvertenza: Questo rapporto è basato su fonti scientifiche e non costituisce consulenza legale.",
        "ru": "Отказ от ответственности: Этот отчет основан на научных источниках и не является юридической консультацией.",
        "zh": "免责声明：本报告基于科学来源，不构成法律建议。",
        "ja": "免責事項：このレポートは科学的な情報源に基づいており、法的アドバイスを構成するものではありません。",
        "ko": "면책 조항: 이 보고서는 과학적 출처를 기반으로 하며 법적 조언을 구성하지 않습니다.",
        "ar": "إخلاء المسؤولية: يستند هذا التقرير إلى مصادر علمية ولا يشكل استشارة قانونية.",
        "he": "הסרת אחריות: דוח זה מבוסס על מקורות מדעיים ואינו מהווה ייעוץ משפטי.",
        "hi": "अस्वीकरण: यह रिपोर्ट वैज्ञानिक स्रोतों पर आधारित है और कानूनी सलाह नहीं है।",
        "tr": "Sorumluluk Reddi: Bu rapor bilimsel kaynaklara dayanmaktadır ve hukuki tavsiye niteliği taşımamaktadır.",
        "pl": "Zastrzeżenie: Raport opiera się na źródłach naukowych i nie stanowi porady prawnej.",
        "nl": "Disclaimer: Dit rapport is gebaseerd op wetenschappelijke bronnen en vormt geen juridisch advies.",
        "uk": "Відмова від відповідальності: Цей звіт ґрунтується на наукових джерелах і не є юридичною порадою.",
    },
    "genealogy_comparison_section": {
        "fi": "Arkeogenetiikka tutkii DNA:ta muinaisnäytteistä. Sukututkimus tutkii kirjallisia ja DNA-todistusaineistoja.",
        "en": "Archaeogenetics studies DNA from ancient samples. Genealogy examines written records and DNA evidence.",
        "sv": "Arkeogenetik studerar DNA från forntida prover. Genealogi undersöker skriftliga källor och DNA-bevis.",
        "de": "Archäogenetik untersucht DNA aus antiken Proben. Genealogie untersucht schriftliche Quellen und DNA-Beweise.",
        "fr": "L'archéogénétique étudie l'ADN des échantillons anciens. La généalogie examine les archives écrites et les preuves ADN.",
        "es": "La arqueogenética estudia el ADN de muestras antiguas. La genealogía examina registros escritos y evidencias de ADN.",
        "pt": "A arqueogenética estuda o DNA de amostras antigas. A genealogia examina registros escritos e evidências de DNA.",
        "it": "L'archeogenetica studia il DNA dai campioni antichi. La genealogia esamina documenti scritti e prove del DNA.",
        "ru": "Археогенетика изучает ДНК из древних образцов. Генеалогия исследует письменные источники и ДНК-свидетельства.",
        "zh": "考古遗传学研究古代样本中的DNA。系谱学研究书面记录和DNA证据。",
        "ja": "考古遺伝学は古代サンプルのDNAを研究します。系譜学は文書記録とDNA証拠を調査します。",
        "ko": "고고유전학은 고대 샘플의 DNA를 연구합니다. 계보학은 문서 기록과 DNA 증거를 검토합니다.",
        "ar": "تدرس الجينات الأثرية الحمض النووي من العينات القديمة. يدرس علم الأنساب السجلات المكتوبة وأدلة الحمض النووي.",
        "tr": "Arkeogenetik, eski örneklerden elde edilen DNA'yı inceler. Soyağacı çalışmaları yazılı kayıtları ve DNA kanıtlarını araştırır.",
        "pl": "Archeogenetyka bada DNA z próbek starożytnych. Genealogia analizuje dokumenty pisane i dowody DNA.",
        "nl": "Archeogenetica bestudeert DNA uit oude monsters. Genealogie onderzoekt schriftelijke bronnen en DNA-bewijs.",
        "uk": "Археогенетика досліджує ДНК зі стародавніх зразків. Генеалогія вивчає письмові джерела та ДНК-докази.",
    },
    "dual_encounters_section": {
        "fi": "Alueilla {regions} Y-DNA {y} ja mtDNA {mt} ovat jäljittäneet samoja väestöliikkeitä.",
        "en": "In regions {regions}, Y-DNA {y} and mtDNA {mt} have tracked the same population movements.",
        "sv": "I regionerna {regions} har Y-DNA {y} och mtDNA {mt} spårat samma befolkningsrörelser.",
        "de": "In den Regionen {regions} haben Y-DNA {y} und mtDNA {mt} dieselben Bevölkerungsbewegungen verfolgt.",
        "fr": "Dans les régions {regions}, l'ADN-Y {y} et l'ADNmt {mt} ont retracé les mêmes mouvements de population.",
        "es": "En las regiones {regions}, el ADN-Y {y} y el ADNmt {mt} han rastreado los mismos movimientos de población.",
        "pt": "Nas regiões {regions}, o DNA-Y {y} e o mtDNA {mt} rastrearam os mesmos movimentos populacionais.",
        "it": "Nelle regioni {regions}, il DNA-Y {y} e il mtDNA {mt} hanno tracciato gli stessi movimenti di popolazione.",
        "ru": "В регионах {regions} Y-ДНК {y} и мтДНК {mt} отслеживали одни и те же перемещения населения.",
        "zh": "在地区 {regions}，Y-DNA {y} 与 mtDNA {mt} 追踪了相同的人口迁徙。",
        "ja": "地域 {regions} では、Y-DNA {y} と mtDNA {mt} が同じ人口移動を追跡しています。",
        "ko": "지역 {regions}에서 Y-DNA {y}와 mtDNA {mt}는 동일한 인구 이동을 추적했습니다.",
        "tr": "{regions} bölgelerinde Y-DNA {y} ve mtDNA {mt} aynı nüfus hareketlerini izledi.",
        "pl": "W regionach {regions} Y-DNA {y} i mtDNA {mt} śledziły te same ruchy populacji.",
        "nl": "In regio's {regions} hebben Y-DNA {y} en mtDNA {mt} dezelfde bevolkingsbewegingen gevolgd.",
        "uk": "У регіонах {regions} Y-ДНК {y} та мтДНК {mt} відстежували однакові переміщення населення.",
    },
    "dual_love_story_section": {
        "fi": "Kahden linjan ({y} ja {mt}) kohtaaminen historian kuluessa",
        "en": "The convergence of two lineages ({y} and {mt}) through history",
        "sv": "Mötet mellan två linjer ({y} och {mt}) genom historien",
        "de": "Das Aufeinandertreffen zweier Linien ({y} und {mt}) im Laufe der Geschichte",
        "fr": "La convergence de deux lignées ({y} et {mt}) à travers l'histoire",
        "es": "La convergencia de dos linajes ({y} y {mt}) a lo largo de la historia",
        "pt": "A convergência de duas linhagens ({y} e {mt}) ao longo da história",
        "it": "La convergenza di due lignaggi ({y} e {mt}) nel corso della storia",
        "ru": "Слияние двух линий ({y} и {mt}) сквозь историю",
        "zh": "两个谱系（{y} 和 {mt}）在历史中的交汇",
        "ja": "二つの系統（{y} と {mt}）の歴史を通じた出会い",
        "ko": "두 계통({y}과 {mt})의 역사 속 만남",
        "tr": "İki soyun ({y} ve {mt}) tarih boyunca buluşması",
        "pl": "Spotkanie dwóch linii ({y} i {mt}) w historii",
        "nl": "De samensmelting van twee lijnen ({y} en {mt}) door de geschiedenis",
        "uk": "Злиття двох ліній ({y} і {mt}) крізь історію",
    },
    "dual_heritage_section": {
        "fi": "Kahden linjan perintö: {y} isämuistina, {mt} äitimuistina.",
        "en": "The legacy of two lineages: {y} as paternal memory, {mt} as maternal memory.",
        "sv": "Arvet från två linjer: {y} som faderligt minne, {mt} som moderligt minne.",
        "de": "Das Erbe zweier Linien: {y} als väterliches Gedächtnis, {mt} als mütterliches Gedächtnis.",
        "fr": "L'héritage de deux lignées : {y} comme mémoire paternelle, {mt} comme mémoire maternelle.",
        "es": "El legado de dos linajes: {y} como memoria paterna, {mt} como memoria materna.",
        "pt": "O legado de duas linhagens: {y} como memória paterna, {mt} como memória materna.",
        "it": "L'eredità di due lignaggi: {y} come memoria paterna, {mt} come memoria materna.",
        "ru": "Наследие двух линий: {y} как отцовская память, {mt} как материнская память.",
        "zh": "两个谱系的遗产：{y} 作为父系记忆，{mt} 作为母系记忆。",
        "ja": "二つの系統の遺産：{y} は父系の記憶、{mt} は母系の記憶。",
        "ko": "두 계통의 유산: {y}는 부계 기억으로, {mt}는 모계 기억으로.",
        "tr": "İki soyun mirası: {y} baba belleği olarak, {mt} anne belleği olarak.",
        "pl": "Spuścizna dwóch linii: {y} jako pamięć ojcowska, {mt} jako pamięć macierzyńska.",
        "nl": "Het erfgoed van twee lijnen: {y} als vaderlijke herinnering, {mt} als moederlijke herinnering.",
        "uk": "Спадщина двох ліній: {y} як батьківська пам'ять, {mt} як материнська пам'ять.",
    },
    "heritage_section": {
        "fi": "Haploryhmä {haplogroup} on osa ihmiskunnan jatkuvaa historiaa.",
        "en": "Haplogroup {haplogroup} is part of humanity's continuous history.",
        "sv": "Haplogrupp {haplogroup} är en del av mänsklighetens kontinuerliga historia.",
        "de": "Haplogruppe {haplogroup} ist Teil der kontinuierlichen Geschichte der Menschheit.",
        "fr": "L'haplogroupe {haplogroup} fait partie de l'histoire continue de l'humanité.",
        "es": "El haplogrupo {haplogroup} forma parte de la historia continua de la humanidad.",
        "pt": "O haplogrupo {haplogroup} faz parte da história contínua da humanidade.",
        "it": "L'aplogruppo {haplogroup} fa parte della storia continua dell'umanità.",
        "ru": "Гаплогруппа {haplogroup} является частью непрерывной истории человечества.",
        "zh": "单倍群 {haplogroup} 是人类连续历史的一部分。",
        "ja": "ハプログループ {haplogroup} は人類の連続した歴史の一部です。",
        "ko": "하플로그룹 {haplogroup}은 인류의 연속적인 역사의 일부입니다.",
        "ar": "المجموعة المتشعبة {haplogroup} جزء من التاريخ المستمر للبشرية.",
        "he": "קבוצת ההפלוגרופ {haplogroup} היא חלק מההיסטוריה הרציפה של האנושות.",
        "hi": "हैप्लोग्रुप {haplogroup} मानवता के निरंतर इतिहास का हिस्सा है।",
        "tr": "{haplogroup} haplogrubu, insanlığın sürekli tarihinin bir parçasıdır.",
        "pl": "Haplogrupa {haplogroup} jest częścią ciągłej historii ludzkości.",
        "nl": "Haplogroep {haplogroup} maakt deel uit van de voortdurende geschiedenis van de mensheid.",
        "uk": "Гаплогрупа {haplogroup} є частиною безперервної історії людства.",
    },
}


def get_style_profile(lang: str = "en", tone: str = "academic") -> Dict[str, str]:
    """
    Palauttaa tyyliprofiili-sanakirjan lokalisoituine template-merkkijonoineen.
    Fallback-ketju: haluttu kieli → en → first available.

    Args:
        lang:  BCP-47-kielikoodi, esim. "fi", "en", "zh"
        tone:  "academic" | "narrative" | "adventure"  (tuleva laajennus)
    """
    result: Dict[str, str] = {}
    for section_key, translations in STYLE_PROFILE_TEMPLATES.items():
        result[section_key] = (
            translations.get(lang)
            or translations.get(_DEFAULT_LANG)
            or next(iter(translations.values()))
        )
    return result


def get_style_profile_template(section: str, lang: str = "en") -> str:
    """
    Palauttaa yksittäisen osion template-merkkijonon.

    Raises:
        KeyError: jos section-avain ei löydy
    """
    translations = STYLE_PROFILE_TEMPLATES[section]
    return (
        translations.get(lang)
        or translations.get(_DEFAULT_LANG)
        or next(iter(translations.values()))
    )


def format_sources_list(sources: List[str], lang: Optional[str] = None) -> str:
    """Muotoilee lähdeluettelon kieli- ja kulttuurisensitiivisesti."""
    lang = lang or get_default_language()
    if not sources:
        return ""
    if lang in ["zh", "ja", "ko"]:
        return "、".join(sources)
    elif lang in ["ar", "he"]:
        return "، ".join(sources)
    else:
        return ", ".join(sources)
