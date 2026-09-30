#!/usr/bin/env python3
"""Depth pass, Grade 10 Science: fill in real, hand-checked data_table
content for the Grade 10 Science lessons not covered by the earlier
breadth-first batch. Brings Grade 10 Science to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sci-g10-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Ecosystem", "A community of organisms interacting with their environment"],
        ]),
    },
    "sci-g10-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Quantum theory", "Describes physics at the atomic and subatomic scale"], ["Relativity", "Einstein's theory relating space, time, and gravity"],
        ]),
    },
    "science-g10-l3": {
        "data_table": table(["Particle", "Charge"], [
            ["Proton", "Positive"], ["Electron", "Negative"], ["Neutron", "Neutral"],
        ]),
    },
    "science-g10-l4": {
        "data_table": table(["Bond Type", "Description"], [
            ["Ionic", "Transfer of electrons"], ["Covalent", "Sharing of electrons"],
        ]),
    },
    "science-g10-l5": {
        "data_table": table(["Rule", "Meaning"], [
            ["Conservation of mass", "Mass of reactants equals mass of products"],
        ]),
    },
    "science-g10-l6": {
        "data_table": table(["pH Range", "Nature"], [
            ["0-6", "Acidic"], ["7", "Neutral"], ["8-14", "Basic"],
        ]),
    },
    "science-g10-l7": {
        "data_table": table(["Factor", "Effect"], [
            ["Temperature", "Higher temperature increases reaction rate"],
        ]),
    },
    "science-g10-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Chemical equilibrium", "Forward and reverse reaction rates are equal"],
        ]),
    },
    "science-g10-l9": {
        "data_table": table(["Compound", "Type"], [
            ["Methane (CH4)", "Alkane hydrocarbon"], ["Ethene (C2H4)", "Alkene hydrocarbon"],
        ]),
    },
    "science-g10-l10": {
        "data_table": table(["Functional Group", "Example"], [
            ["Hydroxyl (-OH)", "Alcohols"], ["Carboxyl (-COOH)", "Carboxylic acids"],
        ]),
    },
    "science-g10-l11": {
        "data_table": table(["Process", "Description"], [
            ["Oxidation", "Loss of electrons"], ["Reduction", "Gain of electrons"],
        ]),
    },
    "science-g10-l12": {
        "data_table": table(["Reaction Type", "Energy Change"], [
            ["Exothermic", "Releases energy"], ["Endothermic", "Absorbs energy"],
        ]),
    },
    "science-g10-l13": {
        "data_table": table(["Change", "Example"], [
            ["Melting", "Solid to liquid"], ["Condensation", "Gas to liquid"],
        ]),
    },
    "science-g10-l15": {
        "data_table": table(["Concept", "Formula"], [
            ["Force", "F = ma"],
        ]),
        "formulae": ["F = ma"],
    },
    "science-g10-l17": {
        "data_table": table(["Quantity", "Formula"], [
            ["Work", "W = Fd"], ["Power", "P = W/t"],
        ]),
        "formulae": ["W = Fd"],
    },
    "science-g10-l18": {
        "data_table": table(["Quantity", "Formula"], [
            ["Momentum", "p = mv"],
        ]),
        "formulae": ["p = mv"],
    },
    "science-g10-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Centripetal force", "The inward force keeping an object in circular motion"],
        ]),
    },
    "science-g10-l20": {
        "data_table": table(["Property", "Meaning"], [
            ["Wavelength", "Distance between successive crests"], ["Amplitude", "Height of a wave"],
        ]),
    },
    "science-g10-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Sound", "A longitudinal wave requiring a medium"],
        ]),
    },
    "science-g10-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Refraction", "Bending of light between media of different densities"],
        ]),
    },
    "science-g10-l23": {
        "data_table": table(["Law", "Formula"], [
            ["Ohm's Law", "V = IR"],
        ]),
        "formulae": ["V = IR"],
    },
    "science-g10-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Electromagnetism", "The interaction between electric currents and magnetic fields"],
        ]),
    },
    "science-g10-l25": {
        "data_table": table(["Method", "Description"], [
            ["Conduction", "Heat transfer via direct contact"], ["Convection", "Heat transfer via fluid movement"],
        ]),
    },
    "science-g10-l26": {
        "data_table": table(["Type", "Description"], [
            ["Alpha decay", "Emits a helium nucleus"], ["Beta decay", "Emits an electron"],
        ]),
    },
    "science-g10-l27": {
        "data_table": table(["Organelle", "Function"], [
            ["Nucleus", "Contains genetic material"], ["Mitochondria", "Produces energy"],
        ]),
    },
    "science-g10-l28": {
        "data_table": table(["Process", "Result"], [
            ["Mitosis", "Two identical daughter cells"], ["Meiosis", "Four genetically varied gametes"],
        ]),
    },
    "science-g10-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["DNA structure", "A double helix discovered by Watson and Crick, 1953"],
        ]),
    },
    "science-g10-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Gene", "A unit of heredity"], ["Allele", "A variant form of a gene"],
        ]),
    },
    "science-g10-l31": {
        "data_table": table(["Step", "Description"], [
            ["Transcription", "DNA is copied into mRNA"], ["Translation", "mRNA is used to build a protein"],
        ]),
    },
    "science-g10-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Genetic engineering", "Directly altering an organism's DNA"],
        ]),
    },
    "science-g10-l33": {
        "data_table": table(["Concept", "Proposed By"], [
            ["Natural selection", "Charles Darwin"],
        ]),
    },
    "science-g10-l34": {
        "data_table": table(["Component", "Function"], [
            ["Neuron", "Transmits electrical signals"], ["Brain", "Controls the body"],
        ]),
    },
    "science-g10-l35": {
        "data_table": table(["Component", "Function"], [
            ["Heart", "Pumps blood"], ["Arteries", "Carry blood away from the heart"],
        ]),
    },
    "science-g10-l36": {
        "data_table": table(["Organ", "Function"], [
            ["Stomach", "Breaks down food with acid and enzymes"], ["Small intestine", "Absorbs nutrients"],
        ]),
    },
    "science-g10-l37": {
        "data_table": table(["Gland", "Hormone"], [
            ["Pancreas", "Insulin"], ["Thyroid", "Thyroxine"],
        ]),
    },
    "science-g10-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Homeostasis", "Maintaining a stable internal environment"],
        ]),
    },
    "science-g10-l39": {
        "data_table": table(["Reactants", "Products"], [
            ["CO2 + H2O + light", "Glucose + O2"],
        ]),
        "formulae": ["6CO2 + 6H2O + light -> C6H12O6 + 6O2"],
    },
    "science-g10-l40": {
        "data_table": table(["Reactants", "Products"], [
            ["Glucose + O2", "CO2 + H2O + energy"],
        ]),
        "formulae": ["C6H12O6 + 6O2 -> 6CO2 + 6H2O + energy"],
    },
    "science-g10-l41": {
        "data_table": table(["Microorganism", "Example Disease"], [
            ["Bacteria", "Tuberculosis"], ["Virus", "Influenza"],
        ]),
    },
    "science-g10-l42": {
        "data_table": table(["Component", "Function"], [
            ["White blood cells", "Fight infection"], ["Antibodies", "Target specific pathogens"],
        ]),
    },
    "science-g10-l43": {
        "data_table": table(["Structure", "Function"], [
            ["Roots", "Absorb water and nutrients"], ["Flowers", "Reproductive structures"],
        ]),
    },
    "science-g10-l44": {
        "data_table": table(["Level", "Example"], [
            ["Kingdom", "Animalia"], ["Species", "Homo sapiens"],
        ]),
    },
    "science-g10-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Plate tectonics", "The Earth's crust is divided into moving plates"],
        ]),
    },
    "science-g10-l46": {
        "data_table": table(["Rock Type", "Formation"], [
            ["Igneous", "Cooled magma or lava"], ["Sedimentary", "Compacted layers of sediment"],
        ]),
    },
    "science-g10-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather", "Short-term atmospheric conditions"], ["Climate", "Long-term average weather patterns"],
        ]),
    },
    "science-g10-l48": {
        "data_table": table(["Planet", "Order from Sun"], [
            ["Mercury", "1st"], ["Earth", "3rd"],
        ]),
    },
    "science-g10-l49": {
        "data_table": table(["Fact", "Detail"], [
            ["Galaxy", "A vast collection of stars, gas, and dust bound by gravity"],
        ]),
    },
    "science-g10-l50": {
        "data_table": table(["Step", "Purpose"], [
            ["Hypothesis", "A testable prediction"], ["Controlled variable", "Kept constant to isolate the effect being tested"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Science lessons (completing 50/50).")


if __name__ == "__main__":
    main()
