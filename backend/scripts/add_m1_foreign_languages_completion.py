#!/usr/bin/env python3
"""Depth pass, M1 Foreign Languages: fill in real, hand-checked
data_table content for the 99 M1 Foreign Languages lessons not
covered by the earlier breadth-first batch. Brings M1 Foreign
Languages to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "foreign-languages-m1-l1": {
        "data_table": table(["Skill", "Feature"], [
            ["Advanced reading & writing", "Builds ability to engage authentic texts and produce structured academic prose"],
        ]),
    },
    "foreign-languages-m1-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Applied translation & linguistics", "Bridges linguistic theory with practical translation and interpretation skill"],
        ]),
    },
    "foreign-languages-m1-l4": {
        "data_table": table(["Language Pair", "Structural Difference"], [
            ["English vs. Spanish", "Spanish marks gender and number agreement across nouns and adjectives"],
        ]),
    },
    "foreign-languages-m1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Phoneme", "The smallest sound unit that distinguishes meaning in a language"],
        ]),
    },
    "foreign-languages-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Multilingual sociolinguistics", "Studies how language choice signals identity and social context"],
        ]),
    },
    "foreign-languages-m1-l7": {
        "data_table": table(["Mode", "Detail"], [
            ["Translation", "Converts written text between languages"],
            ["Interpretation", "Converts spoken language in real time"],
        ]),
    },
    "foreign-languages-m1-l8": {
        "data_table": table(["Method", "Focus"], [
            ["Communicative approach", "Prioritizes meaningful interaction over rote grammar drilling"],
        ]),
    },
    "foreign-languages-m1-l9": {
        "data_table": table(["Tool", "Use"], [
            ["Computer-assisted language learning", "Uses software and adaptive feedback to support language practice"],
        ]),
    },
    "foreign-languages-m1-l10": {
        "data_table": table(["Element", "Purpose"], [
            ["Immersion program design", "Maximizes target-language exposure across structured daily activities"],
        ]),
    },
    "foreign-languages-m1-l11": {
        "data_table": table(["Register", "Use"], [
            ["Business register", "Formal vocabulary and tone suited to professional correspondence"],
        ]),
    },
    "foreign-languages-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Language and identity", "A speaker's language choices shape and express cultural belonging"],
        ]),
    },
    "foreign-languages-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Endangered language", "A language at risk of no longer being passed to new generations"],
        ]),
    },
    "foreign-languages-m1-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Code-switching", "Alternating between languages or dialects within a conversation"],
        ]),
    },
    "foreign-languages-m1-l15": {
        "data_table": table(["Assessment Type", "Focus"], [
            ["Proficiency test", "Measures overall functional ability rather than course-specific content"],
        ]),
    },
    "foreign-languages-m1-l16": {
        "data_table": table(["Genre", "Value"], [
            ["Target-language literature", "Exposes learners to authentic idiom, culture, and stylistic range"],
        ]),
    },
    "foreign-languages-m1-l17": {
        "data_table": table(["Domain", "Vocabulary Focus"], [
            ["Language for specific purposes", "Tailors vocabulary to a professional or technical field"],
        ]),
    },
    "foreign-languages-m1-l18": {
        "data_table": table(["Technology", "Capability"], [
            ["Machine translation", "Automates translation but still struggles with idiom and nuance"],
        ]),
    },
    "foreign-languages-m1-l19": {
        "data_table": table(["Skill", "Detail"], [
            ["Cultural competency", "Ability to navigate social norms appropriately in another culture"],
        ]),
    },
    "foreign-languages-m1-l20": {
        "data_table": table(["Learner Type", "Feature"], [
            ["Heritage language learner", "Has family/cultural connection to a language but limited formal instruction"],
        ]),
    },
    "foreign-languages-m1-l21": {
        "data_table": table(["Clause Type", "Mood"], [
            ["Complex subordinate clause", "Often requires subjunctive to express doubt, wish, or hypothetical condition"],
        ]),
    },
    "foreign-languages-m1-l22": {
        "data_table": table(["Tense", "Register"], [
            ["Passé simple", "A literary past tense rarely used in spoken French"],
        ]),
    },
    "foreign-languages-m1-l23": {
        "data_table": table(["Case", "Use"], [
            ["Dative", "Marks the indirect object of a verb"],
            ["Genitive", "Marks possession, increasingly rare in spoken usage"],
        ]),
    },
    "foreign-languages-m1-l24": {
        "data_table": table(["Classifier", "Use"], [
            ["个 (ge)", "The most general and widely used Chinese measure word"],
        ]),
    },
    "foreign-languages-m1-l25": {
        "data_table": table(["Aspect", "Meaning"], [
            ["Perfective", "Presents an action as a complete, single event"],
            ["Imperfective", "Presents an action as ongoing or habitual"],
        ]),
    },
    "foreign-languages-m1-l26": {
        "data_table": table(["Variety", "Use"], [
            ["Modern Standard Arabic", "Formal writing and pan-Arab media"],
            ["Colloquial dialect", "Everyday spoken communication, varies by region"],
        ]),
    },
    "foreign-languages-m1-l27": {
        "data_table": table(["Speech Level", "Use"], [
            ["Korean honorifics", "Verb endings and vocabulary shift based on relative social status"],
        ]),
    },
    "foreign-languages-m1-l28": {
        "data_table": table(["Mood", "Use"], [
            ["Congiuntivo", "Used after expressions of doubt, emotion, or opinion in Italian subordinate clauses"],
        ]),
    },
    "foreign-languages-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Ergative marking", "The subject of a transitive perfective verb takes special case marking in Hindi"],
        ]),
    },
    "foreign-languages-m1-l30": {
        "data_table": table(["Case", "Use"], [
            ["Instrumental", "Indicates the means or instrument by which an action is performed"],
            ["Locative", "Indicates location, used only with prepositions in Polish"],
        ]),
    },
    "foreign-languages-m1-l31": {
        "data_table": table(["Rule", "Detail"], [
            ["Dutch subordinate word order", "Sends the conjugated verb to the end of the subordinate clause"],
        ]),
    },
    "foreign-languages-m1-l32": {
        "data_table": table(["Aspect", "Detail"], [
            ["Greek verbal aspect", "Distinguishes ongoing, completed, and habitual action independent of tense"],
        ]),
    },
    "foreign-languages-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Binyanim", "Hebrew's seven verb patterns each convey a distinct voice or meaning nuance"],
        ]),
    },
    "foreign-languages-m1-l34": {
        "data_table": table(["Feature", "Detail"], [
            ["Vietnamese tone", "Six tones distinguish otherwise identical syllables, marked by diacritics"],
        ]),
    },
    "foreign-languages-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Thai classifier", "A specific counting word is required alongside numerals for different noun categories"],
        ]),
    },
    "foreign-languages-m1-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["Ezafe construction", "A linking vowel connects a Persian noun to its modifier or possessor"],
        ]),
    },
    "foreign-languages-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Ablative absolute", "A grammatically independent Latin construction expressing time, cause, or circumstance"],
        ]),
    },
    "foreign-languages-m1-l38": {
        "data_table": table(["Feature", "Detail"], [
            ["Classical Chinese grammar", "Highly compressed syntax differs significantly from modern vernacular Chinese"],
        ]),
    },
    "foreign-languages-m1-l39": {
        "data_table": table(["Work", "Significance"], [
            ["Don Quixote", "Often cited as the first modern novel for its self-aware narrative form"],
        ]),
    },
    "foreign-languages-m1-l40": {
        "data_table": table(["Movement", "Feature"], [
            ["Symbolism", "Suggested meaning through evocative imagery rather than direct statement"],
            ["Surrealism", "Explored the unconscious through startling, dreamlike imagery"],
        ]),
    },
    "foreign-languages-m1-l41": {
        "data_table": table(["Work", "Feature"], [
            ["Faust", "Goethe's landmark work exploring ambition and moral compromise"],
        ]),
    },
    "foreign-languages-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Polyphonic novel", "Dostoevsky's technique of giving characters' independent voices equal narrative weight"],
        ]),
    },
    "foreign-languages-m1-l43": {
        "data_table": table(["Work", "Feature"], [
            ["The Tale of Genji", "Often considered the world's first novel, noted for psychological depth"],
        ]),
    },
    "foreign-languages-m1-l44": {
        "data_table": table(["Work", "Feature"], [
            ["Dream of the Red Chamber", "A monumental classical Chinese novel of family and social decline"],
        ]),
    },
    "foreign-languages-m1-l45": {
        "data_table": table(["Form", "Feature"], [
            ["Terza rima", "Dante's interlocking three-line rhyme scheme used in the Divine Comedy"],
        ]),
    },
    "foreign-languages-m1-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Heteronymy", "Pessoa wrote under multiple distinct literary personas, not mere pseudonyms"],
        ]),
    },
    "foreign-languages-m1-l47": {
        "data_table": table(["Feature", "Detail"], [
            ["Cairo Trilogy realism", "Mahfouz depicted Egyptian society through detailed multigenerational family narrative"],
        ]),
    },
    "foreign-languages-m1-l48": {
        "data_table": table(["Genre", "Feature"], [
            ["Magical realism", "Blends fantastical elements into an otherwise realistic narrative world"],
        ]),
    },
    "foreign-languages-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Contemporary Korean fiction", "Frequently explores urban life and shifting family structures"],
        ]),
    },
    "foreign-languages-m1-l50": {
        "data_table": table(["Feature", "Detail"], [
            ["Ibsen's dramatic realism", "Depicted ordinary domestic life with psychological and social realism"],
        ]),
    },
    "foreign-languages-m1-l51": {
        "data_table": table(["Register", "Use"], [
            ["Commercial correspondence Spanish", "Follows formal conventions of address and tone in business writing"],
        ]),
    },
    "foreign-languages-m1-l52": {
        "data_table": table(["Vocabulary", "Use"], [
            ["Formal negotiation French", "Precise vocabulary conveys legally and diplomatically careful positioning"],
        ]),
    },
    "foreign-languages-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Guanxi", "Relationship-based trust networks shape Chinese professional communication norms"],
        ]),
    },
    "foreign-languages-m1-l54": {
        "data_table": table(["Skill", "Purpose"], [
            ["Medical interpreting terminology", "Precise Spanish medical vocabulary is critical for patient safety"],
        ]),
    },
    "foreign-languages-m1-l55": {
        "data_table": table(["Field", "Detail"], [
            ["Legal French terminology", "Contract vocabulary requires precise, unambiguous legal register"],
        ]),
    },
    "foreign-languages-m1-l56": {
        "data_table": table(["Rule", "Detail"], [
            ["German compounding", "Combines multiple nouns into a single long word expressing a compound concept"],
        ]),
    },
    "foreign-languages-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Idiom and register", "Direct translation of French idioms often fails to convey intended meaning"],
        ]),
    },
    "foreign-languages-m1-l58": {
        "data_table": table(["Variety", "Feature"], [
            ["Peninsular Spanish", "Uses vosotros and distinct pronunciation from Latin American varieties"],
            ["Latin American Spanish", "Uses ustedes universally and varies further by country"],
        ]),
    },
    "foreign-languages-m1-l59": {
        "data_table": table(["Variety", "Feature"], [
            ["Brazilian Portuguese", "Diverges notably in pronunciation and vocabulary from European Portuguese"],
        ]),
    },
    "foreign-languages-m1-l60": {
        "data_table": table(["Dialect", "Region"], [
            ["Egyptian Arabic", "Widely understood due to media influence"],
            ["Levantine Arabic", "Spoken across Syria, Lebanon, Jordan, and Palestine"],
        ]),
    },
    "foreign-languages-m1-l61": {
        "data_table": table(["Rule", "Detail"], [
            ["Tone sandhi", "Adjacent tones in Mandarin shift predictably based on surrounding tone context"],
        ]),
    },
    "foreign-languages-m1-l62": {
        "data_table": table(["Language", "Feature"], [
            ["Cantonese", "Retains more tones and different vocabulary than Mandarin, mutually unintelligible"],
        ]),
    },
    "foreign-languages-m1-l63": {
        "data_table": table(["Feature", "Detail"], [
            ["Swedish pitch accent", "Distinguishes word meaning through tonal pattern, unusual among European languages"],
        ]),
    },
    "foreign-languages-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Finnish case system", "Fifteen grammatical cases replace many prepositions used in other languages"],
        ]),
    },
    "foreign-languages-m1-l65": {
        "data_table": table(["Feature", "Detail"], [
            ["Icelandic conservation", "Grammar has changed remarkably little from Old Norse over centuries"],
        ]),
    },
    "foreign-languages-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Welsh mutation", "Initial consonants change systematically depending on grammatical context"],
        ]),
    },
    "foreign-languages-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Irish initial mutation", "Word-initial sounds shift to mark grammatical relationships in a sentence"],
        ]),
    },
    "foreign-languages-m1-l68": {
        "data_table": table(["Alignment", "Detail"], [
            ["Ergative-absolutive", "Basque marks the subject of transitive verbs differently from intransitive subjects"],
        ]),
    },
    "foreign-languages-m1-l69": {
        "data_table": table(["Role", "Detail"], [
            ["Swahili lingua franca", "Serves as a shared trade and communication language across East Africa"],
        ]),
    },
    "foreign-languages-m1-l70": {
        "data_table": table(["Feature", "Detail"], [
            ["Affixation morphology", "Indonesian and Malay build complex meaning through systematic prefixes and suffixes"],
        ]),
    },
    "foreign-languages-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Verb focus system", "Tagalog verb morphology marks which sentence element is grammatically highlighted"],
        ]),
    },
    "foreign-languages-m1-l72": {
        "data_table": table(["System", "Feature"], [
            ["Amharic syllabary", "Each character represents a consonant-vowel combination (abugida)"],
        ]),
    },
    "foreign-languages-m1-l73": {
        "data_table": table(["Feature", "Detail"], [
            ["Yoruba tone", "Pitch differences distinguish otherwise identical-looking words"],
        ]),
    },
    "foreign-languages-m1-l74": {
        "data_table": table(["Feature", "Detail"], [
            ["Zulu clicks", "Distinct click consonants function as regular phonemes in the language"],
        ]),
    },
    "foreign-languages-m1-l75": {
        "data_table": table(["Feature", "Detail"], [
            ["Quechua verbal morphology", "Rich suffixation encodes evidentiality and speaker perspective"],
        ]),
    },
    "foreign-languages-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Classical Nahuatl", "Preserved through colonial-era texts documenting Aztec literary and historical sources"],
        ]),
    },
    "foreign-languages-m1-l77": {
        "data_table": table(["False Friend", "Pitfall"], [
            ["Embarazada", "Means 'pregnant' in Spanish, not 'embarrassed'"],
        ]),
    },
    "foreign-languages-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Semantic drift", "French-English cognates have often diverged in meaning over centuries"],
        ]),
    },
    "foreign-languages-m1-l79": {
        "data_table": table(["Particle", "Function"], [
            ["Modal particle (doch, mal, ja)", "Adds subtle pragmatic nuance rather than core grammatical meaning in German"],
        ]),
    },
    "foreign-languages-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Chengyu", "Four-character idiomatic expressions often reference classical Chinese stories"],
        ]),
    },
    "foreign-languages-m1-l81": {
        "data_table": table(["Work", "Significance"], [
            ["Ashtadhyayi", "Panini's highly systematic grammatical description of Sanskrit"],
        ]),
    },
    "foreign-languages-m1-l82": {
        "data_table": table(["Work", "Feature"], [
            ["Beowulf", "A foundational Old English epic providing key evidence for early English language study"],
        ]),
    },
    "foreign-languages-m1-l83": {
        "data_table": table(["Era", "Feature"], [
            ["Middle French", "Transitional period shaping the syntax of subsequent Modern French"],
        ]),
    },
    "foreign-languages-m1-l84": {
        "data_table": table(["Language", "Detail"], [
            ["Romance languages", "Descend from Vulgar Latin with regular sound-change patterns across regions"],
        ]),
    },
    "foreign-languages-m1-l85": {
        "data_table": table(["Language", "Case Feature"], [
            ["Slavic languages", "Typically mark six or more grammatical cases on nouns"],
        ]),
    },
    "foreign-languages-m1-l86": {
        "data_table": table(["Marker", "Function"], [
            ["Non-manual marker", "Facial expression or head movement carrying grammatical meaning in ASL"],
        ]),
    },
    "foreign-languages-m1-l87": {
        "data_table": table(["Principle", "Detail"], [
            ["Constructed language design", "Esperanto aimed for maximal regularity and ease of learning across speakers"],
        ]),
    },
    "foreign-languages-m1-l88": {
        "data_table": table(["Term", "Meaning"], [
            ["Pidgin", "A simplified contact language with no native speakers"],
            ["Creole", "A pidgin that has stabilized as a full native language"],
        ]),
    },
    "foreign-languages-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Translanguaging", "Multilingual learners fluidly draw on all their linguistic resources together"],
        ]),
    },
    "foreign-languages-m1-l90": {
        "data_table": table(["Skill", "Detail"], [
            ["Simultaneous interpretation", "Requires processing and producing speech in real time with minimal delay"],
        ]),
    },
    "foreign-languages-m1-l91": {
        "data_table": table(["System", "Purpose"], [
            ["Consecutive interpretation notes", "A structured shorthand system supports accurate delayed rendering of speech"],
        ]),
    },
    "foreign-languages-m1-l92": {
        "data_table": table(["Debate", "Detail"], [
            ["Untranslatability", "Poetry's sound and rhythm often resist full translation into another language"],
        ]),
    },
    "foreign-languages-m1-l93": {
        "data_table": table(["Task", "Detail"], [
            ["Machine translation post-editing", "Professional translators refine automated output for accuracy and nuance"],
        ]),
    },
    "foreign-languages-m1-l94": {
        "data_table": table(["Practice", "Purpose"], [
            ["Terminology management", "Maintains consistent technical vocabulary across large translation projects"],
        ]),
    },
    "foreign-languages-m1-l95": {
        "data_table": table(["Feature", "Detail"], [
            ["Xhosa clicks", "Distinct click consonants function as regular phonemes in the language"],
        ]),
    },
    "foreign-languages-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Polypersonal agreement", "Georgian verbs mark information about both subject and object simultaneously"],
        ]),
    },
    "foreign-languages-m1-l97": {
        "data_table": table(["Feature", "Detail"], [
            ["Mongolian vertical script", "Historically written top to bottom, distinct from most world scripts"],
        ]),
    },
    "foreign-languages-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Catalan language policy", "Reflects ongoing negotiation of regional linguistic identity within Spain"],
        ]),
    },
    "foreign-languages-m1-l99": {
        "data_table": table(["Feature", "Detail"], [
            ["Verb-initial syntax", "Malagasy typically places the verb before the subject in a sentence"],
        ]),
    },
    "foreign-languages-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Tibetan honorific register", "Distinct vocabulary is used when addressing individuals of higher status"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Concept", "Meaning"], [
        ["Input hypothesis", "Learners acquire language by understanding input slightly above their level (Krashen)"],
        ["Critical period", "A window when language acquisition is easiest, typically early childhood"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"foreign-languages-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"foreign-languages-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"foreign-languages-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Foreign Languages"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Foreign Languages lessons (completing 120/120).")


if __name__ == "__main__":
    main()
