#!/usr/bin/env python3
"""Depth pass, Grade 4 Islamic Studies: fill in real, hand-checked
data_table content for the 28 Grade 4 Islamic Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 4 Islamic
Studies to full 30/30 coverage.

Content sticks to well-established, uncontroversial facts -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "isl-g4-l1": {
        "data_table": table(["Prophet", "Known For"], [
            ["Ibrahim", "Willingness to obey God"], ["Musa", "Leading his people out of Egypt"],
        ]),
    },
    "islamic-studies-g4-l2": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Shahada", "Declaration of faith"], ["Salah", "Prayer"], ["Zakat", "Charity"],
            ["Sawm", "Fasting"], ["Hajj", "Pilgrimage"],
        ]),
    },
    "islamic-studies-g4-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Salah", "Prayer, performed five times daily"],
        ]),
    },
    "islamic-studies-g4-l4": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Giving a portion of wealth to those in need"],
        ]),
    },
    "islamic-studies-g4-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Ramadan", "The month of fasting"], ["Fasting hours", "From dawn (Fajr) to sunset (Maghrib)"],
        ]),
    },
    "islamic-studies-g4-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Hajj", "Pilgrimage to Makkah"], ["Required of", "Those who are physically and financially able"],
        ]),
    },
    "islamic-studies-g4-l7": {
        "data_table": table(["Value", "Example"], [
            ["Kindness", "Helping someone in need"], ["Good manners", "Speaking politely"],
        ]),
    },
    "islamic-studies-g4-l8": {
        "data_table": table(["Value", "Example"], [
            ["Respecting parents", "Obeying and caring for them"],
        ]),
    },
    "islamic-studies-g4-l9": {
        "data_table": table(["Value", "Meaning"], [
            ["Honesty", "Telling the truth"], ["Trustworthiness", "Keeping promises"],
        ]),
    },
    "islamic-studies-g4-l10": {
        "data_table": table(["Value", "Example"], [
            ["Kindness to neighbors", "Checking in on them, sharing food"],
        ]),
    },
    "islamic-studies-g4-l11": {
        "data_table": table(["Value", "Example"], [
            ["Caring for animals", "Feeding and being gentle with them"],
        ]),
    },
    "islamic-studies-g4-l12": {
        "data_table": table(["Value", "Example"], [
            ["Cleanliness (Tahara)", "Washing before prayer (wudu)"],
        ]),
    },
    "islamic-studies-g4-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Mosque", "A place of worship for Muslims"], ["Purpose", "Prayer and community gathering"],
        ]),
    },
    "islamic-studies-g4-l15": {
        "data_table": table(["Eid", "Marks"], [
            ["Eid al-Fitr", "The end of Ramadan"], ["Eid al-Adha", "The pilgrimage season"],
        ]),
    },
    "islamic-studies-g4-l16": {
        "data_table": table(["Value", "Meaning"], [
            ["Knowledge", "Highly valued in Islamic tradition"],
        ]),
    },
    "islamic-studies-g4-l17": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Obligatory charity"], ["Sadaqah", "Voluntary charity"],
        ]),
    },
    "islamic-studies-g4-l18": {
        "data_table": table(["Value", "Meaning"], [
            ["Patience", "Staying calm through difficulty"], ["Gratitude", "Being thankful"],
        ]),
    },
    "islamic-studies-g4-l19": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Geometric patterns", "Repeating shapes, common in mosque decoration"],
            ["Calligraphy", "Ornate Arabic script"],
        ]),
    },
    "islamic-studies-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Storytelling for values", "Prophet stories used to teach honesty and patience"],
        ]),
    },
    "islamic-studies-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Daily practice", "Following the Five Pillars in everyday life"],
        ]),
    },
    "islamic-studies-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Daily routine", "Praying five times a day"],
        ]),
    },
    "islamic-studies-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Community giving", "Donating to a local charity"],
        ]),
    },
    "islamic-studies-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Self-discipline", "Practicing patience while fasting"],
        ]),
    },
    "islamic-studies-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Travel planning", "Preparing for a long pilgrimage journey"],
        ]),
    },
    "islamic-studies-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Everyday manners", "Greeting others kindly"],
        ]),
    },
    "islamic-studies-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Family life", "Helping parents with household tasks"],
        ]),
    },
    "islamic-studies-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["School life", "Returning a lost item to its owner"],
        ]),
    },
    "islamic-studies-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Community life", "Welcoming a new neighbor"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Islamic Studies lessons (completing 30/30).")


if __name__ == "__main__":
    main()
