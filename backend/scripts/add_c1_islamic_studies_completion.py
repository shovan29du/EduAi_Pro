#!/usr/bin/env python3
"""Depth pass, C1 Islamic Studies: fill in real, hand-checked data_table
content for the 69 C1 Islamic Studies lessons not covered by the earlier
breadth-first batch. Brings C1 Islamic Studies to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "islamic-studies-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Quran", "The central religious text of Islam, believed to be revealed to Muhammad"],
        ]),
    },
    "islamic-studies-c1-l2": {
        "data_table": table(["Period", "Feature"], [
            ["Islamic Golden Age", "Flourishing of science, philosophy, and culture under the Abbasid Caliphate"],
        ]),
    },
    "islamic-studies-c1-l4": {
        "data_table": table(["Feature", "Detail"], [
            ["Surah Al-Fatiha", "The opening chapter of the Quran, recited in every prayer"],
        ]),
    },
    "islamic-studies-c1-l5": {
        "data_table": table(["Feature", "Detail"], [
            ["Surah Al-Baqarah", "The longest chapter of the Quran, covering law, faith, and guidance"],
        ]),
    },
    "islamic-studies-c1-l6": {
        "data_table": table(["Feature", "Detail"], [
            ["Surah Yusuf", "Narrates the story of Prophet Joseph, emphasizing patience and forgiveness"],
        ]),
    },
    "islamic-studies-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Ulum al-Hadith", "The sciences used to authenticate and classify hadith reports"],
        ]),
    },
    "islamic-studies-c1-l8": {
        "data_table": table(["Feature", "Detail"], [
            ["Sahih al-Bukhari", "A major hadith collection compiled by Imam Bukhari"],
        ]),
    },
    "islamic-studies-c1-l9": {
        "data_table": table(["Feature", "Detail"], [
            ["Sahih Muslim", "A major hadith collection compiled by Imam Muslim"],
        ]),
    },
    "islamic-studies-c1-l10": {
        "data_table": table(["Feature", "Detail"], [
            ["Hadith of Intention", "States that actions are judged by their underlying intentions"],
        ]),
    },
    "islamic-studies-c1-l11": {
        "data_table": table(["Period", "Feature"], [
            ["Meccan period", "Early revelations focused on monotheism and faith"],
        ]),
    },
    "islamic-studies-c1-l12": {
        "data_table": table(["Period", "Feature"], [
            ["Medinan period", "Established the first Muslim community and civic laws"],
        ]),
    },
    "islamic-studies-c1-l13": {
        "data_table": table(["Caliph", "Order"], [
            ["Abu Bakr", "First Rashidun caliph"], ["Umar ibn al-Khattab", "Second Rashidun caliph"],
        ]),
    },
    "islamic-studies-c1-l14": {
        "data_table": table(["Feature", "Detail"], [
            ["Umayyad Caliphate", "Expanded Islamic rule from Spain to Central Asia"],
        ]),
    },
    "islamic-studies-c1-l15": {
        "data_table": table(["Feature", "Detail"], [
            ["Abbasid Caliphate", "Era of major advances in science, medicine, and philosophy"],
        ]),
    },
    "islamic-studies-c1-l16": {
        "data_table": table(["Source", "Role"], [
            ["Quran", "Primary source of Islamic law"], ["Sunnah", "The practices and sayings of the Prophet"],
        ]),
    },
    "islamic-studies-c1-l17": {
        "data_table": table(["Pillar", "Practice"], [
            ["Shahada", "Declaration of faith"], ["Salah", "Five daily prayers"], ["Zakat", "Almsgiving"], ["Sawm", "Fasting during Ramadan"], ["Hajj", "Pilgrimage to Mecca"],
        ]),
    },
    "islamic-studies-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Aqidah", "The core system of beliefs in Islamic theology"],
        ]),
    },
    "islamic-studies-c1-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Tawhid", "The Islamic concept of the absolute oneness of God"],
        ]),
    },
    "islamic-studies-c1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Sufism", "The mystical dimension of Islam focused on spiritual purification"],
        ]),
    },
    "islamic-studies-c1-l21": {
        "data_table": table(["Feature", "Detail"], [
            ["Islamic art", "Often avoids figurative imagery, favoring geometric and calligraphic design"],
        ]),
    },
    "islamic-studies-c1-l22": {
        "data_table": table(["Feature", "Purpose"], [
            ["Minaret", "Tower from which the call to prayer is announced"], ["Mihrab", "Niche indicating the direction of prayer"],
        ]),
    },
    "islamic-studies-c1-l23": {
        "data_table": table(["Script", "Feature"], [
            ["Kufic", "An early, angular calligraphic script"], ["Naskh", "A rounded, widely used script for the Quran"],
        ]),
    },
    "islamic-studies-c1-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Madhab", "A school of jurisprudence interpreting Islamic law"],
        ]),
    },
    "islamic-studies-c1-l25": {
        "data_table": table(["Feature", "Detail"], [
            ["Hanafi school", "Founded by Abu Hanifa, widely followed in South and Central Asia"],
        ]),
    },
    "islamic-studies-c1-l26": {
        "data_table": table(["Feature", "Detail"], [
            ["Maliki school", "Founded by Imam Malik, widely followed in North and West Africa"],
        ]),
    },
    "islamic-studies-c1-l27": {
        "data_table": table(["Feature", "Detail"], [
            ["Shafi'i school", "Founded by Imam al-Shafi'i, widely followed in East Africa and Southeast Asia"],
        ]),
    },
    "islamic-studies-c1-l28": {
        "data_table": table(["Feature", "Detail"], [
            ["Hanbali school", "Founded by Ahmad ibn Hanbal, widely followed in the Arabian Peninsula"],
        ]),
    },
    "islamic-studies-c1-l29": {
        "data_table": table(["Principle", "Meaning"], [
            ["Adl", "Justice and fairness in all dealings"],
        ]),
    },
    "islamic-studies-c1-l30": {
        "data_table": table(["Principle", "Meaning"], [
            ["Honest weights and measures", "A core requirement in Islamic commercial ethics"],
        ]),
    },
    "islamic-studies-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Riba", "Interest or usury, prohibited in Islamic financial transactions"],
        ]),
    },
    "islamic-studies-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Zakat", "An obligatory annual charitable contribution, typically 2.5% of savings"],
        ]),
    },
    "islamic-studies-c1-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Waqf", "An inalienable charitable endowment used for religious or social purposes"],
        ]),
    },
    "islamic-studies-c1-l34": {
        "data_table": table(["Principle", "Meaning"], [
            ["Islamic economics", "Economic activity guided by Islamic ethical and legal principles"],
        ]),
    },
    "islamic-studies-c1-l35": {
        "data_table": table(["Figure", "Contribution"], [
            ["Khadijah", "The Prophet's first wife and a successful merchant"],
        ]),
    },
    "islamic-studies-c1-l36": {
        "data_table": table(["Feature", "Detail"], [
            ["Khadijah bint Khuwaylid", "First person to accept Islam and a key early supporter"],
        ]),
    },
    "islamic-studies-c1-l37": {
        "data_table": table(["Feature", "Detail"], [
            ["Aisha bint Abi Bakr", "Narrated a large number of hadith and was a respected scholar"],
        ]),
    },
    "islamic-studies-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Falsafa", "The tradition of Islamic philosophy engaging with Greek thought"],
        ]),
    },
    "islamic-studies-c1-l39": {
        "data_table": table(["Figure", "Contribution"], [
            ["Al-Kindi", "Known as the first Islamic philosopher, integrated Greek philosophy"],
        ]),
    },
    "islamic-studies-c1-l40": {
        "data_table": table(["Figure", "Contribution"], [
            ["Al-Farabi", "Wrote on political philosophy and the ideal state"],
        ]),
    },
    "islamic-studies-c1-l41": {
        "data_table": table(["Figure", "Contribution"], [
            ["Ibn Sina", "Wrote The Canon of Medicine, a foundational medical text"],
        ]),
    },
    "islamic-studies-c1-l42": {
        "data_table": table(["Figure", "Contribution"], [
            ["Al-Ghazali", "Wrote The Revival of the Religious Sciences, blending law and spirituality"],
        ]),
    },
    "islamic-studies-c1-l43": {
        "data_table": table(["Contribution", "Detail"], [
            ["Star catalogs", "Islamic astronomers refined observations of celestial bodies"],
        ]),
    },
    "islamic-studies-c1-l44": {
        "data_table": table(["Figure", "Contribution"], [
            ["Al-Khwarizmi", "His work gave rise to the term 'algebra' and 'algorithm'"],
        ]),
    },
    "islamic-studies-c1-l45": {
        "data_table": table(["Figure", "Contribution"], [
            ["Ibn al-Haytham", "Pioneered the scientific method in the study of optics"],
        ]),
    },
    "islamic-studies-c1-l46": {
        "data_table": table(["Feature", "Detail"], [
            ["House of Wisdom", "A major intellectual center in Baghdad for translation and research"],
        ]),
    },
    "islamic-studies-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Convivencia", "A period of relative coexistence among Muslims, Christians, and Jews in Al-Andalus"],
        ]),
    },
    "islamic-studies-c1-l48": {
        "data_table": table(["Feature", "Detail"], [
            ["Ottoman Empire", "Governed a vast, multi-ethnic empire for over 600 years"],
        ]),
    },
    "islamic-studies-c1-l49": {
        "data_table": table(["Feature", "Detail"], [
            ["Mughal Empire", "Islamic dynasty that ruled much of South Asia, known for architecture like the Taj Mahal"],
        ]),
    },
    "islamic-studies-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Comparative religion", "The study of similarities and differences across world religions"],
        ]),
    },
    "islamic-studies-c1-l51": {
        "data_table": table(["Shared Root", "Detail"], [
            ["Abrahamic tradition", "Both Islam and Judaism trace lineage to Prophet Abraham"],
        ]),
    },
    "islamic-studies-c1-l52": {
        "data_table": table(["Shared Element", "Detail"], [
            ["Jesus", "Recognized as a prophet in Islam and central to Christianity"],
        ]),
    },
    "islamic-studies-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Ahl al-Kitab", "'People of the Book,' referring to Jews and Christians in Islamic tradition"],
        ]),
    },
    "islamic-studies-c1-l54": {
        "data_table": table(["Concept", "Meaning"], [
            ["Prophethood", "Islam recognizes a chain of prophets, with Muhammad as the final one"],
        ]),
    },
    "islamic-studies-c1-l55": {
        "data_table": table(["Tradition", "Feature"], [
            ["Islamic creation account", "Describes God creating the heavens and earth in six days"],
        ]),
    },
    "islamic-studies-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Madrasa", "A traditional Islamic institution of learning"],
        ]),
    },
    "islamic-studies-c1-l57": {
        "data_table": table(["Feature", "Detail"], [
            ["Al-Azhar University", "One of the oldest and most prestigious centers of Islamic learning, in Cairo"],
        ]),
    },
    "islamic-studies-c1-l58": {
        "data_table": table(["Topic", "Focus"], [
            ["Islamic family law", "Governs marriage, divorce, inheritance, and guardianship"],
        ]),
    },
    "islamic-studies-c1-l59": {
        "data_table": table(["Principle", "Meaning"], [
            ["Sadaqah", "Voluntary charity given beyond the obligatory zakat"],
        ]),
    },
    "islamic-studies-c1-l60": {
        "data_table": table(["Country", "Feature"], [
            ["Indonesia", "The world's largest Muslim-majority country by population"],
        ]),
    },
    "islamic-studies-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing early revelation themes", "Tracing monotheism and moral guidance in Meccan surahs"],
        ]),
    },
    "islamic-studies-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing community formation", "Examining the Constitution of Medina's role in civic life"],
        ]),
    },
    "islamic-studies-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing imperial administration", "Comparing Umayyad governance across distant provinces"],
        ]),
    },
    "islamic-studies-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting a Quranic passage", "Applying tafsir methods to a short verse"],
        ]),
    },
    "islamic-studies-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Tracing civilizational contributions", "Linking Abbasid-era scholarship to modern science"],
        ]),
    },
    "islamic-studies-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Comparing exegetical approaches", "Contrasting linguistic and thematic tafsir methods"],
        ]),
    },
    "islamic-studies-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing recitation structure", "Examining why Al-Fatiha is recited in every prayer cycle"],
        ]),
    },
    "islamic-studies-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing legal themes", "Identifying verses in Al-Baqarah related to conduct and law"],
        ]),
    },
    "islamic-studies-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing narrative structure", "Tracing the moral arc of the story of Yusuf"],
        ]),
    },
    "islamic-studies-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating hadith authenticity", "Applying isnad analysis to assess a hadith's chain of narration"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Islamic Studies lessons (completing 70/70).")


if __name__ == "__main__":
    main()
