#!/usr/bin/env python3
"""Depth pass, Grade 9 Physics: fill in real, hand-checked data_table
content for the 48 Grade 9 Physics lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Physics to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_physics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "phys-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Circuit", "A closed loop through which electric current flows"],
        ]),
        "formulae": ["V = IR (Ohm's Law)"],
    },
    "phys-g9-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Electromagnet", "A magnet created by an electric current"],
        ]),
    },
    "phys-g9-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Radioactivity", "The spontaneous emission of particles or energy from an unstable atomic nucleus"],
        ]),
    },
    "physics-g9-l4": {
        "data_table": table(["Quantity", "SI Unit"], [
            ["Mass", "Kilogram (kg)"], ["Length", "Meter (m)"], ["Time", "Second (s)"],
        ]),
    },
    "physics-g9-l5": {
        "data_table": table(["Type", "Example"], [
            ["Scalar", "Speed, mass (magnitude only)"], ["Vector", "Velocity, force (magnitude and direction)"],
        ]),
    },
    "physics-g9-l6": {
        "data_table": table(["Quantity", "Formula"], [
            ["Speed", "distance / time"], ["Velocity", "displacement / time"],
        ]),
        "formulae": ["speed = distance / time"],
    },
    "physics-g9-l7": {
        "data_table": table(["Quantity", "Formula"], [
            ["Acceleration", "change in velocity / time"],
        ]),
        "formulae": ["a = (v - u) / t"],
    },
    "physics-g9-l8": {
        "data_table": table(["Graph Feature", "Meaning"], [
            ["Slope", "Represents speed"], ["Flat line", "Object is stationary"],
        ]),
    },
    "physics-g9-l9": {
        "data_table": table(["Graph Feature", "Meaning"], [
            ["Slope", "Represents acceleration"], ["Area under curve", "Represents distance traveled"],
        ]),
    },
    "physics-g9-l11": {
        "data_table": table(["Law", "Statement"], [
            ["Newton's Second Law", "Force = mass x acceleration"],
        ]),
        "formulae": ["F = ma"],
    },
    "physics-g9-l12": {
        "data_table": table(["Law", "Statement"], [
            ["Newton's Third Law", "For every action, there is an equal and opposite reaction"],
        ]),
    },
    "physics-g9-l13": {
        "data_table": table(["Quantity", "Unit"], [
            ["Mass", "Kilogram, amount of matter"], ["Weight", "Newton, force of gravity on mass"],
        ]),
        "formulae": ["W = mg"],
    },
    "physics-g9-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Free body diagram", "A diagram showing all forces acting on an object"],
        ]),
    },
    "physics-g9-l15": {
        "data_table": table(["Type", "Effect"], [
            ["Friction", "Opposes relative motion between surfaces"],
        ]),
    },
    "physics-g9-l16": {
        "data_table": table(["Quantity", "Formula"], [
            ["Momentum", "mass x velocity"],
        ]),
        "formulae": ["p = mv"],
    },
    "physics-g9-l17": {
        "data_table": table(["Quantity", "Formula"], [
            ["Work", "force x distance"],
        ]),
        "formulae": ["W = Fd"],
    },
    "physics-g9-l19": {
        "data_table": table(["Quantity", "Formula"], [
            ["Gravitational potential energy", "mass x gravity x height"],
        ]),
        "formulae": ["GPE = mgh"],
    },
    "physics-g9-l20": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of energy", "Energy cannot be created or destroyed, only transformed"],
        ]),
    },
    "physics-g9-l21": {
        "data_table": table(["Quantity", "Formula"], [
            ["Power", "work / time"],
        ]),
        "formulae": ["P = W / t"],
    },
    "physics-g9-l22": {
        "data_table": table(["Machine", "Example"], [
            ["Lever", "Seesaw"], ["Pulley", "Flagpole"], ["Wheel and axle", "Doorknob"],
        ]),
    },
    "physics-g9-l23": {
        "data_table": table(["Lever Class", "Example"], [
            ["First class", "Seesaw, fulcrum between effort and load"],
        ]),
    },
    "physics-g9-l24": {
        "data_table": table(["Pulley Type", "Effect"], [
            ["Fixed pulley", "Changes direction of force"], ["Movable pulley", "Reduces the force needed"],
        ]),
    },
    "physics-g9-l25": {
        "data_table": table(["Term", "Effect"], [
            ["Inclined plane", "Reduces the force needed to raise an object, over a longer distance"],
        ]),
    },
    "physics-g9-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Gravitational field strength on Earth", "About 9.8 m/s^2"],
        ]),
    },
    "physics-g9-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["Projectile motion", "Combination of constant horizontal velocity and vertical acceleration due to gravity"],
        ]),
    },
    "physics-g9-l28": {
        "data_table": table(["Quantity", "Formula"], [
            ["Pressure", "force / area"],
        ]),
        "formulae": ["P = F / A"],
    },
    "physics-g9-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Fluid pressure", "Increases with depth"],
        ]),
    },
    "physics-g9-l30": {
        "data_table": table(["Principle", "Statement"], [
            ["Archimedes' principle", "Upward buoyant force equals the weight of fluid displaced"],
        ]),
    },
    "physics-g9-l31": {
        "data_table": table(["Quantity", "Formula"], [
            ["Density", "mass / volume"],
        ]),
        "formulae": ["density = mass / volume"],
    },
    "physics-g9-l32": {
        "data_table": table(["Principle", "Statement"], [
            ["Pascal's principle", "Pressure applied to an enclosed fluid is transmitted equally in all directions"],
        ]),
    },
    "physics-g9-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Heat", "Energy transferred due to temperature difference"], ["Temperature", "A measure of average kinetic energy of particles"],
        ]),
    },
    "physics-g9-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Thermal expansion", "Most materials expand when heated"],
        ]),
    },
    "physics-g9-l35": {
        "data_table": table(["Method", "Description"], [
            ["Conduction", "Heat transfer through direct contact"], ["Convection", "Heat transfer through fluid movement"], ["Radiation", "Heat transfer through electromagnetic waves"],
        ]),
    },
    "physics-g9-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Specific heat capacity", "Energy needed to raise 1 kg of a substance by 1 degree Celsius"],
        ]),
    },
    "physics-g9-l37": {
        "data_table": table(["Change", "Example"], [
            ["Melting", "Solid to liquid"], ["Boiling", "Liquid to gas"],
        ]),
    },
    "physics-g9-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Latent heat", "Energy absorbed or released during a change of state without a temperature change"],
        ]),
    },
    "physics-g9-l39": {
        "data_table": table(["Wave Type", "Example"], [
            ["Transverse wave", "Light"], ["Longitudinal wave", "Sound"],
        ]),
    },
    "physics-g9-l40": {
        "data_table": table(["Property", "Meaning"], [
            ["Wavelength", "Distance between successive wave crests"], ["Frequency", "Number of waves per second"],
        ]),
        "formulae": ["v = f * lambda"],
    },
    "physics-g9-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Sound", "A longitudinal wave requiring a medium to travel"],
        ]),
    },
    "physics-g9-l42": {
        "data_table": table(["Region", "Example Use"], [
            ["Visible light", "Human sight"], ["X-rays", "Medical imaging"],
        ]),
    },
    "physics-g9-l43": {
        "data_table": table(["Law", "Statement"], [
            ["Law of reflection", "Angle of incidence equals angle of reflection"],
        ]),
    },
    "physics-g9-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Refraction", "The bending of light as it passes between media of different densities"],
        ]),
    },
    "physics-g9-l45": {
        "data_table": table(["Lens Type", "Effect"], [
            ["Convex lens", "Converges light rays"], ["Concave lens", "Diverges light rays"],
        ]),
    },
    "physics-g9-l46": {
        "data_table": table(["Eye Part", "Function"], [
            ["Lens", "Focuses light onto the retina"], ["Retina", "Detects light and sends signals to the brain"],
        ]),
    },
    "physics-g9-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Static electricity", "Buildup of electric charge on an object's surface"],
        ]),
    },
    "physics-g9-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Semiconductor", "A material with conductivity between a conductor and insulator, e.g. silicon"],
        ]),
    },
    "physics-g9-l49": {
        "data_table": table(["Quantity", "Formula"], [
            ["Electrical power", "voltage x current"],
        ]),
        "formulae": ["P = VI"],
    },
    "physics-g9-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Nuclear energy", "Energy released from the nucleus of an atom, via fission or fusion"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Physics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Physics lessons (completing 50/50).")


if __name__ == "__main__":
    main()
