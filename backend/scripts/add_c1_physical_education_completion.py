#!/usr/bin/env python3
"""Depth pass, C1 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 69 C1 PE & Self-Defense lessons
not covered by the earlier breadth-first batch. Brings the subject to
full 70/70 coverage.

Note: lesson ids l1-l60 use the prefix "physical-education-and-self-defense-c1-",
while l61-l70 use "physical-education-self-defense-c1-" (no "and-"). Both
forms are preserved exactly as they exist in level_c1.json.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_physical_education_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "physical-education-and-self-defense-c1-l1": {
        "data_table": table(["Component", "Focus"], [
            ["Cardiorespiratory fitness", "The heart and lungs' ability to sustain exercise"], ["Muscular strength", "The maximum force a muscle can produce"],
        ]),
    },
    "physical-education-and-self-defense-c1-l2": {
        "data_table": table(["Principle", "Meaning"], [
            ["Awareness first", "Avoiding a threat is more effective than fighting one"],
        ]),
    },
    "physical-education-and-self-defense-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Biomechanics", "The study of mechanical laws applied to human movement"],
        ]),
    },
    "physical-education-and-self-defense-c1-l5": {
        "data_table": table(["Concept", "Meaning"], [
            ["Sports psychology", "Studies mental factors that influence athletic performance"],
        ]),
    },
    "physical-education-and-self-defense-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Progressive overload", "Gradually increasing training demand to build strength"],
        ]),
    },
    "physical-education-and-self-defense-c1-l7": {
        "data_table": table(["Practice", "Benefit"], [
            ["Proper warm-up", "Prepares muscles and joints, reducing injury risk"],
        ]),
    },
    "physical-education-and-self-defense-c1-l8": {
        "data_table": table(["Nutrient", "Role in Performance"], [
            ["Carbohydrates", "Primary fuel source for high-intensity exercise"],
        ]),
    },
    "physical-education-and-self-defense-c1-l9": {
        "data_table": table(["Skill", "Purpose"], [
            ["Clear feedback", "Helps athletes correct technique effectively"],
        ]),
    },
    "physical-education-and-self-defense-c1-l10": {
        "data_table": table(["Role", "Responsibility"], [
            ["Referee", "Enforces rules and maintains fair play during a game"],
        ]),
    },
    "physical-education-and-self-defense-c1-l11": {
        "data_table": table(["Principle", "Meaning"], [
            ["Adaptive PE", "Modifies activities so students with disabilities can participate fully"],
        ]),
    },
    "physical-education-and-self-defense-c1-l12": {
        "data_table": table(["Stage", "Feature"], [
            ["Cognitive stage", "Learner consciously thinks through each movement"],
        ]),
    },
    "physical-education-and-self-defense-c1-l13": {
        "data_table": table(["Phase", "Focus"], [
            ["Base phase", "Builds general fitness before intense training"], ["Peak phase", "Maximizes performance for competition"],
        ]),
    },
    "physical-education-and-self-defense-c1-l14": {
        "data_table": table(["Principle", "Meaning"], [
            ["Proportional response", "Using only the force necessary to escape danger"],
        ]),
    },
    "physical-education-and-self-defense-c1-l15": {
        "data_table": table(["Art", "Origin"], [
            ["Karate", "Okinawa, Japan"], ["Judo", "Japan, developed by Jigoro Kano"],
        ]),
    },
    "physical-education-and-self-defense-c1-l16": {
        "data_table": table(["Strategy", "Example"], [
            ["Zone defense", "Players guard an area rather than a specific opponent"],
        ]),
    },
    "physical-education-and-self-defense-c1-l17": {
        "data_table": table(["Sport", "Key Technique"], [
            ["Tennis", "Consistent serve toss placement"], ["Swimming", "Efficient stroke rotation and breathing"],
        ]),
    },
    "physical-education-and-self-defense-c1-l18": {
        "data_table": table(["Test", "Measures"], [
            ["VO2 max test", "Aerobic capacity"], ["1-rep max test", "Maximum strength"],
        ]),
    },
    "physical-education-and-self-defense-c1-l19": {
        "data_table": table(["Population", "Consideration"], [
            ["Older adults", "Emphasize balance and joint-friendly movement"], ["Pregnant individuals", "Avoid high-impact and supine exercises later in pregnancy"],
        ]),
    },
    "physical-education-and-self-defense-c1-l20": {
        "data_table": table(["Role", "Responsibility"], [
            ["Athletic director", "Oversees a school or organization's sports programs"],
        ]),
    },
    "physical-education-and-self-defense-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Cardiorespiratory fitness", "The efficiency of the heart and lungs during sustained activity"],
        ]),
    },
    "physical-education-and-self-defense-c1-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Muscular endurance", "The ability of a muscle to sustain repeated contractions over time"],
        ]),
    },
    "physical-education-and-self-defense-c1-l23": {
        "data_table": table(["Type", "Example"], [
            ["Static stretching", "Holding a stretch position for a period of time"], ["Dynamic stretching", "Moving through a range of motion actively"],
        ]),
    },
    "physical-education-and-self-defense-c1-l24": {
        "data_table": table(["Method", "Measures"], [
            ["Skinfold calipers", "Estimates body fat percentage from skin thickness"],
        ]),
    },
    "physical-education-and-self-defense-c1-l25": {
        "data_table": table(["Phase", "Purpose"], [
            ["Warm-up", "Raises heart rate and prepares muscles gradually"], ["Cool-down", "Gradually lowers heart rate after exercise"],
        ]),
    },
    "physical-education-and-self-defense-c1-l26": {
        "data_table": table(["Principle", "Meaning"], [
            ["Specificity", "Training adaptations match the specific demands placed on the body"],
        ]),
    },
    "physical-education-and-self-defense-c1-l27": {
        "data_table": table(["Method", "Feature"], [
            ["Interval training", "Alternates high-intensity bursts with recovery periods"],
        ]),
    },
    "physical-education-and-self-defense-c1-l28": {
        "data_table": table(["Drill", "Trains"], [
            ["Ladder drills", "Foot speed and coordination"],
        ]),
    },
    "physical-education-and-self-defense-c1-l29": {
        "data_table": table(["Exercise", "Trains"], [
            ["Single-leg stance", "Proprioception and core stability"],
        ]),
    },
    "physical-education-and-self-defense-c1-l30": {
        "data_table": table(["Technique", "Purpose"], [
            ["Visualization", "Mentally rehearses performance to build confidence"],
        ]),
    },
    "physical-education-and-self-defense-c1-l31": {
        "data_table": table(["Goal Type", "Example"], [
            ["SMART goal", "Specific, Measurable, Achievable, Relevant, Time-bound"],
        ]),
    },
    "physical-education-and-self-defense-c1-l32": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Habit stacking", "Attaches a new exercise habit to an existing routine"],
        ]),
    },
    "physical-education-and-self-defense-c1-l33": {
        "data_table": table(["Sign", "Meaning"], [
            ["Dark urine color", "A common indicator of dehydration"],
        ]),
    },
    "physical-education-and-self-defense-c1-l34": {
        "data_table": table(["Macronutrient", "Role"], [
            ["Protein", "Supports muscle repair and growth"], ["Fat", "Provides sustained, slow-burning energy"],
        ]),
    },
    "physical-education-and-self-defense-c1-l35": {
        "data_table": table(["Timing", "Purpose"], [
            ["Pre-workout", "Provides accessible energy for the session"], ["Post-workout", "Supports recovery and muscle repair"],
        ]),
    },
    "physical-education-and-self-defense-c1-l36": {
        "data_table": table(["Injury", "Cause"], [
            ["Shin splints", "Repetitive stress on the lower leg, often from running"],
        ]),
    },
    "physical-education-and-self-defense-c1-l37": {
        "data_table": table(["Letter", "Step"], [
            ["R", "Rest"], ["I", "Ice"], ["C", "Compression"], ["E", "Elevation"],
        ]),
    },
    "physical-education-and-self-defense-c1-l38": {
        "data_table": table(["Practice", "Benefit"], [
            ["Dynamic stretching before activity", "Improves range of motion and reduces strain risk"],
        ]),
    },
    "physical-education-and-self-defense-c1-l39": {
        "data_table": table(["Skill", "Purpose"], [
            ["Active listening", "Helps a coach understand an athlete's concerns"],
        ]),
    },
    "physical-education-and-self-defense-c1-l40": {
        "data_table": table(["Step", "Purpose"], [
            ["Breaking a skill into parts", "Makes complex movements easier to learn"],
        ]),
    },
    "physical-education-and-self-defense-c1-l41": {
        "data_table": table(["Skill", "Purpose"], [
            ["Positioning", "Keeps the official in a good vantage point to make calls"],
        ]),
    },
    "physical-education-and-self-defense-c1-l42": {
        "data_table": table(["Example", "Adaptation"], [
            ["Wheelchair basketball", "Adapts standard basketball rules for wheelchair users"],
        ]),
    },
    "physical-education-and-self-defense-c1-l43": {
        "data_table": table(["Practice", "Benefit"], [
            ["Offering activity modifications", "Lets every student participate at their ability level"],
        ]),
    },
    "physical-education-and-self-defense-c1-l44": {
        "data_table": table(["Stage", "Feature"], [
            ["Fundamental movement stage", "Develops basic skills like running, jumping, and throwing"],
        ]),
    },
    "physical-education-and-self-defense-c1-l45": {
        "data_table": table(["Cycle", "Duration"], [
            ["Macrocycle", "A full training year or season"], ["Microcycle", "A single training week"],
        ]),
    },
    "physical-education-and-self-defense-c1-l46": {
        "data_table": table(["Practice", "Benefit"], [
            ["Situational awareness", "Notices potential threats before they escalate"],
        ]),
    },
    "physical-education-and-self-defense-c1-l47": {
        "data_table": table(["Technique", "Target"], [
            ["Palm strike", "Effective for close-range defense without risking hand injury"],
        ]),
    },
    "physical-education-and-self-defense-c1-l48": {
        "data_table": table(["Technique", "Purpose"], [
            ["Wrist escape", "Breaks free from a grabbed wrist using leverage"],
        ]),
    },
    "physical-education-and-self-defense-c1-l49": {
        "data_table": table(["Era", "Feature"], [
            ["Modern boxing", "Codified under the Marquess of Queensberry rules in the 19th century"],
        ]),
    },
    "physical-education-and-self-defense-c1-l50": {
        "data_table": table(["Style", "Feature"], [
            ["Freestyle wrestling", "Allows the use of legs for holds and takedowns"],
        ]),
    },
    "physical-education-and-self-defense-c1-l51": {
        "data_table": table(["Principle", "Meaning"], [
            ["Maximum efficiency, minimum effort", "A core judo principle for using an opponent's force against them"],
        ]),
    },
    "physical-education-and-self-defense-c1-l52": {
        "data_table": table(["Principle", "Meaning"], [
            ["Kime", "Focused power delivered at the moment of impact in karate"],
        ]),
    },
    "physical-education-and-self-defense-c1-l53": {
        "data_table": table(["Concept", "Meaning"], [
            ["Ground fighting", "BJJ's emphasis on controlling an opponent from the ground"],
        ]),
    },
    "physical-education-and-self-defense-c1-l54": {
        "data_table": table(["Sport", "Key Rule"], [
            ["Basketball", "24-second shot clock in professional play"], ["Soccer", "Offside rule restricts attacker positioning"],
        ]),
    },
    "physical-education-and-self-defense-c1-l55": {
        "data_table": table(["Sport", "Key Technique"], [
            ["Tennis", "Proper grip affects shot control and power"], ["Swimming", "Streamlined body position reduces drag"],
        ]),
    },
    "physical-education-and-self-defense-c1-l56": {
        "data_table": table(["Principle", "Meaning"], [
            ["Impartiality", "An official must apply rules the same way to all participants"],
        ]),
    },
    "physical-education-and-self-defense-c1-l57": {
        "data_table": table(["Step", "Purpose"], [
            ["Assessing participant needs", "Shapes activity choices for a recreation program"],
        ]),
    },
    "physical-education-and-self-defense-c1-l58": {
        "data_table": table(["Life Stage", "Focus"], [
            ["Childhood", "Fundamental movement skill development"], ["Older adulthood", "Balance, mobility, and fall prevention"],
        ]),
    },
    "physical-education-and-self-defense-c1-l59": {
        "data_table": table(["Career", "Focus"], [
            ["Sports agent", "Represents athletes in contracts and endorsements"],
        ]),
    },
    "physical-education-and-self-defense-c1-l60": {
        "data_table": table(["Activity", "Benefit"], [
            ["Walking", "Low-impact activity accessible to most fitness levels"],
        ]),
    },
    "physical-education-self-defense-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Building a balanced routine", "Combining cardio, strength, and flexibility work"],
        ]),
    },
    "physical-education-self-defense-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Practicing a defensive response", "Applying an escape technique to a simulated grab"],
        ]),
    },
    "physical-education-self-defense-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Explaining a training adaptation", "Describing why regular cardio lowers resting heart rate"],
        ]),
    },
    "physical-education-self-defense-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a movement", "Identifying inefficient joint angles in a squat"],
        ]),
    },
    "physical-education-self-defense-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Applying a mental technique", "Using visualization before a competitive event"],
        ]),
    },
    "physical-education-self-defense-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Designing a strength program", "Applying progressive overload across weeks of training"],
        ]),
    },
    "physical-education-self-defense-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Reducing injury risk", "Building a proper warm-up for a specific sport"],
        ]),
    },
    "physical-education-self-defense-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Planning fueling strategy", "Timing carbohydrate intake around a workout"],
        ]),
    },
    "physical-education-self-defense-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Giving effective feedback", "Correcting an athlete's technique constructively"],
        ]),
    },
    "physical-education-self-defense-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Applying officiating rules", "Making a fair call in a simulated game scenario"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Physical Education & Self-Defense: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Physical Education & Self-Defense lessons (completing 70/70).")


if __name__ == "__main__":
    main()
