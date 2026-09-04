#!/usr/bin/env python3
"""Depth pass, Grade 10 Chemistry: fill in real, hand-checked
data_table content for the Grade 10 Chemistry lessons not covered by
the earlier breadth-first batch. Brings Grade 10 Chemistry to full
50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_chemistry_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "chem-g10-l1": {
        "data_table": table(["Process", "Description"], [
            ["Oxidation", "Loss of electrons"], ["Reduction", "Gain of electrons"],
        ]),
    },
    "chem-g10-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Chemical equilibrium", "Forward and reverse reaction rates are equal"],
        ]),
    },
    "chemistry-g10-l3": {
        "data_table": table(["Particle", "Charge"], [
            ["Proton", "Positive"], ["Neutron", "Neutral"], ["Electron", "Negative"],
        ]),
    },
    "chemistry-g10-l4": {
        "data_table": table(["Trend", "Direction"], [
            ["Atomic radius", "Decreases across a period, increases down a group"],
        ]),
    },
    "chemistry-g10-l5": {
        "data_table": table(["Bond Type", "Description"], [
            ["Ionic", "Transfer of electrons between atoms"],
        ]),
    },
    "chemistry-g10-l6": {
        "data_table": table(["Bond Type", "Example"], [
            ["Covalent", "Shared electron pair, e.g. water (H2O)"],
        ]),
    },
    "chemistry-g10-l7": {
        "data_table": table(["Bond Type", "Description"], [
            ["Metallic bonding", "Positive metal ions surrounded by a 'sea' of delocalized electrons"],
        ]),
    },
    "chemistry-g10-l8": {
        "data_table": table(["Compound", "Formula"], [
            ["Water", "H2O"], ["Sodium chloride", "NaCl"],
        ]),
    },
    "chemistry-g10-l9": {
        "data_table": table(["Rule", "Reason"], [
            ["Conservation of mass", "Atoms are neither created nor destroyed in a reaction"],
        ]),
        "formulae": ["2H2 + O2 -> 2H2O"],
    },
    "chemistry-g10-l10": {
        "data_table": table(["Reaction Type", "Example"], [
            ["Synthesis", "A + B -> AB"], ["Decomposition", "AB -> A + B"],
        ]),
    },
    "chemistry-g10-l12": {
        "data_table": table(["Reaction", "Products"], [
            ["Acid + Base", "Salt + Water"],
        ]),
        "formulae": ["HCl + NaOH -> NaCl + H2O"],
    },
    "chemistry-g10-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Salt", "An ionic compound formed from the reaction of an acid and a base"],
        ]),
    },
    "chemistry-g10-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Molar mass", "The mass of one mole of a substance, in grams"],
        ]),
    },
    "chemistry-g10-l16": {
        "data_table": table(["State", "Particle Arrangement"], [
            ["Solid", "Tightly packed, fixed positions"], ["Gas", "Widely spaced, moving freely"],
        ]),
    },
    "chemistry-g10-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Solubility", "The maximum amount of a solute that dissolves in a solvent at a given temperature"],
        ]),
    },
    "chemistry-g10-l18": {
        "data_table": table(["Technique", "Separates"], [
            ["Filtration", "Insoluble solids from liquids"], ["Distillation", "Liquids by boiling point"],
        ]),
    },
    "chemistry-g10-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Group", "A vertical column of the periodic table"], ["Period", "A horizontal row of the periodic table"],
        ]),
    },
    "chemistry-g10-l20": {
        "data_table": table(["Property", "Metals", "Non-metals"], [
            ["Conductivity", "Good conductors", "Poor conductors"],
        ]),
    },
    "chemistry-g10-l21": {
        "data_table": table(["Metal", "Reactivity"], [
            ["Potassium", "Very reactive"], ["Gold", "Very unreactive"],
        ]),
    },
    "chemistry-g10-l22": {
        "data_table": table(["Process", "Description"], [
            ["Oxidation", "Loss of electrons"], ["Reduction", "Gain of electrons"],
        ]),
    },
    "chemistry-g10-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Organic chemistry", "The study of carbon-containing compounds"],
        ]),
    },
    "chemistry-g10-l24": {
        "data_table": table(["Compound", "Type"], [
            ["Methane (CH4)", "Alkane hydrocarbon"], ["Ethene (C2H4)", "Alkene hydrocarbon"],
        ]),
    },
    "chemistry-g10-l25": {
        "data_table": table(["Functional Group", "Example"], [
            ["Hydroxyl (-OH)", "Alcohols"], ["Carboxyl (-COOH)", "Carboxylic acids"],
        ]),
    },
    "chemistry-g10-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Polymer", "A large molecule made of repeating smaller units called monomers"],
        ]),
    },
    "chemistry-g10-l27": {
        "data_table": table(["Reaction", "Products"], [
            ["Combustion", "Fuel + Oxygen -> Carbon dioxide + Water + Energy"],
        ]),
    },
    "chemistry-g10-l28": {
        "data_table": table(["Reaction Type", "Energy Change"], [
            ["Exothermic", "Releases energy to surroundings"],
        ]),
    },
    "chemistry-g10-l29": {
        "data_table": table(["Reaction Type", "Energy Change"], [
            ["Endothermic", "Absorbs energy from surroundings"],
        ]),
    },
    "chemistry-g10-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Catalyst", "A substance that speeds up a reaction without being consumed"],
        ]),
    },
    "chemistry-g10-l31": {
        "data_table": table(["Law", "Statement"], [
            ["Boyle's Law", "Pressure and volume are inversely related at constant temperature"],
        ]),
    },
    "chemistry-g10-l32": {
        "data_table": table(["Stage", "Process"], [
            ["Evaporation", "Water turns to vapor"], ["Precipitation", "Water falls as rain or snow"],
        ]),
    },
    "chemistry-g10-l33": {
        "data_table": table(["Method", "Description"], [
            ["Filtration and chlorination", "Common steps in water treatment"],
        ]),
    },
    "chemistry-g10-l34": {
        "data_table": table(["Gas", "Approx. % in Atmosphere"], [
            ["Nitrogen", "78%"], ["Oxygen", "21%"],
        ]),
    },
    "chemistry-g10-l35": {
        "data_table": table(["Pollutant", "Source"], [
            ["Carbon monoxide", "Incomplete combustion of fuels"],
        ]),
    },
    "chemistry-g10-l36": {
        "data_table": table(["Safety Rule", "Reason"], [
            ["Wear goggles", "Protects eyes from splashes"],
        ]),
    },
    "chemistry-g10-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Crystallization", "Forming solid crystals from a solution"],
        ]),
    },
    "chemistry-g10-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Isotope", "Atoms of the same element with different numbers of neutrons"],
        ]),
    },
    "chemistry-g10-l39": {
        "data_table": table(["Nutrient", "Role in Plants"], [
            ["Nitrogen", "Supports leaf and stem growth"],
        ]),
    },
    "chemistry-g10-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["Haber Process", "Industrial synthesis of ammonia from nitrogen and hydrogen"],
        ]),
        "formulae": ["N2 + 3H2 -> 2NH3"],
    },
    "chemistry-g10-l41": {
        "data_table": table(["Material", "Key Chemical"], [
            ["Glass", "Silicon dioxide (SiO2)"],
        ]),
    },
    "chemistry-g10-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Titration", "A technique to determine the concentration of a solution"],
        ]),
    },
    "chemistry-g10-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Chromatography", "Separates mixtures based on how components move through a medium"],
        ]),
    },
    "chemistry-g10-l44": {
        "data_table": table(["Step", "Purpose"], [
            ["Empirical formula calculation", "Determines a compound's simplest whole-number ratio of atoms"],
        ]),
    },
    "chemistry-g10-l45": {
        "data_table": table(["Scientist", "Contribution"], [
            ["Dmitri Mendeleev", "Created an early version of the periodic table, 1869"],
        ]),
    },
    "chemistry-g10-l46": {
        "data_table": table(["Alloy", "Components"], [
            ["Steel", "Iron and carbon"], ["Bronze", "Copper and tin"],
        ]),
    },
    "chemistry-g10-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Rusting", "The oxidation of iron in the presence of water and oxygen"],
        ]),
    },
    "chemistry-g10-l48": {
        "data_table": table(["Nutrient", "Role"], [
            ["Carbohydrates", "Main energy source in food"],
        ]),
    },
    "chemistry-g10-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Green chemistry", "Designing chemical processes that reduce environmental harm"],
        ]),
    },
    "chemistry-g10-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Biochemistry", "The study of chemical processes within living organisms"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Chemistry"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Chemistry: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Chemistry lessons (completing 50/50).")


if __name__ == "__main__":
    main()
