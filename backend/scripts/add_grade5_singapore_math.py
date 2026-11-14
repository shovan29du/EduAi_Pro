#!/usr/bin/env python3
"""Singapore Math integration, Grade 5: adds a `singapore_math` field to
Math lessons where Singapore's MOE Primary Mathematics methodology --
the model (bar) method for ratio, percentage, and fraction operations
-- applies. Supplements the existing Math curriculum without replacing
it.

Idempotent: only fills in the field where it isn't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_singapore_math.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


SINGAPORE_MATH: dict[str, dict] = {
    "math-g5-l1": {
        "method": "Bar Model (Percentage)",
        "explanation": "A percentage problem like 'find 25% of 80' is drawn as a bar of 80 split into 4 equal parts (since 25% is 1/4), so one part -- 20 -- is visibly the answer.",
        "example": table(["Whole", "Split Into", "One Part (25%)"], [["80", "4 equal parts", "20"]]),
    },
    "math-g5-l2": {
        "method": "Bar Model (Ratio)",
        "explanation": "Singapore's hallmark 'ratio bars' represent a ratio like 3:2 as two bars of different lengths, each divided into equal units of the same size -- 3 units for one quantity and 2 units for the other -- so proportional relationships are seen directly.",
        "example": table(["Quantity", "Ratio Units", "If 1 Unit = 10"], [["First quantity", "3 units", "30"], ["Second quantity", "2 units", "20"]]),
    },
    "math-g5-l7": {
        "method": "Bar Model (Unlike Denominators)",
        "explanation": "Adding 1/3 + 1/4 is modeled by drawing two bars of the same total length, one split into 3 parts and one into 4, then redrawing both split into 12 equal parts (the common denominator) so 4/12 + 3/12 = 7/12 is visible.",
        "example": table(["Fraction", "Common Denominator Parts"], [["1/3", "4/12"], ["1/4", "3/12"], ["Sum", "7/12"]]),
    },
    "math-g5-l8": {
        "method": "Bar Model (Fraction of a Fraction)",
        "explanation": "Multiplying 1/2 x 2/3 is modeled by shading 2/3 of a bar, then taking half of that shaded region, showing the overlap directly gives 2/6, which simplifies to 1/3.",
        "example": table(["Step", "Result"], [["Shade 2/3 of the bar", "2/3"], ["Take half of the shaded part", "1/3"]]),
    },
    "math-g5-l9": {
        "method": "Bar Model (Dividing by a Fraction)",
        "explanation": "Dividing 3 by 1/2 asks 'how many halves fit into 3 whole bars?' -- drawing 3 bars each split into 2 halves shows there are 6 halves in total, so 3 / (1/2) = 6.",
        "example": table(["Whole Bars", "Halves per Bar", "Total Halves"], [["3", "2", "6"]]),
    },
    "math-g5-l26": {
        "method": "Bar Model (Word Problems)",
        "explanation": "Multi-operation word problems are solved by drawing a bar for each quantity described, aligning them to show comparisons or combined totals, and reading the answer from the resulting diagram before writing the number sentence.",
        "example": table(["Step", "Bar Model Action"], [["1", "Draw a bar for each named quantity"], ["2", "Mark 'more than' or 'less than' as extra or missing segments"], ["3", "Use the diagram to write the correct operations"]]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in SINGAPORE_MATH if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Math: {missing}")

    updated = 0
    for lid, content in SINGAPORE_MATH.items():
        lesson = by_id[lid]
        if "singapore_math" not in lesson:
            lesson["singapore_math"] = content
            updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added Singapore Math content to {updated} Grade 5 Math lessons.")


if __name__ == "__main__":
    main()
