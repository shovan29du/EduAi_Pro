#!/usr/bin/env python3
"""Depth pass, Grade 8 Islamic Studies: fill in real, hand-checked
data_table content for the 38 Grade 8 Islamic Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 8 Islamic
Studies to full 40/40 coverage.

Content sticks to well-established, uncontroversial facts -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "islamic-studies-g8-l2": {
        "data_table": table(["Article of Faith", "Meaning"], [
            ["Belief in Allah", "The oneness of God"], ["Belief in Angels", "Messengers of God"],
        ]),
    },
    "islamic-studies-g8-l3": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Shahada", "Declaration of faith"], ["Salah", "Prayer"], ["Zakat", "Charity"],
            ["Sawm", "Fasting"], ["Hajj", "Pilgrimage"],
        ]),
    },
    "islamic-studies-g8-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Makkan period", "570-622 CE, before migration to Madinah"],
        ]),
    },
    "islamic-studies-g8-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Madinan period", "622-632 CE, after the Hijra migration"],
        ]),
    },
    "islamic-studies-g8-l6": {
        "data_table": table(["Trait", "Example"], [
            ["Patience", "Endured hardship with steadfastness"], ["Honesty", "Known as Al-Amin (the trustworthy)"],
        ]),
    },
    "islamic-studies-g8-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Quran", "Believed by Muslims to be revealed to Prophet Muhammad"],
            ["Preservation", "Memorized and written down by companions"],
        ]),
    },
    "islamic-studies-g8-l9": {
        "data_table": table(["Theme", "Example"], [
            ["Monotheism", "The oneness of God"], ["Guidance", "Moral and legal instruction"],
        ]),
    },
    "islamic-studies-g8-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Tafsir", "The scholarly interpretation and explanation of the Quran"],
        ]),
    },
    "islamic-studies-g8-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Hadith", "Recorded sayings and actions attributed to Prophet Muhammad"],
        ]),
    },
    "islamic-studies-g8-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Sunnah", "The practices and example of Prophet Muhammad"],
        ]),
    },
    "islamic-studies-g8-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Tawheed", "The oneness of Allah, a central concept in Islam"],
        ]),
    },
    "islamic-studies-g8-l14": {
        "data_table": table(["Prophet", "Known For"], [
            ["Ibrahim", "Willingness to obey God"], ["Musa", "Leading his people out of Egypt"],
        ]),
    },
    "islamic-studies-g8-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Ibrahim (Abraham)", "Known for willingness to obey God"],
        ]),
    },
    "islamic-studies-g8-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Musa (Moses)", "Led his people out of Egypt"],
        ]),
    },
    "islamic-studies-g8-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Isa (Jesus)", "Regarded in Islam as a prophet of God"],
        ]),
    },
    "islamic-studies-g8-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Akhlaq", "Islamic character and moral conduct"],
        ]),
    },
    "islamic-studies-g8-l19": {
        "data_table": table(["Value", "Meaning"], [
            ["Honesty", "Telling the truth"], ["Trustworthiness", "Keeping promises"],
        ]),
    },
    "islamic-studies-g8-l20": {
        "data_table": table(["Value", "Example"], [
            ["Kindness to parents", "Obeying and caring for them"],
        ]),
    },
    "islamic-studies-g8-l21": {
        "data_table": table(["Etiquette", "Example"], [
            ["Greeting", "Assalamu alaikum (peace be upon you)"],
        ]),
    },
    "islamic-studies-g8-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Ummah", "The global community of Muslims"],
        ]),
    },
    "islamic-studies-g8-l23": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Giving a portion of wealth to those in need"],
        ]),
    },
    "islamic-studies-g8-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Sawm", "Fasting from dawn to sunset during Ramadan"],
        ]),
    },
    "islamic-studies-g8-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Hajj", "Pilgrimage to Makkah"], ["Required of", "Those who are physically and financially able"],
        ]),
    },
    "islamic-studies-g8-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Salah", "Prayer, performed five times daily"],
        ]),
    },
    "islamic-studies-g8-l27": {
        "data_table": table(["Wudu Step", "Body Part"], [
            ["Wash", "Hands, face, arms, feet"], ["Wipe", "Head"],
        ]),
    },
    "islamic-studies-g8-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Islamic calendar", "A lunar calendar with 12 months"],
        ]),
    },
    "islamic-studies-g8-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Mosque", "A place of worship for Muslims"],
        ]),
    },
    "islamic-studies-g8-l30": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Geometric patterns", "Repeating shapes"], ["Calligraphy", "Ornate Arabic script"],
        ]),
    },
    "islamic-studies-g8-l31": {
        "data_table": table(["Scholar", "Field"], [
            ["Al-Khwarizmi", "Mathematics, origin of the word 'algorithm'"], ["Ibn Sina (Avicenna)", "Medicine"],
        ]),
    },
    "islamic-studies-g8-l32": {
        "data_table": table(["Scholar", "Field"], [
            ["Al-Khwarizmi", "Mathematics"], ["Al-Battani", "Astronomy"],
        ]),
    },
    "islamic-studies-g8-l33": {
        "data_table": table(["Scholar", "Contribution"], [
            ["Ibn Sina (Avicenna)", "Author of The Canon of Medicine"],
        ]),
    },
    "islamic-studies-g8-l34": {
        "data_table": table(["Woman", "Known For"], [
            ["Khadijah", "Prophet Muhammad's first wife, a successful businesswoman"],
            ["Fatima al-Fihri", "Founded the University of al-Qarawiyyin, c. 859 CE"],
        ]),
    },
    "islamic-studies-g8-l35": {
        "data_table": table(["Value", "Example"], [
            ["Family cohesion", "Caring for extended family members"],
        ]),
    },
    "islamic-studies-g8-l36": {
        "data_table": table(["Value", "Example"], [
            ["Caring for the environment", "Not wasting resources like water"],
        ]),
    },
    "islamic-studies-g8-l37": {
        "data_table": table(["Value", "Meaning"], [
            ["Justice", "Treating people fairly"],
        ]),
    },
    "islamic-studies-g8-l38": {
        "data_table": table(["Fact", "Detail"], [
            ["Historical example", "Muslim, Christian, and Jewish scholars collaborated in Andalusia"],
        ]),
    },
    "islamic-studies-g8-l39": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Obligatory charity"], ["Sadaqah", "Voluntary charity"],
        ]),
    },
    "islamic-studies-g8-l40": {
        "data_table": table(["Value", "Meaning"], [
            ["Seeking knowledge", "Highly valued in Islamic tradition"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Islamic Studies lessons (completing 40/40).")


if __name__ == "__main__":
    main()
