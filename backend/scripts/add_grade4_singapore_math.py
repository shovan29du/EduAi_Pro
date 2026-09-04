#!/usr/bin/env python3
"""Singapore Math integration, Grade 4: adds a `singapore_math` field to
Math lessons where Singapore's MOE Primary Mathematics methodology --
the model (bar) method for fractions and multi-step word problems --
applies. Supplements the existing Math curriculum without replacing it.

Idempotent: only fills in the field where it isn't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_singapore_math.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


SINGAPORE_MATH: dict[str, dict] = {
    "math-g4-l3": {
        "method": "Bar Model (Mixed Numbers)",
        "explanation": "A mixed number like 2 1/3 is drawn as two full bars plus one bar split into 3 parts with 1 shaded, making the 'whole plus part' structure visible before converting it to the improper fraction 7/3.",
        "example": table(["Representation", "Value"], [["2 full bars + 1/3 of a bar", "2 1/3"], ["7 thirds total", "7/3"]]),
    },
    "math-g4-l10": {
        "method": "Bar Model (Equivalent Fractions)",
        "explanation": "Equivalent fractions are shown with two bars of the same length: one split into 2 parts (1/2 shaded) and one split into 4 parts (2 parts shaded), so students see that 1/2 and 2/4 cover the same shaded length.",
        "example": table(["Bar Split Into", "Parts Shaded", "Fraction"], [["2", "1", "1/2"], ["4", "2", "2/4"]]),
    },
    "math-g4-l11": {
        "method": "Bar Model (Adding Fractions)",
        "explanation": "Adding 2/5 + 1/5 is drawn as one bar split into 5 equal parts, shading 2 parts then 1 more part, giving 3 shaded parts out of 5, so the sum 3/5 is seen directly rather than just computed.",
        "example": table(["Bar Split Into", "Parts Shaded", "Sum"], [["5", "2 then 1 more", "3/5"]]),
    },
    "math-g4-l20": {
        "method": "Bar Model (Multi-Step Word Problems)",
        "explanation": "This is the signature Singapore technique: a word problem with multiple steps is translated into a diagram of bars representing each quantity and how they relate, so the correct sequence of operations becomes visible before any calculation starts.",
        "example": table(["Step", "Bar Model Action"], [["1", "Draw a bar for the known total"], ["2", "Split it into labeled parts for each unknown"], ["3", "Use the visible gaps between bars to find the missing value"]]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in SINGAPORE_MATH if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Math: {missing}")

    updated = 0
    for lid, content in SINGAPORE_MATH.items():
        lesson = by_id[lid]
        if "singapore_math" not in lesson:
            lesson["singapore_math"] = content
            updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added Singapore Math content to {updated} Grade 4 Math lessons.")


if __name__ == "__main__":
    main()
