#!/usr/bin/env python3
"""Depth pass, Grade 10 Biology: fill in real, hand-checked data_table
content for the Grade 10 Biology lessons not covered by the earlier
breadth-first batch. Brings Grade 10 Biology to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_biology_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "bio-g10-l1": {
        "data_table": table(["Concept", "Proposed By"], [
            ["Natural selection", "Charles Darwin"],
        ]),
    },
    "bio-g10-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Human reproduction", "Involves the fusion of a sperm and egg cell to form a zygote"],
        ]),
    },
    "biology-g10-l3": {
        "data_table": table(["Organelle", "Function"], [
            ["Nucleus", "Contains genetic material"], ["Mitochondria", "Produces energy (ATP)"],
        ]),
    },
    "biology-g10-l4": {
        "data_table": table(["Feature", "Plant Cell", "Animal Cell"], [
            ["Cell wall", "Present", "Absent"],
        ]),
    },
    "biology-g10-l5": {
        "data_table": table(["Process", "Description"], [
            ["Diffusion", "Movement of particles from high to low concentration"], ["Osmosis", "Diffusion of water across a membrane"],
        ]),
    },
    "biology-g10-l6": {
        "data_table": table(["Phase", "Description"], [
            ["Mitosis", "Cell division producing two identical daughter cells"],
        ]),
    },
    "biology-g10-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Meiosis", "Cell division that produces gametes with half the chromosome number"],
        ]),
    },
    "biology-g10-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Gene", "A unit of heredity"], ["Allele", "A variant form of a gene"],
        ]),
    },
    "biology-g10-l11": {
        "data_table": table(["Disorder", "Cause"], [
            ["Down syndrome", "An extra copy of chromosome 21"],
        ]),
    },
    "biology-g10-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Genetic engineering", "Directly altering an organism's DNA"],
        ]),
    },
    "biology-g10-l13": {
        "data_table": table(["Step", "Description"], [
            ["Transcription", "DNA is copied into mRNA"], ["Translation", "mRNA is used to build a protein"],
        ]),
    },
    "biology-g10-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Enzyme", "A protein that speeds up biochemical reactions"],
        ]),
    },
    "biology-g10-l15": {
        "data_table": table(["Reactants", "Products"], [
            ["CO2 + H2O + light", "Glucose + O2"],
        ]),
        "formulae": ["6CO2 + 6H2O + light -> C6H12O6 + 6O2"],
    },
    "biology-g10-l16": {
        "data_table": table(["Reactants", "Products"], [
            ["Glucose + O2", "CO2 + H2O + energy"],
        ]),
        "formulae": ["C6H12O6 + 6O2 -> 6CO2 + 6H2O + energy"],
    },
    "biology-g10-l17": {
        "data_table": table(["Organ", "Function"], [
            ["Stomach", "Breaks down food with acid and enzymes"], ["Small intestine", "Absorbs nutrients"],
        ]),
    },
    "biology-g10-l18": {
        "data_table": table(["Component", "Function"], [
            ["Heart", "Pumps blood"], ["Arteries", "Carry blood away from the heart"],
        ]),
    },
    "biology-g10-l19": {
        "data_table": table(["Organ", "Function"], [
            ["Lungs", "Exchange oxygen and carbon dioxide"],
        ]),
    },
    "biology-g10-l20": {
        "data_table": table(["Component", "Function"], [
            ["Neuron", "Transmits electrical signals"], ["Brain", "Controls the body"],
        ]),
    },
    "biology-g10-l21": {
        "data_table": table(["Gland", "Hormone"], [
            ["Pancreas", "Insulin"], ["Thyroid", "Thyroxine"],
        ]),
    },
    "biology-g10-l22": {
        "data_table": table(["Organ", "Function"], [
            ["Kidneys", "Filter waste from blood"], ["Bladder", "Stores urine"],
        ]),
    },
    "biology-g10-l23": {
        "data_table": table(["Component", "Function"], [
            ["White blood cells", "Fight infection"], ["Antibodies", "Target specific pathogens"],
        ]),
    },
    "biology-g10-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Homeostasis", "Maintaining a stable internal environment"],
        ]),
    },
    "biology-g10-l25": {
        "data_table": table(["System", "Function"], [
            ["Skeletal system", "Provides support and protection"], ["Muscular system", "Enables movement"],
        ]),
    },
    "biology-g10-l26": {
        "data_table": table(["Structure", "Function"], [
            ["Roots", "Absorb water and nutrients"], ["Leaves", "Site of photosynthesis"],
        ]),
    },
    "biology-g10-l27": {
        "data_table": table(["Method", "Example"], [
            ["Pollination", "Transfer of pollen for fertilization"],
        ]),
    },
    "biology-g10-l28": {
        "data_table": table(["Tissue", "Function"], [
            ["Xylem", "Transports water upward"], ["Phloem", "Transports sugars"],
        ]),
    },
    "biology-g10-l29": {
        "data_table": table(["Level", "Example"], [
            ["Kingdom", "Animalia"], ["Species", "Homo sapiens"],
        ]),
    },
    "biology-g10-l30": {
        "data_table": table(["Microorganism", "Example Disease"], [
            ["Bacteria", "Tuberculosis"], ["Virus", "Influenza"],
        ]),
    },
    "biology-g10-l31": {
        "data_table": table(["Transmission Route", "Example"], [
            ["Airborne", "Influenza"], ["Waterborne", "Cholera"],
        ]),
    },
    "biology-g10-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Vaccination", "Introduces a weakened or inactive pathogen to build immunity"],
        ]),
    },
    "biology-g10-l33": {
        "data_table": table(["Level", "Example"], [
            ["Producer", "Grass"], ["Primary consumer", "Rabbit"],
        ]),
    },
    "biology-g10-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Food web", "A network of interconnected food chains"],
        ]),
    },
    "biology-g10-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of life in a given area"],
        ]),
    },
    "biology-g10-l36": {
        "data_table": table(["Impact", "Example"], [
            ["Deforestation", "Reduces habitat and biodiversity"],
        ]),
    },
    "biology-g10-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Conservation biology", "The study of protecting and preserving biodiversity"],
        ]),
    },
    "biology-g10-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Adaptation", "A trait that helps an organism survive in its environment"],
        ]),
    },
    "biology-g10-l39": {
        "data_table": table(["Factor", "Effect"], [
            ["Limited resources", "Restrains population growth"],
        ]),
    },
    "biology-g10-l40": {
        "data_table": table(["Cycle", "Key Process"], [
            ["Carbon cycle", "Photosynthesis and respiration"], ["Nitrogen cycle", "Nitrogen fixation by bacteria"],
        ]),
    },
    "biology-g10-l41": {
        "data_table": table(["Behavior Type", "Example"], [
            ["Instinct", "Innate, unlearned behavior"], ["Learned behavior", "Acquired through experience"],
        ]),
    },
    "biology-g10-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Comparative anatomy", "Studies structural similarities and differences across species"],
        ]),
    },
    "biology-g10-l43": {
        "data_table": table(["Scientist", "Contribution"], [
            ["Charles Darwin", "Proposed natural selection, 1859"],
        ]),
    },
    "biology-g10-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Selective breeding", "Choosing organisms with desired traits to reproduce"],
        ]),
    },
    "biology-g10-l45": {
        "data_table": table(["Application", "Example"], [
            ["Biotechnology", "Genetically modified crops"],
        ]),
    },
    "biology-g10-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Stem cell", "An undifferentiated cell that can develop into specialized cell types"],
        ]),
    },
    "biology-g10-l47": {
        "data_table": table(["Organ", "Function"], [
            ["Ovaries", "Produce eggs"], ["Testes", "Produce sperm"],
        ]),
    },
    "biology-g10-l48": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "The period of physical changes that lead to sexual maturity"],
        ]),
    },
    "biology-g10-l49": {
        "data_table": table(["Tool", "Use"], [
            ["Microscope", "Magnifies small specimens for observation"],
        ]),
    },
    "biology-g10-l50": {
        "data_table": table(["Career", "Focus"], [
            ["Marine biologist", "Studies ocean life"], ["Geneticist", "Studies genes and heredity"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Biology"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Biology: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Biology lessons (completing 50/50).")


if __name__ == "__main__":
    main()
