#!/usr/bin/env python3
"""Depth pass, Grade 4 Science: fill in real, hand-checked data_table
content for the 28 Grade 4 Science lessons not covered by the earlier
breadth-first batch. Brings Grade 4 Science to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sci-g4-l1": {
        "data_table": table(["Planet", "Position from Sun"], [
            ["Mercury", "1st"], ["Venus", "2nd"], ["Earth", "3rd"], ["Mars", "4th"],
        ]),
    },
    "science-g4-l3": {
        "data_table": table(["State", "Example"], [
            ["Solid", "Ice"], ["Liquid", "Water"], ["Gas", "Steam"],
        ]),
    },
    "science-g4-l4": {
        "data_table": table(["Stage", "Description"], [
            ["Evaporation", "Water turns to vapor"], ["Condensation", "Vapor forms clouds"],
            ["Precipitation", "Water falls as rain"],
        ]),
    },
    "science-g4-l5": {
        "data_table": table(["Simple Machine", "Example"], [
            ["Lever", "See-saw"], ["Pulley", "Flagpole"], ["Wedge", "Axe"],
        ]),
    },
    "science-g4-l6": {
        "data_table": table(["Force", "Effect"], [
            ["Gravity", "Pulls objects toward Earth"], ["Friction", "Slows down moving objects"],
        ]),
    },
    "science-g4-l7": {
        "data_table": table(["Plant Part", "Function"], [
            ["Roots", "Absorb water and nutrients"], ["Leaves", "Make food via photosynthesis"],
        ]),
    },
    "science-g4-l8": {
        "data_table": table(["Stage (Frog)", "Description"], [
            ["Egg", "Laid in water"], ["Tadpole", "Swims, breathes with gills"], ["Adult frog", "Breathes with lungs"],
        ]),
    },
    "science-g4-l9": {
        "data_table": table(["Term", "Example"], [
            ["Food chain", "Grass to rabbit to fox"], ["Food web", "Multiple connected food chains"],
        ]),
    },
    "science-g4-l10": {
        "data_table": table(["Ecosystem", "Example Species"], [
            ["Rainforest", "Toucan, jaguar"], ["Desert", "Camel, cactus"],
        ]),
    },
    "science-g4-l11": {
        "data_table": table(["Rock Type", "Formation"], [
            ["Igneous", "Cooled lava or magma"], ["Sedimentary", "Compressed layers of sediment"],
        ]),
    },
    "science-g4-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather", "Day-to-day atmospheric conditions"], ["Climate", "Average weather over many years"],
        ]),
    },
    "science-g4-l14": {
        "data_table": table(["Organ", "Function"], [
            ["Stomach", "Breaks down food with acid"], ["Small intestine", "Absorbs nutrients"],
        ]),
    },
    "science-g4-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Sound", "Created by vibrations"], ["Eardrum", "Vibrates to let us hear"],
        ]),
    },
    "science-g4-l16": {
        "data_table": table(["Concept", "Explanation"], [
            ["Shadow", "Forms when light is blocked"], ["Transparent object", "Lets light pass through"],
        ]),
    },
    "science-g4-l17": {
        "data_table": table(["Magnet Fact", "Detail"], [
            ["Poles", "North and South"], ["Like poles", "Repel each other"], ["Opposite poles", "Attract each other"],
        ]),
    },
    "science-g4-l18": {
        "data_table": table(["Energy Type", "Example"], [
            ["Kinetic energy", "Energy of motion, like a rolling ball"], ["Potential energy", "Stored energy, like a stretched rubber band"],
        ]),
    },
    "science-g4-l19": {
        "data_table": table(["Adaptation", "Purpose"], [
            ["Giraffe's long neck", "Reaches leaves high in trees"], ["Chameleon's color change", "Camouflage"],
        ]),
    },
    "science-g4-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Hypothesis", "A testable prediction"], ["Fair test", "Changing only one variable at a time"],
        ]),
    },
    "science-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Navigation", "Using star patterns to find direction at night"],
        ]),
    },
    "science-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Home wiring", "A closed circuit powers a light bulb"],
        ]),
    },
    "science-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Cooking", "Water changes from liquid to gas when boiled"],
        ]),
    },
    "science-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Rain forecasting", "Understanding evaporation and condensation"],
        ]),
    },
    "science-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Moving heavy furniture", "Using a ramp (inclined plane)"],
        ]),
    },
    "science-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Riding a bike", "Pedaling applies force to move forward"],
        ]),
    },
    "science-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Gardening", "Understanding what a plant needs to grow"],
        ]),
    },
    "science-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Raising pets", "Understanding an animal's growth stages"],
        ]),
    },
    "science-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Farming", "Understanding how removing one species affects others"],
        ]),
    },
    "science-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Conservation", "Protecting habitats to preserve ecosystems"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Science lessons (completing 30/30).")


if __name__ == "__main__":
    main()
