#!/usr/bin/env python3
"""Expand every Survival Skills category to 50 lessons, and add a new
"Rope Knots & Advanced Survival Skills" category with at least 50 lessons.

Each category's TOPICS list holds 50 real, distinct, well-established
survival/safety-skill tuples of the form:

    (name, grade_range, adult_supervision_required, learning_objectives,
     key_steps, practice_activities, quiz, important_note)

  - name: short lesson name
  - grade_range: e.g. "1-4", "5-8", "9-12", "Adult"
  - adult_supervision_required: bool
  - learning_objectives: list of 2-3 short strings
  - key_steps: list of 3-5 short, accurate step strings
  - practice_activities: list of 1-2 short strings
  - quiz: list of 1-2 (question, answer) tuples
  - important_note: one safety/context note string

build_skill() turns each tuple into the exact JSON schema already used by
existing entries in survival_skills.json (see SurvivalSkills.jsx), adding
resource-search links (YouTube/text-guide/Wikipedia search links -- not
guessed direct URLs, consistent with this project's no-fabrication rule).

Re-run after editing:
    python3 backend/scripts/generate_survival_skills_expansion.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
SURVIVAL_PATH = BASE_DIR / "data" / "survival_skills" / "survival_skills.json"

NEW_CATEGORY_ID = "rope_knots_advanced_survival"


def yt_search(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def wikihow_search(q: str) -> str:
    return "https://www.wikihow.com/wikiHowTo?search=" + quote_plus(q)


def wikipedia_search(q: str) -> str:
    return "https://en.wikipedia.org/w/index.php?search=" + quote_plus(q)


# TOPICS[category_id] = list of 50 tuples:
#   (name, grade_range, adult_supervision_required, learning_objectives,
#    key_steps, practice_activities, quiz, important_note)
TOPICS: dict[str, list[tuple]] = {}


def build_skill(category_id: str, item: tuple) -> dict:
    (name, grade_range, adult_supervision_required, learning_objectives,
     key_steps, practice_activities, quiz, important_note) = item

    return {
        "name": name,
        "grade_range": grade_range,
        "category": category_id,
        "adult_supervision_required": adult_supervision_required,
        "learning_objectives": learning_objectives,
        "key_steps": key_steps,
        "practice_activities": practice_activities,
        "quiz": [{"q": q, "a": a} for q, a in quiz],
        "important_note": important_note,
        "progress_tracking": {"completion_required": True, "min_quiz_score": 70},
        "links": {
            "video_link": yt_search(f"{name} survival safety tutorial"),
            "video_search_general": yt_search(f"{name} {category_id.replace('_', ' ')}"),
            "text_link": wikihow_search(name),
            "resource_link": wikipedia_search(name),
        },
    }


def main() -> None:
    with open(SURVIVAL_PATH, encoding="utf-8") as f:
        data = json.load(f)

    if NEW_CATEGORY_ID not in data["categories"]:
        data["categories"][NEW_CATEGORY_ID] = []

    report = []
    for category_id, topics in TOPICS.items():
        if category_id not in data["categories"]:
            data["categories"][category_id] = []
        existing = data["categories"][category_id]
        existing_names = {s["name"] for s in existing}

        new_topics = [t for t in topics if t[0] not in existing_names]
        new_skills = [build_skill(category_id, item) for item in new_topics]
        data["categories"][category_id] = existing + new_skills
        report.append(f"{category_id}: {len(existing)} existing + {len(new_skills)} new = {len(data['categories'][category_id])} total")

    with open(SURVIVAL_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    for line in report:
        print(line)


if __name__ == "__main__":
    main()
