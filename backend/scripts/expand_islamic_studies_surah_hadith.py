#!/usr/bin/env python3
"""Add real Quranic-studies (Surah) and Hadith-sciences modules to Islamic
Studies across College 1 through Master's 1 (7 levels), reusing the same
lesson schema as generate_advanced_curriculum.py.

Content covers real Surahs (by name, with a short thematic summary -- not
a reproduction of translated verse text) and real Hadith collections
(Sahih al-Bukhari, Sahih Muslim), their compilation history, structure,
and the sciences used to authenticate them, plus brief, paraphrased
descriptions of a few of the best-known hadith themes (e.g. the hadith on
intention) without quoting any specific published translation verbatim.

Re-run after editing:
    python3 backend/scripts/expand_islamic_studies_surah_hadith.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_advanced_curriculum import LEVEL_IDS, _lesson_for  # noqa: E402

SUBJECT = "Islamic Studies"

# (title, summary) -- summaries describe themes/context/structure only,
# never quoting scripture or hadith translations verbatim.
MODULES: dict[str, list[tuple[str, str]]] = {
    "C1": [
        ("Introduction to Tafsir (Quranic Exegesis)", "Surveys the major approaches to interpreting the Quran, distinguishing tafsir bi'l-ma'thur (interpretation via transmitted reports) from tafsir bi'l-ra'y (reasoned interpretation)."),
        ("Surah Al-Fatiha: The Opening", "Studies the seven-verse opening chapter of the Quran, its central role in daily prayer, and its themes of praise, guidance, and supplication."),
        ("Surah Al-Baqarah: Themes and Structure", "Introduces the Quran's longest chapter, covering its major legal, narrative, and theological themes and its structural place at the start of the Quran."),
        ("Surah Yusuf: Narrative and Moral Themes", "Examines the account of Prophet Yusuf (Joseph) as a sustained single narrative, exploring its themes of patience, forgiveness, and divine providence."),
        ("Introduction to Hadith Sciences (Ulum al-Hadith)", "Introduces the discipline of hadith studies, including the components of a hadith (isnad and matn) and why authentication matters."),
        ("Sahih al-Bukhari: Compilation and Structure", "Surveys the life and methodology of Imam al-Bukhari, the organization of Sahih al-Bukhari into books (kutub) and chapters (abwab), and its status as the most authenticated hadith collection."),
        ("Sahih Muslim: Compilation and Structure", "Surveys Imam Muslim's compilation methodology, his organization by subject matter, and how Sahih Muslim complements Sahih al-Bukhari within the six canonical hadith collections."),
        ("The Hadith of Intention", "Studies the widely cited hadith opening Sahih al-Bukhari's collection, which teaches that the value of an action is determined by the intention behind it, and its foundational role in Islamic legal reasoning."),
    ],
    "C2": [
        ("Surah Al-Kahf: The Cave", "Explores the four narratives of this chapter -- the Companions of the Cave, the two garden owners, Musa and Khidr, and Dhul-Qarnayn -- and their shared themes of faith under trial."),
        ("Surah Maryam: Mary in the Quran", "Studies the chapter narrating the account of Maryam (Mary) and the birth of Isa (Jesus), and its place within Quranic discussions of prophethood."),
        ("Surah Ya-Sin: Themes of Resurrection", "Surveys this widely recited chapter's arguments for the resurrection, monotheism, and prophethood."),
        ("Grades of Hadith Authenticity", "Introduces the classification system used by hadith scholars -- sahih (authentic), hasan (good), da'if (weak) -- and the criteria used to assign each grade."),
        ("Isnad Criticism (Ilm al-Rijal)", "Examines the biographical evaluation of hadith narrators (rijal) used to assess the reliability of a chain of transmission."),
        ("The Six Canonical Hadith Collections (Kutub al-Sittah)", "Surveys Sahih al-Bukhari, Sahih Muslim, and the four Sunan collections (Abu Dawud, al-Tirmidhi, al-Nasa'i, Ibn Majah) and their collective role in Sunni hadith literature."),
        ("The Hadith of Gabriel", "Studies the well-known hadith describing a dialogue that outlines the three dimensions of the religion -- islam, iman, and ihsan -- as a foundational framework in Islamic theology."),
        ("Comparative Approaches to Tafsir", "Compares classical, linguistic, legal, and thematic (mawdu'i) approaches to Quranic commentary across different scholarly traditions."),
    ],
    "UG1": [
        ("Surah An-Nisa: Family and Social Legislation", "Studies this chapter's extensive legal content on family relations, inheritance, and social justice within its historical context."),
        ("Surah Al-Ma'idah: Covenants and Law", "Examines this chapter's themes of covenant, dietary law, and interfaith relations."),
        ("Surah Ar-Rahman: Structure and Refrain", "Studies the repeated refrain structure of this chapter and its themes of divine favor across creation."),
        ("Makki and Madani Surahs", "Distinguishes Quranic chapters revealed before and after the migration to Medina, and how this classification shapes thematic and legal content."),
        ("Introduction to Asbab al-Nuzul (Occasions of Revelation)", "Studies how knowledge of the historical circumstances surrounding a revelation informs its interpretation."),
        ("Hadith Qudsi: Sacred Sayings", "Distinguishes hadith qudsi -- sayings attributed to God but not part of the Quran's textual revelation -- from ordinary prophetic hadith."),
        ("Al-Bukhari's Criteria for Authentication", "Examines the specific methodological standards Imam al-Bukhari applied when selecting hadith for inclusion in his collection."),
        ("Muslim's Introduction (Muqaddimah) to Sahih Muslim", "Studies Imam Muslim's own introductory essay on hadith methodology, considered an early landmark in the science of hadith criticism."),
    ],
    "UG2": [
        ("Surah Al-Isra: The Night Journey", "Studies the chapter referencing the Prophet's night journey and ascension, alongside its ethical instructions."),
        ("Surah Luqman: Wisdom Literature", "Examines this chapter's presentation of parental counsel as a form of wisdom literature within the Quran."),
        ("Naskh: Abrogation in Quranic Studies", "Surveys the classical debate over abrogation (naskh) among verses and its role in Islamic legal theory."),
        ("Comparative Hadith Criticism: Bukhari and Muslim's Shared Narrations", "Studies hadith that appear in both Sahih al-Bukhari and Sahih Muslim (muttafaq 'alayh) and what their agreement signifies for authentication."),
        ("Mursal and Munqati Hadith", "Examines categories of hadith with incomplete chains of transmission and how scholars treat their evidentiary weight."),
        ("The Hadith on the Five Pillars", "Studies the well-known hadith outlining the five pillars of Islam as a structural summary of core practice."),
        ("Women Narrators in Hadith Transmission", "Surveys the significant role of women, including Aisha bint Abi Bakr, in transmitting and preserving hadith."),
        ("Tafsir al-Tabari: A Classical Commentary", "Introduces the historical-linguistic commentary tradition exemplified by al-Tabari's early and influential tafsir."),
    ],
    "UG3": [
        ("Surah Al-Hujurat: Social Ethics", "Studies this chapter's guidance on social conduct, including verification of information and avoiding backbiting."),
        ("Surah Al-Mulk: Themes of Sovereignty", "Examines this chapter's meditations on divine sovereignty over creation and its traditional role in nightly recitation."),
        ("Quranic Linguistics and Rhetorical Style (I'jaz)", "Surveys classical arguments for the Quran's inimitability based on its linguistic and rhetorical structure."),
        ("Hadith Fabrication and the Rise of Isnad Criticism", "Studies the historical emergence of hadith fabrication and how it drove the development of rigorous chain-of-transmission scholarship."),
        ("Al-Tirmidhi's Sunan and Hadith Grading Terminology", "Examines al-Tirmidhi's distinctive practice of explicitly grading each hadith and his contributions to hadith terminology."),
        ("The Hadith on Neighborliness and Social Responsibility", "Studies well-known hadith addressing obligations toward neighbors as a lens on Islamic social ethics."),
        ("Comparative Tafsir: Classical and Modern Approaches", "Compares premodern exegetical methods with modern thematic (mawdu'i) and contextual approaches to Quranic interpretation."),
        ("Hadith in Islamic Legal Theory (Usul al-Fiqh)", "Examines how hadith function as a source of Islamic law alongside the Quran, consensus (ijma), and analogical reasoning (qiyas)."),
    ],
    "UG4": [
        ("Surah Al-Rum: Historical Context and Prophecy", "Studies this chapter's references to regional geopolitics of its era as an example of contextual Quranic interpretation."),
        ("Surah Al-Hujurat Revisited: Etiquette in Community Life", "Extends earlier study of this chapter with a focus on its implications for contemporary community ethics."),
        ("The Compilation History of the Quranic Text (Jam' al-Quran)", "Surveys the historical process by which the Quran was compiled into a single standardized written text under the early caliphs."),
        ("Textual Criticism and Hadith Studies in Comparative Perspective", "Compares methods of hadith authentication with textual-criticism methods used in the study of other religious and historical texts."),
        ("Ibn Hajar al-Asqalani's Commentary on Sahih al-Bukhari (Fath al-Bari)", "Introduces this landmark classical commentary and its enduring influence on later hadith scholarship."),
        ("An-Nawawi's Commentary on Sahih Muslim", "Studies Imam an-Nawawi's widely used commentary and his contributions to hadith terminology and jurisprudential analysis."),
        ("The Forty Hadith Genre (Arba'in Collections)", "Surveys the tradition of compiling forty representative hadith on core themes, exemplified by An-Nawawi's Forty Hadith."),
        ("Contemporary Debates in Hadith Studies", "Surveys ongoing academic conversations, both within and outside the Muslim scholarly tradition, regarding hadith historiography and authentication methods."),
    ],
    "M1": [
        ("Research Methods in Quranic Studies", "Introduces graduate-level research methodology for studying the Quran, including manuscript studies, historical-critical approaches, and traditional tafsir methodology."),
        ("Advanced Seminar: Surah Al-Baqarah's Legal Verses", "A close graduate-level reading of the legal content within Surah Al-Baqarah and its role in shaping classical Islamic jurisprudence."),
        ("Advanced Seminar: Narrative Structure in Surah Yusuf", "A graduate-level literary analysis of narrative technique and characterization within Surah Yusuf."),
        ("Advanced Isnad-Matn Analysis", "Graduate-level training in evaluating both the chain of transmission (isnad) and the content (matn) of a hadith in tandem."),
        ("Seminar: Sahih al-Bukhari's Chapter Headings (Tarajim) as Legal Reasoning", "Studies how al-Bukhari's chapter titles themselves encode subtle legal and theological arguments, a distinctive feature of his methodology."),
        ("Seminar: Sahih Muslim's Thematic Organization", "Examines how Imam Muslim's subject-based arrangement differs from and complements al-Bukhari's structure."),
        ("Hadith and Historical-Critical Scholarship", "Surveys how contemporary scholars, both traditional and academic, engage historical-critical questions about hadith transmission and dating."),
        ("Capstone Research Project: A Surah or Hadith Collection of Choice", "Guides students through an independent graduate-level research project analyzing a chosen Surah's themes or a hadith collection's methodology."),
    ],
}


def main() -> None:
    report = {}
    for level in LEVEL_IDS:
        modules = MODULES.get(level, [])
        if not modules:
            continue
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        subjects = data["subjects"]
        if SUBJECT not in subjects:
            print(f"WARNING: {SUBJECT} not found at {level}, skipping")
            continue
        content = subjects[SUBJECT]
        lessons = content.setdefault("lessons", [])
        existing_titles = {l.get("title") for l in lessons}

        max_idx = 0
        for lesson in lessons:
            m = re.search(r"-l(\d+)$", lesson.get("id", ""))
            if m:
                max_idx = max(max_idx, int(m.group(1)))
        idx = max_idx + 1

        added = 0
        for title, summary in modules:
            if title in existing_titles:
                continue
            lessons.append(_lesson_for(SUBJECT, level, idx, title, summary))
            existing_titles.add(title)
            idx += 1
            added += 1

        quiz_bank = content.setdefault("quiz_bank", [])
        existing_qs = {q.get("question") for q in quiz_bank}
        for title, summary in modules[:4]:
            q = f"What is the focus of the '{title}' module?"
            if q in existing_qs:
                continue
            quiz_bank.append({
                "question": q,
                "type": "multiple_choice",
                "options": [summary, "Not part of this subject at this level",
                            "A topic covered only in an earlier level", "None of the above"],
                "answer": summary,
            })
            existing_qs.add(q)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        report[level] = added

    print("Islamic Studies Surah/Hadith modules added per level:")
    for level, added in report.items():
        print(f"  {level}: +{added}")

    total = 0
    for level in LEVEL_IDS:
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if SUBJECT in data["subjects"]:
            total += len(data["subjects"][SUBJECT].get("lessons", []))
    print(f"Total Islamic Studies lessons across C1-M2: {total}")


if __name__ == "__main__":
    main()
