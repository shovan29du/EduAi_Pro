#!/usr/bin/env python3
"""Depth pass, C2 Health Education: fill in real, hand-checked
data_table content for the 99 C2 Health Education lessons not covered
by the earlier breadth-first batch. Brings C2 Health Education to
full 100/100 coverage.

Unlike most C2 subjects (70 lessons), Health Education has 100
lessons: l1-l60 core topics, l61-l80 "Comparative Case Study" lessons,
and l81-l100 "Applied Research Seminar" lessons, both driven by the
same 20-topic list. l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_health_education_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "health-education-c2-l1": {
        "data_table": table(["Topic", "Feature"], [
            ["Public health fundamentals", "Focuses on population-level prevention rather than individual treatment"],
        ]),
    },
    "health-education-c2-l2": {
        "data_table": table(["Topic", "Feature"], [
            ["Health systems & policy", "Examines how care is organized, financed, and regulated"],
        ]),
    },
    "health-education-c2-l4": {
        "data_table": table(["Skill", "Detail"], [
            ["Consumer health literacy", "Evaluates health claims and product marketing critically"],
        ]),
    },
    "health-education-c2-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Community & environmental health", "Links surrounding conditions like air and water quality to health outcomes"],
        ]),
    },
    "health-education-c2-l6": {
        "data_table": table(["Type", "Feature"], [
            ["Communicable disease", "Spreads between individuals via a pathogen"],
            ["Noncommunicable disease", "Not transmissible; often linked to lifestyle or genetics"],
        ]),
    },
    "health-education-c2-l7": {
        "data_table": table(["Strategy", "Detail"], [
            ["Problem-focused coping", "Directly addresses the source of stress"],
            ["Emotion-focused coping", "Manages the emotional response to stress"],
        ]),
    },
    "health-education-c2-l8": {
        "data_table": table(["Skill", "Detail"], [
            ["Assertive communication", "Expresses needs clearly while respecting others in a relationship"],
        ]),
    },
    "health-education-c2-l9": {
        "data_table": table(["Domain", "Change"], [
            ["Adolescent development", "Involves rapid physical, cognitive, and emotional change"],
        ]),
    },
    "health-education-c2-l10": {
        "data_table": table(["Career", "Focus"], [
            ["Public health career", "Works on population-level prevention and policy"],
            ["Clinical career", "Works directly with individual patient care"],
        ]),
    },
    "health-education-c2-l11": {
        "data_table": table(["Approach", "Feature"], [
            ["Comprehensive sexuality education", "Covers a broad range of topics including consent and relationships"],
        ]),
    },
    "health-education-c2-l12": {
        "data_table": table(["Topic", "Focus"], [
            ["Family life education", "Addresses relationships, parenting, and family structure across the lifespan"],
        ]),
    },
    "health-education-c2-l13": {
        "data_table": table(["Strategy", "Detail"], [
            ["Tobacco/vaping prevention", "Combines education, policy, and access restriction to reduce youth uptake"],
        ]),
    },
    "health-education-c2-l14": {
        "data_table": table(["Element", "Purpose"], [
            ["Nutrition label", "Standardizes information to support informed food choices"],
        ]),
    },
    "health-education-c2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Premium", "Regular payment for maintaining health insurance coverage"],
            ["Deductible", "Amount paid out of pocket before insurance coverage begins"],
        ]),
    },
    "health-education-c2-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Telehealth", "Delivers care remotely via digital communication technology"],
        ]),
    },
    "health-education-c2-l17": {
        "data_table": table(["Service", "Purpose"], [
            ["School health service", "Provides on-site basic care and health screening for students"],
        ]),
    },
    "health-education-c2-l18": {
        "data_table": table(["Step", "Purpose"], [
            ["Outbreak investigation", "Identifies the source and mode of spread to contain a disease cluster"],
        ]),
    },
    "health-education-c2-l19": {
        "data_table": table(["Risk Factor", "Modifiable"], [
            ["High blood pressure", "Yes, through diet, exercise, and medication"],
            ["Family history", "No"],
        ]),
    },
    "health-education-c2-l20": {
        "data_table": table(["Concept", "Detail"], [
            ["Cancer screening policy", "Balances early detection benefits against overdiagnosis risk"],
        ]),
    },
    "health-education-c2-l21": {
        "data_table": table(["Type", "Feature"], [
            ["Type 1 diabetes", "Autoimmune destruction of insulin-producing cells, requires insulin therapy"],
            ["Type 2 diabetes", "Insulin resistance, often managed with lifestyle change and medication"],
        ]),
    },
    "health-education-c2-l22": {
        "data_table": table(["Condition", "Feature"], [
            ["Asthma", "Reversible airway inflammation and constriction"],
            ["COPD", "Progressive, largely irreversible airflow limitation"],
        ]),
    },
    "health-education-c2-l23": {
        "data_table": table(["Principle", "Detail"], [
            ["Trauma-informed care", "Recognizes trauma's impact and avoids re-traumatizing the patient"],
        ]),
    },
    "health-education-c2-l24": {
        "data_table": table(["Strategy", "Detail"], [
            ["Suicide prevention", "Combines risk screening, means restriction, and accessible crisis support"],
        ]),
    },
    "health-education-c2-l25": {
        "data_table": table(["Approach", "Detail"], [
            ["Eating disorder treatment", "Integrates medical, nutritional, and psychological care"],
        ]),
    },
    "health-education-c2-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Metabolic health", "Encompasses blood sugar, lipid levels, and blood pressure together"],
        ]),
    },
    "health-education-c2-l27": {
        "data_table": table(["Step", "Purpose"], [
            ["HACCP hazard analysis", "Identifies points in food handling where contamination risk is highest"],
        ]),
    },
    "health-education-c2-l28": {
        "data_table": table(["Deficiency", "Effect"], [
            ["Iron deficiency", "Leads to anemia and fatigue"],
            ["Vitamin D deficiency", "Weakens bone health"],
        ]),
    },
    "health-education-c2-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Training periodization", "Structures training phases to optimize performance and recovery"],
        ]),
    },
    "health-education-c2-l30": {
        "data_table": table(["Step", "Purpose"], [
            ["Concussion protocol", "Removes the athlete from play and requires graded return to activity"],
        ]),
    },
    "health-education-c2-l31": {
        "data_table": table(["Concept", "Formula"], [
            ["Dose-response relationship", "Toxic effect generally increases with exposure dose"],
        ]),
    },
    "health-education-c2-l32": {
        "data_table": table(["Impact", "Detail"], [
            ["Climate change and health", "Rising heat and shifting disease vectors expand certain health risks"],
        ]),
    },
    "health-education-c2-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Ergonomics", "Designs workspaces to reduce strain and prevent repetitive injury"],
        ]),
    },
    "health-education-c2-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Herd immunity", "Sufficient population immunity limits disease spread, protecting the unvaccinated"],
        ]),
    },
    "health-education-c2-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Antibiotic resistance", "Overuse accelerates bacteria evolving resistance to existing drugs"],
        ]),
    },
    "health-education-c2-l36": {
        "data_table": table(["Practice", "Purpose"], [
            ["Routine STI testing", "Detects infections early, often before symptoms appear"],
        ]),
    },
    "health-education-c2-l37": {
        "data_table": table(["Issue", "Detail"], [
            ["Reproductive health policy", "Balances access, autonomy, and public health considerations"],
        ]),
    },
    "health-education-c2-l38": {
        "data_table": table(["Metric", "Detail"], [
            ["Maternal mortality rate", "Tracks deaths related to pregnancy and childbirth per population"],
        ]),
    },
    "health-education-c2-l39": {
        "data_table": table(["Behavior", "Risk"], [
            ["Adolescent risk behavior", "Peer influence and impulsivity elevate certain health risks in this age group"],
        ]),
    },
    "health-education-c2-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Polypharmacy", "Managing multiple concurrent medications raises interaction risk in older adults"],
        ]),
    },
    "health-education-c2-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Disability accommodation", "Modifies environments and services to ensure equitable access"],
        ]),
    },
    "health-education-c2-l42": {
        "data_table": table(["Issue", "Detail"], [
            ["Insurance access disparity", "Coverage gaps disproportionately affect lower-income populations"],
        ]),
    },
    "health-education-c2-l43": {
        "data_table": table(["Model", "Feature"], [
            ["Single-payer system", "Government funds care through a unified public insurance program"],
            ["Multi-payer system", "Multiple private and public insurers coexist"],
        ]),
    },
    "health-education-c2-l44": {
        "data_table": table(["Principle", "Detail"], [
            ["Risk messaging", "Clear, consistent communication builds public trust during a health crisis"],
        ]),
    },
    "health-education-c2-l45": {
        "data_table": table(["Component", "Detail"], [
            ["Health Belief Model", "Behavior change depends on perceived susceptibility, severity, and benefits"],
        ]),
    },
    "health-education-c2-l46": {
        "data_table": table(["Effect", "Detail"], [
            ["Chronic stress", "Sustained cortisol elevation contributes to cardiovascular and immune strain"],
        ]),
    },
    "health-education-c2-l47": {
        "data_table": table(["Approach", "Detail"], [
            ["Substance use disorder treatment", "Combines medical, behavioral, and social support components"],
        ]),
    },
    "health-education-c2-l48": {
        "data_table": table(["Policy", "Detail"], [
            ["Alcohol policy intervention", "Taxation and availability restriction reduce population-level harm"],
        ]),
    },
    "health-education-c2-l49": {
        "data_table": table(["Policy", "Detail"], [
            ["Tobacco control policy", "Taxation, advertising limits, and smoke-free laws reduce smoking rates"],
        ]),
    },
    "health-education-c2-l50": {
        "data_table": table(["System", "Purpose"], [
            ["Trauma triage system", "Directs patients to appropriate care level based on injury severity"],
        ]),
    },
    "health-education-c2-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Disaster public health response", "Coordinates surveillance, care, and resource allocation during emergencies"],
        ]),
    },
    "health-education-c2-l52": {
        "data_table": table(["Step", "Purpose"], [
            ["Community health needs assessment", "Identifies local health priorities to guide resource allocation"],
        ]),
    },
    "health-education-c2-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Health numeracy", "Ability to interpret numerical medical information like risk percentages"],
        ]),
    },
    "health-education-c2-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Alternative medicine claim evaluation", "Requires checking for controlled clinical evidence, not testimonials"],
        ]),
    },
    "health-education-c2-l55": {
        "data_table": table(["Approach", "Detail"], [
            ["Public health violence prevention", "Treats violence as a preventable outcome of risk and protective factors"],
        ]),
    },
    "health-education-c2-l56": {
        "data_table": table(["Disorder", "Feature"], [
            ["Insomnia", "Persistent difficulty falling or staying asleep"],
            ["Sleep apnea", "Repeated breathing interruptions during sleep"],
        ]),
    },
    "health-education-c2-l57": {
        "data_table": table(["Guideline", "Purpose"], [
            ["Preventive screening guideline", "Balances detection benefit against cost and false-positive harm"],
        ]),
    },
    "health-education-c2-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Social determinants of health", "Income, education, and environment shape health outcomes beyond care access"],
        ]),
    },
    "health-education-c2-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Health disparity research", "Documents and explains unequal health outcomes across population groups"],
        ]),
    },
    "health-education-c2-l60": {
        "data_table": table(["Task", "Focus"], [
            ["Community intervention capstone", "Designs a program addressing an identified local health need"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["SMART Goal Letter", "Meaning"], [
    ["S", "Specific"], ["M", "Measurable"], ["A", "Achievable"], ["R", "Relevant"], ["T", "Time-bound"],
])

# 20-topic list underlying both the "Comparative Case Study" (l61-l80)
# and "Applied Research Seminar" (l81-l100) blocks.
TOPIC_TABLES: list[dict] = [
    table(["Topic", "Application"], [["Health literacy", "Ability to find, understand, and apply health information"]]),
    table(["Topic", "Application"], [["Nutrition", "Diet quality shapes long-term chronic disease risk"]]),
    table(["Topic", "Application"], [["Physical activity", "Regular movement supports cardiovascular and metabolic health"]]),
    table(["Topic", "Application"], [["Sleep science", "Sleep quality and duration affect cognitive and physical recovery"]]),
    table(["Topic", "Application"], [["Mental wellbeing", "Psychological health is inseparable from overall physical health"]]),
    table(["Topic", "Application"], [["Stress management", "Effective coping strategies reduce the physiological burden of stress"]]),
    table(["Topic", "Application"], [["Sexual and reproductive health", "Access to accurate information supports informed personal decisions"]]),
    table(["Topic", "Application"], [["Communicable disease", "Prevention relies on hygiene, vaccination, and transmission control"]]),
    table(["Topic", "Application"], [["Noncommunicable disease", "Prevention relies on lifestyle factors and early screening"]]),
    table(["Topic", "Application"], [["Medicines and vaccines", "Safe use requires understanding dosage, interactions, and adherence"]]),
    table(["Topic", "Application"], [["Substance-use prevention", "Early education reduces risk of later substance misuse"]]),
    table(["Topic", "Application"], [["First aid", "Immediate correct response can prevent injury from worsening"]]),
    table(["Topic", "Application"], [["Injury prevention", "Identifying hazards reduces the likelihood of accidental harm"]]),
    table(["Topic", "Application"], [["Environmental health", "Surrounding conditions like air and water quality shape health outcomes"]]),
    table(["Topic", "Application"], [["Workplace health", "Ergonomic and safety practices reduce occupational injury and illness"]]),
    table(["Topic", "Application"], [["Public health systems", "Organized systems coordinate population-level prevention and response"]]),
    table(["Topic", "Application"], [["Health inequality", "Structural factors produce uneven health outcomes across groups"]]),
    table(["Topic", "Application"], [["Digital health", "Technology expands access to information and remote care"]]),
    table(["Topic", "Application"], [["Healthcare decision-making", "Weighing evidence and risk supports informed patient choices"]]),
    table(["Topic", "Application"], [["Personal health planning", "Proactive planning integrates prevention into everyday life"]]),
]

# l61-l80 "Comparative Case Study" lessons cover all 20 topics.
for i, lesson_n in enumerate(range(61, 81)):
    CHARTS[f"health-education-c2-l{lesson_n}"] = {
        "data_table": TOPIC_TABLES[i],
    }

# l81-l100 "Applied Research Seminar" lessons cover all 20 topics.
for i, lesson_n in enumerate(range(81, 101)):
    CHARTS[f"health-education-c2-l{lesson_n}"] = {
        "data_table": TOPIC_TABLES[i],
    }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Health Education lessons (completing 100/100).")


if __name__ == "__main__":
    main()
