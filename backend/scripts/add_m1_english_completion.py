#!/usr/bin/env python3
"""Depth pass, M1 English: fill in real, hand-checked data_table
content for the 99 M1 English lessons not covered by the earlier
breadth-first batch. Brings M1 English to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "english-m1-l1": {
        "data_table": table(["Concept", "Detail"], [
            ["Graduate academic writing", "Emphasizes precise argumentation and engagement with scholarly conversation"],
        ]),
    },
    "english-m1-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["Linguistics", "The scientific study of language structure, meaning, and use"],
        ]),
    },
    "english-m1-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Argumentation theory", "Studies how claims are constructed, warranted, and evaluated"],
        ]),
    },
    "english-m1-l5": {
        "data_table": table(["Skill", "Detail"], [
            ["Theory-driven close reading", "Applies a specific critical framework to interpret textual detail"],
        ]),
    },
    "english-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Generative grammar", "Models the finite rule system underlying speakers' infinite sentence-generating capacity"],
        ]),
    },
    "english-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["History of prose style", "Traces how sentence structure and diction conventions shifted across periods"],
        ]),
    },
    "english-m1-l8": {
        "data_table": table(["Element", "Purpose"], [
            ["Thesis proposal", "Defines a research question, methodology, and scholarly contribution"],
        ]),
    },
    "english-m1-l9": {
        "data_table": table(["Element", "Purpose"], [
            ["Scholarly apparatus", "Footnotes, citations, and bibliography document a work's sources"],
        ]),
    },
    "english-m1-l10": {
        "data_table": table(["Genre", "Feature"], [
            ["Professional/technical writing", "Prioritizes clarity and usability for a defined practical audience"],
        ]),
    },
    "english-m1-l11": {
        "data_table": table(["Practice", "Purpose"], [
            ["Workshop critique", "Peer feedback refines a creative work's craft and clarity"],
        ]),
    },
    "english-m1-l12": {
        "data_table": table(["Field", "Focus"], [
            ["Literary theory", "Frameworks for interpreting texts beyond plot summary"],
        ]),
    },
    "english-m1-l13": {
        "data_table": table(["Approach", "Focus"], [
            ["Textual criticism", "Compares variant editions to establish an authoritative text"],
            ["Performance criticism", "Analyzes how staging choices shape a play's meaning"],
        ]),
    },
    "english-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Theory of the novel", "Examines the novel's distinctive formal and social properties as a genre"],
        ]),
    },
    "english-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Metrical theory", "Analyzes rhythmic patterns of stressed and unstressed syllables in verse"],
        ]),
    },
    "english-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["World Anglophone literature", "English-language literature produced across diverse global contexts"],
        ]),
    },
    "english-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Scholarly editing", "Establishes a reliable text by comparing manuscript and print sources"],
        ]),
    },
    "english-m1-l18": {
        "data_table": table(["Oratory Type", "Purpose"], [
            ["Deliberative", "Persuades an audience about future action"],
            ["Forensic", "Argues about past events, as in a legal setting"],
            ["Epideictic", "Praises or blames, as in a ceremonial speech"],
        ]),
    },
    "english-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Digital humanities composition", "Uses digital tools and media to create and analyze scholarly texts"],
        ]),
    },
    "english-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone research essay", "Synthesizes independent scholarship into an original literary argument"],
        ]),
    },
    "english-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Subaltern", "Spivak's term for groups excluded from dominant power structures and their own representation"],
        ]),
    },
    "english-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Cultural hybridity", "Bhabha's concept of identity formed in the in-between space of colonial encounter"],
        ]),
    },
    "english-m1-l23": {
        "data_table": table(["Approach", "Detail"], [
            ["New Historicism", "Reads literary texts alongside contemporaneous non-literary documents"],
        ]),
    },
    "english-m1-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Deconstruction", "Derrida's method of exposing instability and contradiction within a text's meaning"],
        ]),
    },
    "english-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Lacanian criticism", "Applies psychoanalytic concepts like the unconscious and desire to textual analysis"],
        ]),
    },
    "english-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Ideology critique", "Marxist criticism reads literature as shaped by and reflecting class relations"],
        ]),
    },
    "english-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Ecocriticism", "Examines the relationship between literature and the natural environment"],
        ]),
    },
    "english-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Queer theory", "Examines how texts construct and challenge norms of gender and sexuality"],
        ]),
    },
    "english-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Reader-response theory", "Locates meaning in the interaction between text and reader, not the text alone"],
        ]),
    },
    "english-m1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Narrative discourse", "Genette's distinction between story events and how they are narrated"],
        ]),
    },
    "english-m1-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Semiotics", "Studies how signs and symbols generate meaning within a system"],
        ]),
    },
    "english-m1-l32": {
        "data_table": table(["Feature", "Detail"], [
            ["Gothic convention", "Uses decay, the uncanny, and confinement to externalize cultural anxiety"],
        ]),
    },
    "english-m1-l33": {
        "data_table": table(["Technique", "Detail"], [
            ["Stream of consciousness", "Renders a character's flow of thought with minimal narrative mediation"],
        ]),
    },
    "english-m1-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Metafiction", "Fiction that draws attention to its own status as a constructed narrative"],
        ]),
    },
    "english-m1-l35": {
        "data_table": table(["Practice", "Detail"], [
            ["Serial publication", "Novels released in installments shaped pacing and cliffhanger structure"],
        ]),
    },
    "english-m1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Bildungsroman", "A novel tracing a protagonist's formative moral and psychological growth"],
        ]),
    },
    "english-m1-l37": {
        "data_table": table(["Form", "Feature"], [
            ["Epistolary fiction", "Tells a story through letters, diary entries, or documents"],
        ]),
    },
    "english-m1-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["The sublime", "An aesthetic experience of awe mixed with terror before nature's vastness"],
        ]),
    },
    "english-m1-l39": {
        "data_table": table(["Feature", "Detail"], [
            ["Metaphysical conceit", "An extended, intellectually surprising comparison between unlike things"],
        ]),
    },
    "english-m1-l40": {
        "data_table": table(["Feature", "Detail"], [
            ["Confessional poetry", "Draws directly on the poet's personal and often taboo experience"],
        ]),
    },
    "english-m1-l41": {
        "data_table": table(["Form", "Structure"], [
            ["Petrarchan sonnet", "Octave and sestet, rhyme scheme ABBAABBA CDECDE"],
            ["Shakespearean sonnet", "Three quatrains and a couplet, ABAB CDCD EFEF GG"],
        ]),
    },
    "english-m1-l42": {
        "data_table": table(["Feature", "Detail"], [
            ["Elegy", "A poem of mourning that typically moves toward consolation"],
        ]),
    },
    "english-m1-l43": {
        "data_table": table(["Technique", "Detail"], [
            ["Satire", "Uses irony and exaggeration to critique folly or vice"],
        ]),
    },
    "english-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Tragic flaw (hamartia)", "A character trait driving the protagonist toward downfall"],
        ]),
    },
    "english-m1-l45": {
        "data_table": table(["Feature", "Detail"], [
            ["Comedy of manners", "Satirizes the social customs and affectations of a leisured class"],
        ]),
    },
    "english-m1-l46": {
        "data_table": table(["Feature", "Detail"], [
            ["Absurdist theatre", "Uses illogical dialogue and situations to depict existential futility"],
        ]),
    },
    "english-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Postdramatic theatre", "Moves beyond conventional plot and character toward fragmented performance"],
        ]),
    },
    "english-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Historiographic metafiction", "Fiction that self-consciously questions how history is narrated"],
        ]),
    },
    "english-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Trauma theory", "Examines how literature represents experience that resists direct narration"],
        ]),
    },
    "english-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Affect theory", "Studies emotional and bodily intensities as central to textual meaning"],
        ]),
    },
    "english-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Posthumanism", "Questions human exceptionalism in favor of relations across species and systems"],
        ]),
    },
    "english-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["World-systems theory", "Analyzes literature through global core-periphery economic relations"],
        ]),
    },
    "english-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Translation equivalence", "Theorizes what must be preserved for a translation to count as faithful"],
        ]),
    },
    "english-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Sociolinguistic variation", "Language use shifts systematically with social class and context"],
        ]),
    },
    "english-m1-l55": {
        "data_table": table(["Method", "Purpose"], [
            ["Comparative method", "Reconstructs a proto-language by comparing related languages' sound correspondences"],
        ]),
    },
    "english-m1-l56": {
        "data_table": table(["Method", "Purpose"], [
            ["Corpus linguistics", "Analyzes large text collections to reveal patterns in real language use"],
        ]),
    },
    "english-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Critical discourse studies", "Examines how language use reflects and reproduces power relations"],
        ]),
    },
    "english-m1-l58": {
        "data_table": table(["Maxim", "Meaning"], [
            ["Cooperative principle", "Grice's assumption that conversation partners aim to communicate helpfully"],
        ]),
    },
    "english-m1-l59": {
        "data_table": table(["Approach", "Focus"], [
            ["Truth-conditional semantics", "Meaning defined by the conditions under which a sentence is true"],
            ["Cognitive semantics", "Meaning grounded in conceptual and embodied experience"],
        ]),
    },
    "english-m1-l60": {
        "data_table": table(["Theory", "Focus"], [
            ["Optimality theory", "Explains phonological patterns as resolving competing ranked constraints"],
        ]),
    },
    "english-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Morphology", "Studies how words are built from smaller meaningful units"],
        ]),
    },
    "english-m1-l62": {
        "data_table": table(["Approach", "Focus"], [
            ["Generative acquisition", "Explains language learning via innate grammatical structure"],
            ["Usage-based acquisition", "Explains language learning via exposure and pattern extraction"],
        ]),
    },
    "english-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Second language writing research", "Studies how L2 writers develop and are assessed differently from L1 writers"],
        ]),
    },
    "english-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["World Englishes", "Recognizes multiple legitimate national and regional varieties of English"],
        ]),
    },
    "english-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["AAVE", "A rule-governed English variety with its own consistent grammar and phonology"],
        ]),
    },
    "english-m1-l66": {
        "data_table": table(["Era", "Feature"], [
            ["Early Modern print culture", "The printing press standardized spelling and expanded textual circulation"],
        ]),
    },
    "english-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Sociology of texts", "Studies how material production shapes a text's meaning and reception"],
        ]),
    },
    "english-m1-l68": {
        "data_table": table(["Factor", "Effect"], [
            ["Print culture expansion", "Wider access to printed books fueled the novel's rise as a popular form"],
        ]),
    },
    "english-m1-l69": {
        "data_table": table(["Skill", "Purpose"], [
            ["Paleography", "Deciphers historical handwriting to access manuscript sources"],
        ]),
    },
    "english-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Born-digital literature", "Literary works created natively in digital form rather than adapted from print"],
        ]),
    },
    "english-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Adaptation theory", "Examines how meaning shifts as a work moves between literature and film"],
        ]),
    },
    "english-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["Graphic narrative", "Combines sequential images and text as a distinct narrative form"],
        ]),
    },
    "english-m1-l73": {
        "data_table": table(["Genre", "Feature"], [
            ["Life writing", "Encompasses autobiography and memoir as constructed, selective self-narration"],
        ]),
    },
    "english-m1-l74": {
        "data_table": table(["Concept", "Detail"], [
            ["Colonial discourse in travel writing", "Travel narratives often encoded imperial assumptions about the places described"],
        ]),
    },
    "english-m1-l75": {
        "data_table": table(["Genre", "Feature"], [
            ["Utopian fiction", "Imagines an ideal society to critique the present"],
            ["Dystopian fiction", "Imagines a nightmarish society to warn against present trends"],
        ]),
    },
    "english-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Cognitive estrangement", "Science fiction defamiliarizes the familiar to prompt critical reflection"],
        ]),
    },
    "english-m1-l77": {
        "data_table": table(["Convention", "Detail"], [
            ["Detective fiction structure", "A puzzle is posed, clues are planted, and a rational solution is revealed"],
        ]),
    },
    "english-m1-l78": {
        "data_table": table(["Approach", "Focus"], [
            ["Children's literature criticism", "Examines how texts address child readers and construct childhood itself"],
        ]),
    },
    "english-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["YA literature scholarship", "An emerging field examining texts written for and about adolescence"],
        ]),
    },
    "english-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Participatory culture", "Fan fiction reworks existing texts through active audience creation"],
        ]),
    },
    "english-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Digital archive", "Makes primary textual sources searchable and accessible for scholarship"],
        ]),
    },
    "english-m1-l82": {
        "data_table": table(["Factor", "Effect"], [
            ["Publishing economics", "Market pressures shape what gets published and how it's marketed"],
        ]),
    },
    "english-m1-l83": {
        "data_table": table(["Challenge", "Detail"], [
            ["Literary translation practice", "Must balance fidelity to meaning with preserving stylistic voice"],
        ]),
    },
    "english-m1-l84": {
        "data_table": table(["Approach", "Detail"], [
            ["Comparative literature method", "Studies literary texts across languages and national traditions together"],
        ]),
    },
    "english-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Diaspora literature", "Explores displacement, memory, and identity across national borders"],
        ]),
    },
    "english-m1-l86": {
        "data_table": table(["Practice", "Detail"], [
            ["Decolonial reading", "Reads texts with attention to indigenous perspectives marginalized by colonial framing"],
        ]),
    },
    "english-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Creolization", "Cultural and linguistic blending distinctive to Caribbean literary tradition"],
        ]),
    },
    "english-m1-l88": {
        "data_table": table(["Theme", "Detail"], [
            ["Nation-building narrative", "African literature in English often grapples with postcolonial national identity"],
        ]),
    },
    "english-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["South Asian Anglophone fiction", "English-language fiction engaging South Asian history, migration, and identity"],
        ]),
    },
    "english-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Literary regionalism", "Depicts a specific American locale's dialect, customs, and landscape"],
        ]),
    },
    "english-m1-l91": {
        "data_table": table(["Movement", "Feature"], [
            ["Harlem Renaissance", "1920s flourishing of African American literature, music, and art in New York"],
        ]),
    },
    "english-m1-l92": {
        "data_table": table(["Figure", "Contribution"], [
            ["Emerson", "Advocated self-reliance and individual intuition over convention"],
            ["Thoreau", "Explored simple living and civil disobedience in relation to nature"],
        ]),
    },
    "english-m1-l93": {
        "data_table": table(["Feature", "Detail"], [
            ["Beat Generation writing", "Rejected mainstream convention through spontaneous, countercultural expression"],
        ]),
    },
    "english-m1-l94": {
        "data_table": table(["Form", "Feature"], [
            ["Autofiction", "Blends autobiography and fiction, blurring the line between author and narrator"],
        ]),
    },
    "english-m1-l95": {
        "data_table": table(["Movement", "Feature"], [
            ["New Journalism", "Applied literary narrative techniques to factual reporting"],
        ]),
    },
    "english-m1-l96": {
        "data_table": table(["Debate", "Detail"], [
            ["Genre boundary debate", "Scholars disagree on how strictly generic categories should be defined"],
        ]),
    },
    "english-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Textual materiality", "Treats the physical book itself as a bearer of meaning, not just its words"],
        ]),
    },
    "english-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Intentional fallacy", "New Criticism's claim that authorial intent should not determine textual meaning"],
        ]),
    },
    "english-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Ecopoetics", "Poetry that reimagines human-nature relations amid ecological crisis"],
        ]),
    },
    "english-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Broadside ballad", "A cheaply printed single-sheet poem or song, a key source for popular print history"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Rhetorical Appeal", "Meaning"], [
        ["Ethos", "Appeal to credibility/character"],
        ["Pathos", "Appeal to emotion"],
        ["Logos", "Appeal to logic/reason"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"english-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"english-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"english-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 English lessons (completing 120/120).")


if __name__ == "__main__":
    main()
