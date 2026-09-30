#!/usr/bin/env python3
"""Depth pass, Grade 3 Math: fill in real, hand-checked data_table/graph
content for the 15 Grade 3 Math lessons not covered by the earlier
breadth-first batch. Brings Grade 3 Math to full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "math-g3-l2": {
        "data_table": table(["Division", "Answer"], [
            ["12 / 3", "4"], ["20 / 4", "5"], ["36 / 6", "6"], ["45 / 9", "5"],
        ]),
    },
    "math-g3-l3": {
        "data_table": table(["Fraction", "Equivalent Fraction"], [
            ["1/2", "2/4"], ["1/3", "2/6"], ["2/3", "4/6"], ["3/4", "6/8"],
        ]),
    },
    "math-g3-l6": {
        "data_table": table(["Place", "Value in 8,342"], [
            ["Thousands", "8"], ["Hundreds", "3"], ["Tens", "4"], ["Ones", "2"],
        ]),
    },
    "math-g3-l7": {
        "data_table": table(["Number", "Rounded to Nearest 10"], [
            ["24", "20"], ["27", "30"], ["152", "150"], ["156", "160"],
        ]),
    },
    "math-g3-l8": {
        "data_table": table(["Problem", "Answer"], [
            ["47 + 38", "85"], ["156 + 267", "423"], ["29 + 15", "44"],
        ]),
    },
    "math-g3-l9": {
        "data_table": table(["Problem", "Answer"], [
            ["82 - 47", "35"], ["300 - 156", "144"], ["61 - 29", "32"],
        ]),
    },
    "math-g3-l10": {
        "data_table": table(["Clock Reading", "Meaning"], [
            ["3:15", "Quarter past 3"], ["6:30", "Half past 6"], ["9:45", "Quarter to 10"],
        ]),
    },
    "math-g3-l11": {
        "data_table": table(["Start Time", "End Time", "Elapsed Time"], [
            ["2:00", "3:30", "1 hour 30 minutes"], ["9:15", "10:00", "45 minutes"],
        ]),
    },
    "math-g3-l12": {
        "data_table": table(["Item Cost", "Amount Paid", "Change"], [
            ["$3.50", "$5.00", "$1.50"], ["$7.25", "$10.00", "$2.75"],
        ]),
    },
    "math-g3-l13": {
        "data_table": table(["Unit", "Used to Measure"], [
            ["Centimeter (cm)", "Small lengths, like a pencil"],
            ["Meter (m)", "Room or hallway length"], ["Kilometer (km)", "Distance between cities"],
        ]),
    },
    "math-g3-l14": {
        "data_table": table(["Unit", "Used to Measure"], [
            ["Gram (g)", "Weight of small objects, like a coin"],
            ["Kilogram (kg)", "Weight of heavier objects, like a bag of rice"],
        ]),
    },
    "math-g3-l15": {
        "data_table": table(["Unit", "Used to Measure"], [
            ["Milliliter (mL)", "Small amounts, like a spoonful of medicine"],
            ["Liter (L)", "Larger amounts, like a bottle of water"],
        ]),
    },
    "math-g3-l17": {
        "data_table": table(["Shape", "Number of Sides"], [
            ["Triangle", "3"], ["Square", "4"], ["Pentagon", "5"], ["Hexagon", "6"],
        ]),
    },
    "math-g3-l18": {
        "data_table": table(["Solid Shape", "Number of Faces"], [
            ["Cube", "6"], ["Sphere", "0"], ["Cylinder", "3"], ["Cone", "2"],
        ]),
    },
    "math-g3-l19": {
        "data_table": table(["Shape", "Lines of Symmetry"], [
            ["Square", "4"], ["Circle", "Infinite"], ["Equilateral triangle", "3"], ["Rectangle", "2"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Math lessons (completing 20/20).")


if __name__ == "__main__":
    main()
