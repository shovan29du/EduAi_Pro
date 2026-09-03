#!/usr/bin/env python3
"""Depth pass, C1 Biology: fill in real, hand-checked data_table content
for the 69 C1 Biology lessons not covered by the earlier breadth-first
batch. Brings C1 Biology to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_biology_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "biology-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Cell", "The basic structural and functional unit of all living organisms"],
        ]),
    },
    "biology-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Evolution", "The change in heritable traits of populations over generations"],
        ]),
    },
    "biology-c1-l4": {
        "data_table": table(["Type", "Feature"], [
            ["Prokaryotic cell", "No membrane-bound nucleus, e.g. bacteria"], ["Eukaryotic cell", "Contains a membrane-bound nucleus, e.g. animal and plant cells"],
        ]),
    },
    "biology-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Fluid mosaic model", "Describes the cell membrane as a flexible bilayer with embedded proteins"],
        ]),
    },
    "biology-c1-l6": {
        "data_table": table(["Organelle", "Function"], [
            ["Mitochondria", "Produces cellular energy via respiration"], ["Nucleus", "Houses and protects the cell's DNA"],
        ]),
    },
    "biology-c1-l7": {
        "data_table": table(["Process", "Direction"], [
            ["Diffusion", "Movement of particles from high to low concentration"], ["Osmosis", "Movement of water across a membrane toward higher solute concentration"],
        ]),
    },
    "biology-c1-l8": {
        "data_table": table(["Process", "Feature"], [
            ["Active transport", "Moves molecules against their concentration gradient, requiring energy"],
        ]),
    },
    "biology-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Enzyme", "A protein that catalyzes biochemical reactions without being consumed"],
        ]),
    },
    "biology-c1-l10": {
        "data_table": table(["Stage", "Location"], [
            ["Glycolysis", "Cytoplasm"], ["Krebs cycle", "Mitochondrial matrix"],
        ]),
    },
    "biology-c1-l11": {
        "data_table": table(["Reactant", "Product"], [
            ["Carbon dioxide and water", "Glucose and oxygen"],
        ]),
        "formulae": ["6*CO2 + 6*H2O + light -> C6H12O6 + 6*O2"],
    },
    "biology-c1-l12": {
        "data_table": table(["Phase", "Event"], [
            ["Prophase", "Chromosomes condense and become visible"], ["Anaphase", "Sister chromatids separate to opposite poles"],
        ]),
    },
    "biology-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Meiosis", "Cell division that produces four genetically distinct haploid gametes"],
        ]),
    },
    "biology-c1-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Dominant allele", "An allele whose trait is expressed even with one copy present"], ["Recessive allele", "An allele whose trait is only expressed with two copies present"],
        ]),
    },
    "biology-c1-l15": {
        "data_table": table(["Cross", "Ratio"], [
            ["Heterozygous x heterozygous", "3:1 dominant to recessive phenotype ratio"],
        ]),
    },
    "biology-c1-l16": {
        "data_table": table(["Base Pair", "Bond"], [
            ["Adenine-Thymine", "Two hydrogen bonds"], ["Guanine-Cytosine", "Three hydrogen bonds"],
        ]),
    },
    "biology-c1-l17": {
        "data_table": table(["Level", "Example"], [
            ["Kingdom", "Animalia"], ["Species", "Homo sapiens"],
        ]),
    },
    "biology-c1-l18": {
        "data_table": table(["Level", "Role"], [
            ["Producer", "Converts sunlight into chemical energy"], ["Decomposer", "Breaks down dead organic matter"],
        ]),
    },
    "biology-c1-l19": {
        "data_table": table(["System", "Function"], [
            ["Circulatory system", "Transports blood, nutrients, and gases"], ["Nervous system", "Coordinates responses via electrical signals"],
        ]),
    },
    "biology-c1-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Forming a hypothesis", "Proposes a testable explanation for an observation"],
        ]),
    },
    "biology-c1-l21": {
        "data_table": table(["Property", "Biological Significance"], [
            ["Polarity", "Allows water to dissolve many biological molecules"],
        ]),
    },
    "biology-c1-l22": {
        "data_table": table(["Type", "Example"], [
            ["Monosaccharide", "Glucose"], ["Polysaccharide", "Starch and glycogen"],
        ]),
    },
    "biology-c1-l23": {
        "data_table": table(["Type", "Feature"], [
            ["Saturated fat", "No double bonds, typically solid at room temperature"], ["Unsaturated fat", "Contains double bonds, typically liquid at room temperature"],
        ]),
    },
    "biology-c1-l24": {
        "data_table": table(["Structure Level", "Feature"], [
            ["Primary structure", "The linear sequence of amino acids"], ["Tertiary structure", "The overall 3D folded shape"],
        ]),
    },
    "biology-c1-l25": {
        "data_table": table(["Molecule", "Role"], [
            ["DNA", "Stores genetic information"], ["RNA", "Carries out protein synthesis instructions"],
        ]),
    },
    "biology-c1-l26": {
        "data_table": table(["Factor", "Effect on Enzyme Activity"], [
            ["Temperature", "Activity rises then falls sharply past the optimal point"], ["pH", "Enzymes function best within a specific pH range"],
        ]),
    },
    "biology-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Cell signaling", "The process cells use to communicate and coordinate behavior"],
        ]),
    },
    "biology-c1-l28": {
        "data_table": table(["Component", "Function"], [
            ["Microtubules", "Provide structural support and enable movement"],
        ]),
    },
    "biology-c1-l29": {
        "data_table": table(["Junction Type", "Function"], [
            ["Tight junction", "Prevents leakage between adjacent cells"], ["Gap junction", "Allows direct communication between cells"],
        ]),
    },
    "biology-c1-l30": {
        "data_table": table(["Cell Type", "Potential"], [
            ["Totipotent", "Can become any cell type, including extraembryonic tissue"], ["Pluripotent", "Can become nearly any cell type in the body"],
        ]),
    },
    "biology-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Virus", "A non-cellular infectious agent that replicates only inside a host cell"],
        ]),
    },
    "biology-c1-l32": {
        "data_table": table(["Feature", "Detail"], [
            ["Binary fission", "The primary method of bacterial reproduction"],
        ]),
    },
    "biology-c1-l33": {
        "data_table": table(["Response Type", "Feature"], [
            ["Innate immunity", "A fast, non-specific first line of defense"], ["Adaptive immunity", "A slower, highly specific response with memory"],
        ]),
    },
    "biology-c1-l34": {
        "data_table": table(["Technique", "Use"], [
            ["Gram staining", "Classifies bacteria by cell wall composition"],
        ]),
    },
    "biology-c1-l35": {
        "data_table": table(["Organ", "Function"], [
            ["Roots", "Absorb water and nutrients from soil"], ["Leaves", "Carry out photosynthesis"],
        ]),
    },
    "biology-c1-l36": {
        "data_table": table(["Generation", "Feature"], [
            ["Sporophyte", "The diploid, spore-producing generation"], ["Gametophyte", "The haploid, gamete-producing generation"],
        ]),
    },
    "biology-c1-l37": {
        "data_table": table(["Body Plan", "Example"], [
            ["Radial symmetry", "Jellyfish"], ["Bilateral symmetry", "Most animals, including humans"],
        ]),
    },
    "biology-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Homologous structure", "A similar structure across species due to shared ancestry"],
        ]),
    },
    "biology-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Developmental biology", "Studies how organisms grow and develop from a single cell"],
        ]),
    },
    "biology-c1-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Carrying capacity", "The maximum population size an environment can sustain"],
        ]),
    },
    "biology-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Community ecology", "Studies interactions among different species in a shared habitat"],
        ]),
    },
    "biology-c1-l42": {
        "data_table": table(["Biome", "Feature"], [
            ["Tropical rainforest", "High rainfall and biodiversity"], ["Tundra", "Cold, low precipitation, permafrost"],
        ]),
    },
    "biology-c1-l43": {
        "data_table": table(["Cycle", "Key Process"], [
            ["Carbon cycle", "Carbon moves between atmosphere, organisms, and oceans"], ["Nitrogen cycle", "Nitrogen fixation converts atmospheric nitrogen to usable forms"],
        ]),
    },
    "biology-c1-l44": {
        "data_table": table(["Strategy", "Goal"], [
            ["Habitat protection", "Preserves ecosystems supporting endangered species"],
        ]),
    },
    "biology-c1-l45": {
        "data_table": table(["Nutrient", "Function"], [
            ["Vitamin C", "Supports immune function and collagen synthesis"],
        ]),
    },
    "biology-c1-l46": {
        "data_table": table(["Function", "Detail"], [
            ["Skeletal system", "Provides structure, protection, and mineral storage"],
        ]),
    },
    "biology-c1-l47": {
        "data_table": table(["Muscle Type", "Feature"], [
            ["Skeletal muscle", "Voluntary, attached to bones"], ["Cardiac muscle", "Involuntary, found only in the heart"],
        ]),
    },
    "biology-c1-l48": {
        "data_table": table(["Organ", "Function"], [
            ["Kidneys", "Filter blood and produce urine"],
        ]),
    },
    "biology-c1-l49": {
        "data_table": table(["System", "Function"], [
            ["Reproductive system", "Produces gametes and supports reproduction"],
        ]),
    },
    "biology-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Homeostasis", "The maintenance of a stable internal environment despite external change"],
        ]),
    },
    "biology-c1-l51": {
        "data_table": table(["Application", "Example"], [
            ["Biotechnology", "Using biological systems to develop products, like insulin production"],
        ]),
    },
    "biology-c1-l52": {
        "data_table": table(["Technique", "Use"], [
            ["CRISPR", "Precisely edits specific DNA sequences"],
        ]),
    },
    "biology-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Bioinformatics", "Uses computational tools to analyze biological data, especially genomic data"],
        ]),
    },
    "biology-c1-l54": {
        "data_table": table(["Method", "Basis"], [
            ["Molecular classification", "Groups organisms by genetic similarity rather than appearance alone"],
        ]),
    },
    "biology-c1-l55": {
        "data_table": table(["Behavior Type", "Example"], [
            ["Innate behavior", "Instinctive, present without learning"], ["Learned behavior", "Acquired through experience"],
        ]),
    },
    "biology-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Adaptation", "A trait that improves an organism's fitness in its environment"],
        ]),
    },
    "biology-c1-l57": {
        "data_table": table(["Feature", "Detail"], [
            ["Fungi", "Absorb nutrients externally and have cell walls made of chitin"],
        ]),
    },
    "biology-c1-l58": {
        "data_table": table(["Group", "Example"], [
            ["Protozoa", "Single-celled, animal-like protists"], ["Algae", "Photosynthetic, plant-like protists"],
        ]),
    },
    "biology-c1-l59": {
        "data_table": table(["Microscope Type", "Use"], [
            ["Light microscope", "Views living cells at moderate magnification"], ["Electron microscope", "Views ultrastructure at very high magnification"],
        ]),
    },
    "biology-c1-l60": {
        "data_table": table(["Career", "Focus"], [
            ["Microbiologist", "Studies microorganisms like bacteria and viruses"], ["Ecologist", "Studies interactions between organisms and their environment"],
        ]),
    },
    "biology-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Diagramming the cell cycle", "Sequencing the phases of mitosis correctly"],
        ]),
    },
    "biology-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Comparing root types", "Contrasting taproot and fibrous root systems"],
        ]),
    },
    "biology-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Tracing a plant life cycle", "Following alternation of generations in a fern"],
        ]),
    },
    "biology-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Comparing cell components", "Identifying which organelles a given cell type contains"],
        ]),
    },
    "biology-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Predicting offspring traits", "Applying a Punnett square to a genetic cross"],
        ]),
    },
    "biology-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Explaining a historical discovery", "Describing how early microscopy revealed cells"],
        ]),
    },
    "biology-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Comparing cell types", "Identifying whether a sample is prokaryotic or eukaryotic"],
        ]),
    },
    "biology-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Explaining membrane behavior", "Describing how proteins move within the fluid mosaic"],
        ]),
    },
    "biology-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Mapping organelle function", "Matching an organelle to its role in the cell"],
        ]),
    },
    "biology-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Predicting osmosis direction", "Determining water movement between two solutions of different concentration"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Biology"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Biology: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Biology lessons (completing 70/70).")


if __name__ == "__main__":
    main()
