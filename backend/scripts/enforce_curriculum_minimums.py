"""Enforce EduAI Pro's published lesson minimums.

The script is deterministic and idempotent: existing authored lessons are
never replaced, and only the number of lessons needed to reach a level's
minimum is appended.  It also adds the five adult subjects that were absent
from the C1-M2 curriculum.
"""

from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
SYLLABUS_DIR = ROOT / "syllabus"

LEVEL_TARGETS = {
    **{str(level): 20 for level in range(1, 4)},
    **{str(level): 30 for level in range(4, 7)},
    **{str(level): 40 for level in range(7, 9)},
    **{str(level): 50 for level in range(9, 11)},
    "C1": 70,
    "C2": 70,
    "UG1": 100,
    "UG2": 100,
    "UG3": 100,
    "UG4": 100,
    "M1": 120,
    "M2": 120,
}

PRIORITY_SUBJECTS = {
    "Critical Thinking",
    "Environmental Science",
    "World Politics",
    "World Religions",
    "Civics",
    "Health Education",
    "Business Studies",
}
NEW_ADULT_SUBJECTS = PRIORITY_SUBJECTS - {"Critical Thinking", "Health Education"}

SUBJECT_TOPICS = {
    "Critical Thinking": [
        "Claims and Evidence", "Deductive Reasoning", "Inductive Reasoning",
        "Validity and Soundness", "Informal Fallacies", "Cognitive Bias",
        "Causal Reasoning", "Statistical Claims", "Scientific Reasoning",
        "Source Evaluation", "Media Literacy", "Argument Mapping",
        "Decision Theory", "Ethical Reasoning", "Legal Reasoning",
        "Systems Thinking", "Counterexamples", "Uncertainty and Risk",
        "Constructive Debate", "Metacognition",
    ],
    "Environmental Science": [
        "Earth Systems", "Ecosystem Dynamics", "Biodiversity", "Biogeochemical Cycles",
        "Climate Science", "Atmospheric Pollution", "Freshwater Systems", "Ocean Change",
        "Soil and Agriculture", "Forestry", "Energy Systems", "Waste and Circularity",
        "Toxicology", "Environmental Health", "Conservation Biology", "Urban Ecology",
        "Environmental Economics", "Environmental Law", "Climate Adaptation",
        "Sustainability Transitions",
    ],
    "World Politics": [
        "States and Sovereignty", "Power and Legitimacy", "Political Ideologies",
        "Comparative Institutions", "Democratisation", "Authoritarian Politics",
        "International Relations Theory", "Diplomacy", "International Law",
        "The United Nations", "Security Studies", "War and Peace", "Human Rights",
        "Global Political Economy", "Development Politics", "Migration",
        "Regional Organisations", "Technology and Geopolitics", "Climate Diplomacy",
        "Global Governance",
    ],
    "World Religions": [
        "Methods in Religious Studies", "Indigenous Traditions", "Hindu Traditions",
        "Buddhist Traditions", "Jain Traditions", "Sikh Traditions", "Jewish Traditions",
        "Christian Traditions", "Islamic Traditions", "East Asian Traditions",
        "African Diasporic Traditions", "Sacred Texts", "Ritual and Practice",
        "Religious Ethics", "Mysticism", "Religion and Art", "Religion and Politics",
        "Religion and Science", "Secularism and Nonreligion", "Interfaith Dialogue",
    ],
    "Civics": [
        "Citizenship", "Constitutions", "Rule of Law", "Separation of Powers",
        "Legislatures", "Executives", "Judiciaries", "Elections and Voting",
        "Political Parties", "Local Government", "Public Administration",
        "Civil Liberties", "Human Rights", "Media and Public Opinion",
        "Civil Society", "Public Policy", "Taxation and Public Budgets",
        "Community Organising", "Digital Citizenship", "Democratic Resilience",
    ],
    "Health Education": [
        "Health Literacy", "Nutrition", "Physical Activity", "Sleep Science",
        "Mental Wellbeing", "Stress Management", "Sexual and Reproductive Health",
        "Communicable Disease", "Noncommunicable Disease", "Medicines and Vaccines",
        "Substance-Use Prevention", "First Aid", "Injury Prevention",
        "Environmental Health", "Workplace Health", "Public Health Systems",
        "Health Inequality", "Digital Health", "Healthcare Decision-Making",
        "Personal Health Planning",
    ],
    "Business Studies": [
        "Business Purpose", "Business Models", "Entrepreneurship", "Market Research",
        "Customer Value", "Marketing Strategy", "Operations Management",
        "Supply Chains", "Accounting Fundamentals", "Corporate Finance",
        "People Management", "Organisational Behaviour", "Business Law",
        "Business Ethics", "Strategy", "Innovation Management", "Digital Business",
        "International Business", "Risk and Resilience", "Sustainable Enterprise",
    ],
}

