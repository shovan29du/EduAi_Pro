#!/usr/bin/env python3
"""Depth pass, Grade 9 Math: fill in real, hand-checked data_table
content for the 44 Grade 9 Math lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Math to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "math-g9-l1": {
        "data_table": table(["Ratio", "Name"], [
            ["Opposite/Hypotenuse", "Sine"], ["Adjacent/Hypotenuse", "Cosine"], ["Opposite/Adjacent", "Tangent"],
        ]),
    },
    "math-g9-l2": {
        "data_table": table(["Function", "Example"], [
            ["Linear", "y = 2x + 3"], ["Quadratic", "y = x^2 + 1"],
        ]),
    },
    "math-g9-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Null hypothesis", "The default assumption of no effect"], ["p-value", "Probability of observing the result by chance"],
        ]),
    },
    "math-g9-l4": {
        "data_table": table(["Equation", "Solution"], [
            ["2x + 3 = 11", "x = 4"],
        ]),
    },
    "math-g9-l5": {
        "data_table": table(["Equation", "Example Solution Point"], [
            ["y = 2x + 1", "(0, 1)"],
        ]),
    },
    "math-g9-l6": {
        "data_table": table(["System", "Solution"], [
            ["x + y = 10, x - y = 2", "x = 6, y = 4"],
        ]),
    },
    "math-g9-l7": {
        "data_table": table(["Inequality", "Meaning"], [
            ["x > 3", "x is greater than 3"],
        ]),
    },
    "math-g9-l8": {
        "data_table": table(["Expression", "Factored Form"], [
            ["x^2 + 5x + 6", "(x + 2)(x + 3)"],
        ]),
    },
    "math-g9-l10": {
        "data_table": table(["Function", "Vertex"], [
            ["y = x^2", "(0, 0)"], ["y = (x-2)^2 + 1", "(2, 1)"],
        ]),
    },
    "math-g9-l11": {
        "data_table": table(["Problem", "Answer"], [
            ["(3x + 2) + (2x - 5)", "5x - 3"],
        ]),
    },
    "math-g9-l12": {
        "data_table": table(["Problem", "Answer"], [
            ["(x + 2)(x + 3)", "x^2 + 5x + 6"],
        ]),
    },
    "math-g9-l13": {
        "data_table": table(["Problem", "Answer"], [
            ["(x^2 + 3x) / x", "x + 3"],
        ]),
    },
    "math-g9-l14": {
        "data_table": table(["Rule", "Example"], [
            ["Product rule", "x^2 * x^3 = x^5"], ["Power rule", "(x^2)^3 = x^6"],
        ]),
    },
    "math-g9-l15": {
        "data_table": table(["Number", "Scientific Notation"], [
            ["3,400,000", "3.4 x 10^6"],
        ]),
    },
    "math-g9-l17": {
        "data_table": table(["Expression", "Simplified"], [
            ["(x^2 - 4)/(x - 2)", "x + 2"],
        ]),
    },
    "math-g9-l18": {
        "data_table": table(["Equation", "Solution"], [
            ["1/x = 1/4", "x = 4"],
        ]),
    },
    "math-g9-l19": {
        "data_table": table(["Equation", "Solution"], [
            ["|x| = 5", "x = 5 or x = -5"],
        ]),
    },
    "math-g9-l20": {
        "data_table": table(["Points", "Slope"], [
            ["(1,2) and (3,6)", "2"],
        ]),
    },
    "math-g9-l21": {
        "data_table": table(["Form", "Example"], [
            ["Slope-intercept", "y = mx + b"],
        ]),
    },
    "math-g9-l22": {
        "data_table": table(["Form", "Example"], [
            ["Point-slope", "y - y1 = m(x - x1)"],
        ]),
    },
    "math-g9-l23": {
        "data_table": table(["Line Relationship", "Slope Rule"], [
            ["Parallel", "Same slope"], ["Perpendicular", "Slopes are negative reciprocals"],
        ]),
    },
    "math-g9-l24": {
        "data_table": table(["Variation Type", "Example"], [
            ["Direct", "As x doubles, y doubles"], ["Inverse", "As x doubles, y halves"],
        ]),
    },
    "math-g9-l25": {
        "data_table": table(["Function", "Example"], [
            ["Exponential growth", "y = 2^x"],
        ]),
    },
    "math-g9-l26": {
        "data_table": table(["Type", "Formula"], [
            ["Growth", "A = P(1 + r)^t"], ["Decay", "A = P(1 - r)^t"],
        ]),
    },
    "math-g9-l28": {
        "data_table": table(["Sequence Type", "Example"], [
            ["Geometric", "2, 6, 18, 54 (ratio 3)"],
        ]),
    },
    "math-g9-l29": {
        "data_table": table(["Set Notation", "Meaning"], [
            ["A union B", "Elements in A or B"], ["A intersect B", "Elements in both A and B"],
        ]),
    },
    "math-g9-l30": {
        "data_table": table(["Event Type", "Example"], [
            ["Independent", "Two separate coin flips"], ["Dependent", "Drawing cards without replacement"],
        ]),
    },
    "math-g9-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Combination", "Selection where order doesn't matter"], ["Permutation", "Arrangement where order matters"],
        ]),
    },
    "math-g9-l32": {
        "data_table": table(["Data Set", "Mean", "Median"], [
            ["2, 4, 4, 6", "4", "4"],
        ]),
    },
    "math-g9-l33": {
        "data_table": table(["Display", "Best Used For"], [
            ["Histogram", "Frequency of continuous data"], ["Box plot", "Showing quartiles and outliers"],
        ]),
    },
    "math-g9-l34": {
        "data_table": table(["Correlation Type", "Meaning"], [
            ["Positive", "Both variables increase together"],
        ]),
    },
    "math-g9-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Congruent", "Same shape and size"], ["Similar", "Same shape, different size"],
        ]),
    },
    "math-g9-l37": {
        "data_table": table(["Triangle Type", "Angle Ratio"], [
            ["45-45-90", "1:1:sqrt(2)"], ["30-60-90", "1:sqrt(3):2"],
        ]),
    },
    "math-g9-l38": {
        "data_table": table(["Shape", "Area Formula"], [
            ["Rectangle", "length x width"], ["Triangle", "1/2 x base x height"],
        ]),
    },
    "math-g9-l39": {
        "data_table": table(["Shape", "Surface Area Formula"], [
            ["Cube", "6 x side^2"],
        ]),
    },
    "math-g9-l40": {
        "data_table": table(["Shape", "Volume Formula"], [
            ["Rectangular prism", "length x width x height"], ["Sphere", "4/3 x pi x r^3"],
        ]),
    },
    "math-g9-l42": {
        "data_table": table(["Theorem", "Statement"], [
            ["Angle in a semicircle", "Is always 90 degrees"],
        ]),
    },
    "math-g9-l43": {
        "data_table": table(["Formula", "Use"], [
            ["Distance formula", "sqrt((x2-x1)^2 + (y2-y1)^2)"], ["Midpoint formula", "((x1+x2)/2, (y1+y2)/2)"],
        ]),
    },
    "math-g9-l44": {
        "data_table": table(["Transformation", "Effect"], [
            ["Translation", "Slides a shape without rotating"], ["Reflection", "Flips a shape over a line"],
        ]),
    },
    "math-g9-l45": {
        "data_table": table(["Transformation", "Effect"], [
            ["Rotation", "Turns a shape around a point"], ["Dilation", "Resizes a shape"],
        ]),
    },
    "math-g9-l46": {
        "data_table": table(["Number Type", "Example"], [
            ["Rational", "3/4"], ["Irrational", "Square root of 2"],
        ]),
    },
    "math-g9-l47": {
        "data_table": table(["Problem Type", "Example"], [
            ["Mixture problem", "Combining two solutions of different concentrations"],
        ]),
    },
    "math-g9-l49": {
        "data_table": table(["Interest Type", "Formula"], [
            ["Simple interest", "I = P x R x T"], ["Compound interest", "A = P(1 + r)^t"],
        ]),
    },
    "math-g9-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Proof", "A logical argument establishing a mathematical truth"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Math lessons (completing 50/50).")


if __name__ == "__main__":
    main()
