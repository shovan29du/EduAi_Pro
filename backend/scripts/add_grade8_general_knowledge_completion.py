#!/usr/bin/env python3
"""Depth pass, Grade 8 General Knowledge: fill in real, hand-checked
data_table content for the 38 Grade 8 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings Grade 8 General
Knowledge to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "gk-g8-l1": {
        "data_table": table(["Issue", "Example"], [
            ["Climate change", "Rising global temperatures"], ["Deforestation", "Loss of forest habitats"],
        ]),
    },
    "general-knowledge-g8-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Largest continent", "Asia"], ["Largest ocean", "Pacific Ocean"],
        ]),
    },
    "general-knowledge-g8-l3": {
        "data_table": table(["Landmark", "Country"], [
            ["Eiffel Tower", "France"], ["Taj Mahal", "India"],
        ]),
    },
    "general-knowledge-g8-l4": {
        "data_table": table(["Country", "Flag Colors"], [
            ["Japan", "White and red"],
        ]),
    },
    "general-knowledge-g8-l5": {
        "data_table": table(["Organization", "Purpose"], [
            ["UN", "Promotes peace and cooperation among countries"], ["WHO", "Coordinates global public health"],
            ["UNESCO", "Promotes education, science, and culture"],
        ]),
    },
    "general-knowledge-g8-l6": {
        "data_table": table(["Country", "Currency"], [
            ["United States", "Dollar"], ["Japan", "Yen"],
        ]),
    },
    "general-knowledge-g8-l7": {
        "data_table": table(["Religion", "Approx. Founded"], [
            ["Hinduism", "Ancient, over 4,000 years ago"], ["Islam", "7th century CE"],
        ]),
    },
    "general-knowledge-g8-l8": {
        "data_table": table(["Language", "Spoken Mainly In"], [
            ["Mandarin", "China"], ["Spanish", "Spain, Latin America"],
        ]),
    },
    "general-knowledge-g8-l9": {
        "data_table": table(["Inventor", "Invention"], [
            ["Thomas Edison", "Practical light bulb"],
        ]),
    },
    "general-knowledge-g8-l10": {
        "data_table": table(["Milestone", "Year"], [
            ["First human in space (Yuri Gagarin)", "1961"], ["First Moon landing (Apollo 11)", "1969"],
        ]),
    },
    "general-knowledge-g8-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Bones in an adult human body", "206"],
        ]),
    },
    "general-knowledge-g8-l12": {
        "data_table": table(["Action", "Benefit"], [
            ["Recycling", "Reduces waste in landfills"],
        ]),
    },
    "general-knowledge-g8-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["First modern Olympics", "1896, Athens"],
        ]),
    },
    "general-knowledge-g8-l15": {
        "data_table": table(["Scientist", "Discovery"], [
            ["Isaac Newton", "Laws of motion and gravity"],
        ]),
    },
    "general-knowledge-g8-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Standard time zones worldwide", "24"],
        ]),
    },
    "general-knowledge-g8-l18": {
        "data_table": table(["Government Type", "Description"], [
            ["Democracy", "Citizens vote for leaders"], ["Monarchy", "Rule by a king or queen"],
        ]),
    },
    "general-knowledge-g8-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Democracy", "A system where citizens vote for leaders"],
        ]),
    },
    "general-knowledge-g8-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Universal Declaration of Human Rights", "Adopted by the UN in 1948"],
        ]),
    },
    "general-knowledge-g8-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Global trade", "Buying and selling goods between countries"],
        ]),
    },
    "general-knowledge-g8-l22": {
        "data_table": table(["Explorer", "Known For"], [
            ["Marco Polo", "Travels along the Silk Road"],
        ]),
    },
    "general-knowledge-g8-l23": {
        "data_table": table(["Technology Trend", "Example"], [
            ["Artificial intelligence", "Voice assistants, recommendation systems"],
        ]),
    },
    "general-knowledge-g8-l24": {
        "data_table": table(["Renewable Energy", "Example"], [
            ["Solar power", "Widely used in sunny regions"],
        ]),
    },
    "general-knowledge-g8-l25": {
        "data_table": table(["Organization", "Purpose"], [
            ["WHO", "Coordinates global public health"],
        ]),
    },
    "general-knowledge-g8-l26": {
        "data_table": table(["Cuisine", "Signature Dish"], [
            ["Italian", "Pasta"], ["Indian", "Curry"],
        ]),
    },
    "general-knowledge-g8-l27": {
        "data_table": table(["Festival", "Region"], [
            ["Diwali", "India and Hindu communities worldwide"], ["Eid al-Fitr", "Muslim communities worldwide"],
        ]),
    },
    "general-knowledge-g8-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias", "A leaning toward a particular viewpoint"],
        ]),
    },
    "general-knowledge-g8-l29": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"],
        ]),
    },
    "general-knowledge-g8-l30": {
        "data_table": table(["Author", "Famous Work"], [
            ["Charles Dickens", "Oliver Twist"],
        ]),
    },
    "general-knowledge-g8-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Budget", "A plan for spending and saving money"],
        ]),
    },
    "general-knowledge-g8-l32": {
        "data_table": table(["Career", "Focus"], [
            ["Engineer", "Designs and builds systems"],
        ]),
    },
    "general-knowledge-g8-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Climate change", "Long-term shift in global temperatures and weather patterns"],
        ]),
    },
    "general-knowledge-g8-l34": {
        "data_table": table(["Animal", "Status"], [
            ["Giant panda", "Vulnerable"], ["Bengal tiger", "Endangered"],
        ]),
    },
    "general-knowledge-g8-l35": {
        "data_table": table(["Event", "Approximate Date"], [
            ["Fall of the Roman Empire", "476 CE"], ["World War II ends", "1945"],
        ]),
    },
    "general-knowledge-g8-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Rule of law", "The principle that everyone, including leaders, is subject to the law"],
        ]),
    },
    "general-knowledge-g8-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Media bias", "A leaning toward a particular viewpoint in reporting"],
        ]),
    },
    "general-knowledge-g8-l38": {
        "data_table": table(["Fact", "Detail"], [
            ["Most populous country (as of recent data)", "India"],
        ]),
    },
    "general-knowledge-g8-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Closest planet to the sun", "Mercury"], ["Largest planet", "Jupiter"],
        ]),
    },
    "general-knowledge-g8-l40": {
        "data_table": table(["Leader", "Known For"], [
            ["Nelson Mandela", "Anti-apartheid leader, President of South Africa"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 General Knowledge lessons (completing 40/40).")


if __name__ == "__main__":
    main()
