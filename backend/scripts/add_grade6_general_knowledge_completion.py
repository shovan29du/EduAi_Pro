#!/usr/bin/env python3
"""Depth pass, Grade 6 General Knowledge: fill in real, hand-checked
data_table content for the 28 Grade 6 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings Grade 6 General
Knowledge to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "gk-g6-l1": {
        "data_table": table(["Religion", "Approx. Founded"], [
            ["Hinduism", "Ancient, over 4,000 years ago"], ["Buddhism", "c. 5th century BCE"],
            ["Christianity", "1st century CE"], ["Islam", "7th century CE"],
        ]),
    },
    "general-knowledge-g6-l2": {
        "data_table": table(["Landmark", "Country"], [
            ["Eiffel Tower", "France"], ["Taj Mahal", "India"],
        ]),
    },
    "general-knowledge-g6-l3": {
        "data_table": table(["Country", "Flag Colors"], [
            ["Japan", "White and red"], ["Bangladesh", "Green and red"],
        ]),
    },
    "general-knowledge-g6-l4": {
        "data_table": table(["Country", "Currency"], [
            ["United States", "Dollar"], ["Japan", "Yen"], ["European Union", "Euro"],
        ]),
    },
    "general-knowledge-g6-l5": {
        "data_table": table(["Language", "Spoken Mainly In"], [
            ["Mandarin", "China"], ["Spanish", "Spain, Latin America"],
        ]),
    },
    "general-knowledge-g6-l6": {
        "data_table": table(["Country", "Capital"], [
            ["France", "Paris"], ["Japan", "Tokyo"], ["Bangladesh", "Dhaka"],
        ]),
    },
    "general-knowledge-g6-l7": {
        "data_table": table(["Inventor", "Invention"], [
            ["Thomas Edison", "Practical light bulb"], ["Johannes Gutenberg", "Printing press"],
        ]),
    },
    "general-knowledge-g6-l8": {
        "data_table": table(["Milestone", "Year"], [
            ["First human in space (Yuri Gagarin)", "1961"], ["First Moon landing (Apollo 11)", "1969"],
        ]),
    },
    "general-knowledge-g6-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["First modern Olympics", "1896, Athens"], ["Olympic values", "Excellence, friendship, respect"],
        ]),
    },
    "general-knowledge-g6-l10": {
        "data_table": table(["Record", "Fact"], [
            ["Tallest mountain", "Mount Everest, 8,849 m"], ["Longest river", "The Nile (or Amazon, by some measures)"],
        ]),
    },
    "general-knowledge-g6-l11": {
        "data_table": table(["Holiday", "Celebrated By"], [
            ["Eid al-Fitr", "Muslim communities worldwide"], ["Diwali", "Hindu communities worldwide"],
        ]),
    },
    "general-knowledge-g6-l12": {
        "data_table": table(["Organization", "Purpose"], [
            ["United Nations", "Promotes peace and cooperation among countries"],
            ["WHO", "Coordinates global public health"],
        ]),
    },
    "general-knowledge-g6-l13": {
        "data_table": table(["Explorer", "Known For"], [
            ["Marco Polo", "Travels along the Silk Road"], ["Ibn Battuta", "Extensive travels across Africa and Asia"],
        ]),
    },
    "general-knowledge-g6-l15": {
        "data_table": table(["Animal", "Status"], [
            ["Giant panda", "Vulnerable"], ["Bengal tiger", "Endangered"],
        ]),
    },
    "general-knowledge-g6-l16": {
        "data_table": table(["Food", "Country of Origin"], [
            ["Sushi", "Japan"], ["Pizza", "Italy"], ["Biryani", "South Asia"],
        ]),
    },
    "general-knowledge-g6-l17": {
        "data_table": table(["Scientist", "Discovery"], [
            ["Isaac Newton", "Laws of motion and gravity"], ["Marie Curie", "Research on radioactivity"],
        ]),
    },
    "general-knowledge-g6-l18": {
        "data_table": table(["Event", "Approximate Date"], [
            ["Fall of the Roman Empire", "476 CE"], ["World War II ends", "1945"],
        ]),
    },
    "general-knowledge-g6-l19": {
        "data_table": table(["Nobel Category", "Example"], [
            ["Peace", "Awarded for advancing peace efforts"], ["Physics", "Awarded for major scientific discoveries"],
        ]),
    },
    "general-knowledge-g6-l20": {
        "data_table": table(["Sport", "Origin"], [
            ["Football (soccer)", "England (modern rules)"], ["Basketball", "United States, invented by James Naismith"],
        ]),
    },
    "general-knowledge-g6-l21": {
        "data_table": table(["Museum", "Location"], [
            ["The Louvre", "Paris, France"], ["The British Museum", "London, UK"],
        ]),
    },
    "general-knowledge-g6-l22": {
        "data_table": table(["Wonder", "Location"], [
            ["Great Pyramid of Giza", "Egypt"], ["Hanging Gardens of Babylon", "Mesopotamia (traditionally)"],
        ]),
    },
    "general-knowledge-g6-l23": {
        "data_table": table(["Modern Engineering Feat", "Location"], [
            ["Panama Canal", "Panama"], ["Channel Tunnel", "Between England and France"],
        ]),
    },
    "general-knowledge-g6-l24": {
        "data_table": table(["Calendar", "Basis"], [
            ["Gregorian calendar", "Solar year, used internationally"], ["Islamic (Hijri) calendar", "Lunar cycles"],
        ]),
    },
    "general-knowledge-g6-l25": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"], ["Vincent van Gogh", "The Starry Night"],
        ]),
    },
    "general-knowledge-g6-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Most populous country (as of recent data)", "India"], ["Most populous continent", "Asia"],
        ]),
    },
    "general-knowledge-g6-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias", "A leaning toward a particular viewpoint"], ["Fact-checking", "Verifying claims before trusting them"],
        ]),
    },
    "general-knowledge-g6-l28": {
        "data_table": table(["Game", "Origin"], [
            ["Chess", "India, later developed in Persia"], ["Mancala", "Ancient Africa"],
        ]),
    },
    "general-knowledge-g6-l29": {
        "data_table": table(["Dance Style", "Region"], [
            ["Flamenco", "Spain"], ["Tango", "Argentina"],
        ]),
    },
    "general-knowledge-g6-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Bones in an adult human body", "206"], ["Days in a leap year", "366"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 General Knowledge lessons (completing 30/30).")


if __name__ == "__main__":
    main()
