#!/usr/bin/env python3
"""Depth pass, Grade 8 Chemistry: fill in real, hand-checked data_table
content for the 38 Grade 8 Chemistry lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Chemistry to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_chemistry_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "chem-g8-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Atom", "The smallest unit of an element"], ["Periodic table", "Organizes elements by atomic number"],
        ]),
    },
    "chem-g8-l2": {
        "data_table": table(["Bond Type", "Description"], [
            ["Ionic bond", "Transfer of electrons between atoms"], ["Covalent bond", "Sharing of electrons between atoms"],
        ]),
    },
    "chem-g8-l3": {
        "data_table": table(["Reaction Sign", "Example"], [
            ["Gas bubbles", "Baking soda and vinegar"], ["Color change", "Rusting iron"],
        ]),
    },
    "chemistry-g8-l4": {
        "data_table": table(["State", "Example"], [
            ["Solid", "Ice"], ["Liquid", "Water"], ["Gas", "Steam"],
        ]),
    },
    "chemistry-g8-l5": {
        "data_table": table(["Change Type", "Example"], [
            ["Physical change", "Ice melting into water"], ["Chemical change", "Wood burning into ash"],
        ]),
    },
    "chemistry-g8-l6": {
        "data_table": table(["Term", "Example"], [
            ["Mixture", "Ingredients can be separated, like a salad"], ["Pure substance", "Fixed composition, like distilled water"],
        ]),
    },
    "chemistry-g8-l7": {
        "data_table": table(["Technique", "Use"], [
            ["Filtration", "Separates solids from liquids"], ["Evaporation", "Separates dissolved solids from liquids"],
        ]),
    },
    "chemistry-g8-l8": {
        "data_table": table(["Term", "Example"], [
            ["Solution", "Fully dissolved, like salt water"], ["Solubility", "How much can dissolve in a solvent"],
        ]),
    },
    "chemistry-g8-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Concentration", "The amount of solute dissolved in a given amount of solvent"],
        ]),
    },
    "chemistry-g8-l10": {
        "data_table": table(["Substance", "pH Range"], [
            ["Acid", "Below 7"], ["Base", "Above 7"],
        ]),
    },
    "chemistry-g8-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Neutralization", "An acid and base reacting to form water and a salt"],
        ]),
    },
    "chemistry-g8-l13": {
        "data_table": table(["Indicator", "Color Change"], [
            ["Litmus paper", "Red in acid, blue in base"],
        ]),
    },
    "chemistry-g8-l14": {
        "data_table": table(["Property", "Metals"], [
            ["Conductivity", "Good conductors of heat and electricity"],
        ]),
    },
    "chemistry-g8-l15": {
        "data_table": table(["Property", "Non-Metals"], [
            ["Conductivity", "Generally poor conductors"],
        ]),
    },
    "chemistry-g8-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Metalloid", "An element with properties between metals and non-metals"],
        ]),
    },
    "chemistry-g8-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Group", "A vertical column of the periodic table"], ["Period", "A horizontal row of the periodic table"],
        ]),
    },
    "chemistry-g8-l18": {
        "data_table": table(["Particle", "Charge"], [
            ["Proton", "Positive"], ["Neutron", "Neutral"], ["Electron", "Negative"],
        ]),
    },
    "chemistry-g8-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Isotope", "Atoms of the same element with different numbers of neutrons"],
        ]),
    },
    "chemistry-g8-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Ion", "An atom with an electric charge from gaining or losing electrons"],
        ]),
    },
    "chemistry-g8-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Covalent compound", "Formed by atoms sharing electrons"],
        ]),
    },
    "chemistry-g8-l22": {
        "data_table": table(["Compound", "Formula"], [
            ["Water", "H2O"], ["Carbon dioxide", "CO2"],
        ]),
    },
    "chemistry-g8-l23": {
        "data_table": table(["Equation", "Balanced Form"], [
            ["H2 + O2", "2H2 + O2 -> 2H2O"],
        ]),
    },
    "chemistry-g8-l24": {
        "data_table": table(["Reaction Type", "Example"], [
            ["Synthesis", "Two substances combine into one"], ["Decomposition", "One substance breaks into two or more"],
        ]),
    },
    "chemistry-g8-l25": {
        "data_table": table(["Reaction Type", "Energy"], [
            ["Exothermic", "Releases energy"], ["Endothermic", "Absorbs energy"],
        ]),
    },
    "chemistry-g8-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Catalyst", "A substance that speeds up a reaction without being used up"],
        ]),
    },
    "chemistry-g8-l27": {
        "data_table": table(["Factor", "Effect on Reaction Rate"], [
            ["Temperature", "Higher temperature usually speeds up reactions"],
        ]),
    },
    "chemistry-g8-l28": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of mass", "Mass is neither created nor destroyed in a chemical reaction"],
        ]),
    },
    "chemistry-g8-l29": {
        "data_table": table(["Term", "Example"], [
            ["Oxidation", "A substance loses electrons, like rusting"], ["Combustion", "Burning in the presence of oxygen"],
        ]),
    },
    "chemistry-g8-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Rusting", "The oxidation of iron in the presence of moisture and oxygen"],
        ]),
    },
    "chemistry-g8-l31": {
        "data_table": table(["Property", "Detail"], [
            ["Water molecule", "H2O, polar molecule"],
        ]),
    },
    "chemistry-g8-l32": {
        "data_table": table(["Fact", "Detail"], [
            ["Carbon", "Forms the basis of all known organic compounds"],
        ]),
    },
    "chemistry-g8-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Organic chemistry", "The study of carbon-containing compounds"],
        ]),
    },
    "chemistry-g8-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Polymer", "A large molecule made of repeating smaller units"],
        ]),
    },
    "chemistry-g8-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Crystal", "A solid with a regular, repeating atomic structure"],
        ]),
    },
    "chemistry-g8-l36": {
        "data_table": table(["Safety Rule", "Why"], [
            ["Wear safety goggles", "Protects eyes from chemicals"],
        ]),
    },
    "chemistry-g8-l37": {
        "data_table": table(["Quantity", "Standard Unit"], [
            ["Mass", "Gram (g)"], ["Volume", "Liter (L)"],
        ]),
    },
    "chemistry-g8-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Mole", "A unit representing a fixed number of particles (6.022 x 10^23)"],
        ]),
    },
    "chemistry-g8-l39": {
        "data_table": table(["Material", "Bond Type"], [
            ["Table salt", "Ionic"], ["Water", "Covalent"],
        ]),
    },
    "chemistry-g8-l40": {
        "data_table": table(["Scientist", "Contribution"], [
            ["Dmitri Mendeleev", "Created an early version of the periodic table, 1869"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Chemistry"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Chemistry: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Chemistry lessons (completing 40/40).")


if __name__ == "__main__":
    main()
