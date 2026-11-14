#!/usr/bin/env python3
"""Depth pass, Grade 8 Biology: fill in real, hand-checked data_table
content for the 38 Grade 8 Biology lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Biology to full 40/40 coverage.

Reproductive-system/puberty lessons stick to general, factual, textbook-
level anatomy and physiology -- age-appropriate, nothing fabricated.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_biology_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "bio-g8-l1": {
        "data_table": table(["Cell Structure", "Function"], [
            ["Nucleus", "Controls the cell, holds DNA"], ["Cell membrane", "Controls what enters and exits"],
        ]),
    },
    "bio-g8-l2": {
        "data_table": table(["Molecule", "Role"], [
            ["Protein", "Builds and repairs tissue"], ["Carbohydrate", "Provides energy"],
        ]),
    },
    "bio-g8-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Enzyme", "A protein that speeds up chemical reactions in the body"],
        ]),
    },
    "biology-g8-l4": {
        "data_table": table(["Level", "Example"], [
            ["Cell", "Basic unit of life"], ["Tissue", "Group of similar cells"], ["Organ", "Group of tissues"],
        ]),
    },
    "biology-g8-l5": {
        "data_table": table(["Cell Type", "Unique Structure"], [
            ["Plant cell", "Has a cell wall and chloroplasts"], ["Animal cell", "No cell wall or chloroplasts"],
        ]),
    },
    "biology-g8-l7": {
        "data_table": table(["Input", "Output"], [
            ["Sunlight, water, CO2", "Glucose (sugar) and oxygen"],
        ]),
    },
    "biology-g8-l8": {
        "data_table": table(["Process", "Equation"], [
            ["Cellular respiration", "Glucose + oxygen -> CO2 + water + energy"],
        ]),
    },
    "biology-g8-l9": {
        "data_table": table(["Process", "Meaning"], [
            ["Diffusion", "Movement of particles from high to low concentration"],
            ["Osmosis", "Diffusion of water across a membrane"],
        ]),
    },
    "biology-g8-l10": {
        "data_table": table(["Organ", "Function"], [
            ["Stomach", "Breaks down food with acid"], ["Small intestine", "Absorbs nutrients"],
        ]),
    },
    "biology-g8-l11": {
        "data_table": table(["Organ", "Function"], [
            ["Lungs", "Exchange oxygen and carbon dioxide"],
        ]),
    },
    "biology-g8-l12": {
        "data_table": table(["Component", "Function"], [
            ["Heart", "Pumps blood"], ["Blood vessels", "Carry blood throughout the body"],
        ]),
    },
    "biology-g8-l13": {
        "data_table": table(["Vessel Type", "Function"], [
            ["Arteries", "Carry blood away from the heart"], ["Veins", "Carry blood back to the heart"],
        ]),
    },
    "biology-g8-l14": {
        "data_table": table(["System", "Function"], [
            ["Skeletal", "Supports and protects the body"],
        ]),
    },
    "biology-g8-l15": {
        "data_table": table(["System", "Function"], [
            ["Muscular", "Enables movement"],
        ]),
    },
    "biology-g8-l16": {
        "data_table": table(["Part", "Function"], [
            ["Brain", "Controls the body"], ["Spinal cord", "Carries signals between brain and body"],
        ]),
    },
    "biology-g8-l17": {
        "data_table": table(["Sense", "Organ"], [
            ["Sight", "Eyes"], ["Hearing", "Ears"], ["Smell", "Nose"],
        ]),
    },
    "biology-g8-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Human reproductive system", "Produces reproductive cells and supports growth and development"],
        ]),
    },
    "biology-g8-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "A stage of physical growth and change"],
            ["Timing", "Varies from person to person"],
        ]),
    },
    "biology-g8-l20": {
        "data_table": table(["Gland", "Function"], [
            ["Thyroid", "Regulates metabolism"], ["Pituitary", "Controls growth and other hormones"],
        ]),
    },
    "biology-g8-l21": {
        "data_table": table(["Component", "Function"], [
            ["White blood cells", "Fight infection"], ["Antibodies", "Recognize and neutralize pathogens"],
        ]),
    },
    "biology-g8-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Gene", "A unit of heredity passed from parent to offspring"],
        ]),
    },
    "biology-g8-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["DNA", "The molecule that carries genetic information"],
        ]),
    },
    "biology-g8-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Chromosome", "A structure that carries genes"],
        ]),
    },
    "biology-g8-l25": {
        "data_table": table(["Trait Type", "Meaning"], [
            ["Dominant", "The trait that appears when at least one dominant allele is present"],
            ["Recessive", "The trait that appears only when both alleles are recessive"],
        ]),
    },
    "biology-g8-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Evolution", "The change in species over generations"],
        ]),
    },
    "biology-g8-l27": {
        "data_table": table(["Concept", "Example"], [
            ["Natural selection", "Favorable traits become more common over generations"],
        ]),
    },
    "biology-g8-l28": {
        "data_table": table(["Kingdom", "Example"], [
            ["Animalia", "Animals"], ["Plantae", "Plants"],
        ]),
    },
    "biology-g8-l29": {
        "data_table": table(["Habitat", "Example Species"], [
            ["Rainforest", "Toucan, jaguar"], ["Desert", "Camel, cactus"],
        ]),
    },
    "biology-g8-l30": {
        "data_table": table(["Term", "Example"], [
            ["Food chain", "Grass to rabbit to fox"],
        ]),
    },
    "biology-g8-l31": {
        "data_table": table(["Role", "Example"], [
            ["Producer", "Plants that make their own food"], ["Decomposer", "Fungi that break down dead matter"],
        ]),
    },
    "biology-g8-l32": {
        "data_table": table(["Biome", "Characteristic"], [
            ["Tundra", "Cold, treeless"], ["Rainforest", "Hot, humid"],
        ]),
    },
    "biology-g8-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Population", "All individuals of a species in an area"], ["Community", "All populations living together"],
        ]),
    },
    "biology-g8-l34": {
        "data_table": table(["Human Impact", "Example"], [
            ["Deforestation", "Removes habitats"], ["Pollution", "Harms water and air quality"],
        ]),
    },
    "biology-g8-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of living species in an area"],
        ]),
    },
    "biology-g8-l36": {
        "data_table": table(["Microorganism", "Example Effect"], [
            ["Bacteria", "Can cause illness or aid digestion"], ["Virus", "Causes illnesses like the common cold"],
        ]),
    },
    "biology-g8-l37": {
        "data_table": table(["Plant Part", "Function"], [
            ["Roots", "Absorb water and nutrients"], ["Leaves", "Make food via photosynthesis"],
        ]),
    },
    "biology-g8-l38": {
        "data_table": table(["Plant Part", "Function"], [
            ["Flower", "Reproductive structure"], ["Pollen", "Carries male genetic material"],
        ]),
    },
    "biology-g8-l39": {
        "data_table": table(["Group", "Example"], [
            ["Mammals", "Dogs, whales"], ["Reptiles", "Snakes, lizards"],
        ]),
    },
    "biology-g8-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Homeostasis", "The body's ability to maintain a stable internal environment"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Biology"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Biology: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Biology lessons (completing 40/40).")


if __name__ == "__main__":
    main()
