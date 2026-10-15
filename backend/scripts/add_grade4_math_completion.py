#!/usr/bin/env python3
"""Depth pass, Grade 4 Math: fill in real, hand-checked data_table content
for the 24 Grade 4 Math lessons not covered by the earlier breadth-first
batch. Brings Grade 4 Math to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "math-g4-l1": {
        "data_table": table(["Number", "Word Form"], [
            ["1,000,000", "One million"], ["250,000", "Two hundred fifty thousand"],
        ]),
    },
    "math-g4-l2": {
        "data_table": table(["Problem", "Answer"], [
            ["23 x 14", "322"], ["45 x 32", "1,440"],
        ]),
    },
    "math-g4-l3": {
        "data_table": table(["Improper Fraction", "Mixed Number"], [
            ["7/2", "3 1/2"], ["11/4", "2 3/4"],
        ]),
    },
    "math-g4-l5": {
        "data_table": table(["Number", "Rounded to Nearest 100"], [
            ["452", "500"], ["1,349", "1,300"],
        ]),
    },
    "math-g4-l6": {
        "data_table": table(["Problem", "Answer"], [
            ["4,672 + 1,859", "6,531"], ["5,003 - 2,467", "2,536"],
        ]),
    },
    "math-g4-l7": {
        "data_table": table(["Problem", "Answer"], [
            ["47 / 5", "9 remainder 2"], ["83 / 6", "13 remainder 5"],
        ]),
    },
    "math-g4-l11": {
        "data_table": table(["Problem", "Answer"], [
            ["1/8 + 3/8", "4/8 = 1/2"], ["5/6 - 2/6", "3/6 = 1/2"],
        ]),
    },
    "math-g4-l12": {
        "data_table": table(["Decimal", "Fraction"], [
            ["0.1", "1/10"], ["0.25", "25/100"],
        ]),
    },
    "math-g4-l13": {
        "data_table": table(["Decimals", "Order (smallest to largest)"], [
            ["0.5, 0.05, 0.45", "0.05, 0.45, 0.5"],
        ]),
    },
    "math-g4-l15": {
        "data_table": table(["Shape", "Lines of Symmetry"], [
            ["Square", "4"], ["Rectangle", "2"],
        ]),
    },
    "math-g4-l16": {
        "data_table": table(["Triangle Type", "Property"], [
            ["Equilateral", "All 3 sides equal"], ["Isosceles", "2 sides equal"], ["Scalene", "No sides equal"],
        ]),
    },
    "math-g4-l17": {
        "data_table": table(["Unit", "Used For"], [
            ["Centimeter", "Length"], ["Kilogram", "Mass"], ["Liter", "Volume"],
        ]),
    },
    "math-g4-l18": {
        "data_table": table(["Start", "End", "Elapsed"], [
            ["1:15 PM", "3:45 PM", "2 hours 30 minutes"],
        ]),
    },
    "math-g4-l20": {
        "data_table": table(["Problem", "Answer"], [
            ["Buy 3 items at $4 each, pay with $20", "Change: $8"],
        ]),
    },
    "math-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Population counts", "A city with 1,245,000 residents"],
        ]),
    },
    "math-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Total cost", "12 boxes x 15 items each = 180 items"],
        ]),
    },
    "math-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Recipe scaling", "Using 1 3/4 cups of flour"],
        ]),
    },
    "math-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Building design", "A roof angle of 45 degrees"],
        ]),
    },
    "math-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Estimating a bill", "Rounding $27.85 to $30"],
        ]),
    },
    "math-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Bank balance", "$542 deposit - $178 withdrawal = $364"],
        ]),
    },
    "math-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Sharing items evenly", "50 candies among 6 friends = 8 each, 2 left over"],
        ]),
    },
    "math-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Arranging chairs in equal rows", "24 chairs arranged in rows of 4, 6, 8, or 12"],
        ]),
    },
    "math-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Security codes", "Prime numbers are used in cryptography"],
        ]),
    },
    "math-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Sharing a pizza", "4/8 of a pizza is the same as 1/2"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Math lessons (completing 30/30).")


if __name__ == "__main__":
    main()
