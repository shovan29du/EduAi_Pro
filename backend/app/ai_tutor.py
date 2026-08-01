import os
import re

from .safety import SafetyFilter
from . import levels as levels_module

_sf = SafetyFilter()

_CATEGORY_PERSONA = {
    levels_module.SCHOOL_CATEGORY: (
        "You are EduBot, a warm and encouraging tutor for a school student in {level_label} "
        "(typical ages {age_range}). Use simple, friendly language appropriate for their grade, "
        "plenty of examples and analogies, and keep them curious and motivated."
    ),
    levels_module.COLLEGE_CATEGORY: (
        "You are EduBot, an academic tutor for a college-level student in {level_label} "
        "(typical ages {age_range}), bridging school and university study. Use clear, precise "
        "language, introduce discipline-specific vocabulary, and connect ideas to real-world and "
        "exam-relevant applications."
    ),
    levels_module.UNDERGRADUATE_CATEGORY: (
        "You are EduBot, an academic tutor for an undergraduate student in {level_label} "
        "(typical ages {age_range}) pursuing a bachelor's degree. Use rigorous, discipline-appropriate "
        "language, cite the underlying theory, and give worked examples, derivations, or case studies "
        "as relevant to the subject."
    ),
    levels_module.MASTERS_CATEGORY: (
        "You are EduBot, a graduate-level academic tutor for a master's student in {level_label} "
        "(typical ages {age_range}). Engage at a research-adjacent level: discuss trade-offs, cite "
        "methodologies, reference current practice/literature, and encourage critical, independent "
        "analysis rather than rote answers."
    ),
}

_SAFETY_RULES_BY_CATEGORY = {
    levels_module.SCHOOL_CATEGORY: (
        "- Keep all answers age-appropriate, positive, and educational.\n"
        "- Never discuss graphic violence, sexual content, illegal activity instructions, or anything "
        "inappropriate for a school-age learner.\n"
        "- Use simple language for lower grades; more precise language for higher grades."
    ),
    "adult": (
        "- This learner is a college/university-level or adult learner: mature academic topics "
        "(history of violence and war, politics, human biology and health, economics of alcohol/drugs, "
        "literature with mature themes, philosophy of controversial ideas, etc.) are allowed and expected "
        "when relevant to the subject and level.\n"
        "- Always refuse to give: instructions for making weapons/explosives/dangerous drugs, sexual "
        "content, hate speech, self-harm instructions, or any other genuinely harmful or illegal content.\n"
        "- Treat the learner as a capable adult: be direct, rigorous, and avoid unnecessary hedging or "
        "over-cautious refusals of ordinary academic material."
    ),
}

_COMMON_RULES = (
    "- Encourage curiosity. Use examples, analogies, and real-world connections appropriate to the level.\n"
    "- Keep responses under 250 words unless a detailed explanation is genuinely needed.\n"
    "- Format with bullet points or numbered steps when listing things.\n"
    "- Always end with one encouraging sentence."
)

_LANGUAGE_RULE = "- Respond in {language}, unless the student writes in a different language."
_DIFFICULTY_RULE = "- Calibrate difficulty as '{difficulty}' relative to the normal expectation for this level."


def _resolve_level(level: str | None, grade: int | None) -> dict:
    """Resolve a level id (new levels or legacy numeric grade) to level metadata."""
    candidate = level if level not in (None, "") else grade
    info = levels_module.get_level(candidate) if candidate is not None else None
    if info:
        return info
    # Fall back to a plain school grade for full backward compatibility.
    fallback_grade = grade if grade else 1
    info = levels_module.get_level(fallback_grade)
    return info or levels_module.get_level(1)


def _build_system_prompt(
    level: str | None,
    grade: int | None,
    subject: str,
    age_group: str = "",
    language: str = "",
    difficulty: str = "",
) -> str:
    info = _resolve_level(level, grade)
    persona = _CATEGORY_PERSONA[info["category"]].format(
        level_label=info["label"], age_range=age_group or info["age_range"]
    )
    safety_key = levels_module.SCHOOL_CATEGORY if info["category"] == levels_module.SCHOOL_CATEGORY else "adult"
    rules = [_SAFETY_RULES_BY_CATEGORY[safety_key], _COMMON_RULES]
    if language:
        rules.append(_LANGUAGE_RULE.format(language=language))
    if difficulty:
        rules.append(_DIFFICULTY_RULE.format(difficulty=difficulty))

    return (
        f"{persona}\n"
        f"The student is studying: {subject or 'general topics'}.\n"
        "Rules:\n" + "\n".join(rules)
    )


_FLASHCARD_TEMPLATE = """You are creating educational flashcards for a student at {level_label} studying {subject}.
Generate exactly {count} flashcard pairs as a numbered list.
Format each pair as:
Q: [question]
A: [answer]
Keep questions concise and answers to 1-2 sentences. Calibrate difficulty to {level_label}."""

