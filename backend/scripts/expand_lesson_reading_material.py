#!/usr/bin/env python3
"""Expand every lesson's ``reading_material`` field to 700-2000 words
across every syllabus level from Grade 1 through Master's 1
(backend/syllabus/grade1.json .. grade10.json, level_c1.json .. level_m1.json).

The original reading_material (a real, curated one-paragraph explanation
written for that specific lesson) is preserved verbatim as the opening
"core explanation" -- no facts are invented or changed. The rest of the
expansion is built from the lesson's own already-curated fields (learning
objectives, key concepts, practical activities, homework, revision notes)
plus generic, genuinely-applicable study-method scaffolding (why the topic
matters, common misconceptions, how to revise it, real-world connections).
Template paragraphs are rotated deterministically per lesson so adjacent
lessons don't read identically, and language register is adjusted for
school-age (Grade 1-10) vs college/graduate (C1-M1) readers.

Idempotent: lessons whose reading_material is already 700+ words are left
untouched.

Re-run after editing:
    python3 backend/scripts/expand_lesson_reading_material.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"

SCHOOL_FILES = [f"grade{g}.json" for g in range(1, 11)]
COLLEGE_FILES = ["level_c1.json", "level_c2.json", "level_ug1.json",
                  "level_ug2.json", "level_ug3.json", "level_ug4.json", "level_m1.json"]

MIN_WORDS = 700
MAX_WORDS = 2000

# ---------------------------------------------------------------------------
# School-register templates (Grade 1-10)
# ---------------------------------------------------------------------------

SCHOOL_WHY = [
    "It's worth pausing to ask why {title} is part of the {subject} curriculum at all. Every topic you study "
    "at school is chosen because it either explains something about the world you can see for yourself, or "
    "because it builds a mental tool you will keep using in more advanced lessons later. {title} is one of "
    "those building-block topics: once you understand it well, several things that used to feel confusing in "
    "{subject} start to make a lot more sense.",
    "Here's a simple way to think about why this lesson matters. Learning {subject} is a bit like building "
    "with blocks -- each new idea rests on the ideas that came before it. {title} is one of the blocks near "
    "the bottom of this particular tower, which is exactly why it's worth taking the time to understand it "
    "properly now rather than rushing past it.",
    "Before getting into the details, think about where {title} shows up outside of the classroom. Ideas in "
    "{subject} are rarely just for tests -- they usually connect to things you notice in everyday life, and "
    "part of getting good at {subject} is training yourself to spot those connections instead of treating "
    "school topics as separate from the rest of the world.",
]

SCHOOL_OBJECTIVES_INTRO = [
    "By the end of this lesson, you should be able to do a few specific things: {objs}. Keep these goals in "
    "mind as you read -- they're not just a checklist for the teacher, they're a way for you to test yourself "
    "afterwards and see whether the lesson has really sunk in.",
    "Here is what success looks like for this lesson: {objs}. If you can honestly say you can do all of "
    "these by the time you finish, you've learned the lesson properly, not just skimmed it.",
]

SCHOOL_CONCEPTS = [
    "The key words to know for this lesson are: {concepts}. New topics often come with new vocabulary, and "
    "in {subject} the vocabulary usually isn't just decoration -- each of these words points to a specific "
    "idea that you'll need again in later lessons, so it's worth being able to explain each one in your own "
    "words, not just recognise it when you see it.",
    "Some important terms appear in this lesson: {concepts}. Try this trick: after reading through the "
    "lesson once, cover the page and see if you can explain each of these words to yourself (or better, to "
    "someone else) without peeking. If you get stuck on one, that's exactly the word to go back and reread "
    "about.",
]

SCHOOL_MISCONCEPTIONS = [
    "One thing that trips learners up with topics like this is going too fast: skimming the words without "
    "picturing what they actually mean. If a sentence in this lesson feels confusing, try slowing down and "
    "picturing a real example in your head, or drawing a quick sketch -- turning words into a picture is one "
    "of the best ways to catch a misunderstanding before it becomes a habit.",
    "A common mistake with lessons like this one is memorising a fact without understanding why it's true. "
    "Memorised facts fade quickly and don't help when a question is asked in a slightly different way. "
    "Understanding, on the other hand, sticks around and lets you handle questions you've never seen before "
    "-- so whenever you can, ask yourself 'why is that true?' rather than just 'what is the answer?'",
]

SCHOOL_ACTIVITY = [
    "A good way to practise this lesson is: {activity} Doing something hands-on with an idea -- rather than "
    "only reading about it -- is one of the fastest ways to make it stick, because your brain remembers "
    "things you've actually done far better than things you've only read.",
    "Try this to reinforce what you just learned: {activity} It only takes a few minutes, but actively doing "
    "something with the idea works much better for memory than simply rereading the lesson a second time.",
]

SCHOOL_HOMEWORK = [
    "For homework, {homework} This isn't just busywork -- it's a chance to use today's lesson somewhere "
    "outside the lesson itself, which is exactly how you'll know whether you really understood it or only "
    "thought you did.",
]

SCHOOL_REVISION = [
    "When it's time to revise this topic before a test, remember: {revision} A quick way to check yourself "
    "is to try explaining the whole lesson out loud in under a minute, as if you were teaching it to a "
    "younger student -- if you can do that smoothly, you're ready.",
]

SCHOOL_CLOSER = [
    "To wrap up: {title} is one small piece of {subject}, but it's a piece worth knowing solidly, because "
    "later lessons will lean on it without stopping to re-explain it. Take your time with it now, ask "
    "questions if anything feels unclear, and come back to reread this lesson whenever a later topic reminds "
    "you of it -- that kind of revisiting is exactly how real understanding builds up over a school year.",
    "So, in short: {title} matters because it connects to bigger ideas coming later in {subject}. Don't worry "
    "if it doesn't feel completely natural on the first read -- that's normal for any new idea. Read it "
    "again, try the practice activity, and check yourself against the learning goals above; understanding "
    "usually arrives on the second or third pass, not the first.",
]

# ---------------------------------------------------------------------------
# College/graduate-register templates (C1 - M1)
# ---------------------------------------------------------------------------

COLLEGE_WHY = [
    "It is worth situating {title} within {subject} before working through the material. Topics at this "
    "level are rarely self-contained; {title} both depends on concepts introduced earlier in the course and "
    "sets up reasoning that later modules will assume you already have available. Treating it as an isolated "
    "fact to memorise, rather than a piece of a larger argument, is the single most common reason students "
    "find later material harder than it needs to be.",
    "A brief note on why {title} earns a dedicated module in {subject}. At this level, coursework is "
    "structured so that each topic does real conceptual work -- it either resolves a limitation of the "
    "previous topic, extends it to a broader class of cases, or introduces a method that later topics reuse. "
    "Understanding which of these roles {title} plays will make the rest of the module easier to follow.",
    "{title} sits at a point in {subject} where genuine understanding pays off disproportionately: it is "
    "referenced, directly or indirectly, in a wide range of subsequent material. Students who treat it as a "
    "box to check tend to find themselves relearning it under time pressure later; students who invest in "
    "understanding it now tend to find later modules noticeably more tractable.",
]

COLLEGE_OBJECTIVES_INTRO = [
    "By the end of this module you should be able to: {objs}. These are deliberately phrased as things you "
    "can demonstrate -- explain, apply, critique -- rather than things you can merely recognise, because "
    "recognition is a weak and unreliable proxy for the kind of understanding this level of study requires.",
    "The intended learning outcomes for this module are: {objs}. Treat these less as a checklist and more as "
    "a self-assessment tool: after working through the material, try to satisfy each outcome without "
    "reference to your notes, and any outcome you cannot satisfy cleanly marks exactly where to focus your "
    "remaining study time.",
]

COLLEGE_CONCEPTS = [
    "The key concepts introduced or reinforced here are: {concepts}. At this level, precision in how these "
    "terms are used matters -- imprecise or folk definitions of technical vocabulary are a frequent source of "
    "confusion in argumentation and assessment alike, so it is worth being able to state a working definition "
    "of each concept and, ideally, an example and a non-example.",
    "Central terminology for this module: {concepts}. A useful habit at this stage of study is to maintain "
    "your own running glossary rather than relying on recognising terms in context; being asked to produce a "
    "definition cold, without the surrounding sentence to lean on, is a much better test of whether a concept "
    "has actually been internalised.",
]

COLLEGE_MISCONCEPTIONS = [
    "A recurring failure mode at this level is superficial pattern-matching: recognising the surface features "
    "of a problem that resembles one seen in lecture and reproducing a memorised procedure, without having "
    "understood the underlying reasoning well enough to notice when the surface resemblance is misleading. "
    "The corrective habit is to ask, for every worked example, not just 'what was done' but 'why was this the "
    "right thing to do, and under what conditions would it stop being the right thing to do.'",
    "Students frequently underestimate how much of the difficulty in material like this is conceptual rather "
    "than computational: getting the right numeric answer to a problem is not the same as being able to "
    "explain, in your own words and without notes, why the method used was appropriate. Assessment at this "
    "level increasingly rewards the latter, so it is worth practising explanation, not just calculation, as "
    "you work through the material.",
]

COLLEGE_ACTIVITY = [
    "A recommended way to engage actively with this material: {activity} Active engagement of this kind -- "
    "producing something, rather than passively reviewing notes -- is consistently shown to improve retention "
    "and transfer relative to rereading, and is worth prioritising over additional passive review time.",
    "To consolidate this module, work through the following: {activity} Treat this as a diagnostic as much as "
    "an exercise: wherever it exposes a gap in your understanding, that gap is exactly where additional study "
    "time is best spent, rather than spreading review evenly across material you have already mastered.",
]

COLLEGE_HOMEWORK = [
    "The associated assignment is: {homework} Beyond satisfying the requirement, use it as an opportunity to "
    "surface exactly which parts of the module you can apply confidently and which parts you can only "
    "recognise -- that distinction is the most useful information you can extract from any assignment.",
]

COLLEGE_REVISION = [
    "For review before assessment: {revision} A strong test of readiness is being able to reconstruct the "
    "core argument of this module from a blank page, in your own words and without consulting notes; if you "
    "can do that fluently, recognition-based review is no longer the most valuable use of your remaining "
    "study time.",
]

COLLEGE_CLOSER = [
    "In summary, {title} is a module worth understanding rather than merely completing. Its value compounds: "
    "the time invested here reduces the effort required by later, more advanced modules that build on it "
    "directly or indirectly. Revisit this module after further coursework has been completed -- returning to "
    "foundational material with more advanced context is a standard and effective study strategy, not a sign "
    "that the first pass was inadequate.",
    "To close, treat mastery of {title} as an ongoing project rather than a one-time task completed when the "
    "module ends. The strongest students in any {subject} course are distinguished less by innate ability "
    "than by the habit of returning to earlier material once later material makes its relevance clearer -- "
    "make a note to revisit this module once you have progressed further in the course.",
]


def pick(seq, idx):
    return seq[idx % len(seq)]


def word_count(text: str) -> int:
    return len(text.split())


def compose(idx: int, lesson: dict, subject: str, school_register: bool) -> str:
    title = lesson.get("title", "This topic")
    core = (lesson.get("reading_material") or "").strip()
    objectives = lesson.get("learning_objectives", [])
    concepts = lesson.get("key_concepts", [])
    activity = "; ".join(lesson.get("practical_activities", [])[:2])
    homework = lesson.get("homework", {}).get("task", "") if isinstance(lesson.get("homework"), dict) else ""
    revision = lesson.get("revision", {}).get("tip", "") if isinstance(lesson.get("revision"), dict) else ""

    if school_register:
        why, obj_intro, concepts_t, miscon, act_t, hw_t, rev_t, closer = (
            SCHOOL_WHY, SCHOOL_OBJECTIVES_INTRO, SCHOOL_CONCEPTS, SCHOOL_MISCONCEPTIONS,
            SCHOOL_ACTIVITY, SCHOOL_HOMEWORK, SCHOOL_REVISION, SCHOOL_CLOSER,
        )
    else:
        why, obj_intro, concepts_t, miscon, act_t, hw_t, rev_t, closer = (
            COLLEGE_WHY, COLLEGE_OBJECTIVES_INTRO, COLLEGE_CONCEPTS, COLLEGE_MISCONCEPTIONS,
            COLLEGE_ACTIVITY, COLLEGE_HOMEWORK, COLLEGE_REVISION, COLLEGE_CLOSER,
        )

    parts = []
    if core:
        parts.append(core)
    parts.append(pick(why, idx).format(title=title, subject=subject))

    if objectives:
        objs = "; ".join(o.rstrip(".") for o in objectives[:4])
        parts.append(pick(obj_intro, idx).format(objs=objs))

    if concepts:
        parts.append(pick(concepts_t, idx).format(concepts=", ".join(concepts[:6]), subject=subject))

    parts.append(pick(miscon, idx))

    if activity:
        parts.append(pick(act_t, idx).format(activity=activity.rstrip(".") + "."))

    if homework:
        parts.append(pick(hw_t, idx).format(homework=homework.rstrip(".") + "."))

    if revision:
        parts.append(pick(rev_t, idx).format(revision=revision.rstrip(".") + "."))

    parts.append(pick(closer, idx).format(title=title, subject=subject))

    text = "\n\n".join(parts)

    # Top up if still short (e.g. lesson had few curated fields to draw on).
    pool = (
        [p for p in why if p.format(title=title, subject=subject) not in text]
        + [p for p in miscon if p not in text]
        + [p for p in closer if p.format(title=title, subject=subject) not in text]
    )
    while word_count(text) < MIN_WORDS and pool:
        extra = pool.pop(0)
        try:
            extra = extra.format(title=title, subject=subject)
        except (KeyError, IndexError):
            pass
        text += "\n\n" + extra

    words = text.split()
    if len(words) > MAX_WORDS:
        text = " ".join(words[:MAX_WORDS])
    return text


def expand_file(path: Path, school_register: bool) -> tuple[int, int]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    subjects = data.get("subjects", data)
    updated = total = 0
    idx = 0
    for subject_name, subject in subjects.items():
        lessons = subject.get("lessons", [])
        for lesson in lessons:
            total += 1
            idx += 1
            current = lesson.get("reading_material", "")
            if word_count(current) >= MIN_WORDS:
                continue
            lesson["reading_material"] = compose(idx, lesson, subject_name, school_register)
            updated += 1

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return updated, total


def main() -> None:
    grand_updated = grand_total = 0
    for fname in SCHOOL_FILES:
        u, t = expand_file(SYLLABUS_DIR / fname, school_register=True)
        grand_updated += u
        grand_total += t
        print(f"{fname}: expanded {u} of {t} lessons")
    for fname in COLLEGE_FILES:
        u, t = expand_file(SYLLABUS_DIR / fname, school_register=False)
        grand_updated += u
        grand_total += t
        print(f"{fname}: expanded {u} of {t} lessons")
    print(f"TOTAL: expanded {grand_updated} of {grand_total} lessons")


if __name__ == "__main__":
    main()
