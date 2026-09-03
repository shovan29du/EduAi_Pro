#!/usr/bin/env python3
"""Depth pass, M1 Science: fill in real, hand-checked data_table
content for the 99 M1 Science lessons not covered by the earlier
breadth-first batch. Brings M1 Science to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "science-m1-l1": {
        "data_table": table(["Field", "Focus"], [
            ["Life science", "Studies living organisms and biological systems"],
        ]),
    },
    "science-m1-l2": {
        "data_table": table(["Field", "Focus"], [
            ["Physical science", "Studies matter, energy, and the physical universe"],
        ]),
    },
    "science-m1-l4": {
        "data_table": table(["Position", "View"], [
            ["Scientific realism", "Theoretical entities described by successful theories genuinely exist"],
            ["Anti-realism", "Theories are useful instruments, not necessarily literally true"],
        ]),
    },
    "science-m1-l5": {
        "data_table": table(["Era", "Feature"], [
            ["Scientific Revolution", "17th-century shift toward empirical, mathematical explanation of nature"],
        ]),
    },
    "science-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Interdisciplinary research design", "Integrates methods and frameworks across multiple scientific fields"],
        ]),
    },
    "science-m1-l7": {
        "data_table": table(["Skill", "Purpose"], [
            ["Science communication", "Translates technical findings for a non-specialist public audience"],
        ]),
    },
    "science-m1-l8": {
        "data_table": table(["Step", "Purpose"], [
            ["Peer review", "Independent experts evaluate a study before publication"],
        ]),
    },
    "science-m1-l9": {
        "data_table": table(["Concept", "Formula"], [
            ["Statistical power", "The probability of correctly detecting a true effect"],
        ]),
    },
    "science-m1-l10": {
        "data_table": table(["Technique", "Use"], [
            ["Mass spectrometry", "Identifies compounds by measuring the mass-to-charge ratio of ions"],
        ]),
    },
    "science-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Replication crisis", "Many published findings fail to reproduce under independent testing"],
        ]),
    },
    "science-m1-l12": {
        "data_table": table(["Body", "Role"], [
            ["Institutional review board", "Oversees research ethics to protect human research subjects"],
        ]),
    },
    "science-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Science policy", "Governs how public funding and regulation shape scientific research priorities"],
        ]),
    },
    "science-m1-l14": {
        "data_table": table(["Practice", "Purpose"], [
            ["Open science", "Makes data, methods, and findings freely accessible to accelerate discovery"],
        ]),
    },
    "science-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Science and society", "Examines how scientific findings interact with public values and policy"],
        ]),
    },
    "science-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Emerging technology governance", "Regulatory frameworks lag behind the pace of new technological capability"],
        ]),
    },
    "science-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental science seminar", "Synthesizes research across ecosystems, pollution, and sustainability"],
        ]),
    },
    "science-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Climate science seminar", "Examines evidence and modeling of long-term atmospheric and ocean change"],
        ]),
    },
    "science-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Pandemic preparedness", "Combines surveillance, stockpiling, and coordinated response planning"],
        ]),
    },
    "science-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone research proposal", "Defines a novel scientific question, methodology, and expected contribution"],
        ]),
    },
    "science-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum field theory", "Describes particles as excitations of underlying quantum fields"],
        ]),
    },
    "science-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["General relativity", "Describes gravity as the curvature of spacetime by mass and energy"],
        ]),
    },
    "science-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Phase transition", "A sudden qualitative change in a system's state as a parameter crosses a critical value"],
        ]),
    },
    "science-m1-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Condensed matter theory", "Studies emergent collective behavior in solids and liquids"],
        ]),
    },
    "science-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Standard Model", "The theoretical framework describing known fundamental particles and forces"],
        ]),
    },
    "science-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Astrophysical plasma", "Studies ionized gas dynamics in stars and interstellar environments"],
        ]),
    },
    "science-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Structure formation", "Explains how gravity amplified small density fluctuations into galaxies"],
        ]),
    },
    "science-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Chaos theory", "Studies deterministic systems highly sensitive to initial conditions"],
        ]),
    },
    "science-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Irreversible thermodynamics", "Studies systems away from equilibrium where entropy production is nonzero"],
        ]),
    },
    "science-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Molecular orbital theory", "Models bonding via combination of atomic orbitals into molecular orbitals"],
        ]),
    },
    "science-m1-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Organometallic mechanism", "Explains how metal-carbon bonded compounds catalyze chemical transformations"],
        ]),
    },
    "science-m1-l32": {
        "data_table": table(["Technique", "Use"], [
            ["NMR spectroscopy", "Reveals molecular structure via nuclear spin behavior in a magnetic field"],
        ]),
    },
    "science-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Surface chemistry", "Studies reactions and phenomena occurring at material interfaces"],
        ]),
    },
    "science-m1-l34": {
        "data_table": table(["Method", "Use"], [
            ["Molecular modeling", "Simulates molecular structure and behavior computationally"],
        ]),
    },
    "science-m1-l35": {
        "data_table": table(["Concept", "Formula"], [
            ["Michaelis-Menten kinetics", "Describes the rate of enzyme-catalyzed reactions"],
        ]),
    },
    "science-m1-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["Protein folding", "The process by which a polypeptide chain adopts its functional 3D structure"],
        ]),
    },
    "science-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Gene regulation", "Controls when and how much a gene is expressed as protein"],
        ]),
    },
    "science-m1-l38": {
        "data_table": table(["Mechanism", "Effect"], [
            ["DNA methylation", "Typically silences gene expression without changing the DNA sequence"],
        ]),
    },
    "science-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Systems biology", "Models biological networks as interacting systems rather than isolated parts"],
        ]),
    },
    "science-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Evo-devo", "Studies how developmental processes evolved to produce anatomical diversity"],
        ]),
    },
    "science-m1-l41": {
        "data_table": table(["Concept", "Formula"], [
            ["Hardy-Weinberg equilibrium", "p^2 + 2pq + q^2 = 1 models allele frequencies in a non-evolving population"],
        ]),
    },
    "science-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Metagenomics", "Sequences genetic material directly from environmental samples"],
        ]),
    },
    "science-m1-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["Molecular immunology", "Examines antigen recognition and signaling at the molecular level"],
        ]),
    },
    "science-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Synaptic plasticity", "The ability of synapses to strengthen or weaken over time based on activity"],
        ]),
    },
    "science-m1-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Computational neuroscience", "Builds mathematical models of neural activity and brain function"],
        ]),
    },
    "science-m1-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Cell signaling pathway", "Transmits information from a cell surface receptor to a cellular response"],
        ]),
    },
    "science-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Tumor microenvironment", "The surrounding cellular and molecular context influencing tumor growth"],
        ]),
    },
    "science-m1-l48": {
        "data_table": table(["Cell Type", "Potency"], [
            ["Pluripotent stem cell", "Can differentiate into nearly any cell type"],
        ]),
    },
    "science-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Astrobiology", "Studies the potential origin, distribution, and detection of life beyond Earth"],
        ]),
    },
    "science-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Planetary geophysics", "Studies the physical structure and processes of planetary bodies"],
        ]),
    },
    "science-m1-l51": {
        "data_table": table(["Wave Type", "Feature"], [
            ["P-wave", "Fastest seismic wave, compressional motion"],
            ["S-wave", "Slower shear wave, cannot travel through liquid"],
        ]),
    },
    "science-m1-l52": {
        "data_table": table(["Proxy", "Use"], [
            ["Ice core", "Records past atmospheric composition and temperature"],
        ]),
    },
    "science-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Aerosol science", "Studies suspended particles' formation, transport, and climate effects"],
        ]),
    },
    "science-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Ocean-atmosphere coupling", "Heat and moisture exchange between ocean and atmosphere drive climate patterns"],
        ]),
    },
    "science-m1-l55": {
        "data_table": table(["Method", "Use"], [
            ["Isotope tracing", "Uses isotope ratios to reconstruct geological and environmental history"],
        ]),
    },
    "science-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Nanotechnology", "Engineers materials and devices at the nanometer scale"],
        ]),
    },
    "science-m1-l57": {
        "data_table": table(["Material", "Property"], [
            ["Semiconductor", "Conductivity lies between conductors and insulators, tunable via doping"],
        ]),
    },
    "science-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Superconductivity", "Zero electrical resistance occurs below a material's critical temperature"],
        ]),
    },
    "science-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum optics", "Studies light's quantum properties, including single-photon phenomena"],
        ]),
    },
    "science-m1-l60": {
        "data_table": table(["Source", "Feature"], [
            ["Photovoltaic energy", "Converts sunlight directly into electricity via the photoelectric effect"],
        ]),
    },
    "science-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Electrochemical storage", "Stores energy via reversible chemical reactions, as in batteries"],
        ]),
    },
    "science-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Synthetic biology design", "Engineers standardized biological components into novel functional systems"],
        ]),
    },
    "science-m1-l63": {
        "data_table": table(["Component", "Role"], [
            ["Cas9", "Enzyme that cuts DNA at a location specified by guide RNA"],
        ]),
    },
    "science-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Bioinformatics algorithm", "Computational method for analyzing large-scale genomic sequence data"],
        ]),
    },
    "science-m1-l65": {
        "data_table": table(["Technique", "Use"], [
            ["Proteomic mass spectrometry", "Identifies and quantifies proteins in a complex biological sample"],
        ]),
    },
    "science-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Protein structure prediction", "Computationally infers a protein's 3D fold from its amino acid sequence"],
        ]),
    },
    "science-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Biostatistics for clinical research", "Applies rigorous statistical design to evaluate treatment efficacy and safety"],
        ]),
    },
    "science-m1-l68": {
        "data_table": table(["Model", "Feature"], [
            ["SIR model", "Compartmental model tracking Susceptible, Infected, and Recovered populations"],
        ]),
    },
    "science-m1-l69": {
        "data_table": table(["Concept", "Formula"], [
            ["Dose-response relationship", "Toxic effect generally increases with exposure dose"],
        ]),
    },
    "science-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Pollutant fate", "Tracks how a contaminant transforms and moves through the environment"],
        ]),
    },
    "science-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Biodiversity modeling", "Uses statistical and spatial models to predict species distribution and risk"],
        ]),
    },
    "science-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["Biogeochemical cycle", "The movement of an element like carbon or nitrogen through Earth's systems"],
        ]),
    },
    "science-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Behavioral ecology", "Studies how behavior evolves in response to ecological and social pressures"],
        ]),
    },
    "science-m1-l74": {
        "data_table": table(["Method", "Purpose"], [
            ["Phylogenetic tree building", "Visualizes evolutionary relationships among species or genes"],
        ]),
    },
    "science-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative genomics", "Analyzes genome differences and similarities across species"],
        ]),
    },
    "science-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Developmental signaling network", "Coordinates gene expression that shapes an organism's body plan"],
        ]),
    },
    "science-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Immunotherapy research", "Harnesses the immune system to target disease, particularly cancer"],
        ]),
    },
    "science-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Host-pathogen interaction", "Studies the molecular contest between an infecting virus and its host"],
        ]),
    },
    "science-m1-l79": {
        "data_table": table(["Method", "Use"], [
            ["Instrumental analytical chemistry", "Uses precision instruments for quantitative chemical measurement"],
        ]),
    },
    "science-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Polymer science", "Studies the synthesis and properties of long-chain molecular materials"],
        ]),
    },
    "science-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Turbulence", "Chaotic, irregular fluid motion that remains a major unsolved theoretical problem"],
        ]),
    },
    "science-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Dark matter detection", "Seeks indirect evidence of matter that does not interact via electromagnetism"],
        ]),
    },
    "science-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Gravitational wave", "A ripple in spacetime produced by accelerating massive objects"],
        ]),
    },
    "science-m1-l84": {
        "data_table": table(["Method", "Use"], [
            ["Transit method", "Detects exoplanets by measuring periodic dimming of a star's light"],
        ]),
    },
    "science-m1-l85": {
        "data_table": table(["Technique", "Use"], [
            ["X-ray crystallography", "Determines atomic structure from a crystal's diffraction pattern"],
        ]),
    },
    "science-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["Qubit", "Basic unit of quantum information that can exist in superposition"],
        ]),
    },
    "science-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Control theory in robotics", "Uses feedback to keep a system's behavior within desired bounds"],
        ]),
    },
    "science-m1-l88": {
        "data_table": table(["Method", "Use"], [
            ["Computational fluid dynamics", "Numerically simulates fluid flow behavior"],
        ]),
    },
    "science-m1-l89": {
        "data_table": table(["Concern", "Detail"], [
            ["Genetic engineering ethics", "Weighs benefits of gene editing against consent and unintended consequences"],
        ]),
    },
    "science-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Deep-sea ecosystem", "Supports life through chemosynthesis rather than photosynthesis in some regions"],
        ]),
    },
    "science-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Magma dynamics", "Studies molten rock movement and its role in volcanic eruption behavior"],
        ]),
    },
    "science-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Ice sheet dynamics", "Studies glacial flow and melt processes affecting sea-level change"],
        ]),
    },
    "science-m1-l93": {
        "data_table": table(["Technique", "Use"], [
            ["DNA profiling", "Identifies individuals from biological evidence using genetic markers"],
        ]),
    },
    "science-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Nutritional biochemistry", "Studies how food components are metabolized and affect health"],
        ]),
    },
    "science-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Structure-based drug design", "Uses a target protein's 3D structure to design effective binding molecules"],
        ]),
    },
    "science-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Structural materials science", "Studies material properties relevant to load-bearing engineering applications"],
        ]),
    },
    "science-m1-l97": {
        "data_table": table(["Concept", "Formula"], [
            ["Radioactive decay", "N = N0 * e^(-λt)"],
        ]),
    },
    "science-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Complex systems", "Studies emergent behavior arising from interacting components at scale"],
        ]),
    },
    "science-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Data-driven scientific discovery", "Applies machine learning to identify patterns in large scientific datasets"],
        ]),
    },
    "science-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Metrology", "The science of measurement, ensuring accuracy and standardization"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Philosopher", "Key Idea about Science"], [
        ["Karl Popper", "Science advances by falsification, not verification"],
        ["Thomas Kuhn", "Science progresses through 'paradigm shifts'"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"science-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"science-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"science-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Science lessons (completing 120/120).")


if __name__ == "__main__":
    main()
