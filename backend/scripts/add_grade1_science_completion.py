#!/usr/bin/env python3
"""Depth pass, Grade 1 Science: fill in real, hand-checked data_table
content for the 17 Grade 1 Science lessons not covered by the earlier
breadth-first batch. Brings Grade 1 Science to full 20/20 coverage.

Every fact is real (animal baby names, butterfly/plant life cycle stages,
real magnet-attraction facts, real rock formation types) -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sci-g1-l1": {
        "data_table": table(["Category", "Examples"], [
            ["Living", "Plants, animals, people"], ["Non-living", "Rocks, water, air"],
        ]),
    },
    "sci-g1-l3": {
        "data_table": table(["Habitat", "Example Animal"], [
            ["Ocean", "Fish"], ["Forest", "Deer"], ["Desert", "Camel"], ["Arctic", "Polar bear"],
        ]),
    },
    "science-g1-l4": {
        "data_table": table(["Sense", "Body Part"], [
            ["Sight", "Eyes"], ["Hearing", "Ears"], ["Smell", "Nose"], ["Taste", "Tongue"], ["Touch", "Skin"],
        ]),
    },
    "science-g1-l5": {
        "data_table": table(["Season", "Months (Northern Hemisphere)"], [
            ["Spring", "March, April, May"], ["Summer", "June, July, August"],
            ["Autumn / Fall", "September, October, November"], ["Winter", "December, January, February"],
        ]),
    },
    "science-g1-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Day happens when", "Your part of Earth faces the Sun"],
            ["Night happens when", "Your part of Earth faces away from the Sun"],
            ["Earth rotates once every", "24 hours"],
        ]),
    },
    "science-g1-l8": {
        "data_table": table(["Animal", "Baby Name"], [
            ["Dog", "Puppy"], ["Cat", "Kitten"], ["Cow", "Calf"], ["Horse", "Foal"],
        ]),
    },
    "science-g1-l9": {
        "data_table": table(["Stage", "Description"], [
            ["Egg", "Laid on a leaf"], ["Larva (Caterpillar)", "Eats and grows"],
            ["Pupa (Chrysalis)", "Transforms inside a case"], ["Adult Butterfly", "Emerges and can fly"],
        ]),
    },
    "science-g1-l10": {
        "data_table": table(["Stage", "Description"], [
            ["Seed", "Contains the beginning of a new plant"],
            ["Sprout", "The seed begins to grow"], ["Seedling", "A young plant"],
            ["Mature Plant", "Fully grown, may flower and make seeds"],
        ]),
    },
    "science-g1-l11": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    "science-g1-l12": {
        "data_table": table(["Body Part", "Function"], [
            ["Heart", "Pumps blood"], ["Lungs", "Help you breathe"], ["Brain", "Controls your body and thoughts"],
        ]),
    },
    "science-g1-l13": {
        "data_table": table(["Use of Water", "Example"], [
            ["Drinking", "Staying hydrated"], ["Washing", "Cleaning hands and dishes"],
            ["Growing food", "Watering plants"],
        ]),
    },
    "science-g1-l15": {
        "data_table": table(["Force", "Example"], [
            ["Push", "Pushing a door open"], ["Pull", "Pulling a wagon"],
        ]),
    },
    "science-g1-l16": {
        "data_table": table(["Material", "Attracted to Magnets?"], [
            ["Iron", "Yes"], ["Steel", "Yes"], ["Plastic", "No"], ["Wood", "No"],
        ]),
    },
    "science-g1-l17": {
        "data_table": table(["Object", "Floats or Sinks (in water)"], [
            ["Wooden block", "Floats"], ["Rock", "Sinks"], ["Rubber duck", "Floats"],
        ]),
    },
    "science-g1-l18": {
        "data_table": table(["Action", "How It Helps"], [
            ["Recycling", "Reduces waste sent to landfills"],
            ["Turning off lights", "Saves energy"],
            ["Planting trees", "Provides oxygen and habitats"],
        ]),
    },
    "science-g1-l19": {
        "data_table": table(["Rock Type", "How It Forms"], [
            ["Igneous", "From cooled melted rock (magma/lava)"],
            ["Sedimentary", "From layers of sediment pressed together"],
            ["Metamorphic", "From existing rock changed by heat and pressure"],
        ]),
    },
    "science-g1-l20": {
        "data_table": table(["Simple Machine", "How It Helps"], [
            ["Ramp (inclined plane)", "Makes it easier to move objects up/down"],
            ["Wheel and axle", "Reduces friction so things move more easily"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 Science lessons (completing 20/20).")


if __name__ == "__main__":
    main()
