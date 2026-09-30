#!/usr/bin/env python3
"""Depth pass, Grade 5 Science: fill in real, hand-checked data_table
content for the 28 Grade 5 Science lessons not covered by the earlier
breadth-first batch. Brings Grade 5 Science to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sci-g5-l1": {
        "data_table": table(["Cell Structure", "Function"], [
            ["Nucleus", "Controls the cell, holds DNA"], ["Cell membrane", "Controls what enters and exits"],
        ]),
    },
    "sci-g5-l2": {
        "data_table": table(["Input", "Output"], [
            ["Sunlight, water, CO2", "Glucose (sugar) and oxygen"],
        ]),
    },
    "science-g5-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Variable", "A factor that can be changed or measured"], ["Control", "The unchanged comparison group"],
        ]),
    },
    "science-g5-l4": {
        "data_table": table(["Planet", "Position from Sun"], [
            ["Mercury", "1st"], ["Venus", "2nd"], ["Earth", "3rd"], ["Mars", "4th"],
        ]),
    },
    "science-g5-l5": {
        "data_table": table(["Motion", "Effect"], [
            ["Rotation", "Causes day and night, takes about 24 hours"],
            ["Revolution", "Causes the year, takes about 365.25 days"],
        ]),
    },
    "science-g5-l6": {
        "data_table": table(["Moon Phase", "Description"], [
            ["New Moon", "Not visible"], ["Full Moon", "Fully illuminated"],
        ]),
    },
    "science-g5-l7": {
        "data_table": table(["Layer", "Description"], [
            ["Crust", "Thin outer layer"], ["Mantle", "Thick, hot layer beneath the crust"], ["Core", "Center, mostly iron and nickel"],
        ]),
    },
    "science-g5-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Volcano", "Forms when magma rises through Earth's crust"],
        ]),
    },
    "science-g5-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Weathering", "Breaking down of rock"], ["Erosion", "Movement of weathered material"],
        ]),
    },
    "science-g5-l11": {
        "data_table": table(["Rock Type", "Formation"], [
            ["Igneous", "Cooled lava or magma"], ["Sedimentary", "Compressed layers of sediment"],
            ["Metamorphic", "Changed by heat and pressure"],
        ]),
    },
    "science-g5-l12": {
        "data_table": table(["Term", "Example"], [
            ["Food chain", "Grass to rabbit to fox"], ["Food web", "Multiple connected food chains"],
        ]),
    },
    "science-g5-l13": {
        "data_table": table(["Human Impact", "Example"], [
            ["Deforestation", "Removes habitats"], ["Pollution", "Harms water and air quality"],
        ]),
    },
    "science-g5-l14": {
        "data_table": table(["Group", "Example"], [
            ["Mammals", "Dogs, whales"], ["Reptiles", "Snakes, lizards"], ["Birds", "Eagles, sparrows"],
        ]),
    },
    "science-g5-l15": {
        "data_table": table(["Category", "Example"], [
            ["Vertebrate", "Has a backbone, like a fish"], ["Invertebrate", "No backbone, like an insect"],
        ]),
    },
    "science-g5-l17": {
        "data_table": table(["Organ", "Function"], [
            ["Lungs", "Exchange oxygen and carbon dioxide"], ["Diaphragm", "Muscle that helps breathing"],
        ]),
    },
    "science-g5-l18": {
        "data_table": table(["Part", "Function"], [
            ["Brain", "Controls the body"], ["Spinal cord", "Carries signals between brain and body"],
        ]),
    },
    "science-g5-l19": {
        "data_table": table(["Property", "Example"], [
            ["Density", "How tightly packed matter is"], ["Mass", "Amount of matter in an object"],
        ]),
    },
    "science-g5-l20": {
        "data_table": table(["Term", "Example"], [
            ["Mixture", "Ingredients can be separated, like a salad"],
            ["Solution", "Fully dissolved, like salt water"],
        ]),
    },
    "science-g5-l21": {
        "data_table": table(["Change Type", "Example"], [
            ["Physical change", "Ice melting into water"], ["Chemical change", "Wood burning into ash"],
        ]),
    },
    "science-g5-l22": {
        "data_table": table(["Energy Transfer", "Example"], [
            ["Kinetic to sound", "Clapping hands"], ["Chemical to heat", "Burning wood"],
        ]),
    },
    "science-g5-l23": {
        "data_table": table(["Circuit Type", "Description"], [
            ["Closed circuit", "A complete loop; current flows"], ["Open circuit", "A broken loop; current stops"],
        ]),
    },
    "science-g5-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Static electricity", "Buildup of electric charge on a surface"],
        ]),
    },
    "science-g5-l25": {
        "data_table": table(["Heat Transfer Type", "Example"], [
            ["Conduction", "Touching a hot pan"], ["Convection", "Warm air rising"], ["Radiation", "Sunlight warming skin"],
        ]),
    },
    "science-g5-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Pitch", "How high or low a sound is, based on frequency"],
        ]),
    },
    "science-g5-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Reflection", "Light bouncing off a surface"], ["Refraction", "Light bending as it passes through a medium"],
        ]),
    },
    "science-g5-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Gravity", "Force that pulls objects toward Earth's center"],
        ]),
    },
    "science-g5-l29": {
        "data_table": table(["Resource Type", "Example"], [
            ["Renewable", "Solar, wind, water"], ["Nonrenewable", "Coal, oil, natural gas"],
        ]),
    },
    "science-g5-l30": {
        "data_table": table(["Step", "Purpose"], [
            ["Define the problem", "Identifies what needs solving"], ["Test and improve", "Refines the design"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 Science lessons (completing 30/30).")


if __name__ == "__main__":
    main()
