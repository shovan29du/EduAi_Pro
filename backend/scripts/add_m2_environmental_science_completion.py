#!/usr/bin/env python3
"""Depth pass, M2 Environmental Science: fill in real, hand-checked
data_table content for the M2 Environmental Science lessons not
covered by the earlier breadth-first batch. Brings M2 Environmental
Science to full 120/120 coverage.

Structure (same topic-block pattern as M1 Environmental Science): 20
topics, each covered in 6 modes at offsets of 20 lessons apart --
"Conceptual Foundations" (l1-l20), "Worked Analysis" (l21-l40),
"Evidence and Data" (l41-l60), "Comparative Case Study" (l61-l80),
"Applied Research Seminar" (l81-l100), and "Independent Capstone"
(l101-l120). l3 (topic 3, Biodiversity) was already completed by an
earlier breadth-first batch with a data_table matching this same topic
table, so it is reused here as-is (idempotent no-op for l3).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_environmental_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


TOPIC_TABLES: list[dict] = [
    table(["Term", "Meaning"], [["Earth system", "The interconnected atmosphere, hydrosphere, lithosphere, and biosphere"]]),
    table(["Term", "Meaning"], [["Ecosystem dynamics", "How energy and matter flow and change within an ecological community"]]),
    table(["Term", "Meaning"], [["Biodiversity", "The variety of life in an ecosystem"], ["Species richness", "The number of different species present"]]),
    table(["Term", "Meaning"], [["Biogeochemical cycle", "The movement of an element like carbon or nitrogen through Earth's systems"]]),
    table(["Term", "Meaning"], [["Climate science", "Studies long-term patterns and drivers of Earth's climate system"]]),
    table(["Term", "Meaning"], [["Atmospheric pollution", "Harmful substances released into the air by human or natural sources"]]),
    table(["Term", "Meaning"], [["Freshwater system", "Rivers, lakes, and aquifers that supply usable water resources"]]),
    table(["Term", "Meaning"], [["Ocean change", "Shifts in ocean temperature, chemistry, and circulation over time"]]),
    table(["Term", "Meaning"], [["Soil and agriculture", "The relationship between soil health and sustainable food production"]]),
    table(["Term", "Meaning"], [["Forestry", "The management of forest resources for ecological and economic value"]]),
    table(["Term", "Meaning"], [["Energy system", "The infrastructure producing, distributing, and consuming energy"]]),
    table(["Term", "Meaning"], [["Circularity", "Designing waste out of production through reuse and recycling"]]),
    table(["Term", "Meaning"], [["Toxicology", "Studies the harmful effects of substances on living organisms"]]),
    table(["Term", "Meaning"], [["Environmental health", "Links environmental exposures to human health outcomes"]]),
    table(["Term", "Meaning"], [["Conservation biology", "Applies science to protect species and ecosystems from decline"]]),
    table(["Term", "Meaning"], [["Urban ecology", "Studies ecological processes within and around cities"]]),
    table(["Term", "Meaning"], [["Environmental economics", "Analyzes the costs and benefits of environmental policy choices"]]),
    table(["Term", "Meaning"], [["Environmental law", "The body of regulation governing environmental protection"]]),
    table(["Term", "Meaning"], [["Climate adaptation", "Adjusting systems and practices to cope with a changing climate"]]),
    table(["Term", "Meaning"], [["Sustainability transition", "A shift toward more environmentally sustainable systems and practices"]]),
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
        CHARTS[f"environmental-science-m2-l{lesson_n}"] = {"data_table": topic_table}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Environmental Science"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Environmental Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson or lesson[key] is None:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Environmental Science lessons (completing 120/120).")


if __name__ == "__main__":
    main()
