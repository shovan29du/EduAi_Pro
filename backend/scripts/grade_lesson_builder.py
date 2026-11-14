"""Shared lesson-builder for K-12 grade syllabus files (grade1.json..grade10.json).

Mirrors the lightweight (title, summary) tuple pattern already used for the
college-level expansion (see generate_advanced_curriculum.py's _lesson_for),
but produces the richer field set K-12 lessons use (matching the existing
"math-g1-l1" style lessons already in these files): units, mcq-style quiz
questions, textbook_references as objects, etc.

Only title + a short summary are required per lesson; every other field is
auto-derived from those two strings via templates, exactly like the college
generator. reading_material starts as the short summary and is later expanded
to 700-2000 words by expand_lesson_reading_material.py, same as every other
lesson added this session.
"""
from __future__ import annotations

import re

DIFFICULTY_BY_GRADE = {
    1: "beginner", 2: "beginner", 3: "beginner", 4: "beginner",
    5: "elementary", 6: "elementary",
    7: "intermediate", 8: "intermediate",
    9: "advanced", 10: "advanced",
}
TIME_BY_GRADE = {1: 25, 2: 25, 3: 30, 4: 30, 5: 35, 6: 35, 7: 40, 8: 40, 9: 45, 10: 45}
PASS_SCORE_BY_GRADE = {1: 60, 2: 60, 3: 62, 4: 62, 5: 65, 6: 65, 7: 68, 8: 68, 9: 70, 10: 70}


def _slug(subject: str) -> str:
    return subject.lower().replace(" & ", "-").replace(" ", "-").replace("&", "and")


def build_grade_lesson(subject: str, grade: int, index: int, title: str, summary: str, unit: str | None = None) -> dict:
    unit = unit or title
    first_sentence = summary.split(".")[0].strip() + "."
    key_concepts = [w.strip(",.:&") for w in title.replace("&", "and").split() if len(w) > 3][:5] or [title]
    return {
        "id": f"{_slug(subject)}-g{grade}-l{index}",
        "title": title,
        "unit": unit,
        "grade": grade,
        "subject": subject,
        "difficulty": DIFFICULTY_BY_GRADE.get(grade, "intermediate"),
        "estimated_time_minutes": TIME_BY_GRADE.get(grade, 35),
        "learning_objectives": [
            f"Explain the main idea of {title.lower()}.",
            f"Give an example of {title.lower()} in everyday life.",
            f"Answer questions about {title.lower()} correctly.",
        ],
        "reading_material": summary,
        "key_concepts": key_concepts,
        "practical_activities": [
            f"Class discussion and worksheet on {title.lower()}",
            f"Hands-on activity exploring {title.lower()}",
        ],
        "exercises": [
            {"q": f"In your own words, what is {title.lower()} about?", "type": "short_answer", "answer": first_sentence},
        ],
        "homework": {"task": f"Talk with a family member about what you learned in '{title}' today.", "due": "next_class"},
        "revision": {"notes": first_sentence, "tip": f"Review '{title}' before the next class."},
        "quiz": {
            "questions": [
                {"q": f"Which best describes '{title}'?", "options": [first_sentence, "Unrelated to this subject", "Not covered at this grade", "None of the above"], "answer": first_sentence},
            ]
        },
        "assessment": {"type": "written_test", "criteria": [f"Understands {title.lower()}", "Applies the idea correctly", "Connects it to a real example"], "passing_score": PASS_SCORE_BY_GRADE.get(grade, 65)},
        "prerequisites": [],
        "next_lessons": [],
        "textbook_references": [],
        "video_reference": "",
        "progress_tracking": {"completion_required": True, "min_quiz_score": PASS_SCORE_BY_GRADE.get(grade, 65)},
    }


def next_grade_lesson_index(lessons: list[dict]) -> int:
    max_idx = 0
    for lesson in lessons:
        m = re.search(r"-l(\d+)$", lesson.get("id", ""))
        if m:
            max_idx = max(max_idx, int(m.group(1)))
    return max_idx + 1
