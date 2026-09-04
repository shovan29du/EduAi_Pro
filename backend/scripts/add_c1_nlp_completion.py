#!/usr/bin/env python3
"""Depth pass, C1 Natural Language Processing: fill in real,
hand-checked data_table content for the 69 C1 NLP lessons not covered
by the earlier breadth-first batch. Brings C1 NLP to full 70/70
coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_nlp_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "natural-language-processing-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["NLP", "Natural Language Processing, enables computers to understand human language"],
        ]),
    },
    "natural-language-processing-c1-l2": {
        "data_table": table(["Step", "Purpose"], [
            ["Tokenization", "Splits text into words or sentences"], ["Lowercasing", "Standardizes text case"],
        ]),
    },
    "natural-language-processing-c1-l4": {
        "data_table": table(["Technique", "Effect"], [
            ["Stemming", "Crudely chops words to a root form, e.g. 'running' to 'run'"], ["Lemmatization", "Reduces words to their dictionary base form using grammar"],
        ]),
    },
    "natural-language-processing-c1-l5": {
        "data_table": table(["Pattern", "Matches"], [
            ["\\d+", "One or more digits"], ["\\w+", "One or more word characters"],
        ]),
    },
    "natural-language-processing-c1-l6": {
        "data_table": table(["Method", "Approach"], [
            ["Edit distance", "Finds the closest correctly spelled word by minimal changes"],
        ]),
    },
    "natural-language-processing-c1-l7": {
        "data_table": table(["Method", "Approach"], [
            ["N-gram frequency analysis", "Identifies a language based on common character patterns"],
        ]),
    },
    "natural-language-processing-c1-l8": {
        "data_table": table(["Measure", "Meaning"], [
            ["Cosine similarity", "Measures the angle between two text vectors"],
        ]),
    },
    "natural-language-processing-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Edit distance", "The minimum number of edits needed to change one string into another"],
        ]),
    },
    "natural-language-processing-c1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["TF-IDF", "Weights words by frequency in a document versus rarity across all documents"],
        ]),
    },
    "natural-language-processing-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Bag-of-words", "Represents text as word frequency counts, ignoring order"],
        ]),
    },
    "natural-language-processing-c1-l12": {
        "data_table": table(["Tag", "Example"], [
            ["Noun", "'dog'"], ["Verb", "'runs'"], ["Adjective", "'happy'"],
        ]),
    },
    "natural-language-processing-c1-l13": {
        "data_table": table(["Entity Type", "Example"], [
            ["Person", "'Marie Curie'"], ["Location", "'Paris'"], ["Organization", "'United Nations'"],
        ]),
    },
    "natural-language-processing-c1-l14": {
        "data_table": table(["Task", "Example"], [
            ["Text classification", "Categorizing an email as spam or not spam"],
        ]),
    },
    "natural-language-processing-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Naive Bayes for text", "Classifies text using word probabilities, assuming word independence"],
        ]),
    },
    "natural-language-processing-c1-l16": {
        "data_table": table(["Approach", "Method"], [
            ["Lexicon-based sentiment", "Scores text using a dictionary of words with known sentiment"],
        ]),
    },
    "natural-language-processing-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Keyphrase extraction", "Automatically identifying the most important phrases in a document"],
        ]),
    },
    "natural-language-processing-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Text segmentation", "Dividing text into meaningful units like sentences or topics"],
        ]),
    },
    "natural-language-processing-c1-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Document clustering", "Grouping similar documents together without predefined labels"],
        ]),
    },
    "natural-language-processing-c1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Query understanding", "Interpreting the intent behind a search query"],
        ]),
    },
    "natural-language-processing-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Corpus", "A large structured collection of text used for NLP research and training"],
        ]),
    },
    "natural-language-processing-c1-l22": {
        "data_table": table(["Step", "Purpose"], [
            ["Removing punctuation", "Simplifies text for consistent processing"],
        ]),
    },
    "natural-language-processing-c1-l23": {
        "data_table": table(["Task", "Challenge"], [
            ["Sentence segmentation", "Deciding where sentences end, e.g. handling abbreviations"],
        ]),
    },
    "natural-language-processing-c1-l24": {
        "data_table": table(["Approach", "Example"], [
            ["Whitespace tokenization", "Splits text by spaces"], ["Subword tokenization", "Splits into common word pieces"],
        ]),
    },
    "natural-language-processing-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Stop words", "Common words like 'the' and 'is' often removed before analysis"],
        ]),
    },
    "natural-language-processing-c1-l26": {
        "data_table": table(["Term", "Example"], [
            ["Bigram", "A pair of consecutive words, e.g. 'machine learning'"],
        ]),
    },
    "natural-language-processing-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Text vectorization", "Converting text into numerical vectors for machine learning"],
        ]),
    },
    "natural-language-processing-c1-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["One-hot encoding", "Represents each word as a vector with a single 1 and the rest 0s"],
        ]),
    },
    "natural-language-processing-c1-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Word embedding", "Represents words as dense vectors capturing semantic meaning"],
        ]),
    },
    "natural-language-processing-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Word2Vec", "A method for learning word embeddings from context in large text corpora"],
        ]),
    },
    "natural-language-processing-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["GloVe", "Word embeddings learned from global word co-occurrence statistics"],
        ]),
    },
    "natural-language-processing-c1-l32": {
        "data_table": table(["Step", "Purpose"], [
            ["Preprocessing", "Cleans and tokenizes text"], ["Vectorization", "Converts text into numbers"], ["Classification", "Predicts a category"],
        ]),
    },
    "natural-language-processing-c1-l33": {
        "data_table": table(["Feature", "Signal"], [
            ["Excessive capitalization", "Common indicator of spam"],
        ]),
    },
    "natural-language-processing-c1-l34": {
        "data_table": table(["Approach", "Method"], [
            ["Lexicon-based", "Uses a dictionary of sentiment-scored words"], ["Machine learning-based", "Trains a classifier on labeled sentiment data"],
        ]),
    },
    "natural-language-processing-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Information extraction", "Automatically pulling structured facts from unstructured text"],
        ]),
    },
    "natural-language-processing-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Text summarization", "Automatically condensing a document into its key points"],
        ]),
    },
    "natural-language-processing-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Extractive summarization", "Selects existing sentences from the source text"],
        ]),
    },
    "natural-language-processing-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Abstractive summarization", "Generates new sentences that paraphrase the source text"],
        ]),
    },
    "natural-language-processing-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Semantic search", "Retrieves results based on meaning, not just keyword matching"],
        ]),
    },
    "natural-language-processing-c1-l40": {
        "data_table": table(["Component", "Purpose"], [
            ["Intent recognition", "Identifies what the user wants"],
        ]),
    },
    "natural-language-processing-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Rule-based NLP", "Uses hand-crafted linguistic rules instead of statistical learning"],
        ]),
    },
    "natural-language-processing-c1-l42": {
        "data_table": table(["Pattern", "Use"], [
            ["^[A-Z]", "Matches text starting with a capital letter"],
        ]),
    },
    "natural-language-processing-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Text annotation", "Manually labeling text data to train supervised models"],
        ]),
    },
    "natural-language-processing-c1-l44": {
        "data_table": table(["Metric", "Use"], [
            ["BLEU score", "Evaluates machine translation quality"], ["F1 score", "Balances precision and recall"],
        ]),
    },
    "natural-language-processing-c1-l45": {
        "data_table": table(["Challenge", "Example"], [
            ["Limited training data", "Many languages lack large labeled datasets"],
        ]),
    },
    "natural-language-processing-c1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Machine translation", "Automatically translating text from one language to another"],
        ]),
    },
    "natural-language-processing-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Rule-based MT", "Uses hand-crafted grammar and dictionary rules to translate"],
        ]),
    },
    "natural-language-processing-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Statistical MT", "Learns translation patterns from large bilingual text corpora"],
        ]),
    },
    "natural-language-processing-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Speech-to-text", "Converts spoken audio into written text"],
        ]),
    },
    "natural-language-processing-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Text-to-speech", "Converts written text into spoken audio"],
        ]),
    },
    "natural-language-processing-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["OCR", "Optical Character Recognition, converts images of text into machine-readable text"],
        ]),
    },
    "natural-language-processing-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Question answering system", "Automatically finds or generates answers to natural language questions"],
        ]),
    },
    "natural-language-processing-c1-l53": {
        "data_table": table(["Application", "Example"], [
            ["Text mining social media", "Analyzing public sentiment trends from posts"],
        ]),
    },
    "natural-language-processing-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Word frequency analysis", "Counting how often each word appears in a text"],
        ]),
    },
    "natural-language-processing-c1-l55": {
        "data_table": table(["Metric", "Use"], [
            ["Flesch-Kincaid score", "Estimates how difficult a text is to read"],
        ]),
    },
    "natural-language-processing-c1-l56": {
        "data_table": table(["Tool", "Purpose"], [
            ["Language detection library", "Automatically identifies which language a text is written in"],
        ]),
    },
    "natural-language-processing-c1-l57": {
        "data_table": table(["Category", "Example"], [
            ["PERSON", "'Albert Einstein'"], ["GPE (location)", "'Tokyo'"], ["DATE", "'January 2020'"],
        ]),
    },
    "natural-language-processing-c1-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Coreference resolution", "Determining which words refer to the same entity, e.g. a pronoun and its noun"],
        ]),
    },
    "natural-language-processing-c1-l59": {
        "data_table": table(["Step", "Order"], [
            ["Tokenize, then remove stop words, then stem/lemmatize", "A typical preprocessing pipeline order"],
        ]),
    },
    "natural-language-processing-c1-l60": {
        "data_table": table(["Concern", "Example"], [
            ["Bias in training data", "Can cause NLP models to produce unfair or skewed outputs"],
        ]),
    },
    "natural-language-processing-c1-l61": {
        "data_table": table(["Pattern", "Purpose"], [
            ["[a-zA-Z]+", "Matches sequences of letters, useful for extracting words"],
        ]),
    },
    "natural-language-processing-c1-l62": {
        "data_table": table(["Component", "Meaning"], [
            ["Term frequency", "How often a word appears in a document"], ["Inverse document frequency", "How rare a word is across all documents"],
        ]),
    },
    "natural-language-processing-c1-l63": {
        "data_table": table(["Method", "Use"], [
            ["Topic-based segmentation", "Splits text where the subject matter shifts"],
        ]),
    },
    "natural-language-processing-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Identifying an NLP task", "Classifying a project as translation, summarization, or classification"],
        ]),
    },
    "natural-language-processing-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Cleaning raw text", "Removing HTML tags and special characters from scraped text"],
        ]),
    },
    "natural-language-processing-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Comparing normalization methods", "Applying lowercase and punctuation removal to a sample paragraph"],
        ]),
    },
    "natural-language-processing-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Comparing stemming and lemmatization", "Processing the word 'better' with each technique"],
        ]),
    },
    "natural-language-processing-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Writing a regex", "Extracting all email addresses from a sample text"],
        ]),
    },
    "natural-language-processing-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Correcting a misspelling", "Using edit distance to find the closest valid word"],
        ]),
    },
    "natural-language-processing-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Detecting a language", "Identifying the language of a short sample text"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Natural Language Processing"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Natural Language Processing: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Natural Language Processing lessons (completing 70/70).")


if __name__ == "__main__":
    main()
