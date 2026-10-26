#!/usr/bin/env python3
"""Depth pass, Grade 2 Science: fill in real, hand-checked data_table
content for the 18 Grade 2 Science lessons not covered by the earlier
breadth-first batch. Brings Grade 2 Science to full 20/20 coverage.

Every fact is real (the water cycle stages, food chain roles, real bone
count, real simple machine examples) -- nothing fabricated or presented
as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sci-g2-l2": {
        "data_table": table(["Stage", "Description"], [
            ["Evaporation", "Water turns into vapor and rises"],
            ["Condensation", "Vapor cools and forms clouds"],
            ["Precipitation", "Water falls as rain or snow"],
        ]),
    },
    "science-g2-l3": {
        "data_table": table(["Category", "Examples"], [
            ["Living", "Plants, animals, people"], ["Non-living", "Rocks, water, air"],
        ]),
    },
    "science-g2-l4": {
        "data_table": table(["Plant Part", "Function"], [
            ["Roots", "Absorb water and nutrients, anchor the plant"],
            ["Stem", "Supports the plant, carries water and nutrients"],
            ["Leaves", "Make food from sunlight (photosynthesis)"],
            ["Flower", "Makes seeds for new plants"],
        ]),
    },
    "science-g2-l5": {
        "data_table": table(["Stage", "Description"], [
            ["Seed", "Contains the beginning of a new plant"],
            ["Sprout", "The seed begins to grow"], ["Seedling", "A young plant"],
            ["Mature Plant", "Fully grown, may flower and make seeds"],
        ]),
    },
    "science-g2-l6": {
        "data_table": table(["Stage", "Description"], [
            ["Egg", "Laid on a leaf"], ["Larva (Caterpillar)", "Eats and grows"],
            ["Pupa (Chrysalis)", "Transforms inside a case"], ["Adult Butterfly", "Emerges and can fly"],
        ]),
    },
    "science-g2-l7": {
        "data_table": table(["Habitat", "Example Animal"], [
            ["Ocean", "Fish"], ["Forest", "Deer"], ["Desert", "Camel"], ["Arctic", "Polar bear"],
        ]),
    },
    "science-g2-l9": {
        "data_table": table(["Role", "Example"], [
            ["Producer", "Grass (makes its own food)"], ["Consumer", "Rabbit (eats the grass)"],
            ["Predator", "Fox (eats the rabbit)"],
        ]),
    },
    "science-g2-l10": {
        "data_table": table(["Sense", "Body Part"], [
            ["Sight", "Eyes"], ["Hearing", "Ears"], ["Smell", "Nose"], ["Taste", "Tongue"], ["Touch", "Skin"],
        ]),
    },
    "science-g2-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Number of bones in the adult human body", "206"],
            ["Muscles work in pairs by", "Contracting and relaxing"],
        ]),
    },
    "science-g2-l12": {
        "data_table": table(["Simple Machine", "Example"], [
            ["Lever", "Seesaw"], ["Wheel and axle", "Bicycle wheel"], ["Pulley", "Flagpole rope"],
        ]),
    },
    "science-g2-l13": {
        "data_table": table(["Material", "Attracted to Magnets?"], [
            ["Iron", "Yes"], ["Steel", "Yes"], ["Plastic", "No"], ["Wood", "No"],
        ]),
    },
    "science-g2-l14": {
        "data_table": table(["Force", "Example"], [
            ["Push", "Pushing a door open"], ["Pull", "Pulling a wagon"],
        ]),
    },
    "science-g2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Shadow", "A dark shape formed when an object blocks light"],
            ["Opaque object", "Blocks light completely"],
        ]),
    },
    "science-g2-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Sound is made by", "Vibrations"], ["Ear part that senses sound", "Eardrum"],
        ]),
    },
    "science-g2-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Earth's surface covered by water", "About 71%"], ["Earth's surface covered by land", "About 29%"],
        ]),
    },
    "science-g2-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Day happens when", "Your part of Earth faces the Sun"],
            ["Night happens when", "Your part of Earth faces away from the Sun"],
            ["Earth rotates once every", "24 hours"],
        ]),
    },
    "science-g2-l19": {
        "data_table": table(["Season", "Months (Northern Hemisphere)"], [
            ["Spring", "March, April, May"], ["Summer", "June, July, August"],
            ["Autumn / Fall", "September, October, November"], ["Winter", "December, January, February"],
        ]),
    },
    "science-g2-l20": {
        "data_table": table(["Planet", "Position from the Sun"], [
            ["Mercury", "1"], ["Venus", "2"], ["Earth", "3"], ["Mars", "4"],
            ["Jupiter", "5"], ["Saturn", "6"], ["Uranus", "7"], ["Neptune", "8"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 Science lessons (completing 20/20).")


if __name__ == "__main__":
    main()
