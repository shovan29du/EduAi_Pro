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

    # Load every level upfront so title uniqueness can be enforced PER SUBJECT
    # ACROSS ALL LEVELS, not just within the level currently being merged. A
    # subject's topics are often split across several college_topics_g*.py
    # files written independently (one per wave/level), so without a global
    # check the same title can slip in at two different levels. Checking
    # globally -- and updating the shared set immediately as titles are added
    # -- also makes re-running this script safely idempotent.
    level_data: dict[str, dict] = {}
    for level in LEVEL_IDS:
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        if path.exists():
            with open(path, encoding="utf-8") as f:
                level_data[level] = json.load(f)

    global_titles: dict[str, set[str]] = {}
    for data in level_data.values():
        for subject, content in data["subjects"].items():
            titles = global_titles.setdefault(subject, set())
            for lesson in content.get("lessons", []):
                titles.add(lesson.get("title"))

    report: dict[str, int] = {}
    for level in LEVEL_IDS:
        data = level_data.get(level)
        if data is None:
            continue
        subjects = data["subjects"]

        for subject, per_level in all_modules.items():
            topics = per_level.get(level, [])
            if not topics or subject not in subjects:
                continue
            content = subjects[subject]
            lessons = content.setdefault("lessons", [])
            existing_titles = global_titles.setdefault(subject, set())
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

    for level, data in level_data.items():
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
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


def dedupe_cross_level_titles() -> None:
    """One-off cleanup utility -- NOT called automatically by main().

    Different waves/agents occasionally land on the same topic title for a
    subject at two different levels (they only have visibility into their own
    level's existing titles, not every other level's). This scans every
    subject across all 8 college levels and renames any duplicate title's
    earlier-level occurrence(s) with a " — Foundations" style suffix so titles
    stay unique.

    IMPORTANT: this only renames titles in the syllabus JSON, not in the
    college_topics_g*.py source files. Since main()'s merge loop now enforces
    title uniqueness per subject ACROSS ALL LEVELS (not just the level being
    merged), re-running main() after this cleanup will NOT reintroduce the
    renamed-away originals, as long as no topic file still claims that exact
    title as new content to merge into a level that doesn't have it yet. Run
    this after a merge if the new invariant test flags leftover duplicates
    from before this fix existed; it should rarely be needed going forward.
    """
    level_data = {}
    for level in LEVEL_IDS:
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        with open(path, encoding="utf-8") as f:
            level_data[level] = json.load(f)

    subjects = set()
    for level in LEVEL_IDS:
        subjects.update(level_data[level]["subjects"].keys())

    renamed = 0
    touched_levels = set()
    for subject in sorted(subjects):
        occurrences = []  # (level_index, level, lesson_dict)
        all_titles_in_subject = set()
        for i, level in enumerate(LEVEL_IDS):
            lessons = level_data[level]["subjects"].get(subject, {}).get("lessons", [])
            for lesson in lessons:
                occurrences.append((i, level, lesson))
                all_titles_in_subject.add(lesson["title"])

        by_title: dict[str, list[tuple[int, str, dict]]] = {}
        for occ in occurrences:
            by_title.setdefault(occ[2]["title"], []).append(occ)

        for title, occs in by_title.items():
            if len(occs) < 2:
                continue
            occs.sort(key=lambda o: o[0])
            # Keep the last (most advanced level) occurrence's title as-is;
            # rename every earlier occurrence to a distinct, unique title.
            for occ_i, (_, level, lesson) in enumerate(occs[:-1]):
                suffix = " — Foundations" if occ_i == 0 else f" — Foundations {occ_i + 1}"
                candidate = title + suffix
                while candidate in all_titles_in_subject:
                    occ_i += 1
                    candidate = title + f" — Foundations {occ_i + 1}"
                if lesson.get("unit") == lesson["title"]:
                    lesson["unit"] = candidate
                lesson["title"] = candidate
                all_titles_in_subject.add(candidate)
                touched_levels.add(level)
                renamed += 1

    for level in touched_levels:
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(level_data[level], f, indent=2, ensure_ascii=False)

    if renamed:
        print(f"\nDeduped {renamed} cross-level duplicate lesson titles across {len(touched_levels)} level file(s).")
    else:
        print("\nNo cross-level duplicate lesson titles found.")


if __name__ == "__main__":
    main()
