#!/usr/bin/env python3
"""Depth pass, C2 Islamic Studies: fill in real, hand-checked data_table
content for the 69 C2 Islamic Studies lessons not covered by the earlier
breadth-first batch. Brings C2 Islamic Studies to full 70/70 coverage.

l61-l62 are "Foundations 2" lessons revisiting l16 and l23; l63-l70 are
"Worked Analysis" companions to l1-l8. Both reuse the underlying
data_table of their source lesson. l3 was already completed by an
earlier breadth-first batch, so its data_table is hard-coded for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "islamic-studies-c2-l1": {
        "data_table": table(["Era", "Feature"], [
            ["Islamic history & civilization", "Spans the Prophetic era through successive caliphates and empires"],
        ]),
    },
    "islamic-studies-c2-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Islamic ethics & jurisprudence", "Grounds moral and legal reasoning in Quran, Sunnah, and scholarly consensus"],
        ]),
    },
    "islamic-studies-c2-l4": {
        "data_table": table(["Surah", "Theme"], [
            ["Maryam", "Recounts the story of Mary and the birth of Jesus with emphasis on devotion"],
        ]),
    },
    "islamic-studies-c2-l5": {
        "data_table": table(["Surah", "Theme"], [
            ["Ya-Sin", "Centers on resurrection, prophethood, and the signs of God's power"],
        ]),
    },
    "islamic-studies-c2-l6": {
        "data_table": table(["Grade", "Meaning"], [
            ["Sahih", "Authentic hadith with an unbroken, reliable chain of narrators"],
            ["Da'if", "Weak hadith with a questionable chain or content"],
        ]),
    },
    "islamic-studies-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Isnad criticism", "Scholarly evaluation of a hadith's chain of narrators for reliability"],
        ]),
    },
    "islamic-studies-c2-l8": {
        "data_table": table(["Collection", "Compiler"], [
            ["Sahih al-Bukhari", "Muhammad al-Bukhari"],
            ["Sahih Muslim", "Muslim ibn al-Hajjaj"],
        ]),
    },
    "islamic-studies-c2-l9": {
        "data_table": table(["Hadith", "Significance"], [
            ["Hadith of Gabriel", "Outlines the pillars of Islam, Iman, and Ihsan in dialogue form"],
        ]),
    },
    "islamic-studies-c2-l10": {
        "data_table": table(["Approach", "Focus"], [
            ["Tafsir bi al-ma'thur", "Interprets Quran using Quran, hadith, and companion reports"],
            ["Tafsir bi al-ra'y", "Interprets Quran using scholarly reasoning"],
        ]),
    },
    "islamic-studies-c2-l11": {
        "data_table": table(["Source Type", "Example"], [
            ["Sira literature", "Biographical accounts of the Prophet's life, e.g. Ibn Ishaq's work"],
        ]),
    },
    "islamic-studies-c2-l12": {
        "data_table": table(["Caliph", "Note"], [
            ["Abu Bakr", "First Rightly Guided Caliph, addressed the Ridda wars"],
        ]),
    },
    "islamic-studies-c2-l13": {
        "data_table": table(["Dynasty", "Feature"], [
            ["Umayyad", "Hereditary caliphate centered in Damascus"],
            ["Abbasid", "Overthrew the Umayyads, moved the capital to Baghdad"],
        ]),
    },
    "islamic-studies-c2-l14": {
        "data_table": table(["Institution", "Role"], [
            ["Bayt al-Hikma", "Translation and research center that preserved and advanced classical scholarship"],
        ]),
    },
    "islamic-studies-c2-l15": {
        "data_table": table(["Concept", "Meaning"], [
            ["Usul al-Fiqh", "Methodology governing how Islamic legal rulings are derived from sources"],
        ]),
    },
    "islamic-studies-c2-l16": {
        "data_table": table(["Objective", "Category"], [
            ["Maqasid al-Shariah", "Preservation of religion, life, intellect, lineage, and property"],
        ]),
    },
    "islamic-studies-c2-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Ijtihad", "Independent legal reasoning to derive rulings"],
            ["Taqlid", "Following an established legal school's rulings"],
        ]),
    },
    "islamic-studies-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Qiyas", "Analogical reasoning applying an existing ruling to a new case"],
            ["Ijma", "Scholarly consensus on a legal matter"],
        ]),
    },
    "islamic-studies-c2-l19": {
        "data_table": table(["School", "Founder"], [
            ["Ash'ari", "Abu al-Hasan al-Ash'ari"],
            ["Maturidi", "Abu Mansur al-Maturidi"],
        ]),
    },
    "islamic-studies-c2-l20": {
        "data_table": table(["Movement", "Feature"], [
            ["Mu'tazila", "Emphasized reason and free will in early Islamic theology"],
        ]),
    },
    "islamic-studies-c2-l21": {
        "data_table": table(["Position", "View"], [
            ["Qadariyya", "Emphasized human free will"],
            ["Jabriyya", "Emphasized predestination"],
        ]),
    },
    "islamic-studies-c2-l22": {
        "data_table": table(["Order", "Founder"], [
            ["Qadiriyya", "Abdul Qadir Gilani"],
            ["Naqshbandi", "Baha-ud-Din Naqshband"],
        ]),
    },
    "islamic-studies-c2-l23": {
        "data_table": table(["Doctrine", "Meaning"], [
            ["Wahdat al-Wujud", "Ibn Arabi's concept of the unity of existence within divine reality"],
        ]),
    },
    "islamic-studies-c2-l24": {
        "data_table": table(["Figure", "Contribution"], [
            ["Rumi", "Persian poet whose mystical verse expressed themes of divine love and union"],
        ]),
    },
    "islamic-studies-c2-l25": {
        "data_table": table(["Style", "Region"], [
            ["Mughal architecture", "South Asia — marble domes and intricate inlay work"],
            ["Ottoman architecture", "Anatolia — large central domes and slender minarets"],
        ]),
    },
    "islamic-studies-c2-l26": {
        "data_table": table(["Site", "Significance"], [
            ["Dome of the Rock", "Marks a site of major religious significance in Jerusalem"],
        ]),
    },
    "islamic-studies-c2-l27": {
        "data_table": table(["Element", "Symbolism"], [
            ["Geometric pattern", "Reflects infinite divine order through repeating, non-figurative design"],
        ]),
    },
    "islamic-studies-c2-l28": {
        "data_table": table(["Madhab", "Founder"], [
            ["Hanafi", "Abu Hanifa"], ["Maliki", "Malik ibn Anas"],
            ["Shafi'i", "Al-Shafi'i"], ["Hanbali", "Ahmad ibn Hanbal"],
        ]),
    },
    "islamic-studies-c2-l29": {
        "data_table": table(["School", "Feature"], [
            ["Ja'fari jurisprudence", "Shia legal school named after Ja'far al-Sadiq"],
        ]),
    },
    "islamic-studies-c2-l30": {
        "data_table": table(["Divide", "Origin"], [
            ["Sunni-Shia split", "Rooted in a dispute over rightful succession after the Prophet's death"],
        ]),
    },
    "islamic-studies-c2-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Islamic business ethics", "Contracts must avoid excessive uncertainty (gharar) and exploitation"],
        ]),
    },
    "islamic-studies-c2-l32": {
        "data_table": table(["Structure", "Purpose"], [
            ["Mudarabah", "Profit-sharing partnership structured to avoid interest (riba)"],
        ]),
    },
    "islamic-studies-c2-l33": {
        "data_table": table(["Institution", "Role"], [
            ["Zakat administration", "Historically and today collects and redistributes obligatory almsgiving"],
        ]),
    },
    "islamic-studies-c2-l34": {
        "data_table": table(["Institution", "Role"], [
            ["Waqf", "Charitable endowment historically funding schools, hospitals, and public works"],
        ]),
    },
    "islamic-studies-c2-l35": {
        "data_table": table(["Work", "Contribution"], [
            ["Muqaddimah", "Ibn Khaldun's foundational work on the philosophy of history and economics"],
        ]),
    },
    "islamic-studies-c2-l36": {
        "data_table": table(["Scholar", "Field"], [
            ["Aisha bint Abi Bakr", "Major early narrator of hadith and legal authority"],
        ]),
    },
    "islamic-studies-c2-l37": {
        "data_table": table(["Figure", "Contribution"], [
            ["Fatima al-Fihri", "Founded Al-Qarawiyyin, among the oldest continuously operating institutions of learning"],
        ]),
    },
    "islamic-studies-c2-l38": {
        "data_table": table(["Figure", "Contribution"], [
            ["Ibn Rushd (Averroes)", "Argued for the compatibility of philosophical reason and religious revelation"],
        ]),
    },
    "islamic-studies-c2-l39": {
        "data_table": table(["Figure", "Contribution"], [
            ["Al-Biruni", "Pioneered comparative, empirical methods in studying other religions and cultures"],
        ]),
    },
    "islamic-studies-c2-l40": {
        "data_table": table(["Figure", "Contribution"], [
            ["Ibn Khaldun", "Developed early theories of social cohesion (asabiyyah) shaping historical change"],
        ]),
    },
    "islamic-studies-c2-l41": {
        "data_table": table(["Figure", "Contribution"], [
            ["Al-Razi", "Advanced clinical medicine and distinguished smallpox from measles"],
            ["Ibn Sina", "Authored the Canon of Medicine, a standard text for centuries"],
        ]),
    },
    "islamic-studies-c2-l42": {
        "data_table": table(["Contribution", "Detail"], [
            ["Islamic astronomy", "Built major observatories and refined instruments like the astrolabe"],
        ]),
    },
    "islamic-studies-c2-l43": {
        "data_table": table(["Movement", "Impact"], [
            ["Translation movement", "Preserved and transmitted Greek philosophical and scientific texts to later Europe"],
        ]),
    },
    "islamic-studies-c2-l44": {
        "data_table": table(["Region", "Feature"], [
            ["Al-Andalus", "Period of notable interfaith scholarly exchange in Islamic Iberia"],
        ]),
    },
    "islamic-studies-c2-l45": {
        "data_table": table(["System", "Feature"], [
            ["Ottoman millet system", "Granted religious communities self-governance over communal affairs"],
        ]),
    },
    "islamic-studies-c2-l46": {
        "data_table": table(["Policy", "Detail"], [
            ["Din-i-Ilahi", "Akbar's syncretic religious policy promoting tolerance across faiths"],
        ]),
    },
    "islamic-studies-c2-l47": {
        "data_table": table(["Tradition", "Feature"], [
            ["Islamic and Jewish law", "Both developed detailed legal traditions rooted in scripture and scholarly interpretation"],
        ]),
    },
    "islamic-studies-c2-l48": {
        "data_table": table(["Tradition", "View of Jesus"], [
            ["Islamic view", "Regards Jesus as a revered prophet, not divine"],
        ]),
    },
    "islamic-studies-c2-l49": {
        "data_table": table(["Tradition", "Concept"], [
            ["Islamic eschatology", "Describes a Day of Judgment with resurrection and divine accounting"],
        ]),
    },
    "islamic-studies-c2-l50": {
        "data_table": table(["Practice", "Goal"], [
            ["Interfaith dialogue", "Seeks mutual understanding across religious traditions"],
        ]),
    },
    "islamic-studies-c2-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Religious pluralism", "Islamic scholarship offers varied perspectives on coexistence with other faiths"],
        ]),
    },
    "islamic-studies-c2-l52": {
        "data_table": table(["Movement", "Focus"], [
            ["Legal reform movements", "Seek to reinterpret classical rulings for contemporary contexts"],
        ]),
    },
    "islamic-studies-c2-l53": {
        "data_table": table(["Field", "Example Issue"], [
            ["Islamic bioethics", "Addresses questions like organ donation and end-of-life care"],
        ]),
    },
    "islamic-studies-c2-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental stewardship", "Islamic teaching frames humans as trustees (khalifah) responsible for creation"],
        ]),
    },
    "islamic-studies-c2-l55": {
        "data_table": table(["Discourse", "Detail"], [
            ["Human rights in Islamic law", "Scholars debate how classical sources align with modern rights frameworks"],
        ]),
    },
    "islamic-studies-c2-l56": {
        "data_table": table(["Movement", "Focus"], [
            ["Islamic feminism", "Reinterprets textual sources to address gender equity within an Islamic framework"],
        ]),
    },
    "islamic-studies-c2-l57": {
        "data_table": table(["Movement", "Focus"], [
            ["Islamic modernism", "Seeks to reconcile Islamic tradition with modern institutions and science"],
        ]),
    },
    "islamic-studies-c2-l58": {
        "data_table": table(["Topic", "Detail"], [
            ["Muslim minorities in the West", "Navigate identity formation while adapting to secular or plural societies"],
        ]),
    },
    "islamic-studies-c2-l59": {
        "data_table": table(["Sector", "Detail"], [
            ["Islamic finance", "A growing global sector offering interest-free financial products"],
        ]),
    },
    "islamic-studies-c2-l60": {
        "data_table": table(["Trend", "Detail"], [
            ["Digital-age scholarship", "Online platforms have expanded access to Islamic scholarly discourse"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Surah", "Theme"], [
    ["Al-Kahf", "Themes of faith, trials, and divine guidance told through four parables"],
])

# l61-l62 "Foundations 2" lessons revisit l16 and l23.
FOUNDATIONS_2_MAP = {61: 16, 62: 23}
for worked_n, base_n in FOUNDATIONS_2_MAP.items():
    base_key = f"islamic-studies-c2-l{base_n}"
    CHARTS[f"islamic-studies-c2-l{worked_n}"] = {
        "data_table": CHARTS[base_key]["data_table"],
    }

# l63-l70 "Worked Analysis" lessons reuse the data_table of l1-l8.
WORKED_ANALYSIS_MAP = {63: 1, 64: 2, 65: 3, 66: 4, 67: 5, 68: 6, 69: 7, 70: 8}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"islamic-studies-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"islamic-studies-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"islamic-studies-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Islamic Studies lessons (completing 70/70).")


if __name__ == "__main__":
    main()
