#!/usr/bin/env python3
"""Depth pass, C2 AI Tools: fill in real, hand-checked data_table
content for the 69 C2 AI Tools lessons not covered by the earlier
breadth-first batch. Brings C2 AI Tools to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_ai_tools_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ai-tools-c2-l1": {
        "data_table": table(["Category", "Example Use"], [
            ["AI writing assistant", "Drafting and editing text quickly"], ["AI productivity tool", "Summarizing documents or scheduling tasks"],
        ]),
    },
    "ai-tools-c2-l2": {
        "data_table": table(["Type", "Use Case"], [
            ["Image generation", "Creating original visuals from a text description"], ["Video generation", "Producing short video clips from text or images"],
        ]),
    },
    "ai-tools-c2-l4": {
        "data_table": table(["Step", "Purpose"], [
            ["Refining a prompt", "Adjusts wording based on the model's initial output to improve results"],
        ]),
    },
    "ai-tools-c2-l5": {
        "data_table": table(["Feature", "Purpose"], [
            ["Outline-to-slides generation", "Converts a text outline into a formatted presentation automatically"],
        ]),
    },
    "ai-tools-c2-l6": {
        "data_table": table(["Element", "Purpose"], [
            ["Style descriptor", "Guides the visual style of a generated image"],
        ]),
    },
    "ai-tools-c2-l7": {
        "data_table": table(["Task", "Example"], [
            ["Formula generation", "Asking an AI tool to write a spreadsheet formula from a plain-language request"],
        ]),
    },
    "ai-tools-c2-l8": {
        "data_table": table(["Feature", "Benefit"], [
            ["Automated transcription", "Captures meeting notes without manual typing"],
        ]),
    },
    "ai-tools-c2-l9": {
        "data_table": table(["Task", "Example"], [
            ["Caption generation", "Drafting social media captions matching a brand's tone"],
        ]),
    },
    "ai-tools-c2-l10": {
        "data_table": table(["Criterion", "Consideration"], [
            ["Output quality", "How coherent and accurate the generated text is"], ["Cost", "Pricing model relative to usage needs"],
        ]),
    },
    "ai-tools-c2-l11": {
        "data_table": table(["Task", "Example"], [
            ["Deduplication", "Using AI to identify and merge duplicate records"],
        ]),
    },
    "ai-tools-c2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["AI plugin", "Extends an AI tool's capabilities by connecting it to external data or services"],
        ]),
    },
    "ai-tools-c2-l13": {
        "data_table": table(["Feature", "Example"], [
            ["Auto-captioning", "Automatically generates subtitles for a video"],
        ]),
    },
    "ai-tools-c2-l14": {
        "data_table": table(["Practice", "Reason"], [
            ["Verifying AI-generated facts", "AI outputs can contain confident but incorrect information"],
        ]),
    },
    "ai-tools-c2-l15": {
        "data_table": table(["Component", "Purpose"], [
            ["Intent recognition", "Identifies what the customer is actually asking for"],
        ]),
    },
    "ai-tools-c2-l16": {
        "data_table": table(["Practice", "Benefit"], [
            ["Chaining AI outputs together", "Builds a repeatable multi-step workflow instead of one-off requests"],
        ]),
    },
    "ai-tools-c2-l17": {
        "data_table": table(["Task", "Example"], [
            ["Noise removal", "AI tools can automatically clean up background audio noise"],
        ]),
    },
    "ai-tools-c2-l18": {
        "data_table": table(["Concern", "Detail"], [
            ["Data retention policy", "Determines how long an AI provider stores user input"],
        ]),
    },
    "ai-tools-c2-l19": {
        "data_table": table(["Task", "Example"], [
            ["Budget categorization", "AI tools can automatically classify transactions into spending categories"],
        ]),
    },
    "ai-tools-c2-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Combining multiple tools", "Builds an end-to-end workflow spanning research, drafting, and design"],
        ]),
    },
    "ai-tools-c2-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Enterprise RAG", "Grounds an AI assistant's answers in a company's internal documents"],
        ]),
    },
    "ai-tools-c2-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Vector database", "Stores embeddings and enables fast similarity search for semantic retrieval"],
        ]),
    },
    "ai-tools-c2-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["AI agent with tool use", "An AI system that can call external functions or APIs to complete tasks"],
        ]),
    },
    "ai-tools-c2-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Multi-agent orchestration", "Coordinates several specialized AI agents to complete a complex task together"],
        ]),
    },
    "ai-tools-c2-l25": {
        "data_table": table(["Feature", "Benefit"], [
            ["No-code fine-tuning platform", "Lets non-engineers customize a model's behavior through a simple interface"],
        ]),
    },
    "ai-tools-c2-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Benchmark leaderboard", "Ranks AI models by standardized task performance for comparison"],
        ]),
    },
    "ai-tools-c2-l27": {
        "data_table": table(["Practice", "Reason"], [
            ["Setting rate limits", "Prevents runaway API costs from unexpected usage spikes"],
        ]),
    },
    "ai-tools-c2-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Prompt chaining", "Passes the output of one AI call as input to the next, automating multi-step tasks"],
        ]),
    },
    "ai-tools-c2-l29": {
        "data_table": table(["Task", "Example"], [
            ["Automated code review", "Flagging style violations and potential bugs before human review"],
        ]),
    },
    "ai-tools-c2-l30": {
        "data_table": table(["Task", "Example"], [
            ["Test case generation", "Producing unit tests automatically from function signatures"],
        ]),
    },
    "ai-tools-c2-l31": {
        "data_table": table(["Feature", "Benefit"], [
            ["BI copilot", "Lets users query business data using natural language instead of writing SQL"],
        ]),
    },
    "ai-tools-c2-l32": {
        "data_table": table(["Task", "Example"], [
            ["Clause extraction", "Automatically identifying risk clauses across thousands of contracts"],
        ]),
    },
    "ai-tools-c2-l33": {
        "data_table": table(["Task", "Example"], [
            ["Ambient documentation", "Generating clinical notes automatically from a patient conversation"],
        ]),
    },
    "ai-tools-c2-l34": {
        "data_table": table(["Task", "Example"], [
            ["Scenario modeling", "Generating multiple financial forecast scenarios from historical data"],
        ]),
    },
    "ai-tools-c2-l35": {
        "data_table": table(["Task", "Example"], [
            ["Survey synthesis", "Summarizing themes across thousands of open-ended survey responses"],
        ]),
    },
    "ai-tools-c2-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Model risk management", "Identifies and monitors risks from deploying AI models in production"],
        ]),
    },
    "ai-tools-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Synthetic data", "Artificially generated data used to train or test models without exposing real records"],
        ]),
    },
    "ai-tools-c2-l38": {
        "data_table": table(["Task", "Example"], [
            ["Data annotation", "Labeling images or text so a model can learn from them"],
        ]),
    },
    "ai-tools-c2-l39": {
        "data_table": table(["Task", "Example"], [
            ["Automated localization", "Adapting content for a new language and region using AI translation"],
        ]),
    },
    "ai-tools-c2-l40": {
        "data_table": table(["Step", "Purpose"], [
            ["Automating video assembly", "Combines generated clips, captions, and audio without manual editing"],
        ]),
    },
    "ai-tools-c2-l41": {
        "data_table": table(["Concern", "Detail"], [
            ["Consent for voice cloning", "Using someone's voice without permission raises serious ethical and legal issues"],
        ]),
    },
    "ai-tools-c2-l42": {
        "data_table": table(["Task", "Example"], [
            ["Texture generation", "Creating game asset textures automatically from a text description"],
        ]),
    },
    "ai-tools-c2-l43": {
        "data_table": table(["Feature", "Benefit"], [
            ["Embedded copilot", "Surfaces AI assistance directly within existing enterprise software"],
        ]),
    },
    "ai-tools-c2-l44": {
        "data_table": table(["Task", "Example"], [
            ["Content gap analysis", "Identifying missing keywords or topics across a website's content"],
        ]),
    },
    "ai-tools-c2-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Prompt injection", "Malicious input designed to override an AI system's intended instructions"],
        ]),
    },
    "ai-tools-c2-l46": {
        "data_table": table(["Practice", "Reason"], [
            ["Access controls on AI tools", "Prevents unauthorized use and limits exposure of sensitive data"],
        ]),
    },
    "ai-tools-c2-l47": {
        "data_table": table(["Step", "Purpose"], [
            ["Testing prompt variants", "Identifies which prompt wording produces the most reliable output"],
        ]),
    },
    "ai-tools-c2-l48": {
        "data_table": table(["Step", "Purpose"], [
            ["Embedding and indexing documents", "Enables fast semantic search over a large document collection"],
        ]),
    },
    "ai-tools-c2-l49": {
        "data_table": table(["Task", "Example"], [
            ["Auto-generating documentation", "Producing API docs directly from code comments"],
        ]),
    },
    "ai-tools-c2-l50": {
        "data_table": table(["Task", "Example"], [
            ["Bulk sentiment scoring", "Classifying thousands of reviews as positive, neutral, or negative"],
        ]),
    },
    "ai-tools-c2-l51": {
        "data_table": table(["Feature", "Benefit"], [
            ["Component generation", "Creates reusable UI components from a design description"],
        ]),
    },
    "ai-tools-c2-l52": {
        "data_table": table(["Task", "Example"], [
            ["Automated contrast checking", "Flagging text and background color combinations that fail accessibility standards"],
        ]),
    },
    "ai-tools-c2-l53": {
        "data_table": table(["Task", "Example"], [
            ["Demand signal detection", "Identifying early indicators of shifting product demand"],
        ]),
    },
    "ai-tools-c2-l54": {
        "data_table": table(["Concern", "Detail"], [
            ["Bias in screening tools", "AI resume screeners can inherit and amplify historical hiring bias"],
        ]),
    },
    "ai-tools-c2-l55": {
        "data_table": table(["Task", "Example"], [
            ["Meeting summary extraction", "Automatically identifying action items and owners from a meeting transcript"],
        ]),
    },
    "ai-tools-c2-l56": {
        "data_table": table(["Factor", "Consideration"], [
            ["Build", "More control but higher engineering investment"], ["Buy", "Faster deployment but less customization"],
        ]),
    },
    "ai-tools-c2-l57": {
        "data_table": table(["Consideration", "Detail"], [
            ["Voice UI error handling", "Must gracefully manage misheard or ambiguous commands"],
        ]),
    },
    "ai-tools-c2-l58": {
        "data_table": table(["Task", "Example"], [
            ["Synthesizing research papers", "Summarizing key findings across many academic sources"],
        ]),
    },
    "ai-tools-c2-l59": {
        "data_table": table(["Task", "Example"], [
            ["Regulatory change tracking", "Flagging new rules relevant to a company's compliance obligations"],
        ]),
    },
    "ai-tools-c2-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Phased rollout", "Introduces an AI tool to a small group before organization-wide deployment"],
        ]),
    },
    "ai-tools-c2-l61": {
        "data_table": table(["Task", "Example"], [
            ["Building a pivot table via prompt", "Describing the desired summary in plain language"],
        ]),
    },
    "ai-tools-c2-l62": {
        "data_table": table(["Feature", "Detail"], [
            ["Escalation to human agent", "Ensures complex or sensitive issues are routed to a person"],
        ]),
    },
    "ai-tools-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Drafting an email with AI", "Comparing a first draft against a manually written version"],
        ]),
    },
    "ai-tools-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Generating a marketing image", "Iterating on a prompt to match a brand's visual style"],
        ]),
    },
    "ai-tools-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Writing an effective prompt", "Structuring instructions, context, and format in one request"],
        ]),
    },
    "ai-tools-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Refining a weak output", "Adding constraints to fix a vague first response"],
        ]),
    },
    "ai-tools-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Building a presentation outline", "Converting bullet points into a structured slide deck"],
        ]),
    },
    "ai-tools-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Specifying image style", "Comparing outputs from vague versus detailed style prompts"],
        ]),
    },
    "ai-tools-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Automating a repetitive spreadsheet task", "Writing a prompt that generates a reusable formula"],
        ]),
    },
    "ai-tools-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Reviewing a meeting transcript", "Extracting decisions and next steps from an AI-generated summary"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["AI Tools"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json AI Tools: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 AI Tools lessons (completing 70/70).")


if __name__ == "__main__":
    main()
