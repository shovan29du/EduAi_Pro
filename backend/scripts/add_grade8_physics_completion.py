#!/usr/bin/env python3
"""Depth pass, Grade 8 Physics: fill in real, hand-checked data_table
content for the 38 Grade 8 Physics lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Physics to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_physics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "phys-g8-l1": {
        "data_table": table(["Law", "Statement"], [
            ["Newton's First Law", "An object stays at rest or in motion unless acted on by a force"],
            ["Newton's Second Law", "Force equals mass times acceleration (F = ma)"],
            ["Newton's Third Law", "For every action, there is an equal and opposite reaction"],
        ]),
    },
    "phys-g8-l2": {
        "data_table": table(["Term", "Formula"], [
            ["Work", "Force x distance"], ["Energy", "The capacity to do work"],
        ]),
    },
    "phys-g8-l3": {
        "data_table": table(["Wave Type", "Example"], [
            ["Transverse wave", "Light wave"], ["Longitudinal wave", "Sound wave"],
        ]),
    },
    "physics-g8-l5": {
        "data_table": table(["Term", "Formula"], [
            ["Acceleration", "Change in velocity / time"],
        ]),
    },
    "physics-g8-l6": {
        "data_table": table(["Graph", "Slope Represents"], [
            ["Distance-time graph", "Speed"], ["Speed-time graph", "Acceleration"],
        ]),
    },
    "physics-g8-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Gravity", "Force that pulls objects toward Earth's center"], ["Weight", "The force of gravity on an object's mass"],
        ]),
    },
    "physics-g8-l8": {
        "data_table": table(["Force", "Effect"], [
            ["Friction", "Resists motion between surfaces"],
        ]),
    },
    "physics-g8-l9": {
        "data_table": table(["Term", "Formula"], [
            ["Momentum", "Mass x velocity"],
        ]),
    },
    "physics-g8-l10": {
        "data_table": table(["Term", "Formula"], [
            ["Pressure", "Force / area"],
        ]),
    },
    "physics-g8-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Water pressure", "Increases with depth"],
        ]),
    },
    "physics-g8-l12": {
        "data_table": table(["Term", "Formula"], [
            ["Density", "Mass / volume"],
        ]),
    },
    "physics-g8-l13": {
        "data_table": table(["Simple Machine", "Example"], [
            ["Lever", "See-saw"], ["Pulley", "Flagpole"],
        ]),
    },
    "physics-g8-l14": {
        "data_table": table(["Simple Machine", "Example"], [
            ["Inclined plane", "Ramp"], ["Wheel and axle", "Bicycle wheel"],
        ]),
    },
    "physics-g8-l15": {
        "data_table": table(["Term", "Formula"], [
            ["Power", "Work / time"],
        ]),
    },
    "physics-g8-l17": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of energy", "Energy cannot be created or destroyed, only transformed"],
        ]),
    },
    "physics-g8-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Heat", "Energy transferred due to a temperature difference"], ["Temperature", "A measure of average kinetic energy"],
        ]),
    },
    "physics-g8-l19": {
        "data_table": table(["Heat Transfer Type", "Example"], [
            ["Conduction", "Touching a hot pan"], ["Convection", "Warm air rising"], ["Radiation", "Sunlight warming skin"],
        ]),
    },
    "physics-g8-l20": {
        "data_table": table(["State", "Example"], [
            ["Solid", "Ice"], ["Liquid", "Water"], ["Gas", "Steam"],
        ]),
    },
    "physics-g8-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Sound", "Created by vibrations, travels as waves"],
        ]),
    },
    "physics-g8-l22": {
        "data_table": table(["Property", "Meaning"], [
            ["Pitch", "How high or low a sound is, based on frequency"], ["Volume", "How loud a sound is, based on amplitude"],
        ]),
    },
    "physics-g8-l23": {
        "data_table": table(["Wave Type", "Approximate Wavelength"], [
            ["Radio waves", "Longest"], ["Gamma rays", "Shortest"],
        ]),
    },
    "physics-g8-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Reflection", "Light bouncing off a surface"],
        ]),
    },
    "physics-g8-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Refraction", "Light bending as it passes through a medium"],
        ]),
    },
    "physics-g8-l26": {
        "data_table": table(["Lens Type", "Effect"], [
            ["Convex lens", "Converges light, used to magnify"], ["Concave lens", "Diverges light"],
        ]),
    },
    "physics-g8-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["Static electricity", "Buildup of electric charge on a surface"],
        ]),
    },
    "physics-g8-l28": {
        "data_table": table(["Circuit Type", "Description"], [
            ["Closed circuit", "A complete loop; current flows"], ["Open circuit", "A broken loop; current stops"],
        ]),
    },
    "physics-g8-l29": {
        "data_table": table(["Circuit Type", "Property"], [
            ["Series", "Same current flows through all components"], ["Parallel", "Voltage same across each branch"],
        ]),
    },
    "physics-g8-l30": {
        "data_table": table(["Term", "Formula/Unit"], [
            ["Current", "Measured in amperes (A)"], ["Voltage", "Measured in volts (V)"],
        ]),
    },
    "physics-g8-l31": {
        "data_table": table(["Law", "Statement"], [
            ["Ohm's Law", "Voltage = Current x Resistance (V = IR)"],
        ]),
    },
    "physics-g8-l32": {
        "data_table": table(["Magnet Fact", "Detail"], [
            ["Poles", "North and South"], ["Like poles", "Repel each other"],
        ]),
    },
    "physics-g8-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Electromagnet", "A magnet created by an electric current"],
        ]),
    },
    "physics-g8-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Electromagnetic induction", "Generating electric current from a changing magnetic field"],
        ]),
    },
    "physics-g8-l35": {
        "data_table": table(["Resource Type", "Example"], [
            ["Renewable", "Solar, wind"], ["Nonrenewable", "Coal, oil"],
        ]),
    },
    "physics-g8-l36": {
        "data_table": table(["Simple Machine", "Everyday Example"], [
            ["Lever", "A see-saw or a crowbar"], ["Wheel and axle", "A doorknob"],
        ]),
    },
    "physics-g8-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Gravity in space", "The force keeping planets in orbit around the sun"],
        ]),
    },
    "physics-g8-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Projectile motion", "The curved path of an object launched into the air"],
        ]),
    },
    "physics-g8-l39": {
        "data_table": table(["Quantity", "Standard Unit"], [
            ["Mass", "Kilogram (kg)"], ["Length", "Meter (m)"], ["Time", "Second (s)"],
        ]),
    },
    "physics-g8-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Scientific model", "A simplified representation used to explain and predict phenomena"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Physics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Physics lessons (completing 40/40).")


if __name__ == "__main__":
    main()
