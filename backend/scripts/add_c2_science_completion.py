#!/usr/bin/env python3
"""Depth pass, C2 Science: fill in real, hand-checked data_table content
for the 69 C2 Science lessons not covered by the earlier breadth-first
batch. Brings C2 Science to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "science-c2-l1": {
        "data_table": table(["Field", "Focus"], [
            ["Geology", "Structure and processes of the solid Earth"], ["Astronomy", "Celestial objects and the universe"],
        ]),
    },
    "science-c2-l2": {
        "data_table": table(["Field", "Focus"], [
            ["Botany", "The study of plant life"], ["Zoology", "The study of animal life"],
        ]),
    },
    "science-c2-l4": {
        "data_table": table(["Concept", "Meaning"], [
            ["Correlation", "Two variables change together"], ["Causation", "One variable directly produces a change in another"],
        ]),
    },
    "science-c2-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Paradigm shift", "A fundamental change in the basic assumptions of a scientific field"],
        ]),
    },
    "science-c2-l6": {
        "data_table": table(["Field", "Focus"], [
            ["Biochemistry", "Studies the chemical processes within living organisms"],
        ]),
    },
    "science-c2-l7": {
        "data_table": table(["Practice", "Reason"], [
            ["Avoiding jargon", "Makes scientific findings accessible to a general audience"],
        ]),
    },
    "science-c2-l8": {
        "data_table": table(["Element", "Purpose"], [
            ["Control group", "Provides a baseline for comparison against the treatment group"],
        ]),
    },
    "science-c2-l9": {
        "data_table": table(["Statistic", "Meaning"], [
            ["Mean", "The arithmetic average of a data set"], ["Median", "The middle value when data is ordered"],
        ]),
    },
    "science-c2-l10": {
        "data_table": table(["Practice", "Reason"], [
            ["Reading safety data sheets", "Ensures proper handling of hazardous chemicals"],
        ]),
    },
    "science-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Replication crisis", "Difficulty reproducing many published scientific findings"],
        ]),
    },
    "science-c2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Conflict of interest", "A situation where personal or financial interests could bias research"],
        ]),
    },
    "science-c2-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Science policy", "Government decisions shaping research funding and regulation"],
        ]),
    },
    "science-c2-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Citizen science", "Public participation in collecting or analyzing scientific data"],
        ]),
    },
    "science-c2-l15": {
        "data_table": table(["Case", "Insight"], [
            ["Manhattan Project", "Illustrates science's entanglement with major societal consequences"],
        ]),
    },
    "science-c2-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Biotechnology", "Using biological systems to develop products and technologies"],
        ]),
    },
    "science-c2-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Carrying capacity", "The maximum population an ecosystem's resources can support"],
        ]),
    },
    "science-c2-l18": {
        "data_table": table(["Gas", "Warming Contribution"], [
            ["Carbon dioxide", "Largest contributor by volume of human emissions"], ["Methane", "More potent per molecule but shorter atmospheric lifetime"],
        ]),
    },
    "science-c2-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Epidemiology", "The study of disease patterns and causes in populations"],
        ]),
    },
    "science-c2-l20": {
        "data_table": table(["Stage", "Feature"], [
            ["REM sleep", "Associated with dreaming and memory consolidation"],
        ]),
    },
    "science-c2-l21": {
        "data_table": table(["Law", "Statement"], [
            ["First law of thermodynamics", "Energy cannot be created or destroyed, only transformed"], ["Second law", "Entropy of an isolated system tends to increase"],
        ]),
    },
    "science-c2-l22": {
        "data_table": table(["Concept", "Meaning"], [
            ["Quantization", "Energy exists in discrete units rather than a continuum"],
        ]),
    },
    "science-c2-l23": {
        "data_table": table(["Concept", "Meaning"], [
            ["Wave-particle duality", "Light and matter exhibit both wave-like and particle-like behavior"],
        ]),
    },
    "science-c2-l24": {
        "data_table": table(["Process", "Feature"], [
            ["Radioactive decay", "The spontaneous transformation of an unstable nucleus, releasing radiation"],
        ]),
    },
    "science-c2-l25": {
        "data_table": table(["Step", "Purpose"], [
            ["Using mole ratios", "Converts moles of one reactant to moles of a product"],
        ]),
    },
    "science-c2-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Chemical equilibrium", "A state where forward and reverse reaction rates are equal"],
        ]),
    },
    "science-c2-l27": {
        "data_table": table(["Factor", "Effect"], [
            ["Temperature", "Higher temperature generally increases reaction rate"],
        ]),
    },
    "science-c2-l28": {
        "data_table": table(["Group", "Example"], [
            ["Hydroxyl", "Found in alcohols"], ["Carboxyl", "Found in carboxylic acids"],
        ]),
    },
    "science-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Molecular biology", "Studies biological activity at the molecular level, especially DNA and RNA"],
        ]),
    },
    "science-c2-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Gene expression", "The process by which genetic information produces a functional product"],
        ]),
    },
    "science-c2-l31": {
        "data_table": table(["Technique", "Use"], [
            ["CRISPR", "Precisely edits specific DNA sequences"],
        ]),
    },
    "science-c2-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Population genetics", "Studies the distribution and change of allele frequencies in populations"],
        ]),
    },
    "science-c2-l33": {
        "data_table": table(["Mechanism", "Meaning"], [
            ["Genetic drift", "Random changes in allele frequency, especially in small populations"],
        ]),
    },
    "science-c2-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Population dynamics", "How population size and structure change over time"],
        ]),
    },
    "science-c2-l35": {
        "data_table": table(["Cycle", "Key Process"], [
            ["Carbon cycle", "Carbon moves between atmosphere, biosphere, and oceans"],
        ]),
    },
    "science-c2-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Comparative anatomy", "Compares body structures across species to understand evolutionary relationships"],
        ]),
    },
    "science-c2-l37": {
        "data_table": table(["System Part", "Function"], [
            ["Central nervous system", "Processes information (brain and spinal cord)"], ["Peripheral nervous system", "Connects the CNS to the rest of the body"],
        ]),
    },
    "science-c2-l38": {
        "data_table": table(["Gland", "Hormone"], [
            ["Thyroid", "Regulates metabolism"], ["Pancreas", "Regulates blood sugar via insulin"],
        ]),
    },
    "science-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Mantle convection", "Slow circular movement of mantle material driving plate motion"],
        ]),
    },
    "science-c2-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Crystal structure", "The ordered arrangement of atoms within a mineral"],
        ]),
    },
    "science-c2-l41": {
        "data_table": table(["Storm Type", "Feature"], [
            ["Hurricane", "A large rotating storm fueled by warm ocean water"], ["Tornado", "A violently rotating column of air, small but intense"],
        ]),
    },
    "science-c2-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Climate model", "A computational simulation predicting future climate conditions"],
        ]),
    },
    "science-c2-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Habitable zone", "The orbital range where liquid water could exist on a planet's surface"],
        ]),
    },
    "science-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Stellar nucleosynthesis", "The creation of new elements through nuclear fusion inside stars"],
        ]),
    },
    "science-c2-l45": {
        "data_table": table(["Concept", "Meaning"], [
            ["General relativity", "Describes gravity as the curvature of spacetime caused by mass"],
        ]),
    },
    "science-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Astrobiology", "The study of the potential for life beyond Earth"],
        ]),
    },
    "science-c2-l47": {
        "data_table": table(["Concept", "Use"], [
            ["p-value", "Assesses statistical significance of a research result"],
        ]),
    },
    "science-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Confound", "An unaccounted variable that could explain an observed effect"],
        ]),
    },
    "science-c2-l49": {
        "data_table": table(["Step", "Purpose"], [
            ["Peer review", "Independent experts evaluate research quality before publication"],
        ]),
    },
    "science-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Scientific model", "A simplified representation used to explain or predict a phenomenon"],
        ]),
    },
    "science-c2-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental toxicology", "Studies the effects of pollutants on living organisms"],
        ]),
    },
    "science-c2-l52": {
        "data_table": table(["Source", "Feature"], [
            ["Solar", "Converts sunlight directly into electricity"], ["Wind", "Converts kinetic energy of moving air into electricity"],
        ]),
    },
    "science-c2-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Epidemiology", "The study of disease distribution and determinants in populations"],
        ]),
    },
    "science-c2-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Herd immunity", "Population-level protection when enough people are immune to a disease"],
        ]),
    },
    "science-c2-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Bioinformatics", "Uses computational tools to analyze biological data, especially genomic sequences"],
        ]),
    },
    "science-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["CRISPR-Cas9", "A gene-editing tool that precisely cuts DNA at targeted locations"],
        ]),
    },
    "science-c2-l57": {
        "data_table": table(["Evidence", "Insight"], [
            ["Ice core data", "Shows historical correlation between CO2 levels and temperature"],
        ]),
    },
    "science-c2-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Systems biology", "Studies biological systems holistically through their component interactions"],
        ]),
    },
    "science-c2-l59": {
        "data_table": table(["Case", "Insight"], [
            ["Vaccine approval process", "Illustrates the interplay of science, regulation, and public trust"],
        ]),
    },
    "science-c2-l60": {
        "data_table": table(["Career", "Focus"], [
            ["Science communicator", "Translates complex research for public understanding"],
        ]),
    },
    "science-c2-l61": {
        "data_table": table(["Group", "Example"], [
            ["Amine", "Found in amino acids"], ["Ketone", "Found in fructose"],
        ]),
    },
    "science-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Comparing Earth systems", "Contrasting plate tectonics with atmospheric circulation"],
        ]),
    },
    "science-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Classifying an organism", "Placing a species within taxonomic ranks"],
        ]),
    },
    "science-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Designing a testable hypothesis", "Writing a falsifiable prediction for an experiment"],
        ]),
    },
    "science-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Identifying a confound", "Spotting a third variable explaining a spurious correlation"],
        ]),
    },
    "science-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Applying paradigm shift", "Comparing pre- and post-Copernican views of the solar system"],
        ]),
    },
    "science-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Connecting disciplines", "Explaining a metabolic pathway using chemical reactions"],
        ]),
    },
    "science-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Simplifying findings", "Rewriting a technical abstract for a general audience"],
        ]),
    },
    "science-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Designing an experiment", "Identifying independent, dependent, and control variables"],
        ]),
    },
    "science-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting variability", "Comparing standard deviation across two data sets"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Science lessons (completing 70/70).")


if __name__ == "__main__":
    main()
