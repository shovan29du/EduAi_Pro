#!/usr/bin/env python3
"""Extend the Assessment Centre with adult age groups, so assessments cover
learners up to age 60 (previously capped at 13-16).

Adds age_groups: "17-25" (young adult / college), "26-40" (adult learner),
and "41-60" (experienced adult learner), each with critical-thinking,
subject-aptitude, and learning-style sections appropriate to adult
self-learners, plus new skill_recommendations entries pointing at the
platform's college/university-level and new subjects (AI, ML, NLP, Data
Science, Business Analytics, Economics, Finance).

Re-run after editing:
    python3 backend/scripts/generate_adult_assessments.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSESSMENT_PATH = BASE_DIR / "data" / "assessment" / "assessments.json"


def learning_style_section(prefix: str) -> dict:
    return {
        "id": "learning_style",
        "title": "Learning Style Preferences",
        "type": "multiple_choice",
        "questions": [
            {
                "id": f"{prefix}_ls1",
                "question": "When learning something new, you prefer to:",
                "options": ["Read detailed material", "Watch a video demonstration", "Try it hands-on immediately", "Discuss it with others"],
                "answer": 2, "skill": "kinesthetic_learning",
            },
            {
                "id": f"{prefix}_ls2",
                "question": "You retain information best when it is:",
                "options": ["Presented as a structured outline", "Shown as a diagram or chart", "Explained through a real story or case study", "Repeated through practice questions"],
                "answer": 3, "skill": "practice_based_learning",
            },
            {
                "id": f"{prefix}_ls3",
                "question": "When studying for a certification or exam, you prefer:",
                "options": ["A fixed daily schedule", "Flexible study whenever you find time", "Group study sessions", "One long intensive session"],
                "answer": 0, "skill": "self_directed_learning",
            },
        ],
    }


AGE_GROUPS = {
    "17-25": {
        "label": "Young Adults (Ages 17–25)",
        "description": "Assessments for college-age and early-career learners covering advanced reasoning, academic aptitude, and career-relevant subject fit.",
        "sections": [
            {
                "id": "advanced_reasoning",
                "title": "Advanced Critical Reasoning",
                "type": "multiple_choice",
                "questions": [
                    {"id": "ya_cr1", "question": "A correlation is found between ice cream sales and drowning deaths. What is the most likely explanation?",
                     "options": ["Ice cream causes drowning", "Drowning causes ice cream sales", "A third factor (hot weather) explains both", "The data must be fake"],
                     "answer": 2, "skill": "confounding_variables"},
                    {"id": "ya_cr2", "question": "Which of these is a logical fallacy known as 'ad hominem'?",
                     "options": ["Attacking the argument's evidence", "Attacking the person instead of their argument", "Providing a counter-example", "Citing a credible source"],
                     "answer": 1, "skill": "logical_fallacies"},
                    {"id": "ya_cr3", "question": "In a well-designed experiment, why is a control group used?",
                     "options": ["To make the study take longer", "To provide a baseline for comparison", "To reduce the sample size needed", "To avoid needing statistics"],
                     "answer": 1, "skill": "experimental_design"},
                    {"id": "ya_cr4", "question": "Which best describes 'confirmation bias'?",
                     "options": ["Seeking out information that confirms existing beliefs", "Always changing your mind", "Only trusting official sources", "Ignoring all evidence"],
                     "answer": 0, "skill": "cognitive_bias"},
                ],
            },
            {
                "id": "career_subject_aptitude",
                "title": "Career & Subject Aptitude",
                "type": "multiple_choice",
                "questions": [
                    {"id": "ya_sa1", "question": "Which task would you find most engaging?",
                     "options": ["Analyzing a dataset to find patterns", "Writing an essay analyzing a novel", "Designing a marketing campaign", "Building and testing a small program"],
                     "answer": 0, "skill": "data_analysis_aptitude"},
                    {"id": "ya_sa2", "question": "Which best describes your interest in numbers and models?",
                     "options": ["I enjoy building financial or statistical models", "I prefer working with words and ideas", "I prefer hands-on building/making", "I prefer working directly with people"],
                     "answer": 0, "skill": "quantitative_aptitude"},
                    {"id": "ya_sa3", "question": "When solving a problem, you tend to:",
                     "options": ["Break it into an algorithm or step-by-step process", "Look at the historical or social context", "Consider the ethical implications first", "Consider the business/financial impact first"],
                     "answer": 0, "skill": "computational_thinking"},
                    {"id": "ya_sa4", "question": "Which project sounds most interesting to you?",
                     "options": ["Training a machine learning model", "Writing a business plan", "Analyzing an economic policy", "Studying language and linguistics"],
                     "answer": 0, "skill": "technical_aptitude"},
                ],
            },
            learning_style_section("ya"),
        ],
    },
    "26-40": {
        "label": "Adult Learners (Ages 26–40)",
        "description": "Assessments for working adults and career-changers, covering professional reasoning, financial literacy, and preferred learning style.",
        "sections": [
            {
                "id": "professional_reasoning",
                "title": "Professional Reasoning",
                "type": "multiple_choice",
                "questions": [
                    {"id": "al_pr1", "question": "Your team's project is behind schedule. What is the best first step?",
                     "options": ["Assign blame to whoever is slowest", "Identify the specific bottleneck causing the delay", "Extend the deadline without investigation", "Add more people without a plan"],
                     "answer": 1, "skill": "problem_diagnosis"},
                    {"id": "al_pr2", "question": "A dataset shows your company's sales rose after a price increase. What should you check before concluding the price increase caused the rise?",
                     "options": ["Whether other factors (season, marketing) changed too", "Nothing, the data speaks for itself", "Only the price change matters", "Whether the CEO approved it"],
                     "answer": 0, "skill": "business_data_literacy"},
                    {"id": "al_pr3", "question": "When negotiating, which approach best serves a long-term relationship?",
                     "options": ["Try to win at all costs", "Look for a mutually acceptable outcome", "Avoid the negotiation entirely", "Let the other side decide everything"],
                     "answer": 1, "skill": "negotiation"},
                ],
            },
            {
                "id": "financial_literacy_adult",
                "title": "Financial Literacy",
                "type": "multiple_choice",
                "questions": [
                    {"id": "al_fl1", "question": "What is the main purpose of an emergency fund?",
                     "options": ["Covering unexpected expenses without going into debt", "Maximizing investment returns", "Avoiding taxes", "Paying rent every month"],
                     "answer": 0, "skill": "financial_planning"},
                    {"id": "al_fl2", "question": "Compound interest means:",
                     "options": ["Interest earned only on the original amount", "Interest earned on both the principal and previously earned interest", "A one-time interest payment", "Interest that decreases over time"],
                     "answer": 1, "skill": "compound_interest"},
                    {"id": "al_fl3", "question": "Diversifying investments primarily helps to:",
                     "options": ["Guarantee profit", "Reduce risk by spreading it across assets", "Avoid all taxes", "Eliminate the need to save"],
                     "answer": 1, "skill": "investment_basics"},
                ],
            },
            learning_style_section("al"),
        ],
    },
    "41-60": {
        "label": "Experienced Adult Learners (Ages 41–60)",
        "description": "Assessments for experienced adult learners and career changers, covering applied critical thinking, digital literacy, and learning-style preferences.",
        "sections": [
            {
                "id": "applied_critical_thinking",
                "title": "Applied Critical Thinking",
                "type": "multiple_choice",
                "questions": [
                    {"id": "ex_ct1", "question": "A news article cites a single study to make a sweeping claim. What is the most reasonable response?",
                     "options": ["Accept it immediately since it's 'a study'", "Check if the finding has been replicated by other research", "Share it widely without checking", "Dismiss it without reading further"],
                     "answer": 1, "skill": "evidence_evaluation"},
                    {"id": "ex_ct2", "question": "Which of these best reflects lifelong learning mindset?",
                     "options": ["Assuming your existing knowledge never needs updating", "Being open to revising your views with new evidence", "Avoiding anything unfamiliar", "Relying only on decades-old training"],
                     "answer": 1, "skill": "growth_mindset"},
                    {"id": "ex_ct3", "question": "When mentoring a younger colleague on a new technology, the most useful approach is to:",
                     "options": ["Insist your older approach is always better", "Learn the fundamentals alongside them", "Refuse to engage with the new technology", "Delegate all of it without understanding it"],
                     "answer": 1, "skill": "adaptability"},
                ],
            },
            {
                "id": "digital_literacy",
                "title": "Digital & Technology Literacy",
                "type": "multiple_choice",
                "questions": [
                    {"id": "ex_dl1", "question": "What is a practical first step to improve your online account security?",
                     "options": ["Reuse the same simple password everywhere", "Enable two-factor authentication on important accounts", "Share passwords by email", "Turn off all security settings"],
                     "answer": 1, "skill": "digital_security"},
                    {"id": "ex_dl2", "question": "Which best describes what 'artificial intelligence' broadly refers to?",
                     "options": ["Robots that think exactly like humans", "Computer systems performing tasks that typically require human intelligence", "Only science-fiction concepts", "A single specific software product"],
                     "answer": 1, "skill": "ai_literacy"},
                    {"id": "ex_dl3", "question": "Before sharing an unfamiliar online article, a good practice is to:",
                     "options": ["Check the source and look for corroboration", "Share it immediately if the headline is interesting", "Assume all online content is accurate", "Ignore the source entirely"],
                     "answer": 0, "skill": "media_literacy"},
                ],
            },
            learning_style_section("ex"),
        ],
    },
}

NEW_SKILL_RECOMMENDATIONS = {
    "confounding_variables": ["Data Science", "Critical Thinking"],
    "logical_fallacies": ["Critical Thinking", "Philosophy"],
    "experimental_design": ["Data Science", "Science"],
    "cognitive_bias": ["Critical Thinking", "Philosophy"],
    "data_analysis_aptitude": ["Data Science", "Machine Learning"],
    "quantitative_aptitude": ["Business Analytics", "Finance", "Economics"],
    "computational_thinking": ["Artificial Intelligence", "Coding"],
    "technical_aptitude": ["Machine Learning", "Natural Language Processing"],
    "problem_diagnosis": ["Business Studies", "Critical Thinking"],
    "business_data_literacy": ["Business Analytics", "Data Science"],
    "negotiation": ["Business Studies", "Economics"],
    "financial_planning": ["Finance", "Business Studies"],
    "compound_interest": ["Finance", "Economics"],
    "investment_basics": ["Finance", "Economics"],
    "evidence_evaluation": ["Critical Thinking", "Data Science"],
    "growth_mindset": ["Critical Thinking"],
    "adaptability": ["Business Studies", "Artificial Intelligence"],
    "digital_security": ["ICT & Computer Science"],
    "ai_literacy": ["Artificial Intelligence", "Machine Learning"],
    "media_literacy": ["Critical Thinking", "World Politics"],
    "kinesthetic_learning": ["Practical Skills"],
    "practice_based_learning": ["Practical Skills"],
    "self_directed_learning": ["Study Skills", "Practical Skills"],
}


def main() -> None:
    with open(ASSESSMENT_PATH, encoding="utf-8") as f:
        data = json.load(f)

    data["age_groups"].update(AGE_GROUPS)
    data.setdefault("skill_recommendations", {}).update(NEW_SKILL_RECOMMENDATIONS)

    with open(ASSESSMENT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Assessment Centre now covers age groups: {list(data['age_groups'].keys())}")


if __name__ == "__main__":
    main()
