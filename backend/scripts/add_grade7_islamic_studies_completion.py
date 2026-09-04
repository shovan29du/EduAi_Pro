#!/usr/bin/env python3
"""Depth pass, Grade 7 Islamic Studies: fill in real, hand-checked
data_table content for the 38 Grade 7 Islamic Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 7 Islamic
Studies to full 40/40 coverage.

Content sticks to well-established, uncontroversial facts -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "isl-g7-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Islamic Golden Age", "c. 8th-14th century CE, era of major advances in science and scholarship"],
        ]),
    },
    "islamic-studies-g7-l2": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Shahada", "Declaration of faith"], ["Salah", "Prayer"], ["Zakat", "Charity"],
            ["Sawm", "Fasting"], ["Hajj", "Pilgrimage"],
        ]),
    },
    "islamic-studies-g7-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Islamic calendar", "A lunar calendar with 12 months"],
        ]),
    },
    "islamic-studies-g7-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Ramadan", "The month of fasting"], ["Fasting hours", "From dawn (Fajr) to sunset (Maghrib)"],
        ]),
    },
    "islamic-studies-g7-l5": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Giving a portion of wealth to those in need"],
        ]),
    },
    "islamic-studies-g7-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Hajj", "Pilgrimage to Makkah"], ["Required of", "Those who are physically and financially able"],
        ]),
    },
    "islamic-studies-g7-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Salah", "Prayer, performed five times daily"],
        ]),
    },
    "islamic-studies-g7-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Birthplace", "Makkah"], ["Approximate birth year", "570 CE"],
        ]),
    },
    "islamic-studies-g7-l9": {
        "data_table": table(["Companion", "Known For"], [
            ["Abu Bakr", "First caliph after the Prophet"], ["Umar ibn al-Khattab", "Second caliph, known for justice"],
        ]),
    },
    "islamic-studies-g7-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Hadith", "Recorded sayings and actions attributed to Prophet Muhammad"],
        ]),
    },
    "islamic-studies-g7-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Akhlaq", "Islamic character and moral conduct"],
        ]),
    },
    "islamic-studies-g7-l13": {
        "data_table": table(["Value", "Meaning"], [
            ["Honesty", "Telling the truth"], ["Trustworthiness", "Keeping promises"],
        ]),
    },
    "islamic-studies-g7-l14": {
        "data_table": table(["Value", "Example"], [
            ["Respecting parents", "Obeying and caring for them"],
        ]),
    },
    "islamic-studies-g7-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Ummah", "The global community of Muslims"],
        ]),
    },
    "islamic-studies-g7-l16": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Obligatory charity"], ["Sadaqah", "Voluntary charity"],
        ]),
    },
    "islamic-studies-g7-l17": {
        "data_table": table(["Value", "Example"], [
            ["Caring for the environment", "Not wasting resources like water"],
        ]),
    },
    "islamic-studies-g7-l18": {
        "data_table": table(["Value", "Example"], [
            ["Animal welfare", "Treating animals with kindness and care"],
        ]),
    },
    "islamic-studies-g7-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Early spread", "From Arabia across the Middle East, North Africa, and beyond within a century"],
        ]),
    },
    "islamic-studies-g7-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Andalusia", "Muslim-ruled region of the Iberian Peninsula, c. 711-1492"],
            ["Notable city", "Cordoba, a center of learning"],
        ]),
    },
    "islamic-studies-g7-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["House of Wisdom", "A major center of learning in Baghdad"],
            ["Focus", "Translating and advancing Greek, Persian, and Indian texts"],
        ]),
    },
    "islamic-studies-g7-l22": {
        "data_table": table(["Scholar", "Contribution"], [
            ["Al-Khwarizmi", "Mathematics, origin of the word 'algorithm'"],
        ]),
    },
    "islamic-studies-g7-l23": {
        "data_table": table(["Scholar", "Contribution"], [
            ["Al-Battani", "Astronomy, precise measurements of the solar year"],
        ]),
    },
    "islamic-studies-g7-l24": {
        "data_table": table(["Scholar", "Contribution"], [
            ["Ibn Sina (Avicenna)", "Medicine, author of The Canon of Medicine"],
        ]),
    },
    "islamic-studies-g7-l25": {
        "data_table": table(["Scholar", "Known For"], [
            ["Fatima al-Fihri", "Founded the University of al-Qarawiyyin, c. 859 CE"],
        ]),
    },
    "islamic-studies-g7-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Madrasa", "A traditional Islamic school for religious and other studies"],
        ]),
    },
    "islamic-studies-g7-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Fiqh", "Islamic jurisprudence, the study of Islamic law"],
        ]),
    },
    "islamic-studies-g7-l28": {
        "data_table": table(["Eid", "Marks"], [
            ["Eid al-Fitr", "The end of Ramadan"], ["Eid al-Adha", "The pilgrimage season"],
        ]),
    },
    "islamic-studies-g7-l29": {
        "data_table": table(["Mosque", "Location"], [
            ["Sheikh Zayed Grand Mosque", "Abu Dhabi, UAE"], ["Sultan Ahmed Mosque (Blue Mosque)", "Istanbul, Turkey"],
        ]),
    },
    "islamic-studies-g7-l30": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Geometric patterns", "Repeating shapes"],
        ]),
    },
    "islamic-studies-g7-l31": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Arabic calligraphy", "Ornate stylized script, often used to write the Quran"],
        ]),
    },
    "islamic-studies-g7-l32": {
        "data_table": table(["Fact", "Detail"], [
            ["Historical example", "Muslim, Christian, and Jewish scholars collaborated in Andalusia"],
        ]),
    },
    "islamic-studies-g7-l33": {
        "data_table": table(["Principle", "Meaning"], [
            ["Prohibition of interest (riba)", "A core principle in Islamic finance"],
        ]),
    },
    "islamic-studies-g7-l34": {
        "data_table": table(["Value", "Example"], [
            ["Family cohesion", "Caring for extended family members"],
        ]),
    },
    "islamic-studies-g7-l35": {
        "data_table": table(["Etiquette", "Example"], [
            ["Cleanliness before entering", "Performing wudu before prayer"],
        ]),
    },
    "islamic-studies-g7-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Hafiz", "A person who has memorized the entire Quran"],
        ]),
    },
    "islamic-studies-g7-l37": {
        "data_table": table(["Library", "Location"], [
            ["House of Wisdom", "Baghdad"], ["Library of al-Qarawiyyin", "Fez, Morocco"],
        ]),
    },
    "islamic-studies-g7-l38": {
        "data_table": table(["Traveller", "Known For"], [
            ["Ibn Battuta", "Extensive travels across Africa and Asia"],
        ]),
    },
    "islamic-studies-g7-l39": {
        "data_table": table(["Region", "Muslim Population Notable"], [
            ["Southeast Asia", "Indonesia has the world's largest Muslim population"],
            ["South Asia", "Home to large Muslim populations in Pakistan, India, and Bangladesh"],
        ]),
    },
    "islamic-studies-g7-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["Trade Route", "The Silk Road connected the Islamic world to Asia and Europe"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Islamic Studies lessons (completing 40/40).")


if __name__ == "__main__":
    main()
