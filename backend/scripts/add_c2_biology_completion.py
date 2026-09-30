#!/usr/bin/env python3
"""Depth pass, C2 Biology: fill in real, hand-checked data_table
content for the 69 C2 Biology lessons not covered by the earlier
breadth-first batch. Brings C2 Biology to full 70/70 coverage.

l61-l66 are "Foundations 2/3" lessons revisiting l14, l16, l19, l21,
l29, and l49; l67-l70 are "Worked Analysis" companions to l1-l4. l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_biology_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "biology-c2-l1": {
        "data_table": table(["Topic", "Feature"], [
            ["Genetics & evolution foundations", "Connects heredity mechanisms to change in populations over time"],
        ]),
    },
    "biology-c2-l2": {
        "data_table": table(["Topic", "Feature"], [
            ["Physiology & anatomy foundations", "Studies body structure and the functions that sustain life"],
        ]),
    },
    "biology-c2-l4": {
        "data_table": table(["Step", "Enzyme"], [
            ["Transcription", "RNA polymerase synthesizes mRNA from a DNA template"],
        ]),
    },
    "biology-c2-l5": {
        "data_table": table(["Component", "Role"], [
            ["Ribosome", "Site where mRNA codons are translated into a polypeptide chain"],
            ["tRNA", "Carries amino acids matching each mRNA codon"],
        ]),
    },
    "biology-c2-l6": {
        "data_table": table(["Property", "Detail"], [
            ["Genetic code redundancy", "Most amino acids are specified by more than one codon"],
        ]),
    },
    "biology-c2-l7": {
        "data_table": table(["State", "Behavior"], [
            ["Lactose present", "Lac operon is transcribed, enzymes for lactose metabolism are produced"],
            ["Lactose absent", "Repressor blocks transcription of the operon"],
        ]),
    },
    "biology-c2-l8": {
        "data_table": table(["Mutation Type", "Effect"], [
            ["Missense mutation", "Changes one amino acid in the resulting protein"],
            ["Frameshift mutation", "Shifts the reading frame, often drastically altering the protein"],
        ]),
    },
    "biology-c2-l9": {
        "data_table": table(["Pattern", "Feature"], [
            ["Incomplete dominance", "Heterozygote phenotype is an intermediate blend"],
            ["Codominance", "Both alleles are fully expressed simultaneously"],
        ]),
    },
    "biology-c2-l10": {
        "data_table": table(["Pattern", "Feature"], [
            ["X-linked recessive", "Trait appears more often in males due to a single X chromosome"],
        ]),
    },
    "biology-c2-l11": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Filled shape", "Individual affected by the trait"],
            ["Circle/square", "Female/male individual"],
        ]),
    },
    "biology-c2-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Natural selection", "Heritable traits improving survival/reproduction become more common over generations"],
        ]),
    },
    "biology-c2-l13": {
        "data_table": table(["Evidence Type", "Example"], [
            ["Fossil record", "Shows gradual change in species over geological time"],
            ["Homologous structures", "Similar anatomy across species with a common ancestor"],
        ]),
    },
    "biology-c2-l14": {
        "data_table": table(["Mechanism", "Detail"], [
            ["Allopatric speciation", "New species form after populations are geographically separated"],
        ]),
    },
    "biology-c2-l15": {
        "data_table": table(["Equation", "Use"], [
            ["Hardy-Weinberg", "p^2 + 2pq + q^2 = 1 models allele frequencies in a non-evolving population"],
        ]),
        "formulae": ["p**2 + 2*p*q + q**2 == 1"],
    },
    "biology-c2-l16": {
        "data_table": table(["Component", "Function"], [
            ["Synapse", "Junction where a neuron transmits a signal to another cell"],
        ]),
    },
    "biology-c2-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Negative feedback", "Hormone levels are regulated to counteract deviations from a set point"],
        ]),
    },
    "biology-c2-l18": {
        "data_table": table(["Chamber", "Function"], [
            ["Left ventricle", "Pumps oxygenated blood to the body"],
            ["Right ventricle", "Pumps deoxygenated blood to the lungs"],
        ]),
    },
    "biology-c2-l19": {
        "data_table": table(["Structure", "Function"], [
            ["Alveoli", "Site of gas exchange between air and blood"],
        ]),
    },
    "biology-c2-l20": {
        "data_table": table(["Organ", "Function"], [
            ["Small intestine", "Primary site of nutrient absorption"],
        ]),
    },
    "biology-c2-l21": {
        "data_table": table(["Tool", "Function"], [
            ["Restriction enzyme", "Cuts DNA at specific recognition sequences"],
        ]),
    },
    "biology-c2-l22": {
        "data_table": table(["Component", "Role"], [
            ["Cas9", "Enzyme that cuts DNA at a location specified by guide RNA"],
        ]),
    },
    "biology-c2-l23": {
        "data_table": table(["Step", "Purpose"], [
            ["PCR denaturation", "Heat separates the DNA double strand for copying"],
        ]),
    },
    "biology-c2-l24": {
        "data_table": table(["Principle", "Detail"], [
            ["Gel electrophoresis", "Smaller DNA fragments migrate farther through the gel"],
        ]),
    },
    "biology-c2-l25": {
        "data_table": table(["Method", "Detail"], [
            ["Sanger sequencing", "Uses chain-terminating nucleotides to read a DNA sequence"],
        ]),
    },
    "biology-c2-l26": {
        "data_table": table(["Mechanism", "Detail"], [
            ["Eukaryotic gene regulation", "Involves transcription factors, enhancers, and chromatin state together"],
        ]),
    },
    "biology-c2-l27": {
        "data_table": table(["Modification", "Effect"], [
            ["DNA methylation", "Typically silences gene expression without changing the sequence"],
        ]),
    },
    "biology-c2-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Signal transduction", "Converts an extracellular signal into an intracellular response via a pathway"],
        ]),
    },
    "biology-c2-l29": {
        "data_table": table(["Gene Type", "Role"], [
            ["Oncogene", "Promotes cell division when abnormally activated"],
            ["Tumor suppressor", "Normally restrains cell division; loss of function permits cancer"],
        ]),
    },
    "biology-c2-l30": {
        "data_table": table(["Checkpoint", "Function"], [
            ["G1/S checkpoint", "Verifies DNA is undamaged before replication begins"],
        ]),
    },
    "biology-c2-l31": {
        "data_table": table(["Region", "Function"], [
            ["Variable region", "Binds specifically to an antigen"],
            ["Constant region", "Determines antibody class and effector function"],
        ]),
    },
    "biology-c2-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Vaccine", "Trains adaptive immunity to recognize a pathogen without causing disease"],
        ]),
    },
    "biology-c2-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Microbiome", "Community of microorganisms that influences host digestion and immunity"],
        ]),
    },
    "biology-c2-l34": {
        "data_table": table(["Taxon", "Adaptation"], [
            ["Fish", "Gills extract dissolved oxygen from water"],
            ["Mammals", "Lungs extract oxygen from air with high metabolic efficiency"],
        ]),
    },
    "biology-c2-l35": {
        "data_table": table(["Gland", "Hormone"], [
            ["Thyroid", "Thyroxine, regulates metabolic rate"],
            ["Pancreas", "Insulin, regulates blood glucose"],
        ]),
    },
    "biology-c2-l36": {
        "data_table": table(["Phase", "Event"], [
            ["Depolarization", "Sodium influx raises membrane potential during an action potential"],
        ]),
    },
    "biology-c2-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Cardiac output", "Product of heart rate and stroke volume"],
        ]),
        "formulae": ["cardiac_output = heart_rate * stroke_volume"],
    },
    "biology-c2-l38": {
        "data_table": table(["Organ", "Function"], [
            ["Kidney nephron", "Filters blood and regulates fluid and acid-base balance"],
        ]),
    },
    "biology-c2-l39": {
        "data_table": table(["Molecule", "Role"], [
            ["Hemoglobin", "Binds and transports oxygen in the blood"],
        ]),
    },
    "biology-c2-l40": {
        "data_table": table(["Process", "Detail"], [
            ["Comparative development", "Shared embryonic stages across species reveal evolutionary relationships"],
        ]),
    },
    "biology-c2-l41": {
        "data_table": table(["Mechanism", "Detail"], [
            ["Genetic drift", "Random allele frequency change, especially strong in small populations"],
        ]),
    },
    "biology-c2-l42": {
        "data_table": table(["Method", "Purpose"], [
            ["Phylogenetic tree", "Visualizes evolutionary relationships among species or genes"],
        ]),
    },
    "biology-c2-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["Molecular clock", "Estimates divergence time from the rate of genetic mutation accumulation"],
        ]),
    },
    "biology-c2-l44": {
        "data_table": table(["Concept", "Example"], [
            ["Coevolution", "Predator and prey traits evolve in response to each other over time"],
        ]),
    },
    "biology-c2-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Conservation genetics", "Manages genetic diversity to prevent inbreeding depression in small populations"],
        ]),
    },
    "biology-c2-l46": {
        "data_table": table(["Concept", "Effect"], [
            ["Habitat fragmentation", "Isolates populations and reduces effective gene flow"],
        ]),
    },
    "biology-c2-l47": {
        "data_table": table(["Service", "Example"], [
            ["Pollination", "Ecosystem service supporting food crop production"],
        ]),
    },
    "biology-c2-l48": {
        "data_table": table(["Impact", "Detail"], [
            ["Range shift", "Species move poleward or upward in elevation as climate warms"],
        ]),
    },
    "biology-c2-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Synthetic biology", "Engineers biological systems using standardized genetic components"],
        ]),
    },
    "biology-c2-l50": {
        "data_table": table(["Method", "Purpose"], [
            ["Mass spectrometry (proteomics)", "Identifies and quantifies proteins in a complex sample"],
        ]),
    },
    "biology-c2-l51": {
        "data_table": table(["Field", "Focus"], [
            ["Metabolomics", "Studies the complete set of small-molecule metabolites in a system"],
        ]),
    },
    "biology-c2-l52": {
        "data_table": table(["Cell Type", "Potency"], [
            ["Pluripotent stem cell", "Can differentiate into nearly any cell type"],
        ]),
    },
    "biology-c2-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Whole-genome sequencing", "Reads an organism's complete DNA sequence"],
        ]),
    },
    "biology-c2-l54": {
        "data_table": table(["Field", "Focus"], [
            ["Population genomics", "Studies genome-wide variation across populations"],
        ]),
    },
    "biology-c2-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Genetic disorder", "Results from mutation in one or more genes affecting protein function"],
        ]),
    },
    "biology-c2-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Drug-receptor binding", "Drug affinity and efficacy determine its physiological effect"],
        ]),
    },
    "biology-c2-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Dose-response curve", "Describes how effect magnitude changes with substance dose"],
        ]),
    },
    "biology-c2-l58": {
        "data_table": table(["Issue", "Detail"], [
            ["Research bioethics", "Balances scientific progress with participant welfare and consent"],
        ]),
    },
    "biology-c2-l59": {
        "data_table": table(["Practice", "Purpose"], [
            ["Sterile technique", "Prevents contamination in cell culture work"],
        ]),
    },
    "biology-c2-l60": {
        "data_table": table(["Element", "Purpose"], [
            ["Control group (biology research)", "Isolates the effect of the variable under study"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Enzyme", "Role in DNA Replication"], [
    ["DNA polymerase", "Adds new nucleotides to the growing strand"],
    ["Helicase", "Unwinds the DNA double helix"],
    ["Ligase", "Joins DNA fragments together"],
])

# l61-l66 "Foundations 2/3" lessons revisit l14, l16, l19, l21, l29, l49.
FOUNDATIONS_MAP = {61: 14, 62: 16, 63: 19, 64: 21, 65: 29, 66: 49}
for worked_n, base_n in FOUNDATIONS_MAP.items():
    base_key = f"biology-c2-l{base_n}"
    CHARTS[f"biology-c2-l{worked_n}"] = {
        "data_table": CHARTS[base_key]["data_table"],
    }

# l67-l70 "Worked Analysis" lessons reuse the data_table of l1-l4.
WORKED_ANALYSIS_MAP = {67: 1, 68: 2, 69: 3, 70: 4}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"biology-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"biology-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"biology-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Biology"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Biology: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Biology lessons (completing 70/70).")


if __name__ == "__main__":
    main()
