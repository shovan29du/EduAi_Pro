#!/usr/bin/env python3
"""Depth pass, C1 English: fill in real, hand-checked data_table
content for the 69 C1 English lessons not covered by the earlier
breadth-first batch. Brings C1 English to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "english-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Rhetoric", "The art of effective or persuasive writing and speaking"],
        ]),
    },
    "english-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Literary analysis", "Examining how a text creates meaning through its elements"],
        ]),
    },
    "english-c1-l4": {
        "data_table": table(["Part", "Purpose"], [
            ["Thesis", "States the central argument"], ["Evidence", "Supports the claim"], ["Rebuttal", "Addresses counterarguments"],
        ]),
    },
    "english-c1-l5": {
        "data_table": table(["Technique", "Purpose"], [
            ["Annotating", "Marking a text to track meaning as you read"],
        ]),
    },
    "english-c1-l6": {
        "data_table": table(["Clause Type", "Example"], [
            ["Independent clause", "Can stand alone as a sentence"], ["Dependent clause", "Cannot stand alone"],
        ]),
    },
    "english-c1-l7": {
        "data_table": table(["Element", "Meaning"], [
            ["Voice", "A writer's distinctive way of using language"],
        ]),
    },
    "english-c1-l8": {
        "data_table": table(["Element", "Purpose"], [
            ["Research question", "Guides the direction of inquiry"], ["Thesis statement", "States the argument the paper will make"],
        ]),
    },
    "english-c1-l9": {
        "data_table": table(["Reason to Cite", "Purpose"], [
            ["Give credit", "Acknowledges original authors"], ["Avoid plagiarism", "Distinguishes your ideas from sourced ones"],
        ]),
    },
    "english-c1-l10": {
        "data_table": table(["Feature", "Purpose"], [
            ["Clear subject line", "Helps the reader know the email's purpose immediately"],
        ]),
    },
    "english-c1-l11": {
        "data_table": table(["Genre", "Example"], [
            ["Short story", "A compact fictional narrative"], ["Poetry", "Language shaped by rhythm and imagery"],
        ]),
    },
    "english-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Literary theory", "A framework for interpreting texts, e.g. feminist or historical criticism"],
        ]),
    },
    "english-c1-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Shakespeare", "English playwright, 1564-1616"], ["Iambic pentameter", "A common rhythmic pattern in his verse"],
        ]),
    },
    "english-c1-l14": {
        "data_table": table(["Feature", "Meaning"], [
            ["Novel", "An extended work of fiction, typically with developed characters and plot"],
        ]),
    },
    "english-c1-l15": {
        "data_table": table(["Element", "Meaning"], [
            ["Rhythm", "The pattern of stressed and unstressed syllables"], ["Rhyme", "Matching end sounds in lines"],
        ]),
    },
    "english-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Anglophone literature", "Literature written in English from around the world"],
        ]),
    },
    "english-c1-l17": {
        "data_table": table(["Step", "Purpose"], [
            ["Read aloud", "Helps catch awkward phrasing"], ["Check structure", "Ensures logical flow of ideas"],
        ]),
    },
    "english-c1-l18": {
        "data_table": table(["Skill", "Purpose"], [
            ["Eye contact", "Engages the audience"], ["Pacing", "Keeps the talk clear and controlled"],
        ]),
    },
    "english-c1-l19": {
        "data_table": table(["Format", "Feature"], [
            ["Screenplay", "Uses scene headings and dialogue formatting"],
        ]),
    },
    "english-c1-l20": {
        "data_table": table(["Period", "Feature"], [
            ["Old English", "c. 450-1150 CE"], ["Middle English", "c. 1150-1500 CE, includes Chaucer"],
        ]),
    },
    "english-c1-l21": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Learning word roots", "Helps decode unfamiliar academic vocabulary"],
        ]),
    },
    "english-c1-l22": {
        "data_table": table(["Element", "Purpose"], [
            ["Topic sentence", "States the paragraph's main idea"], ["Unity", "All sentences support one central idea"],
        ]),
    },
    "english-c1-l23": {
        "data_table": table(["Part", "Purpose"], [
            ["Thesis statement", "Announces the essay's central claim"],
        ]),
    },
    "english-c1-l24": {
        "data_table": table(["Error", "Example"], [
            ["Run-on sentence", "Two independent clauses joined without punctuation"], ["Sentence fragment", "An incomplete sentence"],
        ]),
    },
    "english-c1-l25": {
        "data_table": table(["Skill", "Meaning"], [
            ["Summarizing", "Condensing a text's main ideas"], ["Paraphrasing", "Restating a text in your own words"],
        ]),
    },
    "english-c1-l26": {
        "data_table": table(["Structure", "Description"], [
            ["Point-by-point", "Compares one aspect at a time"], ["Block method", "Discusses one subject fully, then the other"],
        ]),
    },
    "english-c1-l27": {
        "data_table": table(["Technique", "Purpose"], [
            ["Sensory detail", "Helps the reader picture a scene vividly"],
        ]),
    },
    "english-c1-l28": {
        "data_table": table(["Element", "Purpose"], [
            ["Plot arc", "The sequence of events building narrative tension"],
        ]),
    },
    "english-c1-l29": {
        "data_table": table(["Feature", "Example"], [
            ["Short story", "A compact narrative focused on a single incident"],
        ]),
    },
    "english-c1-l30": {
        "data_table": table(["Device", "Meaning"], [
            ["Metaphor", "An implied comparison between two things"], ["Symbolism", "Using an object to represent an idea"],
        ]),
    },
    "english-c1-l31": {
        "data_table": table(["Feature", "Example"], [
            ["Essay", "A short piece of writing exploring a single topic"],
        ]),
    },
    "english-c1-l32": {
        "data_table": table(["Question", "Purpose"], [
            ["Who wrote this and why?", "Reveals potential bias in nonfiction"],
        ]),
    },
    "english-c1-l33": {
        "data_table": table(["Author", "Famous Work"], [
            ["F. Scott Fitzgerald", "The Great Gatsby"],
        ]),
    },
    "english-c1-l34": {
        "data_table": table(["Author", "Famous Work"], [
            ["William Shakespeare", "Hamlet"],
        ]),
    },
    "english-c1-l35": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Context clues", "Helps guess unfamiliar word meanings while reading"],
        ]),
    },
    "english-c1-l36": {
        "data_table": table(["Step", "Purpose"], [
            ["Give specific feedback", "Helps a peer improve targeted areas of writing"],
        ]),
    },
    "english-c1-l37": {
        "data_table": table(["Part", "Purpose"], [
            ["Introduction", "Hooks the reader and states the thesis"], ["Conclusion", "Reinforces the argument and closes the essay"],
        ]),
    },
    "english-c1-l38": {
        "data_table": table(["Register", "Use"], [
            ["Formal", "Academic or professional writing"], ["Informal", "Casual conversation"],
        ]),
    },
    "english-c1-l39": {
        "data_table": table(["Method", "Feature"], [
            ["Cornell notes", "Splits notes into cues, notes, and summary sections"],
        ]),
    },
    "english-c1-l40": {
        "data_table": table(["Element", "Meaning"], [
            ["Audience", "Who the writing is intended for"], ["Purpose", "Why the writing was created"],
        ]),
    },
    "english-c1-l41": {
        "data_table": table(["Feature", "Example"], [
            ["Personal essay", "First-person reflection on a specific experience or idea"],
        ]),
    },
    "english-c1-l42": {
        "data_table": table(["Element", "Meaning"], [
            ["Stage direction", "Instructions describing actor movement or setting"],
        ]),
    },
    "english-c1-l43": {
        "data_table": table(["Style", "Feature"], [
            ["Journalistic writing", "Concise, factual, and objective"],
        ]),
    },
    "english-c1-l44": {
        "data_table": table(["Element", "Meaning"], [
            ["Imagery", "Descriptive language appealing to the senses"],
        ]),
    },
    "english-c1-l45": {
        "data_table": table(["Practice", "Benefit"], [
            ["Timed writing", "Builds speed and confidence under time pressure"],
        ]),
    },
    "english-c1-l46": {
        "data_table": table(["Step", "Purpose"], [
            ["Outlining", "Organizes ideas before drafting"], ["Prewriting", "Generates ideas freely before structuring"],
        ]),
    },
    "english-c1-l47": {
        "data_table": table(["Point of View", "Example"], [
            ["First person", "'I walked to the store.'"], ["Third person omniscient", "Narrator knows all characters' thoughts"],
        ]),
    },
    "english-c1-l48": {
        "data_table": table(["Method", "Example"], [
            ["Direct characterization", "Author states a trait outright"], ["Indirect characterization", "Trait shown through actions"],
        ]),
    },
    "english-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Setting", "The time and place of a story"], ["Atmosphere", "The emotional mood created by the setting"],
        ]),
    },
    "english-c1-l50": {
        "data_table": table(["Transition Word", "Function"], [
            ["However", "Signals contrast"], ["Therefore", "Signals a conclusion"],
        ]),
    },
    "english-c1-l51": {
        "data_table": table(["Variety", "Region"], [
            ["British English", "United Kingdom"], ["Nigerian English", "Nigeria"],
        ]),
    },
    "english-c1-l52": {
        "data_table": table(["Format", "Example"], [
            ["Multimodal composition", "Combines text, image, and sound"],
        ]),
    },
    "english-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Theme", "The central message or idea of a work"],
        ]),
    },
    "english-c1-l54": {
        "data_table": table(["Appeal", "Focus"], [
            ["Ethos", "Credibility"], ["Pathos", "Emotion"], ["Logos", "Logic"],
        ]),
    },
    "english-c1-l55": {
        "data_table": table(["Element", "Purpose"], [
            ["Evidence", "Supports and strengthens a claim"],
        ]),
    },
    "english-c1-l56": {
        "data_table": table(["Purpose", "Benefit"], [
            ["Reading response journal", "Tracks personal reactions and questions while reading"],
        ]),
    },
    "english-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Denotation", "A word's literal dictionary meaning"], ["Connotation", "The emotional association a word carries"],
        ]),
    },
    "english-c1-l58": {
        "data_table": table(["Skill", "Purpose"], [
            ["Comparative analysis", "Examines similarities and differences between texts from different cultures"],
        ]),
    },
    "english-c1-l59": {
        "data_table": table(["Element", "Purpose"], [
            ["Summary", "Briefly describes the book's content"], ["Evaluation", "Assesses the book's strengths and weaknesses"],
        ]),
    },
    "english-c1-l60": {
        "data_table": table(["Technique", "Effect"], [
            ["Varying sentence length", "Creates rhythm and emphasis in writing"],
        ]),
    },
    "english-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Rhetorical analysis", "Examining how a speech uses ethos, pathos, and logos"],
        ]),
    },
    "english-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Close reading a poem", "Tracing how imagery builds a poem's meaning"],
        ]),
    },
    "english-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Identifying rhetorical situation", "Analyzing the audience and purpose of a real speech"],
        ]),
    },
    "english-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Outlining an argumentative essay", "Structuring claim, evidence, and rebuttal for a topic"],
        ]),
    },
    "english-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Annotating a passage", "Marking key phrases and questions while reading"],
        ]),
    },
    "english-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Fixing sentence errors", "Revising run-ons and fragments in a sample paragraph"],
        ]),
    },
    "english-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Developing a distinct voice", "Comparing two drafts of the same paragraph in different voices"],
        ]),
    },
    "english-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Refining a thesis", "Narrowing a broad topic into an arguable thesis statement"],
        ]),
    },
    "english-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Practicing citation", "Formatting the same source in MLA and APA style"],
        ]),
    },
    "english-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Writing a professional email", "Drafting a clear request to a professor or colleague"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 English lessons (completing 70/70).")


if __name__ == "__main__":
    main()
