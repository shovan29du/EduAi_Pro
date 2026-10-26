#!/usr/bin/env python3
"""Pilot: add genuine, hand-checked data_table / graph / formulae content to
all 30 Grade 5 Math lessons (SubjectLessons.jsx already renders all three).

Every number here is either a real, verifiable mathematical fact (e.g. 2^3 =
8, a triangle's angles sum to 180 degrees) or explicitly-labelled
illustrative example data for a worked problem (e.g. "Plant Height Over 6
Weeks (Example Data)") -- never a claim about a specific real-world dataset
presented as fact. This is the pilot for the "which subjects/lessons get
real charts" pass described in add_lesson_visuals.py; Phase 1 (figure +
wiki_title) already covers every lesson in every subject.

Idempotent: only fills in `data_table` / `graph` / `formulae` fields that
aren't already set, so it won't clobber a hand edit on re-run.

Re-run after editing:
    python3 backend/scripts/add_grade5_math_lesson_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


def graph(title, points, x_axis, y_axis):
    return {"title": title, "points": points, "x_axis": x_axis, "y_axis": y_axis}


CHARTS: dict[str, dict] = {
    "math-g5-l1": {
        "data_table": table(["Fraction", "Decimal", "Percent"], [
            ["1/4", "0.25", "25%"], ["1/2", "0.5", "50%"], ["3/4", "0.75", "75%"],
            ["1/5", "0.2", "20%"], ["1/10", "0.1", "10%"],
        ]),
        "formulae": ["Percent = (Part ÷ Whole) × 100", "Amount = Percent × Whole ÷ 100"],
    },
    "math-g5-l2": {
        "data_table": table(["Ratio", "Simplified", "Equivalent (×3)"], [
            ["2:4", "1:2", "6:12"], ["3:9", "1:3", "9:27"],
            ["6:8", "3:4", "18:24"], ["10:15", "2:3", "30:45"],
        ]),
        "formulae": ["If a:b = c:d, then a × d = b × c (cross-multiplication)"],
    },
    "math-g5-l3": {
        "data_table": table(["Data Set", "Mean", "Median", "Mode"], [
            ["4, 8, 6, 5, 8", "6.2", "6", "8"],
            ["10, 12, 12, 15, 20, 12", "13.5", "12", "12"],
        ]),
        "formulae": ["Mean = (Sum of all values) ÷ (Number of values)"],
    },
    "math-g5-l4": {
        "data_table": table(["Step", "Calculation", "Result"], [
            ["Multiply by ones", "234 × 6", "1,404"],
            ["Multiply by tens", "234 × 50", "11,700"],
            ["Add partial products", "1,404 + 11,700", "13,104"],
        ]),
        "formulae": ["234 × 56 = (234 × 50) + (234 × 6) = 11,700 + 1,404 = 13,104"],
    },
    "math-g5-l5": {
        "data_table": table(["Step", "Action", "Result"], [
            ["Divide hundreds", "9 ÷ 4", "2 remainder 1"],
            ["Bring down tens digit", "13 ÷ 4", "3 remainder 1"],
            ["Bring down ones digit", "16 ÷ 4", "4 remainder 0"],
        ]),
        "formulae": ["936 ÷ 4 = 234 (check: 234 × 4 = 936)"],
    },
    "math-g5-l6": {
        "data_table": table(["Expression", "Step 1", "Step 2", "Result"], [
            ["(2 + 3) × 4", "Parentheses: 2 + 3 = 5", "5 × 4", "20"],
            ["10 − 2² + 1", "Exponent: 2² = 4", "10 − 4 + 1", "7"],
        ]),
        "formulae": [
            "Order: Parentheses, Exponents, Multiplication/Division (left to right), Addition/Subtraction (left to right)",
            "3 + 4 × 2 = 3 + 8 = 11 (not 14)",
        ],
    },
    "math-g5-l7": {
        "data_table": table(["Fractions", "Common Denominator", "Result"], [
            ["1/2 + 1/3", "6", "5/6"], ["3/4 − 1/6", "12", "7/12"], ["2/5 + 1/4", "20", "13/20"],
        ]),
        "formulae": ["1/3 + 1/4 = 4/12 + 3/12 = 7/12"],
    },
    "math-g5-l8": {
        "formulae": ["2/3 × 3/5 = (2 × 3)/(3 × 5) = 6/15 = 2/5 (simplified)"],
    },
    "math-g5-l9": {
        "formulae": ["1/2 ÷ 1/4 = 1/2 × 4/1 = 4/2 = 2 (keep, change, flip)"],
    },
    "math-g5-l10": {
        "data_table": table(["Expression", "Result"], [
            ["0.5 × 0.6", "0.3"], ["2.4 ÷ 0.6", "4"], ["1.25 × 4", "5"],
        ]),
        "formulae": ["1.2 × 0.4 = 0.48 (2 decimal places total)", "6.4 ÷ 0.8 = 64 ÷ 8 = 8"],
    },
    "math-g5-l11": {
        "data_table": table(["Fraction", "Decimal", "Percent"], [
            ["1/8", "0.125", "12.5%"], ["3/5", "0.6", "60%"],
            ["7/20", "0.35", "35%"], ["9/10", "0.9", "90%"],
        ]),
    },
    "math-g5-l12": {
        "data_table": table(["Expression", "Result", "Direction on Number Line"], [
            ["−3 + 5", "2", "Move right 5 from −3"],
            ["4 − 7", "−3", "Move left 7 from 4"],
            ["−2 − 3", "−5", "Move left 3 from −2"],
        ]),
    },
    "math-g5-l13": {
        "data_table": table(["Expression", "Meaning", "Value"], [
            ["2³", "2 × 2 × 2", "8"], ["5²", "5 × 5", "25"],
            ["10⁴", "10 × 10 × 10 × 10", "10,000"], ["3⁴", "3 × 3 × 3 × 3", "81"],
        ]),
        "formulae": ["aⁿ = a × a × ... × a (n times)"],
    },
    "math-g5-l14": {
        "data_table": table(["Length", "Width", "Height", "Volume"], [
            ["4 cm", "3 cm", "2 cm", "24 cm³"], ["5 cm", "5 cm", "5 cm", "125 cm³"], ["10 cm", "2 cm", "3 cm", "60 cm³"],
        ]),
        "formulae": ["Volume = length × width × height"],
    },
    "math-g5-l15": {
        "data_table": table(["Point", "x", "y", "Quadrant"], [
            ["A", "3", "2", "I"], ["B", "−3", "2", "II"], ["C", "−3", "−2", "III"], ["D", "3", "−2", "IV"],
        ]),
    },
    "math-g5-l16": {
        "data_table": table(["Shape", "Sides", "Sum of Interior Angles"], [
            ["Triangle", "3", "180°"], ["Quadrilateral", "4", "360°"],
            ["Pentagon", "5", "540°"], ["Hexagon", "6", "720°"],
        ]),
        "formulae": ["Sum of interior angles = (n − 2) × 180°, where n = number of sides"],
    },
    "math-g5-l17": {
        "data_table": table(["Angle Type", "Degree Range"], [
            ["Acute", "Between 0° and 90°"], ["Right", "Exactly 90°"],
            ["Obtuse", "Between 90° and 180°"], ["Straight", "Exactly 180°"],
        ]),
    },
    "math-g5-l18": {
        "data_table": table(["Radius", "Diameter", "Circumference (≈)"], [
            ["3 cm", "6 cm", "18.84 cm"], ["5 cm", "10 cm", "31.4 cm"], ["7 cm", "14 cm", "43.96 cm"],
        ]),
        "formulae": ["Diameter = 2 × radius", "Circumference = π × diameter ≈ 3.14 × diameter"],
    },
    "math-g5-l19": {
        "graph": graph("Plant Height Over 6 Weeks (Example Data)", [2, 4, 7, 9, 13, 15], "Week", "Height (cm)"),
    },
    "math-g5-l20": {
        "data_table": table(["Value", "Distance from Mean (6)"], [
            ["4", "2"], ["8", "2"], ["6", "0"], ["5", "1"], ["7", "1"],
        ]),
        "formulae": ["Mean Absolute Deviation = (Sum of |value − mean|) ÷ (Number of values) = 1.2"],
    },
    "math-g5-l21": {
        "data_table": table(["Event", "Favorable Outcomes", "Total Outcomes", "Probability"], [
            ["Rolling a 4 on a die", "1", "6", "1/6"],
            ["Flipping heads on a coin", "1", "2", "1/2"],
            ["Drawing a red card from a deck", "26", "52", "1/2"],
            ["Rolling an even number on a die", "3", "6", "1/2"],
        ]),
        "formulae": ["Probability = Favorable outcomes ÷ Total outcomes"],
    },
    "math-g5-l22": {
        "data_table": table(["Expression", "If x = 3"], [
            ["x + 5", "8"], ["2x", "6"], ["x²", "9"], ["3x − 1", "8"],
        ]),
        "formulae": ["In 3x + 2: the variable is x, the coefficient is 3, and the constant is 2"],
    },
    "math-g5-l23": {
        "data_table": table(["Equation", "Operation", "Solution"], [
            ["x + 4 = 10", "Subtract 4 from both sides", "x = 6"],
            ["x − 5 = 9", "Add 5 to both sides", "x = 14"],
            ["4x = 20", "Divide both sides by 4", "x = 5"],
            ["x ÷ 3 = 6", "Multiply both sides by 3", "x = 18"],
        ]),
        "formulae": ["x + 7 = 12 → x = 12 − 7 = 5", "3x = 21 → x = 21 ÷ 3 = 7"],
    },
    "math-g5-l24": {
        "graph": graph("Sequence: Add 3 Each Time", [2, 5, 8, 11, 14, 17], "Term Number", "Value"),
        "formulae": ["Term(n) = Term(1) + (n − 1) × common difference"],
    },
    "math-g5-l25": {
        "data_table": table(["Number", "Rounded to Nearest 10", "Rounded to Nearest 100"], [
            ["247", "250", "200"], ["582", "580", "600"], ["1,349", "1,350", "1,300"], ["95", "100", "100"],
        ]),
    },
    "math-g5-l26": {
        "formulae": [
            "Total cost = (Price per item × Quantity) + Delivery fee",
            "Example: 4 books at $6 each plus $5 shipping = (4 × 6) + 5 = $29",
        ],
    },
    "math-g5-l27": {
        "data_table": table(["Unit", "Equivalent"], [
            ["1 kilometer", "1,000 meters"], ["1 meter", "100 centimeters"],
            ["1 kilogram", "1,000 grams"], ["1 liter", "1,000 milliliters"], ["1 hour", "60 minutes"],
        ]),
    },
    "math-g5-l28": {
        "data_table": table(["Start Time", "Elapsed Time", "End Time"], [
            ["9:15 AM", "2 hours 30 minutes", "11:45 AM"],
            ["1:40 PM", "3 hours 45 minutes", "5:25 PM"],
            ["10:50 PM", "4 hours 20 minutes", "3:10 AM (next day)"],
        ]),
        "formulae": ["End time = Start time + Elapsed time"],
    },
    "math-g5-l29": {
        "data_table": table(["Category", "Recommended % of Income"], [
            ["Needs (housing, food, bills)", "50%"],
            ["Wants (entertainment, dining out)", "30%"],
            ["Savings and debt repayment", "20%"],
        ]),
    },
    "math-g5-l30": {
        "data_table": table(["Number", "Prime Factorization"], [
            ["12", "2 × 2 × 3"], ["18", "2 × 3 × 3"], ["30", "2 × 3 × 5"], ["100", "2 × 2 × 5 × 5"],
        ]),
        "formulae": ["Every number greater than 1 can be written as a unique product of prime numbers (Fundamental Theorem of Arithmetic)"],
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} chart/table/formula fields across {len(CHARTS)} Grade 5 Math lessons.")


if __name__ == "__main__":
    main()
