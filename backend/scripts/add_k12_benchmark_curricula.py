#!/usr/bin/env python3
"""Curriculum benchmarking, Grades 1-10: adds `external_courses` entries
to Math and the Science family (Science, Physics, Chemistry, Biology)
citing the specific benchmark curricula requested -- Singapore MOE and
MIT OpenCourseWare for Math; IB, AP, and Khan Academy for the sciences.

These reuse the existing `external_courses` subject field and its
"More Courses" tab in SubjectLessons.jsx (already used at C1-M2/UG
levels), so no frontend change is required -- the links simply appear
in that tab for these K-12 subjects for the first time.

Idempotent: only adds a source if that subject doesn't already carry
external_courses (never overwrites or duplicates existing entries).

Re-run after editing:
    python3 backend/scripts/add_k12_benchmark_curricula.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"

MATH_BENCHMARKS = [
    {
        "title": "Singapore MOE — Mathematics Syllabuses",
        "url": "https://www.moe.gov.sg/education-in-sg/syllabuses",
        "source": "Singapore MOE",
        "safe": True,
    },
    {
        "title": "MIT OpenCourseWare — Mathematics",
        "url": "https://ocw.mit.edu/search/?q=mathematics",
        "source": "MIT OpenCourseWare",
        "safe": True,
    },
    {
        "title": "Khan Academy — Math",
        "url": "https://www.khanacademy.org/math",
        "source": "Khan Academy",
        "safe": True,
    },
]

SCIENCE_BENCHMARKS_BY_SUBJECT = {
    "Science": "science",
    "Physics": "physics",
    "Chemistry": "chemistry",
    "Biology": "biology",
}


def science_benchmarks(subject_name: str) -> list[dict]:
    query = SCIENCE_BENCHMARKS_BY_SUBJECT[subject_name]
    return [
        {
            "title": "IB Diploma Programme — Sciences Curriculum",
            "url": "https://www.ibo.org/programmes/diploma-programme/curriculum/",
            "source": "IB",
            "safe": True,
        },
        {
            "title": f"AP {subject_name} — College Board",
            "url": "https://apstudents.collegeboard.org/courses",
            "source": "AP",
            "safe": True,
        },
        {
            "title": f"Khan Academy — {subject_name}",
            "url": f"https://www.khanacademy.org/{query}",
            "source": "Khan Academy",
            "safe": True,
        },
    ]


def main() -> None:
    updated_subjects = 0
    for grade in range(1, 11):
        path = SYLLABUS_DIR / f"grade{grade}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        subjects = data["subjects"]
        changed = False

        if "Math" in subjects and not subjects["Math"].get("external_courses"):
            subjects["Math"]["external_courses"] = list(MATH_BENCHMARKS)
            updated_subjects += 1
            changed = True

        for subject_name in SCIENCE_BENCHMARKS_BY_SUBJECT:
            if subject_name in subjects and not subjects[subject_name].get("external_courses"):
                subjects[subject_name]["external_courses"] = science_benchmarks(subject_name)
                updated_subjects += 1
                changed = True

        if changed:
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
            print(f"Grade {grade}: updated")

    print(f"Total subjects updated with benchmark curricula: {updated_subjects}")


if __name__ == "__main__":
    main()
