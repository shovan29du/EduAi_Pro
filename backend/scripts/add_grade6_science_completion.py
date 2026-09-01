#!/usr/bin/env python3
"""Depth pass, Grade 6 Science: fill in real, hand-checked data_table
content for the 28 Grade 6 Science lessons not covered by the earlier
breadth-first batch. Brings Grade 6 Science to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sci-g6-l2": {
        "data_table": table(["Body System", "Function"], [
            ["Circulatory", "Moves blood through the body"], ["Digestive", "Breaks down food"],
        ]),
    },
    "science-g6-l3": {
        "data_table": table(["Step", "Purpose"], [
            ["Hypothesis", "A testable prediction"], ["Experiment", "Tests the hypothesis"], ["Conclusion", "Interprets the results"],
        ]),
    },
    "science-g6-l4": {
        "data_table": table(["State", "Example"], [
            ["Solid", "Ice"], ["Liquid", "Water"], ["Gas", "Steam"],
        ]),
    },
    "science-g6-l5": {
        "data_table": table(["Change Type", "Example"], [
            ["Physical change", "Ice melting into water"], ["Chemical change", "Wood burning into ash"],
        ]),
    },
    "science-g6-l6": {
        "data_table": table(["Term", "Example"], [
            ["Mixture", "Ingredients can be separated, like a salad"],
            ["Solution", "Fully dissolved, like salt water"],
        ]),
    },
    "science-g6-l7": {
        "data_table": table(["Cell Structure", "Function"], [
            ["Nucleus", "Controls the cell, holds DNA"], ["Mitochondria", "Produces energy for the cell"],
        ]),
    },
    "science-g6-l8": {
        "data_table": table(["Input", "Output"], [
            ["Sunlight, water, CO2", "Glucose (sugar) and oxygen"],
        ]),
    },
    "science-g6-l9": {
        "data_table": table(["Term", "Example"], [
            ["Food chain", "Grass to rabbit to fox"], ["Food web", "Multiple connected food chains"],
        ]),
    },
    "science-g6-l10": {
        "data_table": table(["Group", "Example"], [
            ["Mammals", "Dogs, whales"], ["Reptiles", "Snakes, lizards"],
        ]),
    },
    "science-g6-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Gene", "A unit of heredity passed from parent to offspring"],
            ["Trait", "A characteristic influenced by genes"],
        ]),
    },
    "science-g6-l12": {
        "data_table": table(["Force", "Effect"], [
            ["Gravity", "Pulls objects toward Earth"], ["Friction", "Slows down moving objects"],
        ]),
    },
    "science-g6-l14": {
        "data_table": table(["Simple Machine", "Example"], [
            ["Lever", "See-saw"], ["Pulley", "Flagpole"], ["Inclined plane", "Ramp"],
        ]),
    },
    "science-g6-l15": {
        "data_table": table(["Energy Type", "Example"], [
            ["Kinetic energy", "A moving ball"], ["Potential energy", "A stretched rubber band"],
        ]),
    },
    "science-g6-l16": {
        "data_table": table(["Circuit Type", "Description"], [
            ["Closed circuit", "A complete loop; current flows"], ["Open circuit", "A broken loop; current stops"],
        ]),
    },
    "science-g6-l17": {
        "data_table": table(["Magnet Fact", "Detail"], [
            ["Poles", "North and South"], ["Like poles", "Repel each other"],
        ]),
    },
    "science-g6-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Sound", "Created by vibrations, travels as waves"],
            ["Pitch", "How high or low a sound is, based on frequency"],
        ]),
    },
    "science-g6-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Reflection", "Light bouncing off a surface"], ["Refraction", "Light bending as it passes through a medium"],
        ]),
    },
    "science-g6-l20": {
        "data_table": table(["Planet", "Position from Sun"], [
            ["Mercury", "1st"], ["Earth", "3rd"], ["Jupiter", "5th"],
        ]),
    },
    "science-g6-l21": {
        "data_table": table(["Layer", "Description"], [
            ["Crust", "Thin outer layer"], ["Mantle", "Thick, hot layer beneath the crust"],
        ]),
    },
    "science-g6-l22": {
        "data_table": table(["Rock Type", "Formation"], [
            ["Igneous", "Cooled lava or magma"], ["Sedimentary", "Compressed layers of sediment"],
            ["Metamorphic", "Changed by heat and pressure"],
        ]),
    },
    "science-g6-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Weathering", "Breaking down of rock"], ["Erosion", "Movement of weathered material"],
        ]),
    },
    "science-g6-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather", "Day-to-day atmospheric conditions"], ["Climate", "Average weather over many years"],
        ]),
    },
    "science-g6-l25": {
        "data_table": table(["Stage", "Description"], [
            ["Evaporation", "Water turns into vapor"], ["Precipitation", "Water falls as rain or snow"],
        ]),
    },
    "science-g6-l26": {
        "data_table": table(["Event", "Cause"], [
            ["Earthquake", "Movement of tectonic plates"], ["Volcanic eruption", "Magma rising through the crust"],
        ]),
    },
    "science-g6-l27": {
        "data_table": table(["Resource Type", "Example"], [
            ["Renewable", "Solar, wind, water"], ["Nonrenewable", "Coal, oil, natural gas"],
        ]),
    },
    "science-g6-l28": {
        "data_table": table(["Conservation Action", "Benefit"], [
            ["Recycling", "Reduces waste in landfills"], ["Protecting habitats", "Preserves biodiversity"],
        ]),
    },
    "science-g6-l29": {
        "data_table": table(["Microorganism", "Example Effect"], [
            ["Bacteria", "Can cause illness or aid digestion"], ["Virus", "Causes illnesses like the common cold"],
        ]),
    },
    "science-g6-l30": {
        "data_table": table(["Safety Rule", "Why"], [
            ["Wear safety goggles", "Protects eyes from chemicals"], ["Follow the teacher's instructions", "Prevents accidents"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Science lessons (completing 30/30).")


if __name__ == "__main__":
    main()
