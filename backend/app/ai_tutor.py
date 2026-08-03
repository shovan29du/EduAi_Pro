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


def explain_chess_position(
    fen: str, move_history: list[str] | None = None, level: str | None = None, grade: int = 1,
) -> str:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = f"""You are a friendly chess coach explaining a position to a student at {info['label']}.
Describe the position in plain language: material balance, piece activity, king safety, and any
tactical or strategic ideas available for the side to move. Keep it encouraging and educational,
suitable for someone still learning chess."""
    history_text = " ".join(move_history or []) or "(start of game)"
    user = f"Move history so far: {history_text}\nCurrent position (FEN): {fen}\nExplain this position."
    return _call(system, user, max_tokens=500, strict=strict)


def answer_chess_question(
    fen: str, question: str, move_history: list[str] | None = None, level: str | None = None, grade: int = 1,
) -> str:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = f"""You are a friendly chess coach helping a student at {info['label']} understand a specific
chess position. Answer the student's question about the position clearly, referring to actual pieces
and squares where it helps."""
    history_text = " ".join(move_history or []) or "(start of game)"
    user = f"Move history so far: {history_text}\nCurrent position (FEN): {fen}\n\nQuestion: {question}"
    return _call(system, user, max_tokens=400, strict=strict)


def make_study_plan(subject: str, grade: int = 1, days: int = 7, level: str | None = None) -> str:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = _STUDY_PLAN_TEMPLATE.format(level_label=info["label"], subject=subject, days=days)
    return _call(
        system, f"Create a {days}-day study plan for {subject} at {info['label']}.", max_tokens=600, strict=strict
    )


def _parse_study_questions_response(raw: str) -> list[dict]:
    questions = []
    blocks = re.split(r"\n(?=TYPE:)", raw.strip())
    for block in blocks:
        type_m = re.search(r"TYPE:\s*(MCQ|OPEN)", block)
        q_m = re.search(r"Q:\s*(.+)", block)
        if not type_m or not q_m:
            continue
        qtype = type_m.group(1).strip()
        if qtype == "MCQ":
            opts = re.findall(r"([A-D])\)\s*(.+)", block)
            ans_m = re.search(r"ANSWER:\s*([A-D])", block)
            exp_m = re.search(r"EXPLANATION:\s*(.+)", block)
            if len(opts) >= 2 and ans_m:
                questions.append({
                    "type": "mcq",
                    "question": q_m.group(1).strip(),
                    "options": {o[0]: o[1].strip() for o in opts},
                    "answer": ans_m.group(1).strip(),
                    "explanation": exp_m.group(1).strip() if exp_m else "",
                })
        else:
            points_m = re.search(r"KEY_POINTS:\s*(.+)", block)
            exp_m = re.search(r"EXPLANATION:\s*(.+)", block)
            key_points = [p.strip() for p in (points_m.group(1).split(";") if points_m else []) if p.strip()]
            questions.append({
                "type": "open",
                "question": q_m.group(1).strip(),
                "key_points": key_points,
                "explanation": exp_m.group(1).strip() if exp_m else "",
            })
    return questions


def generate_study_questions(
    topic: str, subject: str = "", grade: int = 1, level: str | None = None, count: int = 6, mode: str = "mixed",
) -> list[dict]:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    mode_instruction = {
        "mcq": "all multiple-choice",
        "dissertative": "all open-ended short-answer",
        "mixed": "a mix of multiple-choice and open-ended short-answer",
    }.get(mode, "a mix of multiple-choice and open-ended short-answer")
    system = f"""You create study questions for spaced-repetition practice, for a student at {info['label']}
studying {subject or topic}. Generate exactly {count} questions, {mode_instruction}, testing real understanding
(not just recall) of {topic}. Format each multiple-choice question exactly as:
TYPE: MCQ
Q: [question]
A) [option]
B) [option]
C) [option]
D) [option]
ANSWER: [A/B/C/D]
EXPLANATION: [one sentence]

Format each open-ended question exactly as:
TYPE: OPEN
Q: [question]
KEY_POINTS: [point one; point two; point three]
EXPLANATION: [one-sentence model answer summary]
"""
    raw = _call(system, f"Topic: {topic}", max_tokens=1500, strict=strict)
    return _parse_study_questions_response(raw)


