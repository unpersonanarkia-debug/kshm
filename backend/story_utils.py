# story_utils.py

from typing import Dict, List
import random

def generate_story_html(haplo_data: Dict, user_name: str, notes: str = "") -> str:
    haplogroup = haplo_data.get("haplogroup", "Tuntematon")
    ancient_samples = haplo_data.get("ancient_samples", [])
    regions = haplo_data.get("regions", [])
    time_depth = haplo_data.get("time_depth", "esihistoriallinen aika")
    lineage_type = haplo_data.get("lineage_type", "mtDNA")

    narrative_style = select_narrative_style(haplogroup)

    intro = build_intro(haplogroup, user_name, narrative_style)
    body = build_body(haplo_data, narrative_style)
    timeline = build_timeline(ancient_samples)
    conclusion = build_conclusion(haplogroup, user_name, narrative_style)

    notes_section = ""
    if notes:
        notes_section = f"<section><h2>📝 Käyttäjän huomioita</h2><p>{notes}</p></section>"

    html = f"""
    <html>
    <head>
        <meta charset="utf-8"/>
        <title>{haplogroup} – Verilinjan tarina</title>
        <style>
            body {{ font-family: Georgia, serif; background: #fdfaf3; padding: 40px; }}
            h1, h2, h3 {{ color: #7c3f00; }}
            section {{ margin-bottom: 40px; }}
            .quote {{ font-style: italic; color: #555; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <section>{intro}</section>
        <section>{body}</section>
        <section>{timeline}</section>
        {notes_section}
        <section>{conclusion}</section>
    </body>
    </html>
    """

    return html


# ------------------------------
# Narrative styles
# ------------------------------

def select_narrative_style(haplogroup: str) -> str:
    """
    Valitsee tarinatyyli haploryhmän mukaan.
    """
    if haplogroup.startswith("H"):
        return "explorer_legacy"
    elif haplogroup.startswith("U"):
        return "ancestral_memory"
    elif haplogroup.startswith("J"):
        return "migration_chronicle"
    elif haplogroup.startswith("K"):
        return "matriarchal_line"
    elif haplogroup.startswith("T"):
        return "trade_route_story"
    elif haplogroup.startswith("C") or haplogroup.startswith("D"):
        return "steppe_and_eastward"
    elif haplogroup.startswith("A") or haplogroup.startswith("B"):
        return "ancestral_continuity"
    elif haplogroup.startswith("Y"):
        return "polar_frontier"
    else:
        return "archaeological_journey"


# ------------------------------
# Sections
# ------------------------------

def build_intro(haplogroup: str, user_name: str, style: str) -> str:
    intros = {
        "explorer_legacy": f"""
            <h1>🧭 {haplogroup} – Tutkimusmatkailijan veri</h1>
            <p>Rakas {user_name},</p>
            <p>Veressäsi kulkee linja, joka on tottunut liikkeeseen, muutokseen ja horisontin ylittämiseen.
            Tämä ei ole sattumaa – se on perintö, joka syntyi jo kauan ennen kirjoitettua historiaa.</p>
        """,
        "ancestral_memory": f"""
            <h1>🪶 {haplogroup} – Muistin linja</h1>
            <p>{user_name}, tämä tarina ei ole vain liikkeestä – vaan muistamisesta.
            Linjasi on yksi ihmiskunnan vanhimmista, ja se kantaa mukanaan hiljaista jatkuvuutta.</p>
        """,
        "migration_chronicle": f"""
            <h1>🌍 {haplogroup} – Vaellusten kronikka</h1>
            <p>{user_name}, tämä on tarina liikkeestä – ei pakolaisuudesta, vaan sopeutumisesta.
            Veresi on kulkenut läpi mantereiden ja kulttuurien.</p>
        """,
        "matriarchal_line": f"""
            <h1>👩‍👧‍👧 {haplogroup} – Äitien ketju</h1>
            <p>{user_name}, tämä tarina kulkee äidiltä tyttärelle – katkeamattomana.
            Se on hiljainen voima, joka on selvinnyt myrskyistä, sodista ja muutoksista.</p>
        """,
        "trade_route_story": f"""
            <h1>⚓ {haplogroup} – Kauppareittien veri</h1>
            <p>{user_name}, veresi kulki markkinoiden, satamien ja rajojen halki.
            Tämä on tarina ihmisistä, jotka yhdistivät maailmoja ennen karttoja.</p>
        """,
        "steppe_and_eastward": f"""
            <h1>🐎 {haplogroup} – Aavikon ja arojen perintö</h1>
            <p>{user_name}, linjasi syntyi avoimilla tasangoilla ja vuorten juurilla,
            siellä missä ihminen oppi kulkemaan pitkiä matkoja ilman rajoja.</p>
        """,
        "ancestral_continuity": f"""
            <h1>🌱 {haplogroup} – Jatkuvuuden veri</h1>
            <p>{user_name}, tämä linja ei kadonnut. Se ei katkennut.
            Se sopeutui, juurtui ja säilyi.</p>
        """,
        "polar_frontier": f"""
            <h1>❄️ {haplogroup} – Äärirajojen linja</h1>
            <p>{user_name}, veresi syntyi kylmän, tuulen ja pitkien talvien maailmassa.
            Tämä on selviytymisen tarina.</p>
        """,
        "archaeological_journey": f"""
            <h1>🗺️ {haplogroup} – Arkeologinen matka</h1>
            <p>{user_name}, tämä tarina syntyy maasta, kivestä ja luista.
            Se on löydösten ketju, joka johtaa sinuun.</p>
        """
    }

    return intros.get(style, intros["archaeological_journey"])


