#!/usr/bin/env python3
"""Depth pass, C1 AI Tools: fill in real, hand-checked data_table
content for the 69 C1 AI Tools lessons not covered by the earlier
breadth-first batch. Brings C1 AI Tools to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_ai_tools_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ai-tools-c1-l1": {
        "data_table": table(["Category", "Example Use"], [
            ["Writing assistants", "Drafting and editing text"], ["Image generators", "Creating visual content"],
        ]),
    },
    "ai-tools-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Conversational AI", "AI systems that interact with users through natural language dialogue"],
        ]),
    },
    "ai-tools-c1-l4": {
        "data_table": table(["Step", "Purpose"], [
            ["Type a clear question", "Gets a more useful and accurate response"],
        ]),
    },
    "ai-tools-c1-l5": {
        "data_table": table(["Practice", "Reason"], [
            ["Being specific", "Reduces ambiguity and improves output quality"], ["Giving examples", "Helps the AI match your intended format"],
        ]),
    },
    "ai-tools-c1-l6": {
        "data_table": table(["Use Case", "Benefit"], [
            ["Summarizing meeting notes", "Saves time reviewing lengthy transcripts"],
        ]),
    },
    "ai-tools-c1-l7": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI image generator", "Creates images from text descriptions"],
        ]),
    },
    "ai-tools-c1-l8": {
        "data_table": table(["Use Case", "Benefit"], [
            ["Drafting email replies", "Saves time on routine correspondence"],
        ]),
    },
    "ai-tools-c1-l9": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI answer engine", "Provides direct answers by synthesizing multiple sources"],
        ]),
    },
    "ai-tools-c1-l10": {
        "data_table": table(["Tool Type", "Function"], [
            ["Transcription tool", "Converts spoken audio into written text"],
        ]),
    },
    "ai-tools-c1-l11": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI translation tool", "Converts text from one language to another"],
        ]),
    },
    "ai-tools-c1-l12": {
        "data_table": table(["Sign", "Detail"], [
            ["Unnaturally uniform style", "Can indicate AI-generated writing"],
        ]),
    },
    "ai-tools-c1-l13": {
        "data_table": table(["Benefit", "Detail"], [
            ["24/7 availability", "AI chatbots can respond to customers at any time"],
        ]),
    },
    "ai-tools-c1-l14": {
        "data_table": table(["Use Case", "Benefit"], [
            ["Generating practice questions", "Reinforces learning through active recall"],
        ]),
    },
    "ai-tools-c1-l15": {
        "data_table": table(["Use Case", "Benefit"], [
            ["Automating repetitive data entry", "Reduces manual effort and errors"],
        ]),
    },
    "ai-tools-c1-l16": {
        "data_table": table(["Example", "Function"], [
            ["Voice assistant", "Responds to spoken commands to perform tasks"],
        ]),
    },
    "ai-tools-c1-l17": {
        "data_table": table(["Tool Type", "Function"], [
            ["Grammar checker", "Flags spelling, grammar, and style issues in writing"],
        ]),
    },
    "ai-tools-c1-l18": {
        "data_table": table(["Tier", "Feature"], [
            ["Free tier", "Limited usage, basic features"], ["Paid tier", "Higher limits, advanced features"],
        ]),
    },
    "ai-tools-c1-l19": {
        "data_table": table(["Principle", "Meaning"], [
            ["Fact-checking AI output", "AI can produce confident but incorrect information"],
        ]),
    },
    "ai-tools-c1-l20": {
        "data_table": table(["Activity", "Purpose"], [
            ["Trying several tools hands-on", "Builds practical comfort with everyday AI"],
        ]),
    },
    "ai-tools-c1-l21": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI coding assistant", "Suggests and completes code as you type"],
        ]),
    },
    "ai-tools-c1-l22": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI website builder", "Generates a website layout from a description"],
        ]),
    },
    "ai-tools-c1-l23": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI resume tool", "Helps draft and tailor resumes to job postings"],
        ]),
    },
    "ai-tools-c1-l24": {
        "data_table": table(["Tool Type", "Function"], [
            ["Text-to-speech tool", "Converts written text into spoken audio"],
        ]),
    },
    "ai-tools-c1-l25": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI captioning tool", "Automatically generates subtitles for video"],
        ]),
    },
    "ai-tools-c1-l26": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI music generator", "Creates original music from a text prompt or style"],
        ]),
    },
    "ai-tools-c1-l27": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI 3D model generator", "Creates 3D assets from text or image input"],
        ]),
    },
    "ai-tools-c1-l28": {
        "data_table": table(["Tool Type", "Function"], [
            ["Browser AI extension", "Adds AI features directly into a web browser"],
        ]),
    },
    "ai-tools-c1-l29": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI research assistant", "Helps find and cite relevant sources"],
        ]),
    },
    "ai-tools-c1-l30": {
        "data_table": table(["Use Case", "Benefit"], [
            ["Generating weekly meal plans", "Saves time and reduces decision fatigue"],
        ]),
    },
    "ai-tools-c1-l31": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI legal document assistant", "Helps draft or review standard legal documents"],
        ]),
    },
    "ai-tools-c1-l32": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI lead generation tool", "Identifies and prioritizes potential sales prospects"],
        ]),
    },
    "ai-tools-c1-l33": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI accessibility tool", "Assists users with disabilities, e.g. screen readers with AI descriptions"],
        ]),
    },
    "ai-tools-c1-l34": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI language learning app", "Personalizes lessons and gives instant feedback"],
        ]),
    },
    "ai-tools-c1-l35": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI design mockup tool", "Generates UI layouts from a text description"],
        ]),
    },
    "ai-tools-c1-l36": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI task tracker", "Automatically organizes and prioritizes to-do items"],
        ]),
    },
    "ai-tools-c1-l37": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI photo editor", "Automatically enhances or modifies images"],
        ]),
    },
    "ai-tools-c1-l38": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI avatar generator", "Creates a talking digital character from text or audio"],
        ]),
    },
    "ai-tools-c1-l39": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI OCR tool", "Converts handwritten or printed text in images into digital text"],
        ]),
    },
    "ai-tools-c1-l40": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI data visualization assistant", "Suggests and builds charts from raw data"],
        ]),
    },
    "ai-tools-c1-l41": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI spam filter", "Automatically identifies and blocks unwanted messages"],
        ]),
    },
    "ai-tools-c1-l42": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI budgeting app", "Tracks spending and suggests savings automatically"],
        ]),
    },
    "ai-tools-c1-l43": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI fitness coach", "Personalizes workout plans based on user data"],
        ]),
    },
    "ai-tools-c1-l44": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI travel planner", "Builds itineraries based on preferences and budget"],
        ]),
    },
    "ai-tools-c1-l45": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI note organizer", "Automatically tags and structures notes"],
        ]),
    },
    "ai-tools-c1-l46": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI show-notes generator", "Summarizes a podcast episode into structured notes"],
        ]),
    },
    "ai-tools-c1-l47": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI survey analysis tool", "Identifies themes and sentiment in open-ended responses"],
        ]),
    },
    "ai-tools-c1-l48": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI interview prep tool", "Simulates interview questions and gives feedback"],
        ]),
    },
    "ai-tools-c1-l49": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI event planning tool", "Helps organize logistics and schedules for events"],
        ]),
    },
    "ai-tools-c1-l50": {
        "data_table": table(["Use", "Benefit"], [
            ["Comparison sites", "Help evaluate AI tools side by side before choosing one"],
        ]),
    },
    "ai-tools-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Custom GPT", "A tailored AI assistant configured for a specific task without coding"],
        ]),
    },
    "ai-tools-c1-l52": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI flashcard tool", "Generates spaced-repetition flashcards from study material"],
        ]),
    },
    "ai-tools-c1-l53": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI speaker coach", "Gives feedback on pacing, filler words, and delivery"],
        ]),
    },
    "ai-tools-c1-l54": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI screen recorder", "Automatically generates tutorials from recorded screen activity"],
        ]),
    },
    "ai-tools-c1-l55": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI job matching tool", "Matches resumes to relevant job postings"],
        ]),
    },
    "ai-tools-c1-l56": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI home automation", "Learns routines to automatically control smart devices"],
        ]),
    },
    "ai-tools-c1-l57": {
        "data_table": table(["Step", "Purpose"], [
            ["Define the task clearly", "Guides selecting the right AI tool category"],
        ]),
    },
    "ai-tools-c1-l58": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI image upscaler", "Increases image resolution while preserving detail"],
        ]),
    },
    "ai-tools-c1-l59": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI dubbing tool", "Translates and re-voices video content into another language"],
        ]),
    },
    "ai-tools-c1-l60": {
        "data_table": table(["Tool Type", "Function"], [
            ["AI scraping tool", "Automatically extracts structured data from web pages"],
        ]),
    },
    "ai-tools-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Mapping tools to tasks", "Matching an everyday task to the right AI tool category"],
        ]),
    },
    "ai-tools-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Holding a sample conversation", "Practicing a multi-turn exchange with a conversational AI"],
        ]),
    },
    "ai-tools-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Explaining LLMs simply", "Describing how a language model predicts the next word"],
        ]),
    },
    "ai-tools-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Setting up a first chat", "Creating an account and sending a first prompt to an AI assistant"],
        ]),
    },
    "ai-tools-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Rewriting a vague prompt", "Improving a prompt by adding specificity and context"],
        ]),
    },
    "ai-tools-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Summarizing a document", "Using an AI tool to condense a sample article"],
        ]),
    },
    "ai-tools-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Generating an image", "Writing a text prompt to create a sample illustration"],
        ]),
    },
    "ai-tools-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Drafting an email", "Using AI to write a polite follow-up message"],
        ]),
    },
    "ai-tools-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Fact-checking an AI answer", "Verifying an AI-generated answer against a primary source"],
        ]),
    },
    "ai-tools-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Transcribing an audio clip", "Converting a short recorded conversation to text"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["AI Tools"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json AI Tools: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 AI Tools lessons (completing 70/70).")


if __name__ == "__main__":
    main()
