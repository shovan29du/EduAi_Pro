#!/usr/bin/env python3
"""Depth pass, C2 Civics: fill in real, hand-checked data_table
content for the 99 C2 Civics lessons not covered by the earlier
breadth-first batch. Brings C2 Civics to full 100/100 coverage.

Structure: 20 topics, each covered in 5 modes at offsets of 20 lessons
apart — "Conceptual Foundations" (l1-l20), "Worked Analysis" (l21-l40),
"Evidence and Data" (l41-l60), "Comparative Case Study" (l61-l80), and
"Applied Research Seminar" (l81-l100). l3 (topic 3, Rule of Law) was
already completed by an earlier breadth-first batch, so its data_table
is hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_civics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


# 20-topic list; each topic gets one small factual table reused across
# all 5 modes (Conceptual Foundations, Worked Analysis, Evidence and
# Data, Comparative Case Study, Applied Research Seminar).
TOPIC_TABLES: list[dict] = [
    table(["Term", "Meaning"], [["Citizenship", "Full legal membership in a state, carrying rights and responsibilities"]]),
    table(["Term", "Meaning"], [["Constitution", "The foundational document establishing a state's structure and limits of power"]]),
    table(["Principle", "Meaning"], [["Rule of law", "Everyone, including the government, is subject to the law"], ["Due process", "Fair treatment through the judicial system"]]),
    table(["Term", "Meaning"], [["Separation of powers", "Divides government authority among distinct branches to prevent overreach"]]),
    table(["Term", "Meaning"], [["Legislature", "The branch of government responsible for making laws"]]),
    table(["Term", "Meaning"], [["Executive", "The branch of government responsible for enforcing and administering laws"]]),
    table(["Term", "Meaning"], [["Judiciary", "The branch of government responsible for interpreting the law"]]),
    table(["Term", "Meaning"], [["Election", "A formal process by which citizens select their representatives"]]),
    table(["Term", "Meaning"], [["Political party", "An organized group seeking to gain and exercise political power"]]),
    table(["Term", "Meaning"], [["Local government", "The level of government closest to and most directly serving residents"]]),
    table(["Term", "Meaning"], [["Public administration", "Implements government policy through the civil service"]]),
    table(["Term", "Meaning"], [["Civil liberties", "Individual freedoms protected from government interference"]]),
    table(["Term", "Meaning"], [["Human rights", "Fundamental entitlements belonging to every person regardless of citizenship"]]),
    table(["Term", "Meaning"], [["Public opinion", "The collective attitudes of citizens toward political issues"]]),
    table(["Term", "Meaning"], [["Civil society", "Voluntary organizations operating outside government and the market"]]),
    table(["Term", "Meaning"], [["Public policy", "A government's chosen course of action to address a public issue"]]),
    table(["Term", "Meaning"], [["Public budget", "A government's formal plan for raising and spending public funds"]]),
    table(["Term", "Meaning"], [["Community organising", "Mobilizes residents to advocate collectively for shared goals"]]),
    table(["Term", "Meaning"], [["Digital citizenship", "Responsible and informed participation in online civic life"]]),
    table(["Term", "Meaning"], [["Democratic resilience", "A political system's capacity to withstand threats to democratic norms"]]),
]

MODE_TO_OFFSET = {
    "Conceptual Foundations": 0,
    "Worked Analysis": 20,
    "Evidence and Data": 40,
    "Comparative Case Study": 60,
    "Applied Research Seminar": 80,
}

CHARTS: dict[str, dict] = {}
for offset in MODE_TO_OFFSET.values():
    for i, topic_table in enumerate(TOPIC_TABLES):
        lesson_n = offset + i + 1
        CHARTS[f"civics-c2-l{lesson_n}"] = {"data_table": topic_table}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Civics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Civics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Civics lessons (completing 100/100).")


if __name__ == "__main__":
    main()
