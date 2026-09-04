#!/usr/bin/env python3
"""Depth pass, M2 Physics: fill in real, hand-checked data_table
content for the M2 Physics lessons not covered by the earlier
breadth-first batch. Brings M2 Physics to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning quantum
field theory and particle physics, cosmology and astrophysics,
condensed matter and quantum information, and nonlinear/statistical
physics; l101-l120 are "Worked Analysis" companions reusing the
data_table of l1-l20 (direct 1:1 mapping). l3 was already completed
by an earlier breadth-first batch, so its data_table is hard-coded
here for reuse (it falls within l1-l20, so it is also reused for
l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_physics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Renormalization group flow", "Describes how a physical theory's parameters change as the observation scale changes"],
    ["Fixed point", "A scale-invariant point where the theory's behavior stops changing under RG flow"],
])

CHARTS: dict[str, dict] = {
    "physics-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Advanced theoretical physics research", "Systematic mathematical and conceptual methods for studying fundamental physical theory"],
    ])},
    "physics-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Classical mechanics research", "Rigorous scholarly grounding in the mathematical foundations of classical dynamics"],
    ])},
    "physics-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Power counting", "Organizes an effective field theory's terms by their relative importance at low energy"],
    ])},
    "physics-m2-l5": {"data_table": table(["Type", "Feature"], [
        ["Chiral anomaly", "A classical symmetry broken by quantum effects, affecting particle decay rates"],
        ["Gauge anomaly", "Would break gauge symmetry, requiring cancellation for a consistent theory"],
    ])},
    "physics-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Lattice gauge theory", "Simulates quantum chromodynamics numerically by discretizing spacetime onto a lattice"],
    ])},
    "physics-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Asymptotic freedom", "The strong force weakens at short distances, allowing perturbative calculation at high energy"],
    ])},
    "physics-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Hierarchy problem", "Asks why the Higgs mass is so much smaller than the Planck scale; supersymmetry is one proposed solution"],
    ])},
    "physics-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Grand Unified Theory", "Proposes the strong, weak, and electromagnetic forces merge into one force at very high energy"],
    ])},
    "physics-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["PMNS matrix", "Describes how neutrino flavor states mix with neutrino mass states"],
    ])},
    "physics-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Baryogenesis", "Explains how the universe developed more matter than antimatter, requiring CP violation"],
    ])},
    "physics-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Cosmological constant problem", "The predicted vacuum energy vastly exceeds the observed value, a major unsolved puzzle"],
    ])},
    "physics-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Inflationary cosmology", "Proposes a rapid early-universe expansion that seeded primordial density perturbations"],
    ])},
    "physics-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["CMB anisotropy", "Tiny temperature variations in the cosmic microwave background reveal the early universe's structure"],
    ])},
    "physics-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Matter power spectrum", "Describes how matter density fluctuations are distributed across different length scales"],
    ])},
    "physics-m2-l16": {"data_table": table(["Candidate", "Feature"], [
        ["WIMPs", "Weakly interacting massive particles, a leading dark matter candidate"],
        ["Axions", "Very light particles originally proposed to solve the strong CP problem"],
    ])},
    "physics-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Modified gravity", "Alters gravitational laws instead of invoking dark energy/matter to explain cosmic observations"],
    ])},
    "physics-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Compact binary coalescence", "The merger of two neutron stars or black holes, a primary source of detected gravitational waves"],
    ])},
    "physics-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Numerical relativity", "Solves Einstein's equations computationally to simulate black hole mergers"],
    ])},
    "physics-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Bekenstein-Hawking entropy", "Assigns a black hole entropy proportional to its event horizon's surface area"],
    ])},
    "physics-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Black hole information paradox", "Questions whether information that falls into a black hole is truly destroyed by Hawking radiation"],
    ])},
    "physics-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["AdS/CFT correspondence", "A conjectured duality between gravity in anti-de Sitter space and a conformal field theory on its boundary"],
    ])},
    "physics-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Ryu-Takayanagi formula", "Relates entanglement entropy in a boundary theory to the area of a minimal surface in the bulk"],
    ])},
    "physics-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Spin network", "The quantum state representation of geometry used in loop quantum gravity"],
    ])},
    "physics-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Calabi-Yau manifold", "A special geometric shape used to compactify extra dimensions in string theory"],
    ])},
    "physics-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["D-brane", "An extended object in string theory on which open strings can end, central to gauge/gravity duality"],
    ])},
    "physics-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Lorentz invariance violation", "A possible quantum gravity signature that would break the standard symmetry of relativity"],
    ])},
    "physics-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Symmetry-protected phase", "A topological phase of matter whose properties are protected by an underlying symmetry"],
    ])},
    "physics-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Anyon", "A quasiparticle in 2D systems exhibiting exotic fractional quantum statistics"],
    ])},
    "physics-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Topological insulator", "Insulates in its interior but conducts via protected states on its surface"],
    ])},
    "physics-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Majorana fermion (condensed matter)", "A quasiparticle that is its own antiparticle, sought for topological quantum computing"],
    ])},
    "physics-m2-l32": {"data_table": table(["Type", "Feature"], [
        ["Cuprate superconductors", "Copper-oxide based high-temperature superconductors"],
        ["Iron-based superconductors", "A separate family discovered later with distinct pairing mechanisms"],
    ])},
    "physics-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Cooper pair", "A bound pair of electrons that carries current without resistance in a BCS superconductor"],
    ])},
    "physics-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Quantum criticality", "Studies phase transitions driven by quantum fluctuations at absolute zero"],
    ])},
    "physics-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Bose-Einstein condensation", "A state where a dilute gas of bosons occupies the same lowest quantum state at ultracold temperature"],
    ])},
    "physics-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Optical lattice", "A periodic light-based potential used to trap and simulate quantum many-body systems"],
    ])},
    "physics-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Many-body localization", "Disorder can prevent an isolated quantum system from reaching thermal equilibrium"],
    ])},
    "physics-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Entanglement entropy (many-body)", "Quantifies quantum correlations between subsystems in a complex many-particle state"],
    ])},
    "physics-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Exchange-correlation functional", "The approximated component of density functional theory that captures electron interactions"],
    ])},
    "physics-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Quantum Monte Carlo", "Stochastic methods for computing properties of strongly correlated electron systems"],
    ])},
    "physics-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Matrix product state", "A tensor network representation efficiently capturing entanglement in 1D quantum systems"],
    ])},
    "physics-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Threshold theorem", "Fault-tolerant quantum computation is possible if error rates stay below a critical threshold"],
    ])},
    "physics-m2-l43": {"data_table": table(["Algorithm", "Purpose"], [
        ["Shor's algorithm", "Efficiently factors large numbers, threatening classical encryption"],
        ["Grover's algorithm", "Provides a quadratic speedup for unstructured search"],
    ])},
    "physics-m2-l44": {"data_table": table(["Architecture", "Feature"], [
        ["Trapped ion", "Uses individual ions confined by electromagnetic fields as qubits"],
        ["Superconducting qubit", "Uses superconducting circuits cooled to near absolute zero"],
    ])},
    "physics-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Heisenberg limit", "The fundamental quantum precision bound achievable using entangled measurement resources"],
    ])},
    "physics-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Electron g-2", "One of the most precisely tested predictions in physics, matching QED calculation to extraordinary accuracy"],
    ])},
    "physics-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Muon anomalous magnetic moment", "A measured discrepancy from Standard Model prediction, possibly hinting at new physics"],
    ])},
    "physics-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Jet substructure", "Analyzes the internal pattern of collider particle jets to identify boosted heavy particles"],
    ])},
    "physics-m2-l49": {"data_table": table(["Component", "Role"], [
        ["Calorimeter", "Measures particle energy"],
        ["Tracker", "Reconstructs particle trajectories"],
    ])},
    "physics-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Beyond-Standard-Model search (LHC)", "Systematically searches collider data for evidence of new, unpredicted particles"],
    ])},
    "physics-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Seesaw mechanism", "Explains neutrinos' tiny mass via coupling to a very heavy hypothetical partner particle"],
    ])},
    "physics-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Multi-messenger astronomy", "Combines light, gravitational waves, and neutrinos from the same cosmic event"],
    ])},
    "physics-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Ultra-high-energy cosmic ray", "Extremely energetic particles from space whose origin remains an open astrophysics question"],
    ])},
    "physics-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Stellar nucleosynthesis", "The process by which stars fuse lighter elements into heavier ones"],
    ])},
    "physics-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Neutron star equation of state", "Relates pressure and density inside a neutron star, constrained by mass-radius observations"],
    ])},
    "physics-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Accretion disk physics", "Studies the hot rotating gas disk that forms around a compact object as it falls inward"],
    ])},
    "physics-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Relativistic MHD (jets)", "Models magnetized plasma flows powering astrophysical jets at near-light speed"],
    ])},
    "physics-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Magnetic reconnection", "The sudden rearrangement of magnetic field lines that releases large amounts of energy"],
    ])},
    "physics-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Tokamak plasma stability", "Studies how to confine hot plasma in a magnetic torus long enough to sustain fusion"],
    ])},
    "physics-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Inertial confinement fusion", "Compresses fuel using intense lasers to trigger fusion reactions"],
    ])},
    "physics-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Chaos in Hamiltonian systems", "Studies sensitive dependence on initial conditions in deterministic energy-conserving systems"],
    ])},
    "physics-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Non-equilibrium statistical mechanics", "Studies systems away from thermal equilibrium, where standard statistical rules don't directly apply"],
    ])},
    "physics-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Fluctuation-dissipation theorem", "Relates a system's spontaneous fluctuations to how it responds to external perturbation"],
    ])},
    "physics-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Active matter physics", "Studies self-propelled particles whose collective motion produces emergent patterns"],
    ])},
    "physics-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Polymer dynamics", "Studies how long-chain molecules move and behave in different physical states"],
    ])},
    "physics-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Glass transition", "The poorly understood process by which a liquid becomes a rigid, disordered solid without crystallizing"],
    ])},
    "physics-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Jamming transition", "Disordered granular or particulate systems can abruptly lock into a rigid, immobile state"],
    ])},
    "physics-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Molecular motor biophysics", "Studies how proteins convert chemical (ATP) energy into directed mechanical motion"],
    ])},
    "physics-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Optical/magnetic tweezers", "Techniques that manipulate and measure forces on single molecules directly"],
    ])},
    "physics-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Physics of neural computation", "Applies physical and information-theoretic models to how neurons process information"],
    ])},
    "physics-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Quantum biology", "Investigates whether quantum coherence effects play a functional role in photosynthesis"],
    ])},
    "physics-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Four-wave mixing", "A nonlinear optical process where interacting light waves generate a new frequency"],
    ])},
    "physics-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Attosecond physics", "Uses extremely short laser pulses to observe electron dynamics on their natural timescale"],
    ])},
    "physics-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Cavity QED strong coupling", "A regime where light and matter exchange energy faster than they dissipate it"],
    ])},
    "physics-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Photonic crystal / metamaterial", "Engineered structures that manipulate light in ways natural materials cannot"],
    ])},
    "physics-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Topological photonics", "Uses topological protection to guide light robustly around defects and disorder"],
    ])},
    "physics-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Precision atomic clock", "Uses atomic transitions to achieve extraordinarily accurate frequency and time standards"],
    ])},
    "physics-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Equivalence principle test", "Precisely tests whether gravitational and inertial mass are truly identical"],
    ])},
    "physics-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Baryon acoustic oscillations", "A characteristic length scale in galaxy clustering used as a cosmic 'standard ruler'"],
    ])},
    "physics-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Weak gravitational lensing", "Uses subtle distortions of background galaxy shapes to map dark matter distribution"],
    ])},
    "physics-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["21-cm cosmology", "Uses hydrogen's spin-flip radio signal to probe the universe's reionization epoch"],
    ])},
    "physics-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Transmission spectroscopy", "Analyzes starlight filtered through an exoplanet's atmosphere during transit"],
    ])},
    "physics-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Protoplanetary disk physics", "Studies the gas and dust disk around young stars from which planets form"],
    ])},
    "physics-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Helioseismology", "Studies the sun's internal structure using observed oscillations of its surface"],
    ])},
    "physics-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Space weather physics", "Studies how solar activity affects Earth's magnetosphere and technological systems"],
    ])},
    "physics-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Weyl/Dirac semimetal", "Condensed matter systems hosting quasiparticles mimicking relativistic massless fermions"],
    ])},
    "physics-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Skyrmion", "A topologically stable, particle-like swirling spin texture in chiral magnetic materials"],
    ])},
    "physics-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Spin-transfer torque", "Uses spin-polarized current to directly manipulate a magnetic material's orientation"],
    ])},
    "physics-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Transition metal dichalcogenide", "A family of 2D semiconducting materials studied beyond graphene for electronics"],
    ])},
    "physics-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Twisted bilayer graphene", "At a 'magic angle,' twisted graphene layers exhibit unconventional superconductivity"],
    ])},
    "physics-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Quantum simulation of gauge theories", "Uses controllable quantum systems to simulate otherwise intractable gauge theory dynamics"],
    ])},
    "physics-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Dark matter direct detection theory", "Predicts expected interaction rates between dark matter and detector materials"],
    ])},
    "physics-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Strong CP problem", "Asks why QCD does not visibly violate CP symmetry as strongly as theory allows; axions are a proposed solution"],
    ])},
    "physics-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Hubble tension", "A significant discrepancy between different methods of measuring the universe's expansion rate"],
    ])},
    "physics-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["B-mode polarization", "A predicted CMB polarization pattern that would provide evidence of primordial gravitational waves"],
    ])},
    "physics-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["UV-complete theory of gravity", "Seeks a theory of gravity that remains mathematically consistent at all energy scales"],
    ])},
    "physics-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Instanton", "A nonperturbative solution capturing tunneling effects invisible to standard perturbation theory"],
    ])},
    "physics-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Conformal bootstrap", "Constrains conformal field theories using consistency conditions alone, without a Lagrangian"],
    ])},
    "physics-m2-l99": {"data_table": table(["Component", "Purpose"], [
        ["Thesis research seminar", "Presents and defends original research toward a master's thesis in physics"],
    ])},
    "physics-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Casimir effect", "Two uncharged conducting plates experience a measurable attractive force from quantum vacuum fluctuations"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"physics-m2-l{base_n}"
    worked_key = f"physics-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Physics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Physics lessons.")


if __name__ == "__main__":
    main()
