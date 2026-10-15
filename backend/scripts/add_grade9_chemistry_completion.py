#!/usr/bin/env python3
"""Depth pass, Grade 9 Chemistry: fill in real, hand-checked data_table
content for the 48 Grade 9 Chemistry lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Chemistry to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_chemistry_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "chem-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Acid", "A substance with pH below 7"], ["Base", "A substance with pH above 7"], ["Salt", "Product of an acid-base reaction"],
        ]),
    },
    "chem-g9-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Mole", "The SI unit for amount of substance, 6.022 x 10^23 particles"],
        ]),
    },
    "chem-g9-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Organic chemistry", "The study of carbon-containing compounds"],
        ]),
    },
    "chemistry-g9-l4": {
        "data_table": table(["Particle", "Charge"], [
            ["Proton", "Positive"], ["Neutron", "Neutral"], ["Electron", "Negative"],
        ]),
    },
    "chemistry-g9-l6": {
        "data_table": table(["Trend", "Direction"], [
            ["Atomic radius", "Decreases across a period, increases down a group"],
        ]),
    },
    "chemistry-g9-l7": {
        "data_table": table(["Bond Type", "Description"], [
            ["Ionic", "Transfer of electrons between atoms"], ["Covalent", "Sharing of electrons between atoms"],
        ]),
    },
    "chemistry-g9-l9": {
        "data_table": table(["Bond Type", "Example"], [
            ["Covalent bond", "Shared electron pair, e.g. water (H2O)"],
        ]),
    },
    "chemistry-g9-l10": {
        "data_table": table(["Bond Type", "Description"], [
            ["Metallic bonding", "Positive metal ions surrounded by a 'sea' of delocalized electrons"],
        ]),
    },
    "chemistry-g9-l11": {
        "data_table": table(["Compound", "Formula"], [
            ["Water", "H2O"], ["Carbon dioxide", "CO2"], ["Sodium chloride", "NaCl"],
        ]),
    },
    "chemistry-g9-l12": {
        "data_table": table(["Rule", "Reason"], [
            ["Conservation of mass", "Atoms are neither created nor destroyed in a reaction"],
        ]),
        "formulae": ["2H2 + O2 -> 2H2O"],
    },
    "chemistry-g9-l13": {
        "data_table": table(["Reaction Type", "Example"], [
            ["Synthesis", "A + B -> AB"], ["Decomposition", "AB -> A + B"],
        ]),
    },
    "chemistry-g9-l14": {
        "data_table": table(["Change Type", "Example"], [
            ["Physical change", "Melting ice, no new substance formed"], ["Chemical change", "Burning wood, new substance formed"],
        ]),
    },
    "chemistry-g9-l15": {
        "data_table": table(["State", "Particle Arrangement"], [
            ["Solid", "Tightly packed, fixed positions"], ["Gas", "Widely spaced, moving freely"],
        ]),
    },
    "chemistry-g9-l16": {
        "data_table": table(["Type", "Example"], [
            ["Element", "Oxygen (O)"], ["Compound", "Water (H2O)"], ["Mixture", "Air"],
        ]),
    },
    "chemistry-g9-l17": {
        "data_table": table(["Technique", "Separates"], [
            ["Filtration", "Insoluble solids from liquids"], ["Evaporation", "Dissolved solids from solutions"],
        ]),
    },
    "chemistry-g9-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Filtration", "Separates insoluble solid particles from a liquid using a filter"],
        ]),
    },
    "chemistry-g9-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Distillation", "Separates liquids based on differing boiling points"],
        ]),
    },
    "chemistry-g9-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Chromatography", "Separates mixtures based on how components move through a medium"],
        ]),
    },
    "chemistry-g9-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Solubility", "The maximum amount of a solute that dissolves in a solvent at a given temperature"],
        ]),
    },
    "chemistry-g9-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Concentration", "Amount of solute dissolved in a given volume of solution"],
        ]),
    },
    "chemistry-g9-l23": {
        "data_table": table(["pH Range", "Meaning"], [
            ["0-6", "Acidic"], ["7", "Neutral"], ["8-14", "Basic"],
        ]),
    },
    "chemistry-g9-l24": {
        "data_table": table(["Indicator", "Acid Color", "Base Color"], [
            ["Litmus paper", "Red", "Blue"],
        ]),
    },
    "chemistry-g9-l25": {
        "data_table": table(["Reaction", "Products"], [
            ["Acid + Base", "Salt + Water"],
        ]),
        "formulae": ["HCl + NaOH -> NaCl + H2O"],
    },
    "chemistry-g9-l26": {
        "data_table": table(["Process", "Description"], [
            ["Oxidation", "Loss of electrons"], ["Reduction", "Gain of electrons"],
        ]),
    },
    "chemistry-g9-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Electrolysis", "Using electric current to drive a non-spontaneous chemical reaction"],
        ]),
    },
    "chemistry-g9-l28": {
        "data_table": table(["Metal", "Reactivity"], [
            ["Potassium", "Very reactive"], ["Gold", "Very unreactive"],
        ]),
    },
    "chemistry-g9-l29": {
        "data_table": table(["Method", "Used For"], [
            ["Electrolysis", "Extracting very reactive metals"], ["Reduction with carbon", "Extracting moderately reactive metals like iron"],
        ]),
    },
    "chemistry-g9-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Rusting", "The oxidation of iron in the presence of water and oxygen"],
        ]),
    },
    "chemistry-g9-l31": {
        "data_table": table(["Process", "Role"], [
            ["Photosynthesis", "Removes CO2 from the atmosphere"], ["Respiration", "Releases CO2 into the atmosphere"],
        ]),
    },
    "chemistry-g9-l32": {
        "data_table": table(["Reaction", "Products"], [
            ["Combustion", "Fuel + Oxygen -> Carbon dioxide + Water + Energy"],
        ]),
    },
    "chemistry-g9-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Catalyst", "A substance that speeds up a reaction without being consumed"],
        ]),
    },
    "chemistry-g9-l34": {
        "data_table": table(["Factor", "Effect"], [
            ["Temperature", "Higher temperature increases reaction rate"], ["Concentration", "Higher concentration increases reaction rate"],
        ]),
    },
    "chemistry-g9-l35": {
        "data_table": table(["Type", "Energy Change"], [
            ["Exothermic", "Releases energy to surroundings"], ["Endothermic", "Absorbs energy from surroundings"],
        ]),
    },
    "chemistry-g9-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Activation energy", "Minimum energy needed to start a reaction"],
        ]),
    },
    "chemistry-g9-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Crystallization", "Forming solid crystals from a solution"],
        ]),
    },
    "chemistry-g9-l38": {
        "data_table": table(["Stage", "Process"], [
            ["Evaporation", "Water turns to vapor"], ["Precipitation", "Water falls as rain or snow"],
        ]),
    },
    "chemistry-g9-l39": {
        "data_table": table(["Water Type", "Cause"], [
            ["Hard water", "Contains dissolved calcium and magnesium ions"], ["Soft water", "Low mineral content"],
        ]),
    },
    "chemistry-g9-l40": {
        "data_table": table(["Theory", "Statement"], [
            ["Kinetic theory of gases", "Gas particles are in constant, random motion"],
        ]),
    },
    "chemistry-g9-l41": {
        "data_table": table(["Law", "Statement"], [
            ["Avogadro's law", "Equal volumes of gases at the same temperature and pressure contain equal numbers of particles"],
        ]),
    },
    "chemistry-g9-l42": {
        "data_table": table(["Safety Rule", "Reason"], [
            ["Wear goggles", "Protects eyes from splashes"],
        ]),
    },
    "chemistry-g9-l43": {
        "data_table": table(["Scientist", "Contribution"], [
            ["Dmitri Mendeleev", "Created an early version of the periodic table, 1869"],
        ]),
    },
    "chemistry-g9-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Isotope", "Atoms of the same element with different numbers of neutrons"],
        ]),
    },
    "chemistry-g9-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Radioactive decay", "The process by which an unstable nucleus loses energy by emitting radiation"],
        ]),
    },
    "chemistry-g9-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Polymer", "A large molecule made of repeating smaller units called monomers"],
        ]),
    },
    "chemistry-g9-l47": {
        "data_table": table(["Fuel", "Source"], [
            ["Natural gas", "Fossil fuel"], ["Coal", "Fossil fuel"],
        ]),
    },
    "chemistry-g9-l48": {
        "data_table": table(["Pollutant", "Source"], [
            ["Carbon monoxide", "Incomplete combustion of fuels"],
        ]),
    },
    "chemistry-g9-l49": {
        "data_table": table(["Cause", "Effect"], [
            ["Sulfur dioxide emissions", "Contributes to acid rain"],
        ]),
    },
    "chemistry-g9-l50": {
        "data_table": table(["Alloy", "Components"], [
            ["Steel", "Iron and carbon"], ["Bronze", "Copper and tin"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Chemistry"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Chemistry: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Chemistry lessons (completing 50/50).")


if __name__ == "__main__":
    main()
