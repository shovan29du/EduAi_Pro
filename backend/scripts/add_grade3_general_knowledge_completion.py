#!/usr/bin/env python3
"""Depth pass, Grade 3 General Knowledge: fill in real, hand-checked
data_table content for the 18 Grade 3 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings Grade 3 General
Knowledge to full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "gk-g3-l1": {
        "data_table": table(["Wonder", "Location"], [
            ["Great Wall of China", "China"], ["Taj Mahal", "India"], ["Great Pyramid of Giza", "Egypt"],
        ]),
    },
    "general-knowledge-g3-l2": {
        "data_table": table(["Country", "Flag Colors"], [
            ["Japan", "White and red"], ["Bangladesh", "Green and red"], ["France", "Blue, white, and red"],
        ]),
    },
    "general-knowledge-g3-l3": {
        "data_table": table(["Inventor", "Invention"], [
            ["Thomas Edison", "Practical light bulb"], ["Alexander Graham Bell", "Telephone"],
        ]),
    },
    "general-knowledge-g3-l4": {
        "data_table": table(["Animal", "Continent"], [
            ["Kangaroo", "Australia"], ["Panda", "Asia"], ["Lion", "Africa"],
        ]),
    },
    "general-knowledge-g3-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Closest planet to the sun", "Mercury"], ["Largest planet", "Jupiter"],
        ]),
    },
    "general-knowledge-g3-l6": {
        "data_table": table(["Helper", "Role"], [
            ["Firefighter", "Puts out fires and rescues people"], ["Doctor", "Treats illness and injury"],
        ]),
    },
    "general-knowledge-g3-l7": {
        "data_table": table(["Country", "Currency"], [
            ["United States", "Dollar"], ["Japan", "Yen"], ["Bangladesh", "Taka"], ["United Kingdom", "Pound"],
        ]),
    },
    "general-knowledge-g3-l8": {
        "data_table": table(["Landmark", "Country"], [
            ["Eiffel Tower", "France"], ["Statue of Liberty", "United States"],
        ]),
    },
    "general-knowledge-g3-l9": {
        "data_table": table(["Sport", "Popular Country"], [
            ["Cricket", "India, Bangladesh, England, Australia"], ["Football (soccer)", "Brazil, most of Europe"],
        ]),
    },
    "general-knowledge-g3-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Bones in an adult human body", "206"], ["Largest organ", "Skin"],
        ]),
    },
    "general-knowledge-g3-l11": {
        "data_table": table(["Language", "Spoken Mainly In"], [
            ["Mandarin", "China"], ["Spanish", "Spain, Latin America"], ["Bangla", "Bangladesh, parts of India"],
        ]),
    },
    "general-knowledge-g3-l13": {
        "data_table": table(["Holiday", "Celebrated In"], [
            ["Eid al-Fitr", "Muslim communities worldwide"], ["Diwali", "India and Hindu communities worldwide"],
        ]),
    },
    "general-knowledge-g3-l14": {
        "data_table": table(["Animal", "Status"], [
            ["Giant panda", "Vulnerable"], ["Bengal tiger", "Endangered"],
        ]),
    },
    "general-knowledge-g3-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Largest continent", "Asia"], ["Largest ocean", "Pacific Ocean"],
        ]),
    },
    "general-knowledge-g3-l16": {
        "data_table": table(["Invention", "Impact"], [
            ["The airplane", "Made long-distance travel fast"], ["The train", "Enabled overland mass transport"],
        ]),
    },
    "general-knowledge-g3-l17": {
        "data_table": table(["Explorer", "Known For"], [
            ["Ferdinand Magellan", "First expedition to circumnavigate the globe"],
            ["Ibn Battuta", "Extensive travels across Africa and Asia"],
        ]),
    },
    "general-knowledge-g3-l18": {
        "data_table": table(["Material", "Can Be Recycled Into"], [
            ["Plastic bottle", "New plastic products"], ["Paper", "New paper products"],
        ]),
    },
    "general-knowledge-g3-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Venus flytrap", "A plant that eats insects"], ["Bioluminescence", "Living things that glow, like fireflies"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 General Knowledge lessons (completing 20/20).")


if __name__ == "__main__":
    main()
