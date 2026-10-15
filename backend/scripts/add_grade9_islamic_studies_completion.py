#!/usr/bin/env python3
"""Depth pass, Grade 9 Islamic Studies: fill in real, hand-checked
data_table content for the 48 Grade 9 Islamic Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 9 Islamic
Studies to full 50/50 coverage.

Content sticks to well-established, uncontroversial facts -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "is-g9-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Islamic Golden Age", "c. 8th-14th century CE, era of major advances in science and scholarship"],
        ]),
    },
    "islamic-studies-g9-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Birthplace", "Makkah"], ["Approximate birth year", "570 CE"],
        ]),
    },
    "islamic-studies-g9-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["First revelation", "Received in the Cave of Hira"], ["Approximate age at first revelation", "40"],
        ]),
    },
    "islamic-studies-g9-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Madinah community", "Established following the Hijrah in 622 CE"],
        ]),
    },
    "islamic-studies-g9-l6": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Shahada", "Declaration of faith"], ["Salah", "Prayer"], ["Zakat", "Charity"],
            ["Sawm", "Fasting"], ["Hajj", "Pilgrimage"],
        ]),
    },
    "islamic-studies-g9-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Shahada", "The declaration of faith, first of the Five Pillars"],
        ]),
    },
    "islamic-studies-g9-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Salah", "Prayer, performed five times daily"],
        ]),
    },
    "islamic-studies-g9-l9": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Zakat", "Giving a portion of wealth to those in need"],
        ]),
    },
    "islamic-studies-g9-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Ramadan", "The month of fasting"], ["Fasting hours", "From dawn (Fajr) to sunset (Maghrib)"],
        ]),
    },
    "islamic-studies-g9-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Hajj", "Pilgrimage to Makkah"], ["Required of", "Those who are physically and financially able"],
        ]),
    },
    "islamic-studies-g9-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Quran", "Believed by Muslims to be revealed to Prophet Muhammad"],
            ["Preservation", "Memorized and written down by companions"],
        ]),
    },
    "islamic-studies-g9-l13": {
        "data_table": table(["Theme", "Example"], [
            ["Monotheism", "The oneness of God"], ["Guidance", "Moral and legal instruction"],
        ]),
    },
    "islamic-studies-g9-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Hadith", "Recorded sayings and actions attributed to Prophet Muhammad"],
        ]),
    },
    "islamic-studies-g9-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Sunnah", "The practices and example of Prophet Muhammad"],
        ]),
    },
    "islamic-studies-g9-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Tawhid", "The oneness of Allah, a central concept in Islam"],
        ]),
    },
    "islamic-studies-g9-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Angels", "Believed to be created from light and to carry out God's commands"],
        ]),
    },
    "islamic-studies-g9-l19": {
        "data_table": table(["Prophet", "Known For"], [
            ["Ibrahim", "Willingness to obey God"], ["Musa", "Leading his people out of Egypt"],
        ]),
    },
    "islamic-studies-g9-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Akhirah", "Belief in the afterlife and Day of Judgment"],
        ]),
    },
    "islamic-studies-g9-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Qadr", "Belief in divine decree alongside personal responsibility"],
        ]),
    },
    "islamic-studies-g9-l22": {
        "data_table": table(["Caliph", "Order"], [
            ["Abu Bakr", "1st"], ["Umar ibn al-Khattab", "2nd"], ["Uthman ibn Affan", "3rd"], ["Ali ibn Abi Talib", "4th"],
        ]),
    },
    "islamic-studies-g9-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Early Muslim community", "Faced persecution in Makkah before migrating to Madinah"],
        ]),
    },
    "islamic-studies-g9-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Early spread", "From Arabia across the Middle East, North Africa, and beyond within a century"],
        ]),
    },
    "islamic-studies-g9-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Sharia", "The body of Islamic religious law"], ["Fiqh", "Islamic jurisprudence, the interpretation of Sharia"],
        ]),
    },
    "islamic-studies-g9-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Akhlaq", "Islamic character and moral conduct"],
        ]),
    },
    "islamic-studies-g9-l27": {
        "data_table": table(["Value", "Example"], [
            ["Family cohesion", "Caring for extended family members"],
        ]),
    },
    "islamic-studies-g9-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Ummah", "The global community of Muslims"],
        ]),
    },
    "islamic-studies-g9-l29": {
        "data_table": table(["Value", "Meaning"], [
            ["Justice", "Treating people fairly"],
        ]),
    },
    "islamic-studies-g9-l30": {
        "data_table": table(["Value", "Meaning"], [
            ["Seeking knowledge", "Highly valued in Islamic tradition"],
        ]),
    },
    "islamic-studies-g9-l31": {
        "data_table": table(["Woman", "Known For"], [
            ["Khadijah", "Prophet Muhammad's first wife, a successful businesswoman"],
            ["Fatima al-Fihri", "Founded the University of al-Qarawiyyin, c. 859 CE"],
        ]),
    },
    "islamic-studies-g9-l32": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Geometric patterns", "Repeating shapes"],
        ]),
    },
    "islamic-studies-g9-l33": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Arabic calligraphy", "Ornate stylized script, often used to write the Quran"],
        ]),
    },
    "islamic-studies-g9-l34": {
        "data_table": table(["Mosque", "Location"], [
            ["Sheikh Zayed Grand Mosque", "Abu Dhabi, UAE"], ["Sultan Ahmed Mosque (Blue Mosque)", "Istanbul, Turkey"],
        ]),
    },
    "islamic-studies-g9-l35": {
        "data_table": table(["Scholar", "Contribution"], [
            ["Al-Khwarizmi", "Mathematics, origin of the word 'algorithm'"],
        ]),
    },
    "islamic-studies-g9-l36": {
        "data_table": table(["Scholar", "Contribution"], [
            ["Ibn Sina (Avicenna)", "Author of The Canon of Medicine"],
        ]),
    },
    "islamic-studies-g9-l37": {
        "data_table": table(["Scholar", "Contribution"], [
            ["Al-Battani", "Astronomy, precise measurements of the solar year"],
        ]),
    },
    "islamic-studies-g9-l38": {
        "data_table": table(["Scholar", "Field"], [
            ["Ibn Rushd (Averroes)", "Philosophy, commentary on Aristotle"],
        ]),
    },
    "islamic-studies-g9-l39": {
        "data_table": table(["Principle", "Meaning"], [
            ["Prohibition of interest (riba)", "A core principle in Islamic finance"],
        ]),
    },
    "islamic-studies-g9-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["Historical example", "Muslim, Christian, and Jewish scholars collaborated in Andalusia"],
        ]),
    },
    "islamic-studies-g9-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Andalusia", "Muslim-ruled region of the Iberian Peninsula, c. 711-1492"],
            ["Notable city", "Cordoba, a center of learning"],
        ]),
    },
    "islamic-studies-g9-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Ottoman Empire", "1299-1922, centered in Anatolia"],
        ]),
    },
    "islamic-studies-g9-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Sufism", "A mystical tradition within Islam emphasizing spiritual closeness to God"],
        ]),
    },
    "islamic-studies-g9-l44": {
        "data_table": table(["Eid", "Marks"], [
            ["Eid al-Fitr", "The end of Ramadan"], ["Eid al-Adha", "The pilgrimage season"],
        ]),
    },
    "islamic-studies-g9-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Islamic calendar", "A lunar calendar with 12 months"],
        ]),
    },
    "islamic-studies-g9-l46": {
        "data_table": table(["Etiquette", "Example"], [
            ["Greeting", "Assalamu alaikum (peace be upon you)"],
        ]),
    },
    "islamic-studies-g9-l47": {
        "data_table": table(["Value", "Example"], [
            ["Caring for the environment", "Not wasting resources like water"],
        ]),
    },
    "islamic-studies-g9-l48": {
        "data_table": table(["Region", "Muslim Population Notable"], [
            ["Southeast Asia", "Indonesia has the world's largest Muslim population"],
        ]),
    },
    "islamic-studies-g9-l49": {
        "data_table": table(["Value", "Meaning"], [
            ["Peace", "A core value emphasized across Islamic teaching"],
        ]),
    },
    "islamic-studies-g9-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Ummah", "The global community of Muslims, united regardless of nationality"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Islamic Studies lessons (completing 50/50).")


if __name__ == "__main__":
    main()
