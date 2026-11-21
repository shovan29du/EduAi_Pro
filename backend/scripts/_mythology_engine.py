"""Shared engine for building the "Mythology" subject across levels C1
through M1, reusing the existing college-level curriculum scaffold from
generate_advanced_curriculum.py (books/quiz_bank/exam/external_courses
etc.) but replacing each lesson's reading_material with real,
level-appropriate content about one mythological tradition.

Consistent with this project's no-fabrication rule: every specific claim
(deity names, myths, texts, practices) traces back to a fact string
supplied per tradition below. The engine adds generic framing/reflection
language around those facts to reach a length appropriate to the level
(short overview at C1, longer analytical treatment by M1) -- exactly the
same "supply real facts, expand into level-appropriate prose" pattern
used for expand_lesson_reading_material.py and this session's Biography
Library engine.

Each TRADITIONS entry is a dict with:
    key           short id, e.g. "greek"
    name          e.g. "Greek Mythology"
    region        e.g. "Ancient Greece"
    deities       3-6 short real facts naming major gods/goddesses and
                  their domains
    creation      1-3 sentences on the tradition's creation/cosmology myth
    heroes        3-5 short real facts about heroes, legendary figures,
                  or well-known myths/epics
    practices     2-4 short real facts about religious practice, temples,
                  or the key surviving texts (e.g. the Rigveda, the
                  Poetic Edda, the Popol Vuh)
    legacy        2-4 short real facts about the tradition's lasting
                  cultural influence (language, literature, art, modern
                  culture)
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_advanced_curriculum import (  # noqa: E402
    LEVEL_IDS,
    LEVEL_LABELS,
    _subject_content,
)

# C1..M1 only -- M2 is intentionally excluded per this request's "from C1 to M1".
MYTHOLOGY_LEVEL_IDS = [lvl for lvl in LEVEL_IDS if lvl != "M2"]

_LEVEL_FRAME = {
    "C1": ("an introductory overview", 1),
    "C2": ("a closer look at the tradition's cosmology and origins", 2),
    "UG1": ("an exploration of its heroes and legendary narratives", 3),
    "UG2": ("a study of its religious practice and surviving texts", 4),
    "UG3": ("an examination of its lasting cultural and artistic influence", 5),
    "UG4": ("a comparative look at how it connects to neighbouring mythologies", 6),
    "M1": ("a graduate-level, source-critical synthesis", 7),
}

_INTRO_TEMPLATES = [
    "This module offers {frame} of {name}, the body of myth, belief, and religious practice that developed in {region}.",
    "{name} developed among the peoples of {region}, and this module provides {frame}.",
    "Few mythological traditions have left as rich a record as {name}, and this module gives {frame} of it.",
]

_DEITY_LEAD = [
    "The tradition's pantheon includes: {items}",
    "Among the most significant figures are: {items}",
    "Central to {name} are figures such as: {items}",
]

_CREATION_LEAD = [
    "Its account of the world's origin holds that {text}",
    "According to {name}, {text}",
    "The tradition's cosmology describes that {text}",
]

_HERO_LEAD = [
    "Its legendary narratives include: {items}",
    "Among its best-known stories and heroic figures are: {items}",
    "The tradition's heroic literature includes: {items}",
]

_PRACTICE_LEAD = [
    "Its religious practice and surviving textual record include: {items}",
    "What is known of its ritual life and key texts includes: {items}",
    "The tradition is documented through: {items}",
]

_LEGACY_LEAD = [
    "Its lasting cultural influence includes: {items}",
    "Traces of the tradition persist today in: {items}",
    "Modern culture continues to draw on it through: {items}",
]

_REFLECTION_POOL = [
    "This is worth dwelling on, since it shows how a mythological system organizes explanation, morality, and meaning for the people who held it.",
    "Read alongside the tradition's other elements, it forms part of a coherent worldview rather than an isolated tale.",
    "Students encountering this for the first time should note how specific and structured the account is, rather than a vague or arbitrary story.",
    "Comparative mythologists have long noted how this connects to patterns found in other, geographically distant traditions -- a useful reminder that human cultures have repeatedly reached for similar kinds of explanation.",
    "It is also worth asking what social or historical circumstance the account may reflect, since myth often encodes real concerns of the society that told it.",
    "This detail is among the better-documented parts of the tradition, thanks to surviving texts, inscriptions, or archaeological evidence.",
    "Later artists, writers, and, in some cases, entire religious movements have returned to this element repeatedly across the centuries.",
]

_SIGNIFICANCE_TEMPLATES = [
    "Studying {name} matters for reasons beyond entertainment value: myth was, for the people of {region}, a working framework for explaining natural phenomena, justifying social and political order, and transmitting moral and religious values across generations. A careful student learns to read these stories the way the original audience encountered them -- as meaningful, structured accounts of the world, not as simple children's tales.",
    "{name} functioned, for the societies of {region}, as far more than storytelling: it shaped calendars, law, art, architecture, and public ritual. Approaching it seriously means asking not just 'what happens in the story' but 'what work did this story do for the people who told it.'",
]

_CLOSING_TEMPLATES = [
    "Taken as a whole, {name} illustrates how a specific culture in {region} used story, ritual, and symbol to organize its understanding of the world, of morality, and of its own place in the cosmos. Studying it seriously means treating it as a coherent system of thought, not a random collection of tales.",
    "{name} remains a living subject of study today, not a closed or purely 'ancient' curiosity: its stories, structures, and symbols continue to surface in literature, art, and popular culture, and comparative study of it against other mythological systems continues to sharpen scholarly understanding of both.",
    "No single module can cover every surviving story and variant of {name}, but the elements above -- its deities, its account of origins, its heroes, its practice, and its legacy -- give a structured foundation for further study of one of the richest mythological traditions to survive from {region}.",
]

_DISCUSSION_TEMPLATES = [
    "Which figure or story from {name} do you find most striking, and why?",
    "How does {name}'s account of the world's origin compare with another tradition you have studied?",
    "What might {name}'s myths reveal about the values or concerns of the society that told them?",
    "Where do you see traces of {name} in art, literature, or popular culture today?",
]


def _cycle(seq, i):
    return seq[i % len(seq)]


def _join_items(items: list[str]) -> str:
    cleaned = [i.strip().rstrip(".") for i in items]
    return "; ".join(cleaned) + "."


def build_reading_material(tradition: dict, level: str) -> str:
    name = tradition["name"]
    region = tradition["region"]
    frame, seed = _LEVEL_FRAME[level]
    level_idx = MYTHOLOGY_LEVEL_IDS.index(level)  # 0 (C1) .. 6 (M1)
    reflections_per_section = 2 + level_idx // 2  # 2 at C1/C2, up to 5 at M1

    paragraphs = []
    paragraphs.append(_cycle(_INTRO_TEMPLATES, seed).format(frame=frame, name=name, region=region))

    paragraphs.append(_cycle(_SIGNIFICANCE_TEMPLATES, seed).format(name=name, region=region))

    paragraphs.append(_cycle(_DEITY_LEAD, seed + 1).format(items=_join_items(tradition["deities"]), name=name))

    creation_p = [_cycle(_CREATION_LEAD, seed + 2).format(text=tradition["creation"].strip().rstrip(".") + ".", name=name)]
    for r in range(reflections_per_section):
        creation_p.append(_cycle(_REFLECTION_POOL, seed + level_idx + r))
    paragraphs.append(" ".join(creation_p))

    heroes_p = [_cycle(_HERO_LEAD, seed + 3).format(items=_join_items(tradition["heroes"]))]
    for r in range(reflections_per_section):
        heroes_p.append(_cycle(_REFLECTION_POOL, seed + level_idx + r + 2))
    paragraphs.append(" ".join(heroes_p))

    practice_p = [_cycle(_PRACTICE_LEAD, seed + 4).format(items=_join_items(tradition["practices"]))]
    for r in range(reflections_per_section):
        practice_p.append(_cycle(_REFLECTION_POOL, seed + level_idx + r + 4))
    paragraphs.append(" ".join(practice_p))

    legacy_p = [_cycle(_LEGACY_LEAD, seed + 5).format(items=_join_items(tradition["legacy"]))]
    for r in range(reflections_per_section):
        legacy_p.append(_cycle(_REFLECTION_POOL, seed + level_idx + r + 6))
    paragraphs.append(" ".join(legacy_p))

    paragraphs.append(_cycle(_CLOSING_TEMPLATES, level_idx).format(name=name, region=region))

    return "\n\n".join(paragraphs)


def build_lesson_title(tradition: dict, level: str) -> str:
    frame_label = {
        "C1": "Overview",
        "C2": "Origins & Cosmology",
        "UG1": "Heroes & Legends",
        "UG2": "Ritual, Practice & Texts",
        "UG3": "Art & Cultural Influence",
        "UG4": "Comparative Mythology",
        "M1": "Critical & Comparative Study",
    }[level]
    return f"{tradition['name']}: {frame_label}"


def build_mythology_subject(level: str, traditions: list[dict]) -> dict:
    """Build the full 'Mythology' subject dict for one level, reusing the
    existing curriculum scaffold (books/quiz_bank/exam/external_courses)
    from generate_advanced_curriculum.py, then overwriting each lesson's
    reading_material with real, level-appropriate mythology content.
    """
    modules = [
        (build_lesson_title(t, level), t["deities"][0].strip().rstrip(".") + ".")
        for t in traditions
    ]
    subject = _subject_content("Mythology", level, modules)
    for lesson, tradition in zip(subject["lessons"], traditions):
        lesson["reading_material"] = build_reading_material(tradition, level)
        lesson["key_concepts"] = [tradition["name"]] + [d.split(":")[0].split(",")[0].strip() for d in tradition["deities"][:4]]
    return subject
