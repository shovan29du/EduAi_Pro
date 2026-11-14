#!/usr/bin/env python3
"""Depth pass, Grade 5 Islamic Studies: fill in real, hand-checked
data_table content for the 28 Grade 5 Islamic Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 5 Islamic
Studies to full 30/30 coverage.

Content sticks to well-established, uncontroversial facts -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "is-g5-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Akhlaq", "Islamic character and moral conduct"],
        ]),
    },
    "islamic-studies-g5-l3": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Shahada", "Declaration of faith"], ["Salah", "Prayer"], ["Zakat", "Charity"],
            ["Sawm", "Fasting"], ["Hajj", "Pilgrimage"],
        ]),
    },
    "islamic-studies-g5-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Birthplace", "Makkah"], ["Approximate birth year", "570 CE"],
        ]),
    },
    "islamic-studies-g5-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["First revelation", "Received in the Cave of Hira"], ["Approximate age at first revelation", "40"],
        ]),
    },
    "islamic-studies-g5-l6": {
        "data_table": table(["Prophet", "Known For"], [
            ["Ibrahim", "Willingness to obey God"], ["Musa", "Leading his people out of Egypt"],
        ]),
    },
    "islamic-studies-g5-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Salah", "Prayer, performed five times daily"],
        ]),
    },
    "islamic-studies-g5-l8": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Giving a portion of wealth to those in need"],
        ]),
    },
    "islamic-studies-g5-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Ramadan", "The month of fasting"], ["Fasting hours", "From dawn (Fajr) to sunset (Maghrib)"],
        ]),
    },
    "islamic-studies-g5-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Hajj", "Pilgrimage to Makkah"], ["Required of", "Those who are physically and financially able"],
        ]),
    },
    "islamic-studies-g5-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Quran", "Believed by Muslims to be revealed to Prophet Muhammad"],
            ["Preservation", "Memorized and written down by companions"],
        ]),
    },
    "islamic-studies-g5-l12": {
        "data_table": table(["Value", "Example"], [
            ["Respecting parents", "Obeying and caring for them"],
        ]),
    },
    "islamic-studies-g5-l13": {
        "data_table": table(["Value", "Example"], [
            ["Kindness to neighbors", "Checking in on them, sharing food"],
        ]),
    },
    "islamic-studies-g5-l14": {
        "data_table": table(["Value", "Meaning"], [
            ["Honesty", "Telling the truth"], ["Trustworthiness", "Keeping promises"],
        ]),
    },
    "islamic-studies-g5-l15": {
        "data_table": table(["Value", "Meaning"], [
            ["Patience", "Staying calm through difficulty"], ["Perseverance", "Continuing despite challenges"],
        ]),
    },
    "islamic-studies-g5-l16": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Obligatory charity"], ["Sadaqah", "Voluntary charity"],
        ]),
    },
    "islamic-studies-g5-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Ummah", "The global community of Muslims"],
        ]),
    },
    "islamic-studies-g5-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Mosque", "A place of worship for Muslims"], ["Purpose", "Prayer and community gathering"],
        ]),
    },
    "islamic-studies-g5-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Eid al-Fitr", "Marks the end of Ramadan"], ["Common practice", "Special prayers and family gatherings"],
        ]),
    },
    "islamic-studies-g5-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Eid al-Adha", "Commemorates Ibrahim's willingness to sacrifice"],
            ["Common practice", "Sharing food with family and those in need"],
        ]),
    },
    "islamic-studies-g5-l22": {
        "data_table": table(["Scholar", "Field"], [
            ["Ibn al-Haytham", "Optics"], ["Al-Khwarizmi", "Mathematics, origin of the word 'algorithm'"],
        ]),
    },
    "islamic-studies-g5-l23": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Geometric patterns", "Repeating shapes"], ["Calligraphy", "Ornate Arabic script"],
        ]),
    },
    "islamic-studies-g5-l24": {
        "data_table": table(["Value", "Example"], [
            ["Caring for the environment", "Not wasting resources like water"],
        ]),
    },
    "islamic-studies-g5-l25": {
        "data_table": table(["Value", "Meaning"], [
            ["Justice", "Treating people fairly"], ["Fairness", "Making impartial decisions"],
        ]),
    },
    "islamic-studies-g5-l26": {
        "data_table": table(["Value", "Meaning"], [
            ["Gratitude", "Being thankful for blessings"],
        ]),
    },
    "islamic-studies-g5-l27": {
        "data_table": table(["Value", "Example"], [
            ["Respecting elders", "Speaking politely and listening"], ["Respecting teachers", "Valuing their knowledge"],
        ]),
    },
    "islamic-studies-g5-l28": {
        "data_table": table(["Value", "Meaning"], [
            ["Seeking knowledge", "Highly valued in Islamic tradition"],
        ]),
    },
    "islamic-studies-g5-l29": {
        "data_table": table(["Value", "Meaning"], [
            ["Unity", "Standing together as a community"], ["Brotherhood", "Treating others as family"],
        ]),
    },
    "islamic-studies-g5-l30": {
        "data_table": table(["Value", "Example"], [
            ["Good manners", "Speaking politely and greeting others kindly"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 Islamic Studies lessons (completing 30/30).")


if __name__ == "__main__":
    main()
