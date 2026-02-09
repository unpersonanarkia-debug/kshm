# 🧬 Kadonneen Sukuhistorian Metsästäjä (KSHM)

*Kadonneen Sukuhistorian Metsästäjä* on verkkopohjainen DNA-raporttigeneraattori, joka tuottaa käyttäjän haploryhmään perustuvan *arkeogeneettisen historian*: kronologisen kertomuksen todellisista löydöistä, kulttuureista ja väestöliikkeistä, joissa kyseinen haploryhmä on dokumentoitu.

🌐 Live-sivusto: https://kshm.fi  
📦 Repositorio: https://github.com/unpersonanarkia-debug/kshm

---

## 🔍 Projektin tarkoitus

Tämä projekti:
- Kerää arkeogeneettisiä havaintoja useista kansainvälisistä tietolähteistä
- Yhdistää ne kronologiseksi ja maantieteelliseksi kokonaisuudeksi
- Tuottaa haploryhmäkohtaisen *tieteellisesti pohjautuvan historiakertomuksen*
- Generoi tästä PDF-raportin ja toimittaa sen sähköpostitse
- Soveltuu kuluttajille, tutkijoille, opettajille, historian harrastajille ja etenkin sukututkijoille

---

## 📂 Projektirakenne

```plaintext
kshm/
├── backend/
│   ├── main.py            # FastAPI-sovelluksen ydin
│   ├── data_utils.py      # Arkeogeneettinen tietohakuverkosto
│   ├── story_utils.py     # Kronologinen haploryhmähistorian rakentaja
│   ├── pdf_utils.py       # PDF-raporttigeneraattori
│   ├── email_utils.py     # Sähköpostilähetys
│   ├── requirements.txt
│   └── .env               # Ympäristömuuttujat (ei versionhallintaan)
│
├── index.html
├── tilaa.html
├── h1-t16189c.html        # Esimerkki yhden haploryhmän tarinasta
├── CNAME
├── LICENSE
└── README.md
kshm.fi

⚙️ Teknologiat
	•	Backend: Python + FastAPI
	•	Frontend: HTML + Tailwind CSS
	•	PDF: WeasyPrint / xhtml2pdf / ReportLab
	•	Sähköposti: SMTP (oma domain)
	•	Hosting: Render / VPS
	•	Data: YFull, FTDNA, Haplogrep, Eupedia, Geni, ancientdna.info, EBI, CNGB, RIKEN, venäläiset ja euraasialaiset tietokannat


🧬 Arkeogeneettinen lähestymistapa

Raportti perustuu:
	•	todellisiin muinaisnäytteisiin
	•	dokumentoituihin ajoituksiin
	•	arkeologisiin kulttuureihin
	•	väestöliikkeisiin ja leviämisreitteihin

Tarinan muoto:
	•	on kronologinen
	•	pohjautuu löydösten ajalliseen järjestykseen
	•	voi vaihdella kerronnallisesti (kuivasta tieteellisestä → elävämpään esitykseen)
	•	ei sisällä fiktiota eikä narratiivia, joskus kuvailevaa ja symbolista tarinankerrontaa

⸻

🌍 Tietolähdeverkosto

Järjestelmä hyödyntää:
	•	YFull
	•	FamilyTreeDNA
	•	Haplogrep
	•	Eupedia
	•	Geni
	•	ancientdna.info
	•	European Nucleotide Archive (EBI)
	•	Venäjän akateemiset tietokannat (eLIBRARY, RAS)
	•	Kiinan genomipankit (CNGB, BGI)
	•	Japanin RIKEN
	•	Korean Genome Project
	•	Euraasialaiset arkeogeneettiset konsortiot

Kaikki lähteet yhdistetään yhtenäiseksi, haploryhmäkohtaiseksi tietomalliksi.

⸻

🔐 Tietosuoja
	•	Käyttäjätietoja ei tallenneta pysyvästi
	•	Sähköpostia käytetään vain raportin toimittamiseen
	•	Ei seurantalinkkejä, ei markkinointievästeitä

⸻

📄 Lisenssi

MIT License.

⸻

🧭 Visio

KSHM ei rakenna tarinoita mielikuvituksesta —
se kokoaa ihmiskunnan todellisen liikehistorian DNA:n perusteella.

Se on kartta veressä.
Se on tiedettä, ei symboliikkaa.
Se on dokumentoitu menneisyys, ei legenda.
