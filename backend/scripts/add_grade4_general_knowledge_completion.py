#!/usr/bin/env python3
"""Depth pass, Grade 4 General Knowledge: fill in real, hand-checked
data_table content for the 28 Grade 4 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings Grade 4 General
Knowledge to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "gk-g4-l1": {
        "data_table": table(["Record", "Fact"], [
            ["Tallest mountain", "Mount Everest, 8,849 m"], ["Longest river", "The Nile (or Amazon, by some measures)"],
        ]),
    },
    "general-knowledge-g4-l2": {
        "data_table": table(["Country", "Flag Colors"], [
            ["Japan", "White and red"], ["Bangladesh", "Green and red"], ["France", "Blue, white, and red"],
        ]),
    },
    "general-knowledge-g4-l3": {
        "data_table": table(["Country", "Currency"], [
            ["United States", "Dollar"], ["Japan", "Yen"], ["European Union", "Euro"],
        ]),
    },
    "general-knowledge-g4-l5": {
        "data_table": table(["Inventor", "Invention"], [
            ["Thomas Edison", "Practical light bulb"], ["Alexander Graham Bell", "Telephone"],
        ]),
    },
    "general-knowledge-g4-l6": {
        "data_table": table(["Milestone", "Year"], [
            ["First human in space (Yuri Gagarin)", "1961"], ["First Moon landing (Apollo 11)", "1969"],
        ]),
    },
    "general-knowledge-g4-l7": {
        "data_table": table(["Explorer", "Known For"], [
            ["Marco Polo", "Travels along the Silk Road"], ["Ibn Battuta", "Extensive travels across Africa and Asia"],
        ]),
    },
    "general-knowledge-g4-l8": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Flag", "Represents a country's identity"], ["National anthem", "A patriotic song"],
        ]),
    },
    "general-knowledge-g4-l9": {
        "data_table": table(["Organization", "Purpose"], [
            ["United Nations", "Promotes peace and cooperation among countries"],
            ["WHO", "Coordinates global public health"],
        ]),
    },
    "general-knowledge-g4-l11": {
        "data_table": table(["Language", "Spoken Mainly In"], [
            ["Mandarin", "China"], ["Spanish", "Spain, Latin America"], ["Bangla", "Bangladesh"],
        ]),
    },
    "general-knowledge-g4-l12": {
        "data_table": table(["Landmark", "Country"], [
            ["Eiffel Tower", "France"], ["Taj Mahal", "India"],
        ]),
    },
    "general-knowledge-g4-l13": {
        "data_table": table(["Animal", "Continent"], [
            ["Kangaroo", "Australia"], ["Panda", "Asia"],
        ]),
    },
    "general-knowledge-g4-l14": {
        "data_table": table(["Invention", "Impact"], [
            ["The wheel", "Enabled transportation and machines"], ["The printing press", "Spread knowledge faster"],
        ]),
    },
    "general-knowledge-g4-l15": {
        "data_table": table(["Scientist", "Discovery"], [
            ["Isaac Newton", "Laws of motion and gravity"], ["Marie Curie", "Research on radioactivity"],
        ]),
    },
    "general-knowledge-g4-l16": {
        "data_table": table(["Religion", "Approx. Founded"], [
            ["Hinduism", "Ancient, over 4,000 years ago"], ["Buddhism", "c. 5th century BCE"],
            ["Christianity", "1st century CE"], ["Islam", "7th century CE"],
        ]),
    },
    "general-knowledge-g4-l17": {
        "data_table": table(["Calendar", "Basis"], [
            ["Gregorian calendar", "Solar year, used internationally"], ["Islamic (Hijri) calendar", "Lunar cycles"],
        ]),
    },
    "general-knowledge-g4-l18": {
        "data_table": table(["Author", "Famous Work"], [
            ["Hans Christian Andersen", "The Ugly Duckling"], ["Lewis Carroll", "Alice's Adventures in Wonderland"],
        ]),
    },
    "general-knowledge-g4-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Current events", "Things happening in the news right now"],
            ["Reliable source", "A news outlet that checks facts before publishing"],
        ]),
    },
    "general-knowledge-g4-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Bones in an adult human body", "206"], ["Days in a leap year", "366"],
        ]),
    },
    "general-knowledge-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Comparing distances", "Understanding how far Everest's summit rises"],
        ]),
    },
    "general-knowledge-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Traveling", "Recognizing flags of countries visited"],
        ]),
    },
    "general-knowledge-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Travel budgeting", "Exchanging money into local currency"],
        ]),
    },
    "general-knowledge-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Tourism", "Visiting ancient wonders like the pyramids"],
        ]),
    },
    "general-knowledge-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Everyday devices", "Using light bulbs and telephones daily"],
        ]),
    },
    "general-knowledge-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Watching a rocket launch", "Understanding the history of space milestones"],
        ]),
    },
    "general-knowledge-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Studying maps", "Following explorers' historic routes"],
        ]),
    },
    "general-knowledge-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Citizenship ceremonies", "Reciting a national anthem"],
        ]),
    },
    "general-knowledge-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Global cooperation", "Countries working together on health crises"],
        ]),
    },
    "general-knowledge-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Watching the Olympics", "Recognizing the history behind the games"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 General Knowledge lessons (completing 30/30).")


if __name__ == "__main__":
    main()
