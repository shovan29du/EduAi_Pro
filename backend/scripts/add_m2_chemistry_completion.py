#!/usr/bin/env python3
"""Depth pass, M2 Chemistry: fill in real, hand-checked data_table
content for the M2 Chemistry lessons not covered by the earlier
breadth-first batch. Brings M2 Chemistry to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
catalysis and synthetic methodology, materials/energy chemistry,
medicinal chemistry and drug design, spectroscopy and computational
chemistry, and polymer/green chemistry; l101-l120 are "Worked
Analysis" companions reusing the data_table of l1-l20 (direct 1:1
mapping). l3 was already completed by an earlier breadth-first batch,
so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_chemistry_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Organocatalysis", "Uses small organic molecules, rather than metals, to catalyze reactions"],
    ["Chiral amine catalyst", "Directs a reaction to preferentially form one mirror-image (enantiomer) product"],
])

CHARTS: dict[str, dict] = {
    "chemistry-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Advanced/analytical chemistry research", "Systematic instrumental and quantitative methods for chemical analysis"],
    ])},
    "chemistry-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["General/inorganic chemistry research", "Rigorous scholarly grounding in fundamental chemical structure and reactivity"],
    ])},
    "chemistry-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["C-H bond activation", "Metal catalysts selectively functionalize normally inert carbon-hydrogen bonds"],
    ])},
    "chemistry-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Photoredox catalysis", "Uses light-excited catalysts to drive single-electron radical coupling reactions"],
    ])},
    "chemistry-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Frustrated Lewis pair", "A Lewis acid-base pair sterically prevented from bonding, enabling unusual small-molecule activation"],
    ])},
    "chemistry-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Mechanochemical synthesis", "Uses mechanical grinding (ball-milling) to drive chemical reactions without solvent"],
    ])},
    "chemistry-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Bioorthogonal click chemistry", "Reactions selective enough to occur inside living systems without disrupting biology"],
    ])},
    "chemistry-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Metal-organic framework", "A porous crystalline material designed for selective gas capture and separation"],
    ])},
    "chemistry-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Covalent organic framework", "A porous crystalline material built entirely from covalently linked organic building blocks"],
    ])},
    "chemistry-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Single-atom catalyst", "Isolated individual metal atoms on a support maximize catalytic efficiency"],
    ])},
    "chemistry-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Electrocatalytic CO2 reduction", "Uses electrical energy and catalysts to convert CO2 into useful chemical products"],
    ])},
    "chemistry-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Hydrogen evolution reaction", "The catalytic reaction producing hydrogen gas, central to water-splitting technology"],
    ])},
    "chemistry-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Oxygen evolution reaction", "The catalytic reaction producing oxygen gas, the bottleneck step in water splitting"],
    ])},
    "chemistry-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Solid-state electrolyte", "A non-liquid ion conductor optimized to move ions quickly in next-generation batteries"],
    ])},
    "chemistry-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Lithium-sulfur battery degradation", "Studies polysulfide dissolution and other mechanisms limiting battery lifetime"],
    ])},
    "chemistry-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Solid-electrolyte interphase", "A protective layer forming on lithium-ion battery electrodes that governs performance and safety"],
    ])},
    "chemistry-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Perovskite defect passivation", "Chemically treats defects in perovskite solar cells to improve efficiency and stability"],
    ])},
    "chemistry-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Donor-acceptor morphology", "The nanoscale blend structure of organic photovoltaic materials that governs charge separation"],
    ])},
    "chemistry-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Host-guest complex", "A supramolecular assembly where one molecule (host) selectively binds another (guest)"],
    ])},
    "chemistry-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic covalent chemistry", "Uses reversible covalent bonds to make materials that can self-heal after damage"],
    ])},
    "chemistry-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Rotaxane", "A molecular machine where a ring component is mechanically interlocked around an axle"],
    ])},
    "chemistry-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Chiral amplification", "A small enantiomeric excess is autocatalytically amplified into near-complete chirality"],
    ])},
    "chemistry-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["DFT reaction mechanism prediction", "Uses density functional theory to computationally model how a chemical reaction proceeds"],
    ])},
    "chemistry-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["ML retrosynthesis", "Machine learning models suggest efficient synthetic routes by working backward from a target molecule"],
    ])},
    "chemistry-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["High-throughput experimentation", "Rapidly tests many reaction conditions in parallel to optimize a chemical process"],
    ])},
    "chemistry-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Flow chemistry", "Runs reactions continuously through tubing rather than in a traditional batch flask"],
    ])},
    "chemistry-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Directed evolution (enzymes)", "Iteratively mutates and selects enzymes to improve or alter their catalytic function"],
    ])},
    "chemistry-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Cascade biocatalysis", "Chains multiple enzymatic reactions together in one pot to build complex molecules"],
    ])},
    "chemistry-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Solvent effects", "The choice of solvent can significantly alter a reaction's rate and product selectivity"],
    ])},
    "chemistry-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Ionic liquid", "A salt that is liquid near room temperature, used as a designer green solvent"],
    ])},
    "chemistry-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Deep eutectic solvent", "A sustainable solvent mixture with a melting point far below its components'"],
    ])},
    "chemistry-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Atom economy", "Measures the fraction of reactant atoms incorporated into the final desired product"],
    ])},
    "chemistry-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Total synthesis strategy", "Plans a multistep route to construct a complex natural product from simple starting materials"],
    ])},
    "chemistry-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Late-stage functionalization", "Modifies a complex molecule's structure near the end of synthesis rather than from scratch"],
    ])},
    "chemistry-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Bioisosteric replacement", "Substitutes a molecular fragment with a similarly-behaving one to improve a drug candidate"],
    ])},
    "chemistry-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Fragment-based drug design", "Builds drugs by linking small, weakly-binding molecular fragments into a potent compound"],
    ])},
    "chemistry-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Structure-based drug design", "Designs new drug molecules using the 3D structure of their biological target"],
    ])},
    "chemistry-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Covalent inhibitor", "A drug that forms a permanent chemical bond with its target, tuned via reactive 'warhead' design"],
    ])},
    "chemistry-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["PROTAC", "A bifunctional molecule that recruits cellular machinery to degrade a target protein"],
    ])},
    "chemistry-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Prodrug design", "Chemically modifies a drug to improve its absorption, then converts to active form in the body"],
    ])},
    "chemistry-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Nanoparticle surface functionalization", "Chemically modifies nanoparticle surfaces to target and control drug delivery"],
    ])},
    "chemistry-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Polymer-drug conjugate", "Attaches a drug to a polymer carrier to control its release rate and duration"],
    ])},
    "chemistry-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Mass spectrometry proteomics", "Identifies and quantifies proteins in a sample based on their mass-to-charge ratios"],
    ])},
    "chemistry-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Cryo-EM sample preparation", "Optimizes flash-freezing conditions to preserve molecular structure for electron microscopy"],
    ])},
    "chemistry-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["NMR of protein dynamics", "Uses nuclear magnetic resonance to study how proteins move and change shape"],
    ])},
    "chemistry-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["2D NMR techniques", "Correlate multiple nuclei to resolve complex molecular structures that 1D NMR cannot"],
    ])},
    "chemistry-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Single-molecule spectroscopy", "Observes individual molecules' reaction dynamics rather than bulk-averaged behavior"],
    ])},
    "chemistry-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Femtosecond spectroscopy", "Uses ultrafast laser pulses to observe excited-state chemical dynamics on their natural timescale"],
    ])},
    "chemistry-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Time-resolved X-ray absorption", "Tracks catalytic intermediates' electronic structure as a reaction proceeds"],
    ])},
    "chemistry-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Surface-enhanced Raman spectroscopy", "Amplifies weak Raman signals to detect trace amounts of a molecule"],
    ])},
    "chemistry-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Electron paramagnetic resonance", "Detects and characterizes unpaired-electron radical intermediates in reactions"],
    ])},
    "chemistry-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Enzyme active site electrostatics", "Computationally models how charge distribution in an active site drives catalysis"],
    ])},
    "chemistry-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Binding free energy simulation", "Computationally estimates how strongly a small molecule binds a protein target"],
    ])},
    "chemistry-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Machine learning force field", "A trained model that approximates quantum forces for much faster molecular simulation"],
    ])},
    "chemistry-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Quantum computing (electronic structure)", "Explores using quantum computers to calculate molecular electronic properties efficiently"],
    ])},
    "chemistry-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Ab initio molecular dynamics", "Simulates atomic motion using quantum mechanical forces computed on the fly"],
    ])},
    "chemistry-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Multireference methods", "Quantum chemistry methods needed for systems where a single electron configuration is inadequate"],
    ])},
    "chemistry-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Time-dependent DFT", "Computes a molecule's excited electronic states and optical properties"],
    ])},
    "chemistry-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Inverse materials design", "Uses machine learning to work backward from desired properties to candidate material structures"],
    ])},
    "chemistry-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["High-throughput catalyst screening", "Computationally evaluates large libraries of candidate catalysts efficiently"],
    ])},
    "chemistry-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Crystal structure prediction", "Computationally predicts a compound's most stable crystal packing arrangement"],
    ])},
    "chemistry-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Pharmaceutical polymorphism", "Different crystal forms of the same drug can have significantly different properties"],
    ])},
    "chemistry-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Cocrystal engineering", "Combines a drug with a second compound in one crystal to improve solubility"],
    ])},
    "chemistry-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Amorphous solid dispersion", "Stabilizes a drug in a non-crystalline form to improve its solubility and bioavailability"],
    ])},
    "chemistry-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Living radical polymerization", "Enables precise control over polymer chain length and architecture"],
    ])},
    "chemistry-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Ring-opening metathesis polymerization", "Builds polymers by opening strained cyclic monomers via metal catalysis"],
    ])},
    "chemistry-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Block copolymer self-assembly", "Distinct polymer segments spontaneously organize into ordered nanostructures"],
    ])},
    "chemistry-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Stimuli-responsive polymer", "A smart material that changes properties in response to a specific external trigger"],
    ])},
    "chemistry-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Degradable polymer design", "Engineers polymers to break down predictably at end of life for sustainability"],
    ])},
    "chemistry-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Chemical plastic recycling", "Uses catalytic depolymerization to break plastics back into reusable monomers"],
    ])},
    "chemistry-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Carbon capture sorbent", "Materials designed to selectively bind and release CO2 with minimal regeneration energy"],
    ])},
    "chemistry-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Secondary organic aerosol formation", "Studies how atmospheric chemistry converts gases into airborne particulate matter"],
    ])},
    "chemistry-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Photocatalytic water purification", "Uses light-activated catalysts to break down contaminants in water"],
    ])},
    "chemistry-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Green chemistry metrics", "Quantitative measures for evaluating a chemical process's environmental sustainability"],
    ])},
    "chemistry-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Biomass valorization", "Converts plant-derived biomass into valuable platform chemicals"],
    ])},
    "chemistry-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Lignin depolymerization", "Breaks down lignin, a plant polymer, to recover valuable aromatic chemicals"],
    ])},
    "chemistry-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Electrochemical nitrogen reduction", "Explores a sustainable, lower-energy alternative to the Haber-Bosch ammonia process"],
    ])},
    "chemistry-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Zeolite framework", "Porous crystalline aluminosilicates used for shape-selective catalysis"],
    ])},
    "chemistry-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Bimetallic catalyst synergy", "Combining two metals in a nanoparticle can produce catalytic activity exceeding either alone"],
    ])},
    "chemistry-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Plasmonic photocatalysis", "Uses light-excited 'hot electrons' from metal nanoparticles to drive chemical reactions"],
    ])},
    "chemistry-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Molecular ion sensor", "A designed molecule that selectively binds and signals the presence of a target ion"],
    ])},
    "chemistry-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Electrochemical biosensor", "Detects biomolecules by converting a binding event into a measurable electrical signal"],
    ])},
    "chemistry-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Aptamer sensing", "Uses short, folded nucleic acid sequences that bind specific targets for chemical sensing"],
    ])},
    "chemistry-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Isotope labeling (kinetics)", "Tracks isotopically labeled atoms to reveal a reaction's mechanistic pathway"],
    ])},
    "chemistry-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Hammett relationship", "Correlates substituent electronic effects with reaction rate to probe mechanism"],
    ])},
    "chemistry-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Marcus theory", "Predicts electron transfer rates based on reorganization energy and driving force"],
    ])},
    "chemistry-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Non-covalent interaction analysis", "Studies weak forces (hydrogen bonds, pi-stacking) that govern molecular recognition"],
    ])},
    "chemistry-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Chiral metal complex catalysis", "Uses chiral metal catalysts to control stereochemistry in carbon-carbon bond formation"],
    ])},
    "chemistry-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Radical chain polymerization control", "Manages initiation, propagation, and termination to control polymer properties"],
    ])},
    "chemistry-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Electrochemical impedance spectroscopy", "Measures how a system responds to an oscillating voltage to probe interfacial reactions"],
    ])},
    "chemistry-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Operando spectroscopy", "Observes a catalyst's surface while it is actively working, not just before/after"],
    ])},
    "chemistry-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Pericyclic reaction selectivity", "Molecular orbital symmetry rules (Woodward-Hoffmann) predict outcomes of concerted reactions"],
    ])},
    "chemistry-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["[2+2] photocycloaddition", "A light-driven reaction forming a four-membered ring from two alkene units"],
    ])},
    "chemistry-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Halogen bonding", "A directional non-covalent interaction used in crystal engineering and molecular design"],
    ])},
    "chemistry-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Chirality transfer", "Studies how stereochemical information passes from catalyst to product across a reaction cycle"],
    ])},
    "chemistry-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Trace-level method validation", "Establishes rigor for analytical methods detecting very low contaminant concentrations"],
    ])},
    "chemistry-m2-l98": {"data_table": table(["Component", "Purpose"], [
        ["Thesis-level capstone", "Develops an original synthetic methodology as graduate-level research"],
    ])},
    "chemistry-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Tandem photoelectrochemical cell", "Stacks two light absorbers to more efficiently split water using sunlight"],
    ])},
    "chemistry-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Sonochemistry", "Uses ultrasound-induced bubble collapse (cavitation) to drive unusual chemical reactions"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"chemistry-m2-l{base_n}"
    worked_key = f"chemistry-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Chemistry"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Chemistry: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Chemistry lessons.")


if __name__ == "__main__":
    main()
