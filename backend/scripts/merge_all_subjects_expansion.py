#!/usr/bin/env python3
"""Merge topic-module files into the college-level syllabus (C1 through
M1), bringing every listed subject up toward 20+ lessons per level.

Each contributing file (college_topics_g*.py) defines:

    MODULES: dict[str, dict[str, list[tuple[str, str]]]]
    # MODULES[subject_name][level_id] = [(title, summary), ...]

This script imports every college_topics_g*.py module it finds next to
it, and for each (subject, level, topics) merges the topics into that
subject's "lessons" list at that level, deduping by title and continuing
id numbering from the highest existing lesson index. Also extends the
quiz_bank and real_world_examples the same way the earlier college
module scripts did.

Re-run any time after adding/editing a college_topics_g*.py file:
    python3 backend/scripts/merge_all_subjects_expansion.py
"""
from __future__ import annotations

import importlib
import json
import pkgutil
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"
SCRIPTS_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS_DIR))
from generate_advanced_curriculum import LEVEL_IDS, _lesson_for  # noqa: E402


def load_all_module_files() -> dict[str, dict[str, list[tuple]]]:
    combined: dict[str, dict[str, list[tuple]]] = {}
    for finder, name, ispkg in pkgutil.iter_modules([str(SCRIPTS_DIR)]):
        if not name.startswith("college_topics_g"):
            continue
        mod = importlib.import_module(name)
        modules = getattr(mod, "MODULES", {})
        for subject, per_level in modules.items():
            combined.setdefault(subject, {})
            for level, topics in per_level.items():
                combined[subject].setdefault(level, [])
                combined[subject][level].extend(topics)
    return combined


def next_lesson_index(lessons: list[dict]) -> int:
    max_idx = 0
    for lesson in lessons:
        m = re.search(r"-l(\d+)$", lesson.get("id", ""))
        if m:
            max_idx = max(max_idx, int(m.group(1)))
    return max_idx + 1


def main() -> None:
    all_modules = load_all_module_files()
    print(f"Loaded topic modules for {len(all_modules)} subjects from college_topics_g*.py files.")

    report: dict[str, int] = {}
    for level in LEVEL_IDS:
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        subjects = data["subjects"]

        for subject, per_level in all_modules.items():
            topics = per_level.get(level, [])
            if not topics or subject not in subjects:
                continue
            content = subjects[subject]
            lessons = content.setdefault("lessons", [])
            existing_titles = {l.get("title") for l in lessons}
            idx = next_lesson_index(lessons)

            added = 0
            for title, summary in topics:
                if title in existing_titles:
                    continue
                lessons.append(_lesson_for(subject, level, idx, title, summary))
                existing_titles.add(title)
                idx += 1
                added += 1

            quiz_bank = content.setdefault("quiz_bank", [])
            existing_qs = {q.get("question") for q in quiz_bank}
            for title, summary in topics[:4]:
                q = f"What is the focus of the '{title}' module?"
                if q in existing_qs:
                    continue
                quiz_bank.append({
                    "question": q,
                    "type": "multiple_choice",
                    "options": [summary, "Not part of this subject at this level",
                                "A topic covered only in an earlier level", "None of the above"],
                    "answer": summary,
                })
                existing_qs.add(q)

            report[subject] = report.get(subject, 0) + added

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print("Lessons added per subject (across all levels present in the topic files):")
    for subject, count in sorted(report.items()):
        print(f"  {subject}: +{count}")

    # Report current totals per subject per level.
    print("\nCurrent lessons-per-level for touched subjects:")
    for subject in sorted(all_modules.keys()):
        counts = []
        for level in LEVEL_IDS:
            path = SYLLABUS_DIR / f"level_{level.lower()}.json"
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            n = len(data["subjects"].get(subject, {}).get("lessons", []))
            counts.append(f"{level}:{n}")
        print(f"  {subject}: {' '.join(counts)}")


if __name__ == "__main__":
    main()
