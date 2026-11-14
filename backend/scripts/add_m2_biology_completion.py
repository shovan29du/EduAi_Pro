#!/usr/bin/env python3
"""Depth pass, M2 Biology: fill in real, hand-checked data_table
content for the M2 Biology lessons not covered by the earlier
breadth-first batch. Brings M2 Biology to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning genomics
and molecular biology techniques, synthetic biology and evolution,
ecology and organismal biology, cell biology and aging, and
developmental/systems biology; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_biology_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["CRISPR-Cas9", "A gene-editing tool that uses guide RNA to direct a Cas9 enzyme to cut specific DNA sequences"],
    ["Off-target effect", "Unintended DNA cuts at sites resembling but not matching the intended target sequence"],
])

CHARTS: dict[str, dict] = {
    "biology-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Advanced/systems biology research", "Systematic quantitative methods for studying complex biological networks"],
    ])},
    "biology-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Cell & molecular biology research", "Rigorous scholarly grounding in the mechanisms underlying cellular function"],
    ])},
    "biology-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Prime editing", "A CRISPR-based technique that precisely rewrites DNA without double-strand breaks"],
    ])},
    "biology-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Trajectory inference", "Computationally orders single cells along a developmental path from RNA sequencing data"],
    ])},
    "biology-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Spatial transcriptomics", "Measures gene expression while preserving each cell's physical location in a tissue"],
    ])},
    "biology-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["ATAC-seq", "Profiles which regions of chromatin are accessible and likely active for gene expression"],
    ])},
    "biology-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Epigenetic clock", "Estimates biological age from patterns of DNA methylation"],
    ])},
    "biology-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Long non-coding RNA", "RNA molecules that regulate gene expression without being translated into protein"],
    ])},
    "biology-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["CRISPR screen", "Systematically disrupts many genes to identify which are functionally important for a trait"],
    ])},
    "biology-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["AlphaFold-class methods", "Deep learning models that predict a protein's 3D structure from its amino acid sequence"],
    ])},
    "biology-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Cryo-electron microscopy", "Determines molecular structures by imaging flash-frozen samples with an electron microscope"],
    ])},
    "biology-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Liquid-liquid phase separation", "Cellular components can demix into distinct liquid-like compartments without a membrane"],
    ])},
    "biology-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Mitochondrial heteroplasmy", "The coexistence of mutant and normal mitochondrial DNA within one cell, with a disease threshold"],
    ])},
    "biology-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Organoid", "A lab-grown miniature organ-like structure used to study development and disease"],
    ])},
    "biology-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["FRET", "Fluorescence Resonance Energy Transfer; measures nanoscale distances between labeled molecules"],
    ])},
    "biology-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Optogenetics", "Uses light-sensitive proteins to precisely control neural activity"],
    ])},
    "biology-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Connectomics", "Maps the complete wiring diagram of connections within a neural circuit or brain"],
    ])},
    "biology-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Gut microbiome functional annotation", "Identifies what metabolic functions gut microbial genes actually encode"],
    ])},
    "biology-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Quorum sensing", "Bacteria coordinate collective behavior by detecting population density via signaling molecules"],
    ])},
    "biology-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Phage therapy resistance evolution", "Studies how bacteria evolve resistance to therapeutic bacteriophages over time"],
    ])},
    "biology-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Tumor immune evasion", "Mechanisms cancer cells use to escape detection and destruction by the immune system"],
    ])},
    "biology-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Clonal evolution (cancer)", "Cancer progresses through competing cell lineages that accumulate distinct mutations"],
    ])},
    "biology-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["CAR-T for solid tumors", "Engineers T cells to target solid tumors, a harder challenge than blood cancers"],
    ])},
    "biology-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic gene circuit", "An engineered set of genes designed to perform a programmed cellular function"],
    ])},
    "biology-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Directed evolution", "Iteratively mutates and selects proteins to improve or alter their catalytic function"],
    ])},
    "biology-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Cell-free protein synthesis", "Produces proteins outside living cells using isolated cellular machinery"],
    ])},
    "biology-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Minimal genome synthetic cell", "Constructs a cell with the smallest possible gene set still capable of life"],
    ])},
    "biology-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Xenobiology", "Explores expanded or alternative genetic alphabets beyond natural DNA/RNA bases"],
    ])},
    "biology-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Metabolic flux analysis", "Uses isotope tracing to measure the actual rates of reactions in a metabolic network"],
    ])},
    "biology-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Gene regulatory network modeling", "Systems-level models of how genes turn each other on and off"],
    ])},
    "biology-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["GWAS fine-mapping", "Narrows a genome-wide association signal down to the likely causal genetic variant"],
    ])},
    "biology-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Polygenic risk score", "Combines effects of many genetic variants to estimate disease risk"],
    ])},
    "biology-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Ancient DNA / paleogenomics", "Extracts and analyzes degraded genetic material from historical or fossil remains"],
    ])},
    "biology-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Convergent trait evolution", "Comparative genomics reveals how unrelated species evolve similar traits independently"],
    ])},
    "biology-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Phylogenomic inference", "Reconstructs evolutionary relationships using whole-genome sequence alignments"],
    ])},
    "biology-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Speciation genomics", "Studies the genetic barriers that prevent interbreeding between diverging populations"],
    ])},
    "biology-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Experimental evolution", "Observes real-time evolutionary change in microbial populations under controlled conditions"],
    ])},
    "biology-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Coevolutionary dynamics", "Studies how hosts and parasites reciprocally evolve in response to each other"],
    ])},
    "biology-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Ecological niche modeling", "Predicts a species' suitable habitat under future climate change scenarios"],
    ])},
    "biology-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Metapopulation dynamics", "Models how separate populations connected by migration persist across a landscape"],
    ])},
    "biology-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Trophic cascade", "A change at one level of a food web ripples through to affect other levels, used in restoration"],
    ])},
    "biology-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Stable isotope food web analysis", "Uses isotope ratios to trace energy flow through an ecosystem's food web"],
    ])},
    "biology-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Environmental DNA metabarcoding", "Detects species present in an environment from DNA traces in water or soil samples"],
    ])},
    "biology-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Coral symbiosis breakdown", "Thermal stress disrupts the coral-algae relationship, causing bleaching"],
    ])},
    "biology-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Plant-microbiome interactions", "Studies how root-zone (rhizosphere) microbes influence plant health and nutrition"],
    ])},
    "biology-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["CRISPR gene drive", "A genetic element designed to spread rapidly through a population, potentially suppressing it"],
    ])},
    "biology-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Plant synthetic biology (photosynthesis)", "Engineers plants to make photosynthesis more efficient"],
    ])},
    "biology-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Vernalization", "A cold-induced epigenetic memory that enables plants to flower at the right season"],
    ])},
    "biology-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Mycorrhizal network", "Fungal networks connect plant roots, transferring nutrients between different plants"],
    ])},
    "biology-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Stomatal signaling (drought)", "Molecular pathways controlling leaf pore closure to conserve water under drought stress"],
    ])},
    "biology-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Circadian clock mechanisms", "Studies the molecular feedback loops generating roughly 24-hour cycles across species"],
    ])},
    "biology-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Sleep homeostasis regulators", "Molecular factors that track and drive the biological need for sleep"],
    ])},
    "biology-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Proteostasis collapse (neurodegeneration)", "Failure of protein quality control systems underlies neurodegenerative disease"],
    ])},
    "biology-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Prion-like propagation", "Misfolded proteins can template the misfolding of normal proteins, spreading like an infection"],
    ])},
    "biology-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Adult neurogenesis niche", "Regulates the specialized brain environment that supports new neuron formation in adults"],
    ])},
    "biology-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Glial synaptic plasticity contribution", "Non-neuronal glial cells actively shape and modulate synaptic connections"],
    ])},
    "biology-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Blood-brain barrier dysfunction", "Breakdown of this protective barrier contributes to various neurological diseases"],
    ])},
    "biology-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Axon guidance cues", "Molecular signals that direct growing neurons to their correct target connections"],
    ])},
    "biology-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Highly regenerative species", "Studies organisms like axolotls that can regrow complex tissues and organs"],
    ])},
    "biology-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Stem cell niche", "The local environment that regulates stem cell self-renewal and fate determination"],
    ])},
    "biology-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["iPSC reprogramming efficiency", "Studies the factors limiting how efficiently adult cells convert to pluripotent stem cells"],
    ])},
    "biology-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Somatic mosaicism", "Individual cells within one body accumulate distinct mutations, creating genetic diversity within tissues"],
    ])},
    "biology-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Telomere biology", "Telomere shortening with each cell division limits a cell's total replicative lifespan"],
    ])},
    "biology-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Senolytic therapy", "Drugs designed to selectively eliminate accumulated senescent cells"],
    ])},
    "biology-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Autophagy regulation", "The cellular process of degrading and recycling damaged components to maintain homeostasis"],
    ])},
    "biology-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Unfolded protein response", "A cellular stress signaling network that manages accumulation of misfolded proteins"],
    ])},
    "biology-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Mitophagy", "Selective autophagic removal of damaged mitochondria to maintain cellular quality control"],
    ])},
    "biology-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Cell cycle checkpoint", "Surveillance mechanisms that halt cell division if DNA damage or errors are detected"],
    ])},
    "biology-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["DNA damage response", "Signaling cascades that detect DNA damage and coordinate repair or cell death"],
    ])},
    "biology-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Homologous recombination pathway choice", "Cells select between distinct DNA repair pathways depending on cell cycle stage"],
    ])},
    "biology-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Replication stress", "Obstacles during DNA replication can cause genome instability if unresolved"],
    ])},
    "biology-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Centromere/kinetochore assembly", "Regulates the chromosomal structures needed for accurate cell division"],
    ])},
    "biology-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Aneuploidy origins", "Chromosome segregation errors produce cells with abnormal chromosome numbers"],
    ])},
    "biology-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Extracellular vesicle signaling", "Cells communicate by releasing small membrane-bound packages carrying molecular cargo"],
    ])},
    "biology-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Cell migration mechanics", "The physical forces and mechanisms driving cell movement during tissue formation"],
    ])},
    "biology-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Mechanotransduction", "Cells convert physical mechanical forces into biochemical signals during development"],
    ])},
    "biology-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Reaction-diffusion morphogen gradient", "A mathematical model explaining how spatial patterns form from diffusing signaling molecules"],
    ])},
    "biology-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Left-right asymmetry", "Molecular mechanisms that establish consistent body-side asymmetry during vertebrate development"],
    ])},
    "biology-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Clock-and-wavefront model", "Explains rhythmic segment formation (somitogenesis) via an internal timer and moving signal"],
    ])},
    "biology-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Placental signaling", "Studies molecular communication across the maternal-fetal interface"],
    ])},
    "biology-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Primordial germ cell migration", "Studies how germline precursor cells are specified and travel to the developing gonad"],
    ])},
    "biology-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Genomic imprinting", "Some genes are expressed depending on which parent they were inherited from"],
    ])},
    "biology-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Transposable element regulation", "Cellular mechanisms that silence mobile genetic elements to protect genome integrity"],
    ])},
    "biology-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Alternative splicing code", "Computational prediction of the regulatory rules governing how exons are spliced together"],
    ])},
    "biology-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Ribosome profiling", "Measures how efficiently mRNAs are actively being translated into protein"],
    ])},
    "biology-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["mRNA vaccine platform", "Designs and stabilizes messenger RNA to safely instruct cells to produce an antigen"],
    ])},
    "biology-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Structural vaccinology", "Uses a pathogen's 3D structure to rationally design an effective vaccine antigen"],
    ])},
    "biology-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Broadly neutralizing antibody", "Antibodies effective against many strains of a rapidly mutating virus"],
    ])},
    "biology-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Antigenic drift", "Gradual viral mutation that allows a pathogen to evade prior immune recognition"],
    ])},
    "biology-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Viral latent reservoir", "A hidden, dormant infection reservoir that persists despite treatment"],
    ])},
    "biology-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Zoonotic spillover risk", "Models the factors that determine when a pathogen jumps from animals to humans"],
    ])},
    "biology-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Antimicrobial resistance transmission", "Studies how resistance genes spread between bacteria across networks"],
    ])},
    "biology-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Biofilm formation", "Bacteria form protective, structured communities embedded in a self-produced matrix"],
    ])},
    "biology-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Extremophile adaptation", "Studies molecular mechanisms allowing organisms to survive extreme environmental conditions"],
    ])},
    "biology-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Bioluminescence pathway diversity", "Different organisms have independently evolved distinct biochemical light-producing pathways"],
    ])},
    "biology-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Venom peptide evolution", "Studies how venom components diversify and specialize functionally over evolutionary time"],
    ])},
    "biology-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Sensory transduction (non-model organisms)", "Studies how diverse species convert sensory stimuli into neural signals"],
    ])},
    "biology-m2-l99": {"data_table": table(["Component", "Purpose"], [
        ["Thesis-level capstone", "Investigates an original molecular mechanism as graduate-level research"],
    ])},
    "biology-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Metabolic scaling theory", "Relates how metabolic rate scales with body size across the range of life, via allometry"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"biology-m2-l{base_n}"
    worked_key = f"biology-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Biology"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Biology: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Biology lessons.")


if __name__ == "__main__":
    main()
