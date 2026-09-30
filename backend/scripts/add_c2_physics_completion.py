#!/usr/bin/env python3
"""Depth pass, C2 Physics: fill in real, hand-checked data_table/formulae
content for the 69 C2 Physics lessons not covered by the earlier
breadth-first batch. Brings C2 Physics to full 70/70 coverage.

l61-l64 are "Foundations 2" lessons revisiting l7, l12, l17, and l46;
l65-l70 are "Worked Analysis" companions to l1-l6. l3 was already
completed by an earlier breadth-first batch, so its data_table/formulae
are hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_physics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "physics-c2-l1": {
        "data_table": table(["Topic", "Feature"], [
            ["Electricity, magnetism & waves", "Foundational unit connecting circuits, fields, and oscillatory motion"],
        ]),
    },
    "physics-c2-l2": {
        "data_table": table(["Topic", "Feature"], [
            ["Modern & quantum physics", "Extends classical mechanics to atomic and relativistic scales"],
        ]),
    },
    "physics-c2-l4": {
        "data_table": table(["Quantity", "Relation"], [
            ["Work-energy theorem", "Net work done equals the change in kinetic energy"],
        ]),
        "formulae": ["W_net = ΔKE = (1/2)mv_f^2 - (1/2)mv_i^2"],
    },
    "physics-c2-l5": {
        "data_table": table(["Quantity", "Formula"], [
            ["Torque", "τ = r x F sin(θ)"],
        ]),
        "formulae": ["τ = r * F * sin(theta)"],
    },
    "physics-c2-l6": {
        "data_table": table(["Property", "Meaning"], [
            ["Wavelength", "Distance between successive wave crests"],
            ["Frequency", "Number of wave cycles per second"],
        ]),
        "formulae": ["v = f * lambda"],
    },
    "physics-c2-l7": {
        "data_table": table(["Law", "Statement"], [
            ["First law of thermodynamics", "Energy is conserved: ΔU = Q - W"],
        ]),
        "formulae": ["delta_U = Q - W"],
    },
    "physics-c2-l8": {
        "data_table": table(["Principle", "Statement"], [
            ["Pascal's principle", "Pressure applied to an enclosed fluid is transmitted equally throughout"],
        ]),
        "formulae": ["P = F / A"],
    },
    "physics-c2-l9": {
        "data_table": table(["Quantity", "Formula"], [
            ["Magnetic force on a moving charge", "F = qvB sin(θ)"],
        ]),
        "formulae": ["F = q * v * B"],
    },
    "physics-c2-l10": {
        "data_table": table(["Lens Type", "Effect"], [
            ["Convex lens", "Converges light rays, can form real or virtual images"],
            ["Concave lens", "Diverges light rays, forms virtual images"],
        ]),
        "formulae": ["1/f = 1/d_o + 1/d_i"],
    },
    "physics-c2-l11": {
        "data_table": table(["Effect", "Formula"], [
            ["Time dilation", "t = t0 / sqrt(1 - v^2/c^2)"],
        ]),
        "formulae": ["t = t0 / (1 - v**2/c**2)**0.5"],
    },
    "physics-c2-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Wave-particle duality", "Light and matter exhibit both wave-like and particle-like behavior"],
        ]),
        "formulae": ["E = h * f"],
    },
    "physics-c2-l13": {
        "data_table": table(["Concept", "Formula"], [
            ["Radioactive decay", "N = N0 * e^(-λt)"],
        ]),
        "formulae": ["N = N0 * (0.5 ** (t / half_life))"],
    },
    "physics-c2-l14": {
        "data_table": table(["Particle Class", "Example"], [
            ["Quarks", "Up, down, charm, strange, top, bottom"],
            ["Leptons", "Electron, muon, tau, and their neutrinos"],
        ]),
    },
    "physics-c2-l15": {
        "data_table": table(["Class", "Feature"], [
            ["O-type star", "Hottest and most massive, blue-white in color"],
            ["M-type star", "Coolest, red in color, most common class"],
        ]),
    },
    "physics-c2-l16": {
        "data_table": table(["Property", "Detail"], [
            ["Resistivity", "Intrinsic material property determining resistance to current flow"],
        ]),
        "formulae": ["R = resistivity * L / A"],
    },
    "physics-c2-l17": {
        "data_table": table(["Law", "Statement"], [
            ["Ideal gas law", "PV = nRT"],
        ]),
        "formulae": ["P * V = n * R * T"],
    },
    "physics-c2-l18": {
        "data_table": table(["Method", "Use"], [
            ["Numerical integration", "Approximates position and velocity from acceleration data over small time steps"],
        ]),
        "formulae": ["v_next = v + a * dt\nx_next = x + v * dt"],
    },
    "physics-c2-l19": {
        "data_table": table(["Error Type", "Detail"], [
            ["Systematic error", "Consistent bias affecting all measurements the same way"],
            ["Random error", "Unpredictable variation scattered around the true value"],
        ]),
    },
    "physics-c2-l20": {
        "data_table": table(["Phenomenon", "Explanation"], [
            ["Boiling", "Occurs when vapor pressure equals surrounding atmospheric pressure"],
        ]),
    },
    "physics-c2-l21": {
        "data_table": table(["Quantity", "Formula"], [
            ["2D projectile range", "R = v0^2 sin(2θ) / g"],
        ]),
        "formulae": ["R = (v0**2) * math.sin(2*theta) / g"],
    },
    "physics-c2-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Center of mass", "The weighted average position of a system's mass distribution"],
        ]),
        "formulae": ["x_cm = sum(m_i * x_i) / sum(m_i)"],
    },
    "physics-c2-l23": {
        "data_table": table(["Effect", "Detail"], [
            ["Air resistance", "Introduces velocity-dependent drag that shortens projectile range"],
        ]),
    },
    "physics-c2-l24": {
        "data_table": table(["Shape", "Moment of Inertia"], [
            ["Solid sphere", "I = (2/5)mr^2"],
            ["Hoop", "I = mr^2"],
        ]),
        "formulae": ["I_sphere = (2/5) * m * r**2"],
    },
    "physics-c2-l25": {
        "data_table": table(["Law", "Statement"], [
            ["Angular momentum conservation", "L = Iω remains constant absent external torque"],
        ]),
        "formulae": ["L = I * omega"],
    },
    "physics-c2-l26": {
        "data_table": table(["Law", "Statement"], [
            ["Kepler's third law", "T^2 is proportional to a^3 for orbiting bodies"],
        ]),
        "formulae": ["T**2 = (4 * math.pi**2 / (G * M)) * a**3"],
    },
    "physics-c2-l27": {
        "data_table": table(["Collision Type", "Feature"], [
            ["Elastic collision", "Kinetic energy is conserved"],
            ["Inelastic collision", "Kinetic energy is not conserved, though momentum still is"],
        ]),
        "formulae": ["m1*v1 + m2*v2 = m1*v1_f + m2*v2_f"],
    },
    "physics-c2-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Lagrangian mechanics", "Formulates motion using energy differences rather than forces directly"],
        ]),
        "formulae": ["L = KE - PE"],
    },
    "physics-c2-l29": {
        "data_table": table(["Type", "Feature"], [
            ["Damped oscillation", "Amplitude decreases over time due to energy loss"],
            ["Driven oscillation", "External periodic force sustains or amplifies motion"],
        ]),
    },
    "physics-c2-l30": {
        "data_table": table(["Interference Type", "Result"], [
            ["Constructive interference", "Waves combine to produce larger amplitude"],
            ["Destructive interference", "Waves combine to reduce or cancel amplitude"],
        ]),
    },
    "physics-c2-l31": {
        "data_table": table(["Concept", "Formula"], [
            ["Standing wave frequency", "f_n = n*v / (2L)"],
        ]),
        "formulae": ["f_n = n * v / (2 * L)"],
    },
    "physics-c2-l32": {
        "data_table": table(["Effect", "Formula"], [
            ["Doppler shift (approaching source)", "f_observed = f_source * v / (v - v_source)"],
        ]),
        "formulae": ["f_observed = f_source * v / (v - v_source)"],
    },
    "physics-c2-l33": {
        "data_table": table(["Law", "Statement"], [
            ["Second law of thermodynamics", "Total entropy of an isolated system never decreases"],
        ]),
    },
    "physics-c2-l34": {
        "data_table": table(["Cycle", "Feature"], [
            ["Carnot cycle", "Sets the theoretical maximum efficiency for a heat engine"],
        ]),
        "formulae": ["efficiency = 1 - (T_cold / T_hot)"],
    },
    "physics-c2-l35": {
        "data_table": table(["Principle", "Formula"], [
            ["Bernoulli's principle", "P + (1/2)ρv^2 + ρgh = constant"],
        ]),
        "formulae": ["P + 0.5*rho*v**2 + rho*g*h = constant"],
    },
    "physics-c2-l36": {
        "data_table": table(["Property", "Effect"], [
            ["Viscosity", "Internal friction that resists fluid flow"],
        ]),
    },
    "physics-c2-l37": {
        "data_table": table(["Concept", "Formula"], [
            ["Electric field from a point charge", "E = kQ/r^2"],
        ]),
        "formulae": ["E = k * Q / r**2"],
    },
    "physics-c2-l38": {
        "data_table": table(["Concept", "Formula"], [
            ["Electric potential energy", "U = kQq/r"],
        ]),
        "formulae": ["U = k * Q * q / r"],
    },
    "physics-c2-l39": {
        "data_table": table(["Concept", "Formula"], [
            ["Capacitance", "C = Q/V"],
        ]),
        "formulae": ["C = Q / V"],
    },
    "physics-c2-l40": {
        "data_table": table(["Law", "Statement"], [
            ["Kirchhoff's current law", "Sum of currents entering a junction equals sum leaving"],
            ["Kirchhoff's voltage law", "Sum of voltage changes around a closed loop equals zero"],
        ]),
    },
    "physics-c2-l41": {
        "data_table": table(["Circuit", "Behavior"], [
            ["RC circuit", "Charges/discharges exponentially with time constant τ = RC"],
        ]),
        "formulae": ["tau = R * C"],
    },
    "physics-c2-l42": {
        "data_table": table(["Quantity", "Formula"], [
            ["Magnetic force on moving charge", "F = qv x B"],
        ]),
        "formulae": ["F = q * v * B"],
    },
    "physics-c2-l43": {
        "data_table": table(["Law", "Statement"], [
            ["Ampere's law", "Relates the magnetic field circulating around a loop to enclosed current"],
        ]),
    },
    "physics-c2-l44": {
        "data_table": table(["Equation", "Describes"], [
            ["Gauss's law", "Relates electric flux to enclosed charge"],
            ["Faraday's law", "Relates changing magnetic flux to induced EMF"],
        ]),
    },
    "physics-c2-l45": {
        "data_table": table(["Phenomenon", "Detail"], [
            ["Diffraction", "Bending of waves around obstacles or through narrow openings"],
        ]),
    },
    "physics-c2-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Polarization", "Restricting light's electric field oscillation to a single plane"],
        ]),
    },
    "physics-c2-l47": {
        "data_table": table(["Model", "Feature"], [
            ["Bohr model", "Electrons occupy discrete energy levels around the nucleus"],
        ]),
        "formulae": ["E_n = -13.6 / n**2"],
    },
    "physics-c2-l48": {
        "data_table": table(["Equation", "Purpose"], [
            ["Schrödinger equation", "Describes how a quantum system's wavefunction evolves over time"],
        ]),
    },
    "physics-c2-l49": {
        "data_table": table(["Quantum Number", "Meaning"], [
            ["Principal (n)", "Energy level of the electron"],
            ["Spin (m_s)", "Intrinsic electron spin orientation"],
        ]),
    },
    "physics-c2-l50": {
        "data_table": table(["Concept", "Formula"], [
            ["Binding energy", "E = Δm c^2"],
        ]),
        "formulae": ["E = delta_m * c**2"],
    },
    "physics-c2-l51": {
        "data_table": table(["Force", "Particle Carrier"], [
            ["Electromagnetic force", "Photon"],
            ["Strong force", "Gluon"],
        ]),
    },
    "physics-c2-l52": {
        "data_table": table(["Effect", "Formula"], [
            ["Length contraction", "L = L0 * sqrt(1 - v^2/c^2)"],
        ]),
        "formulae": ["L = L0 * (1 - v**2/c**2)**0.5"],
    },
    "physics-c2-l53": {
        "data_table": table(["Concept", "Formula"], [
            ["Mass-energy equivalence", "E = mc^2"],
        ]),
        "formulae": ["E = m * c**2"],
    },
    "physics-c2-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["General relativity", "Gravity arises from the curvature of spacetime by mass and energy"],
        ]),
    },
    "physics-c2-l55": {
        "data_table": table(["Process", "Detail"], [
            ["Nuclear fusion in stars", "Hydrogen nuclei fuse into helium, releasing energy that powers the star"],
        ]),
    },
    "physics-c2-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Big Bang cosmology", "The universe has been expanding from an extremely hot, dense initial state"],
        ]),
    },
    "physics-c2-l57": {
        "data_table": table(["Structure", "Feature"], [
            ["Crystal lattice", "A regular, repeating arrangement of atoms in a solid"],
        ]),
    },
    "physics-c2-l58": {
        "data_table": table(["Material", "Property"], [
            ["Semiconductor", "Conductivity lies between conductors and insulators, tunable via doping"],
        ]),
    },
    "physics-c2-l59": {
        "data_table": table(["Concept", "Formula"], [
            ["Boltzmann distribution", "P(E) ∝ e^(-E/kT)"],
        ]),
        "formulae": ["P = math.exp(-E / (k * T))"],
    },
    "physics-c2-l60": {
        "data_table": table(["Element", "Purpose"], [
            ["Control group", "Isolates the effect of the variable under investigation"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Newton's Law", "Statement"], [
    ["1st Law (Inertia)", "An object stays at rest or in motion unless acted on by a force"],
    ["2nd Law", "F = m x a (Force = mass x acceleration)"],
    ["3rd Law", "For every action there is an equal and opposite reaction"],
])
_l3_source_formulae = ["F = m x a"]

# l61-l64 "Foundations 2" lessons revisit l7, l12, l17, and l46.
FOUNDATIONS_2_MAP = {61: 7, 62: 12, 63: 17, 64: 46}
for worked_n, base_n in FOUNDATIONS_2_MAP.items():
    base_key = f"physics-c2-l{base_n}"
    fields = {"data_table": CHARTS[base_key]["data_table"]}
    if "formulae" in CHARTS[base_key]:
        fields["formulae"] = CHARTS[base_key]["formulae"]
    CHARTS[f"physics-c2-l{worked_n}"] = fields

# l65-l70 "Worked Analysis" lessons reuse the data_table/formulae of l1-l6.
WORKED_ANALYSIS_MAP = {65: 1, 66: 2, 67: 3, 68: 4, 69: 5, 70: 6}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"physics-c2-l{base_n}"
    if base_key in CHARTS:
        fields = {"data_table": CHARTS[base_key]["data_table"]}
        if "formulae" in CHARTS[base_key]:
            fields["formulae"] = CHARTS[base_key]["formulae"]
        CHARTS[f"physics-c2-l{worked_n}"] = fields
    elif base_n == 3:
        CHARTS[f"physics-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
            "formulae": _l3_source_formulae,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Physics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Physics lessons (completing 70/70).")


if __name__ == "__main__":
    main()
