#!/usr/bin/env python3
"""Singapore Math integration, Grade 6: adds a `singapore_math` field to
Math lessons where Singapore's MOE Primary Mathematics methodology --
the model (bar) method for fractions, ratios, rates, and percentages
-- applies. This is the final year of Singapore's Primary Mathematics
syllabus (Primary 6 / PSLE), where the bar model is used for its most
advanced word problems. Supplements the existing Math curriculum
without replacing it.

Idempotent: only fills in the field where it isn't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_singapore_math.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


SINGAPORE_MATH: dict[str, dict] = {
    "math-g6-l4": {
        "method": "Bar Model (Mixed Numbers)",
        "explanation": "Working with mixed numbers like 3 2/5 continues the bar model from earlier grades: whole bars plus a partially shaded bar, making it easy to convert to the improper fraction 17/5 or back again.",
        "example": table(["Representation", "Value"], [["3 full bars + 2/5 of a bar", "3 2/5"], ["17 fifths total", "17/5"]]),
    },
    "math-g6-l5": {
        "method": "Bar Model (Adding and Subtracting Fractions)",
        "explanation": "Adding fractions with different denominators is modeled by redrawing both bars split into the same number of equal parts (the common denominator), so the parts can be counted and combined directly.",
        "example": table(["Fraction", "Common Denominator Parts"], [["2/3", "8/12"], ["1/4", "3/12"], ["Sum", "11/12"]]),
    },
    "math-g6-l6": {
        "method": "Bar Model (Fraction of a Fraction)",
        "explanation": "Multiplying fractions is modeled by shading one fraction of a bar, then taking a further fraction of that shaded region, so the final overlap shows the product visually before simplifying.",
        "example": table(["Step", "Result"], [["Shade 3/4 of the bar", "3/4"], ["Take 2/3 of the shaded part", "1/2"]]),
    },
    "math-g6-l9": {
        "method": "Bar Model (Ratio)",
        "explanation": "Ratio bars remain central at this level: a ratio of 5:3 is drawn as two bars split into 5 and 3 equal units of the same size, so proportional word problems (e.g. sharing a total in a given ratio) can be solved by finding the value of one unit first.",
        "example": table(["Quantity", "Ratio Units", "If Total is 40 (8 units)"], [["First quantity", "5 units", "25"], ["Second quantity", "3 units", "15"]]),
    },
    "math-g6-l10": {
        "method": "Bar Model (Rate)",
        "explanation": "A unit rate like 'km per hour' is modeled as a single bar representing one unit of the base quantity (1 hour) matched to its rate value, so scaling up to more hours means repeating that same bar length.",
        "example": table(["Base Unit", "Rate", "Scaled (x4)"], [["1 hour", "60 km", "240 km"]]),
    },
    "math-g6-l11": {
        "method": "Bar Model (Percentage)",
        "explanation": "Percent problems such as 'find 15% of 200' are modeled as a bar of 200 split into 20 equal parts (each 5%), so 3 parts (15%) is read off directly as 30.",
        "example": table(["Whole", "Split Into", "3 Parts (15%)"], [["200", "20 equal parts (5% each)", "30"]]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in SINGAPORE_MATH if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Math: {missing}")

    updated = 0
    for lid, content in SINGAPORE_MATH.items():
        lesson = by_id[lid]
        if "singapore_math" not in lesson:
            lesson["singapore_math"] = content
            updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added Singapore Math content to {updated} Grade 6 Math lessons.")


if __name__ == "__main__":
    main()