def build_body(haplo_data: Dict, style: str) -> str:
    samples = haplo_data.get("ancient_samples", [])
    regions = haplo_data.get("regions", [])
    description = haplo_data.get("description", "")

    paragraphs = []

    if style in ["explorer_legacy", "trade_route_story"]:
        paragraphs.append(f"""
            <p>Varhaisimmat tunnetut löydöt linjastasi sijoittuvat alueille:
            {", ".join(regions[:5])}. Näissä paikoissa ihmiset eivät pysyneet paikallaan –
            he liikkuivat, vaihtoivat ja rakensivat yhteyksiä.</p>
        """)
    elif style in ["ancestral_memory", "ancestral_continuity"]:
        paragraphs.append(f"""
            <p>Linjasi näkyy jatkuvana kerroksena arkeologisissa aineistoissa,
            erityisesti alueilla {", ".join(regions[:5])}. Tämä ei ole liike, vaan säilyminen.</p>
        """)
    elif style in ["migration_chronicle", "steppe_and_eastward"]:
        paragraphs.append(f"""
            <p>Veresi reitti kulki useiden kulttuurivyöhykkeiden halki:
            {", ".join(regions[:6])}. Jokainen siirtymä jätti jäljen geneettiseen tarinaan.</p>
        """)
    elif style == "matriarchal_line":
        paragraphs.append(f"""
            <p>Tämä linja tunnetaan erityisesti äitien kautta periytyvänä ketjuna,
            joka on dokumentoitu näillä alueilla: {", ".join(regions[:5])}.</p>
        """)
    else:
        paragraphs.append(f"""
            <p>Arkeologiset löydöt osoittavat linjasi levinneisyyden seuraavilla alueilla:
            {", ".join(regions[:6])}. Jokainen löytö on pala suurempaa kokonaisuutta.</p>
        """)

    if description:
        paragraphs.append(f"<p>{description}</p>")

    if samples:
        sample_texts = []
        for s in samples[:4]:
            sample_texts.append(f"""
                <p>📍 <strong>{s.get("location", "Tuntematon paikka")}</strong> 
                ({s.get("date", "ajoittamaton")}): 
                {s.get("context", "Arkeologinen näyte")}</p>
            """)
        paragraphs.append("<h3>Keskeisiä muinaisnäytteitä:</h3>" + "".join(sample_texts))

    return "".join(paragraphs)


def build_timeline(samples: List[Dict]) -> str:
    if not samples:
        return "<h2>🗓️ Aikajana</h2><p>Ei saatavilla olevia ajoitettuja muinaisnäytteitä.</p>"

    timeline_items = []
    for s in sorted(samples, key=lambda x: x.get("year_bp", 0), reverse=True):
        timeline_items.append(f"""
            <li><strong>{s.get("date", "Tuntematon aika")}</strong> – 
            {s.get("location", "Tuntematon paikka")} 
            ({s.get("culture", "kulttuuri tuntematon")})</li>
        """)

    return f"""
        <h2>🗓️ Aikajana – Verilinjan jäljet ajassa</h2>
        <ul>{"".join(timeline_items)}</ul>
    """


def build_conclusion(haplogroup: str, user_name: str, style: str) -> str:
    endings = {
        "explorer_legacy": f"""
            <h2>🌟 Loppusanat</h2>
            <p>{user_name}, veresi kertoo tarinan ihmisistä, jotka eivät pelänneet horisonttia.
            Sinä olet tämän ketjun uusin luku.</p>
        """,
        "ancestral_memory": f"""
            <h2>🌟 Loppusanat</h2>
            <p>{user_name}, tämä linja ei kadonnut, koska se muisti.
            Ja nyt sinä olet sen muisti.</p>
        """,
        "migration_chronicle": f"""
            <h2>🌟 Loppusanat</h2>
            <p>{user_name}, veresi kantaa mukanaan kartan, jota ei ole piirretty –
            mutta joka on silti kuljettu.</p>
        """,
        "matriarchal_line": f"""
            <h2>🌟 Loppusanat</h2>
            <p>{user_name}, tämä tarina kulkee äidiltä tyttärelle,
            ja nyt se jatkuu sinussa.</p>
        """,
        "trade_route_story": f"""
            <h2>🌟 Loppusanat</h2>
            <p>{user_name}, veresi yhdisti maailmoja ennen kuin kartat tekivät sen.
            Nyt se yhdistää menneisyyden ja nykyisyyden sinussa.</p>
        """,
        "steppe_and_eastward": f"""
            <h2>🌟 Loppusanat</h2>
            <p>{user_name}, tämä on selviytymisen ja liikkeen perintö.
            Sinä olet sen nykyaikainen kantaja.</p>
        """,
        "ancestral_continuity": f"""
            <h2>🌟 Loppusanat</h2>
            <p>{user_name}, tämä linja ei ole katkonnut – se on jatkunut.
            Ja nyt se jatkuu sinussa.</p>
        """,
        "polar_frontier": f"""
            <h2>🌟 Loppusanat</h2>
            <p>{user_name}, veresi syntyi äärirajoilla – ja siksi se kestää.</p>
        """,
        "archaeological_journey": f"""
            <h2>🌟 Loppusanat</h2>
            <p>{user_name}, tämä on arkeologinen matka, joka ei pääty kaivaukseen –
            vaan sinuun.</p>
        """
    }

    return endings.get(style, endings["archaeological_journey"])
