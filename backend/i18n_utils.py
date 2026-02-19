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
        },

        # ─────────────────────────────────────────────────────────────
        # UI-avaimet: story_utils.py:n section-otsikot ja fallback-tekstit
        # ─────────────────────────────────────────────────────────────

        "story_title": {
            "fi": "Haploryhmä {haplogroup} – Verilinjan seikkailu ajassa",
            "en": "Haplogroup {haplogroup} – A Bloodline's Journey Through Time",
            "sv": "Haplogrupp {haplogroup} – En blodslinjes resa genom tid",
            "de": "Haplogruppe {haplogroup} – Eine Reise durch die Zeit",
            "fr": "Haplogroupe {haplogroup} – Le voyage d'une lignée à travers le temps",
            "es": "Haplogrupo {haplogroup} – El viaje de un linaje a través del tiempo",
            "pt": "Haplogrupo {haplogroup} – A jornada de uma linhagem ao longo do tempo",
            "it": "Aplogruppo {haplogroup} – Il viaggio di un lignaggio nel tempo",
            "ru": "Гаплогруппа {haplogroup} – Путешествие рода сквозь время",
            "zh": "单倍群 {haplogroup} ——血脉的时空之旅",
            "ja": "ハプログループ {haplogroup} ── 血脈の時を超えた旅",
            "ko": "하플로그룹 {haplogroup} – 혈통의 시간 여행",
            "ar": "المجموعة {haplogroup} – رحلة سلالة عبر الزمن",
            "he": "הפלוגרופ {haplogroup} – מסע שושלת בזמן",
            "hi": "हैप्लोग्रुप {haplogroup} – एक वंश का समय के पार सफर",
            "tr": "Haplogrubu {haplogroup} – Bir Soyun Zamanda Yolculuğu",
            "pl": "Haplogrupa {haplogroup} – podróż rodu przez czas",
            "nl": "Haplogroep {haplogroup} – Een bloedsreis door de tijd",
            "da": "Haplogruppe {haplogroup} – En blodslinjes rejse gennem tid",
            "uk": "Гаплогрупа {haplogroup} – Подорож роду крізь час",
        },
        "story_subtitle": {
            "fi": "Arkeogeneettinen kertomus | Linjatyyppi: {lineage_type}",
            "en": "Archaeogenetic narrative | Lineage type: {lineage_type}",
            "sv": "Arkeogenetisk berättelse | Linjtyp: {lineage_type}",
            "de": "Archäogenetische Erzählung | Linientyp: {lineage_type}",
            "fr": "Récit archéogénétique | Type de lignée : {lineage_type}",
            "es": "Narrativa arqueogenética | Tipo de linaje: {lineage_type}",
            "pt": "Narrativa arqueogenética | Tipo de linhagem: {lineage_type}",
            "it": "Racconto archeogenetico | Tipo di lignaggio: {lineage_type}",
            "ru": "Археогенетическое повествование | Тип линии: {lineage_type}",
            "zh": "考古遗传学叙述 | 谱系类型：{lineage_type}",
            "ja": "考古遺伝学的物語 | 系統タイプ：{lineage_type}",
            "ko": "고고유전학적 서사 | 계통 유형: {lineage_type}",
            "ar": "سرد أثري جيني | نوع السلالة: {lineage_type}",
            "he": "נרטיב ארכאוגנטי | סוג שושלת: {lineage_type}",
            "hi": "पुरातात्विक-आनुवंशिक कथा | वंश प्रकार: {lineage_type}",
            "tr": "Arkeogenetik anlatı | Soy türü: {lineage_type}",
            "pl": "Narracja archeogenetyczna | Typ linii: {lineage_type}",
            "uk": "Археогенетичне оповідання | Тип лінії: {lineage_type}",
        },
        "story_hook": {
            "fi": (
                "Rakas ystävä, tämä ei ole tavallinen raportti. "
                "Tämä on hetki, jolloin menneisyys astuu huoneeseen ja sanoo: "
                "'Minä olen täällä. Olen aina ollut täällä. Ja minä olen sinä.' "
                " Veresi on viimeinen lenkki {haplogroup}-ketjussa, "
                "joka ulottuu tuhansien vuosien taakse."
            ),
            "en": (
                "Dear reader, this is not an ordinary report. "
                "This is the moment when the past steps into the room and says: "
                "'I am here. I have always been here. And I am you.' "
                "Your blood is the last link in the {haplogroup} chain, "
                "stretching back thousands of years."
            ),
            "sv": (
                "Käre läsare, detta är inte en vanlig rapport. "
                "Det är ögonblicket då det förflutna kliver in i rummet och säger: "
                "'Jag är här. Jag har alltid funnits här. Och jag är du.' "
                "Ditt blod är den sista länken i {haplogroup}-kedjan."
            ),
            "de": (
                "Lieber Leser, dies ist kein gewöhnlicher Bericht. "
                "Dies ist der Moment, in dem die Vergangenheit den Raum betritt und sagt: "
                "'Ich bin hier. Ich war immer hier. Und ich bin du.' "
                "Dein Blut ist das letzte Glied in der {haplogroup}-Kette."
            ),
            "fr": (
                "Cher lecteur, ce n'est pas un rapport ordinaire. "
                "C'est le moment où le passé entre dans la pièce et dit : "
                "'Je suis là. J'ai toujours été là. Et je suis toi.' "
                "Votre sang est le dernier maillon de la chaîne {haplogroup}."
            ),
            "es": (
                "Querido lector, este no es un informe ordinario. "
                "Es el momento en que el pasado entra a la sala y dice: "
                "'Estoy aquí. Siempre he estado aquí. Y soy tú.' "
                "Tu sangre es el último eslabón en la cadena {haplogroup}."
            ),
            "pt": (
                "Caro leitor, este não é um relatório comum. "
                "É o momento em que o passado entra na sala e diz: "
                "'Estou aqui. Sempre estive aqui. E eu sou você.' "
                "Seu sangue é o último elo da cadeia {haplogroup}."
            ),
            "it": (
                "Caro lettore, questa non è una relazione ordinaria. "
                "È il momento in cui il passato entra nella stanza e dice: "
                "'Sono qui. Sono sempre stato qui. E sono te.' "
                "Il tuo sangue è l'ultimo anello della catena {haplogroup}."
            ),
            "ru": (
                "Дорогой читатель, это не обычный отчёт. "
                "Это момент, когда прошлое входит в комнату и говорит: "
                "«Я здесь. Я всегда был здесь. И я — это ты». "
                "Твоя кровь — последнее звено в цепи {haplogroup}."
            ),
            "zh": "亲爱的读者，这不是一份普通的报告。这是过去踏入房间说：'我在这里，我一直都在，我就是你'的时刻。你的血脉是 {haplogroup} 链条的最后一环。",
            "ja": "親愛なる読者へ、これは普通のレポートではありません。過去が部屋に入り「私はここにいる、ずっとここにいた、そして私はあなただ」と語る瞬間です。あなたの血は {haplogroup} の鎖の最後の環です。",
            "ko": "친애하는 독자여, 이것은 평범한 보고서가 아닙니다. 과거가 방으로 들어와 '나는 여기 있다, 항상 여기 있었다, 나는 당신이다'라고 말하는 순간입니다. 당신의 혈통은 {haplogroup} 사슬의 마지막 고리입니다.",
            "ar": "عزيزي القارئ، هذا ليس تقريراً عادياً. إنه اللحظة التي يدخل فيها الماضي الغرفة ويقول: 'أنا هنا، كنت دائماً هنا، وأنا أنت.' دمك هو الحلقة الأخيرة في سلسلة {haplogroup}.",
            "he": "קורא יקר, זה לא דוח רגיל. זהו הרגע שבו העבר נכנס לחדר ואומר: 'אני כאן, תמיד הייתי כאן, ואני אתה.' דמך הוא החוליה האחרונה בשרשרת {haplogroup}.",
            "tr": "Sevgili okuyucu, bu sıradan bir rapor değil. Geçmişin odaya girip 'Buradayım, hep buradaydım ve ben senim' dediği andır. Kanın {haplogroup} zincirinin son halkasıdır.",
            "pl": "Drogi czytelniku, to nie jest zwykły raport. To moment, gdy przeszłość wchodzi do pokoju i mówi: 'Jestem tutaj, zawsze tu byłem i jestem tobą.' Twoja krew jest ostatnim ogniwem łańcucha {haplogroup}.",
            "uk": "Дорогий читачу, це не звичайний звіт. Це момент, коли минуле заходить до кімнати і каже: «Я тут, я завжди був тут, і я — це ти». Твоя кров — остання ланка в ланцюгу {haplogroup}.",
        },

        # ─── Section titles ──────────────────────────────────────────
        "section_introduction_title": {
            "fi": "Johdanto", "en": "Introduction", "sv": "Introduktion",
            "de": "Einleitung", "fr": "Introduction", "es": "Introducción",
            "pt": "Introdução", "it": "Introduzione", "ru": "Введение",
            "zh": "简介", "ja": "はじめに", "ko": "소개",
            "ar": "مقدمة", "he": "מבוא", "hi": "परिचय",
            "tr": "Giriş", "pl": "Wstęp", "nl": "Inleiding",
            "da": "Introduktion", "uk": "Вступ",
        },
        "section_chronological_title": {
            "fi": "Kronologinen matka", "en": "Chronological Journey",
            "sv": "Kronologisk resa", "de": "Chronologische Reise",
            "fr": "Voyage chronologique", "es": "Viaje cronológico",
            "pt": "Viagem cronológica", "it": "Viaggio cronologico",
            "ru": "Хронологическое путешествие", "zh": "时间顺序之旅",
            "ja": "年代順の旅", "ko": "연대순 여정",
            "ar": "رحلة زمنية", "he": "מסע כרונולוגי",
            "hi": "कालानुक्रमिक यात्रा", "tr": "Kronolojik Yolculuk",
            "pl": "Podróż chronologiczna", "uk": "Хронологічна подорож",
        },
        "section_cultural_title": {
            "fi": "Kulttuurikonteksti", "en": "Cultural Context",
            "sv": "Kulturellt sammanhang", "de": "Kultureller Kontext",
            "fr": "Contexte culturel", "es": "Contexto cultural",
            "pt": "Contexto cultural", "it": "Contesto culturale",
            "ru": "Культурный контекст", "zh": "文化背景",
            "ja": "文化的文脈", "ko": "문화적 맥락",
            "ar": "السياق الثقافي", "he": "הקשר תרבותי",
            "hi": "सांस्कृतिक संदर्भ", "tr": "Kültürel Bağlam",
            "pl": "Kontekst kulturowy", "uk": "Культурний контекст",
        },
        "section_famous_people_title": {
            "fi": "Tunnetut historialliset henkilöt", "en": "Notable Historical Figures",
            "sv": "Kända historiska personer", "de": "Bekannte historische Persönlichkeiten",
            "fr": "Personnages historiques notables", "es": "Personajes históricos notables",
            "pt": "Figuras históricas notáveis", "it": "Figure storiche notevoli",
            "ru": "Известные исторические личности", "zh": "著名历史人物",
            "ja": "著名な歴史的人物", "ko": "주목할 역사적 인물",
            "ar": "شخصيات تاريخية بارزة", "he": "דמויות היסטוריות בולטות",
            "hi": "प्रसिद्ध ऐतिहासिक व्यक्तित्व", "tr": "Önemli Tarihî Şahsiyetler",
            "pl": "Znane postacie historyczne", "uk": "Відомі історичні особи",
        },
        "section_hotspots_title": {
            "fi": "Erityiset esiintymiskeskittymät", "en": "Notable Hotspots",
            "sv": "Anmärkningsvärda hotspots", "de": "Besondere Häufungspunkte",
            "fr": "Points chauds notables", "es": "Zonas de concentración notables",
            "pt": "Pontos de concentração notáveis", "it": "Hotspot notevoli",
            "ru": "Особые очаги концентрации", "zh": "值得关注的热点地区",
            "ja": "注目のホットスポット", "ko": "주목할 핫스팟",
            "ar": "نقاط تركيز بارزة", "he": "נקודות חמות בולטות",
            "hi": "उल्लेखनीय हॉटस्पॉट", "tr": "Önemli Yoğunluk Noktaları",
            "pl": "Szczególne skupiska", "uk": "Особливі осередки концентрації",
        },
        "section_region_title": {
            "fi": "Alue: {region}", "en": "Region: {region}",
            "sv": "Region: {region}", "de": "Region: {region}",
            "fr": "Région : {region}", "es": "Región: {region}",
            "pt": "Região: {region}", "it": "Regione: {region}",
            "ru": "Регион: {region}", "zh": "地区：{region}",
            "ja": "地域：{region}", "ko": "지역: {region}",
            "ar": "المنطقة: {region}", "he": "אזור: {region}",
            "hi": "क्षेत्र: {region}", "tr": "Bölge: {region}",
            "pl": "Region: {region}", "uk": "Регіон: {region}",
        },
        "section_source_narrative_title": {
            "fi": "Tietolähteiden kuvaukset", "en": "Data Source Descriptions",
            "sv": "Datakällsbeskrivningar", "de": "Datenquellenbeschreibungen",
            "fr": "Descriptions des sources de données", "es": "Descripciones de fuentes de datos",
            "pt": "Descrições de fontes de dados", "it": "Descrizioni delle fonti dati",
            "ru": "Описания источников данных", "zh": "数据来源说明",
            "ja": "データソースの説明", "ko": "데이터 소스 설명",
            "ar": "أوصاف مصادر البيانات", "he": "תיאורי מקורות נתונים",
            "hi": "डेटा स्रोत विवरण", "tr": "Veri Kaynağı Açıklamaları",
            "pl": "Opisy źródeł danych", "uk": "Опис джерел даних",
        },
        "section_modern_distribution_title": {
            "fi": "Nykyinen levinneisyys", "en": "Modern Distribution",
            "sv": "Modern utbredning", "de": "Moderne Verbreitung",
            "fr": "Répartition moderne", "es": "Distribución moderna",
            "pt": "Distribuição moderna", "it": "Distribuzione moderna",
            "ru": "Современное распространение", "zh": "现代分布",
            "ja": "現代の分布", "ko": "현대 분포",
            "ar": "التوزيع الحديث", "he": "תפוצה מודרנית",
            "hi": "आधुनिक वितरण", "tr": "Modern Dağılım",
            "pl": "Współczesny zasięg", "uk": "Сучасне поширення",
        },
        "section_genealogy_comparison_title": {
            "fi": "Ero perinteiseen sukututkimukseen", "en": "Difference from Traditional Genealogy",
            "sv": "Skillnad från traditionell genealogi", "de": "Unterschied zur traditionellen Genealogie",
            "fr": "Différence avec la généalogie traditionnelle", "es": "Diferencia con la genealogía tradicional",
            "pt": "Diferença da genealogia tradicional", "it": "Differenza dalla genealogia tradizionale",
            "ru": "Отличие от традиционной генеалогии", "zh": "与传统家谱学的区别",
            "ja": "伝統的な系譜学との違い", "ko": "전통 계보학과의 차이",
            "ar": "الفرق عن علم الأنساب التقليدي", "he": "הבדל מהגנאולוגיה המסורתית",
            "hi": "पारंपरिक वंशावली से अंतर", "tr": "Geleneksel Soyağacından Fark",
            "pl": "Różnica od tradycyjnej genealogii", "uk": "Відмінність від традиційної генеалогії",
        },
        "section_sources_title": {
            "fi": "Lähteet ja luotettavuus", "en": "Sources & Reliability",
            "sv": "Källor och tillförlitlighet", "de": "Quellen & Zuverlässigkeit",
            "fr": "Sources et fiabilité", "es": "Fuentes y fiabilidad",
            "pt": "Fontes e confiabilidade", "it": "Fonti e affidabilità",
            "ru": "Источники и надёжность", "zh": "来源与可靠性",
            "ja": "情報源と信頼性", "ko": "출처 및 신뢰도",
            "ar": "المصادر والموثوقية", "he": "מקורות ואמינות",
            "hi": "स्रोत और विश्वसनीयता", "tr": "Kaynaklar ve Güvenilirlik",
            "pl": "Źródła i wiarygodność", "uk": "Джерела та надійність",
        },
        "section_legal_title": {
            "fi": "Oikeudellinen ilmoitus ja yksityisyys", "en": "Legal Notice & Privacy",
            "sv": "Rättslig information och integritet", "de": "Rechtlicher Hinweis & Datenschutz",
            "fr": "Mention légale et confidentialité", "es": "Aviso legal y privacidad",
            "pt": "Aviso legal e privacidade", "it": "Note legali e privacy",
            "ru": "Правовое уведомление и конфиденциальность", "zh": "法律声明与隐私",
            "ja": "法的通知とプライバシー", "ko": "법적 고지 및 개인정보",
            "ar": "إشعار قانوني وخصوصية", "he": "הודעה משפטית ופרטיות",
            "hi": "कानूनी सूचना और गोपनीयता", "tr": "Yasal Uyarı ve Gizlilik",
            "pl": "Nota prawna i prywatność", "uk": "Правове повідомлення та конфіденційність",
        },
        "section_heritage_title": {
            "fi": "Perintö ja merkitys", "en": "Heritage & Significance",
            "sv": "Arv och betydelse", "de": "Erbe & Bedeutung",
            "fr": "Héritage et signification", "es": "Herencia y significado",
            "pt": "Herança e significado", "it": "Eredità e significato",
            "ru": "Наследие и значение", "zh": "遗产与意义",
            "ja": "遺産と意義", "ko": "유산 및 의미",
            "ar": "التراث والأهمية", "he": "מורשת ומשמעות",
            "hi": "विरासत और महत्व", "tr": "Miras ve Anlam",
            "pl": "Dziedzictwo i znaczenie", "uk": "Спадщина та значення",
        },
        "section_y_story_title": {
            "fi": "Y-DNA linja: {haplogroup}", "en": "Y-DNA Lineage: {haplogroup}",
            "sv": "Y-DNA-linje: {haplogroup}", "de": "Y-DNA-Linie: {haplogroup}",
            "fr": "Lignée Y-ADN : {haplogroup}", "es": "Linaje ADN-Y: {haplogroup}",
            "pt": "Linhagem DNA-Y: {haplogroup}", "it": "Lignaggio DNA-Y: {haplogroup}",
            "ru": "Линия Y-ДНК: {haplogroup}", "zh": "Y-DNA 系统：{haplogroup}",
            "ja": "Y-DNA 系統：{haplogroup}", "ko": "Y-DNA 계통: {haplogroup}",
            "ar": "سلالة الحمض النووي-Y: {haplogroup}", "he": "שושלת Y-DNA: {haplogroup}",
            "tr": "Y-DNA Soyu: {haplogroup}", "pl": "Linia Y-DNA: {haplogroup}",
            "uk": "Лінія Y-ДНК: {haplogroup}",
        },
        "section_mt_story_title": {
            "fi": "mtDNA linja: {haplogroup}", "en": "mtDNA Lineage: {haplogroup}",
            "sv": "mtDNA-linje: {haplogroup}", "de": "mtDNA-Linie: {haplogroup}",
            "fr": "Lignée ADNmt : {haplogroup}", "es": "Linaje ADNmt: {haplogroup}",
            "pt": "Linhagem mtDNA: {haplogroup}", "it": "Lignaggio mtDNA: {haplogroup}",
            "ru": "Линия мтДНК: {haplogroup}", "zh": "mtDNA 系统：{haplogroup}",
            "ja": "mtDNA 系統：{haplogroup}", "ko": "mtDNA 계통: {haplogroup}",
            "ar": "سلالة الحمض النووي للميتوكوندريا: {haplogroup}", "he": "שושלת mtDNA: {haplogroup}",
            "tr": "mtDNA Soyu: {haplogroup}", "pl": "Linia mtDNA: {haplogroup}",
            "uk": "Лінія мтДНК: {haplogroup}",
        },
        "section_dual_encounters_title": {
            "fi": "Historialliset kohtaamiset", "en": "Historical Encounters",
            "sv": "Historiska möten", "de": "Historische Begegnungen",
            "fr": "Rencontres historiques", "es": "Encuentros históricos",
            "pt": "Encontros históricos", "it": "Incontri storici",
            "ru": "Исторические встречи", "zh": "历史相遇",
            "ja": "歴史的な出会い", "ko": "역사적 만남",
            "ar": "اللقاءات التاريخية", "he": "מפגשים היסטוריים",
            "tr": "Tarihsel Karşılaşmalar", "pl": "Historyczne spotkania",
            "uk": "Історичні зустрічі",
        },
        "section_dual_love_story_title": {
            "fi": "Kahden linjan tarina", "en": "The Story of Two Lineages",
            "sv": "Berättelsen om två linjer", "de": "Die Geschichte zweier Linien",
            "fr": "L'histoire de deux lignées", "es": "La historia de dos linajes",
            "pt": "A história de duas linhagens", "it": "La storia di due lignaggi",
            "ru": "История двух линий", "zh": "两条谱系的故事",
            "ja": "二つの系統の物語", "ko": "두 계통의 이야기",
            "ar": "قصة سلالتين", "he": "סיפור שתי שושלות",
            "tr": "İki Soyun Hikayesi", "pl": "Historia dwóch linii",
            "uk": "Історія двох ліній",
        },
        "section_dual_heritage_title": {
            "fi": "Yhteinen perintö", "en": "Shared Heritage",
            "sv": "Gemensamt arv", "de": "Gemeinsames Erbe",
            "fr": "Héritage commun", "es": "Herencia compartida",
            "pt": "Herança compartilhada", "it": "Eredità comune",
            "ru": "Общее наследие", "zh": "共同遗产",
            "ja": "共有の遺産", "ko": "공유 유산",
            "ar": "التراث المشترك", "he": "מורשת משותפת",
            "tr": "Ortak Miras", "pl": "Wspólne dziedzictwo",
            "uk": "Спільна спадщина",
        },
        "dual_story_title": {
            "fi": "Kahden verilinjan seikkailu: {y} × {mt}",
            "en": "The Journey of Two Lineages: {y} × {mt}",
            "sv": "Två blodslinjers resa: {y} × {mt}",
            "de": "Die Reise zweier Linien: {y} × {mt}",
            "fr": "Le voyage de deux lignées : {y} × {mt}",
            "es": "El viaje de dos linajes: {y} × {mt}",
            "pt": "A jornada de duas linhagens: {y} × {mt}",
            "it": "Il viaggio di due lignaggi: {y} × {mt}",
            "ru": "Путешествие двух линий: {y} × {mt}",
            "zh": "两条谱系之旅：{y} × {mt}",
            "ja": "二つの系統の旅：{y} × {mt}",
            "ko": "두 계통의 여정: {y} × {mt}",
            "tr": "İki Soyun Yolculuğu: {y} × {mt}",
            "pl": "Podróż dwóch linii: {y} × {mt}",
            "uk": "Подорож двох ліній: {y} × {mt}",
        },
        "dual_story_subtitle": {
            "fi": "Y-DNA + mtDNA yhdistetty arkeogeneettinen kertomus",
            "en": "Y-DNA + mtDNA combined archaeogenetic narrative",
            "sv": "Y-DNA + mtDNA kombinerad arkeogenetisk berättelse",
            "de": "Y-DNA + mtDNA kombinierte archäogenetische Erzählung",
            "fr": "Y-ADN + ADNmt – récit archéogénétique combiné",
            "es": "ADN-Y + ADNmt – narrativa arqueogenética combinada",
            "pt": "DNA-Y + mtDNA – narrativa arqueogenética combinada",
            "it": "DNA-Y + mtDNA – racconto archeogenetico combinato",
            "ru": "Y-ДНК + мтДНК – объединённое археогенетическое повествование",
            "zh": "Y-DNA + mtDNA 综合考古遗传叙述",
            "ja": "Y-DNA + mtDNA 統合考古遺伝学的物語",
            "ko": "Y-DNA + mtDNA 통합 고고유전학 서사",
            "tr": "Y-DNA + mtDNA kombinasyonlu arkeogenetik anlatı",
            "pl": "Y-DNA + mtDNA połączona narracja archeogenetyczna",
            "uk": "Y-ДНК + мтДНК – об'єднане археогенетичне оповідання",
        },

        # ─── Fallback / placeholder tekstit ─────────────────────────
        "no_ancient_samples_available": {
            "fi": "Muinaisnäytteitä ei ole tällä hetkellä saatavilla tälle haploryhmälle.",
            "en": "No ancient samples are currently available for this haplogroup.",
            "sv": "Inga forntida prover är för närvarande tillgängliga för denna haplogrupp.",
            "de": "Für diese Haplogruppe sind derzeit keine antiken Proben verfügbar.",
            "fr": "Aucun échantillon ancien n'est actuellement disponible pour ce haplogroupe.",
            "es": "No hay muestras antiguas disponibles actualmente para este haplogrupo.",
            "pt": "Não há amostras antigas disponíveis atualmente para este haplogrupo.",
            "it": "Non sono attualmente disponibili campioni antichi per questo aplogruppo.",
            "ru": "Для этой гаплогруппы пока нет доступных древних образцов.",
            "zh": "目前没有该单倍群的古代样本。",
            "ja": "このハプログループの古代サンプルは現在利用できません。",
            "ko": "이 하플로그룹에 대한 고대 샘플이 현재 없습니다.",
            "tr": "Bu haplogrubu için şu anda eski örnek bulunmamaktadır.",
            "pl": "Brak dostępnych starożytnych próbek dla tej haplogrupy.",
            "uk": "Стародавні зразки для цієї гаплогрупи наразі відсутні.",
        },
        "no_cultural_data_available": {
            "fi": "Kulttuuridataa ei ole saatavilla.", "en": "No cultural data available.",
            "sv": "Ingen kulturdata tillgänglig.", "de": "Keine Kulturdaten verfügbar.",
            "fr": "Aucune donnée culturelle disponible.", "es": "No hay datos culturales disponibles.",
            "pt": "Sem dados culturais disponíveis.", "it": "Nessun dato culturale disponibile.",
            "ru": "Культурные данные недоступны.", "zh": "无文化数据。",
            "ja": "文化データなし。", "ko": "문화 데이터 없음.",
            "tr": "Kültür verisi yok.", "pl": "Brak danych kulturowych.",
            "uk": "Культурні дані відсутні.",
        },
        "no_genealogy_comparison_available": {
            "fi": "Vertailua ei ole saatavilla.", "en": "Comparison not available.",
            "sv": "Jämförelse ej tillgänglig.", "de": "Vergleich nicht verfügbar.",
            "fr": "Comparaison non disponible.", "es": "Comparación no disponible.",
            "pt": "Comparação não disponível.", "it": "Confronto non disponibile.",
            "ru": "Сравнение недоступно.", "zh": "比较不可用。",
            "ja": "比較利用不可。", "ko": "비교 불가.",
            "tr": "Karşılaştırma mevcut değil.", "pl": "Porównanie niedostępne.",
            "uk": "Порівняння недоступне.",
        },
        "no_regions_available": {
            "fi": "Alueita ei ole saatavilla.", "en": "No regions available.",
            "sv": "Inga regioner tillgängliga.", "de": "Keine Regionen verfügbar.",
            "fr": "Aucune région disponible.", "es": "No hay regiones disponibles.",
            "pt": "Sem regiões disponíveis.", "it": "Nessuna regione disponibile.",
            "ru": "Регионы недоступны.", "zh": "无地区信息。",
            "ja": "地域情報なし。", "ko": "지역 없음.",
            "tr": "Bölge yok.", "pl": "Brak regionów.",
            "uk": "Регіони відсутні.",
        },
        "no_shared_regions": {
            "fi": "Yhteisiä alueita ei löydetty.", "en": "No shared regions found.",
            "sv": "Inga gemensamma regioner hittades.", "de": "Keine gemeinsamen Regionen gefunden.",
            "fr": "Aucune région commune trouvée.", "es": "No se encontraron regiones comunes.",
            "pt": "Nenhuma região comum encontrada.", "it": "Nessuna regione comune trovata.",
            "ru": "Общих регионов не найдено.", "zh": "未找到共同地区。",
            "ja": "共通地域なし。", "ko": "공유 지역 없음.",
            "tr": "Ortak bölge bulunamadı.", "pl": "Brak wspólnych regionów.",
            "uk": "Спільних регіонів не знайдено.",
        },
        "unknown_time_depth": {
            "fi": "tuntematon aika", "en": "unknown time",
            "sv": "okänd tid", "de": "unbekannte Zeit",
            "fr": "période inconnue", "es": "tiempo desconocido",
            "pt": "tempo desconhecido", "it": "tempo sconosciuto",
            "ru": "неизвестное время", "zh": "未知时期",
            "ja": "不明な時期", "ko": "알 수 없는 시간",
            "tr": "bilinmeyen zaman", "pl": "nieznany czas",
            "uk": "невідомий час",
        },
        "unknown_location": {
            "fi": "tuntematon paikka", "en": "unknown location",
            "sv": "okänd plats", "de": "unbekannter Ort",
            "fr": "lieu inconnu", "es": "ubicación desconocida",
            "pt": "localização desconhecida", "it": "luogo sconosciuto",
            "ru": "неизвестное место", "zh": "未知地点",
            "ja": "不明な場所", "ko": "알 수 없는 위치",
            "tr": "bilinmeyen konum", "pl": "nieznane miejsce",
            "uk": "невідоме місце",
        },
        "unknown_date": {
            "fi": "tuntematon päivämäärä", "en": "unknown date",
            "sv": "okänt datum", "de": "unbekanntes Datum",
            "fr": "date inconnue", "es": "fecha desconocida",
            "pt": "data desconhecida", "it": "data sconosciuta",
            "ru": "неизвестная дата", "zh": "未知日期",
            "ja": "不明な日付", "ko": "알 수 없는 날짜",
            "tr": "bilinmeyen tarih", "pl": "nieznana data",
            "uk": "невідома дата",
        },
        "unknown_culture": {
            "fi": "tuntematon kulttuuri", "en": "unknown culture",
            "sv": "okänd kultur", "de": "unbekannte Kultur",
            "fr": "culture inconnue", "es": "cultura desconocida",
            "pt": "cultura desconhecida", "it": "cultura sconosciuta",
            "ru": "неизвестная культура", "zh": "未知文化",
            "ja": "不明な文化", "ko": "알 수 없는 문화",
            "tr": "bilinmeyen kültür", "pl": "nieznana kultura",
            "uk": "невідома культура",
        },
        "unknown_sample": {
            "fi": "tuntematon näyte", "en": "unknown sample",
            "sv": "okänt prov", "de": "unbekannte Probe",
            "fr": "échantillon inconnu", "es": "muestra desconocida",
            "pt": "amostra desconhecida", "it": "campione sconosciuto",
            "ru": "неизвестный образец", "zh": "未知样本",
            "ja": "不明なサンプル", "ko": "알 수 없는 샘플",
            "tr": "bilinmeyen örnek", "pl": "nieznana próbka",
            "uk": "невідомий зразок",
        },
        "methodology_archaeogenetics": {
            "fi": "Arkeogenetiikka", "en": "Archaeogenetics",
            "sv": "Arkeogenetik", "de": "Archäogenetik",
            "fr": "Archéogénétique", "es": "Arqueogenética",
            "pt": "Arqueogenética", "it": "Archeogenetica",
            "ru": "Археогенетика", "zh": "考古遗传学",
            "ja": "考古遺伝学", "ko": "고고유전학",
            "ar": "الجينات الأثرية", "he": "ארכאוגנטיקה",
            "tr": "Arkeogenetik", "pl": "Archeogenetyka",
            "uk": "Археогенетика",
        },
        "source_type_peer_reviewed": {
            "fi": "Vertaisarvioidut julkaisut", "en": "Peer-reviewed publications",
            "sv": "Kollegialt granskade publikationer", "de": "Peer-Review-Publikationen",
            "fr": "Publications évaluées par les pairs", "es": "Publicaciones revisadas por pares",
            "pt": "Publicações revisadas por pares", "it": "Pubblicazioni peer-reviewed",
            "ru": "Рецензируемые публикации", "zh": "同行评审期刊",
            "ja": "査読付き論文", "ko": "동료 심사 출판물",
            "ar": "منشورات محكّمة", "he": "פרסומים שעברו ביקורת עמיתים",
            "tr": "Hakemli yayınlar", "pl": "Recenzowane publikacje",
            "uk": "Рецензовані публікації",
        },

        # ─── Fragment keys: data_utils.py:n source_* avaimet ─────────
        "source_yfull": {
            "fi": "YFull tarjoaa kalibroidut fylogeneettiset puut ja aikasyvyysarviot haploryhmälle {haplogroup}.",
            "en": "YFull provides calibrated phylogenetic trees and time-depth estimates for haplogroup {haplogroup}.",
            "sv": "YFull tillhandahåller kalibrerade fylogenetiska träd och tidsdjupsestimat för haplogrupp {haplogroup}.",
            "de": "YFull bietet kalibrierte phylogenetische Bäume und Zeittiefenschätzungen für Haplogruppe {haplogroup}.",
            "fr": "YFull fournit des arbres phylogénétiques calibrés et des estimations de profondeur temporelle pour l'haplogroupe {haplogroup}.",
            "es": "YFull proporciona árboles filogenéticos calibrados y estimaciones de profundidad temporal para el haplogrupo {haplogroup}.",
            "pt": "YFull fornece árvores filogenéticas calibradas e estimativas de profundidade temporal para o haplogrupo {haplogroup}.",
            "it": "YFull fornisce alberi filogenetici calibrati e stime di profondità temporale per l'aplogruppo {haplogroup}.",
            "ru": "YFull предоставляет откалиброванные филогенетические деревья и оценки глубины времени для гаплогруппы {haplogroup}.",
            "zh": "YFull 为单倍群 {haplogroup} 提供经校准的系统发育树和时间深度估算。",
            "ja": "YFull はハプログループ {haplogroup} の較正された系統樹と時間的深度推定を提供します。",
            "ko": "YFull은 하플로그룹 {haplogroup}에 대한 보정된 계통수와 시간 깊이 추정값을 제공합니다.",
            "tr": "{haplogroup} haplogrubu için YFull kalibreli filogenetik ağaçlar ve zaman derinliği tahminleri sunar.",
            "pl": "YFull dostarcza skalibrowane drzewa filogenetyczne i szacunki głębokości czasu dla haplogrupy {haplogroup}.",
            "uk": "YFull надає відкалібровані філогенетичні дерева та оцінки глибини часу для гаплогрупи {haplogroup}.",
        },
        "source_isogg": {
            "fi": "ISOGG Y-DNA Tree dokumentoi haploryhmän {haplogroup} haarautumat ja SNP-mutaatiot.",
            "en": "ISOGG Y-DNA Tree documents the branches and SNP mutations of haplogroup {haplogroup}.",
            "sv": "ISOGG Y-DNA Tree dokumenterar grenarna och SNP-mutationerna för haplogrupp {haplogroup}.",
            "de": "ISOGG Y-DNA Tree dokumentiert die Äste und SNP-Mutationen der Haplogruppe {haplogroup}.",
            "fr": "L'arbre Y-ADN ISOGG documente les branches et les mutations SNP de l'haplogroupe {haplogroup}.",
            "es": "El árbol ADN-Y de ISOGG documenta las ramas y mutaciones SNP del haplogrupo {haplogroup}.",
            "pt": "A Árvore DNA-Y do ISOGG documenta as ramificações e mutações SNP do haplogrupo {haplogroup}.",
            "it": "L'albero Y-DNA ISOGG documenta i rami e le mutazioni SNP dell'aplogruppo {haplogroup}.",
            "ru": "ISOGG Y-DNA Tree документирует ветви и SNP-мутации гаплогруппы {haplogroup}.",
            "zh": "ISOGG Y-DNA 树记录了单倍群 {haplogroup} 的分支和 SNP 突变。",
            "ja": "ISOGG Y-DNA ツリーはハプログループ {haplogroup} の分岐と SNP 変異を記録しています。",
            "ko": "ISOGG Y-DNA 트리는 하플로그룹 {haplogroup}의 분기와 SNP 변이를 기록합니다.",
            "tr": "ISOGG Y-DNA Ağacı, {haplogroup} haplogrubunun dallarını ve SNP mutasyonlarını belgeler.",
            "pl": "Drzewo Y-DNA ISOGG dokumentuje gałęzie i mutacje SNP haplogrupy {haplogroup}.",
            "uk": "Дерево Y-ДНК ISOGG документує гілки та SNP-мутації гаплогрупи {haplogroup}.",
        },
        "source_familytreedna": {
            "fi": "FamilyTreeDNA-projektit kartoittavat haploryhmän {haplogroup} nykyaikaisia ja historiallisia haaroja.",
            "en": "FamilyTreeDNA projects map the modern and historical branches of haplogroup {haplogroup}.",
            "de": "FamilyTreeDNA-Projekte kartieren die modernen und historischen Äste der Haplogruppe {haplogroup}.",
            "fr": "Les projets FamilyTreeDNA cartographient les branches modernes et historiques de l'haplogroupe {haplogroup}.",
            "es": "Los proyectos de FamilyTreeDNA mapean las ramas modernas e históricas del haplogrupo {haplogroup}.",
            "ru": "Проекты FamilyTreeDNA картируют современные и исторические ветви гаплогруппы {haplogroup}.",
            "zh": "FamilyTreeDNA 项目绘制单倍群 {haplogroup} 的现代和历史分支图谱。",
            "ja": "FamilyTreeDNA プロジェクトはハプログループ {haplogroup} の現代・歴史的分岐をマッピングします。",
            "ko": "FamilyTreeDNA 프로젝트는 하플로그룹 {haplogroup}의 현대 및 역사적 분기를 매핑합니다.",
            "tr": "FamilyTreeDNA projeleri {haplogroup} haplogrubunun modern ve tarihsel dallarını haritalandırır.",
            "pl": "Projekty FamilyTreeDNA mapują nowoczesne i historyczne gałęzie haplogrupy {haplogroup}.",
            "uk": "Проєкти FamilyTreeDNA картують сучасні та історичні гілки гаплогрупи {haplogroup}.",
        },
        "source_haplogrep": {
            "fi": "Haplogrep tarjoaa filogeneettisen luokittelun ja haploryhmäennusteet haploryhmälle {haplogroup}.",
            "en": "Haplogrep provides phylogenetic classification and haplogroup predictions for {haplogroup}.",
            "de": "Haplogrep bietet phylogenetische Klassifizierung und Haplogruppen-Vorhersagen für {haplogroup}.",
            "fr": "Haplogrep fournit une classification phylogénétique et des prédictions de haplogroupe pour {haplogroup}.",
            "es": "Haplogrep ofrece clasificación filogenética y predicciones de haplogrupo para {haplogroup}.",
            "ru": "Haplogrep обеспечивает филогенетическую классификацию и предсказания гаплогрупп для {haplogroup}.",
            "zh": "Haplogrep 为 {haplogroup} 提供系统发育分类和单倍群预测。",
            "ja": "Haplogrep は {haplogroup} の系統的分類とハプログループ予測を提供します。",
            "ko": "Haplogrep은 {haplogroup}에 대한 계통 분류와 하플로그룹 예측을 제공합니다.",
            "tr": "Haplogrep, {haplogroup} için filogenetik sınıflandırma ve haplogrubu tahminleri sunar.",
            "pl": "Haplogrep zapewnia klasyfikację filogenetyczną i prognozy haplogrup dla {haplogroup}.",
            "uk": "Haplogrep забезпечує філогенетичну класифікацію та прогнози гаплогруп для {haplogroup}.",
        },
        "source_eupedia": {
            "fi": "Eupedia kuvaa haploryhmän {haplogroup} historiallista levinneisyyttä ja kulttuuriyhteyksiä.",
            "en": "Eupedia describes the historical distribution and cultural connections of haplogroup {haplogroup}.",
            "de": "Eupedia beschreibt die historische Verbreitung und kulturellen Verbindungen der Haplogruppe {haplogroup}.",
            "fr": "Eupedia décrit la distribution historique et les connexions culturelles de l'haplogroupe {haplogroup}.",
            "es": "Eupedia describe la distribución histórica y las conexiones culturales del haplogrupo {haplogroup}.",
            "ru": "Eupedia описывает историческое распространение и культурные связи гаплогруппы {haplogroup}.",
            "zh": "Eupedia 描述单倍群 {haplogroup} 的历史分布和文化联系。",
            "ja": "Eupedia はハプログループ {haplogroup} の歴史的分布と文化的つながりを説明します。",
            "ko": "Eupedia는 하플로그룹 {haplogroup}의 역사적 분포와 문화적 연결을 설명합니다.",
            "tr": "Eupedia, {haplogroup} haplogrubunun tarihsel dağılımını ve kültürel bağlantılarını açıklar.",
            "pl": "Eupedia opisuje historyczny zasięg i powiązania kulturowe haplogrupy {haplogroup}.",
            "uk": "Eupedia описує історичне поширення та культурні зв'язки гаплогрупи {haplogroup}.",
        },
        "source_geni": {
            "fi": "Geni yhdistää sukupuita haploryhmäpohjaisesti haploryhmälle {haplogroup}.",
            "en": "Geni connects family trees using haplogroup-based matching for {haplogroup}.",
            "de": "Geni verbindet Stammbäume auf Basis von Haplogruppen für {haplogroup}.",
            "fr": "Geni connecte les arbres généalogiques sur la base des haplogroupes pour {haplogroup}.",
            "es": "Geni conecta árboles genealógicos basándose en haplogrupos para {haplogroup}.",
            "ru": "Geni соединяет семейные деревья на основе гаплогрупп для {haplogroup}.",
            "zh": "Geni 基于单倍群 {haplogroup} 连接家族树。",
            "ja": "Geni はハプログループ {haplogroup} に基づいて家系図をつなげます。",
            "ko": "Geni는 {haplogroup} 기반 하플로그룹 매칭으로 가계도를 연결합니다.",
            "tr": "Geni, {haplogroup} haplogrubu tabanlı eşleştirme kullanarak aile ağaçlarını bağlar.",
            "pl": "Geni łączy drzewa genealogiczne na podstawie haplogrupy {haplogroup}.",
            "uk": "Geni з'єднує родовідні дерева на основі гаплогрупи {haplogroup}.",
        },
        "source_ancientdna_info": {
            "fi": "AncientDNA-arkistot sisältävät muinaisnäytteitä haploryhmälle {haplogroup}, joita voidaan verrata moderniin DNA:han.",
            "en": "AncientDNA archives contain ancient samples for haplogroup {haplogroup} that can be compared to modern DNA.",
            "de": "AncientDNA-Archive enthalten antike Proben für Haplogruppe {haplogroup}, die mit modernem DNA verglichen werden können.",
            "fr": "Les archives AncientDNA contiennent des échantillons anciens pour l'haplogroupe {haplogroup}, comparables à l'ADN moderne.",
            "es": "Los archivos AncientDNA contienen muestras antiguas del haplogrupo {haplogroup} comparables con el ADN moderno.",
            "ru": "Архивы AncientDNA содержат древние образцы гаплогруппы {haplogroup}, сравнимые с современной ДНК.",
            "zh": "AncientDNA 档案库含有单倍群 {haplogroup} 的古代样本，可与现代 DNA 比对。",
            "ja": "AncientDNA アーカイブには、ハプログループ {haplogroup} の古代サンプルが含まれており、現代 DNA と比較できます。",
            "ko": "AncientDNA 아카이브에는 하플로그룹 {haplogroup}의 고대 샘플이 포함되어 있어 현대 DNA와 비교할 수 있습니다.",
            "tr": "AncientDNA arşivleri, {haplogroup} haplogrubu için modern DNA ile karşılaştırılabilecek eski örnekler içerir.",
            "pl": "Archiwa AncientDNA zawierają starożytne próbki haplogrupy {haplogroup} możliwe do porównania z nowoczesnym DNA.",
            "uk": "Архіви AncientDNA містять стародавні зразки гаплогрупи {haplogroup}, які можна порівняти з сучасною ДНК.",
        },
        "source_ena": {
            "fi": "European Nucleotide Archive tarjoaa raakadataa muinaisille ja moderneille {haplogroup}-näytteille.",
            "en": "European Nucleotide Archive provides raw data for ancient and modern {haplogroup} samples.",
            "de": "Das European Nucleotide Archive bietet Rohdaten für antike und moderne {haplogroup}-Proben.",
            "fr": "L'European Nucleotide Archive fournit des données brutes pour les échantillons anciens et modernes de {haplogroup}.",
            "es": "El European Nucleotide Archive proporciona datos brutos para muestras antiguas y modernas de {haplogroup}.",
            "ru": "European Nucleotide Archive предоставляет исходные данные для древних и современных образцов {haplogroup}.",
            "zh": "European Nucleotide Archive 为 {haplogroup} 的古代和现代样本提供原始数据。",
            "ja": "European Nucleotide Archive は {haplogroup} の古代・現代サンプルの生データを提供します。",
            "ko": "European Nucleotide Archive는 {haplogroup}의 고대 및 현대 샘플 원시 데이터를 제공합니다.",
            "tr": "European Nucleotide Archive, {haplogroup} için eski ve modern örneklere ait ham veri sağlar.",
            "pl": "European Nucleotide Archive dostarcza surowe dane dla starożytnych i nowoczesnych próbek {haplogroup}.",
            "uk": "European Nucleotide Archive надає вихідні дані для стародавніх та сучасних зразків {haplogroup}.",
        },
        "source_pubmed_count": {
            "fi": "PubMedissä on tunnistettu {count} tutkimusta haploryhmään {haplogroup} liittyen.",
            "en": "PubMed has identified {count} studies related to haplogroup {haplogroup}.",
            "sv": "PubMed har identifierat {count} studier relaterade till haplogrupp {haplogroup}.",
            "de": "PubMed hat {count} Studien zur Haplogruppe {haplogroup} identifiziert.",
            "fr": "PubMed a identifié {count} études liées à l'haplogroupe {haplogroup}.",
            "es": "PubMed ha identificado {count} estudios relacionados con el haplogrupo {haplogroup}.",
            "pt": "O PubMed identificou {count} estudos relacionados ao haplogrupo {haplogroup}.",
            "it": "PubMed ha identificato {count} studi relativi all'aplogruppo {haplogroup}.",
            "ru": "PubMed выявил {count} исследований по гаплогруппе {haplogroup}.",
            "zh": "PubMed 已确认 {count} 篇与单倍群 {haplogroup} 相关的研究。",
            "ja": "PubMed はハプログループ {haplogroup} に関連する {count} 件の研究を確認しました。",
            "ko": "PubMed는 하플로그룹 {haplogroup}과 관련된 {count}개의 연구를 확인했습니다.",
            "ar": "حدّد PubMed {count} دراسة تتعلق بالمجموعة {haplogroup}.",
            "he": "PubMed זיהה {count} מחקרים הקשורים לקבוצה {haplogroup}.",
            "tr": "PubMed, {haplogroup} haplogrubuyla ilgili {count} çalışma tespit etti.",
            "pl": "PubMed zidentyfikował {count} badań dotyczących haplogrupy {haplogroup}.",
            "uk": "PubMed виявив {count} досліджень щодо гаплогрупи {haplogroup}.",
        },
        "source_russian_academic": {
            "fi": "Venäläiset tutkimukset dokumentoivat haploryhmän {haplogroup} esiintymistä Siperiassa, Volgalla ja Kaukasuksella.",
            "en": "Russian academic sources document haplogroup {haplogroup} in Siberia, the Volga region, and the Caucasus.",
            "de": "Russische Quellen dokumentieren die Haplogruppe {haplogroup} in Sibirien, an der Wolga und im Kaukasus.",
            "fr": "Les sources académiques russes documentent le haplogroupe {haplogroup} en Sibérie, dans la région de la Volga et dans le Caucase.",
            "es": "Fuentes académicas rusas documentan el haplogrupo {haplogroup} en Siberia, la región del Volga y el Cáucaso.",
            "ru": "Российские академические источники документируют гаплогруппу {haplogroup} в Сибири, Поволжье и на Кавказе.",
            "zh": "俄罗斯学术来源记录了单倍群 {haplogroup} 在西伯利亚、伏尔加地区和高加索的分布。",
            "ja": "ロシアの学術情報源はシベリア、ヴォルガ地域、コーカサスにおけるハプログループ {haplogroup} を記録しています。",
            "ko": "러시아 학술 자료는 시베리아, 볼가 지역, 코카서스의 하플로그룹 {haplogroup}을 기록합니다.",
            "tr": "Rus akademik kaynaklar, Sibirya, Volga bölgesi ve Kafkasya'daki {haplogroup} haplogrubunu belgelemektedir.",
            "uk": "Російські академічні джерела документують гаплогрупу {haplogroup} у Сибіру, Поволжі та на Кавказі.",
        },
        "source_eurasian_archaeogenetics": {
            "fi": "Euraasialaiset tutkimukset liittävät haploryhmän {haplogroup} aroalueiden ja paimentolaiskulttuurien liikkeisiin.",
            "en": "Eurasian archaeogenetics links haplogroup {haplogroup} to steppe populations and nomadic culture movements.",
            "de": "Eurasische Archäogenetik verknüpft Haplogruppe {haplogroup} mit Steppenpopulationen und nomadischen Kulturzügen.",
            "fr": "L'archéogénétique eurasienne relie l'haplogroupe {haplogroup} aux populations des steppes et aux mouvements culturels nomades.",
            "es": "La arqueogenética euroasiática vincula el haplogrupo {haplogroup} con las poblaciones de las estepas y los movimientos nómadas.",
            "ru": "Евразийская археогенетика связывает гаплогруппу {haplogroup} со степными популяциями и кочевыми культурами.",
            "zh": "欧亚考古遗传学将单倍群 {haplogroup} 与草原人群及游牧文化的迁移联系起来。",
            "ja": "ユーラシア考古遺伝学はハプログループ {haplogroup} をステップ集団と遊牧文化の移動に結びつけています。",
            "ko": "유라시아 고고유전학은 하플로그룹 {haplogroup}을 스텝 집단과 유목 문화 이동에 연결합니다.",
            "tr": "Avrasya arkeogenetiği, {haplogroup} haplogrubunu step popülasyonları ve göçebe kültür hareketleriyle ilişkilendirir.",
            "uk": "Євразійська археогенетика пов'язує гаплогрупу {haplogroup} зі степовими популяціями та кочовими культурами.",
        },
        "source_middle_east_archaeogenetics": {
            "fi": "Lähi-idän arkeogenetiikka yhdistää haploryhmän {haplogroup} varhaisiin maanviljelijöihin ja kauppaverkostoihin.",
            "en": "Middle Eastern archaeogenetics connects haplogroup {haplogroup} to early farmers and trade networks.",
            "de": "Nahöstliche Archäogenetik verbindet Haplogruppe {haplogroup} mit frühen Bauern und Handelsnetzwerken.",
            "fr": "L'archéogénétique du Moyen-Orient relie l'haplogroupe {haplogroup} aux premiers agriculteurs et aux réseaux commerciaux.",
            "es": "La arqueogenética de Oriente Medio vincula el haplogrupo {haplogroup} con los primeros agricultores y redes comerciales.",
            "ru": "Ближневосточная археогенетика связывает гаплогруппу {haplogroup} с ранними земледельцами и торговыми сетями.",
            "zh": "中东考古遗传学将单倍群 {haplogroup} 与早期农民和贸易网络联系起来。",
            "ja": "中東考古遺伝学はハプログループ {haplogroup} を初期農民と交易網に結びつけています。",
            "ko": "중동 고고유전학은 하플로그룹 {haplogroup}을 초기 농경민과 교역망에 연결합니다.",
            "tr": "Orta Doğu arkeogenetiği, {haplogroup} haplogrubunu erken çiftçiler ve ticaret ağlarıyla ilişkilendirir.",
            "uk": "Близькосхідна археогенетика пов'язує гаплогрупу {haplogroup} з ранніми землеробами та торговельними мережами.",
        },
        "source_south_asian_archaeogenetics": {
            "fi": "Etelä-Aasian tutkimukset liittävät haploryhmän {haplogroup} Indus-laakson ja aroliikkeiden vuorovaikutukseen.",
            "en": "South Asian archaeogenetics connects haplogroup {haplogroup} to Indus Valley and steppe interaction.",
            "de": "Südasiatische Archäogenetik verbindet Haplogruppe {haplogroup} mit dem Indus-Tal und der Steppen-Interaktion.",
            "fr": "L'archéogénétique sud-asiatique relie l'haplogroupe {haplogroup} à la vallée de l'Indus et aux interactions avec les steppes.",
            "es": "La arqueogenética del sur de Asia vincula el haplogrupo {haplogroup} con el valle del Indo y la interacción con las estepas.",
            "ru": "Южноазиатская археогенетика связывает гаплогруппу {haplogroup} с долиной Инда и степными взаимодействиями.",
            "zh": "南亚考古遗传学将单倍群 {haplogroup} 与印度河流域及草原的相互作用联系起来。",
            "ja": "南アジア考古遺伝学はハプログループ {haplogroup} をインダス渓谷とステップの相互作用に結びつけています。",
            "ko": "남아시아 고고유전학은 하플로그룹 {haplogroup}을 인더스 계곡과 스텝 상호작용에 연결합니다.",
            "tr": "Güney Asya arkeogenetiği, {haplogroup} haplogrubunu İndus Vadisi ve step etkileşimiyle ilişkilendirir.",
            "uk": "Південноазійська археогенетика пов'язує гаплогрупу {haplogroup} з долиною Інду та степовою взаємодією.",
        },
        # Alueelliset lähteet — lyhyempi kattavuus (fi+en+de+fr+es+ru+zh+ja+ko+tr+pl+uk)
        "source_chinese_genomics": {
            "fi": "Kiinalaiset genomitietokannat dokumentoivat haploryhmän {haplogroup} esiintymistä Itä- ja Keski-Aasiassa.",
            "en": "Chinese genomic databases document haplogroup {haplogroup} in East and Central Asia.",
            "de": "Chinesische Genomdatenbanken dokumentieren Haplogruppe {haplogroup} in Ost- und Zentralasien.",
            "fr": "Les bases de données génomiques chinoises documentent l'haplogroupe {haplogroup} en Asie orientale et centrale.",
            "es": "Las bases de datos genómicas chinas documentan el haplogrupo {haplogroup} en Asia oriental y central.",
            "ru": "Китайские геномные базы данных документируют гаплогруппу {haplogroup} в Восточной и Центральной Азии.",
            "zh": "中国基因组数据库记录了单倍群 {haplogroup} 在东亚和中亚的分布。",
            "ja": "中国のゲノムデータベースは東アジアと中央アジアにおけるハプログループ {haplogroup} を記録しています。",
            "ko": "중국 유전체 데이터베이스는 동아시아와 중앙아시아의 하플로그룹 {haplogroup}을 기록합니다.",
            "tr": "Çin genomik veri tabanları, {haplogroup} haplogrubunu Doğu ve Orta Asya'da belgelemektedir.",
            "uk": "Китайські геномні бази даних документують гаплогрупу {haplogroup} у Східній і Центральній Азії.",
        },
        "source_korean_genomics": {
            "fi": "Korean genomitutkimukset osoittavat haploryhmän {haplogroup} esiintymistä Korean niemimaalla.",
            "en": "Korean genomic research documents haplogroup {haplogroup} on the Korean Peninsula.",
            "de": "Koreanische Genomforschung dokumentiert Haplogruppe {haplogroup} auf der koreanischen Halbinsel.",
            "fr": "La recherche génomique coréenne documente l'haplogroupe {haplogroup} sur la péninsule coréenne.",
            "es": "La investigación genómica coreana documenta el haplogrupo {haplogroup} en la península coreana.",
            "ru": "Корейские геномные исследования документируют гаплогруппу {haplogroup} на Корейском полуострове.",
            "zh": "韩国基因组研究记录了朝鲜半岛的单倍群 {haplogroup}。",
            "ja": "韓国のゲノム研究は朝鮮半島におけるハプログループ {haplogroup} を記録しています。",
            "ko": "한국 유전체 연구는 한반도의 하플로그룹 {haplogroup}을 기록합니다.",
            "tr": "Kore genomik araştırmaları, Kore Yarımadası'ndaki {haplogroup} haplogrubunu belgelemektedir.",
            "uk": "Корейські геномні дослідження документують гаплогрупу {haplogroup} на Корейському півострові.",
        },
        "source_japanese_genomics": {
            "fi": "Japanilaiset genomitutkimukset liittävät haploryhmän {haplogroup} Jōmon- ja Yayoi-populaatioihin.",
            "en": "Japanese genomic research links haplogroup {haplogroup} to Jōmon and Yayoi populations.",
            "de": "Japanische Genomforschung verknüpft Haplogruppe {haplogroup} mit Jōmon- und Yayoi-Populationen.",
            "fr": "La recherche génomique japonaise relie l'haplogroupe {haplogroup} aux populations Jōmon et Yayoi.",
            "es": "La investigación genómica japonesa vincula el haplogrupo {haplogroup} con las poblaciones Jōmon y Yayoi.",
            "ru": "Японские геномные исследования связывают гаплогруппу {haplogroup} с популяциями Дзёмон и Яёй.",
            "zh": "日本基因组研究将单倍群 {haplogroup} 与绳文和弥生人群联系起来。",
            "ja": "日本のゲノム研究はハプログループ {haplogroup} を縄文・弥生集団と結びつけています。",
            "ko": "일본 유전체 연구는 하플로그룹 {haplogroup}을 조몬 및 야요이 집단과 연결합니다.",
            "tr": "Japon genomik araştırmaları, {haplogroup} haplogrubunu Jōmon ve Yayoi popülasyonlarıyla ilişkilendirir.",
            "uk": "Японські геномні дослідження пов'язують гаплогрупу {haplogroup} з популяціями Дзьомон і Яєй.",
        },
        "source_southeast_asian_archaeogenetics": {
            "fi": "Kaakkois-Aasian tutkimukset yhdistävät haploryhmän {haplogroup} varhaisiin merellisiin verkostoihin.",
            "en": "Southeast Asian archaeogenetics connects haplogroup {haplogroup} to early maritime networks.",
            "de": "Südostasiatische Archäogenetik verbindet Haplogruppe {haplogroup} mit frühen maritimen Netzwerken.",
            "fr": "L'archéogénétique d'Asie du Sud-Est relie l'haplogroupe {haplogroup} aux premiers réseaux maritimes.",
            "es": "La arqueogenética del sudeste asiático vincula el haplogrupo {haplogroup} con las primeras redes marítimas.",
            "ru": "Юго-восточноазиатская археогенетика связывает гаплогруппу {haplogroup} с ранними морскими сетями.",
            "zh": "东南亚考古遗传学将单倍群 {haplogroup} 与早期海洋网络联系起来。",
            "ja": "東南アジア考古遺伝学はハプログループ {haplogroup} を初期の海洋ネットワークに結びつけています。",
            "ko": "동남아시아 고고유전학은 하플로그룹 {haplogroup}을 초기 해양 네트워크에 연결합니다.",
            "tr": "Güneydoğu Asya arkeogenetiği, {haplogroup} haplogrubunu erken deniz ağlarıyla ilişkilendirir.",
            "uk": "Археогенетика Південно-Східної Азії пов'язує гаплогрупу {haplogroup} з ранніми морськими мережами.",
        },
        "source_african_archaeogenetics": {
            "fi": "Afrikan arkeogenetiikka dokumentoi haploryhmän {haplogroup} varhaisimmat juuret ja levinneisyyden.",
            "en": "African archaeogenetics documents the earliest roots and distribution of haplogroup {haplogroup}.",
            "de": "Afrikanische Archäogenetik dokumentiert die frühesten Wurzeln und die Verbreitung der Haplogruppe {haplogroup}.",
            "fr": "L'archéogénétique africaine documente les racines les plus anciennes et la distribution de l'haplogroupe {haplogroup}.",
            "es": "La arqueogenética africana documenta las raíces más antiguas y la distribución del haplogrupo {haplogroup}.",
            "ru": "Африканская археогенетика документирует древнейшие корни и распространение гаплогруппы {haplogroup}.",
            "zh": "非洲考古遗传学记录了单倍群 {haplogroup} 最早的根源和分布。",
            "ja": "アフリカ考古遺伝学はハプログループ {haplogroup} の最古の起源と分布を記録しています。",
            "ko": "아프리카 고고유전학은 하플로그룹 {haplogroup}의 가장 오래된 기원과 분포를 기록합니다.",
            "tr": "Afrika arkeogenetiği, {haplogroup} haplogrubunun en eski köklerini ve dağılımını belgelemektedir.",
            "uk": "Африканська археогенетика документує найдавніші корені та поширення гаплогрупи {haplogroup}.",
        },
        "source_north_african_archaeogenetics": {
            "fi": "Pohjois-Afrikan tutkimukset yhdistävät haploryhmän {haplogroup} Välimeren ja Saharan verkostoihin.",
            "en": "North African archaeogenetics connects haplogroup {haplogroup} to Mediterranean and Saharan networks.",
            "de": "Nordafrikanische Archäogenetik verbindet Haplogruppe {haplogroup} mit Mittelmeernetzwerken und Sahara-Netzwerken.",
            "fr": "L'archéogénétique nord-africaine relie l'haplogroupe {haplogroup} aux réseaux méditerranéens et sahariens.",
            "es": "La arqueogenética norteafricana vincula el haplogrupo {haplogroup} con redes mediterráneas y del Sahara.",
            "ru": "Североафриканская археогенетика связывает гаплогруппу {haplogroup} со средиземноморскими и сахарскими сетями.",
            "zh": "北非考古遗传学将单倍群 {haplogroup} 与地中海和撒哈拉网络联系起来。",
            "ja": "北アフリカ考古遺伝学はハプログループ {haplogroup} を地中海とサハラのネットワークに結びつけています。",
            "ko": "북아프리카 고고유전학은 하플로그룹 {haplogroup}을 지중해 및 사하라 네트워크에 연결합니다.",
            "tr": "Kuzey Afrika arkeogenetiği, {haplogroup} haplogrubunu Akdeniz ve Sahra ağlarıyla ilişkilendirir.",
            "uk": "Північноафриканська археогенетика пов'язує гаплогрупу {haplogroup} із середземноморськими та сахарськими мережами.",
        },
        "source_subsaharan_archaeogenetics": {
            "fi": "Sub-Saharan Afrikan tutkimukset liittävät haploryhmän {haplogroup} Bantu-laajenemiseen ja varhaisiin metsästäjä-keräilijöihin.",
            "en": "Sub-Saharan African archaeogenetics links haplogroup {haplogroup} to the Bantu expansion and early hunter-gatherers.",
            "de": "Subsaharische Archäogenetik verbindet Haplogruppe {haplogroup} mit der Bantu-Expansion und frühen Jägern und Sammlern.",
            "fr": "L'archéogénétique d'Afrique subsaharienne relie l'haplogroupe {haplogroup} à l'expansion bantoue et aux premiers chasseurs-cueilleurs.",
            "es": "La arqueogenética subsahariana vincula el haplogrupo {haplogroup} con la expansión bantú y los primeros cazadores-recolectores.",
            "ru": "Субсахарская африканская археогенетика связывает гаплогруппу {haplogroup} с экспансией Банту и ранними охотниками-собирателями.",
            "zh": "撒哈拉以南非洲考古遗传学将单倍群 {haplogroup} 与班图扩张和早期狩猎采集者联系起来。",
            "ja": "サハラ以南のアフリカ考古遺伝学はハプログループ {haplogroup} をバンツー拡張と初期の狩猟採集民に結びつけています。",
            "ko": "사하라 이남 아프리카 고고유전학은 하플로그룹 {haplogroup}을 반투 팽창과 초기 수렵채집인에 연결합니다.",
            "tr": "Sahra Altı Afrika arkeogenetiği, {haplogroup} haplogrubunu Bantu genişlemesi ve erken avcı-toplayıcılarla ilişkilendirir.",
            "uk": "Субсахарська африканська археогенетика пов'язує гаплогрупу {haplogroup} з розширенням банту та ранніми мисливцями-збирачами.",
        },
        "source_native_american_archaeogenetics": {
            "fi": "Pohjois-Amerikan alkuperäiskansojen tutkimukset yhdistävät haploryhmän {haplogroup} Beringian reitteihin.",
            "en": "Native American archaeogenetics connects haplogroup {haplogroup} to Beringian migration routes.",
            "de": "Indianische Archäogenetik verbindet Haplogruppe {haplogroup} mit beringischen Migrationsrouten.",
            "fr": "L'archéogénétique amérindienne relie l'haplogroupe {haplogroup} aux routes de migration béringiennes.",
            "es": "La arqueogenética de los nativos americanos vincula el haplogrupo {haplogroup} con las rutas de migración por Beringia.",
            "ru": "Индейская археогенетика связывает гаплогруппу {haplogroup} с берингийскими маршрутами миграции.",
            "zh": "北美原住民考古遗传学将单倍群 {haplogroup} 与白令路桥迁徙路线联系起来。",
            "ja": "アメリカ先住民考古遺伝学はハプログループ {haplogroup} をベーリング移住ルートに結びつけています。",
            "ko": "아메리카 원주민 고고유전학은 하플로그룹 {haplogroup}을 베링 이주 경로에 연결합니다.",
            "tr": "Kızılderili arkeogenetiği, {haplogroup} haplogrubunu Beringian göç güzergahlarıyla ilişkilendirir.",
            "uk": "Індіанська археогенетика пов'язує гаплогрупу {haplogroup} з берингійськими маршрутами міграції.",
        },
        "source_south_american_archaeogenetics": {
            "fi": "Etelä-Amerikan tutkimukset liittävät haploryhmän {haplogroup} Andien ja Amazonian kulttuureihin.",
            "en": "South American archaeogenetics links haplogroup {haplogroup} to Andean and Amazonian cultures.",
            "de": "Südamerikanische Archäogenetik verbindet Haplogruppe {haplogroup} mit andinen und amazonischen Kulturen.",
            "fr": "L'archéogénétique sud-américaine relie l'haplogroupe {haplogroup} aux cultures andines et amazoniennes.",
            "es": "La arqueogenética sudamericana vincula el haplogrupo {haplogroup} con las culturas andinas y amazónicas.",
            "ru": "Южноамериканская археогенетика связывает гаплогруппу {haplogroup} с андской и амазонской культурами.",
            "zh": "南美考古遗传学将单倍群 {haplogroup} 与安第斯和亚马孙文化联系起来。",
            "ja": "南米考古遺伝学はハプログループ {haplogroup} をアンデスとアマゾン文化に結びつけています。",
            "ko": "남아메리카 고고유전학은 하플로그룹 {haplogroup}을 안데스 및 아마존 문화에 연결합니다.",
            "tr": "Güney Amerika arkeogenetiği, {haplogroup} haplogrubunu And ve Amazon kültürleriyle ilişkilendirir.",
            "uk": "Південноамериканська археогенетика пов'язує гаплогрупу {haplogroup} з андськими та амазонськими культурами.",
        },
        "source_caribbean_archaeogenetics": {
            "fi": "Karibian tutkimukset yhdistävät haploryhmän {haplogroup} Taino- ja Arawak-kulttuureihin.",
            "en": "Caribbean archaeogenetics connects haplogroup {haplogroup} to Taíno and Arawak cultures.",
            "de": "Karibische Archäogenetik verbindet Haplogruppe {haplogroup} mit Taíno- und Arawak-Kulturen.",
            "fr": "L'archéogénétique caribéenne relie l'haplogroupe {haplogroup} aux cultures Taïno et Arawak.",
            "es": "La arqueogenética caribeña vincula el haplogrupo {haplogroup} con las culturas taíno y arawak.",
            "ru": "Карибская археогенетика связывает гаплогруппу {haplogroup} с культурами таино и аравак.",
            "zh": "加勒比考古遗传学将单倍群 {haplogroup} 与泰诺和阿拉瓦克文化联系起来。",
            "ja": "カリブ考古遺伝学はハプログループ {haplogroup} をタイノとアラワク文化に結びつけています。",
            "ko": "카리브해 고고유전학은 하플로그룹 {haplogroup}을 타이노 및 아라와크 문화에 연결합니다.",
            "tr": "Karayip arkeogenetiği, {haplogroup} haplogrubunu Taíno ve Arawak kültürleriyle ilişkilendirir.",
            "uk": "Карибська археогенетика пов'язує гаплогрупу {haplogroup} з культурами таїно та аравак.",
        },
        "source_arctic_archaeogenetics": {
            "fi": "Arktiset tutkimukset liittävät haploryhmän {haplogroup} paleo-eskimoihin ja inuiittikulttuureihin.",
            "en": "Arctic archaeogenetics links haplogroup {haplogroup} to Paleo-Eskimos and Inuit cultures.",
            "de": "Arktische Archäogenetik verbindet Haplogruppe {haplogroup} mit Paläo-Eskimos und Inuit-Kulturen.",
            "fr": "L'archéogénétique arctique relie l'haplogroupe {haplogroup} aux Paléo-Esquimaux et aux cultures inuites.",
            "es": "La arqueogenética ártica vincula el haplogrupo {haplogroup} con los Paleo-esquimales y las culturas inuit.",
            "ru": "Арктическая археогенетика связывает гаплогруппу {haplogroup} с палео-эскимосами и культурами инуитов.",
            "zh": "北极考古遗传学将单倍群 {haplogroup} 与古爱斯基摩人和因纽特文化联系起来。",
            "ja": "北極考古遺伝学はハプログループ {haplogroup} を古代エスキモーとイヌイット文化に結びつけています。",
            "ko": "북극 고고유전학은 하플로그룹 {haplogroup}을 고대 에스키모와 이누이트 문화에 연결합니다.",
            "tr": "Arktik arkeogenetik, {haplogroup} haplogrubunu Paleo-Eskimolar ve Inuit kültürleriyle ilişkilendirir.",
            "uk": "Арктична археогенетика пов'язує гаплогрупу {haplogroup} з палео-ескімосами та культурами інуїтів.",
        },
        "source_australian_archaeogenetics": {
            "fi": "Australian tutkimukset liittävät haploryhmän {haplogroup} varhaisiin Sahul-alueen populaatioihin.",
            "en": "Australian archaeogenetics links haplogroup {haplogroup} to early Sahul populations.",
            "de": "Australische Archäogenetik verbindet Haplogruppe {haplogroup} mit frühen Sahul-Populationen.",
            "fr": "L'archéogénétique australienne relie l'haplogroupe {haplogroup} aux premières populations de Sahul.",
            "es": "La arqueogenética australiana vincula el haplogrupo {haplogroup} con las poblaciones tempranas de Sahul.",
            "ru": "Австралийская археогенетика связывает гаплогруппу {haplogroup} с ранними популяциями Сахула.",
            "zh": "澳大利亚考古遗传学将单倍群 {haplogroup} 与早期萨胡尔人群联系起来。",
            "ja": "オーストラリア考古遺伝学はハプログループ {haplogroup} を初期サフール集団に結びつけています。",
            "ko": "호주 고고유전학은 하플로그룹 {haplogroup}을 초기 사훌 집단에 연결합니다.",
            "tr": "Avustralya arkeogenetiği, {haplogroup} haplogrubunu erken Sahul popülasyonlarıyla ilişkilendirir.",
            "uk": "Австралійська археогенетика пов'язує гаплогрупу {haplogroup} з ранніми популяціями Сагулу.",
        },
        "source_polynesian_archaeogenetics": {
            "fi": "Polynesian tutkimukset yhdistävät haploryhmän {haplogroup} austronesialaiseen laajenemiseen.",
            "en": "Polynesian archaeogenetics connects haplogroup {haplogroup} to the Austronesian expansion.",
            "de": "Polynesische Archäogenetik verbindet Haplogruppe {haplogroup} mit der austronesischen Expansion.",
            "fr": "L'archéogénétique polynésienne relie l'haplogroupe {haplogroup} à l'expansion austronésienne.",
            "es": "La arqueogenética polinesia vincula el haplogrupo {haplogroup} con la expansión austronesia.",
            "ru": "Полинезийская археогенетика связывает гаплогруппу {haplogroup} с австронезийской экспансией.",
            "zh": "波利尼西亚考古遗传学将单倍群 {haplogroup} 与南岛语族扩张联系起来。",
            "ja": "ポリネシア考古遺伝学はハプログループ {haplogroup} をオーストロネシア拡張に結びつけています。",
            "ko": "폴리네시아 고고유전학은 하플로그룹 {haplogroup}을 오스트로네시아 팽창에 연결합니다.",
            "tr": "Polinezya arkeogenetiği, {haplogroup} haplogrubunu Avustronezya genişlemesiyle ilişkilendirir.",
            "uk": "Полінезійська археогенетика пов'язує гаплогрупу {haplogroup} з австронезійською експансією.",
        },
        "source_melanesian_archaeogenetics": {
            "fi": "Melanesian tutkimukset liittävät haploryhmän {haplogroup} Sahulin ja Papuan varhaisiin väestöihin.",
            "en": "Melanesian archaeogenetics links haplogroup {haplogroup} to early Sahul and Papuan populations.",
            "de": "Melanesische Archäogenetik verbindet Haplogruppe {haplogroup} mit frühen Sahul- und Papua-Populationen.",
            "fr": "L'archéogénétique mélanésienne relie l'haplogroupe {haplogroup} aux premières populations de Sahul et de Papouasie.",
            "es": "La arqueogenética melanesia vincula el haplogrupo {haplogroup} con las primeras poblaciones de Sahul y Papúa.",
            "ru": "Меланезийская археогенетика связывает гаплогруппу {haplogroup} с ранними популяциями Сахула и Папуа.",
            "zh": "美拉尼西亚考古遗传学将单倍群 {haplogroup} 与早期萨胡尔和巴布亚人群联系起来。",
            "ja": "メラネシア考古遺伝学はハプログループ {haplogroup} を初期サフールとパプア集団に結びつけています。",
            "ko": "멜라네시아 고고유전학은 하플로그룹 {haplogroup}을 초기 사훌 및 파푸아 집단에 연결합니다.",
            "tr": "Melanezya arkeogenetiği, {haplogroup} haplogrubunu erken Sahul ve Papua popülasyonlarıyla ilişkilendirir.",
            "uk": "Меланезійська археогенетика пов'язує гаплогрупу {haplogroup} з ранніми популяціями Сагулу та Папуа.",
        },
        "source_micronesian_archaeogenetics": {
            "fi": "Mikronesian tutkimukset yhdistävät haploryhmän {haplogroup} merellisiin siirtoreitteihin Tyynellämerellä.",
            "en": "Micronesian archaeogenetics connects haplogroup {haplogroup} to Pacific maritime migration routes.",
            "de": "Mikronesische Archäogenetik verbindet Haplogruppe {haplogroup} mit pazifischen maritimen Migrationsrouten.",
            "fr": "L'archéogénétique micronésienne relie l'haplogroupe {haplogroup} aux routes de migration maritime dans le Pacifique.",
            "es": "La arqueogenética de Micronesia vincula el haplogrupo {haplogroup} con las rutas de migración marítima en el Pacífico.",
            "ru": "Микронезийская археогенетика связывает гаплогруппу {haplogroup} с тихоокеанскими морскими маршрутами миграции.",
            "zh": "密克罗尼西亚考古遗传学将单倍群 {haplogroup} 与太平洋海洋迁徙路线联系起来。",
            "ja": "ミクロネシア考古遺伝学はハプログループ {haplogroup} を太平洋の海洋移住ルートに結びつけています。",
            "ko": "미크로네시아 고고유전학은 하플로그룹 {haplogroup}을 태평양 해양 이주 경로에 연결합니다.",
            "tr": "Mikronezya arkeogenetiği, {haplogroup} haplogrubunu Pasifik denizcilik göç güzergahlarıyla ilişkilendirir.",
            "uk": "Мікронезійська археогенетика пов'язує гаплогрупу {haplogroup} з тихоокеанськими морськими маршрутами міграції.",
        },
        "source_new_zealand_archaeogenetics": {
            "fi": "Uuden-Seelannin tutkimukset liittävät haploryhmän {haplogroup} maorien esi-isiin.",
            "en": "New Zealand archaeogenetics links haplogroup {haplogroup} to Māori ancestors and the Polynesian expansion.",
            "de": "Neuseeländische Archäogenetik verbindet Haplogruppe {haplogroup} mit Māori-Vorfahren und der polynesischen Expansion.",
            "fr": "L'archéogénétique néo-zélandaise relie l'haplogroupe {haplogroup} aux ancêtres maori et à l'expansion polynésienne.",
            "es": "La arqueogenética de Nueva Zelanda vincula el haplogrupo {haplogroup} con los ancestros maorís y la expansión polinesia.",
            "ru": "Новозеландская археогенетика связывает гаплогруппу {haplogroup} с предками маори и полинезийской экспансией.",
            "zh": "新西兰考古遗传学将单倍群 {haplogroup} 与毛利祖先和波利尼西亚扩张联系起来。",
            "ja": "ニュージーランド考古遺伝学はハプログループ {haplogroup} をマオリの祖先とポリネシア拡張に結びつけています。",
            "ko": "뉴질랜드 고고유전학은 하플로그룹 {haplogroup}을 마오리 조상과 폴리네시아 팽창에 연결합니다.",
            "tr": "Yeni Zelanda arkeogenetiği, {haplogroup} haplogrubunu Maori ataları ve Polinezya genişlemesiyle ilişkilendirir.",
            "uk": "Новозеландська археогенетика пов'язує гаплогрупу {haplogroup} з предками маорі та полінезійською експансією.",
        },
        "source_indian_ocean_islands": {
            "fi": "Intian valtameren saarien tutkimukset yhdistävät haploryhmän {haplogroup} afrikkalaisiin, austronesialaisiin ja eteläaasialaisiin reitteihin.",
            "en": "Indian Ocean island research connects haplogroup {haplogroup} to African, Austronesian, and South Asian routes.",
            "de": "Forschung auf den Inseln des Indischen Ozeans verbindet Haplogruppe {haplogroup} mit afrikanischen, austronesischen und südasiatischen Routen.",
            "fr": "La recherche sur les îles de l'océan Indien relie l'haplogroupe {haplogroup} aux routes africaines, austronésiennes et sud-asiatiques.",
            "es": "La investigación en las islas del Océano Índico vincula el haplogrupo {haplogroup} con rutas africanas, austronesias y del sur de Asia.",
            "ru": "Исследования островов Индийского океана связывают гаплогруппу {haplogroup} с африканскими, австронезийскими и южноазиатскими маршрутами.",
            "zh": "印度洋岛屿研究将单倍群 {haplogroup} 与非洲、南岛和南亚路线联系起来。",
            "ja": "インド洋の島々の研究はハプログループ {haplogroup} をアフリカ、オーストロネシア、南アジアのルートに結びつけています。",
            "ko": "인도양 섬 연구는 하플로그룹 {haplogroup}을 아프리카, 오스트로네시아, 남아시아 경로에 연결합니다.",
            "tr": "Hint Okyanusu adaları araştırması, {haplogroup} haplogrubunu Afrika, Avustronezya ve Güney Asya güzergahlarıyla ilişkilendirir.",
            "uk": "Дослідження островів Індійського океану пов'язують гаплогрупу {haplogroup} з африканськими, австронезійськими та південноазійськими маршрутами.",
        },
        "source_north_atlantic_islands": {
            "fi": "Pohjois-Atlantin saarten tutkimukset yhdistävät haploryhmän {haplogroup} viikinkeihin ja varhaisiin merikulttuureihin.",
            "en": "North Atlantic island research connects haplogroup {haplogroup} to Viking and early maritime cultures.",
            "sv": "Forskning på Nordatlantens öar kopplar haplogrupp {haplogroup} till vikingarna och tidiga marina kulturer.",
            "de": "Forschung auf den Nordatlantik-Inseln verbindet Haplogruppe {haplogroup} mit Wikingern und frühen Seekulturen.",
            "fr": "La recherche sur les îles de l'Atlantique Nord relie l'haplogroupe {haplogroup} aux Vikings et aux premières cultures maritimes.",
            "es": "La investigación en las islas del Atlántico Norte vincula el haplogrupo {haplogroup} con los vikingos y las primeras culturas marítimas.",
            "ru": "Исследования островов Северной Атлантики связывают гаплогруппу {haplogroup} с викингами и ранними морскими культурами.",
            "zh": "北大西洋岛屿研究将单倍群 {haplogroup} 与维京人和早期海洋文化联系起来。",
            "ja": "北大西洋の島々の研究はハプログループ {haplogroup} をヴァイキングと初期の海洋文化に結びつけています。",
            "ko": "북대서양 섬 연구는 하플로그룹 {haplogroup}을 바이킹과 초기 해양 문화에 연결합니다.",
            "tr": "Kuzey Atlantik adaları araştırması, {haplogroup} haplogrubunu Vikingler ve erken denizcilik kültürleriyle ilişkilendirir.",
            "uk": "Дослідження островів Північної Атлантики пов'язують гаплогрупу {haplogroup} з вікінгами та ранніми морськими культурами.",
        },
        "source_raw_data_providers": {
            "fi": "Useat kaupalliset palvelut tarjoavat raakadataa arkeogeneettiseen analyysiin haploryhmälle {haplogroup}.",
            "en": "Several commercial services provide raw data for archaeogenetic analysis of haplogroup {haplogroup}.",
            "sv": "Flera kommersiella tjänster tillhandahåller rådata för arkeogenetisk analys av haplogrupp {haplogroup}.",
            "de": "Mehrere kommerzielle Dienste bieten Rohdaten für die archäogenetische Analyse der Haplogruppe {haplogroup}.",
            "fr": "Plusieurs services commerciaux fournissent des données brutes pour l'analyse archéogénétique de l'haplogroupe {haplogroup}.",
            "es": "Varios servicios comerciales proporcionan datos brutos para el análisis arqueogenético del haplogrupo {haplogroup}.",
            "pt": "Vários serviços comerciais fornecem dados brutos para análise arqueogenética do haplogrupo {haplogroup}.",
            "it": "Diversi servizi commerciali forniscono dati grezzi per l'analisi archeogenetica dell'aplogruppo {haplogroup}.",
            "ru": "Несколько коммерческих сервисов предоставляют исходные данные для археогенетического анализа гаплогруппы {haplogroup}.",
            "zh": "多家商业服务为单倍群 {haplogroup} 的考古遗传分析提供原始数据。",
            "ja": "いくつかの商業サービスがハプログループ {haplogroup} の考古遺伝分析用の生データを提供しています。",
            "ko": "여러 상업 서비스가 하플로그룹 {haplogroup}의 고고유전 분석을 위한 원시 데이터를 제공합니다.",
            "tr": "Çeşitli ticari hizmetler, {haplogroup} haplogrubunun arkeogenetik analizi için ham veri sağlamaktadır.",
            "pl": "Kilka komercyjnych serwisów dostarcza surowych danych do analizy archeogenetycznej haplogrupy {haplogroup}.",
            "uk": "Кілька комерційних сервісів надають вихідні дані для археогенетичного аналізу гаплогрупи {haplogroup}.",
        },
        "source_analysis_tools": {
            "fi": "Useat analyysialustat mahdollistavat muinais-DNA-vertailut ja populaatiomallinnuksen haploryhmälle {haplogroup}.",
            "en": "Several analysis platforms enable ancient DNA comparisons and population modelling for haplogroup {haplogroup}.",
            "sv": "Flera analysplattformar möjliggör jämförelser av forntida DNA och populationsmodellering för haplogrupp {haplogroup}.",
            "de": "Mehrere Analyseplattformen ermöglichen antike DNA-Vergleiche und Populationsmodellierung für Haplogruppe {haplogroup}.",
            "fr": "Plusieurs plateformes d'analyse permettent des comparaisons d'ADN ancien et la modélisation de populations pour l'haplogroupe {haplogroup}.",
            "es": "Varias plataformas de análisis permiten comparaciones de ADN antiguo y modelado de poblaciones para el haplogrupo {haplogroup}.",
            "pt": "Várias plataformas de análise permitem comparações de DNA antigo e modelagem de populações para o haplogrupo {haplogroup}.",
            "it": "Diverse piattaforme di analisi consentono confronti di DNA antico e modellazione di popolazioni per l'aplogruppo {haplogroup}.",
            "ru": "Несколько аналитических платформ позволяют проводить сравнения древней ДНК и моделирование популяций для гаплогруппы {haplogroup}.",
            "zh": "多个分析平台支持对单倍群 {haplogroup} 进行古代 DNA 比较和种群建模。",
            "ja": "複数の分析プラットフォームがハプログループ {haplogroup} の古代 DNA 比較と集団モデリングを可能にします。",
            "ko": "여러 분석 플랫폼이 하플로그룹 {haplogroup}의 고대 DNA 비교 및 인구 모델링을 가능하게 합니다.",
            "tr": "Çeşitli analiz platformları, {haplogroup} haplogrubu için eski DNA karşılaştırmaları ve popülasyon modellemesi yapılmasına olanak tanır.",
            "pl": "Kilka platform analitycznych umożliwia porównania starożytnego DNA i modelowanie populacji dla haplogrupy {haplogroup}.",
            "uk": "Кілька аналітичних платформ дозволяють порівняння стародавніх ДНК і моделювання популяцій для гаплогрупи {haplogroup}.",
        },

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