def _parse_graded_answer_response(raw: str) -> dict:
    score_m = re.search(r"SCORE:\s*(\d+)", raw)
    feedback_m = re.search(r"FEEDBACK:\s*(.+)", raw, re.S)
    score = int(score_m.group(1)) if score_m else 0
    score = max(0, min(score, 100))
    feedback = feedback_m.group(1).strip() if feedback_m else raw.strip()
    return {"score": score, "feedback": feedback}


def grade_open_answer(
    question: str, key_points: list[str], given_answer: str, level: str | None = None, grade: int = 1,
) -> dict:
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    points_text = "; ".join(key_points) or "(no specific key points given -- judge on general correctness)"
    system = f"""You are grading a student's answer at {info['label']}. Be encouraging but honest.
Compare the student's answer to the expected key points and award a score from 0 to 100 reflecting how
completely and correctly they answered. Format your reply exactly as:
SCORE: [0-100]
FEEDBACK: [two or three encouraging, specific sentences on what was right and what to improve]
"""
    user = f"Question: {question}\nExpected key points: {points_text}\nStudent's answer: {given_answer}"
    raw = _call(system, user, max_tokens=300, strict=strict)
    return _parse_graded_answer_response(raw)


_COURSE_ASSISTANT_EXCERPT_CHARS_PER_DOC = 6000


def answer_from_course_materials(
    question: str, documents: list[dict], level: str | None = None, grade: int = 1,
) -> str:
    """Answer a question grounded strictly in the given course materials
    (each a {"filename": str, "text": str} dict), refusing to use outside
    knowledge -- mirrors a closed-book course assistant rather than a
    general tutor."""
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    system = f"""You are a course assistant for a student at {info['label']}. You must answer the student's
question using ONLY the course materials provided below -- do not use outside knowledge, even if you know
the answer. If the materials do not contain the answer, say clearly that it isn't covered in the provided
materials instead of guessing. When you do answer, mention which document(s) (by filename) the answer came
from."""
    materials_block = "\n\n".join(
        f"=== {doc['filename']} ===\n{doc['text'][:_COURSE_ASSISTANT_EXCERPT_CHARS_PER_DOC]}"
        for doc in documents
    )
    user = f"Course materials:\n\n{materials_block}\n\nQuestion: {question}"
    return _call(system, user, max_tokens=600, strict=strict)


_RESUME_FORMAT_INSTRUCTIONS = """Respond in exactly this format, with no extra commentary before or after:
SUMMARY: [2-3 sentence professional summary tailored to the target role]
SKILLS: [comma-separated list, reusing and lightly polishing the candidate's own skills]
EXPERIENCE:
- [first achievement bullet: action-led and quantified wherever the candidate's notes support it]
- [second achievement bullet]
(write exactly one bullet per experience/portfolio note given, in the same order, and do not omit any)"""


def _parse_resume_content(raw: str, fallback_skills: list[str], fallback_experience: list[str]) -> dict:
    summary_m = re.search(r"SUMMARY:\s*(.+)", raw)
    skills_m = re.search(r"SKILLS:\s*(.+)", raw)
    experience_m = re.search(r"EXPERIENCE:\s*(.+)", raw, re.S)

    summary = summary_m.group(1).strip() if summary_m else raw.strip()[:400]
    skills = (
        [s.strip() for s in skills_m.group(1).split(",") if s.strip()] if skills_m else list(fallback_skills)
    )
    bullets = []
    if experience_m:
        bullets = [
            line.strip()[1:].strip()
            for line in experience_m.group(1).splitlines()
            if line.strip().startswith("-")
        ]
    if not bullets:
        bullets = list(fallback_experience)

    return {"summary": summary, "skills": skills, "experience": bullets}


