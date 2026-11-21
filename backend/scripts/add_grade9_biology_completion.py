#!/usr/bin/env python3
"""Depth pass, Grade 9 Biology: fill in real, hand-checked data_table
content for the 48 Grade 9 Biology lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Biology to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_biology_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "bio-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Transpiration", "Loss of water vapor from plant leaves"], ["Xylem", "Transports water upward"],
        ]),
    },
    "bio-g9-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Gene", "A unit of heredity made of DNA"], ["Allele", "A version of a gene"],
        ]),
    },
    "bio-g9-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Homeostasis", "Maintaining a stable internal environment"],
        ]),
    },
    "biology-g9-l4": {
        "data_table": table(["Organelle", "Function"], [
            ["Nucleus", "Contains genetic material"], ["Mitochondria", "Produces energy (ATP)"],
        ]),
    },
    "biology-g9-l5": {
        "data_table": table(["Feature", "Plant Cell", "Animal Cell"], [
            ["Cell wall", "Present", "Absent"],
        ]),
    },
    "biology-g9-l6": {
        "data_table": table(["Organelle", "Function"], [
            ["Ribosome", "Makes proteins"], ["Chloroplast", "Site of photosynthesis"],
        ]),
    },
    "biology-g9-l7": {
        "data_table": table(["Level", "Example"], [
            ["Cell", "Smallest unit of life"], ["Tissue", "Group of similar cells"], ["Organ", "Group of tissues"],
        ]),
    },
    "biology-g9-l8": {
        "data_table": table(["Tissue Example", "Organ Example"], [
            ["Muscle tissue", "Heart"],
        ]),
    },
    "biology-g9-l10": {
        "data_table": table(["Component", "Function"], [
            ["Heart", "Pumps blood"], ["Blood vessels", "Carry blood around the body"],
        ]),
    },
    "biology-g9-l11": {
        "data_table": table(["Organ", "Function"], [
            ["Lungs", "Exchange oxygen and carbon dioxide"],
        ]),
    },
    "biology-g9-l12": {
        "data_table": table(["Organ", "Function"], [
            ["Kidneys", "Filter waste from blood"], ["Bladder", "Stores urine"],
        ]),
    },
    "biology-g9-l13": {
        "data_table": table(["Component", "Function"], [
            ["Brain", "Controls the body"], ["Neuron", "Transmits nerve signals"],
        ]),
    },
    "biology-g9-l14": {
        "data_table": table(["Gland", "Hormone"], [
            ["Pancreas", "Insulin"], ["Thyroid", "Thyroxine"],
        ]),
    },
    "biology-g9-l15": {
        "data_table": table(["Function", "Detail"], [
            ["Support", "Provides the body's frame"], ["Protection", "Shields organs like the brain and heart"],
        ]),
    },
    "biology-g9-l16": {
        "data_table": table(["Muscle Type", "Example"], [
            ["Skeletal muscle", "Bicep, voluntary"], ["Cardiac muscle", "Heart, involuntary"],
        ]),
    },
    "biology-g9-l17": {
        "data_table": table(["Component", "Function"], [
            ["White blood cells", "Fight infection"], ["Antibodies", "Target specific pathogens"],
        ]),
    },
    "biology-g9-l18": {
        "data_table": table(["Organ", "Function"], [
            ["Ovaries", "Produce eggs"], ["Testes", "Produce sperm"],
        ]),
    },
    "biology-g9-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "The period of physical changes that lead to sexual maturity"],
        ]),
    },
    "biology-g9-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Meiosis", "Cell division that produces gametes with half the chromosome number"],
        ]),
    },
    "biology-g9-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["DNA", "Deoxyribonucleic acid, carries genetic instructions"],
        ]),
    },
    "biology-g9-l23": {
        "data_table": table(["Process", "Description"], [
            ["Protein synthesis", "The process of building proteins from DNA instructions"],
        ]),
    },
    "biology-g9-l24": {
        "data_table": table(["Reactants", "Products"], [
            ["Carbon dioxide + Water + Light", "Glucose + Oxygen"],
        ]),
        "formulae": ["6CO2 + 6H2O + light -> C6H12O6 + 6O2"],
    },
    "biology-g9-l25": {
        "data_table": table(["Reactants", "Products"], [
            ["Glucose + Oxygen", "Carbon dioxide + Water + Energy"],
        ]),
        "formulae": ["C6H12O6 + 6O2 -> 6CO2 + 6H2O + energy"],
    },
    "biology-g9-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Enzyme", "A protein that speeds up biochemical reactions"],
        ]),
    },
    "biology-g9-l27": {
        "data_table": table(["Process", "Description"], [
            ["Diffusion", "Movement of particles from high to low concentration"], ["Osmosis", "Diffusion of water across a membrane"],
        ]),
    },
    "biology-g9-l28": {
        "data_table": table(["Structure", "Function"], [
            ["Roots", "Absorb water and nutrients"], ["Leaves", "Site of photosynthesis"],
        ]),
    },
    "biology-g9-l29": {
        "data_table": table(["Method", "Example"], [
            ["Pollination", "Transfer of pollen for fertilization"],
        ]),
    },
    "biology-g9-l30": {
        "data_table": table(["Level", "Example"], [
            ["Kingdom", "Animalia"], ["Species", "Homo sapiens"],
        ]),
    },
    "biology-g9-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of life in a given area"],
        ]),
    },
    "biology-g9-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Ecosystem", "A community of organisms interacting with their environment"],
        ]),
    },
    "biology-g9-l33": {
        "data_table": table(["Level", "Example"], [
            ["Producer", "Grass"], ["Primary consumer", "Rabbit"], ["Secondary consumer", "Fox"],
        ]),
    },
    "biology-g9-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Energy flow", "Roughly 10% of energy transfers to the next trophic level"],
        ]),
    },
    "biology-g9-l35": {
        "data_table": table(["Cycle", "Key Process"], [
            ["Carbon cycle", "Photosynthesis and respiration"], ["Nitrogen cycle", "Nitrogen fixation by bacteria"],
        ]),
    },
    "biology-g9-l36": {
        "data_table": table(["Factor", "Effect"], [
            ["Limited resources", "Restrains population growth"],
        ]),
    },
    "biology-g9-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Adaptation", "A trait that helps an organism survive in its environment"],
        ]),
    },
    "biology-g9-l38": {
        "data_table": table(["Concept", "Proposed By"], [
            ["Natural selection", "Charles Darwin"],
        ]),
    },
    "biology-g9-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Bacteria", "Single-celled prokaryotic organisms"],
        ]),
    },
    "biology-g9-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["Virus", "A non-cellular infectious agent that needs a host cell to reproduce"],
        ]),
    },
    "biology-g9-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Fungi", "Organisms that absorb nutrients from their environment, e.g. mushrooms, yeast"],
        ]),
    },
    "biology-g9-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Pathogen", "A microorganism that causes disease"],
        ]),
    },
    "biology-g9-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Microbiome", "The community of microorganisms living in and on the human body"],
        ]),
    },
    "biology-g9-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Vaccination", "Introduces a weakened or inactive pathogen to build immunity"],
        ]),
    },
    "biology-g9-l45": {
        "data_table": table(["Nutrient Group", "Example"], [
            ["Carbohydrates", "Bread, rice"], ["Proteins", "Meat, beans"],
        ]),
    },
    "biology-g9-l46": {
        "data_table": table(["Function", "Detail"], [
            ["Sweating", "Cools the body through evaporation"],
        ]),
    },
    "biology-g9-l47": {
        "data_table": table(["Sense", "Organ"], [
            ["Sight", "Eyes"], ["Hearing", "Ears"], ["Smell", "Nose"],
        ]),
    },
    "biology-g9-l48": {
        "data_table": table(["Lifestyle Disease", "Risk Factor"], [
            ["Type 2 diabetes", "Poor diet and inactivity"],
        ]),
    },
    "biology-g9-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Genetic engineering", "Directly manipulating an organism's DNA"],
        ]),
    },
    "biology-g9-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Conservation biology", "The study of protecting and preserving biodiversity"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Biology"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Biology: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Biology lessons (completing 50/50).")


if __name__ == "__main__":
    main()
