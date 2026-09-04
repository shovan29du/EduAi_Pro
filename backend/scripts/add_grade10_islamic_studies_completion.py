#!/usr/bin/env python3
"""Depth pass, Grade 10 Islamic Studies: fill in real, hand-checked
data_table content for the Grade 10 Islamic Studies lessons not covered
by the earlier breadth-first batch. Brings Grade 10 Islamic Studies to
full 50/50 coverage.

Content sticks to well-established, uncontroversial facts -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "isl-g10-l1": {
        "data_table": table(["Value", "Meaning"], [
            ["Justice ('adl)", "A core ethical principle in Islamic teaching"],
        ]),
    },
    "islamic-studies-g10-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Meccan period", "c. 610-622 CE, before the migration to Madinah"],
        ]),
    },
    "islamic-studies-g10-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Medinan period", "622-632 CE, following the Hijrah"],
        ]),
    },
    "islamic-studies-g10-l4": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Shahada", "Declaration of faith"], ["Salah", "Prayer"], ["Zakat", "Charity"], ["Sawm", "Fasting"], ["Hajj", "Pilgrimage"],
        ]),
    },
    "islamic-studies-g10-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Tawhid", "The oneness of Allah, a central concept in Islam"],
        ]),
    },
    "islamic-studies-g10-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Quran", "Central religious text of Islam, believed by Muslims to be revealed to Prophet Muhammad"],
        ]),
    },
    "islamic-studies-g10-l7": {
        "data_table": table(["Value", "Meaning"], [
            ["Rahma (compassion)", "A recurring theme in Islamic teaching"],
        ]),
    },
    "islamic-studies-g10-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Hadith", "Recorded sayings and actions attributed to Prophet Muhammad"],
        ]),
    },
    "islamic-studies-g10-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Salah", "Performed five times daily, facing the Kaaba in Makkah"],
        ]),
    },
    "islamic-studies-g10-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Sawm", "Fasting during the month of Ramadan, from dawn to sunset"],
        ]),
    },
    "islamic-studies-g10-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Zakat", "Giving a portion of wealth to those in need, one of the Five Pillars"],
        ]),
    },
    "islamic-studies-g10-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Hajj", "Pilgrimage to Makkah, required once for those who are able"],
        ]),
    },
    "islamic-studies-g10-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Islamic Golden Age", "c. 8th-14th century CE, era of major scientific and scholarly advances"],
        ]),
    },
    "islamic-studies-g10-l15": {
        "data_table": table(["Scholar", "Contribution"], [
            ["Al-Khwarizmi", "Mathematics, origin of the word 'algorithm'"], ["Al-Battani", "Astronomy, precise solar year measurements"],
        ]),
    },
    "islamic-studies-g10-l16": {
        "data_table": table(["Scholar", "Contribution"], [
            ["Ibn Sina (Avicenna)", "Author of The Canon of Medicine"],
        ]),
    },
    "islamic-studies-g10-l17": {
        "data_table": table(["Scholar", "Field"], [
            ["Ibn Rushd (Averroes)", "Philosophy, commentary on Aristotle"],
        ]),
    },
    "islamic-studies-g10-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Sharia", "The body of Islamic religious law"], ["Fiqh", "Islamic jurisprudence, the interpretation of Sharia"],
        ]),
    },
    "islamic-studies-g10-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Sufism", "A mystical tradition within Islam emphasizing spiritual closeness to God"],
        ]),
    },
    "islamic-studies-g10-l21": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Geometric patterns", "Repeating shapes based on mathematical principles"], ["Arabic calligraphy", "Ornate stylized script"],
        ]),
    },
    "islamic-studies-g10-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["Mosque", "Serves as a place of worship and community gathering"],
        ]),
    },
    "islamic-studies-g10-l23": {
        "data_table": table(["Value", "Example"], [
            ["Family cohesion", "Caring for extended family members"],
        ]),
    },
    "islamic-studies-g10-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Sadaqah", "Voluntary charity, in addition to obligatory Zakat"],
        ]),
    },
    "islamic-studies-g10-l25": {
        "data_table": table(["Value", "Example"], [
            ["Environmental stewardship", "Not wasting resources like water"],
        ]),
    },
    "islamic-studies-g10-l26": {
        "data_table": table(["Woman", "Known For"], [
            ["Khadijah", "Prophet Muhammad's first wife, a successful businesswoman"], ["Fatima al-Fihri", "Founded the University of al-Qarawiyyin, c. 859 CE"],
        ]),
    },
    "islamic-studies-g10-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["Andalusia", "Muslim, Christian, and Jewish scholars collaborated in Islamic Spain"],
        ]),
    },
    "islamic-studies-g10-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Islamic calendar", "A lunar calendar with 12 months"],
        ]),
    },
    "islamic-studies-g10-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Ramadan", "The ninth month of the Islamic calendar, a time of fasting and community"],
        ]),
    },
    "islamic-studies-g10-l30": {
        "data_table": table(["Eid", "Marks"], [
            ["Eid al-Fitr", "The end of Ramadan"], ["Eid al-Adha", "The pilgrimage season"],
        ]),
    },
    "islamic-studies-g10-l31": {
        "data_table": table(["Principle", "Meaning"], [
            ["Prohibition of riba (interest)", "A core principle in Islamic finance and trade"],
        ]),
    },
    "islamic-studies-g10-l32": {
        "data_table": table(["Value", "Meaning"], [
            ["'Adl (justice)", "Treating people fairly, a foundational Islamic value"],
        ]),
    },
    "islamic-studies-g10-l33": {
        "data_table": table(["Value", "Meaning"], [
            ["Seeking knowledge", "Highly valued throughout Islamic tradition"],
        ]),
    },
    "islamic-studies-g10-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Ottoman Empire", "1299-1922, made major contributions to art, architecture, and law"],
        ]),
    },
    "islamic-studies-g10-l35": {
        "data_table": table(["Fact", "Detail"], [
            ["Al-Andalus", "Muslim-ruled region of the Iberian Peninsula, c. 711-1492"],
        ]),
    },
    "islamic-studies-g10-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Trade routes", "Islam spread partly through merchants along the Silk Road and Indian Ocean trade"],
        ]),
    },
    "islamic-studies-g10-l37": {
        "data_table": table(["Value", "Meaning"], [
            ["Sulh (reconciliation)", "Peaceful resolution valued in Islamic tradition"],
        ]),
    },
    "islamic-studies-g10-l38": {
        "data_table": table(["Scholar", "Legacy"], [
            ["Al-Ghazali", "Influential theologian and philosopher"],
        ]),
    },
    "islamic-studies-g10-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Ummah", "The global community of Muslims"],
        ]),
    },
    "islamic-studies-g10-l40": {
        "data_table": table(["Value", "Meaning"], [
            ["Care for the body", "Regarded as an important part of overall wellbeing"],
        ]),
    },
    "islamic-studies-g10-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Mosques historically", "Served as centers of learning alongside worship"],
        ]),
    },
    "islamic-studies-g10-l42": {
        "data_table": table(["Right", "Example"], [
            ["Right to dignity", "Emphasized across Islamic teaching on human worth"],
        ]),
    },
    "islamic-studies-g10-l43": {
        "data_table": table(["Value", "Example"], [
            ["Stewardship (khalifa)", "Humans viewed as caretakers of the Earth"],
        ]),
    },
    "islamic-studies-g10-l44": {
        "data_table": table(["Fact", "Detail"], [
            ["Quran preservation", "Memorized and written down by companions during Prophet Muhammad's life"],
        ]),
    },
    "islamic-studies-g10-l45": {
        "data_table": table(["Value", "Meaning"], [
            ["Amanah (trustworthiness)", "A key virtue emphasized in Islamic ethics"],
        ]),
    },
    "islamic-studies-g10-l46": {
        "data_table": table(["Value", "Meaning"], [
            ["Community service", "Encouraged as an expression of faith"],
        ]),
    },
    "islamic-studies-g10-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Ihsan", "Striving for excellence and sincerity in faith and action"],
        ]),
    },
    "islamic-studies-g10-l48": {
        "data_table": table(["Fact", "Detail"], [
            ["Historical trade", "Muslim merchants connected markets across Asia, Africa, and Europe"],
        ]),
    },
    "islamic-studies-g10-l49": {
        "data_table": table(["Region", "Notable Fact"], [
            ["Southeast Asia", "Indonesia has the world's largest Muslim population"],
        ]),
    },
    "islamic-studies-g10-l50": {
        "data_table": table(["Value", "Meaning"], [
            ["Balance (wasatiyyah)", "Moderation is emphasized as a guiding principle in Islamic life"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Islamic Studies lessons (completing 50/50).")


if __name__ == "__main__":
    main()
