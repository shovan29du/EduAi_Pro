#!/usr/bin/env python3
"""Depth pass, M1 Chemistry: fill in real, hand-checked data_table
content for the 99 M1 Chemistry lessons not covered by the earlier
breadth-first batch. Brings M1 Chemistry to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_chemistry_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "chemistry-m1-l1": {
        "data_table": table(["Field", "Feature"], [
            ["Physical chemistry", "Applies physics principles to explain chemical behavior"],
        ]),
    },
    "chemistry-m1-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Advanced & analytical chemistry", "Focuses on precise identification and quantification of chemical composition"],
        ]),
    },
    "chemistry-m1-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Molecular symmetry", "A molecule's symmetry elements predict its spectroscopic and reactive behavior"],
        ]),
    },
    "chemistry-m1-l5": {
        "data_table": table(["Technique", "Use"], [
            ["Multinuclear NMR", "Probes structure via nuclei beyond hydrogen, like carbon-13 or phosphorus-31"],
        ]),
    },
    "chemistry-m1-l6": {
        "data_table": table(["Technique", "Use"], [
            ["Tandem MS", "Fragments ions in stages to determine detailed peptide and protein structure"],
        ]),
    },
    "chemistry-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["Potential energy surface", "Maps how a molecular system's energy changes with atomic configuration"],
        ]),
    },
    "chemistry-m1-l8": {
        "data_table": table(["Type", "Feature"], [
            ["Homogeneous catalysis", "Catalyst exists in the same phase as reactants, often enabling high selectivity"],
            ["Heterogeneous catalysis", "Catalyst exists in a different phase, easing separation and reuse"],
        ]),
    },
    "chemistry-m1-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Organometallic catalysis", "Metal-carbon bonded compounds enable industrially critical transformations"],
        ]),
    },
    "chemistry-m1-l10": {
        "data_table": table(["Technique", "Use"], [
            ["Gel permeation chromatography", "Determines a polymer's molecular weight distribution"],
        ]),
    },
    "chemistry-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Self-assembly", "Molecules spontaneously organize into ordered nanoscale structures"],
        ]),
    },
    "chemistry-m1-l12": {
        "data_table": table(["Technique", "Use"], [
            ["Impedance spectroscopy", "Characterizes electrochemical interfaces via frequency-dependent response"],
        ]),
    },
    "chemistry-m1-l13": {
        "data_table": table(["Method", "Use"], [
            ["Molecular dynamics simulation", "Simulates atomic motion over time by numerically integrating interatomic forces"],
        ]),
    },
    "chemistry-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Signal transduction chemistry", "Studies the molecular mechanisms converting an extracellular signal into cellular response"],
        ]),
    },
    "chemistry-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Chemical biology probe", "Uses designed small molecules to investigate biomolecular function"],
        ]),
    },
    "chemistry-m1-l16": {
        "data_table": table(["Application", "Detail"], [
            ["Radiochemistry", "Uses radioactive isotopes for tracing, dating, and medical applications"],
        ]),
    },
    "chemistry-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Climate chemistry", "Studies the chemical processes governing atmospheric composition and climate feedback"],
        ]),
    },
    "chemistry-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Chemometrics", "Applies statistical methods to extract meaningful information from chemical data"],
        ]),
    },
    "chemistry-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Reproducibility in chemistry", "Independent replication is essential for validating experimental findings"],
        ]),
    },
    "chemistry-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone research defense", "Presents and defends original chemistry research findings and methodology"],
        ]),
    },
    "chemistry-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Exchange-correlation functional", "Approximates electron interaction effects central to density functional theory accuracy"],
        ]),
    },
    "chemistry-m1-l22": {
        "data_table": table(["Method", "Detail"], [
            ["Ab initio molecular dynamics", "Computes forces quantum mechanically at each simulation step rather than using fixed force fields"],
        ]),
    },
    "chemistry-m1-l23": {
        "data_table": table(["Method", "Detail"], [
            ["Coupled cluster theory", "Provides highly accurate electronic structure calculations for smaller systems"],
        ]),
    },
    "chemistry-m1-l24": {
        "data_table": table(["Theory", "Detail"], [
            ["Transition state theory", "Estimates reaction rate from the energy barrier at the reaction's critical configuration"],
        ]),
    },
    "chemistry-m1-l25": {
        "data_table": table(["Theory", "Detail"], [
            ["Marcus theory", "Predicts electron transfer rates based on reorganization energy and driving force"],
        ]),
    },
    "chemistry-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Photoredox catalysis", "Uses light-excited catalysts to drive otherwise inaccessible redox transformations"],
        ]),
    },
    "chemistry-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Organocatalysis", "Small organic molecules catalyze reactions with high enantioselectivity, without a metal"],
        ]),
    },
    "chemistry-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["C-H activation", "Directly functionalizes typically unreactive carbon-hydrogen bonds"],
        ]),
    },
    "chemistry-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Palladium cross-coupling", "Forms new carbon-carbon bonds via a palladium catalytic cycle"],
        ]),
    },
    "chemistry-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Click chemistry", "Uses highly reliable, high-yielding reactions like azide-alkyne cycloaddition"],
        ]),
    },
    "chemistry-m1-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Metal-organic framework", "A porous crystalline structure built from metal nodes and organic linkers"],
        ]),
    },
    "chemistry-m1-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Covalent organic framework", "A porous crystalline structure held together entirely by covalent bonds"],
        ]),
    },
    "chemistry-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Host-guest chemistry", "Studies selective, noncovalent binding between a host molecule and a guest species"],
        ]),
    },
    "chemistry-m1-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Molecular machine", "A mechanically interlocked molecule capable of controlled motion, e.g. a rotaxane"],
        ]),
    },
    "chemistry-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Jablonski diagram", "Maps the energy transitions a molecule undergoes after absorbing light"],
        ]),
    },
    "chemistry-m1-l36": {
        "data_table": table(["Technique", "Use"], [
            ["Time-resolved spectroscopy", "Tracks ultrafast chemical dynamics on femtosecond to nanosecond timescales"],
        ]),
    },
    "chemistry-m1-l37": {
        "data_table": table(["Technique", "Use"], [
            ["COSY", "Reveals which protons are coupled through bonds"],
            ["NOESY", "Reveals which protons are close in space"],
        ]),
    },
    "chemistry-m1-l38": {
        "data_table": table(["Technique", "Use"], [
            ["Solid-state NMR", "Characterizes materials that cannot be dissolved for solution-state analysis"],
        ]),
    },
    "chemistry-m1-l39": {
        "data_table": table(["Technique", "Use"], [
            ["X-ray crystallography", "Determines atomic structure from a crystal's diffraction pattern"],
        ]),
    },
    "chemistry-m1-l40": {
        "data_table": table(["Technique", "Use"], [
            ["Small-angle X-ray scattering", "Probes nanoscale structure and morphology in solution or solid samples"],
        ]),
    },
    "chemistry-m1-l41": {
        "data_table": table(["Technique", "Use"], [
            ["EPR spectroscopy", "Detects and characterizes species with unpaired electrons, like radicals"],
        ]),
    },
    "chemistry-m1-l42": {
        "data_table": table(["Technique", "Use"], [
            ["Ion mobility MS", "Separates ions by shape and size in addition to mass-to-charge ratio"],
        ]),
    },
    "chemistry-m1-l43": {
        "data_table": table(["Concept", "Formula"], [
            ["Van Deemter equation", "Relates chromatographic plate height to flow rate and band broadening"],
        ]),
    },
    "chemistry-m1-l44": {
        "data_table": table(["Technique", "Use"], [
            ["Chiral chromatography", "Separates enantiomers using a chiral stationary phase"],
        ]),
    },
    "chemistry-m1-l45": {
        "data_table": table(["Application", "Detail"], [
            ["Electrochemical impedance spectroscopy", "Diagnoses interfacial and charge transport behavior in electrochemical systems"],
        ]),
    },
    "chemistry-m1-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Solid electrolyte interphase", "A protective layer forming on battery electrodes that shapes cycling performance"],
        ]),
    },
    "chemistry-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Fuel cell catalysis", "Electrode catalysts control the rate of hydrogen oxidation and oxygen reduction"],
        ]),
    },
    "chemistry-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Photoelectrochemical water splitting", "Uses light-absorbing electrodes to drive hydrogen and oxygen production"],
        ]),
    },
    "chemistry-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["CO2 reduction electrocatalysis", "Converts carbon dioxide into useful fuels or chemicals using electrical energy"],
        ]),
    },
    "chemistry-m1-l50": {
        "data_table": table(["Approach", "Feature"], [
            ["Biological nitrogen fixation", "Nitrogenase enzymes convert atmospheric nitrogen under ambient conditions"],
            ["Synthetic nitrogen fixation", "The Haber-Bosch process requires high temperature and pressure"],
        ]),
    },
    "chemistry-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Ligand design", "Ligand electronic and steric properties tune a catalyst's activity and selectivity"],
        ]),
    },
    "chemistry-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Surface science", "Studies how reactants adsorb and react on a heterogeneous catalyst's surface"],
        ]),
    },
    "chemistry-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Zeolite shape selectivity", "A zeolite's pore geometry restricts which molecules can enter and react"],
        ]),
    },
    "chemistry-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Living polymerization", "Chain growth proceeds without termination, enabling precise molecular weight control"],
        ]),
    },
    "chemistry-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Block copolymer self-assembly", "Chemically distinct polymer blocks phase-separate into ordered nanostructures"],
        ]),
    },
    "chemistry-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Conducting polymer", "A polymer whose conjugated backbone enables electrical charge transport"],
        ]),
    },
    "chemistry-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Biodegradable polymer", "Designed to break down via natural biological processes after use"],
        ]),
    },
    "chemistry-m1-l58": {
        "data_table": table(["Principle", "Detail"], [
            ["Green chemistry", "Designs processes to minimize hazardous waste and solvent use"],
        ]),
    },
    "chemistry-m1-l59": {
        "data_table": table(["Metric", "Meaning"], [
            ["Atom economy", "The proportion of reactant mass incorporated into the desired product"],
        ]),
        "formulae": ["atom_economy = product_mass / total_reactant_mass * 100"],
    },
    "chemistry-m1-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Flow chemistry", "Continuous reaction processing enables safer, more scalable synthesis than batch methods"],
        ]),
    },
    "chemistry-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Mechanochemistry", "Uses mechanical force like grinding to drive reactions without solvent"],
        ]),
    },
    "chemistry-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Ionic liquid", "A salt that is liquid near room temperature, useful as a designer reaction medium"],
        ]),
    },
    "chemistry-m1-l63": {
        "data_table": table(["Technique", "Use"], [
            ["Radiochemical tracer", "Follows a labeled atom's path to reveal a reaction's detailed mechanism"],
        ]),
    },
    "chemistry-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Fission product chemistry", "Studies the chemical behavior of the diverse elements produced by nuclear fission"],
        ]),
    },
    "chemistry-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Actinide coordination chemistry", "Studies the distinctive bonding behavior of actinide elements with ligands"],
        ]),
    },
    "chemistry-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Metalloenzyme active site", "A metal ion at the enzyme core enables catalysis unavailable to organic groups alone"],
        ]),
    },
    "chemistry-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Bioconjugation", "Chemically links a biomolecule to another molecule while preserving biological function"],
        ]),
    },
    "chemistry-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Glycosylation mechanism", "Forms the glycosidic bond linking sugar units in carbohydrate synthesis"],
        ]),
    },
    "chemistry-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Total synthesis strategy", "Plans an efficient, selective route to construct a complex natural product"],
        ]),
    },
    "chemistry-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Chiral ligand design", "Ligand asymmetry transfers stereochemical control to the catalytic reaction product"],
        ]),
    },
    "chemistry-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Computational docking", "Predicts how a small molecule binds within a target protein's active site"],
        ]),
    },
    "chemistry-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["QSAR modeling", "Statistically relates molecular structure to biological activity for drug design"],
        ]),
    },
    "chemistry-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Lead optimization", "Iteratively refines a promising drug candidate's potency, selectivity, and safety"],
        ]),
    },
    "chemistry-m1-l74": {
        "data_table": table(["Concept", "Detail"], [
            ["Prodrug", "An inactive compound metabolized in the body into its active therapeutic form"],
        ]),
    },
    "chemistry-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Trace contaminant detection", "Requires highly sensitive analytical methods to detect substances at very low concentration"],
        ]),
    },
    "chemistry-m1-l76": {
        "data_table": table(["Reaction", "Detail"], [
            ["Ozone formation/depletion", "Photochemical reactions between pollutants and UV light shape stratospheric ozone levels"],
        ]),
    },
    "chemistry-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Aerosol climate forcing", "Atmospheric particles can either warm or cool climate depending on their optical properties"],
        ]),
    },
    "chemistry-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental fate modeling", "Predicts how a persistent pollutant moves and transforms through ecosystems"],
        ]),
    },
    "chemistry-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["Heavy metal speciation", "A metal's specific chemical form determines its mobility and toxicity in soil"],
        ]),
    },
    "chemistry-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Advanced oxidation process", "Generates highly reactive radicals to break down persistent water contaminants"],
        ]),
    },
    "chemistry-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Corrosion chemistry", "Electrochemical processes gradually degrade metals exposed to their environment"],
        ]),
    },
    "chemistry-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Nanoparticle synthesis control", "Reaction conditions precisely tune nanoparticle size and shape"],
        ]),
    },
    "chemistry-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum dot photophysics", "Nanoscale semiconductor size directly determines the emitted light's color"],
        ]),
    },
    "chemistry-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Perovskite solar cell material", "A crystal structure enabling efficient, low-cost photovoltaic light absorption"],
        ]),
    },
    "chemistry-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Thermoelectric material", "Converts a temperature gradient directly into electrical voltage"],
        ]),
    },
    "chemistry-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["Critical temperature trend", "Different superconductor material classes exhibit widely varying transition temperatures"],
        ]),
    },
    "chemistry-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Sol-gel process", "Transforms a liquid precursor solution into a solid ceramic or glass network"],
        ]),
    },
    "chemistry-m1-l88": {
        "data_table": table(["Concept", "Detail"], [
            ["Electrochemical biosensor", "Converts a biomolecule binding event into a measurable electrical signal"],
        ]),
    },
    "chemistry-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Fluorescent probe", "Designed to change light emission upon binding a specific cellular target"],
        ]),
    },
    "chemistry-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Gadolinium contrast agent", "A paramagnetic complex enhancing MRI image contrast in soft tissue"],
        ]),
    },
    "chemistry-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Radiopharmaceutical", "A radioactively labeled compound used for medical diagnostic imaging"],
        ]),
    },
    "chemistry-m1-l92": {
        "data_table": table(["Mode", "Feature"], [
            ["Competitive inhibition", "Inhibitor competes directly with substrate for the enzyme active site"],
            ["Non-competitive inhibition", "Inhibitor binds elsewhere, reducing enzyme activity regardless of substrate binding"],
        ]),
    },
    "chemistry-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Kinetic isotope effect", "Comparing reaction rates with isotope substitution reveals mechanistic detail"],
        ]),
    },
    "chemistry-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Software benchmarking", "Compares computational chemistry methods for accuracy and efficiency trade-offs"],
        ]),
    },
    "chemistry-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["High-throughput experimentation", "Rapidly screens many reaction conditions in parallel to accelerate discovery"],
        ]),
    },
    "chemistry-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Machine learning reaction prediction", "Trains models on reaction data to forecast likely outcomes and yields"],
        ]),
    },
    "chemistry-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Computer-aided synthesis planning", "Software proposes efficient synthetic routes by retrosynthetic analysis"],
        ]),
    },
    "chemistry-m1-l98": {
        "data_table": table(["Practice", "Purpose"], [
            ["Laboratory hazard assessment", "Identifies chemical risks before they cause harm in the research setting"],
        ]),
    },
    "chemistry-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Photocatalytic CO2-to-fuel conversion", "Uses light-driven catalysis to transform carbon dioxide into usable fuel"],
        ]),
    },
    "chemistry-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Metal-free organocatalytic aldol reaction", "Achieves high enantioselectivity without a metal, using a small organic catalyst"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Orbital Type", "Effect"], [
        ["Bonding orbital", "Lower energy, stabilizes the molecule"],
        ["Antibonding orbital", "Higher energy, destabilizes the molecule"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"chemistry-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"chemistry-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"chemistry-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Chemistry"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Chemistry: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Chemistry lessons (completing 120/120).")


if __name__ == "__main__":
    main()
