#!/usr/bin/env python3
"""Depth pass, Grade 2 Islamic Studies: fill in real, hand-checked
data_table content for the 18 Grade 2 Islamic Studies lessons not covered
by the earlier breadth-first batch. Brings Grade 2 Islamic Studies to
full 20/20 coverage.

Content sticks to well-established, uncontroversial facts (the five daily
prayers and their names, the Quran's real Surah count, standard Islamic
greetings) -- nothing fabricated or presented as fact when it's actually
invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "islamic-studies-g2-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Tawheed", "The belief in the oneness of Allah (God)"],
            ["Core concept in", "Islam's central teaching"],
        ]),
    },
    "islamic-studies-g2-l3": {
        "data_table": table(["Value Shown", "Example"], [
            ["Kindness", "Caring for those in need"],
            ["Honesty", "Known as 'Al-Amin' (the trustworthy)"],
        ]),
    },
    "islamic-studies-g2-l4": {
        "data_table": table(["Value", "Example"], [
            ["Honesty", "Telling the truth even when it's hard"],
            ["Trustworthiness", "Keeping a promise you made"],
        ]),
    },
    "islamic-studies-g2-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Number of daily prayers", "5"], ["Prayer names", "Fajr, Dhuhr, Asr, Maghrib, Isha"],
        ]),
    },
    "islamic-studies-g2-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Zakat", "Charity given to those in need"], ["One of the", "Five Pillars of Islam"],
        ]),
    },
    "islamic-studies-g2-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Ramadan is", "The 9th month of the Islamic calendar"],
            ["Main practice", "Fasting from dawn to sunset"],
        ]),
    },
    "islamic-studies-g2-l9": {
        "data_table": table(["Way to Show Respect", "Example"], [
            ["Listening", "Paying attention when they speak"], ["Helping", "Assisting with chores"],
        ]),
    },
    "islamic-studies-g2-l10": {
        "data_table": table(["Kind Action", "Example"], [
            ["Feeding", "Giving a pet food and water"], ["Gentle handling", "Petting an animal softly"],
        ]),
    },
    "islamic-studies-g2-l11": {
        "data_table": table(["Practice", "Purpose"], [
            ["Washing hands before eating", "Cleanliness before meals"],
            ["Wudu (ablution)", "Washing before prayer"],
        ]),
    },
    "islamic-studies-g2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Mosque", "A place where Muslims gather to pray"],
            ["Minaret", "A tower often used for the call to prayer"],
        ]),
    },
    "islamic-studies-g2-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Number of chapters (Surahs)", "114"], ["Longest Surah", "Al-Baqarah"],
        ]),
    },
    "islamic-studies-g2-l14": {
        "data_table": table(["Prophet", "Lesson"], [
            ["Prophet Ayyub (Job)", "Patience through hardship"],
            ["Prophet Nuh (Noah)", "Patience over many years"],
        ]),
    },
    "islamic-studies-g2-l15": {
        "data_table": table(["Sharing Example", "Who Benefits"], [
            ["Sharing food", "Family and friends at the table"], ["Sharing toys", "Playmates"],
        ]),
    },
    "islamic-studies-g2-l16": {
        "data_table": table(["Situation", "Way to Show Gratitude"], [
            ["Receiving a blessing", "Saying 'Alhamdulillah' (praise be to God)"],
            ["Being helped", "Thanking the person"],
        ]),
    },
    "islamic-studies-g2-l17": {
        "data_table": table(["Manner", "Example"], [
            ["Kind speech", "Speaking gently to others"], ["Politeness", "Greeting others warmly"],
        ]),
    },
    "islamic-studies-g2-l18": {
        "data_table": table(["Way to Help", "Example"], [
            ["Charity", "Giving food or money to those who need it"],
            ["Volunteering", "Helping at a community event"],
        ]),
    },
    "islamic-studies-g2-l19": {
        "data_table": table(["Value", "Why It Matters"], [
            ["Truthfulness", "Builds trust between people"],
            ["Lying", "Breaks trust and causes harm"],
        ]),
    },
    "islamic-studies-g2-l20": {
        "data_table": table(["Greeting", "Meaning"], [
            ["As-salamu alaykum", "Peace be upon you"],
            ["Wa alaykumu s-salam", "And upon you be peace (the reply)"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 Islamic Studies lessons (completing 20/20).")


if __name__ == "__main__":
    main()
