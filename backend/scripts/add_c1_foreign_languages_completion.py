#!/usr/bin/env python3
"""Depth pass, C1 Foreign Languages: fill in real, hand-checked
data_table content for the 69 C1 Foreign Languages lessons not covered
by the earlier breadth-first batch. Brings C1 Foreign Languages to full
70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "foreign-languages-c1-l1": {
        "data_table": table(["Phrase", "Meaning"], [
            ["Hello / Goodbye", "The most basic conversational opener and closer in any language"],
        ]),
    },
    "foreign-languages-c1-l2": {
        "data_table": table(["Skill", "Focus"], [
            ["Intermediate conversation", "Handling multi-turn exchanges beyond simple Q&A"],
        ]),
    },
    "foreign-languages-c1-l4": {
        "data_table": table(["Language", "Word Order"], [
            ["English", "Subject-Verb-Object"], ["Japanese", "Subject-Object-Verb"],
        ]),
    },
    "foreign-languages-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Phoneme", "The smallest unit of sound that distinguishes meaning in a language"],
        ]),
    },
    "foreign-languages-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Multilingualism", "The regular use of more than one language by an individual or community"],
        ]),
    },
    "foreign-languages-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Interpretation", "Real-time oral translation between languages"], ["Translation", "Written conversion of text between languages"],
        ]),
    },
    "foreign-languages-c1-l8": {
        "data_table": table(["Method", "Feature"], [
            ["Communicative approach", "Emphasizes real-life interaction over rote grammar drills"],
        ]),
    },
    "foreign-languages-c1-l9": {
        "data_table": table(["Tool", "Use"], [
            ["Spaced repetition app", "Schedules vocabulary review at optimal intervals for retention"],
        ]),
    },
    "foreign-languages-c1-l10": {
        "data_table": table(["Element", "Purpose"], [
            ["Target-language-only rule", "Maximizes exposure during an immersion program"],
        ]),
    },
    "foreign-languages-c1-l11": {
        "data_table": table(["Register", "Use"], [
            ["Formal business register", "Used in professional emails and meetings"],
        ]),
    },
    "foreign-languages-c1-l12": {
        "data_table": table(["Concept", "Meaning"], [
            ["Language and identity", "A person's language often shapes their sense of belonging and self"],
        ]),
    },
    "foreign-languages-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Endangered language", "A language at risk of falling out of use as speakers decline"],
        ]),
    },
    "foreign-languages-c1-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Code-switching", "Alternating between two or more languages within a conversation"],
        ]),
    },
    "foreign-languages-c1-l15": {
        "data_table": table(["Framework", "Purpose"], [
            ["CEFR", "Common European Framework of Reference, standardizes language proficiency levels"],
        ]),
    },
    "foreign-languages-c1-l16": {
        "data_table": table(["Benefit", "Detail"], [
            ["Reading native literature", "Exposes learners to authentic idiom and cultural context"],
        ]),
    },
    "foreign-languages-c1-l17": {
        "data_table": table(["Field", "Example Vocabulary"], [
            ["Medical Spanish", "Vocabulary specific to clinical settings"],
        ]),
    },
    "foreign-languages-c1-l18": {
        "data_table": table(["Tool", "Limitation"], [
            ["Machine translation", "Often struggles with idiom, tone, and cultural nuance"],
        ]),
    },
    "foreign-languages-c1-l19": {
        "data_table": table(["Skill", "Benefit"], [
            ["Cultural competency", "Reduces misunderstanding when interacting across cultures"],
        ]),
    },
    "foreign-languages-c1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Heritage learner", "A student with a personal or family connection to the language being studied"],
        ]),
    },
    "foreign-languages-c1-l21": {
        "data_table": table(["Verb", "Yo Form"], [
            ["Hablar (to speak)", "Hablo"], ["Comer (to eat)", "Como"],
        ]),
    },
    "foreign-languages-c1-l22": {
        "data_table": table(["Verb", "Use"], [
            ["Ser", "Permanent characteristics, e.g. Soy alto (I am tall)"], ["Estar", "Temporary states, e.g. Estoy cansado (I am tired)"],
        ]),
    },
    "foreign-languages-c1-l23": {
        "data_table": table(["Spanish", "English"], [
            ["Gracias", "Thank you"], ["Por favor", "Please"],
        ]),
    },
    "foreign-languages-c1-l24": {
        "data_table": table(["Group", "Example Verb"], [
            ["-er verbs", "Parler → je parle"], ["-ir verbs", "Finir → je finis"],
        ]),
    },
    "foreign-languages-c1-l25": {
        "data_table": table(["Gender", "Example"], [
            ["Masculine", "le chat (the cat)"], ["Feminine", "la table (the table)"],
        ]),
    },
    "foreign-languages-c1-l26": {
        "data_table": table(["French", "English"], [
            ["Bonjour", "Hello"], ["Merci", "Thank you"],
        ]),
    },
    "foreign-languages-c1-l27": {
        "data_table": table(["Article", "Gender"], [
            ["der", "Masculine"], ["die", "Feminine"], ["das", "Neuter"],
        ]),
    },
    "foreign-languages-c1-l28": {
        "data_table": table(["Verb", "Ich Form"], [
            ["sprechen (to speak)", "ich spreche"],
        ]),
    },
    "foreign-languages-c1-l29": {
        "data_table": table(["Case", "Use"], [
            ["Nominative", "The subject of a sentence"], ["Accusative", "The direct object of a sentence"],
        ]),
    },
    "foreign-languages-c1-l30": {
        "data_table": table(["Verb", "Io Form"], [
            ["parlare (to speak)", "io parlo"],
        ]),
    },
    "foreign-languages-c1-l31": {
        "data_table": table(["Italian", "English"], [
            ["Il conto, per favore", "The bill, please"],
        ]),
    },
    "foreign-languages-c1-l32": {
        "data_table": table(["Verb", "Eu Form"], [
            ["falar (to speak)", "eu falo"],
        ]),
    },
    "foreign-languages-c1-l33": {
        "data_table": table(["Verb", "Use"], [
            ["Ser", "Permanent qualities"], ["Estar", "Temporary states or location"],
        ]),
    },
    "foreign-languages-c1-l34": {
        "data_table": table(["Tone", "Meaning Example"], [
            ["mā (first tone)", "Mother"], ["mǎ (third tone)", "Horse"],
        ]),
    },
    "foreign-languages-c1-l35": {
        "data_table": table(["Structure", "Example"], [
            ["Subject-Verb-Object", "Wǒ chī fàn (I eat rice)"],
        ]),
    },
    "foreign-languages-c1-l36": {
        "data_table": table(["Script", "Use"], [
            ["Hiragana", "Native Japanese words and grammar"], ["Katakana", "Foreign loanwords"],
        ]),
    },
    "foreign-languages-c1-l37": {
        "data_table": table(["Particle", "Function"], [
            ["wa", "Marks the topic of a sentence"], ["ga", "Marks the grammatical subject"],
        ]),
    },
    "foreign-languages-c1-l38": {
        "data_table": table(["Feature", "Detail"], [
            ["Hangul", "A phonetic writing system designed for Korean in the 15th century"],
        ]),
    },
    "foreign-languages-c1-l39": {
        "data_table": table(["Structure", "Order"], [
            ["Korean sentence", "Subject-Object-Verb"],
        ]),
    },
    "foreign-languages-c1-l40": {
        "data_table": table(["Feature", "Detail"], [
            ["Arabic script", "Written right to left, with connected letterforms"],
        ]),
    },
    "foreign-languages-c1-l41": {
        "data_table": table(["Arabic", "English"], [
            ["Marhaban", "Hello"], ["Shukran", "Thank you"],
        ]),
    },
    "foreign-languages-c1-l42": {
        "data_table": table(["Feature", "Detail"], [
            ["Cyrillic alphabet", "Used for Russian and several other Slavic languages"],
        ]),
    },
    "foreign-languages-c1-l43": {
        "data_table": table(["Case", "Use"], [
            ["Nominative", "The subject of the sentence"], ["Genitive", "Indicates possession"],
        ]),
    },
    "foreign-languages-c1-l44": {
        "data_table": table(["Declension", "Example"], [
            ["First declension", "Feminine nouns ending in -a, like puella (girl)"],
        ]),
    },
    "foreign-languages-c1-l45": {
        "data_table": table(["Conjugation", "Example Verb"], [
            ["First conjugation", "amare (to love) → amo"],
        ]),
    },
    "foreign-languages-c1-l46": {
        "data_table": table(["Element", "Purpose"], [
            ["Fingerspelling", "Spells out words letter by letter using the manual alphabet"],
        ]),
    },
    "foreign-languages-c1-l47": {
        "data_table": table(["Sign", "Meaning"], [
            ["Thank you", "Flat hand moved from chin outward"],
        ]),
    },
    "foreign-languages-c1-l48": {
        "data_table": table(["Swahili", "English"], [
            ["Jambo", "Hello"], ["Asante", "Thank you"],
        ]),
    },
    "foreign-languages-c1-l49": {
        "data_table": table(["Feature", "Detail"], [
            ["Devanagari", "A syllabic script used for Hindi and Sanskrit"],
        ]),
    },
    "foreign-languages-c1-l50": {
        "data_table": table(["Structure", "Order"], [
            ["Hindi sentence", "Subject-Object-Verb"],
        ]),
    },
    "foreign-languages-c1-l51": {
        "data_table": table(["Tense", "Use"], [
            ["Preterite", "Completed actions in the past"], ["Imperfect", "Ongoing or habitual past actions"],
        ]),
    },
    "foreign-languages-c1-l52": {
        "data_table": table(["Method", "Example"], [
            ["Intonation rise", "Turning a statement into a question by rising pitch"],
        ]),
    },
    "foreign-languages-c1-l53": {
        "data_table": table(["Modal Verb", "Meaning"], [
            ["können", "can / to be able to"], ["müssen", "must / to have to"],
        ]),
    },
    "foreign-languages-c1-l54": {
        "data_table": table(["Article Type", "Example"], [
            ["Definite", "il libro (the book)"], ["Indefinite", "un libro (a book)"],
        ]),
    },
    "foreign-languages-c1-l55": {
        "data_table": table(["Measure Word", "Used For"], [
            ["ge", "General-purpose measure word for many objects"],
        ]),
    },
    "foreign-languages-c1-l56": {
        "data_table": table(["Form", "Example"], [
            ["Present (-masu)", "tabemasu (eat)"], ["Past (-mashita)", "tabemashita (ate)"],
        ]),
    },
    "foreign-languages-c1-l57": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Reading graded readers", "Builds vocabulary with comprehensible input"],
        ]),
    },
    "foreign-languages-c1-l58": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Reading simple dialogues", "Models natural conversational rhythm and phrasing"],
        ]),
    },
    "foreign-languages-c1-l59": {
        "data_table": table(["Language", "One"], [
            ["Spanish", "uno"], ["French", "un"], ["German", "eins"],
        ]),
    },
    "foreign-languages-c1-l60": {
        "data_table": table(["Type", "Example"], [
            ["True cognate", "Spanish 'información' / English 'information'"], ["False friend", "Spanish 'embarazada' does not mean 'embarrassed'"],
        ]),
    },
    "foreign-languages-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Holding a basic exchange", "Introducing oneself and asking simple questions"],
        ]),
    },
    "foreign-languages-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Sustaining a longer dialogue", "Discussing preferences and giving reasons"],
        ]),
    },
    "foreign-languages-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Applying acquisition theory", "Explaining why comprehensible input speeds learning"],
        ]),
    },
    "foreign-languages-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Comparing grammar structures", "Contrasting verb placement across two languages"],
        ]),
    },
    "foreign-languages-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Identifying sounds", "Distinguishing two similar phonemes by ear"],
        ]),
    },
    "foreign-languages-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Observing code-switching", "Noting when a bilingual speaker shifts languages mid-sentence"],
        ]),
    },
    "foreign-languages-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Comparing translation choices", "Evaluating two translations of the same phrase for nuance"],
        ]),
    },
    "foreign-languages-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a teaching method", "Selecting an activity that matches a communicative approach"],
        ]),
    },
    "foreign-languages-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Using a learning app", "Setting up a spaced-repetition vocabulary deck"],
        ]),
    },
    "foreign-languages-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Designing an immersion activity", "Planning a target-language-only cooking class"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Foreign Languages"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Foreign Languages lessons (completing 70/70).")


if __name__ == "__main__":
    main()