ACADEMIC_LENSES = [
    "Conceptual Foundations",
    "Worked Analysis",
    "Evidence and Data",
    "Comparative Case Study",
    "Applied Research Seminar",
    "Independent Capstone",
]
SCHOOL_LENSES = [
    "Guided Practice", "Real-Life Application", "Investigation",
    "Problem-Solving Workshop", "Review and Challenge",
]

AUTHORITATIVE_LINKS = {
    "Environmental Science": "https://www.unep.org/resources",
    "World Politics": "https://www.un.org/en/global-issues",
    "World Religions": "https://pluralism.org/religions",
    "Civics": "https://www.un.org/en/about-us/universal-declaration-of-human-rights",
    "Business Studies": "https://openstax.org/details/books/principles-management",
}


def external_course_links(subject_name: str, level: str) -> list[dict]:
    query = quote_plus(f"{subject_name} {level} university course")
    return [
        {"title": "Udemy course search", "url": f"https://www.udemy.com/courses/search/?q={query}", "source": "Udemy", "safe": True},
        {"title": "Coursera course search", "url": f"https://www.coursera.org/search?query={query}", "source": "Coursera", "safe": True},
        {"title": "edX course search", "url": f"https://www.edx.org/search?q={query}", "source": "edX", "safe": True},
        {"title": "MIT OpenCourseWare search", "url": f"https://ocw.mit.edu/search/?q={query}", "source": "MIT OpenCourseWare", "safe": True},
        {"title": "Harvard Online search", "url": f"https://pll.harvard.edu/catalog?keywords={query}", "source": "Harvard Online Learning", "safe": True},
        {"title": "Pinterest study resources", "url": f"https://www.pinterest.com/search/pins/?q={query}", "source": "Pinterest", "safe": True},
    ]


def slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "subject"


def syllabus_path(level: str) -> Path:
    return SYLLABUS_DIR / (f"grade{level}.json" if level.isdigit() else f"level_{level.lower()}.json")


def source_url(subject: dict, subject_name: str) -> str:
    for collection in ("text_resources", "books", "textbooks", "external_courses"):
        for item in subject.get(collection, []):
            if isinstance(item, str) and item.startswith(("http://", "https://")):
                return item
            if isinstance(item, dict):
                for key in ("url", "link"):
                    value = item.get(key)
                    if isinstance(value, str) and value.startswith(("http://", "https://")):
                        return value
    return AUTHORITATIVE_LINKS.get(subject_name, "https://openstax.org/subjects")


