#!/usr/bin/env python3
"""Add adult-friendly self-defense and life-skills content:

- backend/data/practical_skills/practical_skills.json: new "self_defense_adult"
  pathway (situational awareness, de-escalation, escape technique, safety
  planning -- non-violent, educational, matches what a community self-defense
  class teaches) plus a new "adult_life_skills" pathway (renting, taxes,
  salary negotiation, etc).
- backend/data/survival_skills/survival_skills.json: new "adult_personal_safety"
  category, parallel to the existing child-oriented "personal_safety" category
  but written for adult learners (no "adult_supervision_required", real adult
  safety-organization links instead of child-safety ones).

Re-run after editing:
    python3 backend/scripts/generate_adult_skills_content.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
PRACTICAL_PATH = BASE_DIR / "data" / "practical_skills" / "practical_skills.json"
SURVIVAL_PATH = BASE_DIR / "data" / "survival_skills" / "survival_skills.json"


def yt(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


SELF_DEFENSE_SKILLS = [
    {
        "id": "sd1", "title": "Situational Awareness",
        "description": "Notice your surroundings and potential risks before they become a problem.",
        "why": "Most self-defense experts agree that avoiding a dangerous situation is far more effective than physically escaping one.",
        "steps": "1. Keep your head up and phone away when walking alone. 2. Notice exits when you enter a new place. 3. Trust your gut -- if a situation feels wrong, leave. 4. Vary your routes and routines when possible.",
        "activity": "Practice a 'safety scan' next time you enter an unfamiliar building: note the exits and anyone acting unusually.",
        "grade_range": "Adult",
    },
    {
        "id": "sd2", "title": "Verbal De-escalation",
        "description": "Use calm, assertive communication to defuse a tense confrontation before it turns physical.",
        "why": "Most conflicts can be de-escalated with calm, non-threatening language and body positioning.",
        "steps": "1. Keep a calm, low, steady voice. 2. Keep hands visible and open, not clenched. 3. Give the other person an easy way to back down without losing face. 4. Create space and move toward an exit while talking.",
        "activity": "Role-play a tense conversation with a friend and practice de-escalating it verbally.",
        "grade_range": "Adult",
    },
    {
        "id": "sd3", "title": "Basic Escape from a Wrist Grab",
        "description": "A simple, low-force technique to break free if someone grabs your wrist.",
        "why": "Escaping a grab quickly creates distance so you can get away and call for help.",
        "steps": "1. Turn your wrist toward the attacker's thumb, the weakest point of their grip. 2. Pull sharply and step back at the same time. 3. Immediately create distance and move toward people or an exit. 4. Call out loudly for help while moving away.",
        "activity": "Practice the wrist-turn escape slowly and safely with a partner at low intensity, or watch a certified instructor demonstrate it.",
        "grade_range": "Adult",
    },
    {
        "id": "sd4", "title": "Personal Safety Planning",
        "description": "Build simple habits and a plan that reduce risk in daily life.",
        "why": "A safety plan (who to call, where to go, what to carry) means you react faster under stress.",
        "steps": "1. Share your location with a trusted contact on longer trips. 2. Keep your phone charged and know your local emergency number. 3. Carry a whistle or personal alarm if it makes you feel safer. 4. Know the nearest safe locations (police station, 24-hour store) on routes you travel often.",
        "activity": "Write out a one-page personal safety plan: emergency contacts, local emergency number, and two safe locations near home and work.",
        "grade_range": "Adult",
    },
    {
        "id": "sd5", "title": "When and How to Get Professional Training",
        "description": "Understand the value of in-person self-defense classes and how to choose one.",
        "why": "No article or video can replace hands-on practice with a certified instructor who can correct your technique safely.",
        "steps": "1. Look for certified instructors in krav maga, Brazilian jiu-jitsu, judo, or a dedicated women's self-defense course. 2. Attend a trial class before committing. 3. Practice regularly -- self-defense is a skill that fades without repetition. 4. Know your local laws on self-defense and reasonable force, which vary by country and state.",
        "activity": "Research one certified self-defense class or martial arts school near you and note its schedule and cost.",
        "grade_range": "Adult",
    },
]

SELF_DEFENSE_MODULES = [
    {
        "title": "Awareness and Avoidance", "level": "beginner", "duration_minutes": 30,
        "description": "The first and most effective layer of self-defense: noticing and avoiding danger.",
        "learning_objectives": ["Explain why awareness prevents most confrontations", "Identify environmental risk cues", "Practice a safety scan routine"],
        "steps": ["Scan a room or street for exits and people", "Keep situational awareness while using a phone", "Trust intuition and leave uncomfortable situations early"],
        "hands_on_activity": "Do a safety scan in three different real locations this week and note what you noticed.",
        "quiz": [{"q": "What is the most effective form of self-defense?", "a": "Avoiding the dangerous situation in the first place"}],
        "pro_tip": "Confidence and calm body language alone can deter many potential confrontations.",
        "links": {"video_link": yt("situational awareness self defense basics"), "text_link": "https://www.rainn.org/articles/self-defense", "resource_link": yt("women's self defense class basics")},
    },
    {
        "title": "De-escalation and Boundary-Setting", "level": "intermediate", "duration_minutes": 30,
        "description": "Using voice, distance, and body language to defuse tense situations.",
        "learning_objectives": ["Use a calm assertive voice", "Set a clear verbal boundary", "Maintain safe distance and open body language"],
        "steps": ["Practice saying 'Back up, I need space' calmly and firmly", "Keep hands open and visible", "Move toward an exit while speaking"],
        "hands_on_activity": "Role-play three different de-escalation scenarios with a partner.",
        "quiz": [{"q": "What tone of voice works best for de-escalation?", "a": "Calm, low, and steady"}],
        "pro_tip": "Assertive is not the same as aggressive -- stay firm but non-threatening.",
        "links": {"video_link": yt("verbal de-escalation techniques self defense"), "text_link": "https://www.rainn.org/articles/self-defense", "resource_link": yt("conflict de-escalation training")},
    },
    {
        "title": "Basic Physical Escapes", "level": "advanced", "duration_minutes": 35,
        "description": "Simple, low-force techniques to escape common grabs and create distance.",
        "learning_objectives": ["Perform a basic wrist-grab escape", "Understand the goal is escape, not a fight", "Combine physical escape with calling for help"],
        "steps": ["Turn toward the attacker's thumb to break a wrist grab", "Step back immediately to create distance", "Call loudly for help while moving toward people or an exit"],
        "hands_on_activity": "Practice the escape at slow, safe speed with a training partner or find a local class to try it hands-on.",
        "quiz": [{"q": "After escaping a grab, what should you do next?", "a": "Create distance and move toward help, calling out loudly"}],
        "pro_tip": "Escaping and getting to safety is always the goal -- not winning a physical fight.",
        "links": {"video_link": yt("basic wrist grab escape self defense technique"), "text_link": "https://www.rainn.org/articles/self-defense", "resource_link": yt("beginner self defense techniques")},
    },
]

ADULT_LIFE_SKILLS = [
    {
        "id": "al1", "title": "Understanding a Rental Lease",
        "description": "Read and understand the key terms of a residential lease before signing.",
        "why": "A lease is a binding legal contract -- understanding it protects your money and rights as a tenant.",
        "steps": "1. Check the rent amount, due date, and deposit terms. 2. Note the lease length and renewal/termination conditions. 3. Understand who's responsible for repairs and utilities. 4. Ask about rules on guests, pets, and subletting before signing.",
        "activity": "Read a sample lease agreement online and list five clauses you would want clarified before signing.",
        "grade_range": "Adult",
    },
    {
        "id": "al2", "title": "Basic Income Tax Concepts",
        "description": "Understand the basic vocabulary and process of filing income taxes.",
        "why": "Nearly every working adult needs a basic understanding of taxes to avoid costly mistakes.",
        "steps": "1. Learn the difference between gross and net (take-home) income. 2. Understand common deductions and credits. 3. Know your country's filing deadline. 4. Keep receipts and records organized throughout the year.",
        "activity": "Look up your country's tax authority website and identify this year's filing deadline and standard deduction.",
        "grade_range": "Adult",
    },
    {
        "id": "al3", "title": "Negotiating a Salary or Raise",
        "description": "Prepare for and conduct a professional salary negotiation.",
        "why": "Most employers expect some negotiation, and a well-prepared case can meaningfully increase lifetime earnings.",
        "steps": "1. Research typical salary ranges for your role and location. 2. Document your achievements and impact. 3. Practice stating your ask clearly and confidently. 4. Be ready to discuss the whole package (benefits, flexibility), not just base pay.",
        "activity": "Write a two-minute script making the case for a raise, including three concrete achievements.",
        "grade_range": "Adult",
    },
    {
        "id": "al4", "title": "Building an Emergency Fund",
        "description": "Understand why and how to save a basic financial safety net.",
        "why": "An emergency fund prevents a sudden expense from becoming a debt crisis.",
        "steps": "1. Set a target of 3-6 months of essential expenses. 2. Open a separate savings account for it. 3. Automate a small regular transfer, even if modest. 4. Only use it for genuine emergencies, and rebuild it after use.",
        "activity": "Calculate your own 3-month essential-expenses target and set up (or review) a dedicated savings account.",
        "grade_range": "Adult",
    },
    {
        "id": "al5", "title": "Healthy Work-Life Boundaries",
        "description": "Set sustainable boundaries between work and personal life.",
        "why": "Chronic overwork is linked to burnout and worse long-term performance and health.",
        "steps": "1. Define clear work hours and communicate them to colleagues. 2. Turn off work notifications outside those hours where possible. 3. Schedule personal time and treat it as non-negotiable. 4. Notice early signs of burnout and address them proactively.",
        "activity": "Write down your ideal weekly work-hours boundary and one change you'll make this week to protect it.",
        "grade_range": "Adult",
    },
]

ADULT_LIFE_MODULES = [
    {
        "title": "Renting and Contracts", "level": "beginner", "duration_minutes": 30,
        "description": "Understand rental leases and other everyday contracts.",
        "learning_objectives": ["Identify key lease terms", "Understand tenant rights and responsibilities", "Spot red flags in a contract"],
        "steps": ["Review rent, deposit, and length of a sample lease", "Identify repair and utility responsibilities", "List questions to ask a landlord before signing"],
        "hands_on_activity": "Annotate a sample lease with questions you would ask before signing.",
        "quiz": [{"q": "Why is it important to understand a lease before signing?", "a": "It is a legally binding contract that affects your money and rights"}],
        "pro_tip": "Always get any verbal promise from a landlord in writing.",
        "links": {"video_link": yt("how to read a rental lease agreement"), "text_link": "https://www.usa.gov/renters-rights", "resource_link": yt("first apartment tips")},
    },
    {
        "title": "Personal Finance Fundamentals", "level": "intermediate", "duration_minutes": 35,
        "description": "Build core adult financial literacy: budgeting, saving, and taxes.",
        "learning_objectives": ["Build a basic monthly budget", "Explain the purpose of an emergency fund", "Describe basic income tax concepts"],
        "steps": ["List monthly income and essential expenses", "Set a savings target for an emergency fund", "Identify your country's tax filing deadline"],
        "hands_on_activity": "Create a one-page monthly budget using your own (or estimated) income and expenses.",
        "quiz": [{"q": "What is an emergency fund for?", "a": "Covering unexpected expenses without going into debt"}],
        "pro_tip": "Automating savings removes the need for willpower every month.",
        "links": {"video_link": yt("personal finance basics for adults"), "text_link": "https://www.investopedia.com/personal-finance-4427760", "resource_link": yt("budgeting for beginners")},
    },
    {
        "title": "Career and Workplace Skills", "level": "advanced", "duration_minutes": 35,
        "description": "Negotiate compensation and protect work-life balance.",
        "learning_objectives": ["Prepare a salary negotiation case", "Identify signs of burnout", "Set healthy work boundaries"],
        "steps": ["Research typical pay for your role", "Draft a negotiation script with concrete achievements", "Define and communicate personal work-hour boundaries"],
        "hands_on_activity": "Practice your negotiation script out loud with a friend or mentor.",
        "quiz": [{"q": "Besides base salary, what else can be negotiated in a job offer?", "a": "Benefits, flexibility, bonuses, and other parts of the total package"}],
        "pro_tip": "Employers usually expect candidates to negotiate -- it rarely hurts to ask professionally.",
        "links": {"video_link": yt("how to negotiate salary raise"), "text_link": "https://www.investopedia.com/personal-finance-4427760", "resource_link": yt("avoiding burnout at work")},
    },
]


def build_pathway(label, emoji, certificate, skills, modules):
    quiz = []
    for m in modules:
        for q in m["quiz"]:
            quiz.append({
                "question": q["q"],
                "options": [q["a"], "Not applicable", "Ignore the situation", "None of the above"],
                "answer": 0,
            })
    return {
        "label": label,
        "emoji": emoji,
        "certificate": certificate,
        "skills": skills,
        "quiz": quiz,
        "modules": modules,
    }


def update_practical_skills():
    with open(PRACTICAL_PATH, encoding="utf-8") as f:
        data = json.load(f)

    data["pathways"]["self_defense_adult"] = build_pathway(
        "Self-Defense for Adults", "🛡️", "Personal Safety & Self-Defense Certificate",
        SELF_DEFENSE_SKILLS, SELF_DEFENSE_MODULES,
    )
    data["pathways"]["adult_life_skills"] = build_pathway(
        "Adult Life Skills", "🏠", "Adult Life Skills Certificate",
        ADULT_LIFE_SKILLS, ADULT_LIFE_MODULES,
    )

    with open(PRACTICAL_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"practical_skills.json now has {len(data['pathways'])} pathways.")


ADULT_PERSONAL_SAFETY = [
    {
        "name": "Situational Awareness for Adults",
        "grade_range": "Adult",
        "category": "adult_personal_safety",
        "adult_supervision_required": False,
        "learning_objectives": [
            "Notice environmental risk cues before they escalate",
            "Build habits that reduce personal risk",
            "Trust intuition about unsafe situations",
        ],
        "key_steps": [
            "Keep your head up and stay off your phone when walking alone at night",
            "Identify exits whenever you enter a new place",
            "Vary routines and routes when practical",
            "Trust your gut instinct and leave a situation that feels wrong",
        ],
        "practice_activities": [
            "Do a 'safety scan' the next time you enter an unfamiliar venue",
            "Share your live location with a trusted contact on a solo trip",
        ],
        "quiz": [
            {"q": "What is usually the most effective form of self-defense?", "a": "Avoiding the dangerous situation altogether through awareness"},
            {"q": "What should you do if a situation feels wrong, even without clear proof?", "a": "Trust your instinct and leave"},
        ],
        "important_note": "This module covers general safety awareness, not a substitute for a certified self-defense or personal safety course.",
        "progress_tracking": {"completion_required": True, "min_quiz_score": 70},
        "links": {
            "video_link": yt("personal safety awareness tips for adults"),
            "text_link": "https://www.rainn.org/articles/self-defense",
            "resource_link": yt("women's safety tips walking alone"),
            "video_search_general": yt("adult personal safety self defense"),
        },
    },
    {
        "name": "Verbal De-escalation Techniques",
        "grade_range": "Adult",
        "category": "adult_personal_safety",
        "adult_supervision_required": False,
        "learning_objectives": [
            "Use calm, assertive language to defuse tension",
            "Maintain safe distance and open body language",
            "Recognize when to disengage and seek help",
        ],
        "key_steps": [
            "Keep your voice calm, low, and steady",
            "Keep hands visible and open, avoid crossing arms or clenching fists",
            "Give the other person an easy way to back down",
            "Move toward an exit or other people while talking",
        ],
        "practice_activities": [
            "Role-play a tense conversation with a friend and practice de-escalating calmly",
        ],
        "quiz": [
            {"q": "What voice tone helps de-escalate a tense situation?", "a": "Calm, low, and steady"},
        ],
        "important_note": "If a situation feels physically dangerous, prioritize leaving and calling for help over continued conversation.",
        "progress_tracking": {"completion_required": True, "min_quiz_score": 70},
        "links": {
            "video_link": yt("verbal de-escalation techniques adults"),
            "text_link": "https://www.rainn.org/articles/self-defense",
            "resource_link": yt("conflict de-escalation training basics"),
            "video_search_general": yt("de-escalation skills training"),
        },
    },
    {
        "name": "Travel and Public Transport Safety",
        "grade_range": "Adult",
        "category": "adult_personal_safety",
        "adult_supervision_required": False,
        "learning_objectives": [
            "Apply safety habits when traveling or commuting alone",
            "Plan ahead for unfamiliar destinations",
            "Know how to get help while traveling",
        ],
        "key_steps": [
            "Share your itinerary with someone you trust",
            "Research the safety reputation of an area before visiting",
            "Sit near the driver or other passengers on public transport when possible",
            "Keep your phone charged and emergency numbers saved",
        ],
        "practice_activities": [
            "Write a simple travel safety checklist for your next trip",
        ],
        "quiz": [
            {"q": "What is a simple safety habit for solo travel?", "a": "Share your itinerary with a trusted contact"},
        ],
        "important_note": "Local emergency numbers and norms vary by country -- always check before you travel.",
        "progress_tracking": {"completion_required": True, "min_quiz_score": 70},
        "links": {
            "video_link": yt("solo travel safety tips adults"),
            "text_link": "https://travel.state.gov/content/travel/en/international-travel/before-you-go/travel-safety.html",
            "resource_link": yt("public transport safety tips"),
            "video_search_general": yt("adult travel safety tips"),
        },
    },
    {
        "name": "Digital and Online Safety for Adults",
        "grade_range": "Adult",
        "category": "adult_personal_safety",
        "adult_supervision_required": False,
        "learning_objectives": [
            "Protect personal information online",
            "Recognize common scams and phishing attempts",
            "Practice safe password and account habits",
        ],
        "key_steps": [
            "Use unique, strong passwords and a password manager",
            "Enable two-factor authentication on important accounts",
            "Be skeptical of urgent requests for money or personal information",
            "Limit how much personal/location information you share publicly",
        ],
        "practice_activities": [
            "Audit your most important accounts and enable two-factor authentication where missing",
        ],
        "quiz": [
            {"q": "What is a simple way to protect an important online account?", "a": "Enable two-factor authentication and use a strong, unique password"},
        ],
        "important_note": "If you suspect fraud, contact your bank or platform directly using an official number, not one provided by the suspicious contact.",
        "progress_tracking": {"completion_required": True, "min_quiz_score": 70},
        "links": {
            "video_link": yt("online safety tips for adults"),
            "text_link": "https://www.cisa.gov/topics/cybersecurity-best-practices",
            "resource_link": yt("how to spot a phishing scam"),
            "video_search_general": yt("cybersecurity basics for adults"),
        },
    },
]


def update_survival_skills():
    with open(SURVIVAL_PATH, encoding="utf-8") as f:
        data = json.load(f)
    data["categories"]["adult_personal_safety"] = ADULT_PERSONAL_SAFETY
    with open(SURVIVAL_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"survival_skills.json now has {len(data['categories'])} categories.")


def main():
    update_practical_skills()
    update_survival_skills()


if __name__ == "__main__":
    main()
