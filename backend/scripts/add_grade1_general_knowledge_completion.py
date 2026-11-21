#!/usr/bin/env python3
"""Depth pass, Grade 1 General Knowledge: fill in real, hand-checked
data_table content for the 17 Grade 1 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings Grade 1 General
Knowledge to full 20/20 coverage.

Every fact is real (continent/ocean counts, real landmarks and their
countries, real emergency numbers, real inventors) -- nothing fabricated
or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "gk-g1-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Number of continents", "7"], ["Number of oceans", "5"],
        ]),
    },
    "general-knowledge-g1-l4": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Flag", "Represents a country's identity"], ["Anthem", "A country's official patriotic song"],
        ]),
    },
    "general-knowledge-g1-l5": {
        "data_table": table(["Landmark", "Country"], [
            ["Eiffel Tower", "France"], ["Great Wall", "China"], ["Statue of Liberty", "USA"],
        ]),
    },
    "general-knowledge-g1-l6": {
        "data_table": table(["Animal", "Habitat"], [
            ["Lion", "African savanna"], ["Polar Bear", "Arctic"], ["Tiger", "Asian forests"],
        ]),
    },
    "general-knowledge-g1-l7": {
        "data_table": table(["Pet", "Basic Care"], [
            ["Dog", "Food, water, walks"], ["Fish", "Clean water and food"], ["Cat", "Food, water, litter box"],
        ]),
    },
    "general-knowledge-g1-l8": {
        "data_table": table(["Type", "Examples"], [
            ["Fruits", "Apples, bananas, oranges"], ["Vegetables", "Carrots, broccoli, potatoes"],
        ]),
    },
    "general-knowledge-g1-l9": {
        "data_table": table(["Transport", "Environment"], [
            ["Car", "Road"], ["Boat", "Water"], ["Airplane", "Air"],
        ]),
    },
    "general-knowledge-g1-l10": {
        "data_table": table(["Helper", "Job"], [
            ["Doctor", "Helps sick people"], ["Police officer", "Keeps people safe"],
            ["Teacher", "Helps children learn"],
        ]),
    },
    "general-knowledge-g1-l11": {
        "data_table": table(["Rule", "Why"], [
            ["Don't touch hot stoves", "Prevents burns"],
            ["Keep medicines out of reach", "Prevents accidental poisoning"],
        ]),
    },
    "general-knowledge-g1-l12": {
        "data_table": table(["Rule", "Why"], [
            ["Look both ways before crossing", "Prevents being hit by a vehicle"],
            ["Hold an adult's hand", "Stays safe near traffic"],
        ]),
    },
    "general-knowledge-g1-l13": {
        "data_table": table(["Manner", "Example"], [
            ["Politeness", "Saying 'please' and 'thank you'"],
            ["Table manners", "Chewing with your mouth closed"],
        ]),
    },
    "general-knowledge-g1-l14": {
        "data_table": table(["Material", "Can Be Recycled Into"], [
            ["Paper", "New paper products"], ["Plastic bottles", "New plastic items"],
            ["Aluminum cans", "New cans"],
        ]),
    },
    "general-knowledge-g1-l15": {
        "data_table": table(["Technology", "Everyday Use"], [
            ["Telephone", "Talking to people far away"], ["Refrigerator", "Keeping food cold"],
        ]),
    },
    "general-knowledge-g1-l16": {
        "data_table": table(["Sport", "Popular In"], [
            ["Soccer/Football", "Worldwide, especially Europe and South America"],
            ["Cricket", "India, UK, Australia"], ["Sumo wrestling", "Japan"],
        ]),
    },
    "general-knowledge-g1-l17": {
        "data_table": table(["Festival", "Country/Region"], [
            ["Diwali", "India"], ["Chinese New Year", "China"], ["Christmas", "Celebrated worldwide"],
        ]),
    },
    "general-knowledge-g1-l18": {
        "data_table": table(["Inventor", "Invention"], [
            ["Thomas Edison", "Light bulb (practical version)"], ["Alexander Graham Bell", "Telephone"],
        ]),
    },
    "general-knowledge-g1-l19": {
        "data_table": table(["Country", "Emergency Number"], [
            ["USA", "911"], ["UK", "999"], ["EU", "112"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 General Knowledge lessons (completing 20/20).")


if __name__ == "__main__":
    main()
