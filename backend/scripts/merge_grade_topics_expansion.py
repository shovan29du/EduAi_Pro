#!/usr/bin/env python3
"""Merge grade_topics_g*.py module files into grade1.json..grade10.json,
bringing every subject up toward its grade-tier lesson-count target:

    Grades 1-4:  20 lessons/subject
    Grades 5-6:  30 lessons/subject
    Grades 7-8:  40 lessons/subject
    Grades 9-10: 50 lessons/subject

Each contributing file (grade_topics_g<N>.py) defines:

    GRADE: int
    MODULES: dict[str, list[tuple[str, str]]]   # MODULES[subject] = [(title, summary), ...]

Re-run any time after adding/editing a grade_topics_g*.py file:
    python3 backend/scripts/merge_grade_topics_expansion.py
"""
from __future__ import annotations

import importlib
import json
import pkgutil
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"
SCRIPTS_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS_DIR))
from grade_lesson_builder import build_grade_lesson, next_grade_lesson_index  # noqa: E402

TARGET_BY_GRADE = {
    1: 20, 2: 20, 3: 20, 4: 20,
    5: 30, 6: 30,
    7: 40, 8: 40,
    9: 50, 10: 50,
}


def load_grade_module_files() -> dict[int, dict[str, list[tuple]]]:
    combined: dict[int, dict[str, list[tuple]]] = {}
    for finder, name, ispkg in pkgutil.iter_modules([str(SCRIPTS_DIR)]):
        if not name.startswith("grade_topics_g"):
            continue
        mod = importlib.import_module(name)
        grade = getattr(mod, "GRADE", None)
        modules = getattr(mod, "MODULES", {})
        if grade is None:
            continue
        combined.setdefault(grade, {})
        for subject, topics in modules.items():
            combined[grade].setdefault(subject, [])
            combined[grade][subject].extend(topics)
    return combined


def main() -> None:
    all_modules = load_grade_module_files()
    print(f"Loaded grade topic modules for grades: {sorted(all_modules.keys())}")

    report: dict[str, int] = {}
    for grade, per_subject in all_modules.items():
        path = SYLLABUS_DIR / f"grade{grade}.json"
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        subjects = data["subjects"]
        target = TARGET_BY_GRADE.get(grade, 20)

        for subject, topics in per_subject.items():
            if subject not in subjects:
                continue
            content = subjects[subject]
            lessons = content.setdefault("lessons", [])
            existing_titles = {l.get("title") for l in lessons}
            idx = next_grade_lesson_index(lessons)

            added = 0
            for title, summary in topics:
                if len(lessons) >= target:
                    break
                if title in existing_titles:
                    continue
                lessons.append(build_grade_lesson(subject, grade, idx, title, summary))
                existing_titles.add(title)
                idx += 1
                added += 1

            quiz_bank = content.setdefault("quiz_bank", [])
            existing_qs = {q.get("question") for q in quiz_bank}
            for title, summary in topics[:4]:
                q = f"What is the focus of the '{title}' lesson?"
                if q in existing_qs:
                    continue
                first_sentence = summary.split(".")[0].strip() + "."
                quiz_bank.append({
                    "question": q,
                    "type": "multiple_choice",
                    "options": [first_sentence, "Not part of this subject at this grade",
                                "A topic covered only in an earlier grade", "None of the above"],
                    "answer": first_sentence,
                })
                existing_qs.add(q)

            key = f"Grade {grade}: {subject}"
            report[key] = added

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print("Lessons added per grade/subject:")
    for key, count in sorted(report.items()):
        print(f"  {key}: +{count}")

    print("\nFinal lesson counts:")
    for grade in sorted(all_modules.keys()):
        path = SYLLABUS_DIR / f"grade{grade}.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        counts = {name: len(content.get("lessons", [])) for name, content in data["subjects"].items()}
        print(f"  Grade {grade}: {counts}")


if __name__ == "__main__":
    main()
