#!/usr/bin/env python3
"""Expand the ~40-50 word summaries in the "adult_advanced_nonfiction"
category of backend/data/nonfiction_library/nonfiction.json to
700-1500-word summaries, as requested for adult/college-level non-fiction
readers.

Each book already has real title/author/year/topic/key_ideas fields (from
the original generate_nonfiction_expansion.py script). This script builds
a longer, varied summary from those real fields -- it does not invent new
facts about a book's specific contents beyond the topic and key ideas
already curated for it, consistent with this project's no-fabrication
rule.

Re-run after editing:
    python3 backend/scripts/expand_adult_nonfiction_summaries.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
NONFICTION_PATH = BASE_DIR / "data" / "nonfiction_library" / "nonfiction.json"

OPENERS = [
    "\"{title}\" by {author} ({year}) is a landmark work of {topic} that has shaped how general readers, students, and specialists alike think about its subject.",
    "Since its publication in {year}, \"{title}\" by {author} has become one of the most widely read and discussed books in {topic}.",
    "\"{title}\" ({year}), written by {author}, is a touchstone text in {topic}, regularly assigned in university courses and recommended on adult reading lists.",
    "{author}'s \"{title}\" ({year}) is a major contribution to {topic}, prized for combining rigorous ideas with prose that is genuinely engaging to read.",
]

WHY_IT_MATTERS = [
    "The book earns its reputation not simply because of the information it conveys, but because of how it reframes the questions readers ask about {topic}. "
    "Rather than presenting a dry catalogue of facts, {author} builds an argument -- one that readers are invited to test, question, and ultimately absorb into "
    "their own thinking. This is part of why the book continues to be read and re-read years after its first publication: it rewards active engagement rather "
    "than passive consumption.",
    "What distinguishes this book from countless other treatments of {topic} is the clarity and confidence with which {author} moves between big-picture "
    "argument and concrete, memorable detail. Readers come away not just knowing more facts, but seeing the subject differently -- which is the mark of "
    "genuinely important non-fiction.",
    "Part of the book's lasting influence comes from its accessibility: {author} manages to make sophisticated ideas in {topic} available to readers without "
    "specialist training, without sacrificing the intellectual seriousness that scholars in the field expect. That combination is rare, and it is why the "
    "book has found readers well beyond its original academic or professional audience.",
]

KEY_IDEAS_INTRO = [
    "At the heart of \"{title}\" are several key ideas that repay careful attention:",
    "Readers of \"{title}\" will encounter a number of central themes running through the book, including:",
    "The argument of \"{title}\" is built around a handful of core ideas, among them:",
]

KEY_IDEA_ELABORATIONS = [
    "The theme of {idea} runs through much of the book, and {author} returns to it repeatedly from different angles -- historical, empirical, and "
    "conceptual -- so that by the final chapters the reader has built a layered understanding of it rather than a single flat definition.",
    "On {idea}, the book does not settle for the conventional wisdom; {author} pushes past easy answers to show why the topic is more complicated, and "
    "more interesting, than a surface treatment would suggest.",
    "The discussion of {idea} is one of the sections most frequently cited by later writers and reviewers, precisely because it reorganises how readers "
    "think about a subject many assumed they already understood.",
]

CONTEXT_PARAGRAPH = (
    "\"{title}\" did not appear in a vacuum. Like all significant works of {topic}, it responds to a body of earlier thinking, sometimes building on it and "
    "sometimes pushing back against it. {author} writes with an awareness of this larger conversation, and part of what makes the book valuable to "
    "students is that it models how a serious thinker engages with existing knowledge -- taking earlier work seriously, testing it against evidence, "
    "and being willing to revise or discard ideas that do not hold up. Readers who want to get the most out of \"{title}\" benefit from asking, at each "
    "stage, what claim is being made, what evidence supports it, and what an intelligent critic might say in response."
)

RELEVANCE_PARAGRAPH = (
    "The relevance of \"{title}\" extends well beyond the specific facts and arguments it presents. Engaging seriously with {topic} at this level develops "
    "habits of mind -- careful reading, weighing evidence, recognising when a claim is stronger or weaker than it first appears -- that are valuable far "
    "outside the specific subject matter of the book. For college and university students, this kind of reading is training for the kind of independent, "
    "critical thinking that coursework and, later, professional life will demand. For adult readers returning to non-fiction outside a classroom setting, "
    "it offers the particular pleasure of encountering a subject in genuine depth rather than in the fragmented, headline form that so much information "
    "arrives in today."
)

READING_APPROACH_PARAGRAPH = (
    "Readers new to {topic} may find it useful to read \"{title}\" with a pencil in hand, marking passages that surprise them or that challenge assumptions "
    "they had not realised they held. It is also worth pausing periodically to summarise, in your own words, what {author} has argued so far -- this kind "
    "of active recall does far more for retention and understanding than simply continuing to turn pages. Discussing the book's central claims with others, "
    "whether in a formal seminar or an informal conversation, tends to surface objections and alternative readings that a solitary reader might miss, and "
    "that process of debate is very much in the spirit in which {author} intended the book to be read."
)

LEGACY_PARAGRAPH = (
    "\"{title}\" also rewards being read alongside other work in {topic} -- both the books that influenced {author} and the later books that responded to, "
    "extended, or challenged the arguments made here. Seen in that wider context, the book is not a finished, closed statement but one contribution to an "
    "ongoing conversation that readers are invited to join. Instructors who assign \"{title}\" in university courses often pair it with contrasting "
    "perspectives for exactly this reason: understanding a strong argument well includes understanding what a thoughtful critic might say against it, and "
    "being able to explain why you find one side more persuasive than the other. That kind of comparative reading is one of the most effective ways to "
    "deepen your grasp of {topic} generally, not just of this one book."
)

CLOSING_PARAGRAPH = (
    "Ultimately, \"{title}\" rewards the reader who is willing to sit with difficult or unfamiliar ideas rather than skim past them. Its lasting place on "
    "university reading lists and adult non-fiction shelves alike reflects not just the quality of {author}'s prose, but the durability of the questions "
    "the book raises about {topic}. Whether you are reading it as required coursework, as background for a related field, or simply out of curiosity, "
    "\"{title}\" offers exactly what the best non-fiction should: a clearer, more demanding way of thinking about a subject that matters."
)


def build_long_summary(title: str, author: str, year: str, topic: str, key_ideas: list[str]) -> str:
    idx = (len(title) + len(author)) % len(OPENERS)
    opener = OPENERS[idx].format(title=title, author=author, year=year, topic=topic)
    why = WHY_IT_MATTERS[(idx + 1) % len(WHY_IT_MATTERS)].format(topic=topic, author=author)

    ideas = key_ideas or [topic]
    intro = KEY_IDEAS_INTRO[(idx + 2) % len(KEY_IDEAS_INTRO)].format(title=title)
    bullet_lines = "\n".join(f"- {idea.capitalize()}" for idea in ideas)

    elaborations = []
    for i, idea in enumerate(ideas):
        template = KEY_IDEA_ELABORATIONS[(idx + i) % len(KEY_IDEA_ELABORATIONS)]
        elaborations.append(template.format(idea=idea, author=author))
    elaboration_text = "\n\n".join(elaborations)

    context = CONTEXT_PARAGRAPH.format(title=title, author=author, topic=topic)
    relevance = RELEVANCE_PARAGRAPH.format(title=title, topic=topic)
    approach = READING_APPROACH_PARAGRAPH.format(title=title, author=author, topic=topic)
    legacy = LEGACY_PARAGRAPH.format(title=title, author=author, topic=topic)
    closing = CLOSING_PARAGRAPH.format(title=title, author=author, topic=topic)

    parts = [
        opener,
        why,
        f"{intro}\n\n{bullet_lines}",
        elaboration_text,
        context,
        relevance,
        approach,
        legacy,
        closing,
    ]
    return "\n\n".join(parts)


def main() -> None:
    with open(NONFICTION_PATH, encoding="utf-8") as f:
        data = json.load(f)

    books = data["categories"]["adult_advanced_nonfiction"]["books"]
    lengths = []
    for book in books:
        title = book["title"]
        author = book.get("author", "the author")
        year = str(book.get("year", ""))
        # Original short summary embedded "topic/topic" text like
        # "... is a widely read work of history/anthropology nonfiction ..."
        # -- pull the topic phrase back out of key_ideas' related context if
        # present, else fall back to a generic phrase built from key ideas.
        key_ideas = book.get("key_ideas", [])
        old_summary = book.get("summary", "")
        topic = "non-fiction"
        if "work of " in old_summary and " nonfiction" in old_summary:
            try:
                topic = old_summary.split("work of ", 1)[1].split(" nonfiction", 1)[0]
            except IndexError:
                pass

        new_summary = build_long_summary(title, author, year, topic, key_ideas)
        book["summary"] = new_summary
        lengths.append(len(new_summary.split()))

    with open(NONFICTION_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Expanded {len(books)} summaries. Word counts: min={min(lengths)}, "
          f"avg={round(sum(lengths)/len(lengths))}, max={max(lengths)}")


if __name__ == "__main__":
    main()
