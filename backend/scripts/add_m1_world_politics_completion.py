#!/usr/bin/env python3
"""Depth pass, M1 World Politics: fill in real, hand-checked
data_table content for the 119 M1 World Politics lessons not covered
by the earlier breadth-first batch. Brings M1 World Politics to full
120/120 coverage.

Structure: 20 topics, each covered in 6 modes at offsets of 20 lessons
apart — "Conceptual Foundations" (l1-l20), "Worked Analysis" (l21-l40),
"Evidence and Data" (l41-l60), "Comparative Case Study" (l61-l80),
"Applied Research Seminar" (l81-l100), and "Independent Capstone"
(l101-l120). l3 (topic 3, Political Ideologies) was already completed
by an earlier breadth-first batch with a data_table matching this
same topic table, so it is reused here as-is (idempotent no-op for l3).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_world_politics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


TOPIC_TABLES: list[dict] = [
    table(["Term", "Meaning"], [["Sovereignty", "A state's supreme authority to govern within its own territory"]]),
    table(["Term", "Meaning"], [["Legitimacy", "The recognized right of a government to hold and exercise power"]]),
    table(["Political Ideology", "Core Idea"], [["Liberalism", "Individual rights and freedoms"], ["Conservatism", "Tradition and gradual change"], ["Socialism", "Collective/state ownership of production"]]),
    table(["Term", "Meaning"], [["Comparative institutions", "Studies how political structures differ and function across countries"]]),
    table(["Term", "Meaning"], [["Democratisation", "The process of a political system transitioning toward democracy"]]),
    table(["Term", "Meaning"], [["Authoritarian politics", "Governance concentrating power with limited accountability or pluralism"]]),
    table(["Theory", "Core Idea"], [["Realism", "States act primarily out of self-interest and power competition"], ["Liberalism (IR)", "Cooperation and institutions can moderate state conflict"]]),
    table(["Term", "Meaning"], [["Diplomacy", "The practice of managing relations between states through negotiation"]]),
    table(["Term", "Meaning"], [["International law", "Rules governing relations between states and international actors"]]),
    table(["Term", "Meaning"], [["United Nations", "An intergovernmental organization coordinating international peace and cooperation"]]),
    table(["Term", "Meaning"], [["Security studies", "Examines threats to states and populations and how they are managed"]]),
    table(["Term", "Meaning"], [["War and peace", "Studies the causes of armed conflict and the conditions for lasting peace"]]),
    table(["Term", "Meaning"], [["Human rights (global)", "Universal entitlements protected across international legal frameworks"]]),
    table(["Term", "Meaning"], [["Global political economy", "Studies how politics and economics interact across national borders"]]),
    table(["Term", "Meaning"], [["Development politics", "Examines political factors shaping a country's economic development"]]),
    table(["Term", "Meaning"], [["Migration (global)", "The cross-border movement of people driven by economic, political, or conflict factors"]]),
    table(["Term", "Meaning"], [["Regional organisation", "A body coordinating policy among states within a geographic region"]]),
    table(["Term", "Meaning"], [["Technology and geopolitics", "How emerging technology reshapes global power competition"]]),
    table(["Term", "Meaning"], [["Climate diplomacy", "Negotiating international cooperation to address climate change"]]),
    table(["Term", "Meaning"], [["Global governance", "Coordination among states and institutions without a central world government"]]),
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
        CHARTS[f"world-politics-m1-l{lesson_n}"] = {"data_table": topic_table}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Politics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json World Politics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 World Politics lessons (completing 120/120).")


if __name__ == "__main__":
    main()
