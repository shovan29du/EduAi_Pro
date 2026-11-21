#!/usr/bin/env python3
"""Merge the expanded college-subject module topics into the college-level
syllabus files (level_c1.json .. level_m2.json), giving each of the seven
requested subjects -- Environmental Science, World Politics, World
Religion, Economics, Health Education, Business Studies, and Civics -- at
least 50-100 lessons across College 1 through Masters 2 (8 bespoke modules
per level x 8 levels = 64 lessons per subject, plus whatever each subject
already had).

Module topic lists live in college_subject_modules_a.py (Environmental
Science, World Politics, World Religion) and college_subject_modules_b.py
(Economics, Health Education, Business Studies, Civics). Lessons are built
with the same _lesson_for/_subject_content machinery as the main
curriculum generator, so the schema matches existing lessons exactly.

Idempotent: lessons are deduped by title within each subject/level, and
lesson ids continue from the highest existing index.

Re-run after editing:
    python3 backend/scripts/merge_college_subject_expansion.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"

sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_advanced_curriculum import (  # noqa: E402
    LEVEL_IDS,
    _lesson_for,
    _subject_content,
)
from college_subject_modules_a import MODULES as MODULES_A  # noqa: E402
from college_subject_modules_b import MODULES as MODULES_B  # noqa: E402

ALL_MODULES: dict[str, dict[str, list[tuple[str, str]]]] = {**MODULES_A, **MODULES_B}


def next_lesson_index(lessons: list[dict], subject: str, level: str) -> int:
    """Find the highest existing -l<N> suffix so new ids don't collide."""
    max_idx = 0
    for lesson in lessons:
        m = re.search(r"-l(\d+)$", lesson.get("id", ""))
        if m:
            max_idx = max(max_idx, int(m.group(1)))
    return max_idx + 1


def main() -> None:
    report = {}
    for level in LEVEL_IDS:
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        subjects = data["subjects"]

        for subject, per_level in ALL_MODULES.items():
            modules = per_level.get(level, [])
            if not modules:
                continue

            if subject not in subjects:
                # Brand-new subject (World Religion): build full content from
                # this level's modules.
                subjects[subject] = _subject_content(subject, level, modules)
                report[subject] = report.get(subject, 0) + len(subjects[subject]["lessons"])
                continue

            content = subjects[subject]
            lessons = content.setdefault("lessons", [])
            existing_titles = {l.get("title") for l in lessons}
            idx = next_lesson_index(lessons, subject, level)

            added = 0
            for title, summary in modules:
                if title in existing_titles:
                    continue
                lessons.append(_lesson_for(subject, level, idx, title, summary))
                existing_titles.add(title)
                idx += 1
                added += 1

            # Extend the quiz bank and real-world examples with the new
            # modules (deduped by question / example text).
            quiz_bank = content.setdefault("quiz_bank", [])
            existing_qs = {q.get("question") for q in quiz_bank}
            for title, summary in modules[:4]:
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

            examples = content.setdefault("real_world_examples", [])
            existing_examples = set(examples)
            for title, summary in modules[:2]:
                ex = f"How '{title}' shows up in real-world {subject.lower()} practice: {summary}"
                if ex not in existing_examples:
                    examples.append(ex)
                    existing_examples.add(ex)

            report[subject] = report.get(subject, 0) + added

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print("Lessons added per subject (across all college levels):")
    for subject, count in sorted(report.items()):
        print(f"  {subject}: +{count}")

    # Verify final totals per subject across college levels.
    totals: dict[str, int] = {}
    for level in LEVEL_IDS:
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        for subject in ALL_MODULES:
            if subject in data["subjects"]:
                totals[subject] = totals.get(subject, 0) + len(data["subjects"][subject].get("lessons", []))
    print("Total lessons per subject across C1-M2:")
    for subject, count in sorted(totals.items()):
        status = "OK" if count >= 50 else "UNDER 50!"
        print(f"  {subject}: {count} ({status})")


if __name__ == "__main__":
    main()
