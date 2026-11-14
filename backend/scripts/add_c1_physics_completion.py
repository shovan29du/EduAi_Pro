#!/usr/bin/env python3
"""Depth pass, C1 Physics: fill in real, hand-checked data_table and
formulae content for the 69 C1 Physics lessons not covered by the
earlier breadth-first batch. Brings C1 Physics to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_physics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "physics-c1-l1": {
        "data_table": table(["Concept", "Meaning"], [
            ["Classical mechanics", "The study of motion and forces on macroscopic objects"],
        ]),
    },
    "physics-c1-l2": {
        "data_table": table(["Concept", "Meaning"], [
            ["Wave", "A disturbance that transfers energy without transferring matter"],
        ]),
    },
    "physics-c1-l4": {
        "data_table": table(["Quantity", "Formula"], [
            ["Work", "W = F × d"], ["Kinetic energy", "KE = 1/2 m v^2"],
        ]),
        "formulae": ["W = F * d", "KE = 0.5 * m * v**2"],
    },
    "physics-c1-l5": {
        "data_table": table(["Linear", "Rotational Analog"], [
            ["Velocity (v)", "Angular velocity (ω)"], ["Force (F)", "Torque (τ)"],
        ]),
    },
    "physics-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Oscillation", "Repeated back-and-forth motion around an equilibrium point"],
        ]),
    },
    "physics-c1-l7": {
        "data_table": table(["Law", "Statement"], [
            ["First law of thermodynamics", "Energy cannot be created or destroyed, only transformed"],
        ]),
    },
    "physics-c1-l8": {
        "data_table": table(["Principle", "Statement"], [
            ["Pascal's principle", "Pressure applied to a confined fluid is transmitted equally in all directions"],
        ]),
    },
    "physics-c1-l9": {
        "data_table": table(["Quantity", "Formula"], [
            ["Coulomb's law", "F = k q1 q2 / r^2"],
        ]),
        "formulae": ["F = k * q1 * q2 / r**2"],
    },
    "physics-c1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Optics", "The study of the behavior and properties of light"],
        ]),
    },
    "physics-c1-l11": {
        "data_table": table(["Postulate", "Statement"], [
            ["Constancy of light speed", "The speed of light is the same for all observers, regardless of motion"],
        ]),
    },
    "physics-c1-l12": {
        "data_table": table(["Concept", "Meaning"], [
            ["Quantization", "Energy exists in discrete packets, or quanta, rather than a continuum"],
        ]),
    },
    "physics-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Nucleus", "The dense, positively charged core of an atom containing protons and neutrons"],
        ]),
    },
    "physics-c1-l14": {
        "data_table": table(["Particle", "Category"], [
            ["Quark", "Fundamental particle, building block of protons and neutrons"], ["Electron", "Fundamental lepton particle"],
        ]),
    },
    "physics-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Astrophysics", "Applies physics to understand stars, galaxies, and the universe"],
        ]),
    },
    "physics-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Condensed matter physics", "Studies the physical properties of solids and liquids"],
        ]),
    },
    "physics-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Statistical mechanics", "Uses probability to explain the behavior of large systems of particles"],
        ]),
    },
    "physics-c1-l18": {
        "data_table": table(["Method", "Use"], [
            ["Numerical simulation", "Models physical systems too complex to solve analytically"],
        ]),
    },
    "physics-c1-l19": {
        "data_table": table(["Step", "Purpose"], [
            ["Controlling variables", "Isolates the effect of the variable being tested"],
        ]),
    },
    "physics-c1-l20": {
        "data_table": table(["Phenomenon", "Explanation"], [
            ["Rainbow", "Light refracting and reflecting inside water droplets"],
        ]),
    },
    "physics-c1-l21": {
        "data_table": table(["Quantity", "SI Unit"], [
            ["Length", "Meter (m)"], ["Mass", "Kilogram (kg)"], ["Time", "Second (s)"],
        ]),
    },
    "physics-c1-l22": {
        "data_table": table(["Type", "Example"], [
            ["Scalar", "Speed, mass — magnitude only"], ["Vector", "Velocity, force — magnitude and direction"],
        ]),
    },
    "physics-c1-l23": {
        "data_table": table(["Quantity", "Formula"], [
            ["Average velocity", "v = Δx / Δt"], ["Acceleration", "a = Δv / Δt"],
        ]),
        "formulae": ["v = delta_x / delta_t", "a = delta_v / delta_t"],
    },
    "physics-c1-l24": {
        "data_table": table(["Component", "Behavior"], [
            ["Horizontal", "Constant velocity (no air resistance)"], ["Vertical", "Constant acceleration due to gravity"],
        ]),
    },
    "physics-c1-l25": {
        "data_table": table(["Law", "Statement"], [
            ["Newton's second law", "F = m a"],
        ]),
        "formulae": ["F = m * a"],
    },
    "physics-c1-l26": {
        "data_table": table(["Type", "Feature"], [
            ["Static friction", "Prevents an object at rest from starting to move"], ["Kinetic friction", "Opposes motion of a moving object"],
        ]),
    },
    "physics-c1-l27": {
        "data_table": table(["Quantity", "Formula"], [
            ["Centripetal force", "F = m v^2 / r"],
        ]),
        "formulae": ["F = m * v**2 / r"],
    },
    "physics-c1-l28": {
        "data_table": table(["Quantity", "Formula"], [
            ["Newton's law of gravitation", "F = G m1 m2 / r^2"],
        ]),
        "formulae": ["F = G * m1 * m2 / r**2"],
    },
    "physics-c1-l29": {
        "data_table": table(["Quantity", "Formula"], [
            ["Momentum", "p = m v"], ["Impulse", "J = F Δt"],
        ]),
        "formulae": ["p = m * v", "J = F * delta_t"],
    },
    "physics-c1-l30": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of momentum", "Total momentum before a collision equals total momentum after"],
        ]),
    },
    "physics-c1-l31": {
        "data_table": table(["Theorem", "Statement"], [
            ["Work-energy theorem", "The net work done on an object equals its change in kinetic energy"],
        ]),
    },
    "physics-c1-l32": {
        "data_table": table(["Quantity", "Formula"], [
            ["Gravitational potential energy", "PE = m g h"],
        ]),
        "formulae": ["PE = m * g * h"],
    },
    "physics-c1-l33": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of energy", "Energy in an isolated system remains constant, only changing form"],
        ]),
    },
    "physics-c1-l34": {
        "data_table": table(["Quantity", "Formula"], [
            ["Power", "P = W / t"],
        ]),
        "formulae": ["P = W / t"],
    },
    "physics-c1-l35": {
        "data_table": table(["Feature", "Detail"], [
            ["Simple harmonic motion", "Restoring force is proportional to displacement from equilibrium"],
        ]),
    },
    "physics-c1-l36": {
        "data_table": table(["Quantity", "Formula"], [
            ["Wave speed", "v = f λ"],
        ]),
        "formulae": ["v = f * wavelength"],
    },
    "physics-c1-l37": {
        "data_table": table(["Property", "Detail"], [
            ["Sound wave", "A longitudinal mechanical wave requiring a medium to travel"],
        ]),
    },
    "physics-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Heat", "Energy transferred between objects due to a temperature difference"],
        ]),
    },
    "physics-c1-l39": {
        "data_table": table(["Mechanism", "Feature"], [
            ["Conduction", "Heat transfer through direct contact"], ["Convection", "Heat transfer through fluid movement"], ["Radiation", "Heat transfer via electromagnetic waves"],
        ]),
    },
    "physics-c1-l40": {
        "data_table": table(["Quantity", "Formula"], [
            ["Ideal gas law", "PV = nRT"],
        ]),
        "formulae": ["P * V = n * R * T"],
    },
    "physics-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Electric charge", "A fundamental property of matter that experiences a force in an electric field"],
        ]),
    },
    "physics-c1-l42": {
        "data_table": table(["Quantity", "Formula"], [
            ["Coulomb's law", "F = k q1 q2 / r^2"],
        ]),
        "formulae": ["F = k * q1 * q2 / r**2"],
    },
    "physics-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Current", "The rate of flow of electric charge"], ["Voltage", "The electric potential difference driving current"],
        ]),
    },
    "physics-c1-l44": {
        "data_table": table(["Quantity", "Formula"], [
            ["Ohm's law", "V = I R"],
        ]),
        "formulae": ["V = I * R"],
    },
    "physics-c1-l45": {
        "data_table": table(["Circuit Type", "Feature"], [
            ["Series", "Same current through all components"], ["Parallel", "Same voltage across all branches"],
        ]),
    },
    "physics-c1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Magnetic field", "A region where magnetic forces act on moving charges or magnetic materials"],
        ]),
    },
    "physics-c1-l47": {
        "data_table": table(["Law", "Statement"], [
            ["Faraday's law", "A changing magnetic field induces an electromotive force"],
        ]),
    },
    "physics-c1-l48": {
        "data_table": table(["Region", "Wavelength Range"], [
            ["Visible light", "About 400-700 nanometers"], ["X-rays", "About 0.01-10 nanometers"],
        ]),
    },
    "physics-c1-l49": {
        "data_table": table(["Law", "Statement"], [
            ["Snell's law", "n1 sin(θ1) = n2 sin(θ2)"],
        ]),
        "formulae": ["n1 * sin(theta1) = n2 * sin(theta2)"],
    },
    "physics-c1-l50": {
        "data_table": table(["Type", "Effect"], [
            ["Convex lens", "Converges light rays to a focal point"], ["Concave mirror", "Reflects light to converge at a focal point"],
        ]),
    },
    "physics-c1-l51": {
        "data_table": table(["Model", "Feature"], [
            ["Bohr model", "Electrons orbit the nucleus in fixed energy levels"],
        ]),
    },
    "physics-c1-l52": {
        "data_table": table(["Type", "Feature"], [
            ["Alpha decay", "Emits a helium nucleus"], ["Beta decay", "Emits an electron or positron"],
        ]),
    },
    "physics-c1-l53": {
        "data_table": table(["Process", "Feature"], [
            ["Fission", "Splitting a heavy nucleus, releasing energy"], ["Fusion", "Combining light nuclei, releasing energy"],
        ]),
    },
    "physics-c1-l54": {
        "data_table": table(["Concept", "Meaning"], [
            ["Photoelectric effect", "Light striking a material ejects electrons, demonstrating light's particle nature"],
        ]),
    },
    "physics-c1-l55": {
        "data_table": table(["Concept", "Meaning"], [
            ["Wave-particle duality", "Light and matter exhibit both wave-like and particle-like properties"],
        ]),
    },
    "physics-c1-l56": {
        "data_table": table(["Body", "Feature"], [
            ["Sun", "The star at the center of the solar system"], ["Jupiter", "The largest planet in the solar system"],
        ]),
    },
    "physics-c1-l57": {
        "data_table": table(["Stage", "Detail"], [
            ["Main sequence", "A star fusing hydrogen into helium in its core"], ["Red giant", "A later stage of stellar expansion after core hydrogen depletes"],
        ]),
    },
    "physics-c1-l58": {
        "data_table": table(["Structure", "Scale"], [
            ["Galaxy", "Billions of stars bound by gravity"], ["Galaxy cluster", "Groups of galaxies bound together"],
        ]),
    },
    "physics-c1-l59": {
        "data_table": table(["Error Type", "Cause"], [
            ["Systematic error", "A consistent bias from equipment or method"], ["Random error", "Unpredictable variation between measurements"],
        ]),
    },
    "physics-c1-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Drawing a diagram", "Clarifies the physical setup before applying equations"],
        ]),
    },
    "physics-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Applying Newton's laws", "Calculating the acceleration of a block on an incline"],
        ]),
        "formulae": ["F_net = m * a"],
    },
    "physics-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a circuit", "Calculating current using Ohm's law"],
        ]),
        "formulae": ["I = V / R"],
    },
    "physics-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Solving a kinematics problem", "Finding final velocity given initial velocity and acceleration"],
        ]),
        "formulae": ["v_f = v_i + a * t"],
    },
    "physics-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Calculating work done", "Finding the work required to lift an object a given height"],
        ]),
        "formulae": ["W = m * g * h"],
    },
    "physics-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Calculating torque", "Finding the torque needed to rotate a lever arm"],
        ]),
        "formulae": ["torque = F * r * sin(theta)"],
    },
    "physics-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Finding the period of a pendulum", "Applying the simple pendulum period formula"],
        ]),
        "formulae": ["T = 2 * pi * sqrt(L / g)"],
    },
    "physics-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Applying the first law", "Calculating heat added given work and internal energy change"],
        ]),
        "formulae": ["Q = delta_U + W"],
    },
    "physics-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Applying Bernoulli's principle", "Comparing fluid speed and pressure at two points in a pipe"],
        ]),
    },
    "physics-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Calculating electric field strength", "Finding the field due to a point charge at a given distance"],
        ]),
        "formulae": ["E = k * q / r**2"],
    },
    "physics-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Applying the lens equation", "Finding image distance given object distance and focal length"],
        ]),
        "formulae": ["1/f = 1/d_o + 1/d_i"],
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Physics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Physics lessons (completing 70/70).")


if __name__ == "__main__":
    main()
