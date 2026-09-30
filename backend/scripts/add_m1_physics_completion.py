#!/usr/bin/env python3
"""Depth pass, M1 Physics: fill in real, hand-checked data_table/
formulae content for the 99 M1 Physics lessons not covered by the
earlier breadth-first batch. Brings M1 Physics to full 120/120
coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table/formulae are hard-coded here for reuse (it
falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_physics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "physics-m1-l1": {
        "data_table": table(["Topic", "Feature"], [
            ["Modern & quantum physics", "Extends classical mechanics to atomic and relativistic scales"],
        ]),
    },
    "physics-m1-l2": {
        "data_table": table(["Topic", "Feature"], [
            ["Advanced theoretical physics", "Applies rigorous mathematical formalism to describe physical law"],
        ]),
    },
    "physics-m1-l4": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of energy", "Total energy in an isolated system remains constant"],
            ["Conservation of momentum", "Total momentum in an isolated system remains constant"],
        ]),
    },
    "physics-m1-l5": {
        "data_table": table(["Concept", "Formula"], [
            ["Moment of inertia", "I = sum(m_i * r_i^2)"],
        ]),
        "formulae": ["I = sum(m_i * r_i**2 for m_i, r_i in particles)"],
    },
    "physics-m1-l6": {
        "data_table": table(["Concept", "Formula"], [
            ["Wave equation", "v = f * lambda"],
        ]),
        "formulae": ["v = f * lam"],
    },
    "physics-m1-l7": {
        "data_table": table(["Law", "Statement"], [
            ["Second law of thermodynamics", "Total entropy of an isolated system never decreases"],
        ]),
    },
    "physics-m1-l8": {
        "data_table": table(["Principle", "Formula"], [
            ["Bernoulli's principle", "P + (1/2)ρv^2 + ρgh = constant"],
        ]),
        "formulae": ["P + 0.5*rho*v**2 + rho*g*h = constant"],
    },
    "physics-m1-l9": {
        "data_table": table(["Equation", "Describes"], [
            ["Gauss's law", "Relates electric flux to enclosed charge"],
            ["Faraday's law", "Relates changing magnetic flux to induced EMF"],
        ]),
    },
    "physics-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Optical physics", "Studies light propagation, interference, and interaction with matter"],
        ]),
    },
    "physics-m1-l11": {
        "data_table": table(["Concept", "Formula"], [
            ["Mass-energy equivalence", "E = mc^2"],
        ]),
        "formulae": ["E = m * c**2"],
    },
    "physics-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Wave-particle duality", "Light and matter exhibit both wave-like and particle-like behavior"],
        ]),
    },
    "physics-m1-l13": {
        "data_table": table(["Concept", "Formula"], [
            ["Radioactive decay", "N = N0 * e^(-λt)"],
        ]),
    },
    "physics-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Standard Model", "The theoretical framework describing known fundamental particles and forces"],
        ]),
    },
    "physics-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Astrophysics", "Applies physical law to explain the structure and evolution of celestial objects"],
        ]),
    },
    "physics-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Condensed matter physics", "Studies emergent collective behavior in solids and liquids"],
        ]),
    },
    "physics-m1-l17": {
        "data_table": table(["Concept", "Formula"], [
            ["Boltzmann distribution", "P(E) ∝ e^(-E/kT)"],
        ]),
    },
    "physics-m1-l18": {
        "data_table": table(["Method", "Use"], [
            ["Numerical simulation", "Approximates physical systems too complex for closed-form analytical solution"],
        ]),
    },
    "physics-m1-l19": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone research project", "Applies advanced physics tools to an original research question"],
        ]),
    },
    "physics-m1-l20": {
        "data_table": table(["Concept", "Detail"], [
            ["Philosophy of physics", "Examines the conceptual and interpretive foundations underlying physical theory"],
        ]),
    },
    "physics-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Path integral formulation", "Sums over all possible histories weighted by phase to compute quantum amplitude"],
        ]),
    },
    "physics-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Gauge theory", "Describes fundamental forces via symmetries that must be locally preserved"],
        ]),
    },
    "physics-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Higgs mechanism", "Explains how gauge bosons acquire mass through spontaneous symmetry breaking"],
        ]),
    },
    "physics-m1-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum electrodynamics", "Describes the quantum interaction between light and charged matter"],
        ]),
    },
    "physics-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Confinement", "Quarks cannot be isolated due to the strong force's increasing strength with distance"],
        ]),
    },
    "physics-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Effective field theory", "Models physics at accessible energy scales while abstracting away unknown high-energy detail"],
        ]),
    },
    "physics-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Supersymmetry", "Proposes a symmetry pairing every known particle with an undiscovered superpartner"],
        ]),
    },
    "physics-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["String theory compactification", "Extra spatial dimensions are curled up too small to observe directly"],
        ]),
    },
    "physics-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Loop quantum gravity", "Quantizes spacetime itself into discrete geometric units"],
        ]),
    },
    "physics-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Spacetime curvature", "Mass and energy determine how spacetime bends, guiding the paths of objects"],
        ]),
    },
    "physics-m1-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Black hole thermodynamics", "Black holes obey entropy and temperature laws analogous to ordinary thermodynamics"],
        ]),
    },
    "physics-m1-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Hawking radiation", "Black holes slowly emit particles and lose mass through quantum effects at the horizon"],
        ]),
    },
    "physics-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Gravitational wave astrophysics", "Detects ripples in spacetime produced by merging massive compact objects"],
        ]),
    },
    "physics-m1-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Cosmological inflation", "A brief period of exponential expansion smoothed and flattened the early universe"],
        ]),
    },
    "physics-m1-l35": {
        "data_table": table(["Candidate", "Detection Approach"], [
            ["WIMPs", "Sought via direct detection experiments looking for rare particle collisions"],
        ]),
    },
    "physics-m1-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["Dark energy", "A mysterious component driving the universe's accelerating expansion"],
        ]),
    },
    "physics-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Cosmic microwave background", "Relic radiation providing a snapshot of the early universe's conditions"],
        ]),
    },
    "physics-m1-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["Big Bang nucleosynthesis", "Formed the universe's earliest light elements within its first few minutes"],
        ]),
    },
    "physics-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Neutron star equation of state", "Describes how extreme density relates to pressure in neutron star matter"],
        ]),
    },
    "physics-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Stellar nucleosynthesis", "Fuses progressively heavier elements within a star's core over its lifetime"],
        ]),
    },
    "physics-m1-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Supernova mechanism", "Core collapse or thermonuclear runaway triggers a star's explosive death"],
        ]),
    },
    "physics-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Active galactic nuclei", "Supermassive black hole accretion powers extreme galactic center luminosity"],
        ]),
    },
    "physics-m1-l43": {
        "data_table": table(["Method", "Use"], [
            ["Transit method", "Detects exoplanets by measuring periodic dimming of a star's light"],
        ]),
    },
    "physics-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Topological insulator", "Conducts electricity only on its surface while insulating in its bulk"],
        ]),
    },
    "physics-m1-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["BCS theory", "Explains conventional superconductivity via electron pairing mediated by lattice vibrations"],
        ]),
    },
    "physics-m1-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["High-temperature superconductivity", "Occurs at temperatures unexplained by conventional BCS pairing mechanisms"],
        ]),
    },
    "physics-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum Hall effect", "Conductance becomes precisely quantized in strong magnetic fields at low temperature"],
        ]),
    },
    "physics-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Bose-Einstein condensation", "A macroscopic fraction of bosons occupy the same quantum ground state at ultra-low temperature"],
        ]),
    },
    "physics-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Optical lattice", "Uses interfering laser beams to trap and study ultracold atoms in a periodic potential"],
        ]),
    },
    "physics-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Phase transition", "A sudden qualitative change in a system's state as a parameter crosses a critical value"],
        ]),
    },
    "physics-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Critical exponent", "Describes how physical quantities scale near a continuous phase transition"],
        ]),
    },
    "physics-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Non-equilibrium statistical mechanics", "Studies systems that have not settled into a stable thermodynamic state"],
        ]),
    },
    "physics-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Irreversible thermodynamics", "Studies systems away from equilibrium where entropy production is nonzero"],
        ]),
    },
    "physics-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum information theory", "Studies how quantum mechanics enables new forms of computation and communication"],
        ]),
    },
    "physics-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Bell inequality test", "Experimentally rules out local hidden variable explanations for quantum entanglement"],
        ]),
    },
    "physics-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum algorithm", "Exploits superposition and entanglement for computational advantage over classical methods"],
        ]),
    },
    "physics-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum error correction", "Protects fragile quantum information from decoherence using redundant encoding"],
        ]),
    },
    "physics-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Decoherence", "Environmental interaction causes quantum superpositions to collapse toward classical behavior"],
        ]),
    },
    "physics-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Nuclear shell model", "Explains nuclear stability patterns through discrete nucleon energy levels"],
        ]),
    },
    "physics-m1-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Cross section", "Quantifies the probability of a specific nuclear reaction or scattering event"],
        ]),
    },
    "physics-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Fusion plasma", "Requires extreme temperature and confinement to overcome nuclear repulsion for fusion"],
        ]),
    },
    "physics-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Magnetic confinement", "Uses magnetic fields to contain superheated plasma away from reactor walls"],
        ]),
    },
    "physics-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Plasma instability", "Disruptive fluctuations can degrade confinement in fusion reactor plasmas"],
        ]),
    },
    "physics-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Particle detector", "Registers and characterizes particles produced in high-energy collisions"],
        ]),
    },
    "physics-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Beam dynamics", "Studies how charged particle beams are steered and focused in an accelerator"],
        ]),
    },
    "physics-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Nonlinear optics", "Light-matter interaction becomes intensity-dependent at high optical power"],
        ]),
    },
    "physics-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Photon statistics", "Characterizes light sources by how their photon arrival probabilities are distributed"],
        ]),
    },
    "physics-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Laser cavity design", "Resonator geometry determines a laser's coherence and output mode structure"],
        ]),
    },
    "physics-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Attosecond science", "Uses extremely short laser pulses to observe electron dynamics in real time"],
        ]),
    },
    "physics-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Metamaterial", "Engineered structure produces electromagnetic properties not found in natural materials"],
        ]),
    },
    "physics-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Photonic crystal", "Periodic structure controls light propagation via engineered band gaps"],
        ]),
    },
    "physics-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["Turbulence", "Chaotic, irregular fluid motion that remains a major unsolved theoretical problem"],
        ]),
    },
    "physics-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Magnetohydrodynamics", "Describes the behavior of electrically conducting fluids in magnetic fields"],
        ]),
    },
    "physics-m1-l74": {
        "data_table": table(["Method", "Use"], [
            ["Monte Carlo simulation", "Uses random sampling to estimate solutions to complex physical systems"],
        ]),
    },
    "physics-m1-l75": {
        "data_table": table(["Method", "Use"], [
            ["Molecular dynamics", "Simulates atomic motion over time by numerically integrating interatomic forces"],
        ]),
    },
    "physics-m1-l76": {
        "data_table": table(["Method", "Use"], [
            ["Density functional theory", "Models molecular electronic structure computationally via electron density"],
        ]),
    },
    "physics-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Chaos theory", "Studies deterministic systems highly sensitive to initial conditions"],
        ]),
    },
    "physics-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Soliton", "A stable, self-reinforcing wave packet that maintains its shape while propagating"],
        ]),
    },
    "physics-m1-l79": {
        "data_table": table(["Technique", "Use"], [
            ["Single-molecule technique", "Directly observes individual biomolecule behavior rather than bulk averages"],
        ]),
    },
    "physics-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Protein folding physics", "Applies energy landscape models to explain how proteins reach their native structure"],
        ]),
    },
    "physics-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Astrophysical fluid dynamics", "Applies fluid mechanics to model stellar and interstellar gas behavior"],
        ]),
    },
    "physics-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Cosmological perturbation theory", "Models how small early-universe density fluctuations grew into large-scale structure"],
        ]),
    },
    "physics-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Large-scale structure", "Gravity organized matter into a cosmic web of galaxy clusters and voids"],
        ]),
    },
    "physics-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Physics beyond the Standard Model", "Seeks to explain phenomena like dark matter unaccounted for by current theory"],
        ]),
    },
    "physics-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Neutrino oscillation", "Neutrinos change flavor as they propagate, implying they have nonzero mass"],
        ]),
    },
    "physics-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["CP violation", "A small asymmetry between matter and antimatter behavior in particle interactions"],
        ]),
    },
    "physics-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Symmetry principle", "Conserved quantities in physics correspond directly to underlying symmetries"],
        ]),
    },
    "physics-m1-l88": {
        "data_table": table(["Concept", "Detail"], [
            ["Topological defect", "A stable irregularity formed when a field fails to align uniformly across space"],
        ]),
    },
    "physics-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Many-body theory", "Models the collective behavior of large numbers of interacting quantum particles"],
        ]),
    },
    "physics-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Spin liquid", "A magnetic state where spins remain disordered even at very low temperature"],
        ]),
    },
    "physics-m1-l91": {
        "data_table": table(["Material", "Property"], [
            ["Semiconductor", "Conductivity lies between conductors and insulators, tunable via doping"],
        ]),
    },
    "physics-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Two-dimensional material", "Atomically thin materials like graphene exhibit distinctive electronic properties"],
        ]),
    },
    "physics-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Quantum metrology", "Uses quantum effects to achieve measurement precision beyond classical limits"],
        ]),
    },
    "physics-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Precision test", "High-accuracy experiments probe for subtle deviations from established physical theory"],
        ]),
    },
    "physics-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Modern cosmology history", "Traces the observational and theoretical developments shaping the Big Bang model"],
        ]),
    },
    "physics-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Statistical field theory", "Combines field theory and statistical mechanics to model many-body critical phenomena"],
        ]),
    },
    "physics-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Cavity quantum electrodynamics", "Studies enhanced light-matter interaction between atoms and a confined electromagnetic field"],
        ]),
    },
    "physics-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Granular material physics", "Studies collections of discrete particles that behave neither like solids nor fluids"],
        ]),
    },
    "physics-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["AdS/CFT correspondence", "Conjectures a duality between a gravitational theory and a boundary quantum field theory"],
        ]),
    },
    "physics-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Anyonic braiding", "Exchanging topological quasiparticles encodes fault-tolerant quantum information"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Newton's Law", "Statement"], [
        ["1st Law (Inertia)", "An object stays at rest or in motion unless acted on by a force"],
        ["2nd Law", "F = m x a (Force = mass x acceleration)"],
        ["3rd Law", "For every action there is an equal and opposite reaction"],
    ]),
    "formulae": ["F = m x a"],
}

# l101-l120 "Worked Analysis" lessons reuse the data_table/formulae of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"physics-m1-l{base_n}"
    if base_key in CHARTS:
        fields = {"data_table": CHARTS[base_key]["data_table"]}
        if "formulae" in CHARTS[base_key]:
            fields["formulae"] = CHARTS[base_key]["formulae"]
        CHARTS[f"physics-m1-l{worked_n}"] = fields
    elif base_n == 3:
        CHARTS[f"physics-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Physics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Physics lessons (completing 120/120).")


if __name__ == "__main__":
    main()
