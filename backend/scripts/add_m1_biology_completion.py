#!/usr/bin/env python3
"""Depth pass, M1 Biology: fill in real, hand-checked data_table
content for the 99 M1 Biology lessons not covered by the earlier
breadth-first batch. Brings M1 Biology to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_biology_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "biology-m1-l1": {
        "data_table": table(["Field", "Feature"], [
            ["Physiology & anatomy", "Studies body structure and the functions that sustain life"],
        ]),
    },
    "biology-m1-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Systems biology", "Models biological networks as interacting systems rather than isolated parts"],
        ]),
    },
    "biology-m1-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Cell signaling pathway", "Transmits information from a cell surface receptor to a cellular response"],
        ]),
    },
    "biology-m1-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Autoimmunity", "The immune system mistakenly targets the body's own healthy tissue"],
        ]),
    },
    "biology-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Emerging viral threat", "Requires rapid genomic surveillance to track novel pathogen spread"],
        ]),
    },
    "biology-m1-l7": {
        "data_table": table(["Technology", "Use"], [
            ["Next-generation sequencing", "Rapidly reads massive amounts of DNA in parallel"],
        ]),
    },
    "biology-m1-l8": {
        "data_table": table(["Method", "Use"], [
            ["Protein structure prediction", "Computationally infers a protein's 3D fold from its amino acid sequence"],
        ]),
    },
    "biology-m1-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Molecular evolution", "Studies how DNA and protein sequences change over evolutionary time"],
        ]),
    },
    "biology-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Ecosystem modeling", "Uses mathematical models to predict ecological system behavior and change"],
        ]),
    },
    "biology-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Computational neuroscience", "Builds mathematical models of neural activity and brain function"],
        ]),
    },
    "biology-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Regenerative medicine", "Applies developmental biology principles to repair or replace damaged tissue"],
        ]),
    },
    "biology-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Conservation genetics", "Manages genetic diversity to prevent inbreeding depression in small populations"],
        ]),
    },
    "biology-m1-l14": {
        "data_table": table(["Step", "Purpose"], [
            ["Outbreak investigation", "Identifies the source and mode of spread to contain a disease cluster"],
        ]),
    },
    "biology-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Synthetic genomics", "Designs and constructs novel genetic sequences for engineered biological function"],
        ]),
    },
    "biology-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Precision oncology", "Tailors cancer treatment based on a tumor's specific molecular profile"],
        ]),
    },
    "biology-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Microbiome research", "Studies how resident microbial communities influence host health"],
        ]),
    },
    "biology-m1-l18": {
        "data_table": table(["Element", "Purpose"], [
            ["Grant proposal", "Communicates a research vision persuasively to secure funding"],
        ]),
    },
    "biology-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Responsible conduct of research", "Establishes ethical norms for integrity in scientific practice"],
        ]),
    },
    "biology-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone research defense", "Presents and defends original biology research findings and methodology"],
        ]),
    },
    "biology-m1-l21": {
        "data_table": table(["Component", "Role"], [
            ["Cas9", "Enzyme that cuts DNA at a location specified by guide RNA"],
        ]),
    },
    "biology-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Single-cell RNA sequencing", "Profiles gene expression in individual cells rather than bulk tissue averages"],
        ]),
    },
    "biology-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Spatial transcriptomics", "Maps gene expression while preserving each cell's original tissue location"],
        ]),
    },
    "biology-m1-l24": {
        "data_table": table(["Technique", "Use"], [
            ["ChIP-seq", "Identifies where a specific protein binds across the genome"],
        ]),
    },
    "biology-m1-l25": {
        "data_table": table(["Technique", "Use"], [
            ["ATAC-seq", "Maps regions of open, accessible chromatin genome-wide"],
        ]),
    },
    "biology-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Long non-coding RNA", "Regulates gene expression without being translated into protein"],
        ]),
    },
    "biology-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["MicroRNA silencing", "Small RNAs bind target mRNA to suppress its translation into protein"],
        ]),
    },
    "biology-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Alternative splicing", "Produces multiple protein variants from a single gene by combining exons differently"],
        ]),
    },
    "biology-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Molecular chaperone", "Assists proteins in folding correctly and prevents harmful aggregation"],
        ]),
    },
    "biology-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Ubiquitin-proteasome system", "Tags and degrades unwanted or misfolded proteins within the cell"],
        ]),
    },
    "biology-m1-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Autophagy", "Recycles damaged cellular components to maintain cellular quality control"],
        ]),
    },
    "biology-m1-l32": {
        "data_table": table(["Process", "Detail"], [
            ["Mitophagy", "Selectively degrades damaged mitochondria to maintain cellular health"],
        ]),
    },
    "biology-m1-l33": {
        "data_table": table(["Checkpoint", "Function"], [
            ["G1/S checkpoint", "Verifies DNA is undamaged before replication begins"],
        ]),
    },
    "biology-m1-l34": {
        "data_table": table(["Pathway", "Trigger"], [
            ["Intrinsic apoptosis", "Triggered by internal cellular stress signals"],
            ["Extrinsic apoptosis", "Triggered by external death receptor signals"],
        ]),
    },
    "biology-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Stem cell niche", "The local microenvironment that regulates stem cell behavior and fate"],
        ]),
    },
    "biology-m1-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["iPSC reprogramming", "Converts mature adult cells back into a pluripotent stem cell state"],
        ]),
    },
    "biology-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Organoid", "A lab-grown miniature tissue structure used to model disease and development"],
        ]),
    },
    "biology-m1-l38": {
        "data_table": table(["Technique", "Use"], [
            ["Single-molecule imaging", "Directly observes individual biomolecule behavior rather than bulk averages"],
        ]),
    },
    "biology-m1-l39": {
        "data_table": table(["Technique", "Use"], [
            ["Cryo-electron microscopy", "Determines high-resolution protein structure by freezing samples rapidly"],
        ]),
    },
    "biology-m1-l40": {
        "data_table": table(["Technique", "Use"], [
            ["Proteomic mass spectrometry", "Identifies and quantifies proteins in a complex biological sample"],
        ]),
    },
    "biology-m1-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Metabolomics", "Studies the complete set of small-molecule metabolites in a system"],
        ]),
    },
    "biology-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Gene regulatory network", "Models how genes and their products control each other's expression"],
        ]),
    },
    "biology-m1-l43": {
        "data_table": table(["Method", "Use"], [
            ["Flux balance analysis", "Predicts metabolic flow through a network under steady-state assumptions"],
        ]),
    },
    "biology-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Synteny", "Conserved gene order across species reveals evolutionary relationships"],
        ]),
    },
    "biology-m1-l45": {
        "data_table": table(["Method", "Purpose"], [
            ["Species tree reconstruction", "Infers evolutionary relationships using data from many genes together"],
        ]),
    },
    "biology-m1-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Selection scan", "Identifies genomic regions bearing signatures of past natural selection"],
        ]),
    },
    "biology-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Ancient DNA analysis", "Recovers and analyzes degraded genetic material from historical specimens"],
        ]),
    },
    "biology-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Horizontal gene transfer", "Microbes acquire genetic material from other organisms outside direct inheritance"],
        ]),
    },
    "biology-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Metagenomic sequencing", "Sequences genetic material directly from environmental or microbiome samples"],
        ]),
    },
    "biology-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Host-microbiome signaling", "Resident microbes communicate with host cells to influence physiology"],
        ]),
    },
    "biology-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Quorum sensing", "Bacteria coordinate collective behavior based on population density signals"],
        ]),
    },
    "biology-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Antibiotic resistance", "Overuse accelerates bacteria evolving resistance to existing drugs"],
        ]),
    },
    "biology-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Phage therapy", "Uses bacteriophages to selectively target and destroy pathogenic bacteria"],
        ]),
    },
    "biology-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Viral receptor recognition", "A virus's entry depends on binding a specific host cell surface receptor"],
        ]),
    },
    "biology-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Innate immune sensing", "Pattern recognition receptors detect conserved pathogen molecular features"],
        ]),
    },
    "biology-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["TCR diversity", "Genetic recombination generates a vast repertoire of antigen-recognizing T cell receptors"],
        ]),
    },
    "biology-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Affinity maturation", "B cells iteratively refine antibodies for stronger antigen binding"],
        ]),
    },
    "biology-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Immune checkpoint", "Cancer cells exploit checkpoint proteins to evade immune attack"],
        ]),
    },
    "biology-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["CAR T cell engineering", "Modifies a patient's T cells to specifically recognize and attack tumor cells"],
        ]),
    },
    "biology-m1-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Tumor microenvironment", "The surrounding cellular and molecular context influencing tumor growth"],
        ]),
    },
    "biology-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Driver mutation", "A genetic alteration that actively promotes cancer development, unlike a passenger mutation"],
        ]),
    },
    "biology-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Epigenetic reprogramming in cancer", "Abnormal gene expression patterns can drive tumor progression without DNA sequence change"],
        ]),
    },
    "biology-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Liquid biopsy", "Detects tumor-derived DNA in blood as a minimally invasive cancer monitoring tool"],
        ]),
    },
    "biology-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Morphogen gradient", "A signaling molecule's concentration gradient specifies cell fate across a developing tissue"],
        ]),
    },
    "biology-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Hox gene", "A conserved gene family specifying body segment identity along the developmental axis"],
        ]),
    },
    "biology-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Neural crest migration", "A specialized cell population migrates widely to form diverse tissue types"],
        ]),
    },
    "biology-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Regenerative model organism", "Species like axolotl and planaria reveal mechanisms of complex tissue regrowth"],
        ]),
    },
    "biology-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Molecular clock", "A feedback loop of gene expression generates the roughly 24-hour circadian rhythm"],
        ]),
    },
    "biology-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Synaptic remodeling", "Neural connections strengthen or weaken based on activity, underlying learning"],
        ]),
    },
    "biology-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Protein aggregation", "Misfolded proteins accumulate and contribute to neurodegenerative disease"],
        ]),
    },
    "biology-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Glial cell function", "Supports, insulates, and modulates neuronal signaling within neural circuits"],
        ]),
    },
    "biology-m1-l72": {
        "data_table": table(["Technique", "Use"], [
            ["Optogenetics", "Uses light-sensitive proteins to precisely control neural activity"],
        ]),
    },
    "biology-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Connectomics", "Maps the complete wiring diagram of neural connections in a nervous system"],
        ]),
    },
    "biology-m1-l74": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantitative trait locus", "A genomic region statistically associated with variation in a measurable trait"],
        ]),
    },
    "biology-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Transgenerational epigenetic inheritance", "Some acquired epigenetic marks can be passed to offspring"],
        ]),
    },
    "biology-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Species distribution model", "Predicts a species' likely geographic range from environmental variables"],
        ]),
    },
    "biology-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Metapopulation dynamics", "Studies how spatially separated populations connect through migration"],
        ]),
    },
    "biology-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Trophic cascade", "Changes at one level of a food web ripple through to reshape the entire ecosystem"],
        ]),
    },
    "biology-m1-l79": {
        "data_table": table(["Concept", "Example"], [
            ["Coevolutionary arms race", "Host and parasite continuously evolve countermeasures against each other"],
        ]),
    },
    "biology-m1-l80": {
        "data_table": table(["Barrier Type", "Example"], [
            ["Prezygotic isolation", "Prevents mating or fertilization between species"],
            ["Postzygotic isolation", "Reduces hybrid offspring viability or fertility"],
        ]),
    },
    "biology-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Adaptive radiation", "Rapid diversification of a lineage into many ecologically distinct species"],
        ]),
    },
    "biology-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Genetic rescue", "Introducing new genetic diversity can reduce inbreeding depression in a small population"],
        ]),
    },
    "biology-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Landscape genomics", "Relates genetic variation to environmental and geographic landscape features"],
        ]),
    },
    "biology-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Coral bleaching", "Environmental stress causes coral to expel their symbiotic algae, risking death"],
        ]),
    },
    "biology-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Extremophile adaptation", "Specialized biochemistry allows survival in conditions lethal to most life"],
        ]),
    },
    "biology-m1-l86": {
        "data_table": table(["Hormone", "Effect"], [
            ["Auxin", "Regulates plant cell elongation and growth direction"],
        ]),
    },
    "biology-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Induced plant resistance", "Prior pathogen exposure primes a plant for a faster future defense response"],
        ]),
    },
    "biology-m1-l88": {
        "data_table": table(["Component", "Role"], [
            ["Photosystem II", "Splits water and initiates the photosynthetic electron transport chain"],
        ]),
    },
    "biology-m1-l89": {
        "data_table": table(["Application", "Detail"], [
            ["CRISPR crop improvement", "Precisely edits crop genes to enhance yield, resistance, or nutrition"],
        ]),
    },
    "biology-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Genetic circuit", "Engineered gene networks perform logic-like functions within a living cell"],
        ]),
    },
    "biology-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Metabolic engineering", "Redirects a microorganism's metabolism to efficiently produce a target biofuel"],
        ]),
    },
    "biology-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Directed evolution", "Iterative mutation and selection engineers enzymes with improved industrial properties"],
        ]),
    },
    "biology-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Membrane transport modeling", "Applies biophysical principles to describe molecule movement across cell membranes"],
        ]),
    },
    "biology-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Protein-ligand docking", "Computationally predicts how a small molecule binds within a target protein"],
        ]),
    },
    "biology-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Polypharmacology", "Models how a single drug may interact with multiple biological targets"],
        ]),
    },
    "biology-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["High-dimensional omics statistics", "Requires specialized methods to handle datasets with far more variables than samples"],
        ]),
    },
    "biology-m1-l97": {
        "data_table": table(["Practice", "Purpose"], [
            ["Reproducibility practice", "Ensures experimental results can be independently verified by other labs"],
        ]),
    },
    "biology-m1-l98": {
        "data_table": table(["Concern", "Detail"], [
            ["Germline editing bioethics", "Raises unique concerns because changes are heritable across generations"],
        ]),
    },
    "biology-m1-l99": {
        "data_table": table(["Concern", "Detail"], [
            ["Dual-use research", "Legitimate biological research can carry risk of dangerous misuse"],
        ]),
    },
    "biology-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Xenotransplantation", "Gene-edited animal organs may reduce immune rejection in human transplant recipients"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Term", "Meaning"], [
        ["Chromatin", "The complex of DNA and proteins (histones) that packages DNA"],
        ["Epigenetics", "Heritable changes in gene expression that don't alter the DNA sequence"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"biology-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"biology-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"biology-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Biology"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Biology: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Biology lessons (completing 120/120).")


if __name__ == "__main__":
    main()
