#!/usr/bin/env python3
"""Depth pass, Grade 7 Math: fill in real, hand-checked data_table
content for the 34 Grade 7 Math lessons not covered by the earlier
breadth-first batch. Brings Grade 7 Math to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "math-g7-l1": {
        "data_table": table(["Equation", "Solution"], [
            ["2x + 3 = 11", "x = 4"], ["x - 5 > 2", "x > 7"],
        ]),
    },
    "math-g7-l3": {
        "data_table": table(["Event", "Probability"], [
            ["Coin lands heads", "1/2"], ["Rolling a 6 on a die", "1/6"],
        ]),
    },
    "math-g7-l4": {
        "data_table": table(["Number", "Absolute Value"], [
            ["-7", "7"], ["4", "4"],
        ]),
    },
    "math-g7-l5": {
        "data_table": table(["Problem", "Answer"], [
            ["-3 + 5", "2"], ["-2 x -4", "8"],
        ]),
    },
    "math-g7-l6": {
        "data_table": table(["Ratio", "Simplified"], [
            ["8:12", "2:3"], ["10:15", "2:3"],
        ]),
    },
    "math-g7-l7": {
        "data_table": table(["Original", "New", "% Change"], [
            ["$50", "$60", "+20%"], ["$80", "$60", "-25%"],
        ]),
    },
    "math-g7-l9": {
        "data_table": table(["Expression", "Simplified"], [
            ["3x + 2x - 4", "5x - 4"], ["2(x + 3)", "2x + 6"],
        ]),
    },
    "math-g7-l10": {
        "data_table": table(["Equation", "Solution"], [
            ["2x + 3 = 11", "x = 4"],
        ]),
    },
    "math-g7-l11": {
        "data_table": table(["Point", "Coordinates"], [
            ["Origin", "(0, 0)"], ["Example point", "(3, 4)"],
        ]),
    },
    "math-g7-l12": {
        "data_table": table(["Proportion Type", "Example"], [
            ["Direct", "As x doubles, y doubles"], ["Inverse", "As x doubles, y halves"],
        ]),
    },
    "math-g7-l13": {
        "data_table": table(["Expression", "Value"], [
            ["2^3", "8"], ["5^2", "25"],
        ]),
    },
    "math-g7-l14": {
        "data_table": table(["Number", "Scientific Notation"], [
            ["3,400,000", "3.4 x 10^6"], ["0.00056", "5.6 x 10^-4"],
        ]),
    },
    "math-g7-l16": {
        "data_table": table(["Number", "Prime Factors"], [
            ["12", "2, 2, 3"], ["30", "2, 3, 5"],
        ]),
    },
    "math-g7-l17": {
        "data_table": table(["Numbers", "HCF", "LCM"], [
            ["12, 18", "6", "36"],
        ]),
    },
    "math-g7-l18": {
        "data_table": table(["Angle Pair", "Relationship"], [
            ["Complementary", "Sum to 90 degrees"], ["Supplementary", "Sum to 180 degrees"],
        ]),
    },
    "math-g7-l19": {
        "data_table": table(["Triangle Type", "Property"], [
            ["Equilateral", "All 3 sides equal"], ["Right triangle", "One 90-degree angle"],
        ]),
    },
    "math-g7-l20": {
        "data_table": table(["Shape", "Number of Sides"], [
            ["Pentagon", "5"], ["Hexagon", "6"], ["Octagon", "8"],
        ]),
    },
    "math-g7-l22": {
        "data_table": table(["Shape", "Area Formula"], [
            ["Rectangle", "length x width"], ["Triangle", "1/2 x base x height"],
        ]),
    },
    "math-g7-l23": {
        "data_table": table(["Shape", "Surface Area Formula"], [
            ["Cube", "6 x side^2"], ["Cylinder", "2*pi*r^2 + 2*pi*r*h"],
        ]),
    },
    "math-g7-l24": {
        "data_table": table(["Shape", "Volume Formula"], [
            ["Rectangular prism", "length x width x height"], ["Cylinder", "pi*r^2*h"],
        ]),
    },
    "math-g7-l25": {
        "data_table": table(["Shape", "Net Description"], [
            ["Cube", "6 connected squares"], ["Cylinder", "2 circles and 1 rectangle"],
        ]),
    },
    "math-g7-l26": {
        "data_table": table(["Transformation", "Effect"], [
            ["Translation", "Slides a shape without rotating or resizing"],
            ["Reflection", "Flips a shape over a line"],
            ["Rotation", "Turns a shape around a point"],
        ]),
    },
    "math-g7-l27": {
        "data_table": table(["Scale Factor", "Effect"], [
            ["2", "Doubles the size"], ["0.5", "Halves the size"],
        ]),
    },
    "math-g7-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Congruent", "Same shape and size"], ["Similar", "Same shape, different size"],
        ]),
    },
    "math-g7-l29": {
        "data_table": table(["Shape", "Lines of Symmetry"], [
            ["Square", "4"], ["Regular hexagon", "6"],
        ]),
    },
    "math-g7-l30": {
        "data_table": table(["Construction", "Tool"], [
            ["Bisecting an angle", "Compass and straightedge"], ["Perpendicular bisector", "Compass and straightedge"],
        ]),
    },
    "math-g7-l31": {
        "data_table": table(["Data Set", "Mean", "Median"], [
            ["2, 4, 4, 6", "4", "4"],
        ]),
    },
    "math-g7-l32": {
        "data_table": table(["Chart Type", "Best Used For"], [
            ["Bar chart", "Comparing categories"], ["Histogram", "Showing frequency of continuous data"],
        ]),
    },
    "math-g7-l33": {
        "data_table": table(["Category", "Percentage"], [
            ["Category A", "40%"], ["Category B", "35%"], ["Category C", "25%"],
        ]),
    },
    "math-g7-l34": {
        "data_table": table(["Correlation Type", "Meaning"], [
            ["Positive", "Both variables increase together"], ["Negative", "One increases as the other decreases"],
        ]),
    },
    "math-g7-l35": {
        "data_table": table(["Combined Event", "Probability"], [
            ["Two coin flips both heads", "1/4"], ["Two dice both showing 6", "1/36"],
        ]),
    },
    "math-g7-l36": {
        "data_table": table(["Sequence", "Next Term"], [
            ["2, 4, 6, 8", "10"], ["1, 4, 9, 16", "25"],
        ]),
    },
    "math-g7-l37": {
        "data_table": table(["Line Equation", "Gradient (Slope)"], [
            ["y = 2x + 3", "2"], ["y = -x + 5", "-1"],
        ]),
    },
    "math-g7-l39": {
        "data_table": table(["Budget Category", "Example Allocation"], [
            ["Needs", "50% of income"], ["Wants", "30% of income"], ["Savings", "20% of income"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Math lessons (completing 40/40).")


if __name__ == "__main__":
    main()
