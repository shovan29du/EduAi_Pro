#!/usr/bin/env python3
"""Depth pass, M2 Science: fill in real, hand-checked data_table
content for the M2 Science lessons not covered by the earlier
breadth-first batch. Brings M2 Science to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level research topics spanning
physics, structural/molecular biology, earth and climate science,
materials science, and neuroscience; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Topological quantum matter", "Phases of matter protected by topology rather than local order"],
    ["Majorana fermion", "A quasiparticle that is its own antiparticle, sought for topological quantum computing"],
])

CHARTS: dict[str, dict] = {
    "science-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Physical science research methods", "Systematic experimental and theoretical approaches used in physics and chemistry"],
    ])},
    "science-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Scientific measurement", "Quantifies observations with defined precision, accuracy, and uncertainty"],
    ])},
    "science-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Surface code", "A quantum error correction scheme encoding logical qubits across a 2D lattice of physical qubits"],
    ])},
    "science-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["AdS/CFT correspondence", "A conjectured duality between gravity in anti-de Sitter space and a conformal field theory on its boundary"],
    ])},
    "science-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Effective field theory", "Describes physics at accessible energy scales while integrating out unknown high-energy details"],
    ])},
    "science-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Lattice QCD", "Simulates quantum chromodynamics numerically by discretizing spacetime onto a lattice"],
    ])},
    "science-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Neutrino oscillation", "Neutrinos change flavor as they propagate, revealing they have nonzero mass"],
    ])},
    "science-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Gravitational wave data pipeline", "Extracts faint spacetime ripple signals from detector noise using matched filtering"],
    ])},
    "science-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Inflationary cosmology", "Proposes a rapid early-universe expansion that seeded primordial density perturbations"],
    ])},
    "science-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Dark matter direct detection", "Searches for rare collisions between dark matter particles and detector nuclei"],
    ])},
    "science-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Baryon acoustic oscillations", "A characteristic length scale in galaxy clustering used as a cosmic 'standard ruler'"],
    ])},
    "science-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Cryo-electron microscopy", "Determines molecular structures by imaging flash-frozen samples with an electron microscope"],
    ])},
    "science-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Prime editing", "A CRISPR-based technique that precisely rewrites DNA without double-strand breaks"],
    ])},
    "science-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Single-cell multi-omics", "Combines genomic, transcriptomic, and other data from individual cells simultaneously"],
    ])},
    "science-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Cryo-electron tomography", "Reconstructs 3D structures of cellular components from tilted electron microscope images"],
    ])},
    "science-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["AlphaFold-class methods", "Deep learning models that predict a protein's 3D structure from its amino acid sequence"],
    ])},
    "science-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic genetic circuit", "An engineered set of genes designed to perform a programmed cellular function"],
    ])},
    "science-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Organoid", "A lab-grown miniature organ-like structure used to study development and disease"],
    ])},
    "science-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Epigenetic clock", "Estimates biological age from patterns of DNA methylation"],
    ])},
    "science-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Flux balance analysis", "Predicts metabolic flow through a network under steady-state constraints"],
    ])},
    "science-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Structural variant", "A large-scale genomic alteration (deletion, duplication, inversion) detected from sequencing data"],
    ])},
    "science-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Selection scan", "Identifies genomic regions showing signatures of past natural selection"],
    ])},
    "science-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Ancient DNA / paleogenomics", "Extracts and analyzes degraded genetic material from historical or fossil remains"],
    ])},
    "science-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Metagenomic assembly", "Reconstructs genomes directly from mixed microbial community DNA samples"],
    ])},
    "science-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Host-microbiome signaling", "Studies molecular communication between a host organism and its resident microbes"],
    ])},
    "science-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["CAR-T therapy", "Engineers a patient's own T cells to recognize and attack specific cancer cells"],
    ])},
    "science-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Tumor microenvironment", "The surrounding cells and signals that shape how a cancer grows and evolves"],
    ])},
    "science-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Vitrification", "Rapidly cools biological material into a glass-like state to avoid damaging ice crystals"],
    ])},
    "science-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Climate model downscaling", "Converts coarse global climate projections into finer regional detail"],
    ])},
    "science-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Paleoclimate proxy", "Indirect physical evidence (like ice cores) used to reconstruct past climate"],
    ])},
    "science-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Ocean acidification", "Rising atmospheric CO2 lowers ocean pH, disrupting marine biogeochemistry"],
    ])},
    "science-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Aerosol-cloud interaction", "Aerosol particles alter cloud droplet formation and reflectivity"],
    ])},
    "science-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Tipping point", "A threshold beyond which a system shifts abruptly to a different stable state"],
    ])},
    "science-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Isotope geochemistry", "Uses ratios of isotopes to determine a rock or fluid's age and origin"],
    ])},
    "science-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Mantle convection", "Slow flow of Earth's mantle that drives plate tectonic motion"],
    ])},
    "science-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Paleoseismology", "Studies geological evidence of past earthquakes to estimate recurrence intervals"],
    ])},
    "science-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Transit spectroscopy", "Analyzes starlight filtered through an exoplanet's atmosphere during transit"],
    ])},
    "science-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Stellar nucleosynthesis", "The process by which stars fuse lighter elements into heavier ones"],
    ])},
    "science-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Biosignature", "A measurable indicator suggestive of past or present life on another world"],
    ])},
    "science-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive optics", "Corrects atmospheric distortion in real time to sharpen telescope images"],
    ])},
    "science-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Directed self-assembly", "Guides nanomaterials to organize into desired structures using external cues"],
    ])},
    "science-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Perovskite photovoltaic", "A promising solar cell material offering high efficiency at low production cost"],
    ])},
    "science-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Solid-state electrolyte", "A non-liquid ion conductor used in next-generation batteries for improved safety"],
    ])},
    "science-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Single-atom catalyst", "A catalyst where isolated individual metal atoms drive the reaction, maximizing efficiency"],
    ])},
    "science-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["DFT", "Density Functional Theory; computes molecular electronic structure to predict reaction mechanisms"],
    ])},
    "science-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["ML interatomic potential", "A machine-learned model approximating quantum forces for fast materials simulation"],
    ])},
    "science-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Metal-organic framework", "A porous crystalline material designed for selective gas capture and separation"],
    ])},
    "science-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Photocatalytic water splitting", "Uses light-activated catalysts to split water into hydrogen and oxygen"],
    ])},
    "science-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Quantum dot", "A nanoscale semiconductor whose optical properties can be tuned by its size"],
    ])},
    "science-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Unconventional superconductor", "A superconductor whose mechanism isn't explained by standard BCS phonon pairing"],
    ])},
    "science-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Spin qubit decoherence", "The loss of quantum information in a spin-based qubit due to environmental interaction"],
    ])},
    "science-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Photonic crystal / metamaterial", "Engineered structures that manipulate light in ways natural materials cannot"],
    ])},
    "science-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Plasma confinement", "Contains superheated fusion plasma using magnetic or inertial fields"],
    ])},
    "science-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Turbulence closure model", "Approximates the effect of unresolved small-scale turbulence in fluid simulations"],
    ])},
    "science-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Fluctuation theorem", "Quantifies the probability of entropy-decreasing events in non-equilibrium systems"],
    ])},
    "science-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Active matter physics", "Studies self-propelled particles whose collective motion produces emergent patterns"],
    ])},
    "science-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Network epidemiology", "Models disease spread over the structure of a contact network rather than uniform mixing"],
    ])},
    "science-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Phylodynamics", "Combines pathogen genetic sequences with epidemiological models to reconstruct transmission"],
    ])},
    "science-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Protein-ligand docking", "Computationally predicts how a small molecule binds to a protein's active site"],
    ])},
    "science-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Cryogenic sample preparation", "Rapidly freezes biological samples to preserve native structure for imaging"],
    ])},
    "science-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Optogenetics", "Uses light-sensitive proteins to precisely control neural activity"],
    ])},
    "science-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Connectomics", "Maps the complete wiring diagram of connections within a neural circuit or brain"],
    ])},
    "science-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Synaptic plasticity model", "Computationally represents how synapse strength changes with activity, underlying learning"],
    ])},
    "science-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Neural decoding", "Translates recorded brain activity patterns into inferred intended actions for BCIs"],
    ])},
    "science-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Predictive coding", "Proposes the brain constantly predicts sensory input and updates on prediction error"],
    ])},
    "science-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Circadian rhythm regulation", "Models the molecular feedback loops that generate roughly 24-hour biological cycles"],
    ])},
    "science-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Morphogen gradient", "A concentration gradient of a signaling molecule that patterns tissue during development"],
    ])},
    "science-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Stem cell niche", "The local environment that regulates stem cell self-renewal and differentiation"],
    ])},
    "science-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Cellular senescence", "A stable state of cell cycle arrest linked to aging and age-related disease"],
    ])},
    "science-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Proteostasis", "The cellular network maintaining proper protein folding, whose failure causes misfolding diseases"],
    ])},
    "science-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Structural ecology (biomechanics)", "Studies how organisms' physical structure adapts to extreme environmental forces"],
    ])},
    "science-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Null model (community ecology)", "A statistical baseline used to test whether observed species patterns differ from random"],
    ])},
    "science-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Early warning signal", "Statistical indicators (e.g. rising variance) that precede an ecosystem's critical transition"],
    ])},
    "science-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Coral bleaching", "Corals expel their symbiotic algae under thermal stress, threatening reef survival"],
    ])},
    "science-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Conservation genomics", "Uses genomic data to guide management decisions for endangered species"],
    ])},
    "science-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Landscape genetics", "Studies how landscape features affect gene flow and connectivity between populations"],
    ])},
    "science-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Agroecosystem nutrient cycling", "Models how nutrients move through farmed land systems"],
    ])},
    "science-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Precision fermentation", "Engineers microorganisms to efficiently produce specific target compounds at scale"],
    ])},
    "science-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Nanomedicine drug delivery", "Uses engineered nanoparticles to target drugs precisely to diseased tissue"],
    ])},
    "science-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["PK/PD modeling", "Models a drug's concentration over time (PK) and its resulting effect (PD)"],
    ])},
    "science-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Structure-based drug design", "Designs new drug molecules using the 3D structure of their biological target"],
    ])},
    "science-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Radiochemistry (medical isotopes)", "Produces and purifies radioactive isotopes for diagnostic and therapeutic medicine"],
    ])},
    "science-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Beam dynamics", "Studies how charged particle beams behave and are controlled in accelerators"],
    ])},
    "science-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Particle tracking detector", "Records the paths of charged particles produced in high-energy collisions"],
    ])},
    "science-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["NV center quantum sensing", "Uses nitrogen-vacancy defects in diamond as highly sensitive quantum sensors"],
    ])},
    "science-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Atom interferometry", "Uses matter-wave interference of cold atoms for extremely precise gravity measurements"],
    ])},
    "science-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Optical frequency comb", "A laser spectrum of evenly spaced frequencies enabling ultra-precise metrology"],
    ])},
    "science-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Glassy/amorphous system", "Disordered solids studied through statistical mechanics for their unusual relaxation behavior"],
    ])},
    "science-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Topological data analysis", "Extracts robust geometric and topological features from complex, high-dimensional data"],
    ])},
    "science-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["ML-guided materials discovery", "Uses machine learning to prioritize promising candidate materials for synthesis"],
    ])},
    "science-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Isotope fractionation", "Chemical and physical processes that alter isotope ratios during biogeochemical cycling"],
    ])},
    "science-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Radiative transfer modeling", "Simulates how light is absorbed, scattered, and emitted through a planetary atmosphere"],
    ])},
    "science-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Seismic tomography", "Uses earthquake wave travel times to image Earth's deep internal structure"],
    ])},
    "science-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Volcanic eruption forecasting", "Uses geophysical monitoring signals to anticipate volcanic activity"],
    ])},
    "science-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Ultra-high-energy cosmic ray", "Extremely energetic particles from space whose origin remains an open astrophysics question"],
    ])},
    "science-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Gravitational lensing", "Massive objects bend light, revealing the distribution of dark matter"],
    ])},
    "science-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Multi-messenger astronomy", "Combines light, gravitational waves, and particles from the same cosmic event"],
    ])},
    "science-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Network motif analysis", "Identifies recurring small sub-circuits that recur throughout biological networks"],
    ])},
    "science-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Quantitative systems pharmacology", "Models drug action across integrated biological networks rather than single targets"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"science-m2-l{base_n}"
    worked_key = f"science-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Science lessons.")


if __name__ == "__main__":
    main()
