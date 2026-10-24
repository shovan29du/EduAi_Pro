#!/usr/bin/env python3
"""Depth pass, M1 Natural Language Processing: fill in real,
hand-checked data_table content for the 119 M1 NLP lessons not
covered by the earlier breadth-first batch. Brings M1 NLP to full
120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning speech
processing, language model alignment, retrieval, parsing, dialogue
systems, and applied NLP domains; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_natural_language_processing_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["ASR (Automatic Speech Recognition)", "Converting spoken audio into text"],
    ["Phoneme", "The smallest unit of sound in speech"],
])

CHARTS: dict[str, dict] = {
    "natural-language-processing-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Speech & text interface", "A system that lets users interact through spoken or written natural language"],
    ])},
    "natural-language-processing-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Retrieval-augmented generation", "Combines a language model with retrieved external documents at inference time"],
    ])},
    "natural-language-processing-m1-l4": {"data_table": table(["Component", "Role"], [
        ["Acoustic model", "Maps audio features to phoneme/sub-word probabilities"],
        ["Language model", "Scores which word sequences are more plausible"],
    ])},
    "natural-language-processing-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["End-to-end ASR", "Maps audio directly to text in one trained model, without separate hand-built stages"],
    ])},
    "natural-language-processing-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Text-to-speech", "Synthesizes natural-sounding spoken audio from written text"],
    ])},
    "natural-language-processing-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Speech emotion recognition", "Infers a speaker's emotional state from vocal characteristics"],
    ])},
    "natural-language-processing-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Speaker diarization", "Determines who spoke when in an audio recording with multiple speakers"],
    ])},
    "natural-language-processing-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Voice activity detection", "Identifies segments of audio containing speech versus silence or noise"],
    ])},
    "natural-language-processing-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Bias in NLP", "Systematic skew in model outputs reflecting imbalances in training data"],
    ])},
    "natural-language-processing-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Misinformation detection", "Identifies text likely to contain false or misleading claims"],
    ])},
    "natural-language-processing-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Toxic language detection", "Classifies text as harmful, abusive, or hateful"],
    ])},
    "natural-language-processing-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Robustness testing", "Checks whether an NLP model's predictions remain stable under small input perturbations"],
    ])},
    "natural-language-processing-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Legal NLP", "Applies language models to contract review, case research, and legal document analysis"],
    ])},
    "natural-language-processing-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Biomedical NLP", "Applies language models to biomedical literature and clinical text"],
    ])},
    "natural-language-processing-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Clinical text mining", "Extracts structured medical information from unstructured clinical notes"],
    ])},
    "natural-language-processing-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Text-based recommendation", "Suggests items using natural-language content rather than only interaction history"],
    ])},
    "natural-language-processing-m1-l18": {"data_table": table(["Metric", "Measures"], [
        ["ROUGE / BLEU", "N-gram overlap between generated and reference text"],
    ])},
    "natural-language-processing-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Human evaluation", "Judges an NLP system's outputs using human raters rather than automatic metrics alone"],
    ])},
    "natural-language-processing-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["NLP capstone", "Integrates data collection, modeling, evaluation, and deployment into one project"],
    ])},
    "natural-language-processing-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Subword tokenization", "Splits words into smaller reusable units (e.g. BPE) to handle rare/unseen words"],
    ])},
    "natural-language-processing-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Positional encoding", "Injects token order information into a transformer's otherwise order-agnostic attention"],
    ])},
    "natural-language-processing-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Efficient long-context attention", "Reduces attention's quadratic cost to process much longer sequences"],
    ])},
    "natural-language-processing-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Prompt engineering", "Systematically designs input prompts to elicit better model behavior"],
    ])},
    "natural-language-processing-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["In-context learning", "A model performs a new task from examples in the prompt without weight updates"],
    ])},
    "natural-language-processing-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Chain-of-thought", "Prompts a model to generate intermediate reasoning steps before an answer"],
    ])},
    "natural-language-processing-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Instruction tuning", "Fine-tunes a model on instruction-response pairs to follow natural-language commands"],
    ])},
    "natural-language-processing-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["RLHF", "Reinforcement learning from human feedback; tunes a model using human preference signals"],
    ])},
    "natural-language-processing-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Constitutional AI", "Trains a model to critique and revise its own outputs against written principles"],
    ])},
    "natural-language-processing-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Parameter-efficient fine-tuning", "Adapts a large model by training a small number of new parameters (e.g. LoRA)"],
    ])},
    "natural-language-processing-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Quantization", "Reduces numeric precision of weights/activations to shrink and speed up a model"],
    ])},
    "natural-language-processing-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Mixture-of-experts LM", "Routes each token to a subset of specialized sub-networks"],
    ])},
    "natural-language-processing-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Dense passage retrieval", "Retrieves relevant text using learned dense vector embeddings rather than keyword matching"],
    ])},
    "natural-language-processing-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Hybrid sparse-dense retrieval", "Combines keyword-based and embedding-based retrieval for better recall"],
    ])},
    "natural-language-processing-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge graph integration", "Grounds a language model's outputs in structured relational facts"],
    ])},
    "natural-language-processing-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Hallucination", "A model generates plausible-sounding but factually incorrect or unsupported content"],
    ])},
    "natural-language-processing-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Factual consistency evaluation", "Checks whether generated text accurately reflects its source material"],
    ])},
    "natural-language-processing-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Long-document summarization", "Condenses lengthy documents that exceed a model's usual context handling"],
    ])},
    "natural-language-processing-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Multi-document summarization", "Synthesizes a single summary from several related source documents"],
    ])},
    "natural-language-processing-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Query-focused summarization", "Produces a summary tailored to a specific user question"],
    ])},
    "natural-language-processing-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Cross-lingual transfer", "Applies a model trained in one language to tasks in another"],
    ])},
    "natural-language-processing-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Low-resource language modeling", "Builds effective models for languages with limited training data"],
    ])},
    "natural-language-processing-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Neural machine translation", "Translates text using an end-to-end trained sequence model"],
    ])},
    "natural-language-processing-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Streaming translation", "Translates speech or text incrementally as input arrives, without waiting for completion"],
    ])},
    "natural-language-processing-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Document-level translation", "Translates using context from the whole document, not just isolated sentences"],
    ])},
    "natural-language-processing-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Coreference resolution", "Determines which expressions in text refer to the same real-world entity"],
    ])},
    "natural-language-processing-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Discourse parsing", "Analyzes how sentences relate to form a coherent larger text structure"],
    ])},
    "natural-language-processing-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Semantic role labeling", "Identifies who did what to whom within a sentence"],
    ])},
    "natural-language-processing-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Abstract meaning representation", "A graph-based formalism capturing a sentence's meaning independent of its exact wording"],
    ])},
    "natural-language-processing-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Transition-based parsing", "Builds a dependency parse via a sequence of incremental shift-reduce actions"],
    ])},
    "natural-language-processing-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Constituency parsing", "Builds a tree representing a sentence's nested phrase structure"],
    ])},
    "natural-language-processing-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Low-resource NER", "Recognizes named entities in languages or domains with little labeled data"],
    ])},
    "natural-language-processing-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Relation extraction", "Identifies structured relationships between entities mentioned in text"],
    ])},
    "natural-language-processing-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Event extraction", "Identifies events and their temporal relationships from text"],
    ])},
    "natural-language-processing-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Stance detection", "Classifies whether text is for, against, or neutral toward a claim"],
    ])},
    "natural-language-processing-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Argumentation mining", "Automatically identifies argument components and their relationships in text"],
    ])},
    "natural-language-processing-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Text simplification", "Rewrites text to be easier to read while preserving its meaning"],
    ])},
    "natural-language-processing-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Style transfer", "Rewrites text in a different tone or style while preserving its content"],
    ])},
    "natural-language-processing-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Dialogue state tracking", "Maintains a structured record of what has been established so far in a conversation"],
    ])},
    "natural-language-processing-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Task-oriented dialogue", "A conversational system designed to help a user complete a specific goal"],
    ])},
    "natural-language-processing-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Open-domain dialogue", "Generates conversational responses without being restricted to a narrow task"],
    ])},
    "natural-language-processing-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Persona-consistent dialogue", "Keeps a conversational agent's responses aligned with a defined character or persona"],
    ])},
    "natural-language-processing-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Open-ended generation evaluation", "Judges the quality of free-form text where there is no single correct answer"],
    ])},
    "natural-language-processing-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Calibration", "How well a model's confidence scores match its actual accuracy"],
    ])},
    "natural-language-processing-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Adversarial robustness (NLP)", "How well a model resists small, deliberately crafted input perturbations"],
    ])},
    "natural-language-processing-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Data augmentation", "Generates additional training examples through transformations of existing text"],
    ])},
    "natural-language-processing-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Active learning for annotation", "Selects the most informative unlabeled text examples to annotate next"],
    ])},
    "natural-language-processing-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["LLM distillation", "Trains a smaller model to mimic a larger language model's behavior"],
    ])},
    "natural-language-processing-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["End-to-end speech translation", "Translates speech in one source language directly to text in another"],
    ])},
    "natural-language-processing-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Code-switching", "Alternating between two or more languages within a single conversation or sentence"],
    ])},
    "natural-language-processing-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Distributional semantics", "Represents word meaning by the contexts a word tends to appear in"],
    ])},
    "natural-language-processing-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Compositional semantics", "Builds the meaning of a phrase from the meanings of its parts and how they combine"],
    ])},
    "natural-language-processing-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Probing", "Trains a simple classifier on a model's internal representations to test what they encode"],
    ])},
    "natural-language-processing-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Attention interpretability", "Studies whether attention weights reliably explain a model's predictions"],
    ])},
    "natural-language-processing-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Bias auditing", "Systematically tests an NLP system for unfair or skewed outputs across groups"],
    ])},
    "natural-language-processing-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Privacy-preserving NLP training", "Trains language models while limiting memorization or leakage of sensitive text"],
    ])},
    "natural-language-processing-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Legal document analysis", "Applies NLP to extract clauses, obligations, and risks from contracts"],
    ])},
    "natural-language-processing-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Clinical note understanding", "Extracts structured medical facts from free-text clinical documentation"],
    ])},
    "natural-language-processing-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Scientific literature mining", "Extracts findings and relationships from research papers at scale"],
    ])},
    "natural-language-processing-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Financial text analytics", "Extracts sentiment and signals from financial news, filings, and reports"],
    ])},
    "natural-language-processing-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Social media text normalization", "Converts informal, noisy social text into a more standard form for processing"],
    ])},
    "natural-language-processing-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Cross-lingual information retrieval", "Retrieves documents in one language using a query written in another"],
    ])},
    "natural-language-processing-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Question answering over knowledge bases", "Answers questions by querying a structured knowledge base"],
    ])},
    "natural-language-processing-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Multi-hop QA", "Answers a question that requires combining evidence from multiple sources"],
    ])},
    "natural-language-processing-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Open-domain QA pipeline", "Combines a retriever and a reader to answer questions from a large document collection"],
    ])},
    "natural-language-processing-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Text-to-SQL", "Translates a natural-language question into an executable database query"],
    ])},
    "natural-language-processing-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Table understanding", "Answers questions or extracts facts from structured tabular data"],
    ])},
    "natural-language-processing-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Vision-language model", "Jointly processes and relates image and text data"],
    ])},
    "natural-language-processing-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Grounded language understanding", "Connects language to an embodied agent's perception and actions in an environment"],
    ])},
    "natural-language-processing-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["LLM reasoning evaluation", "Assesses a language model's ability to solve multi-step logical or mathematical problems"],
    ])},
    "natural-language-processing-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Text watermarking", "Embeds a detectable signal in generated text to trace its AI provenance"],
    ])},
    "natural-language-processing-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Ethical LLM deployment", "Considers misuse, bias, and societal impact when releasing large language models"],
    ])},
    "natural-language-processing-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Continual pretraining", "Further trains a language model on new data after its initial pretraining phase"],
    ])},
    "natural-language-processing-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic data generation", "Uses a model to generate additional training data for another model"],
    ])},
    "natural-language-processing-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Emotion cause extraction", "Identifies the specific text span that triggers an expressed emotion"],
    ])},
    "natural-language-processing-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Needle-in-haystack evaluation", "Tests whether a model can retrieve a specific fact buried in a very long context"],
    ])},
    "natural-language-processing-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["RLAIF", "Uses AI-generated feedback, instead of human feedback, to reduce toxic model outputs"],
    ])},
    "natural-language-processing-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Morphologically rich language modeling", "Handles languages where words carry complex internal grammatical structure"],
    ])},
    "natural-language-processing-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Semantic parsing for voice assistants", "Converts a spoken utterance into a structured intent and set of parameters"],
    ])},
    "natural-language-processing-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Cross-lingual word sense disambiguation", "Determines the correct meaning of an ambiguous word across different languages"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"natural-language-processing-m1-l{base_n}"
    worked_key = f"natural-language-processing-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Natural Language Processing"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Natural Language Processing: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Natural Language Processing lessons (completing 120/120).")


if __name__ == "__main__":
    main()
