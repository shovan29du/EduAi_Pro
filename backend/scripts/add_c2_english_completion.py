#!/usr/bin/env python3
"""Depth pass, C2 English: fill in real, hand-checked data_table content
for the 69 C2 English lessons not covered by the earlier breadth-first
batch. Brings C2 English to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "english-c2-l1": {
        "data_table": table(["Element", "Question"], [
            ["Theme", "What central idea does the work explore?"], ["Symbolism", "What deeper meaning do objects or images carry?"],
        ]),
    },
    "english-c2-l2": {
        "data_table": table(["Element", "Purpose"], [
            ["Thesis statement", "States the paper's central argument"], ["Evidence", "Supports the thesis with specific examples"],
        ]),
    },
    "english-c2-l4": {
        "data_table": table(["Structure", "Purpose"], [
            ["Topic sentence", "States the paragraph's main point"], ["Transition", "Links ideas between paragraphs"],
        ]),
    },
    "english-c2-l5": {
        "data_table": table(["Form", "Focus"], [
            ["Poetry", "Compressed language, rhythm, and imagery"], ["Prose", "Extended narrative or expository structure"],
        ]),
    },
    "english-c2-l6": {
        "data_table": table(["Sentence Type", "Example"], [
            ["Simple", "One independent clause"], ["Complex", "An independent clause plus a dependent clause"],
        ]),
    },
    "english-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Tone", "The author's attitude toward the subject"], ["Register", "The level of formality in language use"],
        ]),
    },
    "english-c2-l8": {
        "data_table": table(["Criterion", "Question"], [
            ["Authority", "Is the author qualified to write on this topic?"], ["Currency", "Is the information up to date?"],
        ]),
    },
    "english-c2-l9": {
        "data_table": table(["Element", "MLA Format"], [
            ["In-text citation", "(Author page number)"], ["Works Cited entry", "Author. Title. Publisher, Year."],
        ]),
    },
    "english-c2-l10": {
        "data_table": table(["Document", "Feature"], [
            ["Business letter", "Formal structure with salutation and closing"], ["Memo", "Brief, direct internal communication"],
        ]),
    },
    "english-c2-l11": {
        "data_table": table(["Element", "Meaning"], [
            ["Setting", "The time and place of a story's action"], ["Conflict", "The central struggle driving the plot"],
        ]),
    },
    "english-c2-l12": {
        "data_table": table(["Approach", "Focus"], [
            ["New Criticism", "Analyzes the text itself, independent of author or historical context"],
        ]),
    },
    "english-c2-l13": {
        "data_table": table(["Feature", "Detail"], [
            ["Shakespearean comedy", "Typically ends in marriage and resolution of conflict"],
        ]),
    },
    "english-c2-l14": {
        "data_table": table(["POV Type", "Feature"], [
            ["First person", "Narrator uses 'I,' limited to their own perspective"], ["Third person omniscient", "Narrator knows all characters' thoughts"],
        ]),
    },
    "english-c2-l15": {
        "data_table": table(["Form", "Feature"], [
            ["Sonnet", "14 lines with a structured rhyme scheme"], ["Free verse", "No fixed meter or rhyme scheme"],
        ]),
    },
    "english-c2-l16": {
        "data_table": table(["Author", "Focus"], [
            ["Chinua Achebe", "Explores colonialism's impact on Igbo society"],
        ]),
    },
    "english-c2-l17": {
        "data_table": table(["Step", "Purpose"], [
            ["Giving specific feedback", "Helps a writer identify concrete areas to revise"],
        ]),
    },
    "english-c2-l18": {
        "data_table": table(["Element", "Purpose"], [
            ["Call to action", "Tells the audience what to do after hearing the speech"],
        ]),
    },
    "english-c2-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Multimodal composition", "Combines text with images, audio, or other media to convey meaning"],
        ]),
    },
    "english-c2-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Dialect", "A regional or social variety of a language with distinct vocabulary and grammar"],
        ]),
    },
    "english-c2-l21": {
        "data_table": table(["Element", "Purpose"], [
            ["Complex thesis", "Acknowledges nuance and counterarguments, not just a simple claim"],
        ]),
    },
    "english-c2-l22": {
        "data_table": table(["Type", "Example"], [
            ["Compound-complex sentence", "Contains two independent clauses and at least one dependent clause"],
        ]),
    },
    "english-c2-l23": {
        "data_table": table(["Step", "Purpose"], [
            ["Identifying scholarly sources", "Ensures literary analysis is grounded in credible criticism"],
        ]),
    },
    "english-c2-l24": {
        "data_table": table(["Style", "Feature"], [
            ["APA", "Author-date citation, common in social sciences"], ["Chicago", "Footnote or author-date style, common in history"],
        ]),
    },
    "english-c2-l25": {
        "data_table": table(["Step", "Purpose"], [
            ["Identifying a shared theme", "Anchors comparison between two literary works"],
        ]),
    },
    "english-c2-l26": {
        "data_table": table(["Feature", "Detail"], [
            ["Modernist literature", "Rejects traditional narrative form, embraces fragmentation"],
        ]),
    },
    "english-c2-l27": {
        "data_table": table(["Feature", "Detail"], [
            ["Postmodern literature", "Employs metafiction, irony, and skepticism of grand narratives"],
        ]),
    },
    "english-c2-l28": {
        "data_table": table(["Theory", "Focus"], [
            ["Structuralism", "Analyzes underlying structures shaping meaning"], ["Deconstruction", "Reveals internal contradictions and instability in a text's meaning"],
        ]),
    },
    "english-c2-l29": {
        "data_table": table(["Theory", "Focus"], [
            ["Feminist criticism", "Examines gender roles and power dynamics within a text"],
        ]),
    },
    "english-c2-l30": {
        "data_table": table(["Theory", "Focus"], [
            ["Marxist criticism", "Examines class conflict and economic power in a text"],
        ]),
    },
    "english-c2-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Meter", "The rhythmic pattern of stressed and unstressed syllables"], ["Prosody", "The study of poetic rhythm and sound patterns"],
        ]),
    },
    "english-c2-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Unreliable narrator", "A narrator whose credibility is compromised or questionable"],
        ]),
    },
    "english-c2-l33": {
        "data_table": table(["Technique", "Purpose"], [
            ["Interior monologue", "Reveals a character's inner thoughts directly to the reader"],
        ]),
    },
    "english-c2-l34": {
        "data_table": table(["Element", "Question"], [
            ["Rhetorical situation", "Who is the speaker, audience, and purpose of this discourse?"],
        ]),
    },
    "english-c2-l35": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Refutation", "Directly addresses and counters an opposing argument"],
        ]),
    },
    "english-c2-l36": {
        "data_table": table(["Step", "Purpose"], [
            ["Synthesizing sources", "Weaves multiple sources into a coherent argument rather than listing them"],
        ]),
    },
    "english-c2-l37": {
        "data_table": table(["Technique", "Effect"], [
            ["Varying sentence length", "Creates rhythm and emphasis in prose"],
        ]),
    },
    "english-c2-l38": {
        "data_table": table(["Challenge", "Detail"], [
            ["Reading in translation", "Requires attention to what may be altered from the original"],
        ]),
    },
    "english-c2-l39": {
        "data_table": table(["Form", "Feature"], [
            ["Tragedy", "Ends in the downfall of the protagonist"], ["Comedy", "Ends in resolution and often celebration"],
        ]),
    },
    "english-c2-l40": {
        "data_table": table(["Form", "Feature"], [
            ["Essay collection", "A series of standalone essays often unified by theme"],
        ]),
    },
    "english-c2-l41": {
        "data_table": table(["Platform", "Feature"], [
            ["Online argumentation", "Often shaped by brevity, virality, and audience interaction"],
        ]),
    },
    "english-c2-l42": {
        "data_table": table(["Focus", "Detail"], [
            ["Line editing", "Refines word choice, rhythm, and clarity sentence by sentence"],
        ]),
    },
    "english-c2-l43": {
        "data_table": table(["Technique", "Effect"], [
            ["Syntax manipulation", "Reordering sentence structure to create emphasis or rhythm"],
        ]),
    },
    "english-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Symbolism", "An object representing an abstract idea"], ["Allegory", "A narrative with a consistent symbolic second meaning"],
        ]),
    },
    "english-c2-l45": {
        "data_table": table(["Technique", "Purpose"], [
            ["Subtext in dialogue", "Conveys meaning beneath what characters literally say"],
        ]),
    },
    "english-c2-l46": {
        "data_table": table(["Feature", "Detail"], [
            ["Bildungsroman", "A novel tracing a protagonist's psychological and moral growth"],
        ]),
    },
    "english-c2-l47": {
        "data_table": table(["Genre", "Feature"], [
            ["Speculative fiction", "Imagines alternative worlds, futures, or possibilities"],
        ]),
    },
    "english-c2-l48": {
        "data_table": table(["Element", "Purpose"], [
            ["Literature review", "Synthesizes existing scholarship on a topic before presenting new analysis"],
        ]),
    },
    "english-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Intertextuality", "A text's meaning shaped by its relationship to other texts"], ["Allusion", "A brief reference to another work or event"],
        ]),
    },
    "english-c2-l50": {
        "data_table": table(["Feature", "Purpose"], [
            ["Op-ed", "A concise, persuasive piece of public commentary"],
        ]),
    },
    "english-c2-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Authorial intent", "The meaning an author intended, distinct from reader interpretation"],
        ]),
    },
    "english-c2-l52": {
        "data_table": table(["Perspective", "Focus"], [
            ["Postcolonial perspective", "Examines literature's engagement with colonialism's legacy"],
        ]),
    },
    "english-c2-l53": {
        "data_table": table(["Step", "Purpose"], [
            ["Slowing down complex prose", "Unpacks dense syntax sentence by sentence"],
        ]),
    },
    "english-c2-l54": {
        "data_table": table(["Practice", "Reason"], [
            ["Proper attribution", "Prevents plagiarism by crediting original sources"],
        ]),
    },
    "english-c2-l55": {
        "data_table": table(["Step", "Purpose"], [
            ["Revising for publication", "Polishes a draft to meet a publication's specific standards"],
        ]),
    },
    "english-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Satire", "Uses humor or exaggeration to critique folly or vice"], ["Irony", "A gap between expectation and reality"],
        ]),
    },
    "english-c2-l57": {
        "data_table": table(["Register", "Example"], [
            ["Formal register", "Academic writing"], ["Informal register", "Casual conversation"],
        ]),
    },
    "english-c2-l58": {
        "data_table": table(["Milestone", "Detail"], [
            ["Rise of the novel", "18th-century emergence of extended prose fiction as a dominant literary form"],
        ]),
    },
    "english-c2-l59": {
        "data_table": table(["Element", "Purpose"], [
            ["Digital storytelling", "Combines narrative, image, and sound for an interactive audience experience"],
        ]),
    },
    "english-c2-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Sustained argument development", "Builds a complex thesis across an extended research essay"],
        ]),
    },
    "english-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a text's theme", "Tracing a symbol's meaning across an entire work"],
        ]),
    },
    "english-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Drafting a thesis-driven paragraph", "Structuring evidence around a clear claim"],
        ]),
    },
    "english-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a persuasive text", "Identifying its use of ethos, pathos, and logos"],
        ]),
    },
    "english-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Building a multi-paragraph argument", "Sequencing points from strongest to most persuasive"],
        ]),
    },
    "english-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Comparing genres", "Contrasting how a poem and a short story treat the same theme"],
        ]),
    },
    "english-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Revising for sentence variety", "Combining short, choppy sentences for better flow"],
        ]),
    },
    "english-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Adjusting tone", "Rewriting a passage for a more formal audience"],
        ]),
    },
    "english-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating a source", "Assessing a website's credibility for a research paper"],
        ]),
    },
    "english-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Formatting a citation", "Writing a correct MLA in-text citation and Works Cited entry"],
        ]),
    },
    "english-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Drafting a memo", "Writing a concise, professionally formatted internal memo"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 English lessons (completing 70/70).")


if __name__ == "__main__":
    main()
