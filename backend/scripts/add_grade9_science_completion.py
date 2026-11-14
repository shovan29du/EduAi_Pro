#!/usr/bin/env python3
"""Depth pass, Grade 9 Science: fill in real, hand-checked data_table
content for the 48 Grade 9 Science lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Science to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sci-g9-l2": {
        "data_table": table(["Bond Type", "Description"], [
            ["Ionic bond", "Transfer of electrons between atoms"], ["Covalent bond", "Sharing of electrons"],
        ]),
    },
    "science-g9-l3": {
        "data_table": table(["Cell Structure", "Function"], [
            ["Nucleus", "Controls the cell, holds DNA"], ["Mitochondria", "Produces energy for the cell"],
        ]),
    },
    "science-g9-l4": {
        "data_table": table(["Process", "Result"], [
            ["Mitosis", "Two identical daughter cells"], ["Meiosis", "Four genetically varied sex cells"],
        ]),
    },
    "science-g9-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["DNA", "The molecule that carries genetic information"], ["Replication", "Copying DNA before cell division"],
        ]),
    },
    "science-g9-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Gene", "A unit of heredity passed from parent to offspring"], ["Trait", "A characteristic influenced by genes"],
        ]),
    },
    "science-g9-l8": {
        "data_table": table(["Step", "Location"], [
            ["Transcription", "Nucleus"], ["Translation", "Ribosome"],
        ]),
    },
    "science-g9-l9": {
        "data_table": table(["Component", "Function"], [
            ["Heart", "Pumps blood"], ["Blood vessels", "Carry blood throughout the body"],
        ]),
    },
    "science-g9-l10": {
        "data_table": table(["Organ", "Function"], [
            ["Lungs", "Exchange oxygen and carbon dioxide"],
        ]),
    },
    "science-g9-l11": {
        "data_table": table(["Organ", "Function"], [
            ["Stomach", "Breaks down food with acid"], ["Small intestine", "Absorbs nutrients"],
        ]),
    },
    "science-g9-l12": {
        "data_table": table(["Part", "Function"], [
            ["Brain", "Controls the body"], ["Neuron", "Transmits electrical signals"],
        ]),
    },
    "science-g9-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Homeostasis", "The body's ability to maintain a stable internal environment"],
        ]),
    },
    "science-g9-l14": {
        "data_table": table(["Input", "Output"], [
            ["Sunlight, water, CO2", "Glucose (sugar) and oxygen"],
        ]),
    },
    "science-g9-l15": {
        "data_table": table(["Process", "Equation"], [
            ["Cellular respiration", "Glucose + oxygen -> CO2 + water + energy"],
        ]),
    },
    "science-g9-l16": {
        "data_table": table(["Trophic Level", "Example"], [
            ["Producer", "Plants"], ["Primary consumer", "Herbivores"],
        ]),
    },
    "science-g9-l17": {
        "data_table": table(["Term", "Example"], [
            ["Food chain", "Grass to rabbit to fox"], ["Food web", "Multiple connected food chains"],
        ]),
    },
    "science-g9-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of living species in an area"],
        ]),
    },
    "science-g9-l19": {
        "data_table": table(["Kingdom", "Example"], [
            ["Animalia", "Animals"], ["Plantae", "Plants"],
        ]),
    },
    "science-g9-l20": {
        "data_table": table(["Microorganism", "Example Effect"], [
            ["Bacteria", "Can cause illness or aid digestion"], ["Virus", "Causes illnesses like the common cold"],
        ]),
    },
    "science-g9-l21": {
        "data_table": table(["Component", "Function"], [
            ["White blood cells", "Fight infection"], ["Antibodies", "Recognize and neutralize pathogens"],
        ]),
    },
    "science-g9-l22": {
        "data_table": table(["Particle", "Charge"], [
            ["Proton", "Positive"], ["Neutron", "Neutral"], ["Electron", "Negative"],
        ]),
    },
    "science-g9-l23": {
        "data_table": table(["State", "Example"], [
            ["Solid", "Ice"], ["Liquid", "Water"], ["Gas", "Steam"],
        ]),
    },
    "science-g9-l24": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of mass", "Mass is neither created nor destroyed in a chemical reaction"],
        ]),
    },
    "science-g9-l25": {
        "data_table": table(["Substance", "pH Range"], [
            ["Acid", "Below 7"], ["Base", "Above 7"],
        ]),
    },
    "science-g9-l26": {
        "data_table": table(["Term", "Example"], [
            ["Solution", "Fully dissolved, like salt water"], ["Solubility", "How much can dissolve in a solvent"],
        ]),
    },
    "science-g9-l27": {
        "data_table": table(["Factor", "Effect on Reaction Rate"], [
            ["Temperature", "Higher temperature usually speeds up reactions"],
        ]),
    },
    "science-g9-l28": {
        "data_table": table(["Reaction Type", "Energy"], [
            ["Exothermic", "Releases energy"], ["Endothermic", "Absorbs energy"],
        ]),
    },
    "science-g9-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Carbon", "Forms the basis of all known organic compounds"],
        ]),
    },
    "science-g9-l30": {
        "data_table": table(["Property", "Metals"], [
            ["Conductivity", "Good conductors of heat and electricity"],
        ]),
    },
    "science-g9-l31": {
        "data_table": table(["Law", "Statement"], [
            ["Newton's First Law", "An object stays at rest or in motion unless acted on by a force"],
            ["Newton's Second Law", "F = ma"],
        ]),
    },
    "science-g9-l32": {
        "data_table": table(["Graph", "Slope Represents"], [
            ["Distance-time graph", "Speed"], ["Speed-time graph", "Acceleration"],
        ]),
    },
    "science-g9-l33": {
        "data_table": table(["Term", "Formula"], [
            ["Work", "Force x distance"], ["Power", "Work / time"],
        ]),
    },
    "science-g9-l34": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of energy", "Energy cannot be created or destroyed, only transformed"],
        ]),
    },
    "science-g9-l35": {
        "data_table": table(["Wave Type", "Example"], [
            ["Transverse wave", "Light wave"], ["Longitudinal wave", "Sound wave"],
        ]),
    },
    "science-g9-l36": {
        "data_table": table(["Property", "Meaning"], [
            ["Pitch", "How high or low a sound is"], ["Volume", "How loud a sound is"],
        ]),
    },
    "science-g9-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Reflection", "Light bouncing off a surface"], ["Refraction", "Light bending through a medium"],
        ]),
    },
    "science-g9-l38": {
        "data_table": table(["Circuit Type", "Description"], [
            ["Closed circuit", "A complete loop; current flows"], ["Open circuit", "A broken loop; current stops"],
        ]),
    },
    "science-g9-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Electromagnet", "A magnet created by an electric current"],
        ]),
    },
    "science-g9-l40": {
        "data_table": table(["Term", "Formula"], [
            ["Density", "Mass / volume"],
        ]),
    },
    "science-g9-l41": {
        "data_table": table(["Layer", "Description"], [
            ["Crust", "Thin outer layer"], ["Mantle", "Thick, hot layer beneath the crust"],
        ]),
    },
    "science-g9-l42": {
        "data_table": table(["Event", "Cause"], [
            ["Earthquake", "Movement of tectonic plates"], ["Volcanic eruption", "Magma rising through the crust"],
        ]),
    },
    "science-g9-l43": {
        "data_table": table(["Rock Type", "Formation"], [
            ["Igneous", "Cooled lava or magma"], ["Sedimentary", "Compressed layers of sediment"],
        ]),
    },
    "science-g9-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather", "Day-to-day atmospheric conditions"], ["Climate", "Average weather over many years"],
        ]),
    },
    "science-g9-l45": {
        "data_table": table(["Effect of Climate Change", "Example"], [
            ["Rising sea levels", "Threatens coastal communities"],
        ]),
    },
    "science-g9-l46": {
        "data_table": table(["Stage", "Description"], [
            ["Evaporation", "Water turns into vapor"], ["Precipitation", "Water falls as rain or snow"],
        ]),
    },
    "science-g9-l47": {
        "data_table": table(["Planet", "Position from Sun"], [
            ["Mercury", "1st"], ["Earth", "3rd"], ["Jupiter", "5th"],
        ]),
    },
    "science-g9-l48": {
        "data_table": table(["Star Stage", "Description"], [
            ["Main sequence", "Fusing hydrogen into helium, like our Sun"], ["Red giant", "Expanded outer layers late in life"],
        ]),
    },
    "science-g9-l49": {
        "data_table": table(["Step", "Purpose"], [
            ["Hypothesis", "A testable prediction"], ["Controlled variable", "Kept constant to ensure a fair test"],
        ]),
    },
    "science-g9-l50": {
        "data_table": table(["Safety Rule", "Why"], [
            ["Wear safety goggles", "Protects eyes from chemicals"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Science lessons (completing 50/50).")


if __name__ == "__main__":
    main()
