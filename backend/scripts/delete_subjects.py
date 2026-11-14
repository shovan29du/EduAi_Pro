#!/usr/bin/env python3
"""Delete a set of subjects entirely from every syllabus file (Grade 1
through Master's 1), per an explicit user request to remove Business
Studies, Environmental Science, World Politics, World Religion, and
Civics from the curriculum.

Re-run after editing:
    python3 backend/scripts/delete_subjects.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"

FILES = [f"grade{g}.json" for g in range(1, 11)] + [
    "level_c1.json", "level_c2.json", "level_ug1.json", "level_ug2.json",
    "level_ug3.json", "level_ug4.json", "level_m1.json", "level_m2.json",
]

SUBJECTS_TO_DELETE = [
    "Business Studies",
    "Environmental Science",
    "World Politics",
    "World Religion",
    "Civics",
]


def main() -> None:
    for fname in FILES:
        path = SYLLABUS_DIR / fname
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        subjects = data.get("subjects", data)
        removed = []
        for subject in SUBJECTS_TO_DELETE:
            if subject in subjects:
                del subjects[subject]
                removed.append(subject)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"{fname}: removed {removed}")


if __name__ == "__main__":
    main()