def generate_resume_content(profile: dict) -> dict:
    """Turn a candidate's raw notes (skills, experience/portfolio bullets, target role and
    job description) into a polished, ATS-friendly resume draft: a professional summary,
    a refined skills list, and quantified achievement bullets -- one per input note."""
    name = str(profile.get("name") or "the candidate")
    target_role = str(profile.get("target_role") or "")
    job_description = str(profile.get("job_description") or "")
    skills = list(profile.get("skills") or [])
    experience = list(profile.get("experience") or [])
    education = str(profile.get("education") or "")

    system = (
        "You are an expert professional resume writer. Rewrite the candidate's raw notes into a "
        "polished, ATS-friendly, quantified resume draft. Never invent employers, dates, numbers, or "
        "achievements the candidate did not mention -- only sharpen phrasing and structure.\n"
        + _RESUME_FORMAT_INSTRUCTIONS
    )
    lines = [f"Candidate: {name}", f"Target role: {target_role or 'not specified'}"]
    if job_description:
        lines.append(f"Target job description:\n{job_description}")
    if skills:
        lines.append(f"Raw skills: {', '.join(skills)}")
    if experience:
        lines.append("Raw experience/portfolio notes (one bullet per note, same order):")
        lines.extend(f"- {item}" for item in experience)
    if education:
        lines.append(f"Education: {education}")
    user = "\n".join(lines)

    raw = _call(system, user, max_tokens=800, strict=False)
    return _parse_resume_content(raw, fallback_skills=skills, fallback_experience=experience)


_ARK_AI_SYSTEM = """You are Ark AI, a general-purpose personal assistant available from every page of this
app -- distinct from the subject-bound AI Tutor. You support two modes:

Chat mode: friendly, direct, general-purpose conversation, brainstorming, writing help, and everyday Q&A,
not necessarily tied to schoolwork.

Learn mode: tutoring-oriented. Explain clearly, check understanding, and calibrate to a learner at
{level_label} unless the user's message clearly implies a different audience.

Rules:
{safety_rules}
- Keep answers focused and under 300 words unless the user clearly wants something longer.
- If a request needs live web search, real-time data, image generation, or code execution, say plainly
  that Ark AI can't do that here yet, rather than pretending to."""


def ark_ai_chat(
    message: str, history: list[dict] | None = None, mode: str = "chat",
    level: str | None = None, grade: int = 1,
) -> str:
    """A general-purpose assistant available on every page (not bound to a
    specific subject/lesson) -- inspired by the Ark_Ai multi-model chat
    workspace, reimplemented on this app's existing Claude backend instead of
    Ark_Ai's own multi-provider/OpenRouter routing, which this app has no
    infrastructure for."""
    info = _resolve_level(level, grade)
    strict = info["category"] == levels_module.SCHOOL_CATEGORY
    safety_key = levels_module.SCHOOL_CATEGORY if strict else "adult"
    system = _ARK_AI_SYSTEM.format(level_label=info["label"], safety_rules=_SAFETY_RULES_BY_CATEGORY[safety_key])
    mode_note = "Mode: Learn (tutoring-oriented)." if mode == "learn" else "Mode: Chat (general-purpose)."

    turns = []
    for turn in (history or [])[-6:]:
        role = "Assistant" if turn.get("role") == "assistant" else "User"
        text = str(turn.get("content", ""))[:800]
        if text:
            turns.append(f"{role}: {text}")
    transcript = "\n".join(turns)

    user = f"{mode_note}\n"
    if transcript:
        user += f"Conversation so far:\n{transcript}\n\n"
    user += f"User: {message}"

    return _call(system, user, max_tokens=600, strict=strict)
