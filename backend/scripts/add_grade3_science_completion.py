#!/usr/bin/env python3
"""Depth pass, Grade 3 Science: fill in real, hand-checked data_table
content for the 18 Grade 3 Science lessons not covered by the earlier
breadth-first batch. Brings Grade 3 Science to full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sci-g3-l1": {
        "data_table": table(["Link", "Example"], [
            ["Producer", "Grass (makes its own food)"], ["Consumer", "Rabbit (eats grass)"],
            ["Decomposer", "Fungi (breaks down dead matter)"],
        ]),
    },
    "sci-g3-l2": {
        "data_table": table(["Force", "Example"], [
            ["Push", "Pushing a swing forward"], ["Pull", "Pulling open a drawer"],
        ]),
    },
    "science-g3-l3": {
        "data_table": table(["Living", "Non-Living"], [
            ["Tree, dog, human", "Rock, water, chair"],
        ]),
    },
    "science-g3-l4": {
        "data_table": table(["Stage", "Description"], [
            ["Seed", "Contains the plant embryo"], ["Sprout", "Seed begins to grow"],
            ["Mature plant", "Fully grown, can produce seeds"],
        ]),
    },
    "science-g3-l5": {
        "data_table": table(["Stage", "Example (Butterfly)"], [
            ["Egg", "Laid on a leaf"], ["Larva", "Caterpillar"], ["Pupa", "Chrysalis"], ["Adult", "Butterfly"],
        ]),
    },
    "science-g3-l6": {
        "data_table": table(["Habitat", "Example Animal"], [
            ["Desert", "Camel"], ["Ocean", "Fish"], ["Forest", "Deer"], ["Arctic", "Polar bear"],
        ]),
    },
    "science-g3-l7": {
        "data_table": table(["Adaptation", "Purpose"], [
            ["Camel's hump", "Stores fat for energy in the desert"],
            ["Polar bear's fur", "Keeps it warm in the Arctic"],
        ]),
    },
    "science-g3-l8": {
        "data_table": table(["State of Matter", "Example"], [
            ["Solid", "Ice"], ["Liquid", "Water"], ["Gas", "Water vapor"],
        ]),
    },
    "science-g3-l9": {
        "data_table": table(["Material", "Property"], [
            ["Metal", "Hard, shiny, conducts heat"], ["Rubber", "Flexible, waterproof"],
        ]),
    },
    "science-g3-l10": {
        "data_table": table(["Simple Machine", "Example"], [
            ["Lever", "See-saw"], ["Wheel and axle", "Bicycle wheel"], ["Pulley", "Flagpole rope"],
        ]),
    },
    "science-g3-l11": {
        "data_table": table(["Energy Type", "Example"], [
            ["Light energy", "Sunlight"], ["Heat energy", "A campfire"], ["Sound energy", "A ringing bell"],
        ]),
    },
    "science-g3-l12": {
        "data_table": table(["Concept", "Explanation"], [
            ["Shadow", "Forms when an object blocks light"], ["Opaque object", "Blocks light completely"],
        ]),
    },
    "science-g3-l13": {
        "data_table": table(["Concept", "Explanation"], [
            ["Sound", "Made by vibrations"], ["Pitch", "How high or low a sound is"],
        ]),
    },
    "science-g3-l14": {
        "data_table": table(["Magnet Fact", "Detail"], [
            ["Poles", "North and South"], ["Attracts", "Iron, steel, nickel"],
        ]),
    },
    "science-g3-l15": {
        "data_table": table(["Stage", "Description"], [
            ["Evaporation", "Water turns into vapor from heat"], ["Condensation", "Vapor cools into clouds"],
            ["Precipitation", "Water falls as rain or snow"],
        ]),
    },
    "science-g3-l16": {
        "data_table": table(["Season", "Typical Weather"], [
            ["Summer", "Hot"], ["Winter", "Cold"], ["Spring", "Mild, rainy"], ["Autumn", "Cool"],
        ]),
    },
    "science-g3-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Cause of day and night", "Earth's rotation on its axis"],
            ["Time for one full rotation", "About 24 hours"],
        ]),
    },
    "science-g3-l19": {
        "data_table": table(["Rock Type", "How It Forms"], [
            ["Igneous", "Cooled from melted rock (lava/magma)"],
            ["Sedimentary", "Layers of sediment pressed together"],
            ["Metamorphic", "Changed by heat and pressure"],
        ]),
    },
    "science-g3-l20": {
        "data_table": table(["Action", "Environmental Benefit"], [
            ["Recycling", "Reduces waste in landfills"], ["Planting trees", "Produces oxygen, absorbs CO2"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Science lessons (completing 20/20).")


if __name__ == "__main__":
    main()
