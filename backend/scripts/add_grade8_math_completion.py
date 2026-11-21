#!/usr/bin/env python3
"""Depth pass, Grade 8 Math: fill in real, hand-checked data_table
content for the 34 Grade 8 Math lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Math to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "math-g8-l1": {
        "data_table": table(["System", "Solution"], [
            ["x + y = 10, x - y = 2", "x = 6, y = 4"],
        ]),
    },
    "math-g8-l3": {
        "data_table": table(["Theorem", "Statement"], [
            ["Angle in a semicircle", "Is always 90 degrees"], ["Angles in the same segment", "Are equal"],
        ]),
    },
    "math-g8-l4": {
        "data_table": table(["Equation", "Solution"], [
            ["2x + 3 = 11", "x = 4"],
        ]),
    },
    "math-g8-l5": {
        "data_table": table(["Inequality", "Meaning"], [
            ["x > 3", "x is greater than 3"], ["x <= 5", "x is less than or equal to 5"],
        ]),
    },
    "math-g8-l6": {
        "data_table": table(["Expression", "Factored Form"], [
            ["x^2 + 5x + 6", "(x + 2)(x + 3)"],
        ]),
    },
    "math-g8-l7": {
        "data_table": table(["Identity", "Statement"], [
            ["(a + b)^2", "a^2 + 2ab + b^2"], ["(a - b)^2", "a^2 - 2ab + b^2"],
        ]),
    },
    "math-g8-l8": {
        "data_table": table(["Expression", "Value"], [
            ["2^3", "8"], ["2^-1", "0.5"],
        ]),
    },
    "math-g8-l9": {
        "data_table": table(["Proportion Type", "Example"], [
            ["Direct", "As x doubles, y doubles"], ["Inverse", "As x doubles, y halves"],
        ]),
    },
    "math-g8-l10": {
        "data_table": table(["Ratio", "Simplified"], [
            ["8:12", "2:3"],
        ]),
    },
    "math-g8-l11": {
        "data_table": table(["Original", "New", "% Change"], [
            ["$50", "$60", "+20%"],
        ]),
    },
    "math-g8-l12": {
        "data_table": table(["Item", "Marked Price", "Discount", "Final Price"], [
            ["Shirt", "$40", "25%", "$30"],
        ]),
    },
    "math-g8-l13": {
        "data_table": table(["Interest Type", "Formula"], [
            ["Simple interest", "I = P x R x T"], ["Compound interest", "A = P(1 + r)^t"],
        ]),
    },
    "math-g8-l14": {
        "data_table": table(["Number", "Rational?"], [
            ["3/4", "Yes"], ["Square root of 2", "No (irrational)"],
        ]),
    },
    "math-g8-l17": {
        "data_table": table(["Pattern", "Next Term"], [
            ["2, 4, 6, 8", "10"], ["1, 4, 9, 16", "25"],
        ]),
    },
    "math-g8-l18": {
        "data_table": table(["Shape", "Area Formula"], [
            ["Rectangle", "length x width"], ["Triangle", "1/2 x base x height"],
        ]),
    },
    "math-g8-l19": {
        "data_table": table(["Shape", "Volume Formula"], [
            ["Rectangular prism", "length x width x height"], ["Cylinder", "pi*r^2*h"],
        ]),
    },
    "math-g8-l20": {
        "data_table": table(["Point", "Coordinates"], [
            ["Origin", "(0, 0)"], ["Example point", "(3, 4)"],
        ]),
    },
    "math-g8-l21": {
        "data_table": table(["Line Equation", "Gradient (Slope)"], [
            ["y = 2x + 3", "2"],
        ]),
    },
    "math-g8-l22": {
        "data_table": table(["Data Set", "Mean", "Median"], [
            ["2, 4, 4, 6", "4", "4"],
        ]),
    },
    "math-g8-l23": {
        "data_table": table(["Event", "Probability"], [
            ["Coin lands heads", "1/2"], ["Rolling a 6 on a die", "1/6"],
        ]),
    },
    "math-g8-l24": {
        "data_table": table(["Quadrilateral", "Property"], [
            ["Square", "4 equal sides, 4 right angles"], ["Rhombus", "4 equal sides"],
        ]),
    },
    "math-g8-l25": {
        "data_table": table(["Congruence Rule", "Meaning"], [
            ["SSS", "All three sides equal"], ["SAS", "Two sides and included angle equal"],
        ]),
    },
    "math-g8-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Similar", "Same shape, different size"],
        ]),
    },
    "math-g8-l28": {
        "data_table": table(["Construction", "Tool"], [
            ["Bisecting an angle", "Compass and straightedge"],
        ]),
    },
    "math-g8-l29": {
        "data_table": table(["Transformation", "Effect"], [
            ["Translation", "Slides a shape without rotating or resizing"],
            ["Rotation", "Turns a shape around a point"],
        ]),
    },
    "math-g8-l30": {
        "data_table": table(["Set Notation", "Meaning"], [
            ["A union B", "Elements in A or B"], ["A intersect B", "Elements in both A and B"],
        ]),
    },
    "math-g8-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Function", "A rule assigning each input exactly one output"],
        ]),
    },
    "math-g8-l32": {
        "data_table": table(["Sequence", "Next Term"], [
            ["2, 4, 6, 8", "10"],
        ]),
    },
    "math-g8-l33": {
        "data_table": table(["Bill Type", "Example"], [
            ["Utility bill", "Electricity, water"], ["Tax", "Sales tax on a purchase"],
        ]),
    },
    "math-g8-l35": {
        "data_table": table(["Concept", "Example"], [
            ["Work rate", "A worker completes 1/5 of a job per day"],
        ]),
    },
    "math-g8-l36": {
        "data_table": table(["Expression", "Simplified"], [
            ["3x + 2x - 4", "5x - 4"],
        ]),
    },
    "math-g8-l37": {
        "data_table": table(["Line Equation", "Slope"], [
            ["y = 3x + 1", "3"],
        ]),
    },
    "math-g8-l38": {
        "data_table": table(["Measure", "Meaning"], [
            ["Mean", "The average of a data set"], ["Mode", "The most frequent value"],
        ]),
    },
    "math-g8-l40": {
        "data_table": table(["Graph Type", "Best Used For"], [
            ["Bar chart", "Comparing categories"], ["Histogram", "Showing frequency of continuous data"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Math lessons (completing 40/40).")


if __name__ == "__main__":
    main()
