#!/usr/bin/env python3
"""Depth pass, Grade 8 Science: fill in real, hand-checked data_table
content for the 38 Grade 8 Science lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Science to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sci-g8-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Gene", "A unit of heredity passed from parent to offspring"], ["Trait", "A characteristic influenced by genes"],
        ]),
    },
    "science-g8-l3": {
        "data_table": table(["Cell Structure", "Function"], [
            ["Nucleus", "Controls the cell, holds DNA"], ["Mitochondria", "Produces energy for the cell"],
        ]),
    },
    "science-g8-l4": {
        "data_table": table(["Process", "Equation"], [
            ["Photosynthesis", "CO2 + water + light -> glucose + oxygen"], ["Respiration", "Glucose + oxygen -> CO2 + water + energy"],
        ]),
    },
    "science-g8-l5": {
        "data_table": table(["Organ", "Function"], [
            ["Stomach", "Breaks down food with acid"], ["Small intestine", "Absorbs nutrients"],
        ]),
    },
    "science-g8-l6": {
        "data_table": table(["Component", "Function"], [
            ["Heart", "Pumps blood"], ["Blood vessels", "Carry blood throughout the body"],
        ]),
    },
    "science-g8-l7": {
        "data_table": table(["Organ", "Function"], [
            ["Lungs", "Exchange oxygen and carbon dioxide"],
        ]),
    },
    "science-g8-l8": {
        "data_table": table(["Part", "Function"], [
            ["Brain", "Controls the body"], ["Spinal cord", "Carries signals between brain and body"],
        ]),
    },
    "science-g8-l9": {
        "data_table": table(["System", "Function"], [
            ["Skeletal", "Supports and protects the body"], ["Muscular", "Enables movement"],
        ]),
    },
    "science-g8-l10": {
        "data_table": table(["Plant Part", "Function"], [
            ["Flower", "Reproductive structure"], ["Pollen", "Carries male genetic material"],
        ]),
    },
    "science-g8-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "A stage of physical growth and change"],
        ]),
    },
    "science-g8-l12": {
        "data_table": table(["Term", "Example"], [
            ["Food chain", "Grass to rabbit to fox"], ["Food web", "Multiple connected food chains"],
        ]),
    },
    "science-g8-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of living species in an area"],
        ]),
    },
    "science-g8-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Atom", "The smallest unit of an element"], ["Compound", "Two or more elements chemically bonded"],
        ]),
    },
    "science-g8-l16": {
        "data_table": table(["Bond Type", "Description"], [
            ["Ionic bond", "Transfer of electrons between atoms"], ["Covalent bond", "Sharing of electrons between atoms"],
        ]),
    },
    "science-g8-l17": {
        "data_table": table(["Substance", "pH Range"], [
            ["Acid", "Below 7"], ["Base", "Above 7"], ["Neutral", "7"],
        ]),
    },
    "science-g8-l18": {
        "data_table": table(["Reaction Sign", "Example"], [
            ["Gas bubbles", "Baking soda and vinegar"], ["Color change", "Rusting iron"],
        ]),
    },
    "science-g8-l19": {
        "data_table": table(["Property", "Metals", "Non-Metals"], [
            ["Conductivity", "Good conductors", "Poor conductors"],
        ]),
    },
    "science-g8-l20": {
        "data_table": table(["Change Type", "Example"], [
            ["Physical change", "Ice melting into water"], ["Chemical change", "Wood burning into ash"],
        ]),
    },
    "science-g8-l21": {
        "data_table": table(["Energy Type", "Example"], [
            ["Kinetic energy", "A moving ball"], ["Potential energy", "A stretched rubber band"],
        ]),
    },
    "science-g8-l22": {
        "data_table": table(["Term", "Formula"], [
            ["Work", "Force x distance"], ["Power", "Work / time"],
        ]),
    },
    "science-g8-l23": {
        "data_table": table(["Force", "Effect"], [
            ["Gravity", "Pulls objects toward Earth"], ["Friction", "Slows down moving objects"],
        ]),
    },
    "science-g8-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Gravitation", "The force of attraction between masses"],
        ]),
    },
    "science-g8-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Sound", "Created by vibrations, travels as waves"],
        ]),
    },
    "science-g8-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Reflection", "Light bouncing off a surface"], ["Refraction", "Light bending as it passes through a medium"],
        ]),
    },
    "science-g8-l27": {
        "data_table": table(["Circuit Type", "Description"], [
            ["Closed circuit", "A complete loop; current flows"], ["Open circuit", "A broken loop; current stops"],
        ]),
    },
    "science-g8-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Electromagnet", "A magnet created by an electric current"],
        ]),
    },
    "science-g8-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Heat", "Energy transferred due to a temperature difference"], ["Temperature", "A measure of average kinetic energy"],
        ]),
    },
    "science-g8-l30": {
        "data_table": table(["State", "Example"], [
            ["Solid", "Ice"], ["Liquid", "Water"], ["Gas", "Steam"],
        ]),
    },
    "science-g8-l31": {
        "data_table": table(["Planet", "Position from Sun"], [
            ["Mercury", "1st"], ["Earth", "3rd"], ["Jupiter", "5th"],
        ]),
    },
    "science-g8-l32": {
        "data_table": table(["Layer", "Description"], [
            ["Crust", "Thin outer layer"], ["Mantle", "Thick, hot layer beneath the crust"],
        ]),
    },
    "science-g8-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather", "Day-to-day atmospheric conditions"], ["Climate", "Average weather over many years"],
        ]),
    },
    "science-g8-l34": {
        "data_table": table(["Stage", "Description"], [
            ["Evaporation", "Water turns into vapor"], ["Precipitation", "Water falls as rain or snow"],
        ]),
    },
    "science-g8-l35": {
        "data_table": table(["Resource Type", "Example"], [
            ["Renewable", "Solar, wind, water"], ["Nonrenewable", "Coal, oil, natural gas"],
        ]),
    },
    "science-g8-l36": {
        "data_table": table(["Pollutant", "Health Effect"], [
            ["Air pollution", "Can worsen asthma and respiratory issues"],
        ]),
    },
    "science-g8-l37": {
        "data_table": table(["Microorganism", "Example Effect"], [
            ["Bacteria", "Can cause illness or aid digestion"], ["Virus", "Causes illnesses like the common cold"],
        ]),
    },
    "science-g8-l38": {
        "data_table": table(["Food Group", "Example"], [
            ["Grains", "Bread, rice"], ["Protein", "Chicken, beans"],
        ]),
    },
    "science-g8-l39": {
        "data_table": table(["Safety Rule", "Why"], [
            ["Wear safety goggles", "Protects eyes from chemicals"],
        ]),
    },
    "science-g8-l40": {
        "data_table": table(["Simple Machine", "Example"], [
            ["Lever", "See-saw"], ["Pulley", "Flagpole"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Science lessons (completing 40/40).")


if __name__ == "__main__":
    main()
