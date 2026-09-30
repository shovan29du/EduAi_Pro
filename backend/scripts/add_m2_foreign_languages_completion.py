#!/usr/bin/env python3
"""Depth pass, M2 Foreign Languages: fill in real, hand-checked
data_table content for the M2 Foreign Languages lessons not covered
by the earlier breadth-first batch. Brings M2 Foreign Languages to
full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning the
historical linguistics, literature, and sociolinguistics of a wide
range of world languages (Spanish, French, German, Mandarin,
Japanese, Arabic, Russian, Italian, Portuguese, Korean, Hindi-Urdu,
classical languages, and many others), plus general applied
linguistics topics; l101-l120 are "Worked Analysis" companions
reusing the data_table of l1-l20 (direct 1:1 mapping). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_foreign_languages_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Subjunctive mood", "Expresses doubt, wish, or hypothetical situations rather than stated fact"],
    ["Diachronic development", "Traces how the subjunctive's use has changed across the history of Spanish"],
])

CHARTS: dict[str, dict] = {
    "foreign-languages-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Applied translation/linguistics research", "Systematic scholarly methods for studying translation and language structure"],
    ])},
    "foreign-languages-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Beginner communication research", "Rigorous methods for studying how learners acquire basic communicative competence"],
    ])},
    "foreign-languages-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Caribbean Spanish phonology", "Regional sound features like consonant weakening distinguish Caribbean Spanish dialects"],
    ])},
    "foreign-languages-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Magical realism theory", "A literary mode blending everyday reality with matter-of-fact fantastical elements"],
    ])},
    "foreign-languages-m2-l6": {"data_table": table(["Playwright", "Feature"], [
        ["Lope de Vega", "Codified a popular dramatic formula blending comedy and tragedy in Spanish Golden Age theater"],
    ])},
    "foreign-languages-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Ladino (Judeo-Spanish)", "A Spanish-derived language preserved by Sephardic Jewish communities after 1492"],
    ])},
    "foreign-languages-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Clitic pronoun placement", "Analyzes the syntactic rules governing where unstressed pronouns attach in Spanish"],
    ])},
    "foreign-languages-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Cliticization and verb movement", "Studies how French clitic pronouns interact with verb position in a sentence"],
    ])},
    "foreign-languages-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Old French nasal vowels", "Traces the historical phonological development of nasalized vowel sounds"],
    ])},
    "foreign-languages-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Négritude movement", "A francophone Black literary and political movement affirming African cultural identity"],
    ])},
    "foreign-languages-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Quebec French sociolinguistics", "Studies language variation and policy shaping French in Quebec"],
    ])},
    "foreign-languages-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["French Symbolist poetry", "A movement using suggestive imagery and musicality to evoke meaning indirectly"],
    ])},
    "foreign-languages-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Oulipo", "A French literary group using self-imposed formal constraints to generate creative writing"],
    ])},
    "foreign-languages-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Verb-second word order", "German main clauses place the finite verb in the second syntactic position"],
    ])},
    "foreign-languages-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["German case simplification", "Traces the historical reduction of Germanic case distinctions over time"],
    ])},
    "foreign-languages-m2-l17": {"data_table": table(["Work", "Feature"], [
        ["Nibelungenlied", "A Middle High German epic poem central to medieval German literature"],
    ])},
    "foreign-languages-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["German Idealism (literary influence)", "Philosophical Idealism shaped the themes and aesthetics of German literary Romanticism"],
    ])},
    "foreign-languages-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Austrian German dialectal variation", "Studies distinct phonological and lexical features of Austrian German"],
    ])},
    "foreign-languages-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["German compounding morphology", "Studies the productive rules governing how German forms long compound words"],
    ])},
    "foreign-languages-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Tone sandhi (Mandarin)", "Rules governing how tones change when spoken in sequence with other tones"],
    ])},
    "foreign-languages-m2-l22": {"data_table": table(["Language", "Feature"], [
        ["Classical Chinese", "Terse, literary syntax used in historical texts"],
        ["Modern vernacular", "Closer to spoken Mandarin grammar"],
    ])},
    "foreign-languages-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Topic-prominence", "Mandarin discourse structure organizes sentences around a topic rather than strict subject-verb order"],
    ])},
    "foreign-languages-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Ming-Qing vernacular fiction", "Narrative techniques developed in early Chinese vernacular novels"],
    ])},
    "foreign-languages-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Aspect marking (Mandarin)", "Mandarin marks completion or ongoing action through aspect particles rather than tense"],
    ])},
    "foreign-languages-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Six categories (liushu)", "The traditional classification scheme for how Chinese characters were formed"],
    ])},
    "foreign-languages-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Keigo", "The structured Japanese honorific system marking social relationships through speech"],
    ])},
    "foreign-languages-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Japanese verb conjugation history", "Traces how Japanese verb forms evolved from classical to modern usage"],
    ])},
    "foreign-languages-m2-l29": {"data_table": table(["Work", "Feature"], [
        ["The Tale of Genji", "A Heian-period narrative considered among the world's first novels"],
    ])},
    "foreign-languages-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Sentence-final particles", "Japanese particles at the end of sentences that convey pragmatic nuance"],
    ])},
    "foreign-languages-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Kanji orthography reform", "Post-war standardization simplified and limited Japanese character usage"],
    ])},
    "foreign-languages-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Zero pronoun (Japanese)", "Japanese frequently omits pronouns, relying on discourse context to identify referents"],
    ])},
    "foreign-languages-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Diglossia (Arabic)", "The coexistence of a formal Standard Arabic and distinct spoken colloquial dialects"],
    ])},
    "foreign-languages-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Qasida structure", "A classical Arabic poetic form with a fixed structural and thematic convention"],
    ])},
    "foreign-languages-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Andalusian Arabic literature", "The distinct literary tradition that flourished in Islamic Iberia"],
    ])},
    "foreign-languages-m2-l36": {"data_table": table(["Dialect", "Region"], [
        ["Levantine", "Syria, Lebanon, Jordan, Palestine"],
        ["Gulf", "Saudi Arabia, UAE, Kuwait, and nearby states"],
    ])},
    "foreign-languages-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Quranic rhetorical devices", "The distinctive literary and rhetorical structures used in Quranic Arabic"],
    ])},
    "foreign-languages-m2-l38": {"data_table": table(["Aspect", "Feature"], [
        ["Perfective", "Views an action as a single complete whole"],
        ["Imperfective", "Views an action as ongoing or repeated"],
    ])},
    "foreign-languages-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Syncretism (Russian case)", "Different grammatical cases sometimes share the same word form in Russian"],
    ])},
    "foreign-languages-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Russian Formalism", "A literary theory movement analyzing texts through their formal devices and techniques"],
    ])},
    "foreign-languages-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Bakhtinian polyphony", "Bakhtin's theory that a novel's meaning emerges from interacting, unmerged character voices"],
    ])},
    "foreign-languages-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Old Church Slavonic influence", "The liturgical language that shaped the formation of literary Russian"],
    ])},
    "foreign-languages-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["OBERIU movement", "A Russian absurdist literary group active in the early Soviet period"],
    ])},
    "foreign-languages-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Italian dialectology", "Studies regional Italian dialects and the historical process of linguistic standardization"],
    ])},
    "foreign-languages-m2-l45": {"data_table": table(["Work", "Feature"], [
        ["Divine Comedy", "Dante's poem uses a structured allegorical journey through Hell, Purgatory, and Paradise"],
    ])},
    "foreign-languages-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Italian Futurism", "An early 20th-century movement that experimented radically with language and typography"],
    ])},
    "foreign-languages-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Sicilian School", "A medieval poetic tradition credited with originating the sonnet form"],
    ])},
    "foreign-languages-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Clitic climbing (Italian)", "A syntactic phenomenon where a clitic pronoun can attach to a higher verb in a construction"],
    ])},
    "foreign-languages-m2-l49": {"data_table": table(["Variety", "Feature"], [
        ["Brazilian Portuguese", "Distinct vowel reduction and stress patterns from European Portuguese"],
    ])},
    "foreign-languages-m2-l50": {"data_table": table(["Author", "Feature"], [
        ["Fernando Pessoa", "Wrote under multiple 'heteronyms', each a distinct literary persona"],
    ])},
    "foreign-languages-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Mesoclisis", "A distinctive Portuguese clitic placement inserting the pronoun within the verb form itself"],
    ])},
    "foreign-languages-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Lusophone African literature", "Postcolonial literary traditions from Portuguese-speaking African nations"],
    ])},
    "foreign-languages-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Korean honorific speech levels", "A graded system of verb endings marking social relationship and formality"],
    ])},
    "foreign-languages-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Hangul", "A featural writing system whose letter shapes reflect the articulatory features of their sounds"],
    ])},
    "foreign-languages-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Korean verb ending system", "Verb endings in Korean mark sentence mood and formality directly"],
    ])},
    "foreign-languages-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Sijo", "A traditional Korean poetic form with a fixed three-line structure"],
    ])},
    "foreign-languages-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Split ergativity (Hindi-Urdu)", "Hindi-Urdu marks subjects differently depending on tense and aspect"],
    ])},
    "foreign-languages-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Ghazal", "A poetic form central to Urdu literary tradition, expressing themes of love and loss"],
    ])},
    "foreign-languages-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Sanskritization vs Persianization", "Hindi and Urdu draw formal vocabulary from Sanskrit and Persian respectively"],
    ])},
    "foreign-languages-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Ablative absolute", "A Latin grammatical construction expressing background circumstance independent of the main clause"],
    ])},
    "foreign-languages-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Dactylic hexameter", "The classical Latin meter used in epic poetry, based on six metrical feet per line"],
    ])},
    "foreign-languages-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Medieval Latin", "Diverged from Classical Latin norms in vocabulary and grammar over the Middle Ages"],
    ])},
    "foreign-languages-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Sound changes to Romance", "Traces the historical phonological shifts from Latin to the Romance languages"],
    ])},
    "foreign-languages-m2-l64": {"data_table": table(["Dialect", "Feature"], [
        ["Attic", "The prestige literary dialect of classical Athens"],
        ["Ionic", "Used in early epic and historical works like Herodotus"],
    ])},
    "foreign-languages-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Homeric formulaic diction", "Repeated fixed phrases used to aid oral composition in Homeric epic"],
    ])},
    "foreign-languages-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Ancient Greek aspect", "The Greek verbal system centers on aspect (completed vs. ongoing) rather than pure tense"],
    ])},
    "foreign-languages-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Koine Greek", "The common dialect that spread after Alexander, becoming the language of the New Testament"],
    ])},
    "foreign-languages-m2-l68": {"data_table": table(["Work", "Feature"], [
        ["Ashtadhyayi", "Panini's foundational Sanskrit grammar, remarkably systematic for its ancient date"],
    ])},
    "foreign-languages-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Rasa theory", "A Sanskrit aesthetic theory describing the emotional essence a work evokes in its audience"],
    ])},
    "foreign-languages-m2-l70": {"data_table": table(["Variety", "Feature"], [
        ["Vedic Sanskrit", "The older form, phonologically and grammatically distinct from Classical Sanskrit"],
    ])},
    "foreign-languages-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Utenzi", "A traditional Swahili epic poetic form"],
    ])},
    "foreign-languages-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Vowel harmony (Turkish)", "Turkish suffix vowels systematically match the vowel quality of preceding syllables"],
    ])},
    "foreign-languages-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Case stacking (Turkish)", "Turkish's agglutinative morphology allows multiple grammatical suffixes to stack on a word"],
    ])},
    "foreign-languages-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Ottoman Turkish script reform", "The shift from Arabic to Latin script reshaped Turkish literary language"],
    ])},
    "foreign-languages-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Modern Hebrew revival", "A deliberate language planning effort revived Hebrew as a spoken daily language"],
    ])},
    "foreign-languages-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Biblical Hebrew tense-aspect debate", "Scholars debate whether Biblical Hebrew verb forms mark tense or aspect"],
    ])},
    "foreign-languages-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Medieval Andalusian Hebrew poetry", "A flourishing of Hebrew poetry among Jewish communities in medieval Iberia"],
    ])},
    "foreign-languages-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Polish nominal declension", "Polish nouns inflect across a complex case system marking grammatical role"],
    ])},
    "foreign-languages-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Polish literary standardization", "Traces the historical process of establishing a standard literary Polish"],
    ])},
    "foreign-languages-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Vietnamese six-tone system", "Vietnamese distinguishes meaning through six distinct lexical tones"],
    ])},
    "foreign-languages-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Nom script", "A historical Vietnamese writing system adapting Chinese characters to represent Vietnamese"],
    ])},
    "foreign-languages-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Thai tonal phonology", "Thai's tone system is represented through diacritics within its own script"],
    ])},
    "foreign-languages-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Old Norse sagas", "Analyzes the narrative conventions of medieval Icelandic prose sagas"],
    ])},
    "foreign-languages-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Swedish definite article suffixation", "Swedish attaches its definite article as a suffix rather than a separate word"],
    ])},
    "foreign-languages-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Finnish fifteen-case system", "Finnish uses an extensive case system to express grammatical relationships"],
    ])},
    "foreign-languages-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Initial consonant mutation (Irish)", "Irish Gaelic changes a word's initial sound based on grammatical context"],
    ])},
    "foreign-languages-m2-l87": {"data_table": table(["Work", "Feature"], [
        ["Ulster Cycle", "A major body of Old Irish heroic literature"],
    ])},
    "foreign-languages-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Contrastive rhetoric", "Studies how rhetorical conventions differ across languages in second-language writing"],
    ])},
    "foreign-languages-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Interlanguage pragmatics", "Studies how learners develop appropriate pragmatic competence in a target language"],
    ])},
    "foreign-languages-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Heritage language attrition", "Studies how a heritage language can weaken when not actively maintained"],
    ])},
    "foreign-languages-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Translanguaging (literary texts)", "Analyzes texts that fluidly draw on multiple languages within one literary work"],
    ])},
    "foreign-languages-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Indo-European reconstruction", "Comparative method used to reconstruct the ancestral Proto-Indo-European language"],
    ])},
    "foreign-languages-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Language revitalization case studies", "Examines efforts to revive endangered languages from documented decline"],
    ])},
    "foreign-languages-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["MT evaluation across typologies", "Machine translation quality varies significantly across structurally different language pairs"],
    ])},
    "foreign-languages-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Critical period hypothesis", "Proposes a biologically limited window for optimal native-like phonological acquisition"],
    ])},
    "foreign-languages-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Code-switching (bilingual literature)", "Analyzes how literary narratives alternate between languages for effect"],
    ])},
    "foreign-languages-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["World literature canon debates", "Debates which translated works are included in a global literary canon and why"],
    ])},
    "foreign-languages-m2-l98": {"data_table": table(["Component", "Purpose"], [
        ["Doctoral thesis seminar", "Presents and defends original research in foreign language and literature studies"],
    ])},
    "foreign-languages-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Basque ergative morphosyntax", "Basque, a language isolate, marks grammatical roles through an ergative-absolutive system"],
    ])},
    "foreign-languages-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Quechua grammatical structure", "Studies Quechua's agglutinative grammar and its contact with Spanish in the Andes"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"foreign-languages-m2-l{base_n}"
    worked_key = f"foreign-languages-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Foreign Languages"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Foreign Languages: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Foreign Languages lessons.")


if __name__ == "__main__":
    main()