def subject_shell(subject_name: str, level: str) -> dict:
    query = quote_plus(f"{subject_name} {level} university course")
    reference = AUTHORITATIVE_LINKS[subject_name]
    return {
        "books": [{
            "id": f"{slug(subject_name)}-{level.lower()}-open-reader",
            "title": f"{subject_name}: Open Academic Reader",
            "author": "Curated authoritative sources",
            "edition": "Online",
            "cover": "",
            "link": reference,
            "rating": 4.5,
            "country": "International",
            "paid": False,
            "safe": True,
            "source": "Authoritative open curriculum resource",
        }],
        "video_resources": [{
            "title": f"{subject_name} university lectures",
            "url": f"https://www.youtube.com/results?search_query={query}",
            "description": f"University-level lecture search for {subject_name}.",
            "thumbnail": "",
            "type": "video",
            "safe": True,
        }],
        "cartoon_videos": [],
        "text_resources": [{
            "title": f"{subject_name} authoritative reference",
            "url": reference,
            "source": "Curated authoritative source",
            "safe": True,
        }],
        "infographics": [],
        "quiz_bank": [],
        "exam": {"title": f"{subject_name} cumulative assessment", "questions": []},
        "textbooks": [],
        "audio_resources": [],
        "comics": [],
        "drawing_activities": [],
        "info_cards": [],
        "news_resources": [],
        "lessons": [],
        "project_ideas": [
            f"Evidence-based {subject_name} case study",
            f"Comparative {subject_name} research project",
            f"Applied {subject_name} policy or practice proposal",
        ],
        "real_world_examples": [
            f"Analyse a current problem using {subject_name} methods.",
            f"Compare how two communities approach a {subject_name} question.",
        ],
        "learning_path": (
            "Begin with concepts and vocabulary, progress through evidence and "
            "comparative cases, and finish with independent applied research."
        ),
        "external_courses": external_course_links(subject_name, level),
    }


