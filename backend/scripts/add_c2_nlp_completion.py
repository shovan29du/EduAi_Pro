#!/usr/bin/env python3
"""Depth pass, C2 Natural Language Processing: fill in real, hand-checked
data_table content for the 71 C2 NLP lessons not covered by the earlier
breadth-first batch. Brings C2 NLP to full 72/72 coverage.

Note: unlike most C2 subjects (70 lessons), NLP has 72 lessons.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_nlp_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "natural-language-processing-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Tokenization", "Splitting text into smaller units like words or subwords"],
        ]),
    },
    "natural-language-processing-c2-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Language model", "A model estimating the probability of a sequence of words"],
        ]),
    },
    "natural-language-processing-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Perplexity", "A metric measuring how well a language model predicts a sample, lower is better"],
        ]),
        "formulae": ["perplexity = 2 ** (cross_entropy_loss)"],
    },
    "natural-language-processing-c2-l5": {
        "data_table": table(["Technique", "Purpose"], [
            ["Laplace smoothing", "Prevents zero probabilities for unseen n-grams"],
        ]),
    },
    "natural-language-processing-c2-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Hidden Markov Model", "Models sequences using hidden states, used for tagging parts of speech"],
        ]),
    },
    "natural-language-processing-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Conditional Random Field", "A sequence labeling model considering the full context of a sequence"],
        ]),
    },
    "natural-language-processing-c2-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Probabilistic CFG", "A context-free grammar with probabilities assigned to each production rule"],
        ]),
    },
    "natural-language-processing-c2-l9": {
        "data_table": table(["Feature", "Detail"], [
            ["Bag-of-words with SVM", "A classic strong baseline for text classification tasks"],
        ]),
    },
    "natural-language-processing-c2-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["LDA", "A generative model discovering latent topics as distributions over words"],
        ]),
    },
    "natural-language-processing-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Latent Semantic Analysis", "Uses matrix decomposition to uncover latent relationships between terms and documents"],
        ]),
    },
    "natural-language-processing-c2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["NMF", "Factorizes a document-term matrix into non-negative components representing topics"],
        ]),
    },
    "natural-language-processing-c2-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Word sense disambiguation", "Determines which meaning of a word applies given its context"],
        ]),
    },
    "natural-language-processing-c2-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Semantic role labeling", "Identifies who did what to whom in a sentence"],
        ]),
    },
    "natural-language-processing-c2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Discourse coherence", "How well ideas connect logically across sentences in a text"],
        ]),
    },
    "natural-language-processing-c2-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Rhetorical Structure Theory", "Describes hierarchical relationships between text segments, like cause and elaboration"],
        ]),
    },
    "natural-language-processing-c2-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Aspect-based sentiment analysis", "Identifies sentiment toward specific attributes of an entity, not just overall tone"],
        ]),
    },
    "natural-language-processing-c2-l18": {
        "data_table": table(["Approach", "Feature"], [
            ["Emotion detection", "Classifies text into fine-grained emotions like joy, anger, or fear"],
        ]),
    },
    "natural-language-processing-c2-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Hierarchical text classification", "Assigns labels organized in a tree-structured taxonomy"],
        ]),
    },
    "natural-language-processing-c2-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Multi-label classification", "Assigns multiple non-exclusive categories to a single text"],
        ]),
    },
    "natural-language-processing-c2-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Byte Pair Encoding", "Iteratively merges frequent character pairs to build a subword vocabulary"],
        ]),
    },
    "natural-language-processing-c2-l22": {
        "data_table": table(["Method", "Feature"], [
            ["WordPiece", "Used in BERT, selects merges maximizing likelihood"], ["SentencePiece", "Treats text as raw input, language-agnostic"],
        ]),
    },
    "natural-language-processing-c2-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Contextual embedding", "A word representation that changes based on surrounding context, unlike static embeddings"],
        ]),
    },
    "natural-language-processing-c2-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Self-attention", "Relates each token in a sequence to every other token to compute contextual representations"],
        ]),
    },
    "natural-language-processing-c2-l25": {
        "data_table": table(["Component", "Role"], [
            ["Encoder", "Processes the input sequence into representations"], ["Decoder", "Generates the output sequence using encoder representations"],
        ]),
    },
    "natural-language-processing-c2-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Masked language modeling", "Predicts randomly hidden tokens using bidirectional context, used to pretrain BERT"],
        ]),
    },
    "natural-language-processing-c2-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Autoregressive modeling", "Predicts the next token based only on preceding tokens, used in GPT"],
        ]),
    },
    "natural-language-processing-c2-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Fine-tuning", "Adapts a pretrained language model to a specific downstream task"],
        ]),
    },
    "natural-language-processing-c2-l29": {
        "data_table": table(["Technique", "Example"], [
            ["Chain-of-thought prompting", "Guides a model to reason step by step before answering"],
        ]),
    },
    "natural-language-processing-c2-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Seq2seq model", "Maps a variable-length input sequence to a variable-length output sequence"],
        ]),
    },
    "natural-language-processing-c2-l31": {
        "data_table": table(["Mechanism", "Purpose"], [
            ["Attention in NMT", "Lets the decoder focus on relevant source words when generating each target word"],
        ]),
    },
    "natural-language-processing-c2-l32": {
        "data_table": table(["Metric", "Meaning"], [
            ["BLEU", "Measures n-gram overlap between machine and reference translations"],
        ]),
    },
    "natural-language-processing-c2-l33": {
        "data_table": table(["Approach", "Feature"], [
            ["Abstractive summarization", "Generates new sentences capturing the source's meaning, rather than extracting text"],
        ]),
    },
    "natural-language-processing-c2-l34": {
        "data_table": table(["Metric", "Meaning"], [
            ["ROUGE", "Measures overlap between generated and reference summaries"],
        ]),
    },
    "natural-language-processing-c2-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Dependency parsing", "Analyzes grammatical structure by identifying head-dependent relations between words"],
        ]),
    },
    "natural-language-processing-c2-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Constituency parsing", "Breaks a sentence into nested phrase structures like noun and verb phrases"],
        ]),
    },
    "natural-language-processing-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Coreference resolution", "Identifies when different expressions refer to the same entity"],
        ]),
    },
    "natural-language-processing-c2-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Relation extraction", "Identifies structured relationships between entities mentioned in text"],
        ]),
    },
    "natural-language-processing-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Open-domain QA", "Answers questions using a broad, unrestricted knowledge source rather than a fixed passage"],
        ]),
    },
    "natural-language-processing-c2-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Reading comprehension model", "Extracts or generates an answer from a given passage of text"],
        ]),
    },
    "natural-language-processing-c2-l41": {
        "data_table": table(["Type", "Feature"], [
            ["Task-oriented dialogue system", "Helps users complete specific goals like booking a flight"], ["Open-domain chatbot", "Engages in general conversation without a fixed goal"],
        ]),
    },
    "natural-language-processing-c2-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["RAG", "Retrieves relevant documents and uses them to ground a language model's generated response"],
        ]),
    },
    "natural-language-processing-c2-l43": {
        "data_table": table(["Strategy", "Feature"], [
            ["Greedy decoding", "Always picks the highest-probability next token"], ["Beam search", "Tracks multiple candidate sequences to find a better overall result"],
        ]),
    },
    "natural-language-processing-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Language model bias", "Systematic skew in outputs reflecting patterns in training data"],
        ]),
    },
    "natural-language-processing-c2-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Toxicity detection", "Automatically identifies harmful or abusive language in text"],
        ]),
    },
    "natural-language-processing-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Domain adaptation", "Adjusting a model trained on one text domain to perform well on another"],
        ]),
    },
    "natural-language-processing-c2-l47": {
        "data_table": table(["Challenge", "Detail"], [
            ["Low-resource NLP", "Building effective models for languages with little available training data"],
        ]),
    },
    "natural-language-processing-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Cross-lingual transfer", "Applying knowledge learned in one language to tasks in another language"],
        ]),
    },
    "natural-language-processing-c2-l49": {
        "data_table": table(["Component", "Role"], [
            ["Acoustic model", "Maps audio signals to phonemes"], ["Language model", "Constrains recognized text to plausible word sequences"],
        ]),
    },
    "natural-language-processing-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Neural text-to-speech", "Generates natural-sounding speech audio directly from text using neural networks"],
        ]),
    },
    "natural-language-processing-c2-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Knowledge graph", "Represents entities and their relationships as a structured graph, used to ground NLP outputs"],
        ]),
    },
    "natural-language-processing-c2-l52": {
        "data_table": table(["Method", "Feature"], [
            ["Human evaluation", "Judges quality subjectively but captures nuance automatic metrics miss"], ["Automatic metrics", "Fast and scalable but can miss fluency and factuality issues"],
        ]),
    },
    "natural-language-processing-c2-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Few-shot prompting", "Provides a handful of examples within the prompt to guide model behavior"],
        ]),
    },
    "natural-language-processing-c2-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Instruction tuning", "Fine-tunes a model on instruction-response pairs to better follow user commands"],
        ]),
    },
    "natural-language-processing-c2-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["RLHF", "Uses human preference feedback to train a reward model that further tunes the language model"],
        ]),
    },
    "natural-language-processing-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Hallucination", "When a language model generates confident but factually incorrect content"],
        ]),
    },
    "natural-language-processing-c2-l57": {
        "data_table": table(["Technique", "Purpose"], [
            ["Knowledge distillation", "Trains a smaller model to mimic a larger model's behavior"],
        ]),
    },
    "natural-language-processing-c2-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Multimodal NLP", "Jointly processes text alongside other modalities like images"],
        ]),
    },
    "natural-language-processing-c2-l59": {
        "data_table": table(["Technique", "Purpose"], [
            ["Differential privacy", "Adds calibrated noise to protect individual data while preserving aggregate patterns"],
        ]),
    },
    "natural-language-processing-c2-l60": {
        "data_table": table(["Technique", "Purpose"], [
            ["Attention visualization", "Shows which input tokens a transformer model focused on for a given output"],
        ]),
    },
    "natural-language-processing-c2-l61": {
        "data_table": table(["Order", "Feature"], [
            ["Bigram model", "Considers the previous one word"], ["Trigram model", "Considers the previous two words"],
        ]),
    },
    "natural-language-processing-c2-l62": {
        "data_table": table(["Rule Type", "Example"], [
            ["Terminal rule", "NP -> \"dog\""], ["Non-terminal rule", "S -> NP VP"],
        ]),
    },
    "natural-language-processing-c2-l63": {
        "data_table": table(["Parameter", "Effect"], [
            ["Number of topics (k)", "Controls how many latent topics LDA discovers"],
        ]),
    },
    "natural-language-processing-c2-l64": {
        "data_table": table(["Step", "Purpose"], [
            ["Singular value decomposition", "Reduces the document-term matrix to capture latent semantic structure"],
        ]),
    },
    "natural-language-processing-c2-l65": {
        "data_table": table(["Approach", "Feature"], [
            ["Knowledge-based WSD", "Uses dictionary definitions to disambiguate word senses"],
        ]),
    },
    "natural-language-processing-c2-l66": {
        "data_table": table(["Role", "Example"], [
            ["Agent", "The doer of an action"], ["Patient", "The entity affected by an action"],
        ]),
    },
    "natural-language-processing-c2-l67": {
        "data_table": table(["Strategy", "Feature"], [
            ["Full fine-tuning", "Updates all model parameters"], ["Parameter-efficient fine-tuning (LoRA)", "Updates a small subset of added parameters"],
        ]),
    },
    "natural-language-processing-c2-l68": {
        "data_table": table(["Relation", "Example"], [
            ["Subject dependency", "'dog' as the subject of 'barks' in 'The dog barks'"],
        ]),
    },
    "natural-language-processing-c2-l69": {
        "data_table": table(["Phrase Type", "Example"], [
            ["Noun phrase", "'the small dog'"], ["Verb phrase", "'is barking loudly'"],
        ]),
    },
    "natural-language-processing-c2-l70": {
        "data_table": table(["Step", "Purpose"], [
            ["Retrieving relevant passages", "Narrows the search space before extracting an answer"],
        ]),
    },
    "natural-language-processing-c2-l71": {
        "data_table": table(["Type", "Feature"], [
            ["Extractive QA", "Answers by selecting a span directly from the passage"], ["Abstractive QA", "Generates a novel answer in its own words"],
        ]),
    },
    "natural-language-processing-c2-l72": {
        "data_table": table(["Step", "Purpose"], [
            ["Chunking documents", "Splits long documents into retrievable segments for a RAG pipeline"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Natural Language Processing"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Natural Language Processing: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 NLP lessons (completing 72/72).")


if __name__ == "__main__":
    main()
