#!/usr/bin/env python3
"""Curriculum benchmarking, College/Grad levels: appends curated Ivy
League and top-program links to every subject's existing
`external_courses` array at C1, C2, M1, M2, UG1-4, alongside the
existing Udemy/Coursera/edX/MIT OCW/Harvard Online/Pinterest entries
(never removed or reordered).

Idempotent: for each subject, only appends a source that isn't already
present (matched by the "source" field), so re-running is a no-op once
applied.

Re-run after editing:
    python3 backend/scripts/add_ivy_league_benchmark_links.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"

LEVELS = ["c1", "c2", "m1", "m2", "ug1", "ug2", "ug3", "ug4"]


def ivy_league_links(subject_name: str) -> list[dict]:
    query = quote_plus(subject_name)
    return [
        {
            "title": "Stanford Online — course catalog",
            "url": "https://online.stanford.edu/courses",
            "source": "Stanford Online",
            "safe": True,
        },
        {
            "title": "Open Yale Courses",
            "url": "https://oyc.yale.edu/courses",
            "source": "Open Yale Courses",
            "safe": True,
        },
        {
            "title": f"Wharton (University of Pennsylvania) — course search for {subject_name}",
            "url": f"https://www.coursera.org/search?query={query}+Wharton",
            "source": "Wharton School",
            "safe": True,
        },
        {
            "title": f"Princeton — course search for {subject_name}",
            "url": f"https://www.edx.org/search?q={query}+Princeton",
            "source": "Princeton University",
            "safe": True,
        },
    ]


def main() -> None:
    updated_subjects = 0
    for level in LEVELS:
        path = SYLLABUS_DIR / f"level_{level}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        subjects = data["subjects"]
        changed = False

        for subject_name, subject in subjects.items():
            existing = subject.get("external_courses")
            if not existing:
                continue
            existing_sources = {item.get("source") for item in existing}
            additions = [link for link in ivy_league_links(subject_name) if link["source"] not in existing_sources]
            if additions:
                subject["external_courses"] = existing + additions
                updated_subjects += 1
                changed = True

        if changed:
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
            print(f"{level.upper()}: updated")

    print(f"Total subjects updated with Ivy League benchmark links: {updated_subjects}")


if __name__ == "__main__":
    main()
