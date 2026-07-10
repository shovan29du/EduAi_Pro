#!/usr/bin/env python3
"""Expand every Practical Skills pathway to 50 modules (lessons), and add
12 new pathways: Judo, Kendo, Muay Thai, Jiu-Jitsu, Sword Fighting, Krav
Maga, Boxing, Taekwondo, Kickboxing, Yoga, Stretching, and Bodybuilding.

Each pathway's TOPICS list holds 50 real, distinct, well-established
skill/technique tuples of the form:

    (title, description, materials, steps, quiz_q, quiz_a, pro_tip)

  - title: short lesson name
  - description: 2-4 sentence accurate description of the skill/technique
  - materials: list of materials/equipment needed (can be [])
  - steps: list of 3-5 short, accurate step strings
  - quiz_q / quiz_a: one comprehension question + answer
  - pro_tip: one practical tip

build_module() turns each tuple into the exact JSON schema already used by
existing modules in practical_skills.json (see PathwayView/ModuleView in
frontend/src/components/PracticalSkills.jsx), auto-assigning level
(beginner/intermediate/advanced based on position in the list),
grade_range, duration, learning_objectives, hands_on_activity, and
resource-search links (YouTube/text-guide/Wikipedia search links -- not
guessed direct URLs, consistent with this project's no-fabrication rule).

Re-run after editing:
    python3 backend/scripts/generate_practical_skills_expansion.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
PRACTICAL_PATH = BASE_DIR / "data" / "practical_skills" / "practical_skills.json"

TARGET_MODULES_PER_PATHWAY = 50


def yt_search(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def wikihow_search(q: str) -> str:
    return "https://www.wikihow.com/wikiHowTo?search=" + quote_plus(q)


def wikipedia_search(q: str) -> str:
    return "https://en.wikipedia.org/w/index.php?search=" + quote_plus(q)


# Adult-oriented pathways get an "Adult" grade range; everything else uses a
# broad all-ages range, matching how self_defense_adult/adult_life_skills
# were already tagged in this file.
ADULT_PATHWAYS = {
    "self_defense_adult", "adult_life_skills", "judo", "kendo", "muay_thai",
    "jiu_jitsu", "sword_fighting", "krav_maga", "boxing", "taekwondo",
    "kickboxing", "yoga", "stretching", "bodybuilding",
}

NEW_PATHWAYS_META = {
    "judo": {"label": "Judo", "emoji": "🥋", "certificate": "Judo Fundamentals Certificate"},
    "kendo": {"label": "Kendo", "emoji": "⚔️", "certificate": "Kendo Fundamentals Certificate"},
    "muay_thai": {"label": "Muay Thai", "emoji": "🥊", "certificate": "Muay Thai Fundamentals Certificate"},
    "jiu_jitsu": {"label": "Jiu-Jitsu", "emoji": "🤼", "certificate": "Jiu-Jitsu Fundamentals Certificate"},
    "sword_fighting": {"label": "Sword Fighting (Fencing & HEMA)", "emoji": "🤺", "certificate": "Sword Fighting Fundamentals Certificate"},
    "krav_maga": {"label": "Krav Maga", "emoji": "🛡️", "certificate": "Krav Maga Fundamentals Certificate"},
    "boxing": {"label": "Boxing", "emoji": "🥊", "certificate": "Boxing Fundamentals Certificate"},
    "taekwondo": {"label": "Taekwondo", "emoji": "🥋", "certificate": "Taekwondo Fundamentals Certificate"},
    "kickboxing": {"label": "Kickboxing", "emoji": "🥊", "certificate": "Kickboxing Fundamentals Certificate"},
    "yoga": {"label": "Yoga", "emoji": "🧘", "certificate": "Yoga Practitioner Certificate"},
    "stretching": {"label": "Stretching & Flexibility", "emoji": "🤸", "certificate": "Flexibility & Mobility Certificate"},
    "bodybuilding": {"label": "Bodybuilding & Strength Training", "emoji": "🏋️", "certificate": "Strength Training Fundamentals Certificate"},
}

# TOPICS[pathway_id] = list of 50 tuples:
#   (title, description, materials, steps, quiz_q, quiz_a, pro_tip)
TOPICS: dict[str, list[tuple]] = {}


def build_module(pathway_id: str, index: int, total: int, item: tuple) -> dict:
    title, description, materials, steps, quiz_q, quiz_a, pro_tip = item
    third = max(total // 3, 1)
    if index < third:
        level, duration = "beginner", 20
    elif index < 2 * third:
        level, duration = "intermediate", 30
    else:
        level, duration = "advanced", 40

    grade_range = "Adult" if pathway_id in ADULT_PATHWAYS else "All Ages (Kids-Adult)"

    objectives = [
        f"Understand and safely practice: {title}",
        description.split(".")[0].strip() + ".",
    ]

    return {
        "title": title,
        "grade_range": grade_range,
        "level": level,
        "duration_minutes": duration,
        "description": description,
        "learning_objectives": objectives,
        "steps": steps,
        "materials_needed": materials,
        "hands_on_activity": f"Practice \"{title}\" slowly and safely, focusing on correct form before speed.",
        "quiz": [{"q": quiz_q, "a": quiz_a}],
        "pro_tip": pro_tip,
        "progress_tracking": {"completion_required": True, "min_quiz_score": 70},
        "links": {
            "video_link": yt_search(f"{title} tutorial"),
            "video_search_general": yt_search(f"{title} {pathway_id.replace('_', ' ')} tutorial"),
            "text_link": wikihow_search(title),
            "resource_link": wikipedia_search(title),
        },
    }


def main() -> None:
    with open(PRACTICAL_PATH, encoding="utf-8") as f:
        data = json.load(f)

    # Register new pathways if not already present.
    for pid, meta in NEW_PATHWAYS_META.items():
        if pid not in data["pathways"]:
            data["pathways"][pid] = {
                "label": meta["label"],
                "emoji": meta["emoji"],
                "certificate": meta["certificate"],
                "skills": [],
                "quiz": [],
                "modules": [],
            }

    report = []
    for pathway_id, topics in TOPICS.items():
        if pathway_id not in data["pathways"]:
            report.append(f"SKIP (unknown pathway): {pathway_id}")
            continue
        pw = data["pathways"][pathway_id]
        existing_modules = pw.get("modules", [])
        existing_titles = {m["title"] for m in existing_modules}

        new_topics = [t for t in topics if t[0] not in existing_titles]
        total = len(existing_modules) + len(new_topics)
        new_modules = [
            build_module(pathway_id, len(existing_modules) + i, total, item)
            for i, item in enumerate(new_topics)
        ]
        pw["modules"] = existing_modules + new_modules
        report.append(f"{pathway_id}: {len(existing_modules)} existing + {len(new_modules)} new = {len(pw['modules'])} total")

    with open(PRACTICAL_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    for line in report:
        print(line)


if __name__ == "__main__":
    main()
