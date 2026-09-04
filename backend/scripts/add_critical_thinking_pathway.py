#!/usr/bin/env python3
"""Add a new "Critical Thinking" pathway to Practical Skills, with 50
lessons covering logic, argument analysis, fallacies, cognitive biases,
evidence/research literacy, media literacy, and applied decision-making.

Topics live in critical_thinking_topics.py. Uses the same module schema
and link-building conventions as generate_practical_skills_expansion.py.

Re-run after editing:
    python3 backend/scripts/add_critical_thinking_pathway.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
PRACTICAL_PATH = BASE_DIR / "data" / "practical_skills" / "practical_skills.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from critical_thinking_topics import TOPICS  # noqa: E402

PATHWAY_ID = "critical_thinking"
PATHWAY_META = {
    "label": "Critical Thinking",
    "emoji": "🧠",
    "certificate": "Critical Thinking Fundamentals Certificate",
}


def yt_search(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def wikihow_search(q: str) -> str:
    return "https://www.wikihow.com/wikiHowTo?search=" + quote_plus(q)


def wikipedia_search(q: str) -> str:
    return "https://en.wikipedia.org/w/index.php?search=" + quote_plus(q)


def build_module(index: int, total: int, item: tuple) -> dict:
    title, description, materials, steps, quiz_q, quiz_a, pro_tip = item
    third = max(total // 3, 1)
    if index < third:
        level, duration = "beginner", 20
    elif index < 2 * third:
        level, duration = "intermediate", 30
    else:
        level, duration = "advanced", 40

    objectives = [
        f"Understand and apply: {title}",
        description.split(".")[0].strip() + ".",
    ]

    return {
        "title": title,
        "grade_range": "All Ages (Kids-Adult)",
        "level": level,
        "duration_minutes": duration,
        "description": description,
        "learning_objectives": objectives,
        "steps": steps,
        "materials_needed": materials,
        "hands_on_activity": f"Practice \"{title}\" with a real example from the news, a conversation, or your own reasoning this week.",
        "quiz": [{"q": quiz_q, "a": quiz_a}],
        "pro_tip": pro_tip,
        "progress_tracking": {"completion_required": True, "min_quiz_score": 70},
        "links": {
            "video_link": yt_search(f"{title} critical thinking explained"),
            "video_search_general": yt_search(f"{title} critical thinking tutorial"),
            "text_link": wikihow_search(title),
            "resource_link": wikipedia_search(title),
        },
    }


def main() -> None:
    with open(PRACTICAL_PATH, encoding="utf-8") as f:
        data = json.load(f)

    pw = data["pathways"].get(PATHWAY_ID)
    if pw is None:
        pw = {
            "label": PATHWAY_META["label"],
            "emoji": PATHWAY_META["emoji"],
            "certificate": PATHWAY_META["certificate"],
            "skills": [],
            "quiz": [],
            "modules": [],
        }
        data["pathways"][PATHWAY_ID] = pw

    existing_modules = pw.get("modules", [])
    existing_titles = {m["title"] for m in existing_modules}

    new_topics = [t for t in TOPICS if t[0] not in existing_titles]
    total = len(existing_modules) + len(new_topics)
    new_modules = [
        build_module(len(existing_modules) + i, total, item)
        for i, item in enumerate(new_topics)
    ]
    pw["modules"] = existing_modules + new_modules

    with open(PRACTICAL_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"critical_thinking: {len(existing_modules)} existing + {len(new_modules)} new = {len(pw['modules'])} total")


if __name__ == "__main__":
    main()
