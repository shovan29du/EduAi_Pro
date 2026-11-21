#!/usr/bin/env python3
"""Depth pass, Grade 2 Math: fill in real, hand-checked data_table content
for the 15 Grade 2 Math lessons not covered by the earlier breadth-first
batch. Brings Grade 2 Math to full 20/20 coverage.

Every fact is real arithmetic or standard measurement units -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


def graph(title, points, x_axis, y_axis):
    return {"title": title, "points": points, "x_axis": x_axis, "y_axis": y_axis}


CHARTS: dict[str, dict] = {
    "math-g2-l1": {
        "data_table": table(["Number", "Tens", "Ones"], [
            ["34", "3", "4"], ["58", "5", "8"], ["70", "7", "0"],
        ]),
    },
    "math-g2-l2": {
        "data_table": table(["Fact", "Answer"], [
            ["45 + 32", "77"], ["58 + 26", "84"], ["19 + 45", "64"],
        ]),
    },
    "math-g2-l3": {
        "data_table": table(["Fact", "Answer"], [
            ["87 - 32", "55"], ["64 - 18", "46"], ["100 - 45", "55"],
        ]),
    },
    "math-g2-l7": {
        "data_table": table(["Skip by", "Sequence"], [
            ["2s", "2, 4, 6, 8, 10"], ["5s", "5, 10, 15, 20, 25"], ["10s", "10, 20, 30, 40, 50"],
        ]),
    },
    "math-g2-l8": {
        "data_table": table(["Fact", "Answer"], [
            ["12 / 3", "4"], ["20 / 4", "5"], ["18 / 2", "9"],
        ]),
    },
    "math-g2-l9": {
        "data_table": table(["Clock Position", "Time"], [
            ["Long hand at 12, short hand at 3", "3:00"],
            ["Long hand at 6, short hand between 3 and 4", "3:30"],
        ]),
    },
    "math-g2-l10": {
        "data_table": table(["Minute Mark (Long Hand)", "Time Shown"], [
            ["At 1", "5 minutes past"], ["At 2", "10 minutes past"], ["At 3", "15 minutes past"],
        ]),
    },
    "math-g2-l11": {
        "data_table": table(["Unit", "Abbreviation"], [
            ["Centimeter", "cm"], ["Inch", "in"],
        ]),
    },
    "math-g2-l12": {
        "data_table": table(["Unit", "Used For"], [
            ["Grams (g)", "Light objects"], ["Kilograms (kg)", "Heavier objects"],
        ]),
    },
    "math-g2-l13": {
        "data_table": table(["Unit", "Used For"], [
            ["Milliliters (mL)", "Small amounts of liquid"], ["Liters (L)", "Larger amounts of liquid"],
        ]),
    },
    "math-g2-l14": {
        "data_table": table(["Shape", "Sides", "Corners"], [
            ["Triangle", "3", "3"], ["Square", "4", "4"], ["Pentagon", "5", "5"], ["Hexagon", "6", "6"],
        ]),
    },
    "math-g2-l15": {
        "data_table": table(["3D Shape", "Faces"], [
            ["Cube", "6"], ["Sphere", "0 (one curved surface)"], ["Cylinder", "2 flat + 1 curved"],
        ]),
    },
    "math-g2-l16": {
        "data_table": table(["Shape", "Lines of Symmetry"], [
            ["Square", "4"], ["Circle", "Infinite"], ["Equilateral Triangle", "3"],
        ]),
    },
    "math-g2-l18": {
        "graph": graph("Favorite Pet Survey (Example Data)", [6, 4, 8], "Pet: Dog, Cat, Fish", "Number of Votes"),
    },
    "math-g2-l20": {
        "data_table": table(["Pattern", "Rule", "Next Number"], [
            ["2, 4, 6, 8", "+2", "10"], ["5, 10, 15, 20", "+5", "25"], ["1, 2, 4, 8", "x2", "16"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 Math lessons (completing 20/20).")


if __name__ == "__main__":
    main()
