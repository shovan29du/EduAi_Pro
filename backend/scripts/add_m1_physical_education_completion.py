#!/usr/bin/env python3
"""Depth pass, M1 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the 99 M1 PE lessons not covered
by the earlier breadth-first batch. Brings M1 Physical Education &
Self-Defense to full 120/120 coverage.

Lesson ID quirk (matches the C1/C2 subject): l1-l100 use the prefix
"physical-education-and-self-defense-m1-", while l101-l120 use the
shorter "physical-education-self-defense-m1-" (no "and"). l101-l120
are "Worked Analysis" companions reusing the data_table of l1-l20
(direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_physical_education_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "physical-education-and-self-defense-m1-l1": {
        "data_table": table(["Field", "Feature"], [
            ["Sports science", "Applies physiology, biomechanics, and psychology to athletic performance"],
        ]),
    },
    "physical-education-and-self-defense-m1-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["Performance management", "Systematically tracks and adjusts athlete development over time"],
        ]),
    },
    "physical-education-and-self-defense-m1-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Biomechanics", "Applies mechanical principles to analyze and improve human movement"],
        ]),
    },
    "physical-education-and-self-defense-m1-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Sports psychology", "Examines mental factors influencing athletic performance and motivation"],
        ]),
    },
    "physical-education-and-self-defense-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Strength and conditioning", "Systematically develops physical qualities underlying athletic performance"],
        ]),
    },
    "physical-education-and-self-defense-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["Injury epidemiology", "Tracks injury incidence patterns to inform prevention strategy"],
        ]),
    },
    "physical-education-and-self-defense-m1-l8": {
        "data_table": table(["Concept", "Detail"], [
            ["Sports nutrition science", "Applies evidence-based fueling strategy to optimize athletic performance"],
        ]),
    },
    "physical-education-and-self-defense-m1-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Coaching science", "Applies research evidence to structure effective athlete development"],
        ]),
    },
    "physical-education-and-self-defense-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Sport governance", "Rule-making bodies establish and enforce standards across competitive sport"],
        ]),
    },
    "physical-education-and-self-defense-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Adaptive physical activity", "Modifies movement programming to include participants of varied ability"],
        ]),
    },
    "physical-education-and-self-defense-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Motor learning", "Studies how practice and feedback shape the acquisition of movement skill"],
        ]),
    },
    "physical-education-and-self-defense-m1-l13": {
        "data_table": table(["Cycle", "Duration"], [
            ["Macrocycle", "A full training year or season"],
            ["Microcycle", "A single training week"],
        ]),
    },
    "physical-education-and-self-defense-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Self-defense law", "Legal justification for force generally requires proportionality to the threat"],
        ]),
    },
    "physical-education-and-self-defense-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Martial arts philosophy", "Traditional systems often pair physical technique with ethical discipline"],
        ]),
    },
    "physical-education-and-self-defense-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Tactics analysis", "Breaks down strategic patterns underlying successful competitive play"],
        ]),
    },
    "physical-education-and-self-defense-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Technique analysis", "Examines movement mechanics to identify efficiency and error"],
        ]),
    },
    "physical-education-and-self-defense-m1-l18": {
        "data_table": table(["Test", "Measures"], [
            ["Beep test", "Aerobic capacity via incremental shuttle running"],
        ]),
    },
    "physical-education-and-self-defense-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Clinical exercise physiology", "Applies exercise science to manage and rehabilitate medical conditions"],
        ]),
    },
    "physical-education-and-self-defense-m1-l20": {
        "data_table": table(["Concept", "Detail"], [
            ["Recreation management", "Coordinates programming, facilities, and staffing for sport and leisure services"],
        ]),
    },
    "physical-education-and-self-defense-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Neuromuscular adaptation", "Resistance training improves strength partly through neural efficiency before muscle growth"],
        ]),
    },
    "physical-education-and-self-defense-m1-l22": {
        "data_table": table(["Fiber Type", "Feature"], [
            ["Type I (slow-twitch)", "Fatigue-resistant, suited to endurance activity"],
            ["Type II (fast-twitch)", "Powerful but fatigues quickly, suited to explosive activity"],
        ]),
    },
    "physical-education-and-self-defense-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Elite cardiorespiratory physiology", "Trained athletes exhibit distinctive cardiac and pulmonary adaptations"],
        ]),
    },
    "physical-education-and-self-defense-m1-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Lactate threshold", "The exercise intensity at which lactate accumulates faster than it is cleared"],
        ]),
    },
    "physical-education-and-self-defense-m1-l25": {
        "data_table": table(["Metric", "Meaning"], [
            ["VO2 max", "Maximum rate of oxygen consumption during intense exercise"],
        ]),
    },
    "physical-education-and-self-defense-m1-l26": {
        "data_table": table(["Model", "Feature"], [
            ["Block periodization", "Concentrates training on a narrow set of qualities in sequential blocks"],
        ]),
    },
    "physical-education-and-self-defense-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Interference effect", "Simultaneous strength and endurance training can blunt each other's adaptations"],
        ]),
    },
    "physical-education-and-self-defense-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Altitude training", "Reduced oxygen availability stimulates adaptations that can boost performance at sea level"],
        ]),
    },
    "physical-education-and-self-defense-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Heat acclimatization", "Repeated heat exposure improves the body's thermoregulatory efficiency"],
        ]),
    },
    "physical-education-and-self-defense-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Kinetic chain", "Force and motion transfer sequentially through connected body segments"],
        ]),
    },
    "physical-education-and-self-defense-m1-l31": {
        "data_table": table(["Technology", "Use"], [
            ["Motion capture", "Records precise movement data to analyze and refine athletic technique"],
        ]),
    },
    "physical-education-and-self-defense-m1-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Ground reaction force", "The force the ground exerts back on the body during movement"],
        ]),
    },
    "physical-education-and-self-defense-m1-l33": {
        "data_table": table(["Stage", "Feature"], [
            ["Cognitive stage", "Learner focuses on understanding the basic requirements of a skill"],
            ["Autonomous stage", "Skill becomes largely automatic, requiring little conscious thought"],
        ]),
    },
    "physical-education-and-self-defense-m1-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Dynamical systems theory", "Views motor skill as an emergent property of interacting body and environment constraints"],
        ]),
    },
    "physical-education-and-self-defense-m1-l35": {
        "data_table": table(["Approach", "Detail"], [
            ["Ecological dynamics", "Skill acquisition is shaped directly by perception-action coupling with the environment"],
        ]),
    },
    "physical-education-and-self-defense-m1-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["Flow state", "A state of full immersion and effortless focus during peak performance"],
        ]),
    },
    "physical-education-and-self-defense-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Mental toughness", "The capacity to maintain performance and composure under competitive pressure"],
        ]),
    },
    "physical-education-and-self-defense-m1-l38": {
        "data_table": table(["Technique", "Purpose"], [
            ["Mental rehearsal", "Visualizing successful performance to reinforce neural and psychological preparation"],
        ]),
    },
    "physical-education-and-self-defense-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Overtraining syndrome", "Chronic excessive training without recovery impairs performance and health"],
        ]),
    },
    "physical-education-and-self-defense-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Load management", "Balances training stress with recovery to minimize injury risk"],
        ]),
    },
    "physical-education-and-self-defense-m1-l41": {
        "data_table": table(["Stage", "Criteria"], [
            ["Return-to-play protocol", "Progresses through graded activity stages before full competitive clearance"],
        ]),
    },
    "physical-education-and-self-defense-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Rehabilitation science", "Applies evidence-based progressive loading to restore function after injury"],
        ]),
    },
    "physical-education-and-self-defense-m1-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["Concussion management", "Requires structured cognitive and physical rest before graded return to activity"],
        ]),
    },
    "physical-education-and-self-defense-m1-l44": {
        "data_table": table(["Phase", "Nutrition Focus"], [
            ["Competition phase", "Prioritizes readily available energy and hydration timing"],
        ]),
    },
    "physical-education-and-self-defense-m1-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Thermoregulation in sport", "Sweat rate and fluid replacement strategy must match exercise intensity and heat"],
        ]),
    },
    "physical-education-and-self-defense-m1-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Ergogenic aid", "A substance or method claimed to enhance athletic performance, with varying evidence"],
        ]),
    },
    "physical-education-and-self-defense-m1-l47": {
        "data_table": table(["Method", "Measures"], [
            ["DEXA scan", "Precisely measures body composition including bone density"],
        ]),
    },
    "physical-education-and-self-defense-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Sport-specific program design", "Training demands should mirror the movement patterns of the target sport"],
        ]),
    },
    "physical-education-and-self-defense-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Plyometric training", "Uses rapid stretch-shortening cycles to develop explosive power"],
        ]),
    },
    "physical-education-and-self-defense-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Speed and agility training", "Develops rapid directional change alongside raw sprint velocity"],
        ]),
    },
    "physical-education-and-self-defense-m1-l51": {
        "data_table": table(["Technology", "Use"], [
            ["Wearable GPS tracker", "Monitors athlete workload and movement patterns in real time"],
        ]),
    },
    "physical-education-and-self-defense-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Sports data analytics", "Uses statistical modeling to evaluate performance and inform strategy"],
        ]),
    },
    "physical-education-and-self-defense-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Talent identification", "Uses physical and skill markers to project long-term athletic potential"],
        ]),
    },
    "physical-education-and-self-defense-m1-l54": {
        "data_table": table(["System", "Purpose"], [
            ["Classification system", "Groups para-athletes to ensure fair competition by functional ability"],
        ]),
    },
    "physical-education-and-self-defense-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Athlete-centered coaching", "Shapes decision-making and feedback around the individual athlete's needs"],
        ]),
    },
    "physical-education-and-self-defense-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Anti-doping policy", "Combines testing, education, and sanctions to preserve fair competition"],
        ]),
    },
    "physical-education-and-self-defense-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Performance enhancement ethics", "Weighs fairness and athlete health against competitive advantage"],
        ]),
    },
    "physical-education-and-self-defense-m1-l58": {
        "data_table": table(["Condition", "Exercise Approach"], [
            ["Type 2 diabetes", "Regular moderate exercise improves insulin sensitivity"],
        ]),
    },
    "physical-education-and-self-defense-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Risk stratification", "Screens participants for medical risk before clinical exercise testing"],
        ]),
    },
    "physical-education-and-self-defense-m1-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Gait analysis", "Studies the biomechanics of walking and running to identify inefficiency or injury risk"],
        ]),
    },
    "physical-education-and-self-defense-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Overuse injury", "Accumulates from repetitive stress rather than a single traumatic event"],
        ]),
    },
    "physical-education-and-self-defense-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Tactical periodization", "Integrates physical, technical, and tactical training within a unified weekly structure"],
        ]),
    },
    "physical-education-and-self-defense-m1-l63": {
        "data_table": table(["Method", "Purpose"], [
            ["Notational analysis", "Systematically codes match events to reveal performance patterns"],
        ]),
    },
    "physical-education-and-self-defense-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Skill progression model", "Sequences martial arts technique from foundational to advanced complexity"],
        ]),
    },
    "physical-education-and-self-defense-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Joint manipulation principle", "Grappling leverages joint mechanics to control or submit an opponent safely"],
        ]),
    },
    "physical-education-and-self-defense-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Kinetic linking", "Striking power is generated by sequential transfer of force through the body"],
        ]),
    },
    "physical-education-and-self-defense-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Proportionality", "Legal use of force in self-defense must match the severity of the threat faced"],
        ]),
    },
    "physical-education-and-self-defense-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Situational awareness", "Continuous environmental scanning reduces vulnerability to threats"],
        ]),
    },
    "physical-education-and-self-defense-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Stress inoculation", "Simulated high-pressure training improves performance under real threat conditions"],
        ]),
    },
    "physical-education-and-self-defense-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Verbal de-escalation", "Calm, non-confrontational communication can resolve conflict before it turns physical"],
        ]),
    },
    "physical-education-and-self-defense-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Modern self-defense system evolution", "Contemporary systems blend traditional martial technique with practical scenario training"],
        ]),
    },
    "physical-education-and-self-defense-m1-l72": {
        "data_table": table(["Tradition", "Philosophy"], [
            ["Aikido", "Emphasizes blending with an opponent's energy rather than direct confrontation"],
            ["Karate", "Emphasizes disciplined, direct striking technique"],
        ]),
    },
    "physical-education-and-self-defense-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["BJJ positional hierarchy", "Prioritizes controlling dominant ground positions before attempting submission"],
        ]),
    },
    "physical-education-and-self-defense-m1-l74": {
        "data_table": table(["Term", "Meaning"], [
            ["Kuzushi", "The judo principle of off-balancing an opponent before executing a throw"],
        ]),
    },
    "physical-education-and-self-defense-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Boxing footwork", "Controls range and angle to create advantage over an opponent"],
        ]),
    },
    "physical-education-and-self-defense-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Wrestling takedown mechanics", "Combines level change, penetration step, and finish to complete a takedown"],
        ]),
    },
    "physical-education-and-self-defense-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Youth developmental coaching", "Must account for age-appropriate physical and psychological readiness"],
        ]),
    },
    "physical-education-and-self-defense-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Physical literacy", "Foundational movement competence and confidence built during childhood"],
        ]),
    },
    "physical-education-and-self-defense-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["Exercise and cognition", "Regular physical activity is associated with improved cognitive function across age groups"],
        ]),
    },
    "physical-education-and-self-defense-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Aquatic sport physiology", "Water resistance and buoyancy create distinctive training demands and adaptations"],
        ]),
    },
    "physical-education-and-self-defense-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Cycling aerodynamics", "Body position and equipment design significantly affect drag at racing speeds"],
        ]),
    },
    "physical-education-and-self-defense-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Masters athlete training", "Requires adjusted recovery and injury prevention strategies with advancing age"],
        ]),
    },
    "physical-education-and-self-defense-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Menstrual cycle considerations", "Hormonal fluctuations can influence training response and performance planning"],
        ]),
    },
    "physical-education-and-self-defense-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Female athlete triad", "Links low energy availability, menstrual dysfunction, and reduced bone density"],
        ]),
    },
    "physical-education-and-self-defense-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Injury surveillance", "Systematic data collection tracks injury trends to guide prevention policy"],
        ]),
    },
    "physical-education-and-self-defense-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["Facility risk management", "Proactive design and maintenance reduce liability and participant injury risk"],
        ]),
    },
    "physical-education-and-self-defense-m1-l87": {
        "data_table": table(["Skill", "Purpose"], [
            ["Officiating under pressure", "Requires rapid, consistent decision-making amid high-stakes competitive scrutiny"],
        ]),
    },
    "physical-education-and-self-defense-m1-l88": {
        "data_table": table(["Concept", "Detail"], [
            ["Sport identity and community", "Participation in sport shapes belonging and social identity beyond competition itself"],
        ]),
    },
    "physical-education-and-self-defense-m1-l89": {
        "data_table": table(["Principle", "Detail"], [
            ["Inclusive curriculum design", "Offers multiple means of engagement and participation for all learners"],
        ]),
    },
    "physical-education-and-self-defense-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Authentic assessment", "Evaluates physical education competence through applied, real performance tasks"],
        ]),
    },
    "physical-education-and-self-defense-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Exercise immunology", "Moderate training generally supports immune function, while extreme load can suppress it"],
        ]),
    },
    "physical-education-and-self-defense-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Sleep and recovery", "Adequate sleep is critical for physiological recovery and adaptation to training"],
        ]),
    },
    "physical-education-and-self-defense-m1-l93": {
        "data_table": table(["Modality", "Purpose"], [
            ["Cold water immersion", "A recovery method with mixed evidence for reducing perceived muscle soreness"],
        ]),
    },
    "physical-education-and-self-defense-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Injury prediction modeling", "Uses athlete data to statistically estimate future injury risk"],
        ]),
    },
    "physical-education-and-self-defense-m1-l95": {
        "data_table": table(["Era", "Feature"], [
            ["Modern Olympic movement", "Revived in 1896, has grown into a major global sporting institution"],
        ]),
    },
    "physical-education-and-self-defense-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Fascial system", "Connective tissue network plays an active role in force transmission and movement"],
        ]),
    },
    "physical-education-and-self-defense-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental physiology", "Extreme heat, cold, or altitude requires specific physiological training adaptations"],
        ]),
    },
    "physical-education-and-self-defense-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Krav Maga reflexive defense", "Trains instinctive, efficient responses to common real-world attack scenarios"],
        ]),
    },
    "physical-education-and-self-defense-m1-l99": {
        "data_table": table(["System", "Feature"], [
            ["Filipino martial arts", "Weapon-based training with stick and blade underlies broader empty-hand technique"],
        ]),
    },
    "physical-education-and-self-defense-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Return-to-learn protocol", "Academic accommodations support cognitive recovery alongside physical concussion recovery"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Energy System", "Duration Used"], [
        ["ATP-PCr (Phosphagen)", "0-10 seconds, high intensity"],
        ["Anaerobic glycolysis", "10 seconds-2 minutes"],
        ["Aerobic system", "2+ minutes, endurance"],
    ]),
}

# l101-l120 use the shorter prefix and are "Worked Analysis" companions to l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"physical-education-and-self-defense-m1-l{base_n}"
    worked_key = f"physical-education-self-defense-m1-l{worked_n}"
    if base_key in CHARTS:
        CHARTS[worked_key] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[worked_key] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Physical Education & Self-Defense: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Physical Education & Self-Defense lessons (completing 120/120).")


if __name__ == "__main__":
    main()
