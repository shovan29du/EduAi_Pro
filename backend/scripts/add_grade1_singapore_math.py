#!/usr/bin/env python3
"""Singapore Math integration, Grade 1: adds a `singapore_math` field to
Math lessons where Singapore's Ministry of Education (MOE) Primary
Mathematics methodology -- number bonds and the Concrete-Pictorial-
Abstract (CPA) approach -- genuinely applies. This supplements the
existing Math curriculum; it does not replace any existing content.

Idempotent: only fills in the field where it isn't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_singapore_math.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


SINGAPORE_MATH: dict[str, dict] = {
    "math-g1-l3": {
        "method": "Number Bonds",
        "explanation": "Singapore's Primary Math syllabus teaches addition through number bonds: splitting a number into two parts that combine to make a whole. To add 4 + 3, first see that 3 splits into 1 and 2, so 4 + 1 makes 5 (a friendly 'ten frame' anchor), then 5 + 2 = 7.",
        "example": table(["Bond", "Sum"], [["4 and 3 make", "7"], ["Split 3 into 1 + 2", "4 + 1 = 5, then 5 + 2 = 7"]]),
    },
    "math-g1-l4": {
        "method": "Number Bonds",
        "explanation": "Subtraction is taught as 'the missing part' of a number bond. If 9 is the whole and 4 is one part, the number bond shows the other part must be 5, so 9 - 4 = 5.",
        "example": table(["Whole", "Known Part", "Missing Part"], [["9", "4", "5"]]),
    },
    "math-g1-l13": {
        "method": "Number Bonds — Making Ten",
        "explanation": "For addition beyond 10, Singapore Math uses the 'make a ten' strategy: 8 + 5 becomes 8 + 2 (to make 10) + 3 remaining, giving 10 + 3 = 13.",
        "example": table(["Step", "Result"], [["8 + 2 (make ten)", "10"], ["10 + 3 (remaining)", "13"]]),
    },
    "math-g1-l14": {
        "method": "Number Bonds — Subtracting from Ten",
        "explanation": "For subtraction across 10, break the larger number into 10 and the rest: 14 - 6 becomes 10 - 6 = 4, then 4 + 4 (the leftover from 14) = 8.",
        "example": table(["Step", "Result"], [["14 = 10 + 4", "split the whole"], ["10 - 6 = 4, then 4 + 4", "8"]]),
    },
    "math-g1-l15": {
        "method": "Number Bonds to 10",
        "explanation": "Number bonds to 10 are the foundation of Singapore's mental math: every pair of numbers that sums to 10 (0+10, 1+9, 2+8, 3+7, 4+6, 5+5) is memorized as a single visual bond so later addition and subtraction become instant recall rather than counting.",
        "example": table(["Part", "Part", "Whole"], [["3", "7", "10"], ["4", "6", "10"], ["5", "5", "10"]]),
    },
    "math-g1-l16": {
        "method": "Concrete-Pictorial-Abstract (CPA)",
        "explanation": "Place value is introduced with the CPA approach: first with physical base-ten blocks (concrete), then a drawing of tens-sticks and ones-dots (pictorial), and finally the digits themselves (abstract) -- e.g. 23 is shown as 2 ten-rods and 3 unit-cubes before it is written as '23'.",
        "example": table(["Stage", "Representation of 23"], [["Concrete", "2 ten-rods + 3 unit-cubes"], ["Pictorial", "2 long bars + 3 dots"], ["Abstract", "23"]]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in SINGAPORE_MATH if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json Math: {missing}")

    updated = 0
    for lid, content in SINGAPORE_MATH.items():
        lesson = by_id[lid]
        if "singapore_math" not in lesson:
            lesson["singapore_math"] = content
            updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added Singapore Math content to {updated} Grade 1 Math lessons.")


if __name__ == "__main__":
    main()