_STUDY_PLAN_TEMPLATE = """You are a study planner helping a student at {level_label} prepare for {subject}.
They have {days} days to study.
Create a day-by-day study schedule with:
- Daily focus topic
- Estimated time (minutes)
- One key activity
Keep it motivating and achievable, calibrated to {level_label}."""


def _get_client():
    key = os.getenv("ANTHROPIC_API_KEY", "")
    if not key:
        return None
    try:
        import anthropic
        return anthropic.Anthropic(api_key=key)
    except Exception:
        return None


def _call(system: str, user: str, max_tokens: int = 512, strict: bool = True) -> str:
    client = _get_client()
    if not client:
        return "EduBot is offline. Please ask your teacher, tutor, or a trusted adult for help with this question."
    safe_user = _sf.sanitize(user, strict=strict)
    try:
        import anthropic
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": safe_user}],
        )
        return _sf.sanitize(msg.content[0].text, strict=strict)
    except Exception as exc:
        return f"EduBot is temporarily unavailable. ({type(exc).__name__})"


def ask(
    question: str,
    grade: int = 1,
    subject: str = "",
    context: str = "",
    level: str | None = None,
    age_group: str = "",
    language: str = "",
    difficulty: str = "",
) -> str:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = _build_system_prompt(level, grade, subject, age_group, language, difficulty)
    user = question if not context else f"Lesson context:\n{context[:600]}\n\nStudent question:\n{question}"
    return _call(system, user, max_tokens=512, strict=strict)


def explain_concept(
    concept: str,
    grade: int = 1,
    subject: str = "",
    level: str | None = None,
    age_group: str = "",
    language: str = "",
    difficulty: str = "",
) -> str:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = _build_system_prompt(level, grade, subject, age_group, language, difficulty)
    return _call(
        system,
        f"Please explain this concept clearly for a student at {info['label']}: {concept}",
        max_tokens=600,
        strict=strict,
    )


def generate_flashcards(
    topic: str, grade: int = 1, subject: str = "", count: int = 8, level: str | None = None
) -> list[dict]:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = _FLASHCARD_TEMPLATE.format(level_label=info["label"], subject=subject or topic, count=count)
    raw = _call(system, f"Topic: {topic}", max_tokens=800, strict=strict)
    cards = []
    for block in re.split(r"\n(?=\d+\.)", raw.strip()):
        q_match = re.search(r"Q:\s*(.+)", block)
        a_match = re.search(r"A:\s*(.+)", block)
        if q_match and a_match:
            cards.append({"q": q_match.group(1).strip(), "a": a_match.group(1).strip()})
    return cards or [{"q": topic, "a": "Ask your teacher or tutor for more information on this topic."}]


def _parse_quiz_response(raw: str) -> list[dict]:
    questions = []
    blocks = re.split(r"\n(?=Q:)", raw.strip())
    for block in blocks:
        q_m = re.search(r"Q:\s*(.+)", block)
        opts = re.findall(r"([A-D])\)\s*(.+)", block)
        ans_m = re.search(r"Answer:\s*([A-D])", block)
        exp_m = re.search(r"Explanation:\s*(.+)", block)
        if q_m and len(opts) >= 2 and ans_m:
            questions.append({
                "question": q_m.group(1).strip(),
                "options": {o[0]: o[1].strip() for o in opts},
                "answer": ans_m.group(1).strip(),
                "explanation": exp_m.group(1).strip() if exp_m else "",
            })
    return questions


def generate_quiz(
    topic: str, grade: int = 1, subject: str = "", count: int = 5, level: str | None = None
) -> list[dict]:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = f"""You create multiple-choice quiz questions for a student at {info['label']} studying {subject or topic}.
Generate exactly {count} questions. Format each as:
Q: [question]
A) [option]
B) [option]
C) [option]
D) [option]
Answer: [A/B/C/D]
Explanation: [one sentence]
"""
    raw = _call(system, f"Topic: {topic}", max_tokens=1000, strict=strict)
    return _parse_quiz_response(raw)


# ─── Document-grounded helpers (PDF Explainer) ──────────────────────────────
# A student uploads their own document (see app/pdf_explainer.py for the
# upload/text-extraction/storage side); these functions ground the AI tutor's
# explanation, Q&A, and quiz generation in that document's actual text
# instead of a free-standing topic, so answers stay tied to what the
# document actually says.
_DOCUMENT_EXCERPT_CHARS = 12000


def explain_document(
    text: str,
    grade: int = 1,
    subject: str = "",
    level: str | None = None,
    age_group: str = "",
    language: str = "",
    difficulty: str = "",
) -> str:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = _build_system_prompt(level, grade, subject or "this document", age_group, language, difficulty)
    excerpt = text[:_DOCUMENT_EXCERPT_CHARS]
    user = (
        f"A student uploaded a document. Explain its content clearly and simply for a student at "
        f"{info['label']}, organised by section or theme where useful. If the document is long, focus on "
        f"the most important ideas.\n\nDocument text:\n\n{excerpt}"
    )
    return _call(system, user, max_tokens=1200, strict=strict)


