#!/usr/bin/env python3
"""Depth pass, Grade 7 Science: fill in real, hand-checked data_table
content for the 38 Grade 7 Science lessons not covered by the earlier
breadth-first batch. Brings Grade 7 Science to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sci-g7-l1": {
        "data_table": table(["Reaction Sign", "Example"], [
            ["Gas bubbles", "Baking soda and vinegar"], ["Color change", "Rusting iron"],
        ]),
    },
    "sci-g7-l2": {
        "data_table": table(["Wave Type", "Example"], [
            ["Sound wave", "Requires a medium to travel"], ["Light wave", "Can travel through a vacuum"],
        ]),
    },
    "science-g7-l3": {
        "data_table": table(["Step", "Purpose"], [
            ["Hypothesis", "A testable prediction"], ["Variable", "A factor that can be changed or measured"],
        ]),
    },
    "science-g7-l4": {
        "data_table": table(["Cell Structure", "Function"], [
            ["Nucleus", "Controls the cell, holds DNA"], ["Mitochondria", "Produces energy for the cell"],
        ]),
    },
    "science-g7-l5": {
        "data_table": table(["Kingdom", "Example"], [
            ["Animalia", "Animals"], ["Plantae", "Plants"], ["Fungi", "Mushrooms"],
        ]),
    },
    "science-g7-l6": {
        "data_table": table(["Term", "Example"], [
            ["Food chain", "Grass to rabbit to fox"], ["Food web", "Multiple connected food chains"],
        ]),
    },
    "science-g7-l7": {
        "data_table": table(["Input", "Output"], [
            ["Sunlight, water, CO2", "Glucose (sugar) and oxygen"],
        ]),
    },
    "science-g7-l8": {
        "data_table": table(["Organ", "Function"], [
            ["Stomach", "Breaks down food with acid"], ["Small intestine", "Absorbs nutrients"],
        ]),
    },
    "science-g7-l9": {
        "data_table": table(["Organ", "Function"], [
            ["Lungs", "Exchange oxygen and carbon dioxide"], ["Diaphragm", "Muscle that helps breathing"],
        ]),
    },
    "science-g7-l10": {
        "data_table": table(["Component", "Function"], [
            ["Heart", "Pumps blood"], ["Blood vessels", "Carry blood throughout the body"],
        ]),
    },
    "science-g7-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "A stage of physical growth and change"],
        ]),
    },
    "science-g7-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Gene", "A unit of heredity passed from parent to offspring"], ["Trait", "A characteristic influenced by genes"],
        ]),
    },
    "science-g7-l13": {
        "data_table": table(["Concept", "Example"], [
            ["Adaptation", "A giraffe's long neck reaches high leaves"],
            ["Natural selection", "Favorable traits become more common over generations"],
        ]),
    },
    "science-g7-l14": {
        "data_table": table(["State Change", "Example"], [
            ["Melting", "Ice to water"], ["Evaporation", "Water to vapor"],
        ]),
    },
    "science-g7-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Atom", "The smallest unit of an element"], ["Compound", "Two or more elements chemically bonded"],
        ]),
    },
    "science-g7-l17": {
        "data_table": table(["Technique", "Use"], [
            ["Filtration", "Separates solids from liquids"], ["Evaporation", "Separates dissolved solids from liquids"],
        ]),
    },
    "science-g7-l19": {
        "data_table": table(["Law", "Statement"], [
            ["Newton's First Law", "An object stays at rest or in motion unless acted on by a force"],
            ["Newton's Second Law", "Force equals mass times acceleration"],
        ]),
    },
    "science-g7-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Gravity", "Force that pulls objects toward Earth's center"], ["Weight", "The force of gravity on an object's mass"],
        ]),
    },
    "science-g7-l21": {
        "data_table": table(["Energy Type", "Example"], [
            ["Kinetic energy", "A moving ball"], ["Potential energy", "A stretched rubber band"],
        ]),
    },
    "science-g7-l22": {
        "data_table": table(["Circuit Type", "Description"], [
            ["Closed circuit", "A complete loop; current flows"], ["Open circuit", "A broken loop; current stops"],
        ]),
    },
    "science-g7-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Electromagnet", "A magnet created by an electric current"],
        ]),
    },
    "science-g7-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Density", "Mass per unit of volume"], ["Buoyancy", "The upward force exerted by a fluid on an object"],
        ]),
    },
    "science-g7-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Water pressure", "Increases with depth"],
        ]),
    },
    "science-g7-l26": {
        "data_table": table(["Simple Machine", "Example"], [
            ["Lever", "See-saw"], ["Pulley", "Flagpole"],
        ]),
    },
    "science-g7-l27": {
        "data_table": table(["Layer", "Description"], [
            ["Crust", "Thin outer layer"], ["Mantle", "Thick, hot layer beneath the crust"],
        ]),
    },
    "science-g7-l28": {
        "data_table": table(["Event", "Cause"], [
            ["Earthquake", "Movement of tectonic plates"],
        ]),
    },
    "science-g7-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Volcano", "Forms when magma rises through Earth's crust"],
        ]),
    },
    "science-g7-l30": {
        "data_table": table(["Rock Type", "Formation"], [
            ["Igneous", "Cooled lava or magma"], ["Sedimentary", "Compressed layers of sediment"],
        ]),
    },
    "science-g7-l31": {
        "data_table": table(["Test", "What It Reveals"], [
            ["Hardness (Mohs scale)", "How resistant to scratching"], ["Streak test", "The color of a mineral's powder"],
        ]),
    },
    "science-g7-l32": {
        "data_table": table(["Tool", "Purpose"], [
            ["Barometer", "Measures air pressure"], ["Thermometer", "Measures temperature"],
        ]),
    },
    "science-g7-l33": {
        "data_table": table(["Stage", "Description"], [
            ["Evaporation", "Water turns into vapor"], ["Precipitation", "Water falls as rain or snow"],
        ]),
    },
    "science-g7-l34": {
        "data_table": table(["Climate Zone", "Characteristic"], [
            ["Tropical", "Hot and humid year-round"], ["Polar", "Very cold year-round"],
        ]),
    },
    "science-g7-l35": {
        "data_table": table(["Planet", "Position from Sun"], [
            ["Mercury", "1st"], ["Earth", "3rd"], ["Jupiter", "5th"],
        ]),
    },
    "science-g7-l36": {
        "data_table": table(["Moon Phase", "Description"], [
            ["New Moon", "Not visible"], ["Full Moon", "Fully illuminated"],
        ]),
    },
    "science-g7-l37": {
        "data_table": table(["Resource Type", "Example"], [
            ["Renewable", "Solar, wind, water"], ["Nonrenewable", "Coal, oil, natural gas"],
        ]),
    },
    "science-g7-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of living species in an area"],
        ]),
    },
    "science-g7-l39": {
        "data_table": table(["Microscope Part", "Function"], [
            ["Objective lens", "Magnifies the specimen"], ["Stage", "Holds the slide"],
        ]),
    },
    "science-g7-l40": {
        "data_table": table(["System", "Function"], [
            ["Skeletal", "Supports and protects the body"], ["Muscular", "Enables movement"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Science lessons (completing 40/40).")


if __name__ == "__main__":
    main()
