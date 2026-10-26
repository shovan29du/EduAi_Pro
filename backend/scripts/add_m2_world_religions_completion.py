#!/usr/bin/env python3
"""Depth pass, M2 World Religions: fill in real, hand-checked
data_table content for the M2 World Religions lessons not covered by
the earlier breadth-first batch. Brings M2 World Religions to full
120/120 coverage.

Structure (same topic-block pattern as M1 World Religions): 20 topics,
each covered in 6 modes at offsets of 20 lessons apart -- "Conceptual
Foundations" (l1-l20), "Worked Analysis" (l21-l40), "Evidence and
Data" (l41-l60), "Comparative Case Study" (l61-l80), "Applied Research
Seminar" (l81-l100), and "Independent Capstone" (l101-l120). l3 (topic
3, Hindu Traditions) was already completed by an earlier breadth-first
batch with a data_table matching this same topic table, so it is
reused here as-is (idempotent no-op for l3).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_world_religions_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


TOPIC_TABLES: list[dict] = [
    table(["Term", "Meaning"], [["Comparative religious studies", "Analyzes religions using shared scholarly methods rather than a single faith's assumptions"]]),
    table(["Term", "Meaning"], [["Indigenous tradition", "Belief systems rooted in a specific people's land, ancestry, and oral heritage"]]),
    table(["Term (Hindu Tradition)", "Meaning"], [["Dharma", "Duty, righteousness, moral order"], ["Karma", "Actions and their consequences"], ["Moksha", "Liberation from the cycle of rebirth"]]),
    table(["Term (Buddhist Tradition)", "Meaning"], [["Four Noble Truths", "Core teaching on the nature and cessation of suffering"], ["Nirvana", "Liberation from suffering and the cycle of rebirth"]]),
    table(["Term (Jain Tradition)", "Meaning"], [["Ahimsa", "Nonviolence toward all living beings, a central Jain principle"]]),
    table(["Term (Sikh Tradition)", "Meaning"], [["Guru Granth Sahib", "The central religious scripture and eternal Guru of Sikhism"]]),
    table(["Term (Jewish Tradition)", "Meaning"], [["Torah", "The core text of Jewish law and teaching"], ["Covenant", "The binding relationship between God and the Jewish people"]]),
    table(["Term (Christian Tradition)", "Meaning"], [["Trinity", "The doctrine of God as Father, Son, and Holy Spirit"]]),
    table(["Term (Islamic Tradition)", "Meaning"], [["Five Pillars", "Core obligatory practices of Islamic faith"], ["Tawhid", "The oneness and unity of God"]]),
    table(["Term (East Asian Tradition)", "Meaning"], [["Tao", "The underlying natural order in Daoist thought"], ["Ren", "Confucian virtue of benevolence and humaneness"]]),
    table(["Term (African Diasporic Tradition)", "Meaning"], [["Syncretism", "The blending of African spiritual practices with other religious traditions"]]),
    table(["Term", "Meaning"], [["Sacred text", "A writing regarded by a tradition as authoritative and revelatory"]]),
    table(["Term", "Meaning"], [["Ritual", "A prescribed symbolic act performed within a religious tradition"]]),
    table(["Term", "Meaning"], [["Religious ethics", "Moral guidance and principles derived from religious teaching"]]),
    table(["Term", "Meaning"], [["Mysticism", "Direct, often ineffable spiritual experience of ultimate reality"]]),
    table(["Term", "Meaning"], [["Sacred art", "Visual and material expressions used to convey religious meaning"]]),
    table(["Term", "Meaning"], [["Religion and politics", "The interaction between religious authority and civil governance"]]),
    table(["Term", "Meaning"], [["Religion and science", "The historical and philosophical relationship between faith and scientific inquiry"]]),
    table(["Term", "Meaning"], [["Secularism", "The separation of religious institutions from civil and state affairs"]]),
    table(["Term", "Meaning"], [["Interfaith dialogue", "Structured engagement between different religious traditions aimed at mutual understanding"]]),
]

MODE_TO_OFFSET = {
    "Conceptual Foundations": 0,
    "Worked Analysis": 20,
    "Evidence and Data": 40,
    "Comparative Case Study": 60,
    "Applied Research Seminar": 80,
    "Independent Capstone": 100,
}

CHARTS: dict[str, dict] = {}
for offset in MODE_TO_OFFSET.values():
    for i, topic_table in enumerate(TOPIC_TABLES):
        lesson_n = offset + i + 1
        CHARTS[f"world-religions-m2-l{lesson_n}"] = {"data_table": topic_table}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Religions"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json World Religions: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson or lesson[key] is None:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {updated} fields across {len(CHARTS)} M2 World Religions lessons (completing 120/120).")


if __name__ == "__main__":
    main()
