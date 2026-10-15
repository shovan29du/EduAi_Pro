#!/usr/bin/env python3
"""Depth pass, M2 English: fill in real, hand-checked data_table
content for the M2 English lessons not covered by the earlier
breadth-first batch. Brings M2 English to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
linguistics, literary theory, narratology, translation studies, and
digital humanities; l101-l120 are "Worked Analysis" companions
reusing the data_table of l1-l20 (direct 1:1 mapping). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Corpus", "A large, structured collection of texts used for linguistic analysis"],
    ["Stylistics", "The study of distinctive style in language use"],
])

CHARTS: dict[str, dict] = {
    "english-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Linguistics research methods", "Systematic approaches to studying the structure and use of language"],
    ])},
    "english-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Composition & rhetoric", "Studies how texts are constructed persuasively for a given audience"],
    ])},
    "english-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive poetics", "Applies cognitive science to explain how readers process and respond to literary texts"],
    ])},
    "english-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Transitivity analysis", "Examines how a clause's verb type distributes roles like actor and goal (Systemic Functional Linguistics)"],
    ])},
    "english-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Relevance theory", "Explains pragmatic inference as hearers seeking the most contextually relevant interpretation"],
    ])},
    "english-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Construction grammar", "Treats grammatical patterns themselves as meaningful units, not just word combinations"],
    ])},
    "english-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Optimality theory", "Explains phonological patterns as the output ranking a hierarchy of violable constraints"],
    ])},
    "english-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Sociophonetics", "Measures acoustic properties of speech (like vowel shifts) tied to social variables"],
    ])},
    "english-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Labovian paradigm", "Studies systematic correlation between linguistic variation and social factors"],
    ])},
    "english-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Historical pragmatics", "Studies how speech acts and pragmatic conventions have changed over time"],
    ])},
    "english-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Grammaticalization", "The historical process by which content words evolve into grammatical function words"],
    ])},
    "english-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Kachru's concentric circles", "Models English's global spread as inner, outer, and expanding circles of use"],
    ])},
    "english-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Creole genesis theory", "Explains how new creole languages emerge from contact between languages"],
    ])},
    "english-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Interlanguage theory", "Describes a learner's evolving language system as distinct from both native and target languages"],
    ])},
    "english-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Critical applied linguistics", "Examines how language policy intersects with power and social inequality"],
    ])},
    "english-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Translanguaging", "A pedagogy that lets multilingual learners draw fluidly on their full linguistic repertoire"],
    ])},
    "english-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Eye-tracking (reading research)", "Measures gaze fixations to study real-time cognitive processing during reading"],
    ])},
    "english-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Garden-path sentence", "A sentence that initially misleads the reader's parsing before requiring reanalysis"],
    ])},
    "english-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Aphasia", "Language impairment from brain damage, studied to reveal how language is neurally organized"],
    ])},
    "english-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Discourse parsing", "Automatically identifies the rhetorical structure connecting parts of a text"],
    ])},
    "english-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Multidimensional analysis (register)", "Statistically maps linguistic features that co-occur across text registers"],
    ])},
    "english-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Swalesian move analysis", "Identifies rhetorical 'moves' that structure a genre, like the research article introduction"],
    ])},
    "english-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Focalization", "Genette's term for the perspective through which narrative events are filtered"],
    ])},
    "english-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Free indirect discourse", "Blends a character's voice and thought into third-person narration without direct quotation"],
    ])},
    "english-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Unreliable narration", "A narrator whose credibility is compromised, requiring readers to infer the 'true' story"],
    ])},
    "english-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Iser's implied reader", "The hypothetical reader role a text constructs through its gaps and structure"],
    ])},
    "english-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Deconstruction (Derridean trace)", "Reveals how a text's meaning is destabilized by traces of what it excludes"],
    ])},
    "english-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["New Historicism", "Reads literary texts alongside historical anecdotes to reveal shared cultural discourses"],
    ])},
    "english-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Subaltern studies (Spivak)", "Examines whether and how marginalized colonial subjects can speak within dominant discourse"],
    ])},
    "english-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Hybridity and mimicry (Bhabha)", "Describes ambivalent identities formed at the intersection of colonizer and colonized cultures"],
    ])},
    "english-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Ecocriticism", "Studies literature's representation of the natural environment and ecological crisis"],
    ])},
    "english-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Blue humanities", "Applies literary and cultural analysis to oceans and maritime spaces"],
    ])},
    "english-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Queer theory (textual desire)", "Analyzes how texts encode and destabilize normative categories of gender and desire"],
    ])},
    "english-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Affect theory", "Studies emotional and bodily intensities that texts produce, beyond conscious meaning"],
    ])},
    "english-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Thing theory", "Examines how literary objects accrue meaning beyond their function as mere props"],
    ])},
    "english-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Book history", "Studies texts as material and social objects, including how they were read historically"],
    ])},
    "english-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Scholarly editing theory", "Establishes principles for producing authoritative critical editions of texts"],
    ])},
    "english-m2-l39": {"data_table": table(["Type", "Feature"], [
        ["Analytical bibliography", "Studies a book's physical production process"],
        ["Descriptive bibliography", "Systematically documents a book's physical features"],
    ])},
    "english-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Distant reading", "Analyzes large collections of texts computationally rather than reading individual works closely"],
    ])},
    "english-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Topic modeling (literary corpora)", "Statistically discovers latent thematic patterns across a large collection of texts"],
    ])},
    "english-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Stylometry", "Uses quantitative writing-style features to attribute authorship to disputed texts"],
    ])},
    "english-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Print culture / book trade history", "Studies how the commercial production of books shaped literary history"],
    ])},
    "english-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Paleography", "The study of historical handwriting used to date and interpret manuscripts"],
    ])},
    "english-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Periodical studies", "Examines how serialized publication shaped the form and reception of fiction"],
    ])},
    "english-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Adaptation studies (fidelity)", "Debates whether an adaptation should be judged by faithfulness to its source"],
    ])},
    "english-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["World literature debates", "Examines how texts circulate and gain meaning beyond their national origin"],
    ])},
    "english-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Descriptive translation studies", "Studies actual translation practices and norms rather than prescribing ideal methods"],
    ])},
    "english-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Skopos theory", "Argues a translation's purpose (skopos) should determine the translator's strategy"],
    ])},
    "english-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Retranslation hypothesis", "Proposes that later retranslations tend to move closer to the source text"],
    ])},
    "english-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Untranslatability", "Examines cases where a source text's meaning resists full translation into another language"],
    ])},
    "english-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Conceptual metaphor theory", "Argues abstract concepts are structured through mappings from concrete source domains"],
    ])},
    "english-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Conceptual blending theory", "Explains how meaning emerges from combining elements of separate mental spaces"],
    ])},
    "english-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Speech act theory (dramatic dialogue)", "Analyzes how characters' utterances perform actions within a play"],
    ])},
    "english-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Politeness theory", "Analyzes strategies characters use to manage face and social threat in dialogue"],
    ])},
    "english-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Corpus-assisted discourse studies", "Combines corpus linguistics with discourse analysis for larger-scale evidence"],
    ])},
    "english-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Fairclough's three-dimensional model", "Analyzes discourse as text, discursive practice, and social practice together"],
    ])},
    "english-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal discourse analysis", "Examines meaning-making across combined text, image, and other modes"],
    ])},
    "english-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Forensic linguistics (authorship)", "Uses linguistic evidence like idiolect to help identify a text's author"],
    ])},
    "english-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Forensic discourse analysis", "Analyzes language in legal testimony to assess reliability or meaning"],
    ])},
    "english-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Language documentation", "Records and archives endangered languages to support revitalization efforts"],
    ])},
    "english-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Great Vowel Shift", "A major systematic change in English vowel pronunciation between roughly 1400 and 1700"],
    ])},
    "english-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Semantic change (grammaticalization)", "Tracks how word meanings shift as they take on new grammatical functions"],
    ])},
    "english-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Corpus-based lexicography", "Compiles dictionary entries from evidence of real language use in large text corpora"],
    ])},
    "english-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Onomastics (literary naming)", "Studies how authors use character and place names symbolically"],
    ])},
    "english-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Generative metrics", "Formally models the rules underlying acceptable poetic meter"],
    ])},
    "english-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Prosody (poetic meter)", "Studies the rhythmic sound patterns that structure verse"],
    ])},
    "english-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Ekphrasis", "A literary description that vividly represents a work of visual art"],
    ])},
    "english-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Trauma theory (testimonial narrative)", "Examines how texts represent and transmit the experience of psychological trauma"],
    ])},
    "english-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Autotheory", "Blends autobiographical writing with theoretical analysis, blurring genre boundaries"],
    ])},
    "english-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Autofiction", "Fiction that blends autobiographical fact with invention, blurring the narrating self"],
    ])},
    "english-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Stream of consciousness", "A narrative technique representing a character's continuous, unfiltered flow of thought"],
    ])},
    "english-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Transnational modernisms", "Studies modernist literature as a global, interconnected movement, not just Western"],
    ])},
    "english-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Little magazine culture", "Small independent periodicals that circulated and shaped early modernist literature"],
    ])},
    "english-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Posthumanism (literary theory)", "Questions the human as the central category of literary and philosophical analysis"],
    ])},
    "english-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Object-oriented ontology", "Grants objects independent existence and reality apart from human perception, applied to texts"],
    ])},
    "english-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Actor-network theory (literary production)", "Treats human and non-human elements as equal actors shaping how texts are produced"],
    ])},
    "english-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["World-systems theory (literature)", "Analyzes literature's global unevenness through core-periphery economic relations"],
    ])},
    "english-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Bourdieu's field of cultural production", "Models literary status as a social space of competing positions and capital"],
    ])},
    "english-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Horizon of expectations", "The set of cultural norms readers bring to a text, shaping its historical reception"],
    ])},
    "english-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Genetic criticism (avant-texte)", "Studies a work's drafts and manuscripts to trace its compositional process"],
    ])},
    "english-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Textual variants / editorial apparatus", "Documents differences across a text's versions for scholarly editions"],
    ])},
    "english-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["TEI encoding standard", "A structured XML standard for digitally encoding scholarly texts"],
    ])},
    "english-m2-l84": {"data_table": table(["Method", "Feature"], [
        ["Close reading", "Detailed interpretation of a single passage's language"],
        ["Distant reading", "Computational analysis across large text collections"],
    ])},
    "english-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Surface reading / postcritique", "Argues for attending to a text's explicit meaning rather than only hidden ideology"],
    ])},
    "english-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Archive fever (Derrida)", "Examines the archive's role in both preserving and constructing memory and meaning"],
    ])},
    "english-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Accessible text technologies", "Studies how format and technology shape reading access for people with print disabilities"],
    ])},
    "english-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Code-switching in fiction", "Analyzes how multilingual texts alternate between languages for literary effect"],
    ])},
    "english-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Bakhtinian dialogism / heteroglossia", "Describes the novel as a space where many social voices and languages interact"],
    ])},
    "english-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Chronotope", "Bakhtin's term for how time and space are fused and represented within a narrative"],
    ])},
    "english-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Genre hybridity", "Examines how contemporary fiction blends and blurs established genre categories"],
    ])},
    "english-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive estrangement", "Suvin's theory that speculative fiction defamiliarizes reality through a rational novum"],
    ])},
    "english-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["The Gothic mode", "Theoretical frameworks analyzing horror, transgression, and the uncanny in literature"],
    ])},
    "english-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Holocaust literature studies", "Examines the ethical and formal challenges of representing extreme historical trauma"],
    ])},
    "english-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Standard language myth", "Critiques the ideology that one language variety is inherently more correct than others"],
    ])},
    "english-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Corpus pragmatics", "Uses corpus methods to study discourse markers and pragmatic function across registers"],
    ])},
    "english-m2-l97": {"data_table": table(["Component", "Purpose"], [
        ["Doctoral thesis seminar", "Presents and defends original research contributing new knowledge to English studies"],
    ])},
    "english-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive narratology", "Studies how readers attribute mental states (theory of mind) to fictional characters"],
    ])},
    "english-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Linguistic landscape studies", "Analyzes the semiotics of public multilingual signage in a given space"],
    ])},
    "english-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Slow violence", "Nixon's term for gradual, often invisible environmental harm represented in narrative"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"english-m2-l{base_n}"
    worked_key = f"english-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 English lessons.")


if __name__ == "__main__":
    main()
