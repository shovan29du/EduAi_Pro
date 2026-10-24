#!/usr/bin/env python3
"""Depth pass, Grade 10 Physics: fill in real, hand-checked data_table
content for the Grade 10 Physics lessons not covered by the earlier
breadth-first batch. Brings Grade 10 Physics to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_physics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "phys-g10-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Thermal physics", "Studies heat and temperature and their effects on matter"],
        ]),
    },
    "phys-g10-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Space physics", "Studies the physical processes occurring in space"],
        ]),
    },
    "physics-g10-l3": {
        "data_table": table(["Quantity", "Formula"], [
            ["Speed", "distance / time"], ["Acceleration", "change in velocity / time"],
        ]),
        "formulae": ["speed = distance / time"],
    },
    "physics-g10-l4": {
        "data_table": table(["Law", "Statement"], [
            ["Newton's First Law", "An object stays at rest or in motion unless acted on by a net force"],
        ]),
    },
    "physics-g10-l5": {
        "data_table": table(["Law", "Statement"], [
            ["Newton's Second Law", "Force = mass x acceleration"],
        ]),
        "formulae": ["F = ma"],
    },
    "physics-g10-l6": {
        "data_table": table(["Law", "Statement"], [
            ["Newton's Third Law", "For every action, there is an equal and opposite reaction"],
        ]),
    },
    "physics-g10-l7": {
        "data_table": table(["Quantity", "Unit"], [
            ["Mass", "Kilogram, amount of matter"], ["Weight", "Newton, force of gravity on mass"],
        ]),
        "formulae": ["W = mg"],
    },
    "physics-g10-l8": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of momentum", "Total momentum before a collision equals total momentum after, in a closed system"],
        ]),
        "formulae": ["p = mv"],
    },
    "physics-g10-l10": {
        "data_table": table(["Quantity", "Formula"], [
            ["Kinetic energy", "KE = 1/2 mv^2"], ["Gravitational potential energy", "GPE = mgh"],
        ]),
        "formulae": ["KE = 0.5 * m * v^2"],
    },
    "physics-g10-l11": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of energy", "Energy cannot be created or destroyed, only transformed"],
        ]),
    },
    "physics-g10-l12": {
        "data_table": table(["Machine", "Example"], [
            ["Lever", "Seesaw"], ["Pulley", "Flagpole"],
        ]),
    },
    "physics-g10-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Centripetal force", "The inward force keeping an object in circular motion"],
        ]),
    },
    "physics-g10-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Projectile motion", "Combination of constant horizontal velocity and vertical acceleration due to gravity"],
        ]),
    },
    "physics-g10-l15": {
        "data_table": table(["Type", "Effect"], [
            ["Friction", "Opposes relative motion between surfaces"],
        ]),
    },
    "physics-g10-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Fluid pressure", "Increases with depth"],
        ]),
    },
    "physics-g10-l18": {
        "data_table": table(["Quantity", "Formula"], [
            ["Density", "mass / volume"],
        ]),
        "formulae": ["density = mass / volume"],
    },
    "physics-g10-l19": {
        "data_table": table(["Wave Type", "Example"], [
            ["Transverse wave", "Light"], ["Longitudinal wave", "Sound"],
        ]),
    },
    "physics-g10-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Sound", "A longitudinal wave requiring a medium to travel"],
        ]),
    },
    "physics-g10-l21": {
        "data_table": table(["Region", "Example Use"], [
            ["Visible light", "Human sight"], ["X-rays", "Medical imaging"],
        ]),
    },
    "physics-g10-l22": {
        "data_table": table(["Law", "Statement"], [
            ["Law of reflection", "Angle of incidence equals angle of reflection"], ["Refraction", "Bending of light between media"],
        ]),
    },
    "physics-g10-l23": {
        "data_table": table(["Lens Type", "Effect"], [
            ["Convex lens", "Converges light rays"], ["Concave lens", "Diverges light rays"],
        ]),
    },
    "physics-g10-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Visible spectrum", "Light with wavelengths our eyes perceive as colors, roughly 400-700nm"],
        ]),
    },
    "physics-g10-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Static electricity", "Buildup of electric charge on an object's surface"],
        ]),
    },
    "physics-g10-l26": {
        "data_table": table(["Circuit Type", "Feature"], [
            ["Series circuit", "One path for current"], ["Parallel circuit", "Multiple paths for current"],
        ]),
    },
    "physics-g10-l27": {
        "data_table": table(["Law", "Formula"], [
            ["Ohm's Law", "V = IR"],
        ]),
        "formulae": ["V = IR"],
    },
    "physics-g10-l28": {
        "data_table": table(["Quantity", "Formula"], [
            ["Electrical power", "voltage x current"],
        ]),
        "formulae": ["P = VI"],
    },
    "physics-g10-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Magnetic field", "The region around a magnet where magnetic force acts"],
        ]),
    },
    "physics-g10-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Electromagnetic induction", "Generating current by moving a conductor through a magnetic field"],
        ]),
    },
    "physics-g10-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Radioactivity", "Spontaneous emission of particles or energy from an unstable nucleus"],
        ]),
    },
    "physics-g10-l32": {
        "data_table": table(["Type", "Description"], [
            ["Alpha decay", "Emits a helium nucleus"], ["Beta decay", "Emits an electron"],
        ]),
    },
    "physics-g10-l33": {
        "data_table": table(["Process", "Description"], [
            ["Fission", "Splitting a heavy nucleus, releases energy"], ["Fusion", "Combining light nuclei, releases energy"],
        ]),
    },
    "physics-g10-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Semiconductor", "A material with conductivity between a conductor and insulator, e.g. silicon"],
        ]),
    },
    "physics-g10-l35": {
        "data_table": table(["Source", "Example"], [
            ["Solar", "Renewable energy from sunlight"], ["Wind", "Renewable energy from air movement"],
        ]),
    },
    "physics-g10-l36": {
        "data_table": table(["Source", "Example"], [
            ["Coal", "Non-renewable fossil fuel"], ["Natural gas", "Non-renewable fossil fuel"],
        ]),
    },
    "physics-g10-l37": {
        "data_table": table(["Method", "Description"], [
            ["Conduction", "Heat transfer through direct contact"], ["Convection", "Heat transfer through fluid movement"], ["Radiation", "Heat transfer through electromagnetic waves"],
        ]),
    },
    "physics-g10-l38": {
        "data_table": table(["Change", "Example"], [
            ["Melting", "Solid to liquid"], ["Boiling", "Liquid to gas"],
        ]),
    },
    "physics-g10-l39": {
        "data_table": table(["Quantity", "SI Unit"], [
            ["Mass", "Kilogram (kg)"], ["Length", "Meter (m)"], ["Time", "Second (s)"],
        ]),
    },
    "physics-g10-l40": {
        "data_table": table(["Type", "Example"], [
            ["Scalar", "Speed, mass"], ["Vector", "Velocity, force"],
        ]),
    },
    "physics-g10-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Free body diagram", "A diagram showing all forces acting on an object"],
        ]),
    },
    "physics-g10-l42": {
        "data_table": table(["Quantity", "Formula"], [
            ["Torque", "force x distance from pivot"],
        ]),
        "formulae": ["torque = F * r"],
    },
    "physics-g10-l43": {
        "data_table": table(["Law", "Formula"], [
            ["Hooke's Law", "F = kx"],
        ]),
        "formulae": ["F = kx"],
    },
    "physics-g10-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Doppler effect", "Change in observed frequency due to relative motion of source and observer"],
        ]),
    },
    "physics-g10-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Quantum physics", "Describes physics at the atomic and subatomic scale"],
        ]),
    },
    "physics-g10-l46": {
        "data_table": table(["Scientist", "Discovery"], [
            ["Isaac Newton", "Laws of motion and universal gravitation"], ["Albert Einstein", "Theory of relativity"],
        ]),
    },
    "physics-g10-l47": {
        "data_table": table(["Machine", "Physics Principle"], [
            ["Bicycle", "Gears provide mechanical advantage"],
        ]),
    },
    "physics-g10-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Orbital motion", "A satellite falls toward Earth while moving forward fast enough to keep missing it"],
        ]),
    },
    "physics-g10-l49": {
        "data_table": table(["Planet", "Order from Sun"], [
            ["Mercury", "1st"], ["Earth", "3rd"],
        ]),
    },
    "physics-g10-l50": {
        "data_table": table(["Skill", "Purpose"], [
            ["Recording uncertainty", "Reflects the precision of a physics measurement"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Physics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Physics lessons (completing 50/50).")


if __name__ == "__main__":
    main()
