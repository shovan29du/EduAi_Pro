#!/usr/bin/env python3
"""Depth pass, Grade 6 Islamic Studies: fill in real, hand-checked
data_table content for the 28 Grade 6 Islamic Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 6 Islamic
Studies to full 30/30 coverage.

Content sticks to well-established, uncontroversial facts -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "islamic-studies-g6-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Birthplace", "Makkah"], ["Approximate birth year", "570 CE"],
        ]),
    },
    "islamic-studies-g6-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["First revelation", "Received in the Cave of Hira"], ["Approximate age at first revelation", "40"],
        ]),
    },
    "islamic-studies-g6-l4": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Shahada", "Declaration of faith"], ["Salah", "Prayer"], ["Zakat", "Charity"],
            ["Sawm", "Fasting"], ["Hajj", "Pilgrimage"],
        ]),
    },
    "islamic-studies-g6-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Shahada", "The declaration of faith, first of the Five Pillars"],
        ]),
    },
    "islamic-studies-g6-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Salah", "Prayer, performed five times daily"],
        ]),
    },
    "islamic-studies-g6-l7": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Giving a portion of wealth to those in need"],
        ]),
    },
    "islamic-studies-g6-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Ramadan", "The month of fasting"], ["Fasting hours", "From dawn (Fajr) to sunset (Maghrib)"],
        ]),
    },
    "islamic-studies-g6-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Hajj", "Pilgrimage to Makkah"], ["Required of", "Those who are physically and financially able"],
        ]),
    },
    "islamic-studies-g6-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Tawheed", "The oneness of Allah, a central concept in Islam"],
        ]),
    },
    "islamic-studies-g6-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Angels", "Believed to be created from light and to carry out God's commands"],
        ]),
    },
    "islamic-studies-g6-l13": {
        "data_table": table(["Prophet", "Known For"], [
            ["Ibrahim", "Willingness to obey God"], ["Musa", "Leading his people out of Egypt"],
        ]),
    },
    "islamic-studies-g6-l14": {
        "data_table": table(["Holy Book", "Believed Revealed To"], [
            ["Quran", "Prophet Muhammad"], ["Torah", "Prophet Musa"],
        ]),
    },
    "islamic-studies-g6-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Day of Judgment", "Belief in a day when deeds are accounted for"],
        ]),
    },
    "islamic-studies-g6-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Qadar", "Belief in divine decree alongside personal responsibility"],
        ]),
    },
    "islamic-studies-g6-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Akhlaq", "Islamic character and moral conduct"],
        ]),
    },
    "islamic-studies-g6-l18": {
        "data_table": table(["Value", "Meaning"], [
            ["Honesty", "Telling the truth"], ["Trustworthiness", "Keeping promises"],
        ]),
    },
    "islamic-studies-g6-l19": {
        "data_table": table(["Value", "Example"], [
            ["Kindness to parents", "Obeying and caring for them"],
        ]),
    },
    "islamic-studies-g6-l20": {
        "data_table": table(["Value", "Example"], [
            ["Respect for neighbors", "Checking in on them, sharing food"],
        ]),
    },
    "islamic-studies-g6-l21": {
        "data_table": table(["Etiquette", "Example"], [
            ["Greeting", "Assalamu alaikum (peace be upon you)"],
        ]),
    },
    "islamic-studies-g6-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["Mosque", "A place of worship for Muslims"], ["Purpose", "Prayer and community gathering"],
        ]),
    },
    "islamic-studies-g6-l23": {
        "data_table": table(["Eid", "Marks"], [
            ["Eid al-Fitr", "The end of Ramadan"], ["Eid al-Adha", "The pilgrimage season"],
        ]),
    },
    "islamic-studies-g6-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Islamic calendar", "A lunar calendar with 12 months"],
        ]),
    },
    "islamic-studies-g6-l25": {
        "data_table": table(["Companion", "Known For"], [
            ["Abu Bakr", "First caliph after the Prophet"], ["Umar ibn al-Khattab", "Second caliph, known for justice"],
        ]),
    },
    "islamic-studies-g6-l26": {
        "data_table": table(["Caliph", "Order"], [
            ["Abu Bakr", "1st"], ["Umar ibn al-Khattab", "2nd"], ["Uthman ibn Affan", "3rd"], ["Ali ibn Abi Talib", "4th"],
        ]),
    },
    "islamic-studies-g6-l27": {
        "data_table": table(["Scholar", "Field"], [
            ["Al-Khwarizmi", "Mathematics, origin of the word 'algorithm'"], ["Ibn al-Haytham", "Optics"],
        ]),
    },
    "islamic-studies-g6-l28": {
        "data_table": table(["Scholar", "Field"], [
            ["Ibn Sina (Avicenna)", "Medicine"], ["Al-Battani", "Astronomy"],
        ]),
    },
    "islamic-studies-g6-l29": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Geometric patterns", "Repeating shapes"], ["Calligraphy", "Ornate Arabic script"],
        ]),
    },
    "islamic-studies-g6-l30": {
        "data_table": table(["Value", "Example"], [
            ["Caring for the environment", "Not wasting resources like water"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Islamic Studies lessons (completing 30/30).")


if __name__ == "__main__":
    main()
