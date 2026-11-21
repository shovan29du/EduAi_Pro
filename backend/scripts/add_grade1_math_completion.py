#!/usr/bin/env python3
"""Depth pass, Grade 1 Math: fill in real, hand-checked data_table content
for the 15 Grade 1 Math lessons not covered by the earlier breadth-first
batch (add_math_charts_all_levels.py did 5 of Grade 1's 20 Math lessons).
This brings Grade 1 Math to full 20/20 real-content coverage.

Every fact is real (number words, ordinal words, season months, 3D shape
face counts) or explicitly-labelled illustrative example data (a sorting
graph) -- never fabricated or presented as fact when it's actually
invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


def graph(title, points, x_axis, y_axis):
    return {"title": title, "points": points, "x_axis": x_axis, "y_axis": y_axis}


CHARTS: dict[str, dict] = {
    "math-g1-l1": {
        "data_table": table(["Number", "Number Word"], [
            ["1", "One"], ["2", "Two"], ["3", "Three"], ["4", "Four"], ["5", "Five"],
            ["6", "Six"], ["7", "Seven"], ["8", "Eight"], ["9", "Nine"], ["10", "Ten"],
        ]),
    },
    "math-g1-l2": {
        "data_table": table(["Number", "Number Word"], [
            ["11", "Eleven"], ["12", "Twelve"], ["13", "Thirteen"], ["14", "Fourteen"], ["15", "Fifteen"],
            ["16", "Sixteen"], ["17", "Seventeen"], ["18", "Eighteen"], ["19", "Nineteen"], ["20", "Twenty"],
        ]),
    },
    "math-g1-l4": {
        "data_table": table(["Fact", "Answer"], [
            ["10 - 1", "9"], ["10 - 2", "8"], ["10 - 3", "7"], ["10 - 4", "6"], ["10 - 5", "5"],
        ]),
    },
    "math-g1-l5": {
        "data_table": table(["Pattern Type", "Example"], [
            ["Repeating pattern", "Red, Blue, Red, Blue, Red, Blue"],
            ["Growing pattern", "1 star, 2 stars, 3 stars, 4 stars"],
        ]),
    },
    "math-g1-l6": {
        "data_table": table(["Measurement Type", "Common Units"], [
            ["Length", "Centimeters (cm), Inches (in)"], ["Weight", "Grams (g), Pounds (lb)"],
        ]),
    },
    "math-g1-l7": {
        "data_table": table(["Season", "Months (Northern Hemisphere)"], [
            ["Spring", "March, April, May"], ["Summer", "June, July, August"],
            ["Autumn / Fall", "September, October, November"], ["Winter", "December, January, February"],
        ]),
    },
    "math-g1-l8": {
        "graph": graph("Favorite Color Sorting (Example Data)", [4, 3, 5], "Color: Red, Blue, Green", "Number of Children"),
    },
    "math-g1-l9": {
        "data_table": table(["Skip Count by 10s", "Sequence"], [
            ["10s to 100", "10, 20, 30, 40, 50, 60, 70, 80, 90, 100"],
        ]),
    },
    "math-g1-l11": {
        "data_table": table(["Symbol", "Meaning"], [
            [">", "Greater than"], ["<", "Less than"], ["=", "Equal to"],
        ]),
    },
    "math-g1-l12": {
        "data_table": table(["Position", "Ordinal Word"], [
            ["1", "First"], ["2", "Second"], ["3", "Third"], ["4", "Fourth"], ["5", "Fifth"],
        ]),
    },
    "math-g1-l13": {
        "data_table": table(["Fact", "Answer"], [
            ["12 + 5", "17"], ["8 + 9", "17"], ["15 + 4", "19"],
        ]),
    },
    "math-g1-l14": {
        "data_table": table(["Fact", "Answer"], [
            ["20 - 7", "13"], ["18 - 9", "9"], ["16 - 8", "8"],
        ]),
    },
    "math-g1-l15": {
        "data_table": table(["Part", "Part (Together Make 10)"], [
            ["1", "9"], ["2", "8"], ["3", "7"], ["4", "6"], ["5", "5"],
        ]),
    },
    "math-g1-l18": {
        "data_table": table(["3D Shape", "Faces"], [
            ["Cube", "6"], ["Sphere", "0 (one curved surface)"],
            ["Cylinder", "2 flat + 1 curved"], ["Cone", "1 flat + 1 curved"],
        ]),
    },
    "math-g1-l19": {
        "data_table": table(["Position Word", "Meaning"], [
            ["Above", "Higher than something"], ["Below", "Lower than something"],
            ["Between", "In the middle of two things"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 Math lessons (completing 20/20).")


if __name__ == "__main__":
    main()
