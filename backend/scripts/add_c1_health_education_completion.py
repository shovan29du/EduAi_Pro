#!/usr/bin/env python3
"""Depth pass, C1 Health Education: fill in real, hand-checked
data_table content for the 99 C1 Health Education lessons not covered
by the earlier breadth-first batch. Brings C1 Health Education to full
100/100 coverage.

Note: like Critical Thinking, this subject has 100 lessons (not the
standard 70): l1-l60 core topics, l61 a "Foundations 2" duplicate,
l62-l80 "Comparative Case Study" lessons, and l81-l100 "Applied
Research Seminar" lessons.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_health_education_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "health-education-c1-l1": {
        "data_table": table(["Dimension", "Focus"], [
            ["Physical wellbeing", "Nutrition, activity, sleep, and preventive care"], ["Mental wellbeing", "Emotional regulation and psychological resilience"],
        ]),
    },
    "health-education-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Public health", "Protecting and improving the health of entire populations"],
        ]),
    },
    "health-education-c1-l4": {
        "data_table": table(["Nutrient", "Function"], [
            ["Carbohydrates", "Primary energy source"], ["Protein", "Builds and repairs tissue"],
        ]),
    },
    "health-education-c1-l5": {
        "data_table": table(["Guideline", "Detail"], [
            ["150 minutes moderate activity/week", "Common general adult activity recommendation"],
        ]),
    },
    "health-education-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Mental health literacy", "Knowledge and beliefs that help recognize and manage mental health conditions"],
        ]),
    },
    "health-education-c1-l7": {
        "data_table": table(["Stage", "Feature"], [
            ["REM sleep", "Associated with dreaming and memory consolidation"], ["Deep sleep", "Supports physical restoration"],
        ]),
    },
    "health-education-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Substance misuse", "Using a substance in a way that causes harm"],
        ]),
    },
    "health-education-c1-l9": {
        "data_table": table(["Topic", "Focus"], [
            ["Reproductive health", "Understanding the body's reproductive systems and safe practices"],
        ]),
    },
    "health-education-c1-l10": {
        "data_table": table(["Step", "Purpose"], [
            ["Recognizing hazards early", "Reduces the likelihood of preventable injury"],
        ]),
    },
    "health-education-c1-l11": {
        "data_table": table(["Practice", "Benefit"], [
            ["Handwashing", "One of the most effective ways to prevent disease spread"],
        ]),
    },
    "health-education-c1-l12": {
        "data_table": table(["Certification", "Focus"], [
            ["CPR certification", "Trains responders to assist during cardiac emergencies"],
        ]),
    },
    "health-education-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Health literacy", "The ability to find, understand, and use health information effectively"],
        ]),
    },
    "health-education-c1-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Herd immunity", "Population-level protection when enough people are immune to a disease"],
        ]),
    },
    "health-education-c1-l15": {
        "data_table": table(["Practice", "Reason"], [
            ["Checking expiration dates", "Ensures medication and product effectiveness and safety"],
        ]),
    },
    "health-education-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Body image", "A person's perception and feelings about their own physical appearance"],
        ]),
    },
    "health-education-c1-l17": {
        "data_table": table(["Life Stage", "Health Focus"], [
            ["Childhood", "Growth, immunization, and healthy habit formation"], ["Older adulthood", "Chronic disease management and fall prevention"],
        ]),
    },
    "health-education-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Epidemiology", "The study of disease patterns, causes, and effects in populations"],
        ]),
    },
    "health-education-c1-l19": {
        "data_table": table(["Strategy", "Example"], [
            ["Primary prevention", "Reducing risk factors before disease develops"],
        ]),
    },
    "health-education-c1-l20": {
        "data_table": table(["Risk Factor", "Detail"], [
            ["High blood pressure", "A major modifiable risk factor for heart disease"],
        ]),
    },
    "health-education-c1-l21": {
        "data_table": table(["Screening", "Purpose"], [
            ["Mammogram", "Detects breast cancer early"], ["Colonoscopy", "Detects colorectal cancer early"],
        ]),
    },
    "health-education-c1-l22": {
        "data_table": table(["Type", "Feature"], [
            ["Type 1 diabetes", "Autoimmune, body doesn't produce insulin"], ["Type 2 diabetes", "Often linked to lifestyle, body resists insulin"],
        ]),
    },
    "health-education-c1-l23": {
        "data_table": table(["Condition", "Feature"], [
            ["Asthma", "Chronic inflammation narrowing the airways"],
        ]),
    },
    "health-education-c1-l24": {
        "data_table": table(["Step", "Purpose"], [
            ["ALGEE approach", "A structured framework for helping someone in a mental health crisis"],
        ]),
    },
    "health-education-c1-l25": {
        "data_table": table(["Condition", "Sign"], [
            ["Anxiety", "Persistent excessive worry"], ["Depression", "Persistent low mood and loss of interest"],
        ]),
    },
    "health-education-c1-l26": {
        "data_table": table(["Condition", "Feature"], [
            ["Anorexia nervosa", "Severe restriction of food intake"], ["Bulimia nervosa", "Cycles of binge eating and purging"],
        ]),
    },
    "health-education-c1-l27": {
        "data_table": table(["Approach", "Focus"], [
            ["Sustainable weight management", "Gradual, long-term lifestyle change over quick fixes"],
        ]),
    },
    "health-education-c1-l28": {
        "data_table": table(["Practice", "Reason"], [
            ["Cooking meat to safe temperature", "Kills harmful bacteria that cause foodborne illness"],
        ]),
    },
    "health-education-c1-l29": {
        "data_table": table(["Food Group", "Example"], [
            ["Whole grains", "Brown rice, whole wheat bread"], ["Lean protein", "Chicken, beans, fish"],
        ]),
    },
    "health-education-c1-l30": {
        "data_table": table(["Sign", "Meaning"], [
            ["Dark urine", "A common sign of dehydration"],
        ]),
    },
    "health-education-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Exercise physiology", "The study of how the body responds and adapts to physical activity"],
        ]),
    },
    "health-education-c1-l32": {
        "data_table": table(["Practice", "Benefit"], [
            ["Proper warm-up", "Reduces the risk of sports injury"],
        ]),
    },
    "health-education-c1-l33": {
        "data_table": table(["Hazard", "Example"], [
            ["Air pollution", "Linked to respiratory and cardiovascular disease"],
        ]),
    },
    "health-education-c1-l34": {
        "data_table": table(["Factor", "Health Effect"], [
            ["Particulate matter", "Contributes to respiratory illness"], ["Contaminated water", "Can spread waterborne disease"],
        ]),
    },
    "health-education-c1-l35": {
        "data_table": table(["Practice", "Purpose"], [
            ["Ergonomic assessment", "Reduces workplace injury risk"],
        ]),
    },
    "health-education-c1-l36": {
        "data_table": table(["Response Type", "Feature"], [
            ["Innate immunity", "A fast, non-specific first response"], ["Adaptive immunity", "A slower, targeted, memory-forming response"],
        ]),
    },
    "health-education-c1-l37": {
        "data_table": table(["Route", "Example"], [
            ["Airborne transmission", "Influenza"], ["Contact transmission", "Common cold via surfaces"],
        ]),
    },
    "health-education-c1-l38": {
        "data_table": table(["Practice", "Benefit"], [
            ["Barrier protection", "Reduces STI transmission risk"],
        ]),
    },
    "health-education-c1-l39": {
        "data_table": table(["Method", "Type"], [
            ["Barrier method", "Physically blocks conception"], ["Hormonal method", "Prevents ovulation chemically"],
        ]),
    },
    "health-education-c1-l40": {
        "data_table": table(["Practice", "Reason"], [
            ["Prenatal vitamins", "Supports fetal development, especially folic acid intake"],
        ]),
    },
    "health-education-c1-l41": {
        "data_table": table(["Stage", "Focus"], [
            ["Adolescent health", "Growth, mental health, and risk behavior awareness"],
        ]),
    },
    "health-education-c1-l42": {
        "data_table": table(["Focus", "Detail"], [
            ["Geriatric health", "Emphasizes mobility, chronic disease, and cognitive health"],
        ]),
    },
    "health-education-c1-l43": {
        "data_table": table(["Principle", "Meaning"], [
            ["Universal design", "Creating environments accessible to people of all abilities"],
        ]),
    },
    "health-education-c1-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Deductible", "The amount paid out-of-pocket before insurance coverage begins"], ["Premium", "The regular payment made to maintain insurance coverage"],
        ]),
    },
    "health-education-c1-l45": {
        "data_table": table(["Level", "Example"], [
            ["Primary care", "General practitioners providing routine care"], ["Tertiary care", "Specialized hospital-based treatment"],
        ]),
    },
    "health-education-c1-l46": {
        "data_table": table(["Element", "Purpose"], [
            ["Clear, simple messaging", "Improves the reach and impact of a public health campaign"],
        ]),
    },
    "health-education-c1-l47": {
        "data_table": table(["Model", "Feature"], [
            ["Health Belief Model", "Predicts behavior based on perceived risk and benefit"], ["Transtheoretical Model", "Describes behavior change through stages of readiness"],
        ]),
    },
    "health-education-c1-l48": {
        "data_table": table(["Technique", "Effect"], [
            ["Deep breathing", "Activates the body's relaxation response"],
        ]),
    },
    "health-education-c1-l49": {
        "data_table": table(["Program Type", "Focus"], [
            ["School-based prevention program", "Builds refusal skills and risk awareness early"],
        ]),
    },
    "health-education-c1-l50": {
        "data_table": table(["Effect", "Detail"], [
            ["Liver damage", "A long-term risk of chronic heavy alcohol use"],
        ]),
    },
    "health-education-c1-l51": {
        "data_table": table(["Effect", "Detail"], [
            ["Lung cancer", "A major long-term risk of tobacco use"],
        ]),
    },
    "health-education-c1-l52": {
        "data_table": table(["Injury", "First Response"], [
            ["Minor burn", "Cool running water for several minutes"],
        ]),
    },
    "health-education-c1-l53": {
        "data_table": table(["Item", "Purpose"], [
            ["Emergency supply kit", "Provides essentials during a health crisis or disaster"],
        ]),
    },
    "health-education-c1-l54": {
        "data_table": table(["Resource", "Service"], [
            ["Community health center", "Provides accessible primary care, often on a sliding scale"],
        ]),
    },
    "health-education-c1-l55": {
        "data_table": table(["Practice", "Reason"], [
            ["Asking your provider questions", "Improves understanding of a diagnosis or treatment plan"],
        ]),
    },
    "health-education-c1-l56": {
        "data_table": table(["Red Flag", "Detail"], [
            ["'Miracle cure' language", "A common sign of misleading health advertising"],
        ]),
    },
    "health-education-c1-l57": {
        "data_table": table(["Practice", "Purpose"], [
            ["Situational awareness", "Reduces vulnerability to personal safety risks"],
        ]),
    },
    "health-education-c1-l58": {
        "data_table": table(["Practice", "Benefit"], [
            ["Consistent sleep schedule", "Improves sleep quality and daytime alertness"],
        ]),
    },
    "health-education-c1-l59": {
        "data_table": table(["Screening", "Recommended Frequency"], [
            ["Blood pressure check", "At least every 1-2 years for healthy adults"],
        ]),
    },
    "health-education-c1-l60": {
        "data_table": table(["Challenge", "Detail"], [
            ["Access to clean water", "A major global public health challenge in many regions"],
        ]),
    },
    "health-education-c1-l61": {
        "data_table": table(["Strategy", "Example"], [
            ["Secondary prevention", "Early screening to catch disease before symptoms worsen"],
        ]),
    },
    "health-education-c1-l62": {
        "data_table": table(["Case", "Comparison"], [
            ["Two diet approaches", "Comparing sustainability of a fad diet versus balanced eating"],
        ]),
    },
    "health-education-c1-l63": {
        "data_table": table(["Case", "Comparison"], [
            ["Two activity plans", "Comparing adherence rates of home workouts versus a gym program"],
        ]),
    },
    "health-education-c1-l64": {
        "data_table": table(["Case", "Comparison"], [
            ["Two sleep routines", "Comparing outcomes of consistent versus irregular sleep schedules"],
        ]),
    },
    "health-education-c1-l65": {
        "data_table": table(["Case", "Comparison"], [
            ["Two coping strategies", "Comparing healthy and unhealthy responses to stress"],
        ]),
    },
    "health-education-c1-l66": {
        "data_table": table(["Case", "Comparison"], [
            ["Two stress reduction techniques", "Comparing mindfulness and exercise as coping tools"],
        ]),
    },
    "health-education-c1-l67": {
        "data_table": table(["Case", "Comparison"], [
            ["Two prevention approaches", "Comparing education-based and access-based STI prevention"],
        ]),
    },
    "health-education-c1-l68": {
        "data_table": table(["Case", "Comparison"], [
            ["Two outbreak responses", "Comparing early versus delayed public health intervention"],
        ]),
    },
    "health-education-c1-l69": {
        "data_table": table(["Case", "Comparison"], [
            ["Two chronic disease programs", "Comparing lifestyle-based and medication-based management"],
        ]),
    },
    "health-education-c1-l70": {
        "data_table": table(["Case", "Comparison"], [
            ["Two vaccination campaigns", "Comparing uptake with and without community outreach"],
        ]),
    },
    "health-education-c1-l71": {
        "data_table": table(["Case", "Comparison"], [
            ["Two prevention programs", "Comparing peer-led versus lecture-based substance prevention"],
        ]),
    },
    "health-education-c1-l72": {
        "data_table": table(["Case", "Comparison"], [
            ["Two response times", "Comparing outcomes of fast versus delayed first aid response"],
        ]),
    },
    "health-education-c1-l73": {
        "data_table": table(["Case", "Comparison"], [
            ["Two safety protocols", "Comparing injury rates with and without protective equipment"],
        ]),
    },
    "health-education-c1-l74": {
        "data_table": table(["Case", "Comparison"], [
            ["Two communities", "Comparing health outcomes near versus far from industrial pollution"],
        ]),
    },
    "health-education-c1-l75": {
        "data_table": table(["Case", "Comparison"], [
            ["Two workplaces", "Comparing injury rates with and without a safety program"],
        ]),
    },
    "health-education-c1-l76": {
        "data_table": table(["Case", "Comparison"], [
            ["Two healthcare systems", "Comparing access and outcomes across two national models"],
        ]),
    },
    "health-education-c1-l77": {
        "data_table": table(["Case", "Comparison"], [
            ["Two neighborhoods", "Comparing life expectancy linked to socioeconomic disparity"],
        ]),
    },
    "health-education-c1-l78": {
        "data_table": table(["Case", "Comparison"], [
            ["Two health apps", "Comparing engagement and accuracy of two tracking tools"],
        ]),
    },
    "health-education-c1-l79": {
        "data_table": table(["Case", "Comparison"], [
            ["Two decision approaches", "Comparing shared decision-making versus provider-directed care"],
        ]),
    },
    "health-education-c1-l80": {
        "data_table": table(["Case", "Comparison"], [
            ["Two personal health plans", "Comparing a structured plan against an ad hoc approach"],
        ]),
    },
    "health-education-c1-l81": {
        "data_table": table(["Step", "Focus"], [
            ["Evaluating a health claim", "Checking a wellness claim against credible research"],
        ]),
    },
    "health-education-c1-l82": {
        "data_table": table(["Step", "Focus"], [
            ["Analyzing a diet trend", "Assessing a popular diet against nutrition science"],
        ]),
    },
    "health-education-c1-l83": {
        "data_table": table(["Step", "Focus"], [
            ["Designing an activity plan", "Building a weekly plan meeting activity guidelines"],
        ]),
    },
    "health-education-c1-l84": {
        "data_table": table(["Step", "Focus"], [
            ["Tracking sleep patterns", "Analyzing a sleep log for quality trends"],
        ]),
    },
    "health-education-c1-l85": {
        "data_table": table(["Step", "Focus"], [
            ["Researching a mental health topic", "Summarizing current evidence-based treatment approaches"],
        ]),
    },
    "health-education-c1-l86": {
        "data_table": table(["Step", "Focus"], [
            ["Testing a coping technique", "Evaluating its effect on self-reported stress"],
        ]),
    },
    "health-education-c1-l87": {
        "data_table": table(["Step", "Focus"], [
            ["Reviewing prevention program data", "Assessing effectiveness of a real health campaign"],
        ]),
    },
    "health-education-c1-l88": {
        "data_table": table(["Step", "Focus"], [
            ["Investigating an outbreak", "Tracing spread using basic epidemiological methods"],
        ]),
    },
    "health-education-c1-l89": {
        "data_table": table(["Step", "Focus"], [
            ["Researching risk factors", "Identifying modifiable risks for a chronic disease"],
        ]),
    },
    "health-education-c1-l90": {
        "data_table": table(["Step", "Focus"], [
            ["Comparing vaccine efficacy data", "Interpreting published clinical trial results"],
        ]),
    },
    "health-education-c1-l91": {
        "data_table": table(["Step", "Focus"], [
            ["Evaluating a prevention campaign", "Assessing its measured impact on behavior"],
        ]),
    },
    "health-education-c1-l92": {
        "data_table": table(["Step", "Focus"], [
            ["Reviewing a first aid protocol", "Comparing it against current best-practice guidelines"],
        ]),
    },
    "health-education-c1-l93": {
        "data_table": table(["Step", "Focus"], [
            ["Analyzing injury data", "Identifying trends in a sport's most common injuries"],
        ]),
    },
    "health-education-c1-l94": {
        "data_table": table(["Step", "Focus"], [
            ["Researching a local hazard", "Assessing a real environmental health risk"],
        ]),
    },
    "health-education-c1-l95": {
        "data_table": table(["Step", "Focus"], [
            ["Auditing workplace safety", "Assessing a work environment against safety standards"],
        ]),
    },
    "health-education-c1-l96": {
        "data_table": table(["Step", "Focus"], [
            ["Comparing health systems", "Researching outcomes across two countries' models"],
        ]),
    },
    "health-education-c1-l97": {
        "data_table": table(["Step", "Focus"], [
            ["Researching health disparities", "Identifying causes of unequal health outcomes"],
        ]),
    },
    "health-education-c1-l98": {
        "data_table": table(["Step", "Focus"], [
            ["Evaluating a health app", "Assessing its accuracy and privacy practices"],
        ]),
    },
    "health-education-c1-l99": {
        "data_table": table(["Step", "Focus"], [
            ["Practicing shared decision-making", "Weighing treatment options with provider input"],
        ]),
    },
    "health-education-c1-l100": {
        "data_table": table(["Step", "Focus"], [
            ["Writing a personal health plan", "Setting concrete, trackable wellness goals"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Health Education lessons (completing 100/100).")


if __name__ == "__main__":
    main()