def generated_lesson(
    level: str,
    subject_name: str,
    subject: dict,
    number: int,
    seed_lessons: list[dict],
) -> dict:
    advanced = not level.isdigit()
    level_label = level if advanced else f"Grade {level}"
    level_slug = level.lower() if advanced else f"g{level}"
    topics = SUBJECT_TOPICS.get(subject_name)
    if topics:
        topic = topics[(number - 1) % len(topics)]
        lens_index = ((number - 1) // len(topics)) % len(ACADEMIC_LENSES)
        lens = ACADEMIC_LENSES[lens_index]
    else:
        seed = seed_lessons[(number - 1) % len(seed_lessons)]
        topic = str(seed.get("title") or subject_name)
        lenses = ACADEMIC_LENSES if advanced else SCHOOL_LENSES
        lens = lenses[((number - 1) // max(1, len(seed_lessons))) % len(lenses)]
        if number > len(seed_lessons) * len(lenses):
            lens = f"{lens} {1 + (number - 1) // (len(seed_lessons) * len(lenses))}"

    title = f"{topic}: {lens}"
    reference = source_url(subject, subject_name)
    threshold = 60 if advanced else 70
    difficulty = (
        "masters-advanced" if level.startswith("M")
        else "undergraduate-advanced" if level.startswith("UG")
        else "college-advanced" if level.startswith("C")
        else "elementary"
    )
    objective_verb = "critically evaluate" if advanced else "explain"
    reading = (
        f"This {level_label} lesson examines {topic} through {lens.lower()} in "
        f"{subject_name}. It establishes the main vocabulary, the relationships "
        "between the core ideas, and the boundary conditions under which a claim "
        "or method is reliable.\n\n"
        f"Learners work from a concrete {subject_name} problem to an evidence-based "
        f"explanation. They must identify assumptions, distinguish observations "
        f"from interpretations, and use the supplied source to check important "
        f"claims. The worked analysis deliberately includes an incomplete argument "
        "so that learners can diagnose what evidence is still needed.\n\n"
        f"The lesson concludes by applying {topic} to a second context. Learners "
        f"compare alternatives, justify a decision, record uncertainty, and reflect "
        f"on how the conclusion might change if the evidence changed. Reference: {reference}"
    )
    lesson_id = f"{slug(subject_name)}-{level_slug}-l{number}"
    previous_id = f"{slug(subject_name)}-{level_slug}-l{number - 1}" if number > 1 else None
    next_id = f"{slug(subject_name)}-{level_slug}-l{number + 1}"
    return {
        "id": lesson_id,
        "title": title,
        "unit": topic,
        ("level" if advanced else "grade"): level if advanced else int(level),
        "subject": subject_name,
        "difficulty": difficulty,
        "estimated_time_minutes": 60 if advanced else 45,
        "learning_objectives": [
            f"Explain the central concepts and vocabulary of {topic}.",
            f"Apply {topic} to a worked {subject_name} problem.",
            f"{objective_verb.capitalize()} evidence, assumptions, and alternative conclusions.",
        ],
        "reading_material": reading,
        "key_concepts": [topic, lens, "evidence", "application", "reflection"],
        "practical_activities": [
            f"Build a concept map for {topic}.",
            f"Complete a source-backed {subject_name} case analysis.",
            "Compare two possible conclusions and defend the stronger one.",
        ],
        "exercises": [
            {
                "q": f"What evidence is most important when applying {topic}?",
                "type": "short_answer",
                "answer": "Relevant, credible evidence that directly supports the stated conclusion.",
            },
            {
                "q": f"Give one limitation of the worked {subject_name} case.",
                "type": "short_answer",
                "answer": "A valid answer identifies a missing assumption, evidence gap, or limit on generalisation.",
            },
        ],
        "homework": {
            "task": f"Write a source-backed application of {topic} to a new case and include one counterargument.",
            "due": "next_class",
        },
        "revision": {
            "notes": f"Review the definition, evidence, application, and limitations of {topic}.",
            "tip": "Reconstruct the argument from memory, then verify it against the cited source.",
        },
        "quiz": {
            "questions": [{
                "q": f"Which response best demonstrates mastery of {topic}?",
                "type": "mcq",
                "options": [
                    "A conclusion supported by relevant evidence and explicit assumptions",
                    "An unsupported opinion",
                    "A copied definition with no application",
                    "A claim that ignores counterevidence",
                ],
                "answer": "A conclusion supported by relevant evidence and explicit assumptions",
            }],
        },
        "assessment": {
            "type": "case_analysis",
            "criteria": ["Conceptual accuracy", "Evidence quality", "Application", "Critical reflection"],
            "passing_score": threshold,
        },
        "prerequisites": [previous_id] if previous_id else [],
        "next_lessons": [next_id],
        "textbook_references": [reference],
        "video_reference": f"https://www.youtube.com/results?search_query={quote_plus(topic + ' ' + subject_name + ' lecture')}",
        "progress_tracking": {"completion_required": True, "min_quiz_score": threshold},
    }


def expand_level(level: str) -> tuple[int, int]:
    path = syllabus_path(level)
    payload = json.loads(path.read_text(encoding="utf-8"))
    subjects = payload["subjects"]
    added_subjects = 0
    if not level.isdigit():
        for subject_name in sorted(NEW_ADULT_SUBJECTS):
            if subject_name not in subjects:
                subjects[subject_name] = subject_shell(subject_name, level)
                added_subjects += 1
            else:
                # Keep new adult subjects consistent with every existing
                # subject's six-provider course-integration contract.
                subjects[subject_name]["external_courses"] = external_course_links(subject_name, level)

    added_lessons = 0
    for subject_name, subject in subjects.items():
        lessons = subject.setdefault("lessons", [])
        original = deepcopy(lessons) or [{
            "title": f"Foundations of {subject_name}",
        }]
        target = LEVEL_TARGETS[level]
        if not level.isdigit() and subject_name in PRIORITY_SUBJECTS:
            target = max(target, 100)
        while len(lessons) < target:
            lessons.append(generated_lesson(level, subject_name, subject, len(lessons) + 1, original))
            added_lessons += 1

    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return added_subjects, added_lessons


def main() -> None:
    total_subjects = 0
    total_lessons = 0
    for level in LEVEL_TARGETS:
        subjects, lessons = expand_level(level)
        total_subjects += subjects
        total_lessons += lessons
        print(f"{level}: +{subjects} subjects, +{lessons} lessons")
    print(f"Total: +{total_subjects} subjects, +{total_lessons} lessons")


if __name__ == "__main__":
    main()
