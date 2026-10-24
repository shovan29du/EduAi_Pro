#!/usr/bin/env python3
"""Depth pass, M2 Business Studies: fill in real, hand-checked
data_table content for the M2 Business Studies lessons not covered by
the earlier breadth-first batch. Brings M2 Business Studies to full
120/120 coverage.

Structure (same topic-block pattern as M1 Business Studies): 20
topics, each covered in 6 modes at offsets of 20 lessons apart --
"Conceptual Foundations" (l1-l20), "Worked Analysis" (l21-l40),
"Evidence and Data" (l41-l60), "Comparative Case Study" (l61-l80),
"Applied Research Seminar" (l81-l100), and "Independent Capstone"
(l101-l120). l3 (topic 3, Entrepreneurship) was already completed by
an earlier breadth-first batch with a data_table matching this same
topic table, so it is reused here as-is (idempotent no-op for l3).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_business_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


TOPIC_TABLES: list[dict] = [
    table(["Term", "Meaning"], [["Business purpose", "The core reason a business exists beyond making a profit"]]),
    table(["Term", "Meaning"], [["Business model", "How a company creates, delivers, and captures value"]]),
    table(["Term", "Meaning"], [["Entrepreneur", "A person who starts and runs a business, taking on financial risk"], ["Startup", "A newly founded business, often aiming to scale quickly"]]),
    table(["Term", "Meaning"], [["Market research", "Systematic gathering of data about customers and competitors"]]),
    table(["Term", "Meaning"], [["Customer value", "The benefit a customer perceives relative to what they pay"]]),
    table(["Term", "Meaning"], [["Marketing strategy", "A plan for reaching and persuading a target customer segment"]]),
    table(["Term", "Meaning"], [["Operations management", "Oversees the processes that produce a company's goods or services"]]),
    table(["Term", "Meaning"], [["Supply chain", "The network of organizations moving a product from raw material to customer"]]),
    table(["Term", "Meaning"], [["Accounting", "Records and reports a business's financial transactions"]]),
    table(["Term", "Meaning"], [["Corporate finance", "Manages how a company raises and allocates capital"]]),
    table(["Term", "Meaning"], [["People management", "Recruits, develops, and retains a company's workforce"]]),
    table(["Term", "Meaning"], [["Organisational behaviour", "Studies how individuals and groups act within an organization"]]),
    table(["Term", "Meaning"], [["Business law", "The legal rules governing commercial activity and contracts"]]),
    table(["Term", "Meaning"], [["Business ethics", "Moral principles guiding acceptable conduct in commerce"]]),
    table(["Term", "Meaning"], [["Strategy", "A long-term plan for achieving a sustainable competitive advantage"]]),
    table(["Term", "Meaning"], [["Innovation management", "Systematically organizes a company's development of new ideas"]]),
    table(["Term", "Meaning"], [["Digital business", "Uses digital technology to transform how a company operates"]]),
    table(["Term", "Meaning"], [["International business", "Commercial activity that crosses national borders"]]),
    table(["Term", "Meaning"], [["Risk and resilience", "Identifying threats and building capacity to withstand disruption"]]),
    table(["Term", "Meaning"], [["Sustainable enterprise", "Balances profit with environmental and social responsibility"]]),
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
        CHARTS[f"business-studies-m2-l{lesson_n}"] = {"data_table": topic_table}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Business Studies"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Business Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson or lesson[key] is None:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Business Studies lessons (completing 120/120).")


if __name__ == "__main__":
    main()