def answer_document_question(
    text: str,
    question: str,
    grade: int = 1,
    subject: str = "",
    level: str | None = None,
    age_group: str = "",
    language: str = "",
    difficulty: str = "",
) -> str:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = _build_system_prompt(level, grade, subject or "this document", age_group, language, difficulty)
    excerpt = text[:_DOCUMENT_EXCERPT_CHARS]
    user = (
        f"Document text:\n\n{excerpt}\n\n"
        f"Based only on this document, answer the student's question. If the document does not contain "
        f"the answer, say so rather than guessing.\n\nQuestion: {question}"
    )
    return _call(system, user, max_tokens=500, strict=strict)


def generate_quiz_from_text(
    text: str, grade: int = 1, subject: str = "", count: int = 5, level: str | None = None
) -> list[dict]:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    excerpt = text[:_DOCUMENT_EXCERPT_CHARS]
    system = f"""You create multiple-choice quiz questions strictly based on the document text provided below,
for a student at {info['label']}. Generate exactly {count} questions that test understanding of the
document's actual content -- do not invent facts not present in the text. Format each question as:
Q: [question]
A) [option]
B) [option]
C) [option]
D) [option]
Answer: [A/B/C/D]
Explanation: [one sentence]
"""
    raw = _call(system, f"Document text:\n\n{excerpt}", max_tokens=1200, strict=strict)
    return _parse_quiz_response(raw)


def _parse_lesson_plan_response(raw: str) -> list[dict]:
    lessons = []
    blocks = re.split(r"\n(?=LESSON:)", raw.strip())
    for block in blocks:
        title_m = re.search(r"LESSON:\s*(.+)", block)
        objectives_m = re.search(r"OBJECTIVES:\s*(.+)", block)
        content_m = re.search(r"CONTENT:\s*(.+)", block, re.S)
        if title_m:
            objectives = [o.strip() for o in (objectives_m.group(1).split(";") if objectives_m else []) if o.strip()]
            content = content_m.group(1).strip() if content_m else ""
            lessons.append({
                "title": title_m.group(1).strip(),
                "objectives": objectives,
                "content": content,
            })
    return lessons


def generate_lesson_plan(
    subject: str, term_name: str, lesson_count: int = 10, grade: int = 1,
    level: str | None = None, notes: str = "",
) -> list[dict]:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = f"""You are an experienced curriculum planner helping a teacher plan the term "{term_name}"
for {subject} at {info['label']}. Generate exactly {lesson_count} sequential lessons that build on each
other logically across the term. Format each lesson exactly as:
LESSON: [short lesson title]
OBJECTIVES: [objective one; objective two; objective three]
CONTENT: [a short outline of what the lesson covers, one paragraph]
"""
    user = f"Plan {lesson_count} lessons for {subject} ({term_name}) at {info['label']}."
    if notes.strip():
        user += f" Teacher notes/constraints: {notes.strip()}"
    raw = _call(system, user, max_tokens=1800, strict=strict)
    return _parse_lesson_plan_response(raw)


def _parse_grammar_mistake_response(raw: str) -> dict:
    passage_m = re.search(r"PASSAGE:\s*(.*?)(?=\nMISTAKE:|\Z)", raw.strip(), re.S)
    passage = passage_m.group(1).strip() if passage_m else ""
    mistakes = []
    for m in re.finditer(r"MISTAKE:\s*(.+?)\s*=>\s*(.+?)\s*::\s*(.+)", raw):
        mistakes.append({
            "wrong": m.group(1).strip(),
            "correct": m.group(2).strip(),
            "explanation": m.group(3).strip(),
        })
    return {"passage": passage, "mistakes": mistakes}


def generate_grammar_mistake_exercise(
    topic: str, grade: int = 1, level: str | None = None, language: str = "English", mistake_count: int = 8,
) -> dict:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    mistake_count = max(1, min(int(mistake_count), 20))
    system = f"""You are a {language} grammar teacher creating a "find the mistakes" exercise for a student at
{info['label']}. Write a short, engaging passage (120-200 words) about {topic or 'an interesting everyday topic'}
in {language}, but deliberately insert exactly {mistake_count} grammar, spelling or punctuation mistakes into it.
The mistakes must be realistic errors a learner might make, spread throughout the passage. Format your answer
exactly as:
PASSAGE: [the full passage, containing the {mistake_count} mistakes]
MISTAKE: [incorrect word or phrase exactly as it appears in the passage] => [corrected version] :: [one-sentence explanation of the rule]
(repeat the MISTAKE line once for each mistake, in the order they appear in the passage)
"""
    user = f"Create a grammar mistake-hunting exercise about {topic or 'daily life'} with {mistake_count} mistakes."
    raw = _call(system, user, max_tokens=1000, strict=strict)
    return _parse_grammar_mistake_response(raw)


def make_study_plan(subject: str, grade: int = 1, days: int = 7, level: str | None = None) -> str:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = _STUDY_PLAN_TEMPLATE.format(level_label=info["label"], subject=subject, days=days)
    return _call(
        system, f"Create a {days}-day study plan for {subject} at {info['label']}.", max_tokens=600, strict=strict
    )
