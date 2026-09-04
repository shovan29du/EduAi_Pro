#!/usr/bin/env python3
"""Depth pass, C2 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 69 C2 PE lessons not covered
by the earlier breadth-first batch. Brings C2 Physical Education &
Self-Defense to full 70/70 coverage.

Lesson ID quirk (matches the C1 subject): l1-l60 use the prefix
"physical-education-and-self-defense-c2-", while l61-l70 use the
shorter "physical-education-self-defense-c2-" (no "and"). l61-l70 are
"Worked Analysis" companions to l1-l10. l3 was already completed by
an earlier breadth-first batch, so its data_table is hard-coded here
for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_physical_education_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "physical-education-and-self-defense-c2-l1": {
        "data_table": table(["Skill", "Feature"], [
            ["Applied self-defense", "Combines awareness, avoidance, and physical technique for personal safety"],
        ]),
    },
    "physical-education-and-self-defense-c2-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Sports science", "Applies physiology, biomechanics, and psychology to athletic performance"],
        ]),
    },
    "physical-education-and-self-defense-c2-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Movement pattern analysis", "Identifies inefficiencies or injury risk in fundamental movement"],
        ]),
    },
    "physical-education-and-self-defense-c2-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Goal setting in sport", "Specific, measurable goals improve focus and training adherence"],
        ]),
    },
    "physical-education-and-self-defense-c2-l6": {
        "data_table": table(["Principle", "Detail"], [
            ["Program design", "Balances specificity, overload, and recovery for the athlete's goals"],
        ]),
    },
    "physical-education-and-self-defense-c2-l7": {
        "data_table": table(["Injury", "Cause"], [
            ["Sprain", "Stretching or tearing of a ligament"],
            ["Strain", "Stretching or tearing of a muscle or tendon"],
        ]),
    },
    "physical-education-and-self-defense-c2-l8": {
        "data_table": table(["Nutrient", "Role"], [
            ["Carbohydrates", "Primary fuel source for moderate-to-high intensity exercise"],
        ]),
    },
    "physical-education-and-self-defense-c2-l9": {
        "data_table": table(["Practice", "Purpose"], [
            ["Constructive feedback", "Reinforces correct technique while guiding improvement"],
        ]),
    },
    "physical-education-and-self-defense-c2-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Fair play", "Following both the letter and spirit of a sport's rules"],
        ]),
    },
    "physical-education-and-self-defense-c2-l11": {
        "data_table": table(["Principle", "Detail"], [
            ["Inclusive activity design", "Adapts rules and equipment so participants of varied ability can take part"],
        ]),
    },
    "physical-education-and-self-defense-c2-l12": {
        "data_table": table(["Stage", "Feature"], [
            ["Cognitive stage", "Learner focuses on understanding the basic requirements of a skill"],
            ["Autonomous stage", "Skill becomes largely automatic, requiring little conscious thought"],
        ]),
    },
    "physical-education-and-self-defense-c2-l13": {
        "data_table": table(["Cycle", "Duration"], [
            ["Macrocycle", "A full training year or season"],
            ["Mesocycle", "Weeks to months within a macrocycle"],
            ["Microcycle", "A single training week"],
        ]),
    },
    "physical-education-and-self-defense-c2-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["De-escalation", "Verbal and postural strategies to reduce tension before conflict escalates"],
        ]),
    },
    "physical-education-and-self-defense-c2-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Martial arts discipline", "Emphasizes respect, self-control, and perseverance alongside technique"],
        ]),
    },
    "physical-education-and-self-defense-c2-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Positional play", "Structured team formations improve spacing and coordination"],
        ]),
    },
    "physical-education-and-self-defense-c2-l17": {
        "data_table": table(["Practice", "Purpose"], [
            ["Technique refinement", "Repeated, focused feedback narrows the gap toward correct execution"],
        ]),
    },
    "physical-education-and-self-defense-c2-l18": {
        "data_table": table(["Test", "Measures"], [
            ["Beep test", "Aerobic capacity via incremental shuttle running"],
        ]),
    },
    "physical-education-and-self-defense-c2-l19": {
        "data_table": table(["Life Stage", "Consideration"], [
            ["Older adulthood", "Emphasizes balance and joint-friendly, low-impact activity"],
        ]),
    },
    "physical-education-and-self-defense-c2-l20": {
        "data_table": table(["Element", "Purpose"], [
            ["Recreation program planning", "Balances accessibility, safety, and enjoyment for participants"],
        ]),
    },
    "physical-education-and-self-defense-c2-l21": {
        "data_table": table(["Metric", "Meaning"], [
            ["VO2 max", "Maximum rate of oxygen consumption during intense exercise"],
        ]),
    },
    "physical-education-and-self-defense-c2-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Periodized resistance program", "Systematically varies intensity and volume to optimize strength gains"],
        ]),
    },
    "physical-education-and-self-defense-c2-l23": {
        "data_table": table(["Technique", "Mechanism"], [
            ["PNF stretching", "Alternates muscle contraction and relaxation to increase range of motion"],
        ]),
    },
    "physical-education-and-self-defense-c2-l24": {
        "data_table": table(["Method", "Measures"], [
            ["Skinfold measurement", "Estimates body fat percentage from subcutaneous fat thickness"],
        ]),
    },
    "physical-education-and-self-defense-c2-l25": {
        "data_table": table(["Component", "Purpose"], [
            ["Dynamic warm-up", "Raises heart rate and prepares muscles through movement, not static holds"],
        ]),
    },
    "physical-education-and-self-defense-c2-l26": {
        "data_table": table(["Principle", "Detail"], [
            ["Progressive overload", "Gradually increasing training demand drives continued strength adaptation"],
        ]),
    },
    "physical-education-and-self-defense-c2-l27": {
        "data_table": table(["Adaptation", "Effect"], [
            ["HIIT", "Improves both aerobic and anaerobic capacity in shorter training sessions"],
        ]),
    },
    "physical-education-and-self-defense-c2-l28": {
        "data_table": table(["Drill Type", "Focus"], [
            ["Reactive agility drill", "Trains quick decision-making in response to an unpredictable stimulus"],
        ]),
    },
    "physical-education-and-self-defense-c2-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Neuromuscular balance training", "Improves proprioception and joint stability to reduce injury risk"],
        ]),
    },
    "physical-education-and-self-defense-c2-l30": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Pre-performance routine", "Reduces competitive anxiety through consistent, controlled preparation"],
        ]),
    },
    "physical-education-and-self-defense-c2-l31": {
        "data_table": table(["Letter", "Meaning"], [
            ["S", "Specific"], ["M", "Measurable"], ["A", "Achievable"], ["R", "Relevant"], ["T", "Time-bound"],
        ]),
    },
    "physical-education-and-self-defense-c2-l32": {
        "data_table": table(["Stage", "Detail"], [
            ["Transtheoretical model stage", "Behavior change progresses through stages from precontemplation to maintenance"],
        ]),
    },
    "physical-education-and-self-defense-c2-l33": {
        "data_table": table(["Electrolyte", "Role"], [
            ["Sodium", "Maintains fluid balance and supports nerve/muscle function during exertion"],
        ]),
    },
    "physical-education-and-self-defense-c2-l34": {
        "data_table": table(["Phase", "Nutrition Focus"], [
            ["Competition phase", "Prioritizes readily available energy and hydration timing"],
        ]),
    },
    "physical-education-and-self-defense-c2-l35": {
        "data_table": table(["Window", "Purpose"], [
            ["Post-exercise recovery window", "Prioritizes protein and carbohydrate intake to support repair and glycogen restoration"],
        ]),
    },
    "physical-education-and-self-defense-c2-l36": {
        "data_table": table(["Tool", "Purpose"], [
            ["Movement screen", "Identifies asymmetries or limitations that raise injury risk"],
        ]),
    },
    "physical-education-and-self-defense-c2-l37": {
        "data_table": table(["Stage", "Criteria"], [
            ["Return-to-play protocol", "Progresses through graded activity stages before full competitive clearance"],
        ]),
    },
    "physical-education-and-self-defense-c2-l38": {
        "data_table": table(["Type", "Best Use"], [
            ["Dynamic stretching", "Better suited before activity to prepare muscles for movement"],
            ["Static stretching", "Better suited after activity to improve long-term flexibility"],
        ]),
    },
    "physical-education-and-self-defense-c2-l39": {
        "data_table": table(["Practice", "Purpose"], [
            ["Positive reinforcement", "Increases the likelihood of a desired behavior recurring"],
        ]),
    },
    "physical-education-and-self-defense-c2-l40": {
        "data_table": table(["Approach", "Detail"], [
            ["Constraints-led approach", "Shapes skill learning by manipulating task, environment, and individual constraints"],
        ]),
    },
    "physical-education-and-self-defense-c2-l41": {
        "data_table": table(["Skill", "Purpose"], [
            ["Game management", "Balances rule enforcement with maintaining flow and player safety"],
        ]),
    },
    "physical-education-and-self-defense-c2-l42": {
        "data_table": table(["System", "Purpose"], [
            ["Classification system", "Groups para-athletes to ensure fair competition by functional ability"],
        ]),
    },
    "physical-education-and-self-defense-c2-l43": {
        "data_table": table(["Principle", "Detail"], [
            ["Universal Design for Learning", "Offers multiple means of engagement, representation, and action for all learners"],
        ]),
    },
    "physical-education-and-self-defense-c2-l44": {
        "data_table": table(["Stage", "Feature"], [
            ["Associative stage", "Learner refines technique through practice and feedback after initial understanding"],
        ]),
    },
    "physical-education-and-self-defense-c2-l45": {
        "data_table": table(["Model", "Feature"], [
            ["Block periodization", "Concentrates training on a narrow set of qualities in sequential blocks"],
            ["Undulating periodization", "Varies intensity and volume frequently within a shorter timeframe"],
        ]),
    },
    "physical-education-and-self-defense-c2-l46": {
        "data_table": table(["Strategy", "Detail"], [
            ["Situational de-escalation", "Reads context and body language to reduce risk before physical confrontation"],
        ]),
    },
    "physical-education-and-self-defense-c2-l47": {
        "data_table": table(["Element", "Purpose"], [
            ["Striking combination", "Chains techniques to create openings and control tempo"],
        ]),
    },
    "physical-education-and-self-defense-c2-l48": {
        "data_table": table(["Position", "Advantage"], [
            ["Mount", "Dominant grappling position with maximal control and striking options"],
        ]),
    },
    "physical-education-and-self-defense-c2-l49": {
        "data_table": table(["Tactic", "Purpose"], [
            ["Boxing footwork", "Controls range and angle to create advantage over an opponent"],
        ]),
    },
    "physical-education-and-self-defense-c2-l50": {
        "data_table": table(["Tactic", "Purpose"], [
            ["Wrestling takedown setup", "Uses feints and level changes to create an opening for a takedown"],
        ]),
    },
    "physical-education-and-self-defense-c2-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Combination throw", "Chains judo throws together when the first attempt is defended"],
        ]),
    },
    "physical-education-and-self-defense-c2-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Kata analysis", "Breaks down prearranged forms to reveal practical self-defense applications"],
        ]),
    },
    "physical-education-and-self-defense-c2-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Submission chain", "Links transitions between attacks when an opponent defends the first"],
        ]),
    },
    "physical-education-and-self-defense-c2-l54": {
        "data_table": table(["Sport", "Tactical System"], [
            ["Basketball", "Pick-and-roll creates mismatches through coordinated screening"],
            ["Soccer", "Formation shapes spacing and defensive/offensive transitions"],
        ]),
    },
    "physical-education-and-self-defense-c2-l55": {
        "data_table": table(["Sport", "Strategic Focus"], [
            ["Tennis", "Shot placement and court positioning control rally outcomes"],
            ["Swimming", "Pacing strategy manages energy across race distance"],
        ]),
    },
    "physical-education-and-self-defense-c2-l56": {
        "data_table": table(["Technology", "Purpose"], [
            ["Video review", "Allows officials to verify close or contested calls after the fact"],
        ]),
    },
    "physical-education-and-self-defense-c2-l57": {
        "data_table": table(["Metric", "Purpose"], [
            ["Program evaluation metric", "Assesses whether a recreational program meets participant needs"],
        ]),
    },
    "physical-education-and-self-defense-c2-l58": {
        "data_table": table(["Condition", "Exercise Approach"], [
            ["Type 2 diabetes", "Regular moderate exercise improves insulin sensitivity"],
        ]),
    },
    "physical-education-and-self-defense-c2-l59": {
        "data_table": table(["Area", "Focus"], [
            ["Facility operations", "Coordinates scheduling, maintenance, and safety compliance"],
        ]),
    },
    "physical-education-and-self-defense-c2-l60": {
        "data_table": table(["Component", "Purpose"], [
            ["Personal wellness plan", "Integrates fitness, nutrition, recovery, and mental health goals"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Energy System", "Duration Used"], [
    ["ATP-PCr (Phosphagen)", "0-10 seconds, high intensity"],
    ["Anaerobic glycolysis", "10 seconds-2 minutes"],
    ["Aerobic system", "2+ minutes, endurance"],
])

# l61-l70 use the shorter prefix and are "Worked Analysis" companions to l1-l10.
WORKED_ANALYSIS_MAP = {61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"physical-education-and-self-defense-c2-l{base_n}"
    worked_key = f"physical-education-self-defense-c2-l{worked_n}"
    if base_key in CHARTS:
        CHARTS[worked_key] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[worked_key] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Physical Education & Self-Defense: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Physical Education & Self-Defense lessons (completing 70/70).")


if __name__ == "__main__":
    main()
