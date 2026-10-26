#!/usr/bin/env python3
"""Depth pass, Grade 6 Math: fill in real, hand-checked data_table
content for the 24 Grade 6 Math lessons not covered by the earlier
breadth-first batch. Brings Grade 6 Math to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "math-g6-l1": {
        "data_table": table(["Expression", "Simplified"], [
            ["3x + 2x", "5x"], ["x + 7 = 10", "x = 3"],
        ]),
    },
    "math-g6-l2": {
        "data_table": table(["Number", "Position on Number Line"], [
            ["-5", "5 units left of 0"], ["3", "3 units right of 0"],
        ]),
    },
    "math-g6-l3": {
        "data_table": table(["Point", "Coordinates"], [
            ["Origin", "(0, 0)"], ["Example point", "(3, 4)"],
        ]),
    },
    "math-g6-l4": {
        "data_table": table(["Fraction", "Mixed Number"], [
            ["7/2", "3 1/2"], ["11/4", "2 3/4"],
        ]),
    },
    "math-g6-l5": {
        "data_table": table(["Problem", "Answer"], [
            ["1/4 + 1/2", "3/4"], ["5/6 - 1/3", "1/2"],
        ]),
    },
    "math-g6-l6": {
        "data_table": table(["Problem", "Answer"], [
            ["1/2 x 2/3", "1/3"], ["3/4 / 1/2", "3/2"],
        ]),
    },
    "math-g6-l7": {
        "data_table": table(["Place", "Value in 3.456"], [
            ["Tenths", "4"], ["Hundredths", "5"], ["Thousandths", "6"],
        ]),
    },
    "math-g6-l8": {
        "data_table": table(["Problem", "Answer"], [
            ["2.5 + 1.75", "4.25"], ["3.6 x 2", "7.2"],
        ]),
    },
    "math-g6-l10": {
        "data_table": table(["Rate", "Unit Rate"], [
            ["120 miles in 2 hours", "60 miles per hour"],
        ]),
    },
    "math-g6-l12": {
        "data_table": table(["Fraction", "Decimal", "Percentage"], [
            ["1/2", "0.5", "50%"], ["1/4", "0.25", "25%"],
        ]),
    },
    "math-g6-l13": {
        "data_table": table(["Number", "Prime Factors"], [
            ["12", "2, 2, 3"], ["30", "2, 3, 5"],
        ]),
    },
    "math-g6-l15": {
        "data_table": table(["Step", "Order (PEMDAS)"], [
            ["1", "Parentheses"], ["2", "Exponents"], ["3", "Multiplication/Division"], ["4", "Addition/Subtraction"],
        ]),
    },
    "math-g6-l17": {
        "data_table": table(["Shape", "Area Formula"], [
            ["Rectangle", "length x width"], ["Triangle", "1/2 x base x height"],
        ]),
    },
    "math-g6-l18": {
        "data_table": table(["Shape", "Surface Area Formula"], [
            ["Cube", "6 x side^2"], ["Rectangular prism", "2(lw + lh + wh)"],
        ]),
    },
    "math-g6-l19": {
        "data_table": table(["Shape", "Volume Formula"], [
            ["Rectangular prism", "length x width x height"],
        ]),
    },
    "math-g6-l21": {
        "data_table": table(["Angle Pair", "Relationship"], [
            ["Complementary", "Sum to 90 degrees"], ["Supplementary", "Sum to 180 degrees"],
        ]),
    },
    "math-g6-l22": {
        "data_table": table(["Triangle Type", "Property"], [
            ["Equilateral", "All 3 sides equal"], ["Right triangle", "One 90-degree angle"],
        ]),
    },
    "math-g6-l23": {
        "data_table": table(["Shape", "Lines of Symmetry"], [
            ["Square", "4"], ["Regular hexagon", "6"],
        ]),
    },
    "math-g6-l24": {
        "data_table": table(["Data Value", "Frequency"], [
            ["3", "5"], ["4", "8"], ["5", "3"],
        ]),
    },
    "math-g6-l26": {
        "data_table": table(["Graph Type", "Best Used For"], [
            ["Bar graph", "Comparing categories"], ["Line graph", "Showing change over time"], ["Pie chart", "Showing proportions"],
        ]),
    },
    "math-g6-l27": {
        "data_table": table(["Event", "Probability"], [
            ["Coin lands heads", "1/2"], ["Rolling a 6 on a die", "1/6"],
        ]),
    },
    "math-g6-l28": {
        "data_table": table(["Number", "Absolute Value"], [
            ["-7", "7"], ["4", "4"],
        ]),
    },
    "math-g6-l29": {
        "data_table": table(["Equation", "Solution"], [
            ["x + 5 = 12", "x = 7"], ["3x = 21", "x = 7"],
        ]),
    },
    "math-g6-l30": {
        "data_table": table(["Inequality", "Meaning"], [
            ["x > 3", "x is greater than 3"], ["x <= 5", "x is less than or equal to 5"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Math lessons (completing 30/30).")


if __name__ == "__main__":
    main()
