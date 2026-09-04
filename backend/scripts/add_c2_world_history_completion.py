#!/usr/bin/env python3
"""Depth pass, C2 World History: fill in real, hand-checked data_table
content for the 69 C2 World History lessons not covered by the earlier
breadth-first batch. Brings C2 World History to full 70/70 coverage.

l61-l63 are "Foundations 2" lessons that revisit specific earlier topics
(l61 -> l52 Non-Aligned Movement, l62 -> l11 Columbian Exchange,
l63 -> l17 Scramble for Africa); l64-l70 are "Worked Analysis" companions
to l1-l7. Both reuse the underlying data_table of their source lesson.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_world_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "world-history-c2-l1": {
        "data_table": table(["Era", "Feature"], [
            ["Medieval & Early Modern history", "Spans the fall of Rome through the age of European exploration"],
        ]),
    },
    "world-history-c2-l2": {
        "data_table": table(["Era", "Feature"], [
            ["Modern world history", "Traces industrialization, nation-building, and global conflict from 1750 onward"],
        ]),
    },
    "world-history-c2-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Roman law", "Codified principles like due process influenced later Western legal systems"],
        ]),
    },
    "world-history-c2-l5": {
        "data_table": table(["Route", "Exchange"], [
            ["Silk Road", "Connected Rome, Han China, and India through goods, ideas, and disease"],
        ]),
    },
    "world-history-c2-l6": {
        "data_table": table(["Empire", "Legacy"], [
            ["Byzantine Empire", "Preserved Roman law and Greek scholarship for over a thousand years"],
        ]),
    },
    "world-history-c2-l7": {
        "data_table": table(["Event", "Global Context"], [
            ["The Crusades", "Intensified trade and cultural contact between Europe and the Islamic world"],
        ]),
    },
    "world-history-c2-l8": {
        "data_table": table(["Era", "Feature"], [
            ["Islamic Golden Age", "Trade networks spread scientific and mathematical knowledge across three continents"],
        ]),
    },
    "world-history-c2-l9": {
        "data_table": table(["Civilization", "Feature"], [
            ["Great Zimbabwe", "Stone-walled city that anchored a major East African gold and trade network"],
        ]),
    },
    "world-history-c2-l10": {
        "data_table": table(["Empire", "Impact"], [
            ["Mongol Empire", "Unified trade routes across Eurasia, facilitating exchange but also plague spread"],
        ]),
    },
    "world-history-c2-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Columbian Exchange", "Transfer of crops, animals, people, and disease between the Old and New Worlds"],
        ]),
    },
    "world-history-c2-l12": {
        "data_table": table(["System", "Detail"], [
            ["Middle Passage", "Forced transatlantic voyage that supplied enslaved labor to plantation economies"],
        ]),
    },
    "world-history-c2-l13": {
        "data_table": table(["Figure", "Contribution"], [
            ["Isaac Newton", "Laws of motion and universal gravitation reframed the universe as mechanistic"],
        ]),
    },
    "world-history-c2-l14": {
        "data_table": table(["Revolution", "Outcome"], [
            ["American Revolution", "Established an independent republic grounded in Enlightenment principles"],
            ["French Revolution", "Overthrew the monarchy and spread ideas of popular sovereignty across Europe"],
        ]),
    },
    "world-history-c2-l15": {
        "data_table": table(["Region", "Effect"], [
            ["Industrial Revolution spread", "Mechanized production reshaped labor and urban life beyond Britain"],
        ]),
    },
    "world-history-c2-l16": {
        "data_table": table(["Region", "Trend"], [
            ["Balkans/Eastern Europe", "Rising nationalism fractured multiethnic empires into new nation-states"],
        ]),
    },
    "world-history-c2-l17": {
        "data_table": table(["Event", "Detail"], [
            ["Scramble for Africa", "European powers partitioned the continent with little regard for existing societies"],
        ]),
    },
    "world-history-c2-l18": {
        "data_table": table(["Feature", "Detail"], [
            ["World War I", "Introduced industrialized trench warfare and mass casualties on an unprecedented scale"],
        ]),
    },
    "world-history-c2-l19": {
        "data_table": table(["Provision", "Consequence"], [
            ["Treaty of Versailles", "War-guilt and reparations clauses fueled German resentment and instability"],
        ]),
    },
    "world-history-c2-l20": {
        "data_table": table(["Event", "Outcome"], [
            ["Russian Revolution of 1917", "Toppled the tsarist regime and installed the world's first communist state"],
        ]),
    },
    "world-history-c2-l21": {
        "data_table": table(["Factor", "Role"], [
            ["Bronze Age collapse", "Combination of invasion, drought, and trade breakdown ended several civilizations at once"],
        ]),
    },
    "world-history-c2-l22": {
        "data_table": table(["System", "Feature"], [
            ["Achaemenid administration", "Satrapies and royal roads allowed centralized control of a vast empire"],
        ]),
    },
    "world-history-c2-l23": {
        "data_table": table(["Feature", "Limit"], [
            ["Athenian democracy", "Direct citizen voting excluded women, slaves, and foreign residents"],
        ]),
    },
    "world-history-c2-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Hellenistic syncretism", "Greek culture blended with local traditions across conquered territories"],
        ]),
    },
    "world-history-c2-l25": {
        "data_table": table(["Civilization", "Feature"], [
            ["Phoenicians", "Maritime traders who spread an alphabet and founded colonies across the Mediterranean"],
        ]),
    },
    "world-history-c2-l26": {
        "data_table": table(["Dynasty", "Detail"], [
            ["Kushite rule over Egypt", "The 25th Dynasty of Egyptian pharaohs originated from the Kingdom of Kush"],
        ]),
    },
    "world-history-c2-l27": {
        "data_table": table(["Era", "Feature"], [
            ["Late Antiquity", "Roman institutions gradually transformed rather than collapsing abruptly"],
        ]),
    },
    "world-history-c2-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Bushido", "Samurai code emphasizing loyalty, honor, and martial discipline"],
        ]),
    },
    "world-history-c2-l29": {
        "data_table": table(["System", "Detail"], [
            ["Aztec tribute system", "Conquered city-states paid regular tribute that funded the imperial economy"],
        ]),
    },
    "world-history-c2-l30": {
        "data_table": table(["System", "Detail"], [
            ["Inca road system", "Extensive road network enabled rapid communication and administration across the Andes"],
        ]),
    },
    "world-history-c2-l31": {
        "data_table": table(["Achievement", "Detail"], [
            ["Maya astronomy/writing", "Advanced calendar systems and a hieroglyphic script recorded political history"],
        ]),
    },
    "world-history-c2-l32": {
        "data_table": table(["System", "Detail"], [
            ["Ottoman millet system", "Granted religious communities autonomy over their own legal and communal affairs"],
        ]),
    },
    "world-history-c2-l33": {
        "data_table": table(["Consequence", "Detail"], [
            ["The Reformation", "Fractured religious unity in Europe and reshaped political alliances along confessional lines"],
        ]),
    },
    "world-history-c2-l34": {
        "data_table": table(["Legacy", "Detail"], [
            ["Renaissance humanism", "Emphasized classical learning and individual potential, shaping later Enlightenment thought"],
        ]),
    },
    "world-history-c2-l35": {
        "data_table": table(["System", "Feature"], [
            ["Absolutism", "Centralized royal authority with few institutional checks"],
            ["Constitutionalism", "Power limited by law and representative institutions"],
        ]),
    },
    "world-history-c2-l36": {
        "data_table": table(["Treaty", "Significance"], [
            ["Peace of Westphalia", "Established the principle of state sovereignty underlying the modern international system"],
        ]),
    },
    "world-history-c2-l37": {
        "data_table": table(["Policy", "Detail"], [
            ["Qing frontier expansion", "Incorporated diverse frontier peoples through flexible, multiethnic governance"],
        ]),
    },
    "world-history-c2-l38": {
        "data_table": table(["Policy", "Detail"], [
            ["Sakoku", "Japan restricted foreign trade and contact to maintain internal stability"],
        ]),
    },
    "world-history-c2-l39": {
        "data_table": table(["System", "Feature"], [
            ["Comparative colonial systems", "Spanish, Portuguese, French, and British colonies differed in labor and settlement models"],
        ]),
    },
    "world-history-c2-l40": {
        "data_table": table(["Event", "Impact"], [
            ["Haitian Revolution", "First successful slave revolt to found an independent state, alarming slaveholding powers"],
        ]),
    },
    "world-history-c2-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Caudillismo", "Strongman rule filled power vacuums left after Latin American independence"],
        ]),
    },
    "world-history-c2-l42": {
        "data_table": table(["System", "Detail"], [
            ["Congress System", "Great powers coordinated diplomacy after 1815 to preserve a European balance of power"],
        ]),
    },
    "world-history-c2-l43": {
        "data_table": table(["Policy", "Effect"], [
            ["Meiji industrialization", "State-led modernization rapidly transformed Japan into an industrial power"],
        ]),
    },
    "world-history-c2-l44": {
        "data_table": table(["System", "Detail"], [
            ["Treaty ports/extraterritoriality", "Foreign powers exercised legal jurisdiction within designated Chinese port cities"],
        ]),
    },
    "world-history-c2-l45": {
        "data_table": table(["Feature", "Detail"], [
            ["Total war", "World War II mobilized entire civilian economies and populations for the war effort"],
        ]),
    },
    "world-history-c2-l46": {
        "data_table": table(["Front", "Detail"], [
            ["Eastern Front", "Site of the largest and deadliest military campaigns of World War II"],
        ]),
    },
    "world-history-c2-l47": {
        "data_table": table(["Theater", "Outcome"], [
            ["Pacific Theater", "Ended with the atomic bombings of Hiroshima and Nagasaki and Japan's surrender"],
        ]),
    },
    "world-history-c2-l48": {
        "data_table": table(["Field", "Focus"], [
            ["Genocide studies", "Examines the causes, mechanisms, and historical memory of mass atrocities"],
        ]),
    },
    "world-history-c2-l49": {
        "data_table": table(["Institution", "Purpose"], [
            ["United Nations", "Created to maintain international peace and coordinate postwar global governance"],
        ]),
    },
    "world-history-c2-l50": {
        "data_table": table(["Policy", "Detail"], [
            ["Containment", "US strategy to limit the spread of Soviet communism without direct war"],
        ]),
    },
    "world-history-c2-l51": {
        "data_table": table(["Movement", "Goal"], [
            ["Pan-Africanism", "Sought unity and solidarity among African peoples during and after decolonization"],
        ]),
    },
    "world-history-c2-l52": {
        "data_table": table(["Movement", "Goal"], [
            ["Non-Aligned Movement", "States sought to avoid formal alignment with either Cold War bloc"],
        ]),
    },
    "world-history-c2-l53": {
        "data_table": table(["Event", "Detail"], [
            ["Sino-Soviet Split", "Ideological and strategic rivalry fractured the communist bloc's unity"],
        ]),
    },
    "world-history-c2-l54": {
        "data_table": table(["Conflict Type", "Detail"], [
            ["Proxy war", "Superpowers backed opposing sides in regional conflicts to avoid direct confrontation"],
        ]),
    },
    "world-history-c2-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Nuclear deterrence", "Mutual assured destruction discouraged direct superpower conflict"],
        ]),
    },
    "world-history-c2-l56": {
        "data_table": table(["Movement", "Detail"], [
            ["1960s social movements", "Civil rights, anti-war, and student movements spread across multiple countries"],
        ]),
    },
    "world-history-c2-l57": {
        "data_table": table(["Event", "Outcome"], [
            ["Revolutions of 1989", "Peaceful uprisings toppled communist governments across Eastern Europe"],
        ]),
    },
    "world-history-c2-l58": {
        "data_table": table(["Process", "Detail"], [
            ["Post-Soviet transition", "Former Soviet states navigated new market economies and political institutions"],
        ]),
    },
    "world-history-c2-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Neoliberalism", "Late-20th-century policy shift toward deregulation and market-driven globalization"],
        ]),
    },
    "world-history-c2-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Historical memory", "Contested interpretations shape how societies remember 20th-century events"],
        ]),
    },
}

# l61-l63 "Foundations 2" lessons revisit specific earlier topics.
FOUNDATIONS_2_MAP = {61: 52, 62: 11, 63: 17}
for worked_n, base_n in FOUNDATIONS_2_MAP.items():
    base_key = f"world-history-c2-l{base_n}"
    CHARTS[f"world-history-c2-l{worked_n}"] = {
        "data_table": CHARTS[base_key]["data_table"],
    }

# l64-l70 "Worked Analysis" lessons reuse the data_table of l1-l7.
# l3 was already completed by an earlier breadth-first batch, so its
# data_table is hard-coded here rather than pulled from CHARTS.
CHARTS["world-history-c2-l3-source"] = {
    "data_table": table(["Civilization", "River"], [
        ["Mesopotamia", "Tigris and Euphrates"],
        ["Egypt", "Nile"],
        ["Indus Valley", "Indus"],
        ["Ancient China (Shang)", "Yellow River (Huang He)"],
    ]),
}
_l3_source = CHARTS.pop("world-history-c2-l3-source")

WORKED_ANALYSIS_MAP = {64: 1, 65: 2, 66: 3, 67: 4, 68: 5, 69: 6, 70: 7}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"world-history-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"world-history-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"world-history-c2-l{worked_n}"] = {
            "data_table": _l3_source["data_table"],
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 World History lessons (completing 70/70).")


if __name__ == "__main__":
    main()
