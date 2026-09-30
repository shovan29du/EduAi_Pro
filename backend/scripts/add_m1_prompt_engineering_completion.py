#!/usr/bin/env python3
"""Depth pass, M1 Prompt Engineering: fill in real, hand-checked
data_table content for the 119 M1 Prompt Engineering lessons not
covered by the earlier breadth-first batch. Brings M1 Prompt
Engineering to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning agentic
and multimodal prompting, theoretical foundations of prompting and
in-context learning, evaluation and safety, and applied
domain-specific prompt engineering; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_prompt_engineering_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Agentic workflow", "A prompted system that plans, calls tools, and acts over multiple steps toward a goal"],
    ["Tool-use prompting", "Instructs a model on when and how to invoke external functions or APIs"],
])

CHARTS: dict[str, dict] = {
    "prompt-engineering-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Coding task prompting", "Structures instructions to reliably produce correct, runnable code"],
    ])},
    "prompt-engineering-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Creative task prompting", "Balances constraint and openness to elicit originality from a model"],
    ])},
    "prompt-engineering-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Tool description design", "Writes clear function signatures and docs so an agent selects tools correctly"],
    ])},
    "prompt-engineering-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Multi-agent orchestration", "Coordinates prompts across several specialized agents working on one task"],
    ])},
    "prompt-engineering-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Task decomposition prompting", "Breaks a complex goal into smaller, sequential sub-tasks a model can plan"],
    ])},
    "prompt-engineering-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Memory architecture", "Structures how an agentic system stores and retrieves information across steps"],
    ])},
    "prompt-engineering-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Self-reflection prompting", "Asks a model to critique and improve its own prior output"],
    ])},
    "prompt-engineering-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Autonomous code execution", "Prompts a model to write and run code as part of solving a task"],
    ])},
    "prompt-engineering-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Human oversight", "Keeps a human able to review, approve, or halt an agentic system's actions"],
    ])},
    "prompt-engineering-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal prompting", "Structures prompts combining text with images, audio, or other modalities"],
    ])},
    "prompt-engineering-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Image and text input prompting", "Combines visual and textual context to guide a multimodal model's response"],
    ])},
    "prompt-engineering-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Voice/audio prompting", "Accounts for transcription errors and spoken-language patterns in prompt design"],
    ])},
    "prompt-engineering-m1-l14": {"data_table": table(["Approach", "Trade-off"], [
        ["Prompting", "Fast, flexible, no training required"],
        ["Fine-tuning", "More reliable for a narrow task, but requires data and compute"],
    ])},
    "prompt-engineering-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Prompt compression", "Shortens a prompt while preserving the information the model needs"],
    ])},
    "prompt-engineering-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Internal prompt guidelines", "Standardizes prompt style and safety practices across a team"],
    ])},
    "prompt-engineering-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Prompt engineering careers", "Includes roles like AI product engineer, applied research, and prompt operations"],
    ])},
    "prompt-engineering-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Production prompt system", "A deployed application that reliably serves prompted model outputs at scale"],
    ])},
    "prompt-engineering-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise prompt engineering", "Adds governance, auditability, and compliance to prompt-based applications"],
    ])},
    "prompt-engineering-m1-l20": {"data_table": table(["Trend", "Detail"], [
        ["Emerging prompt engineering", "Includes automated prompt optimization and agentic workflow design"],
    ])},
    "prompt-engineering-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Chain-of-thought", "Prompts a model to generate intermediate reasoning steps before an answer"],
    ])},
    "prompt-engineering-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Graph-of-thought", "Structures reasoning as an explorable graph rather than a single linear chain"],
    ])},
    "prompt-engineering-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Prompt injection", "Malicious input that hijacks a model's instructions to make it act against its intent"],
    ])},
    "prompt-engineering-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Jailbreak", "A crafted prompt designed to bypass a model's safety restrictions"],
    ])},
    "prompt-engineering-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Constitutional AI", "Trains a model to critique and revise its own outputs against written principles"],
    ])},
    "prompt-engineering-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["In-context learning", "A model performs a new task from examples in the prompt without weight updates"],
    ])},
    "prompt-engineering-m1-l27": {"data_table": table(["Method", "Feature"], [
        ["APE / OPRO", "Automatically search for and optimize prompt wording using another model"],
    ])},
    "prompt-engineering-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Gradient-free prompt search", "Optimizes discrete prompt text without access to model gradients"],
    ])},
    "prompt-engineering-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Soft prompting", "Learns continuous embedding vectors prepended to input instead of discrete text"],
    ])},
    "prompt-engineering-m1-l30": {"data_table": table(["Approach", "Feature"], [
        ["Prefix tuning", "Trains a small set of prefix vectors while keeping the model frozen"],
        ["Full fine-tuning", "Updates all model weights, higher cost but more capacity to adapt"],
    ])},
    "prompt-engineering-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Instruction tuning data design", "Curates instruction-response pairs to teach a model to follow commands well"],
    ])},
    "prompt-engineering-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["System prompt architecture", "Structures a persistent instruction layer that governs an assistant's behavior"],
    ])},
    "prompt-engineering-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Persona consistency", "Keeps a model's role-played character stable across a long conversation"],
    ])},
    "prompt-engineering-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Long-context prompting", "Organizes very large prompts so the model attends to relevant information"],
    ])},
    "prompt-engineering-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Prompt caching", "Reuses a previously processed prompt prefix to reduce latency and cost"],
    ])},
    "prompt-engineering-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Structured output", "Constrains a model's response to a valid JSON schema"],
    ])},
    "prompt-engineering-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Function calling", "Lets a model choose to invoke a defined external function with structured arguments"],
    ])},
    "prompt-engineering-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Prompt chaining", "Passes one prompt's output as the input to the next in a pipeline"],
    ])},
    "prompt-engineering-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Prompt templating and versioning", "Tracks and reuses prompt structures like versioned code artifacts"],
    ])},
    "prompt-engineering-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Prompt quality metric", "A measurable criterion (accuracy, relevance) for evaluating a prompt's output"],
    ])},
    "prompt-engineering-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["LLM-as-judge", "Uses one model to evaluate the quality of another model's outputs"],
    ])},
    "prompt-engineering-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Cross-model benchmarking", "Compares how the same prompt strategy performs across different LLMs"],
    ])},
    "prompt-engineering-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Query expansion", "Rewrites or extends a query to improve retrieval or model response coverage"],
    ])},
    "prompt-engineering-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Hallucination mitigation", "Prompt techniques that reduce confidently stated but incorrect model output"],
    ])},
    "prompt-engineering-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Grounding", "Anchors a model's response in retrieved or provided factual source material"],
    ])},
    "prompt-engineering-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Citation prompting", "Instructs a model to attribute claims to specific supporting sources"],
    ])},
    "prompt-engineering-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Code review prompting", "Structures prompts to surface bugs and suggest fixes systematically"],
    ])},
    "prompt-engineering-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Data extraction prompting", "Instructs a model to pull specific structured fields from unstructured text"],
    ])},
    "prompt-engineering-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Summarization quality control", "Prompt techniques to keep summaries faithful, concise, and complete"],
    ])},
    "prompt-engineering-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Classification prompting", "Structures prompts so a model reliably assigns text to defined categories"],
    ])},
    "prompt-engineering-m1-l51": {"data_table": table(["Approach", "Trade-off"], [
        ["Zero-shot", "No examples needed, but less reliable on unusual tasks"],
        ["Few-shot", "More reliable with examples, but uses more prompt tokens"],
    ])},
    "prompt-engineering-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Chain-of-verification", "Prompts a model to generate and check verification questions about its own answer"],
    ])},
    "prompt-engineering-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Self-consistency", "Samples multiple reasoning paths and takes the most common final answer"],
    ])},
    "prompt-engineering-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Ensemble prompting", "Combines outputs from multiple prompt variants or models to improve reliability"],
    ])},
    "prompt-engineering-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Reasoning benchmark prompting", "Tailors prompts to perform well on structured logical reasoning tests"],
    ])},
    "prompt-engineering-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Mathematical reasoning prompt", "Uses stepwise decomposition to improve accuracy on multi-step math problems"],
    ])},
    "prompt-engineering-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Legal document prompting", "Handles precise terminology and citation requirements in legal text analysis"],
    ])},
    "prompt-engineering-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Medical text prompting", "Requires caution, accuracy, and appropriate disclaimers in clinical contexts"],
    ])},
    "prompt-engineering-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Financial document prompting", "Extracts figures and terms accurately from complex financial filings"],
    ])},
    "prompt-engineering-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Multi-turn dialogue prompting", "Maintains context and consistency across an extended conversation"],
    ])},
    "prompt-engineering-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Customer support prompting", "Balances helpfulness, accuracy, and escalation rules for automated support"],
    ])},
    "prompt-engineering-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Content moderation prompting", "Instructs a model to detect and classify policy-violating content"],
    ])},
    "prompt-engineering-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Bias mitigation in prompts", "Adjusts prompt wording to reduce skewed or unfair model outputs"],
    ])},
    "prompt-engineering-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Cultural sensitivity prompting", "Accounts for cultural context to avoid inappropriate or offensive output"],
    ])},
    "prompt-engineering-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Cross-lingual prompt engineering", "Designs prompts that work reliably across multiple languages"],
    ])},
    "prompt-engineering-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Low-resource language prompting", "Adapts prompting strategy where a model has seen little training data"],
    ])},
    "prompt-engineering-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Code generation benchmarking", "Evaluates prompt strategies against standardized coding task suites"],
    ])},
    "prompt-engineering-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Test-driven prompt development", "Writes expected outputs first, then iterates the prompt to pass them"],
    ])},
    "prompt-engineering-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Prompt regression testing", "Detects when a prompt change unexpectedly degrades output quality"],
    ])},
    "prompt-engineering-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["A/B testing prompts", "Compares two prompt variants on real traffic to see which performs better"],
    ])},
    "prompt-engineering-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Prompt observability", "Logs and monitors prompt inputs/outputs to diagnose issues in production"],
    ])},
    "prompt-engineering-m1-l72": {"data_table": table(["Trade-off", "Detail"], [
        ["Cost-latency-quality", "Larger, slower models often produce better but more expensive/slower results"],
    ])},
    "prompt-engineering-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Model routing", "Sends simpler prompts to cheaper models and harder ones to more capable models"],
    ])},
    "prompt-engineering-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Small language model prompting", "Adapts prompt strategy to compensate for a smaller model's limited capacity"],
    ])},
    "prompt-engineering-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Prompted teacher distillation", "Uses a large model's prompted outputs as training data for a smaller model"],
    ])},
    "prompt-engineering-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic data generation", "Uses prompting to generate artificial training examples for another model"],
    ])},
    "prompt-engineering-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Dataset augmentation prompting", "Uses a model to expand a limited dataset with varied paraphrases"],
    ])},
    "prompt-engineering-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Agentic planning loop", "Structures a repeating cycle of plan, act, observe for an autonomous agent"],
    ])},
    "prompt-engineering-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["ReAct", "Interleaves reasoning traces with actions so a model can plan and act iteratively"],
    ])},
    "prompt-engineering-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Reflexion", "An agent verbally reflects on past failures to improve on subsequent attempts"],
    ])},
    "prompt-engineering-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Multi-agent debate", "Multiple model instances argue different positions to reach a better answer"],
    ])},
    "prompt-engineering-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Tool selection disambiguation", "Helps an agent choose the correct tool when several appear similarly relevant"],
    ])},
    "prompt-engineering-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["API orchestration prompting", "Coordinates a model's sequence of calls across multiple external APIs"],
    ])},
    "prompt-engineering-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Security auditing (prompt systems)", "Reviews a deployed prompt system for injection and data leakage risks"],
    ])},
    "prompt-engineering-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Red teaming (LLM apps)", "Deliberately probes an LLM application for harmful or unsafe outputs"],
    ])},
    "prompt-engineering-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Prompt governance", "Establishes review and compliance processes for prompts used in production"],
    ])},
    "prompt-engineering-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Prompt versioning / rollback", "Tracks prompt changes over time and can revert to a prior working version"],
    ])},
    "prompt-engineering-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Document layout prompting", "Instructs a model to interpret spatial structure in scanned or formatted documents"],
    ])},
    "prompt-engineering-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Speech-to-text pipeline prompting", "Structures prompts that account for transcription noise and errors"],
    ])},
    "prompt-engineering-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Embodied agent prompting", "Grounds prompts in a robot's sensor input and possible physical actions"],
    ])},
    "prompt-engineering-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Prompt research methodology", "Applies rigorous experimental design to studying prompting techniques"],
    ])},
    "prompt-engineering-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Scientific discovery prompting", "Uses prompts to help generate and evaluate scientific hypotheses"],
    ])},
    "prompt-engineering-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Recommendation explanation prompting", "Generates human-readable justifications for a system's recommendations"],
    ])},
    "prompt-engineering-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Video/temporal grounding prompting", "Instructs a model to locate events at specific points within a video"],
    ])},
    "prompt-engineering-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["3D/spatial reasoning prompting", "Structures prompts that reason about object positions and relationships in space"],
    ])},
    "prompt-engineering-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Automated unit test generation prompting", "Instructs a model to produce test cases covering a function's behavior"],
    ])},
    "prompt-engineering-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Music/audio generation prompting", "Structures prompts describing style, mood, and structure for generative audio models"],
    ])},
    "prompt-engineering-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Cross-modal alignment", "Ensures text prompts map consistently onto the visual features a diffusion model generates"],
    ])},
    "prompt-engineering-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Negotiation/multi-party simulation prompting", "Designs prompts for agents that simulate strategic multi-party interactions"],
    ])},
    "prompt-engineering-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Regulatory filing prompting", "Structures prompts to draft compliant, precisely worded regulatory documents"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"prompt-engineering-m1-l{base_n}"
    worked_key = f"prompt-engineering-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Prompt Engineering"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Prompt Engineering: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Prompt Engineering lessons (completing 120/120).")


if __name__ == "__main__":
    main()
