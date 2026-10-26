#!/usr/bin/env python3
"""Depth pass, Grade 5 General Knowledge: fill in real, hand-checked
data_table content for the 28 Grade 5 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings Grade 5 General
Knowledge to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "gk-g5-l1": {
        "data_table": table(["Leader", "Known For"], [
            ["Nelson Mandela", "Anti-apartheid leader, President of South Africa"],
            ["Mahatma Gandhi", "Led India's independence movement through nonviolence"],
        ]),
    },
    "general-knowledge-g5-l2": {
        "data_table": table(["Wonder", "Location"], [
            ["Great Pyramid of Giza", "Egypt"], ["Hanging Gardens of Babylon", "Mesopotamia (traditionally)"],
        ]),
    },
    "general-knowledge-g5-l3": {
        "data_table": table(["Modern Wonder", "Location"], [
            ["Great Wall of China", "China"], ["Taj Mahal", "India"], ["Colosseum", "Italy"],
        ]),
    },
    "general-knowledge-g5-l6": {
        "data_table": table(["Country", "Flag Colors"], [
            ["Japan", "White and red"], ["Bangladesh", "Green and red"],
        ]),
    },
    "general-knowledge-g5-l7": {
        "data_table": table(["Country", "Currency"], [
            ["United States", "Dollar"], ["Japan", "Yen"], ["European Union", "Euro"],
        ]),
    },
    "general-knowledge-g5-l8": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Flag", "Represents a country's identity"], ["National anthem", "A patriotic song"],
        ]),
    },
    "general-knowledge-g5-l9": {
        "data_table": table(["Inventor", "Invention"], [
            ["Thomas Edison", "Practical light bulb"], ["Johannes Gutenberg", "Printing press"],
        ]),
    },
    "general-knowledge-g5-l10": {
        "data_table": table(["Scientist", "Discovery"], [
            ["Isaac Newton", "Laws of motion and gravity"], ["Marie Curie", "Research on radioactivity"],
        ]),
    },
    "general-knowledge-g5-l11": {
        "data_table": table(["Explorer", "Known For"], [
            ["Marco Polo", "Travels along the Silk Road"], ["Ibn Battuta", "Extensive travels across Africa and Asia"],
        ]),
    },
    "general-knowledge-g5-l12": {
        "data_table": table(["Landmark", "Country"], [
            ["Eiffel Tower", "France"], ["Taj Mahal", "India"],
        ]),
    },
    "general-knowledge-g5-l13": {
        "data_table": table(["Organization", "Purpose"], [
            ["United Nations", "Promotes peace and cooperation among countries"],
            ["WHO", "Coordinates global public health"],
        ]),
    },
    "general-knowledge-g5-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["First modern Olympics", "1896, Athens"], ["Olympic values", "Excellence, friendship, respect"],
        ]),
    },
    "general-knowledge-g5-l15": {
        "data_table": table(["Record", "Fact"], [
            ["Tallest mountain", "Mount Everest, 8,849 m"], ["Longest river", "The Nile (or Amazon, by some measures)"],
        ]),
    },
    "general-knowledge-g5-l16": {
        "data_table": table(["Animal", "Status"], [
            ["Giant panda", "Vulnerable"], ["Bengal tiger", "Endangered"],
        ]),
    },
    "general-knowledge-g5-l17": {
        "data_table": table(["Milestone", "Year"], [
            ["First human in space (Yuri Gagarin)", "1961"], ["First Moon landing (Apollo 11)", "1969"],
        ]),
    },
    "general-knowledge-g5-l18": {
        "data_table": table(["Religion", "Approx. Founded"], [
            ["Hinduism", "Ancient, over 4,000 years ago"], ["Buddhism", "c. 5th century BCE"],
            ["Christianity", "1st century CE"], ["Islam", "7th century CE"],
        ]),
    },
    "general-knowledge-g5-l19": {
        "data_table": table(["Food", "Country of Origin"], [
            ["Sushi", "Japan"], ["Pizza", "Italy"], ["Biryani", "South Asia"],
        ]),
    },
    "general-knowledge-g5-l20": {
        "data_table": table(["Language Family", "Example Languages"], [
            ["Indo-European", "English, Hindi, Spanish"], ["Sino-Tibetan", "Mandarin, Burmese"],
        ]),
    },
    "general-knowledge-g5-l21": {
        "data_table": table(["Calendar", "Basis"], [
            ["Gregorian calendar", "Solar year, used internationally"], ["Islamic (Hijri) calendar", "Lunar cycles"],
        ]),
    },
    "general-knowledge-g5-l22": {
        "data_table": table(["Inventor", "Invention"], [
            ["Alexander Graham Bell", "Telephone"], ["The Wright brothers", "Powered airplane"],
        ]),
    },
    "general-knowledge-g5-l23": {
        "data_table": table(["Country", "Capital"], [
            ["France", "Paris"], ["Japan", "Tokyo"], ["Bangladesh", "Dhaka"],
        ]),
    },
    "general-knowledge-g5-l24": {
        "data_table": table(["Sport", "Popular Region"], [
            ["Cricket", "South Asia, England, Australia"], ["Football (soccer)", "Most of the world"],
        ]),
    },
    "general-knowledge-g5-l25": {
        "data_table": table(["Trade Good", "Route"], [
            ["Silk", "Silk Road"], ["Spices", "Spice Route"],
        ]),
    },
    "general-knowledge-g5-l26": {
        "data_table": table(["Bridge", "Location"], [
            ["Golden Gate Bridge", "San Francisco, USA"], ["Akashi Kaikyo Bridge", "Japan"],
        ]),
    },
    "general-knowledge-g5-l27": {
        "data_table": table(["Holiday", "Celebrated By"], [
            ["Eid al-Fitr", "Muslim communities worldwide"], ["Diwali", "Hindu communities worldwide"],
        ]),
    },
    "general-knowledge-g5-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Largest continent", "Asia"], ["Largest ocean", "Pacific Ocean"],
        ]),
    },
    "general-knowledge-g5-l29": {
        "data_table": table(["Museum", "Location"], [
            ["The Louvre", "Paris, France"], ["The British Museum", "London, UK"],
        ]),
    },
    "general-knowledge-g5-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Current events", "Things happening in the news right now"],
            ["Reliable source", "A news outlet that checks facts before publishing"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 General Knowledge lessons (completing 30/30).")


if __name__ == "__main__":
    main()
