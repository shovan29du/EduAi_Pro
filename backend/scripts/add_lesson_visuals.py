#!/usr/bin/env python3
"""Add lesson-specific visuals to every lesson across all syllabus files:

1. `figure` -- a concept-flow diagram (SubjectLessons.jsx already renders
   `figure.nodes` as a chain of boxes). Built from the lesson's own existing
   `key_concepts` list, not invented -- just reformatted. A quality filter
   drops stopwords/short fragments and skips the lesson entirely if fewer
   than 3 usable concepts remain, rather than showing a garbled diagram.

2. `wiki_title` -- best-effort guess (the lesson title, lightly cleaned) for
   a live Wikipedia thumbnail lookup on the frontend (same honest
   "real photo or nothing" pattern already used for the Virtual Museum,
   Cuisine Centre, and Herbs & Spices -- a live fetch that gracefully shows
   nothing if no matching real Wikipedia page/thumbnail exists, never a
   fabricated image).

This intentionally does NOT add `data_table`, `graph`, or `formulae` --
those need genuinely accurate subject content and are added by hand, lesson
by lesson, in a separate pass (see backend/scripts/add_math_lesson_charts.py
for the Grade 5 Math pilot).

Idempotent: safe to re-run after editing.

Re-run after editing:
    python3 backend/scripts/add_lesson_visuals.py
"""
from __future__ import annotations

import glob
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"

STOPWORDS = {
    "with", "and", "the", "of", "for", "a", "an", "in", "on", "to", "at",
    "or", "but", "is", "as", "your", "their", "its", "into", "from", "by",
}


def clean_wiki_title(title: str) -> str:
    # Strip a leading "Introduction to " / "Overview of " style prefix,
    # which usually maps better to the underlying topic's real Wikipedia page.
    cleaned = re.sub(r"^(Introduction to|Overview of|Basics of|Understanding)\s+", "", title, flags=re.IGNORECASE)
    return cleaned.strip()


def build_figure(lesson: dict) -> dict | None:
    concepts = lesson.get("key_concepts") or []
    filtered = [c for c in concepts if isinstance(c, str) and c.lower() not in STOPWORDS and len(c) >= 3]
    # Drop exact-duplicate concepts while preserving order.
    seen = set()
    deduped = []
    for c in filtered:
        key = c.lower()
        if key not in seen:
            seen.add(key)
            deduped.append(c)
    if len(deduped) < 3:
        return None
    nodes = deduped[:6]
    return {"caption": f"Key concepts in “{lesson.get('title', '')}”", "nodes": nodes}


def process_file(path: Path) -> tuple[int, int]:
    data = json.loads(path.read_text(encoding="utf-8"))
    figures_added = 0
    titles_added = 0
    for subject in data.get("subjects", {}).values():
        for lesson in subject.get("lessons", []):
            if "figure" not in lesson:
                figure = build_figure(lesson)
                if figure:
                    lesson["figure"] = figure
                    figures_added += 1
            if "wiki_title" not in lesson and lesson.get("title"):
                lesson["wiki_title"] = clean_wiki_title(lesson["title"])
                titles_added += 1
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    return figures_added, titles_added


def main() -> None:
    total_figures = 0
    total_titles = 0
    total_lessons = 0
    for path_str in sorted(glob.glob(str(SYLLABUS_DIR / "*.json"))):
        path = Path(path_str)
        figures, titles = process_file(path)
        data = json.loads(path.read_text(encoding="utf-8"))
        lesson_count = sum(len(s.get("lessons", [])) for s in data.get("subjects", {}).values())
        total_lessons += lesson_count
        total_figures += figures
        total_titles += titles
        print(f"{path.name}: {lesson_count} lessons, +{figures} figures, +{titles} wiki_titles")

    print(f"\nTotal: {total_lessons} lessons across all files.")
    print(f"Added {total_figures} concept-flow figures ({total_figures * 100 // total_lessons}% of lessons).")
    print(f"Added {total_titles} wiki_title fields for live thumbnail lookup.")


if __name__ == "__main__":
    main()
