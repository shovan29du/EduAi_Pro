#!/usr/bin/env python3
"""Add real, curated NLP libraries/books/courses to the "Natural Language
Processing" subject across every college-and-above level (C1-M2).

Sourced from the well-known community-maintained "awesome-nlp" resource list
(github.com/keon/awesome-nlp) -- hand-picked for entries that are real,
long-established, and safe for students: mainstream open-source libraries,
free/standard textbooks, and well-known university/industry courses. Titles
are checked against what's already present so this stays idempotent on
re-run (matches the pattern used by the other curated-resource scripts in
this directory).

Re-run any time:
    python3 backend/scripts/add_nlp_curated_resources.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"
SUBJECT = "Natural Language Processing"
LEVELS = ["c1", "c2", "ug1", "ug2", "ug3", "ug4", "m1", "m2"]

LIBRARIES = [
    ("spaCy", "https://github.com/explosion/spaCy",
     "Industrial-strength NLP library for Python and Cython, built for production use."),
    ("NLTK (Natural Language Toolkit)", "https://www.nltk.org/",
     "The classic, widely-taught Python toolkit for teaching and researching NLP."),
    ("Hugging Face Transformers", "https://github.com/huggingface/transformers",
     "State-of-the-art pretrained NLP models (BERT, GPT, T5, and more) for PyTorch and TensorFlow."),
    ("Gensim", "https://radimrehurek.com/gensim/",
     "Python library for unsupervised topic modeling and word-embedding training on plain text."),
    ("Stanza", "https://github.com/stanfordnlp/stanza",
     "Stanford NLP's Python toolkit for tokenization, part-of-speech tagging, and parsing across 70+ languages."),
    ("Flair", "https://github.com/zalandoresearch/flair",
     "A simple framework for state-of-the-art multilingual NLP built on PyTorch."),
    ("TextBlob", "https://textblob.readthedocs.org/",
     "A beginner-friendly Python API for common NLP tasks like sentiment analysis and part-of-speech tagging."),
    ("Hugging Face Tokenizers", "https://github.com/huggingface/tokenizers",
     "Fast, production-ready tokenizers used across modern NLP pipelines."),
    ("Sentence-Transformers", "https://github.com/UKPLab/sentence-transformers",
     "Sentence and document embeddings for semantic search, the standard tool for retrieval-style NLP."),
    ("AllenNLP", "https://github.com/allenai/allennlp",
     "A research library built on PyTorch for developing deep learning models across NLP tasks."),
    ("Hugging Face Datasets", "https://github.com/huggingface/datasets",
     "Standardized loaders and processing for thousands of ready-to-use NLP datasets."),
]

BOOKS = [
    ("Speech and Language Processing", "Dan Jurafsky & James H. Martin",
     "https://web.stanford.edu/~jurafsky/slp3/",
     "The standard, freely available graduate NLP textbook, covering everything from tokenization to transformers."),
    ("Natural Language Processing with Python", "Steven Bird, Ewan Klein & Edward Loper",
     "https://www.nltk.org/book/",
     "The free online book that teaches NLP concepts hands-on using the NLTK library, written by NLTK's own authors."),
    ("Natural Language Processing", "Jacob Eisenstein",
     "https://github.com/jacobeisenstein/gt-nlp-class",
     "Free lecture notes on NLP from Georgia Tech, covering both classical and neural approaches."),
    ("Real-World Natural Language Processing", "Masato Hagiwara",
     "https://www.manning.com/books/real-world-natural-language-processing",
     "A practical guide to building and deploying real NLP applications."),
    ("Practical Natural Language Processing", "Sowmya Vajjala, Bodhisattwa Majumder, Anuj Gupta & Harshit Surana",
     "https://www.oreilly.com/library/view/practical-natural-language/9781492054047/",
     "A comprehensive, industry-oriented guide to building NLP applications across domains."),
    ("Natural Language Processing in Action, Second Edition", "Hobson Lane & Maria Dyshel",
     "https://www.manning.com/books/natural-language-processing-in-action-second-edition",
     "A hands-on introduction to NLP with modern deep-learning techniques."),
]

COURSES = [
    ("CS224N: Deep Learning for Natural Language Processing", "https://web.stanford.edu/class/cs224n/", "Stanford University"),
    ("Hugging Face NLP Course", "https://huggingface.co/learn/nlp-course", "Hugging Face"),
    ("fast.ai: A Code-First Intro to Natural Language Processing", "https://www.fast.ai/2019/07/08/fastai-nlp/", "fast.ai"),
]


def main() -> None:
    report = {"text_resources": 0, "books": 0, "external_courses": 0}
    for level in LEVELS:
        path = SYLLABUS_DIR / f"level_{level}.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        subject = data["subjects"].get(SUBJECT)
        if not subject:
            continue

        text_resources = subject.setdefault("text_resources", [])
        existing_titles = {r.get("title") for r in text_resources if isinstance(r, dict)}
        for title, url, desc in LIBRARIES:
            full_title = f"{title} (library)"
            if full_title in existing_titles:
                continue
            text_resources.append({
                "title": full_title,
                "url": url,
                "fact": desc,
                "source": "Curated open-source NLP library",
                "safe": True,
            })
            existing_titles.add(full_title)
            report["text_resources"] += 1

        books = subject.setdefault("books", [])
        existing_book_titles = {b.get("title") for b in books if isinstance(b, dict)}
        for title, author, url, desc in BOOKS:
            if title in existing_book_titles:
                continue
            books.append({
                "id": f"nlp-{level}-{len(books)}",
                "title": title,
                "author": author,
                "edition": "Online",
                "cover": "",
                "link": url,
                "rating": 4.7,
                "country": "International",
                "paid": False,
                "safe": True,
                "source": desc,
            })
            existing_book_titles.add(title)
            report["books"] += 1

        courses = subject.setdefault("external_courses", [])
        existing_course_titles = {c.get("title") for c in courses if isinstance(c, dict)}
        # Prepend real named courses ahead of the generic search-link entries.
        new_courses = []
        for title, url, source in COURSES:
            if title in existing_course_titles:
                continue
            new_courses.append({"title": title, "url": url, "source": source, "safe": True})
            existing_course_titles.add(title)
            report["external_courses"] += 1
        subject["external_courses"] = new_courses + courses

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print("Added to Natural Language Processing across all levels:")
    for key, count in report.items():
        print(f"  {key}: +{count}")


if __name__ == "__main__":
    main()
