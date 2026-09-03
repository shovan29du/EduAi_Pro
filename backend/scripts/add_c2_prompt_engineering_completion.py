#!/usr/bin/env python3
"""Depth pass, C2 Prompt Engineering: fill in real, hand-checked
data_table content for the 69 C2 Prompt Engineering lessons not
covered by the earlier breadth-first batch. Brings C2 Prompt
Engineering to full 70/70 coverage. This is the final subject
completing the full C2 depth pass (53/53 subjects).

l61-l70 are "Worked Analysis" companions to l1-l10. l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_prompt_engineering_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "prompt-engineering-c2-l1": {
        "data_table": table(["Prompting Approach", "Description"], [
            ["Zero-shot", "No examples given, just an instruction"],
            ["Few-shot", "A small number of examples given before the task"],
        ]),
    },
    "prompt-engineering-c2-l2": {
        "data_table": table(["Technique", "Effect"], [
            ["Chain-of-thought prompting", "Asks the model to reason step by step before answering"],
        ]),
    },
    "prompt-engineering-c2-l4": {
        "data_table": table(["Technique", "Purpose"], [
            ["Prompt priming", "Sets context or role before the actual task instruction"],
        ]),
    },
    "prompt-engineering-c2-l5": {
        "data_table": table(["Phrase", "Effect"], [
            ["\"Let's think step by step\"", "Encourages the model to show intermediate reasoning"],
        ]),
    },
    "prompt-engineering-c2-l6": {
        "data_table": table(["Technique", "Effect"], [
            ["Self-consistency", "Samples multiple reasoning paths and selects the most common answer"],
        ]),
    },
    "prompt-engineering-c2-l7": {
        "data_table": table(["Technique", "Effect"], [
            ["Least-to-most prompting", "Breaks a complex problem into simpler subproblems solved in sequence"],
        ]),
    },
    "prompt-engineering-c2-l8": {
        "data_table": table(["Concept", "Detail"], [
            ["Tree-of-thought", "Explores multiple reasoning branches and evaluates which to pursue"],
        ]),
    },
    "prompt-engineering-c2-l9": {
        "data_table": table(["Component", "Role"], [
            ["ReAct", "Interleaves reasoning steps with actions like tool calls"],
        ]),
    },
    "prompt-engineering-c2-l10": {
        "data_table": table(["Concept", "Effect"], [
            ["Instruction tuning", "Fine-tunes a model to better follow natural-language instructions"],
        ]),
    },
    "prompt-engineering-c2-l11": {
        "data_table": table(["Technique", "Purpose"], [
            ["Persona consistency", "Reinforces a defined character or role across a multi-turn conversation"],
        ]),
    },
    "prompt-engineering-c2-l12": {
        "data_table": table(["Technique", "Purpose"], [
            ["Style transfer prompting", "Instructs the model to rewrite text in a specified tone or style"],
        ]),
    },
    "prompt-engineering-c2-l13": {
        "data_table": table(["Element", "Purpose"], [
            ["Register control", "Explicit instruction sets formality level in the model's output"],
        ]),
    },
    "prompt-engineering-c2-l14": {
        "data_table": table(["Practice", "Purpose"], [
            ["Translation prompting", "Specifying source/target language and tone improves translation accuracy"],
        ]),
    },
    "prompt-engineering-c2-l15": {
        "data_table": table(["Practice", "Purpose"], [
            ["Sentiment analysis prompting", "Clear output format instructions improve consistency of labels"],
        ]),
    },
    "prompt-engineering-c2-l16": {
        "data_table": table(["Technique", "Purpose"], [
            ["Guardrail prompting", "Explicit constraints reduce unwanted or off-topic model output"],
        ]),
    },
    "prompt-engineering-c2-l17": {
        "data_table": table(["Technique", "Purpose"], [
            ["Length control", "Explicit word/sentence limits shape response conciseness"],
        ]),
    },
    "prompt-engineering-c2-l18": {
        "data_table": table(["Technique", "Purpose"], [
            ["Prompt debugging", "Isolates which part of a prompt causes an undesired output"],
        ]),
    },
    "prompt-engineering-c2-l19": {
        "data_table": table(["Technique", "Purpose"], [
            ["Clarifying ambiguous requests", "Prompting the model to ask a clarifying question reduces misinterpretation"],
        ]),
    },
    "prompt-engineering-c2-l20": {
        "data_table": table(["Technique", "Purpose"], [
            ["Multi-step instruction prompting", "Numbered steps improve reliable execution of sequential tasks"],
        ]),
    },
    "prompt-engineering-c2-l21": {
        "data_table": table(["Variant", "Detail"], [
            ["Zero-shot CoT", "Adds a reasoning trigger phrase without providing worked examples"],
        ]),
    },
    "prompt-engineering-c2-l22": {
        "data_table": table(["Technique", "Purpose"], [
            ["Automatic CoT generation", "Automatically generates reasoning chains rather than hand-writing them"],
        ]),
    },
    "prompt-engineering-c2-l23": {
        "data_table": table(["Component", "Role"], [
            ["Retrieval-augmented generation", "Retrieves relevant documents to ground a model's response in evidence"],
        ]),
    },
    "prompt-engineering-c2-l24": {
        "data_table": table(["Stage", "Purpose"], [
            ["RAG prompt design", "Formats retrieved context clearly so the model can cite and use it"],
        ]),
    },
    "prompt-engineering-c2-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Prompt chaining", "Feeds the output of one prompt as input into the next"],
        ]),
    },
    "prompt-engineering-c2-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Multi-agent workflow", "Coordinates multiple specialized model roles to complete a complex task"],
        ]),
    },
    "prompt-engineering-c2-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Function calling", "The model outputs a structured request to invoke an external tool"],
        ]),
    },
    "prompt-engineering-c2-l28": {
        "data_table": table(["Element", "Purpose"], [
            ["Function schema", "Defines a tool's name, parameters, and types for the model to call correctly"],
        ]),
    },
    "prompt-engineering-c2-l29": {
        "data_table": table(["Threat", "Mitigation"], [
            ["Prompt injection", "Malicious input attempts to override system instructions"],
        ]),
    },
    "prompt-engineering-c2-l30": {
        "data_table": table(["Practice", "Purpose"], [
            ["Red-teaming", "Deliberately probes a system for unsafe or unintended outputs"],
        ]),
    },
    "prompt-engineering-c2-l31": {
        "data_table": table(["Method", "Purpose"], [
            ["LLM output evaluation framework", "Systematically scores outputs against defined quality criteria"],
        ]),
    },
    "prompt-engineering-c2-l32": {
        "data_table": table(["Technique", "Purpose"], [
            ["Automated prompt optimization", "Iteratively refines a prompt based on measured output quality"],
        ]),
    },
    "prompt-engineering-c2-l33": {
        "data_table": table(["Technique", "Purpose"], [
            ["Prompt compression", "Reduces token count while preserving essential instruction content"],
        ]),
    },
    "prompt-engineering-c2-l34": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Long-context management", "Prioritizes and summarizes content to fit within a model's context window"],
        ]),
    },
    "prompt-engineering-c2-l35": {
        "data_table": table(["Technique", "Purpose"], [
            ["Schema validation", "Verifies model output matches an expected structured format"],
        ]),
    },
    "prompt-engineering-c2-l36": {
        "data_table": table(["Technique", "Purpose"], [
            ["Constrained decoding", "Restricts model output to a defined grammar or format at generation time"],
        ]),
    },
    "prompt-engineering-c2-l37": {
        "data_table": table(["Technique", "Purpose"], [
            ["Persona reinforcement", "Periodic reminders maintain character consistency over long conversations"],
        ]),
    },
    "prompt-engineering-c2-l38": {
        "data_table": table(["Technique", "Purpose"], [
            ["Multi-agent debate", "Multiple model instances critique each other to improve answer quality"],
        ]),
    },
    "prompt-engineering-c2-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Program-aided language model", "Generates executable code to perform precise computation within reasoning"],
        ]),
    },
    "prompt-engineering-c2-l40": {
        "data_table": table(["Technique", "Purpose"], [
            ["Multi-step workflow prompting", "Decomposes a complex task into an explicit, ordered sequence of steps"],
        ]),
    },
    "prompt-engineering-c2-l41": {
        "data_table": table(["Practice", "Purpose"], [
            ["Few-shot curation at scale", "Selects diverse, representative examples to maximize prompt generalization"],
        ]),
    },
    "prompt-engineering-c2-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Meta-prompting", "Uses one prompt to generate or refine another prompt"],
        ]),
    },
    "prompt-engineering-c2-l43": {
        "data_table": table(["Technique", "Purpose"], [
            ["Hallucination reduction", "Grounding responses in retrieved evidence reduces fabricated claims"],
        ]),
    },
    "prompt-engineering-c2-l44": {
        "data_table": table(["Practice", "Purpose"], [
            ["Fact-checking prompting", "Asks the model to cite sources or flag uncertain claims"],
        ]),
    },
    "prompt-engineering-c2-l45": {
        "data_table": table(["Practice", "Purpose"], [
            ["Bias auditing", "Systematically tests outputs across demographic variations for unequal treatment"],
        ]),
    },
    "prompt-engineering-c2-l46": {
        "data_table": table(["Consideration", "Detail"], [
            ["Multilingual prompting", "Prompt phrasing and examples should match the target language's conventions"],
        ]),
    },
    "prompt-engineering-c2-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Multimodal prompting", "Combines text with images or other modalities in a single prompt"],
        ]),
    },
    "prompt-engineering-c2-l48": {
        "data_table": table(["Practice", "Purpose"], [
            ["Code review prompting", "Structured prompts guide the model to flag bugs, style, and security issues"],
        ]),
    },
    "prompt-engineering-c2-l49": {
        "data_table": table(["Practice", "Purpose"], [
            ["Data analysis prompting", "Clear schema and goal descriptions improve accuracy of generated analysis"],
        ]),
    },
    "prompt-engineering-c2-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Agentic system prompting", "Defines goals, tools, and constraints for a model operating autonomously"],
        ]),
    },
    "prompt-engineering-c2-l51": {
        "data_table": table(["Element", "Purpose"], [
            ["Production guardrail", "Layered checks catch unsafe or off-policy outputs before they reach users"],
        ]),
    },
    "prompt-engineering-c2-l52": {
        "data_table": table(["Method", "Purpose"], [
            ["Prompt A/B testing", "Compares prompt variants against real usage metrics to select the best"],
        ]),
    },
    "prompt-engineering-c2-l53": {
        "data_table": table(["Factor", "Optimization"], [
            ["Token count", "Shorter prompts reduce both cost and response latency"],
        ]),
    },
    "prompt-engineering-c2-l54": {
        "data_table": table(["Approach", "Detail"], [
            ["Domain-specific prompting", "Incorporates specialized terminology and constraints of a target field"],
        ]),
    },
    "prompt-engineering-c2-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Enterprise knowledge base prompting", "Grounds responses in an organization's proprietary documents"],
        ]),
    },
    "prompt-engineering-c2-l56": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Context window management", "Prioritizes the most relevant content when input exceeds model limits"],
        ]),
    },
    "prompt-engineering-c2-l57": {
        "data_table": table(["Consideration", "Detail"], [
            ["Model architecture differences", "Prompting effectiveness varies across model families and sizes"],
        ]),
    },
    "prompt-engineering-c2-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Instruction tuning alignment", "Aligns model behavior more closely with intended prompt instructions"],
        ]),
    },
    "prompt-engineering-c2-l59": {
        "data_table": table(["Domain", "Application"], [
            ["Industry case study", "Real deployments reveal practical trade-offs not visible in isolated examples"],
        ]),
    },
    "prompt-engineering-c2-l60": {
        "data_table": table(["Element", "Purpose"], [
            ["Prompt engineering portfolio", "Demonstrates applied skill through documented, real-world prompt examples"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Prompting Approach", "Description"], [
    ["Zero-shot", "No examples given, just an instruction"],
    ["Few-shot", "A small number of examples given before the task"],
])

# l61-l70 "Worked Analysis" lessons reuse the data_table of l1-l10.
WORKED_ANALYSIS_MAP = {61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"prompt-engineering-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"prompt-engineering-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"prompt-engineering-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Prompt Engineering"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Prompt Engineering: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Prompt Engineering lessons (completing 70/70).")


if __name__ == "__main__":
    main()
