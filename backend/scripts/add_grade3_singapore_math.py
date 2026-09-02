#!/usr/bin/env python3
"""Singapore Math integration, Grade 3: adds a `singapore_math` field to
Math lessons where Singapore's MOE Primary Mathematics methodology --
the model (bar) method and number bonds -- applies. Supplements the
existing Math curriculum without replacing it.

Idempotent: only fills in the field where it isn't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_singapore_math.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


SINGAPORE_MATH: dict[str, dict] = {
    "math-g3-l1": {
        "method": "Bar Model (Repeated Groups)",
        "explanation": "Multiplication tables are reinforced with equal-length bars: 6 x 7 is drawn as 6 bars of 7 units each (or 7 bars of 6 units), so students see the table fact as a picture, not just a memorized number.",
        "example": table(["Bars", "Units Each", "Total"], [["6", "7", "42"]]),
    },
    "math-g3-l2": {
        "method": "Bar Model (Sharing Equally)",
        "explanation": "Long division builds on the sharing-bar model from Grade 2: dividing 84 by 4 is shown as one long bar of 84 split into 4 equal sections, each worked out to be 21.",
        "example": table(["Total", "Groups", "Each Group"], [["84", "4", "21"]]),
    },
    "math-g3-l3": {
        "method": "Bar Model (Fraction Comparison)",
        "explanation": "To compare 2/3 and 3/4, Singapore Math draws two equal-length bars, one split into 3 parts (shading 2) and one split into 4 parts (shading 3), so the relative sizes are visible before any cross-multiplication.",
        "example": table(["Fraction", "Bar Divided Into", "Parts Shaded"], [["2/3", "3", "2"], ["3/4", "4", "3"]]),
    },
    "math-g3-l8": {
        "method": "Number Bonds — Regrouping",
        "explanation": "Addition with regrouping uses number bonds to show carrying: adding 47 + 38, the ones (7+8=15) bond into 1 ten and 5 ones, so the extra ten is regrouped into the tens column.",
        "example": table(["Column", "Sum", "Regroup"], [["Ones: 7 + 8", "15", "carry 1 ten, keep 5"], ["Tens: 4 + 3 + 1", "8", "no further carry"]]),
    },
    "math-g3-l9": {
        "method": "Number Bonds — Regrouping",
        "explanation": "Subtraction with regrouping uses a number bond to 'borrow': for 52 - 27, the tens digit lends a ten to the ones column, turning 52 into 4 tens and 12 ones so 12 - 7 = 5 becomes possible.",
        "example": table(["Step", "Result"], [["Regroup 52 as", "4 tens + 12 ones"], ["12 - 7, then 4 - 2", "5 and 2, giving 25"]]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in SINGAPORE_MATH if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Math: {missing}")

    updated = 0
    for lid, content in SINGAPORE_MATH.items():
        lesson = by_id[lid]
        if "singapore_math" not in lesson:
            lesson["singapore_math"] = content
            updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added Singapore Math content to {updated} Grade 3 Math lessons.")


if __name__ == "__main__":
    main()
