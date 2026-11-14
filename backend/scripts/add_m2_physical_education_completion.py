#!/usr/bin/env python3
"""Depth pass, M2 Physical Education & Self-Defense: fill in real,
hand-checked data_table content for the M2 Physical Education &
Self-Defense lessons not covered by the earlier breadth-first batch.
Brings M2 Physical Education & Self-Defense to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning sports
science and biomechanics, martial arts technical analysis, applied
sport psychology, and self-defense pedagogy/law; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls
within l1-l20, so it is also reused for l103).

Preserves the subject's lesson-ID prefix quirk: l1-l100 use
"physical-education-and-self-defense-m2-" while l101-l120 use the
shorter "physical-education-self-defense-m2-".

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_physical_education_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Periodization Phase", "Focus"], [
    ["Macrocycle", "A full training year/season"],
    ["Mesocycle", "Several weeks focused on a specific goal"],
    ["Microcycle", "A single week of training"],
])

CHARTS: dict[str, dict] = {
    "physical-education-and-self-defense-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Coaching & performance management research", "Systematic scholarly methods for studying elite athletic coaching practice"],
    ])},
    "physical-education-and-self-defense-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Fitness fundamentals research", "Rigorous study of the core principles underlying physical conditioning"],
    ])},
    "physical-education-and-self-defense-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Neuromuscular adaptation", "Resistance training first improves strength via nervous system efficiency before muscle growth"],
    ])},
    "physical-education-and-self-defense-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Ground reaction force (striking)", "Analyzes how force generated against the ground transfers into striking power"],
    ])},
    "physical-education-and-self-defense-m2-l6": {"data_table": table(["Metric", "Measures"], [
        ["VO2 max", "The body's maximum rate of oxygen consumption during exercise"],
        ["Lactate threshold", "The exercise intensity where lactate begins accumulating faster than it clears"],
    ])},
    "physical-education-and-self-defense-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Kinetic chain (takedowns)", "Analyzes how force transfers sequentially through the body during a grappling takedown"],
    ])},
    "physical-education-and-self-defense-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Contextual interference effect", "Varied, mixed practice produces better long-term skill retention than blocked repetition"],
    ])},
    "physical-education-and-self-defense-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Concussion return-to-play protocol", "A structured, staged process for safely returning an athlete to competition after a concussion"],
    ])},
    "physical-education-and-self-defense-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["PNF stretching", "A rehabilitation technique using contraction and relaxation cycles to improve range of motion"],
    ])},
    "physical-education-and-self-defense-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Overtraining syndrome", "A state of prolonged fatigue and performance decline from insufficient recovery"],
    ])},
    "physical-education-and-self-defense-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["BJJ positional hierarchy", "Ranks grappling positions by dominance to guide strategic ground fighting decisions"],
    ])},
    "physical-education-and-self-defense-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Nage-waza biomechanics", "Analyzes the leverage and timing mechanics underlying Judo throwing techniques"],
    ])},
    "physical-education-and-self-defense-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Flow state", "A state of complete absorption in an activity, associated with peak combat sport performance"],
    ])},
    "physical-education-and-self-defense-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Reaction time under pressure", "Studies how stress affects decision speed and accuracy in self-defense scenarios"],
    ])},
    "physical-education-and-self-defense-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Krav Maga threat assessment", "Trains instinctive, efficient responses to rapidly identified physical threats"],
    ])},
    "physical-education-and-self-defense-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Weapon retention/disarmament", "Techniques for keeping control of a weapon or safely removing one from an attacker"],
    ])},
    "physical-education-and-self-defense-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Pre-attack indicators", "Behavioral cues that can signal an impending physical assault"],
    ])},
    "physical-education-and-self-defense-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Adrenal stress response", "The body's physiological fight-or-flight reaction during a self-defense encounter"],
    ])},
    "physical-education-and-self-defense-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Kali/Eskrima", "Filipino martial arts systems centered on weapon-based (often stick and blade) training"],
    ])},
    "physical-education-and-self-defense-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Sprawl technique", "A defensive wrestling movement lowering the hips to counter a takedown attempt"],
    ])},
    "physical-education-and-self-defense-m2-l22": {"data_table": table(["Punch", "Mechanics"], [
        ["Jab", "A quick, straight lead-hand strike for range and setup"],
        ["Cross", "A powerful straight rear-hand strike with hip rotation"],
    ])},
    "physical-education-and-self-defense-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Muay Thai clinch", "Uses controlled grip leverage to off-balance an opponent and set up strikes"],
    ])},
    "physical-education-and-self-defense-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Weight-class periodization", "Structures training cycles around making a specific competition weight class"],
    ])},
    "physical-education-and-self-defense-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Rapid weight-cutting physiology", "Manages the physiological risks of quickly losing and regaining weight before competition"],
    ])},
    "physical-education-and-self-defense-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Nutrition periodization (strength/power)", "Times nutrient intake to match training phases for strength and power athletes"],
    ])},
    "physical-education-and-self-defense-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Rotational power (striking)", "Analyzes how hip and torso rotation generate power in striking techniques"],
    ])},
    "physical-education-and-self-defense-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Aikido circular redirection", "Uses an attacker's own momentum, redirected circularly, rather than opposing force"],
    ])},
    "physical-education-and-self-defense-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Modern MMA evolution", "Traces how mixed martial arts developed as a technical and cultural synthesis of styles"],
    ])},
    "physical-education-and-self-defense-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Reactive agility training", "Trains an athlete's ability to change direction quickly in response to a stimulus"],
    ])},
    "physical-education-and-self-defense-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Injury epidemiology (grappling)", "Studies patterns and rates of injury specific to grappling-based combat sports"],
    ])},
    "physical-education-and-self-defense-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Strength/conditioning for grapplers", "Designs training programs matching the specific physical demands of grappling"],
    ])},
    "physical-education-and-self-defense-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["De-escalation communication", "Verbal strategies for reducing tension and avoiding physical conflict"],
    ])},
    "physical-education-and-self-defense-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Self-defense scenario design", "Structures realistic training scenarios accounting for environment and situational factors"],
    ])},
    "physical-education-and-self-defense-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["ARV considerations (personal safety)", "Armed response and legal/tactical considerations relevant to personal safety instruction"],
    ])},
    "physical-education-and-self-defense-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Kinesthetic feedback (skill acquisition)", "Uses bodily sensory feedback to accelerate learning of complex martial arts sequences"],
    ])},
    "physical-education-and-self-defense-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Systema breathing principles", "A Russian martial art emphasizing relaxation and breath control as its movement foundation"],
    ])},
    "physical-education-and-self-defense-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Kata and bunkai", "Traditional karate forms (kata) with their practical combat application interpretation (bunkai)"],
    ])},
    "physical-education-and-self-defense-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Pain compliance (joint manipulation)", "The neurophysiological basis for techniques that use joint pressure to control an opponent"],
    ])},
    "physical-education-and-self-defense-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Ukemi (breakfall)", "Techniques for falling safely to minimize impact injury"],
    ])},
    "physical-education-and-self-defense-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Sport-specific plyometrics", "Explosive jump training tailored to develop combat-sport-relevant power"],
    ])},
    "physical-education-and-self-defense-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Video-based performance analysis", "Uses recorded footage to systematically analyze and improve athlete technique"],
    ])},
    "physical-education-and-self-defense-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Pre-competition anxiety regulation", "Sport psychology techniques for managing nerves before combat competition"],
    ])},
    "physical-education-and-self-defense-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Long-term athlete development", "A staged model for developing youth athletes appropriately at each growth stage"],
    ])},
    "physical-education-and-self-defense-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Choke physiology", "The physiological mechanisms (blood or air restriction) underlying strangulation techniques"],
    ])},
    "physical-education-and-self-defense-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["ACL return-to-sport criteria", "Objective benchmarks determining when an athlete can safely resume competition after ACL surgery"],
    ])},
    "physical-education-and-self-defense-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Constraints-led approach", "A coaching pedagogy shaping skill development by manipulating task and environmental constraints"],
    ])},
    "physical-education-and-self-defense-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Kicking biomechanics", "Compares mechanics of kicking techniques across different striking disciplines"],
    ])},
    "physical-education-and-self-defense-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Work-to-rest ratios (combat sport)", "Analyzes the physiological demand pattern of competitive rounds and rest periods"],
    ])},
    "physical-education-and-self-defense-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Self-defense instructor liability", "Legal considerations instructors must understand when teaching self-defense"],
    ])},
    "physical-education-and-self-defense-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Reality-based self-defense curricula", "Compares traditional martial arts training with modern scenario-based self-defense programs"],
    ])},
    "physical-education-and-self-defense-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Startle reflex integration", "Trains defensive movements that work with, rather than against, the body's involuntary startle response"],
    ])},
    "physical-education-and-self-defense-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Multiple-attacker tactics", "Positional awareness strategies for managing threats from more than one attacker"],
    ])},
    "physical-education-and-self-defense-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Bridge and roll escape", "A biomechanical analysis of the hip-driven escape from a mounted grappling position"],
    ])},
    "physical-education-and-self-defense-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Physical literacy framework", "A model for developing lifelong movement competence and confidence"],
    ])},
    "physical-education-and-self-defense-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Exercise prescription (chronic disease)", "Designs safe, effective exercise programs for populations managing chronic conditions"],
    ])},
    "physical-education-and-self-defense-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Core stability transfer", "Examines how trunk stability contributes to performance across combat sport movements"],
    ])},
    "physical-education-and-self-defense-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Heart rate variability monitoring", "Tracks recovery status to guide training load management"],
    ])},
    "physical-education-and-self-defense-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Underhook control (MMA)", "Analyzes the leverage advantage of controlling underneath an opponent's arm in the clinch"],
    ])},
    "physical-education-and-self-defense-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Justifiable use of force doctrine", "Traces the historical and legal development of self-defense law"],
    ])},
    "physical-education-and-self-defense-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Tactical preparation (team combat sports)", "Periodizes training specifically around tactical competition readiness"],
    ])},
    "physical-education-and-self-defense-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["HIIT for combat conditioning", "High-intensity interval training tailored to combat sport energy system demands"],
    ])},
    "physical-education-and-self-defense-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Ethics of teaching lethal techniques", "Considers the pedagogical and moral responsibilities of instructing dangerous techniques"],
    ])},
    "physical-education-and-self-defense-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Timing and distance management", "Analyzes the tactical control of range and rhythm in striking exchanges"],
    ])},
    "physical-education-and-self-defense-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Rate of force development", "The neuromechanics governing how quickly muscles can generate explosive force"],
    ])},
    "physical-education-and-self-defense-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Rotator cuff biomechanics", "Analyzes shoulder mechanics and injury risk in overhead combat sport movements"],
    ])},
    "physical-education-and-self-defense-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Fear management training", "Sport psychology techniques for building readiness to face physical confrontation"],
    ])},
    "physical-education-and-self-defense-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Individualized athlete feedback", "Coaching methods tailored to a specific athlete's skill refinement needs"],
    ])},
    "physical-education-and-self-defense-m2-l69": {"data_table": table(["Setting", "Feature"], [
        ["Standing self-defense", "Emphasizes striking and escape from a threat"],
        ["Ground-based self-defense", "Emphasizes control and escape from grappling positions"],
    ])},
    "physical-education-and-self-defense-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Recovery modalities", "Compares techniques for managing fatigue across high-frequency combat sport training"],
    ])},
    "physical-education-and-self-defense-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Grip fighting strategy", "Analyzes how hand and sleeve control determines advantage in Judo and wrestling"],
    ])},
    "physical-education-and-self-defense-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Vision training (reaction)", "Trains visual anticipation skills to improve reaction speed in combat sports"],
    ])},
    "physical-education-and-self-defense-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Elbow/knee strike mechanics", "Analyzes the close-range biomechanics of Muay Thai elbow and knee strikes"],
    ])},
    "physical-education-and-self-defense-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Sub-concussive impact effects", "Studies long-term consequences of repeated low-level head impacts in combat athletes"],
    ])},
    "physical-education-and-self-defense-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive martial arts instruction", "Pedagogical adaptations for teaching martial arts to disabled populations"],
    ])},
    "physical-education-and-self-defense-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Guard retention (BJJ)", "Analyzes strategies for maintaining an effective defensive guard position"],
    ])},
    "physical-education-and-self-defense-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Tapering strategy", "Systematically reduces training load before competition to peak performance"],
    ])},
    "physical-education-and-self-defense-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Feinting and deceptive movement", "Coaching analysis of how deceptive setups create striking opportunities"],
    ])},
    "physical-education-and-self-defense-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Hip escapes/shrimping", "Foundational biomechanics of hip-based defensive movement in ground grappling"],
    ])},
    "physical-education-and-self-defense-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Fatigue-induced technical breakdown", "Studies how fatigue degrades technique quality across extended competition rounds"],
    ])},
    "physical-education-and-self-defense-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Vulnerable population safety curriculum", "Designs self-defense training specifically for at-risk populations"],
    ])},
    "physical-education-and-self-defense-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Takedown defense sequencing", "Analyzes the coordinated sprawl-and-underhook sequence used to defend takedowns"],
    ])},
    "physical-education-and-self-defense-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Tactical baton training", "Compares traditional weapon kata with modern law-enforcement baton techniques"],
    ])},
    "physical-education-and-self-defense-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Deliberate practice (elite development)", "Applies focused, feedback-driven practice theory to elite martial arts skill acquisition"],
    ])},
    "physical-education-and-self-defense-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Grip strength endurance", "Analyzes the physiological demands of sustained grip strength in grappling competition"],
    ])},
    "physical-education-and-self-defense-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Post-competition mental reset", "Sport psychology strategies for recovery and refocus after competition"],
    ])},
    "physical-education-and-self-defense-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Opponent scouting", "Coaching science of analyzing an upcoming opponent to build a tactical game plan"],
    ])},
    "physical-education-and-self-defense-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Balance and base (standing grappling)", "Kinesiology of maintaining stability during standing grappling exchanges"],
    ])},
    "physical-education-and-self-defense-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Self-defense effectiveness research", "Compares outcomes across different self-defense training programs for assault prevention"],
    ])},
    "physical-education-and-self-defense-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Rule-set influence on tactics", "Examines how referee decisions and rules shape the tactical evolution of combat sports"],
    ])},
    "physical-education-and-self-defense-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Altitude/environmental training", "Studies physiological adaptations from training in altitude or extreme environments"],
    ])},
    "physical-education-and-self-defense-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Integrated fitness/self-defense curriculum", "Combines general fitness education with self-defense literacy in curriculum design"],
    ])},
    "physical-education-and-self-defense-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Fall risk in aging practitioners", "Studies postural control deficits affecting older combat sport participants"],
    ])},
    "physical-education-and-self-defense-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Recovery nutrition timing", "Optimizes when nutrients are consumed following high-intensity combat sport training"],
    ])},
    "physical-education-and-self-defense-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Spinal loading (throws/takedowns)", "Analyzes the repetitive spinal stress from throwing and takedown actions"],
    ])},
    "physical-education-and-self-defense-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Isometric strength (grappling control)", "Analyzes how static strength contributes to maintaining dominant grappling positions"],
    ])},
    "physical-education-and-self-defense-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Decision fatigue (sparring)", "Studies how cognitive load accumulates and degrades decision-making in extended sparring"],
    ])},
    "physical-education-and-self-defense-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Workplace violence prevention training", "Applies self-defense principles to workplace safety programs"],
    ])},
    "physical-education-and-self-defense-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Striking power across classes", "Compares power output across different weight and experience classifications"],
    ])},
    "physical-education-and-self-defense-m2-l100": {"data_table": table(["Component", "Purpose"], [
        ["Master's thesis research seminar", "Presents and defends original research in physical education, kinesiology, and self-defense studies"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"physical-education-and-self-defense-m2-l{base_n}"
    worked_key = f"physical-education-self-defense-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Physical Education & Self-Defense"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Physical Education & Self-Defense: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Physical Education & Self-Defense lessons.")


if __name__ == "__main__":
    main()
