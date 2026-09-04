#!/usr/bin/env python3
"""Depth pass, C1 Prompt Engineering: fill in real, hand-checked
data_table content for the 69 C1 Prompt Engineering lessons not
covered by the earlier breadth-first batch. Brings C1 Prompt
Engineering to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_prompt_engineering_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "prompt-engineering-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Prompt engineering", "Crafting inputs to guide an AI model toward useful outputs"],
        ]),
    },
    "prompt-engineering-c1-l2": {
        "data_table": table(["Concept", "Meaning"], [
            ["Next-token prediction", "LLMs generate text by predicting the most likely next token repeatedly"],
        ]),
    },
    "prompt-engineering-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Token", "A chunk of text, often a word or part of a word, that a model processes"],
        ]),
    },
    "prompt-engineering-c1-l5": {
        "data_table": table(["Component", "Purpose"], [
            ["Task instruction", "States what you want done"], ["Context", "Provides relevant background information"],
        ]),
    },
    "prompt-engineering-c1-l6": {
        "data_table": table(["Practice", "Benefit"], [
            ["Being specific", "Reduces ambiguity and improves output relevance"],
        ]),
    },
    "prompt-engineering-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Instruction-following", "A model's ability to comply with explicit directions in a prompt"],
        ]),
    },
    "prompt-engineering-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Context window", "The maximum amount of text a model can consider at once"],
        ]),
    },
    "prompt-engineering-c1-l9": {
        "data_table": table(["Parameter", "Effect"], [
            ["Temperature", "Higher values produce more random, creative output"],
        ]),
    },
    "prompt-engineering-c1-l10": {
        "data_table": table(["Factor", "Effect"], [
            ["Overly long prompts", "Can dilute focus or exceed context limits"],
        ]),
    },
    "prompt-engineering-c1-l11": {
        "data_table": table(["Delimiter", "Purpose"], [
            ["Triple quotes or XML tags", "Clearly separates instructions from content to process"],
        ]),
    },
    "prompt-engineering-c1-l12": {
        "data_table": table(["Technique", "Benefit"], [
            ["Few-shot prompting", "Provides examples so the model matches your desired pattern"],
        ]),
    },
    "prompt-engineering-c1-l13": {
        "data_table": table(["Mistake", "Fix"], [
            ["Vague instructions", "Add specific detail and desired format"],
        ]),
    },
    "prompt-engineering-c1-l14": {
        "data_table": table(["Step", "Purpose"], [
            ["Test, review, revise", "Improves prompt effectiveness through repeated cycles"],
        ]),
    },
    "prompt-engineering-c1-l15": {
        "data_table": table(["Practice", "Reason"], [
            ["Asking one clear question", "Gets a focused, direct answer"],
        ]),
    },
    "prompt-engineering-c1-l16": {
        "data_table": table(["Element", "Purpose"], [
            ["Label options", "Specifies the categories the model should choose from"],
        ]),
    },
    "prompt-engineering-c1-l17": {
        "data_table": table(["Technique", "Example"], [
            ["Negative prompting", "'Do not include any code in your answer'"],
        ]),
    },
    "prompt-engineering-c1-l18": {
        "data_table": table(["Concept", "Meaning"], [
            ["Output randomness", "The same prompt can yield different responses depending on sampling settings"],
        ]),
    },
    "prompt-engineering-c1-l19": {
        "data_table": table(["Step", "Purpose"], [
            ["Comparing two prompt versions", "Identifies which phrasing produces better results"],
        ]),
    },
    "prompt-engineering-c1-l20": {
        "data_table": table(["Resource", "Purpose"], [
            ["Model documentation", "Explains a model's capabilities, limits, and best practices"],
        ]),
    },
    "prompt-engineering-c1-l21": {
        "data_table": table(["Type", "Purpose"], [
            ["System prompt", "Sets overall behavior and constraints for the model"], ["User prompt", "The specific request from the user"],
        ]),
    },
    "prompt-engineering-c1-l22": {
        "data_table": table(["Technique", "Example"], [
            ["Role prompting", "'You are an expert editor. Review this text...'"],
        ]),
    },
    "prompt-engineering-c1-l23": {
        "data_table": table(["Element", "Purpose"], [
            ["Length constraint", "Specifies how concise the summary should be"],
        ]),
    },
    "prompt-engineering-c1-l24": {
        "data_table": table(["Task", "Example"], [
            ["Content generation", "Drafting a blog post outline from a topic"],
        ]),
    },
    "prompt-engineering-c1-l25": {
        "data_table": table(["Element", "Purpose"], [
            ["Specifying language and requirements", "Guides accurate code generation"],
        ]),
    },
    "prompt-engineering-c1-l26": {
        "data_table": table(["Task", "Example"], [
            ["Data extraction", "Pulling names and dates from unstructured text"],
        ]),
    },
    "prompt-engineering-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Prompt template", "A reusable prompt structure with fillable slots"],
        ]),
    },
    "prompt-engineering-c1-l28": {
        "data_table": table(["Example", "Detail"], [
            ["{{customer_name}}", "A placeholder filled in dynamically at runtime"],
        ]),
    },
    "prompt-engineering-c1-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Conversation history", "Prior turns included so the model maintains context"],
        ]),
    },
    "prompt-engineering-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["System message", "A special instruction set at the start of a chat API call"],
        ]),
    },
    "prompt-engineering-c1-l31": {
        "data_table": table(["Task", "Example"], [
            ["Brainstorming", "Generating multiple ideas for a marketing campaign"],
        ]),
    },
    "prompt-engineering-c1-l32": {
        "data_table": table(["Task", "Example"], [
            ["Paraphrasing", "Rewriting a paragraph in a simpler tone"],
        ]),
    },
    "prompt-engineering-c1-l33": {
        "data_table": table(["Technique", "Example"], [
            ["Requesting a specific format", "'Respond only in valid JSON'"],
        ]),
    },
    "prompt-engineering-c1-l34": {
        "data_table": table(["Format", "Example"], [
            ["JSON", "Structured, machine-readable output"],
        ]),
        "formulae": ["{\"name\": \"Sam\", \"age\": 20}"],
    },
    "prompt-engineering-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Hallucination", "When a model generates confident but factually incorrect information"],
        ]),
    },
    "prompt-engineering-c1-l36": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Asking for sources", "Encourages more grounded, verifiable answers"],
        ]),
    },
    "prompt-engineering-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Model bias", "Systematic skew in outputs reflecting patterns in training data"],
        ]),
    },
    "prompt-engineering-c1-l38": {
        "data_table": table(["Principle", "Meaning"], [
            ["Avoiding harmful outputs", "Designing prompts responsibly to prevent misuse"],
        ]),
    },
    "prompt-engineering-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Prompt injection", "Malicious input designed to override a system's intended instructions"],
        ]),
    },
    "prompt-engineering-c1-l40": {
        "data_table": table(["Practice", "Reason"], [
            ["Validating model output", "Prevents acting on incorrect or unsafe responses"],
        ]),
    },
    "prompt-engineering-c1-l41": {
        "data_table": table(["Task", "Example"], [
            ["Question generation", "Creating quiz questions from a passage of text"],
        ]),
    },
    "prompt-engineering-c1-l42": {
        "data_table": table(["Task", "Example"], [
            ["Explanation", "Asking the model to explain a concept at a specific reading level"],
        ]),
    },
    "prompt-engineering-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Multimodal prompting", "Combining text with other input types like images"],
        ]),
    },
    "prompt-engineering-c1-l44": {
        "data_table": table(["Example", "Detail"], [
            ["Image + question", "Asking a model to describe or answer questions about an uploaded photo"],
        ]),
    },
    "prompt-engineering-c1-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Prompt chaining", "Using the output of one prompt as the input to the next"],
        ]),
    },
    "prompt-engineering-c1-l46": {
        "data_table": table(["Step", "Purpose"], [
            ["Breaking a task into subtasks", "Improves reliability on complex, multi-step problems"],
        ]),
    },
    "prompt-engineering-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["RAG", "Retrieval-Augmented Generation, supplies external documents to ground answers"],
        ]),
    },
    "prompt-engineering-c1-l48": {
        "data_table": table(["Technique", "Benefit"], [
            ["Grounding in provided context", "Reduces hallucination by anchoring answers to real source text"],
        ]),
    },
    "prompt-engineering-c1-l49": {
        "data_table": table(["Parameter", "Effect"], [
            ["Max tokens", "Limits the length of the generated response"],
        ]),
    },
    "prompt-engineering-c1-l50": {
        "data_table": table(["Parameter", "Meaning"], [
            ["Top-p", "Samples from the smallest set of tokens whose probability sums to p"], ["Top-k", "Samples only from the k most likely tokens"],
        ]),
    },
    "prompt-engineering-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Stop sequence", "A string that tells the model to stop generating further text"],
        ]),
    },
    "prompt-engineering-c1-l52": {
        "data_table": table(["Practice", "Reason"], [
            ["Setting explicit length limits", "Keeps responses within a usable size"],
        ]),
    },
    "prompt-engineering-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Prompt library", "A collection of tested, reusable prompts for common tasks"],
        ]),
    },
    "prompt-engineering-c1-l54": {
        "data_table": table(["Practice", "Benefit"], [
            ["Tracking prompt changes over time", "Enables reverting to a previous working version"],
        ]),
    },
    "prompt-engineering-c1-l55": {
        "data_table": table(["Criterion", "Question"], [
            ["Accuracy", "Is the output factually correct?"], ["Relevance", "Does it address the actual request?"],
        ]),
    },
    "prompt-engineering-c1-l56": {
        "data_table": table(["Metric", "Use"], [
            ["Human rating", "Manually scores output quality"], ["BLEU/ROUGE", "Automated text similarity scores"],
        ]),
    },
    "prompt-engineering-c1-l57": {
        "data_table": table(["Model Size", "Prompting Style"], [
            ["Smaller models", "Often need more explicit, structured instructions"], ["Larger models", "Can often handle more open-ended prompts"],
        ]),
    },
    "prompt-engineering-c1-l58": {
        "data_table": table(["Type", "Feature"], [
            ["Open-source model", "Weights are publicly available and modifiable"], ["Proprietary model", "Accessed only via a provider's API"],
        ]),
    },
    "prompt-engineering-c1-l59": {
        "data_table": table(["Approach", "When to Use"], [
            ["Prompting", "Fast, flexible, no retraining needed"], ["Fine-tuning", "Better for consistent, specialized behavior at scale"],
        ]),
    },
    "prompt-engineering-c1-l60": {
        "data_table": table(["Career", "Focus"], [
            ["Prompt engineer", "Designs and optimizes prompts for AI applications"], ["AI interaction designer", "Designs the overall user experience with AI systems"],
        ]),
    },
    "prompt-engineering-c1-l61": {
        "data_table": table(["Element", "Purpose"], [
            ["Explicit length target", "Constrains a summary to a specific word or sentence count"],
        ]),
    },
    "prompt-engineering-c1-l62": {
        "data_table": table(["Principle", "Meaning"], [
            ["Considering downstream impact", "Anticipates how a prompt's output might be used or misused"],
        ]),
    },
    "prompt-engineering-c1-l63": {
        "data_table": table(["Element", "Purpose"], [
            ["Clear category definitions", "Reduces ambiguous classification results"],
        ]),
    },
    "prompt-engineering-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Writing a first prompt", "Drafting a clear instruction for a simple summarization task"],
        ]),
    },
    "prompt-engineering-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Predicting model behavior", "Anticipating how a model will respond to an ambiguous prompt"],
        ]),
    },
    "prompt-engineering-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Explaining LLMs simply", "Describing how a language model generates text one token at a time"],
        ]),
    },
    "prompt-engineering-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Counting tokens", "Estimating how many tokens a sample sentence uses"],
        ]),
    },
    "prompt-engineering-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Building a good prompt", "Assembling instruction, context, and format into one prompt"],
        ]),
    },
    "prompt-engineering-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Rewriting a vague prompt", "Adding specificity to a sample underperforming prompt"],
        ]),
    },
    "prompt-engineering-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Testing instruction-following", "Checking whether a model obeys a formatting constraint"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Prompt Engineering"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Prompt Engineering: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Prompt Engineering lessons (completing 70/70).")


if __name__ == "__main__":
    main()
