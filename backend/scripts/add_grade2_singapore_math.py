#!/usr/bin/env python3
"""Singapore Math integration, Grade 2: adds a `singapore_math` field to
Math lessons where Singapore's MOE Primary Mathematics methodology --
number bonds, the model (bar) method, and the CPA approach -- applies.
Supplements the existing Math curriculum without replacing it.

Idempotent: only fills in the field where it isn't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_singapore_math.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


SINGAPORE_MATH: dict[str, dict] = {
    "math-g2-l1": {
        "method": "Concrete-Pictorial-Abstract (CPA)",
        "explanation": "Place value continues with base-ten blocks: 47 is shown as 4 ten-rods and 7 unit-cubes (concrete), then drawn as 4 bars and 7 dots (pictorial), before being read as the digits '4' tens and '7' ones (abstract).",
        "example": table(["Stage", "Representation of 47"], [["Concrete", "4 ten-rods + 7 unit-cubes"], ["Abstract", "4 tens + 7 ones = 47"]]),
    },
    "math-g2-l2": {
        "method": "Number Bonds — Making Ten",
        "explanation": "Adding within 100 still uses the 'make a ten' bond: 38 + 15 becomes 38 + 2 (to make 40) + 13 remaining, giving 40 + 13 = 53.",
        "example": table(["Step", "Result"], [["38 + 2 (make 40)", "40"], ["40 + 13 (remaining)", "53"]]),
    },
    "math-g2-l3": {
        "method": "Number Bonds",
        "explanation": "Subtracting within 100 uses number bonds to break the number apart: 72 - 25 becomes 72 - 20 - 5 = 52 - 5 = 47, splitting the subtrahend into a tens part and a ones part.",
        "example": table(["Step", "Result"], [["72 - 20", "52"], ["52 - 5", "47"]]),
    },
    "math-g2-l4": {
        "method": "Bar Model (Equal Groups)",
        "explanation": "Multiplication is introduced as equal groups drawn as bars of the same length: 3 groups of 4 are shown as three equal bars, each divided into 4 units, so 3 x 4 = 12.",
        "example": table(["Groups", "Size Each", "Total"], [["3 bars", "4 units", "12"]]),
    },
    "math-g2-l5": {
        "method": "Bar Model (Partitioning a Whole)",
        "explanation": "Fractions are introduced by drawing one bar representing the whole and dividing it into equal parts: for halves, the bar splits into 2 equal parts, and 1 shaded part is 1/2.",
        "example": table(["Whole Bar Divided Into", "Fraction of 1 Part"], [["2 equal parts", "1/2"], ["4 equal parts", "1/4"]]),
    },
    "math-g2-l8": {
        "method": "Bar Model (Sharing Equally)",
        "explanation": "Division is shown as one bar split into equal groups: sharing 12 into 3 equal groups is drawn as a bar of 12 units divided into 3 equal sections, each of 4, so 12 / 3 = 4.",
        "example": table(["Total", "Groups", "Each Group"], [["12", "3", "4"]]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in SINGAPORE_MATH if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json Math: {missing}")

    updated = 0
    for lid, content in SINGAPORE_MATH.items():
        lesson = by_id[lid]
        if "singapore_math" not in lesson:
            lesson["singapore_math"] = content
            updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added Singapore Math content to {updated} Grade 2 Math lessons.")


if __name__ == "__main__":
    main()
