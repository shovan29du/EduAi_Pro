#!/usr/bin/env python3
"""Depth pass, C2 Foreign Languages: fill in real, hand-checked
data_table content for the 69 C2 Foreign Languages lessons not covered
by the earlier breadth-first batch. Brings C2 Foreign Languages to
full 70/70 coverage.

l61-l70 are "Worked Analysis" companions to l1-l10. l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "foreign-languages-c2-l1": {
        "data_table": table(["Skill", "Feature"], [
            ["Intermediate grammar & conversation", "Consolidates tense usage and everyday conversational fluency"],
        ]),
    },
    "foreign-languages-c2-l2": {
        "data_table": table(["Skill", "Feature"], [
            ["Advanced reading & writing", "Builds ability to read authentic texts and write structured prose"],
        ]),
    },
    "foreign-languages-c2-l4": {
        "data_table": table(["Language Pair", "Structural Difference"], [
            ["English vs. Spanish", "Spanish marks gender and number agreement across nouns and adjectives"],
        ]),
    },
    "foreign-languages-c2-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Phoneme", "The smallest sound unit that distinguishes meaning in a language"],
        ]),
    },
    "foreign-languages-c2-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Multilingual sociolinguistics", "Studies how language choice signals identity and social context"],
        ]),
    },
    "foreign-languages-c2-l7": {
        "data_table": table(["Mode", "Detail"], [
            ["Translation", "Converts written text between languages"],
            ["Interpretation", "Converts spoken language in real time"],
        ]),
    },
    "foreign-languages-c2-l8": {
        "data_table": table(["Method", "Focus"], [
            ["Communicative approach", "Prioritizes meaningful interaction over rote grammar drilling"],
        ]),
    },
    "foreign-languages-c2-l9": {
        "data_table": table(["Tool", "Use"], [
            ["Computer-assisted language learning", "Uses software and adaptive feedback to support language practice"],
        ]),
    },
    "foreign-languages-c2-l10": {
        "data_table": table(["Element", "Purpose"], [
            ["Immersion program design", "Maximizes target-language exposure across structured daily activities"],
        ]),
    },
    "foreign-languages-c2-l11": {
        "data_table": table(["Register", "Use"], [
            ["Business register", "Formal vocabulary and tone suited to professional correspondence"],
        ]),
    },
    "foreign-languages-c2-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Language and identity", "A speaker's language choices shape and express cultural belonging"],
        ]),
    },
    "foreign-languages-c2-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Endangered language", "A language at risk of no longer being passed to new generations"],
        ]),
    },
    "foreign-languages-c2-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Code-switching", "Alternating between languages or dialects within a conversation"],
        ]),
    },
    "foreign-languages-c2-l15": {
        "data_table": table(["Assessment Type", "Focus"], [
            ["Proficiency test", "Measures overall functional ability rather than course-specific content"],
        ]),
    },
    "foreign-languages-c2-l16": {
        "data_table": table(["Genre", "Value"], [
            ["Target-language literature", "Exposes learners to authentic idiom, culture, and stylistic range"],
        ]),
    },
    "foreign-languages-c2-l17": {
        "data_table": table(["Domain", "Vocabulary Focus"], [
            ["Language for specific purposes", "Tailors vocabulary to a professional or technical field"],
        ]),
    },
    "foreign-languages-c2-l18": {
        "data_table": table(["Technology", "Capability"], [
            ["Machine translation", "Automates translation but still struggles with idiom and nuance"],
        ]),
    },
    "foreign-languages-c2-l19": {
        "data_table": table(["Skill", "Detail"], [
            ["Cultural competency", "Ability to navigate social norms appropriately in another culture"],
        ]),
    },
    "foreign-languages-c2-l20": {
        "data_table": table(["Learner Type", "Feature"], [
            ["Heritage language learner", "Has family/cultural connection to a language but limited formal instruction"],
        ]),
    },
    "foreign-languages-c2-l21": {
        "data_table": table(["Mood", "Use"], [
            ["Subjunctive", "Expresses doubt, desire, or emotion rather than objective fact"],
        ]),
    },
    "foreign-languages-c2-l22": {
        "data_table": table(["Region", "Variation"], [
            ["Latin American Spanish", "Idiom and vocabulary vary notably by country and region"],
        ]),
    },
    "foreign-languages-c2-l23": {
        "data_table": table(["Mood", "Use"], [
            ["French subjunctive", "Follows expressions of necessity, emotion, or uncertainty"],
        ]),
    },
    "foreign-languages-c2-l24": {
        "data_table": table(["Author", "Feature"], [
            ["Molière", "French playwright known for satirical comedies of manners"],
        ]),
    },
    "foreign-languages-c2-l25": {
        "data_table": table(["Rule", "Detail"], [
            ["German subordinate clause", "Sends the conjugated verb to the end of the clause"],
        ]),
    },
    "foreign-languages-c2-l26": {
        "data_table": table(["Work", "Feature"], [
            ["Goethe's Faust", "A landmark of German literature exploring ambition and moral compromise"],
        ]),
    },
    "foreign-languages-c2-l27": {
        "data_table": table(["Tense", "Use"], [
            ["Passato prossimo", "Describes a completed action at a specific past moment"],
            ["Imperfetto", "Describes ongoing or habitual past action"],
        ]),
    },
    "foreign-languages-c2-l28": {
        "data_table": table(["Work", "Feature"], [
            ["Dante's Inferno", "First part of the Divine Comedy, depicting a journey through Hell"],
        ]),
    },
    "foreign-languages-c2-l29": {
        "data_table": table(["Mood", "Use"], [
            ["Portuguese subjunctive", "Used after expressions of doubt, wish, or hypothetical condition"],
        ]),
    },
    "foreign-languages-c2-l30": {
        "data_table": table(["Genre", "Feature"], [
            ["Brazilian short fiction", "Often blends regional dialect with vivid social commentary"],
        ]),
    },
    "foreign-languages-c2-l31": {
        "data_table": table(["Conjunction", "Function"], [
            ["Suiran (虽然)", "Introduces a concessive clause meaning 'although'"],
        ]),
    },
    "foreign-languages-c2-l32": {
        "data_table": table(["Genre", "Feature"], [
            ["Contemporary Chinese short story", "Often addresses rapid social change and generational contrast"],
        ]),
    },
    "foreign-languages-c2-l33": {
        "data_table": table(["Script", "Detail"], [
            ["Kanji", "Logographic characters conveying meaning, often with multiple readings"],
        ]),
    },
    "foreign-languages-c2-l34": {
        "data_table": table(["Speech Level", "Use"], [
            ["Keigo", "Honorific speech marking social status and formality in Japanese"],
        ]),
    },
    "foreign-languages-c2-l35": {
        "data_table": table(["Speech Level", "Use"], [
            ["Korean honorifics", "Verb endings and vocabulary shift based on relative social status"],
        ]),
    },
    "foreign-languages-c2-l36": {
        "data_table": table(["Genre", "Feature"], [
            ["Contemporary Korean fiction", "Frequently explores urban life and shifting family structures"],
        ]),
    },
    "foreign-languages-c2-l37": {
        "data_table": table(["Form", "Structure"], [
            ["MSA verb conjugation", "Root consonants combine with vowel patterns to form verb forms"],
        ]),
    },
    "foreign-languages-c2-l38": {
        "data_table": table(["Feature", "Detail"], [
            ["Classical Arabic poetry", "Uses strict meter and rhyme rooted in pre-Islamic oral tradition"],
        ]),
    },
    "foreign-languages-c2-l39": {
        "data_table": table(["Case", "Use"], [
            ["Genitive", "Marks possession or relationship between nouns"],
            ["Dative", "Marks the indirect object of a verb"],
        ]),
    },
    "foreign-languages-c2-l40": {
        "data_table": table(["Author", "Feature"], [
            ["Chekhov", "Master of the short story known for subtle psychological realism"],
        ]),
    },
    "foreign-languages-c2-l41": {
        "data_table": table(["Work", "Feature"], [
            ["Gallic Wars", "Caesar's firsthand account of his military campaigns, a classic Latin prose text"],
        ]),
    },
    "foreign-languages-c2-l42": {
        "data_table": table(["Construction", "Use"], [
            ["Latin subjunctive", "Used in purpose, result, and indirect question clauses"],
        ]),
    },
    "foreign-languages-c2-l43": {
        "data_table": table(["Marker", "Function"], [
            ["Non-manual marker", "Facial expression or head movement carrying grammatical meaning in ASL"],
        ]),
    },
    "foreign-languages-c2-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Deaf culture", "A community with shared language, norms, and history centered on ASL"],
        ]),
    },
    "foreign-languages-c2-l45": {
        "data_table": table(["Aspect", "Meaning"], [
            ["Swahili verb aspect", "Prefixes mark tense and aspect distinctly from the verb root"],
        ]),
    },
    "foreign-languages-c2-l46": {
        "data_table": table(["Feature", "Detail"], [
            ["Hindi postpositions", "Function like prepositions but follow the noun they modify"],
        ]),
    },
    "foreign-languages-c2-l47": {
        "data_table": table(["Author", "Feature"], [
            ["Premchand", "Pioneering Hindi/Urdu author known for social realist fiction"],
        ]),
    },
    "foreign-languages-c2-l48": {
        "data_table": table(["Author", "Feature"], [
            ["García Márquez", "Nobel laureate known for pioneering magical realism in Spanish fiction"],
        ]),
    },
    "foreign-languages-c2-l49": {
        "data_table": table(["Register", "Use"], [
            ["Formal Spanish writing", "Requires precise agreement and elevated vocabulary in academic contexts"],
        ]),
    },
    "foreign-languages-c2-l50": {
        "data_table": table(["Register", "Use"], [
            ["Formal French writing", "Follows strict conventions of tone and structure in professional documents"],
        ]),
    },
    "foreign-languages-c2-l51": {
        "data_table": table(["Register", "Use"], [
            ["Formal German writing", "Uses precise case marking and formal address in professional writing"],
        ]),
    },
    "foreign-languages-c2-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Business Chinese etiquette", "Emphasizes hierarchy and indirectness in professional communication"],
        ]),
    },
    "foreign-languages-c2-l53": {
        "data_table": table(["Language", "Verb Feature"], [
            ["Romance languages", "Share Latin-derived conjugation patterns with regular variation"],
        ]),
    },
    "foreign-languages-c2-l54": {
        "data_table": table(["Language", "Case Feature"], [
            ["Slavic languages", "Typically mark six or more grammatical cases on nouns"],
        ]),
    },
    "foreign-languages-c2-l55": {
        "data_table": table(["Challenge", "Detail"], [
            ["Literary translation", "Must balance fidelity to meaning with preserving stylistic voice"],
        ]),
    },
    "foreign-languages-c2-l56": {
        "data_table": table(["Sound", "Difficulty"], [
            ["Rolled r", "Requires precise tongue control, challenging for many learners"],
        ]),
    },
    "foreign-languages-c2-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Idiom study", "Direct translation of idioms often fails to convey intended meaning"],
        ]),
    },
    "foreign-languages-c2-l58": {
        "data_table": table(["Skill", "Detail"], [
            ["Target-language poetry analysis", "Requires attention to rhythm, sound, and cultural allusion"],
        ]),
    },
    "foreign-languages-c2-l59": {
        "data_table": table(["Skill", "Detail"], [
            ["Regional accent comprehension", "Builds tolerance for pronunciation variation across dialect regions"],
        ]),
    },
    "foreign-languages-c2-l60": {
        "data_table": table(["Task", "Focus"], [
            ["Conversational fluency capstone", "Demonstrates sustained, natural conversation in the target language"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Concept", "Meaning"], [
    ["Input hypothesis", "Learners acquire language by understanding input slightly above their level (Krashen)"],
    ["Critical period", "A window when language acquisition is easiest, typically early childhood"],
])

# l61-l70 "Worked Analysis" lessons reuse the data_table of l1-l10.
WORKED_ANALYSIS_MAP = {61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"foreign-languages-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"foreign-languages-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"foreign-languages-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Foreign Languages"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Foreign Languages lessons (completing 70/70).")


if __name__ == "__main__":
    main()
