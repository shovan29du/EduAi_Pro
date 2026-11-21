#!/usr/bin/env python3
"""Depth pass, Grade 3 Islamic Studies: fill in real, hand-checked
data_table content for the 18 Grade 3 Islamic Studies lessons not covered
by the earlier breadth-first batch. Brings Grade 3 Islamic Studies to
full 20/20 coverage.

Content sticks to well-established, uncontroversial facts (the Five
Pillars, prayer names, Ramadan/Eid facts, general good-manners guidance)
without specific Quranic citations requiring verification beyond common
knowledge -- nothing fabricated or presented as fact when it's actually
invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "is-g3-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Birthplace", "Makkah"], ["Role", "Final prophet in Islam"],
        ]),
    },
    "islamic-studies-g3-l2": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Shahada", "Declaration of faith"], ["Salah", "Prayer, five times daily"],
            ["Zakat", "Charity"], ["Sawm", "Fasting during Ramadan"], ["Hajj", "Pilgrimage to Makkah"],
        ]),
    },
    "islamic-studies-g3-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Quran", "The holy book of Islam"], ["Language", "Written in Arabic"],
        ]),
    },
    "islamic-studies-g3-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Salah", "Prayer, one of the Five Pillars"], ["Times per day", "Five"],
        ]),
    },
    "islamic-studies-g3-l5": {
        "data_table": table(["Wudu Step", "Body Part"], [
            ["Wash", "Hands, face, arms, feet"], ["Wipe", "Head"],
        ]),
    },
    "islamic-studies-g3-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Eid al-Fitr", "Marks the end of Ramadan"], ["Common practice", "Special prayers and family gatherings"],
        ]),
    },
    "islamic-studies-g3-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Eid al-Adha", "Commemorates Ibrahim's willingness to sacrifice"],
            ["Common practice", "Sharing food with family and those in need"],
        ]),
    },
    "islamic-studies-g3-l9": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Giving a portion of wealth to those in need"],
        ]),
    },
    "islamic-studies-g3-l11": {
        "data_table": table(["Prophet", "Known For"], [
            ["Ibrahim", "Willingness to obey God"], ["Musa", "Leading his people out of Egypt"],
        ]),
    },
    "islamic-studies-g3-l12": {
        "data_table": table(["Value", "Example"], [
            ["Kindness", "Helping someone in need"], ["Respect", "Listening to elders"],
        ]),
    },
    "islamic-studies-g3-l13": {
        "data_table": table(["Value", "Example"], [
            ["Respecting parents", "Obeying and caring for them"], ["Respecting elders", "Speaking politely"],
        ]),
    },
    "islamic-studies-g3-l14": {
        "data_table": table(["Value", "Example"], [
            ["Caring for neighbors", "Checking in on them, sharing food"],
        ]),
    },
    "islamic-studies-g3-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Mosque", "A place of worship for Muslims"], ["Purpose", "Prayer and community gathering"],
        ]),
    },
    "islamic-studies-g3-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Adhan", "The call to prayer"], ["Called by", "A muezzin"],
        ]),
    },
    "islamic-studies-g3-l17": {
        "data_table": table(["Value", "Meaning"], [
            ["Honesty", "Telling the truth"], ["Trustworthiness", "Being reliable and keeping promises"],
        ]),
    },
    "islamic-studies-g3-l18": {
        "data_table": table(["Value", "Example"], [
            ["Cleanliness", "Washing before prayer (wudu), keeping tidy"],
        ]),
    },
    "islamic-studies-g3-l19": {
        "data_table": table(["Value", "Meaning"], [
            ["Gratitude", "Being thankful"], ["Patience", "Staying calm through difficulty"],
        ]),
    },
    "islamic-studies-g3-l20": {
        "data_table": table(["Value", "Example"], [
            ["Caring for animals", "Feeding and being gentle with them"],
            ["Caring for nature", "Not wasting resources"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Islamic Studies lessons (completing 20/20).")


if __name__ == "__main__":
    main()
