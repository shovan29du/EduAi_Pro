#!/usr/bin/env python3
"""Depth pass, Grade 2 General Knowledge: fill in real, hand-checked
data_table content for the 18 Grade 2 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings Grade 2 General
Knowledge to full 20/20 coverage.

Every fact is real (blue whale is the largest animal, real building
facts, real conservation statuses) -- nothing fabricated or presented as
fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "gk-g2-l1": {
        "data_table": table(["Country", "Flag Colors"], [
            ["USA", "Red, White, Blue"], ["Japan", "White, Red"], ["Brazil", "Green, Yellow, Blue"],
        ]),
    },
    "general-knowledge-g2-l2": {
        "data_table": table(["Landmark", "Country"], [
            ["Eiffel Tower", "France"], ["Great Wall", "China"], ["Statue of Liberty", "USA"],
        ]),
    },
    "general-knowledge-g2-l4": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Flag", "Represents a country's identity"], ["Anthem", "A country's official patriotic song"],
        ]),
    },
    "general-knowledge-g2-l5": {
        "data_table": table(["Inventor", "Invention"], [
            ["Thomas Edison", "Light bulb (practical version)"], ["Alexander Graham Bell", "Telephone"],
        ]),
    },
    "general-knowledge-g2-l7": {
        "data_table": table(["Ocean Animal", "Fact"], [
            ["Blue whale", "The largest animal on Earth"], ["Octopus", "Has 8 arms and 3 hearts"],
        ]),
    },
    "general-knowledge-g2-l8": {
        "data_table": table(["Animal", "Continent"], [
            ["Kangaroo", "Australia"], ["Panda", "Asia (China)"], ["Lion", "Africa"],
        ]),
    },
    "general-knowledge-g2-l9": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"],
            ["Marco Polo", "Travels along the Silk Road to China"],
        ]),
    },
    "general-knowledge-g2-l10": {
        "data_table": table(["Language", "Spoken Widely In"], [
            ["Mandarin Chinese", "China"], ["Spanish", "Spain, Latin America"],
            ["English", "UK, USA, and worldwide"],
        ]),
    },
    "general-knowledge-g2-l11": {
        "data_table": table(["Food", "Country"], [
            ["Sushi", "Japan"], ["Pizza", "Italy"], ["Tacos", "Mexico"],
        ]),
    },
    "general-knowledge-g2-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Number of standard time zones", "24"],
            ["Why time zones exist", "Earth rotates, so different places face the sun at different times"],
        ]),
    },
    "general-knowledge-g2-l13": {
        "data_table": table(["Festival", "Country/Region"], [
            ["Diwali", "India"], ["Chinese New Year", "China"], ["Christmas", "Celebrated worldwide"],
        ]),
    },
    "general-knowledge-g2-l14": {
        "data_table": table(["Invention", "Inventor/Era"], [
            ["The wheel", "Ancient Mesopotamia, c. 3500 BCE"], ["The automobile", "Karl Benz, 1885-1886"],
        ]),
    },
    "general-knowledge-g2-l15": {
        "data_table": table(["Sport", "Popular In"], [
            ["Soccer/Football", "Worldwide, especially Europe and South America"],
            ["Cricket", "India, UK, Australia"], ["Sumo wrestling", "Japan"],
        ]),
    },
    "general-knowledge-g2-l16": {
        "data_table": table(["Building", "Location"], [
            ["Burj Khalifa", "Dubai, UAE (tallest building in the world)"],
            ["Colosseum", "Rome, Italy"],
        ]),
    },
    "general-knowledge-g2-l17": {
        "data_table": table(["Animal", "Conservation Status"], [
            ["Giant Panda", "Vulnerable"], ["Sumatran Tiger", "Critically Endangered"],
        ]),
    },
    "general-knowledge-g2-l18": {
        "data_table": table(["Material", "Can Be Recycled Into"], [
            ["Paper", "New paper products"], ["Plastic bottles", "New plastic items"],
            ["Aluminum cans", "New cans"],
        ]),
    },
    "general-knowledge-g2-l19": {
        "data_table": table(["Helper", "Job"], [
            ["Doctor", "Helps sick people"], ["Police officer", "Keeps people safe"],
            ["Teacher", "Helps children learn"],
        ]),
    },
    "general-knowledge-g2-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Number of bones in the adult human body", "206"], ["Largest organ", "Skin"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 General Knowledge lessons (completing 20/20).")


if __name__ == "__main__":
    main()
