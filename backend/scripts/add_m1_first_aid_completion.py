#!/usr/bin/env python3
"""Depth pass, M1 First Aid: fill in real, hand-checked data_table
content for the 119 M1 First Aid lessons not covered by the earlier
breadth-first batch. Brings M1 First Aid to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_first_aid_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Wound Care Step", "Action"], [
    ["1", "Clean hands and wear gloves if available"],
    ["2", "Stop the bleeding with direct pressure"],
    ["3", "Clean the wound with water"],
    ["4", "Cover with a sterile dressing"],
])

CHARTS: dict[str, dict] = {
    "first-aid-m1-l1": {"data_table": table(["Concept", "Detail"], [
        ["Wilderness & remote medicine", "Manages trauma and illness far from definitive care with improvised resources"],
    ])},
    "first-aid-m1-l2": {"data_table": table(["Concept", "Detail"], [
        ["Advanced life support", "Adds airway devices, IV/IO access, and cardiac drugs beyond basic CPR"],
    ])},
    "first-aid-m1-l4": {"data_table": table(["Burn depth", "Feature"], [
        ["Superficial", "Red, painful, no blisters"],
        ["Partial-thickness", "Blisters, moist, very painful"],
        ["Full-thickness", "White/charred, leathery, often painless"],
    ])},
    "first-aid-m1-l5": {"data_table": table(["Injury", "Field action"], [
        ["Fracture", "Splint in the position found, check circulation before/after"],
        ["Dislocation", "Immobilize; do not force reduction unless trained"],
    ])},
    "first-aid-m1-l6": {"data_table": table(["Shock type", "Cause"], [
        ["Hypovolemic", "Blood or fluid loss"],
        ["Cardiogenic", "Heart failing to pump effectively"],
        ["Distributive", "Vessels abnormally dilated (e.g. sepsis, anaphylaxis)"],
    ])},
    "first-aid-m1-l7": {"data_table": table(["Sign", "Anaphylaxis relevance"], [
        ["Hives + swelling", "Skin/mucosal involvement"],
        ["Wheeze/stridor", "Airway compromise, give epinephrine"],
        ["Hypotension", "Circulatory compromise, give epinephrine"],
    ])},
    "first-aid-m1-l8": {"data_table": table(["Symptom", "Cardiac concern"], [
        ["Crushing chest pain", "Possible myocardial infarction"],
        ["Radiating arm/jaw pain", "Classic cardiac referral pattern"],
    ])},
    "first-aid-m1-l9": {"data_table": table(["Letter (FAST)", "Sign"], [
        ["F", "Face drooping"],
        ["A", "Arm weakness"],
        ["S", "Speech difficulty"],
        ["T", "Time to call emergency services"],
    ])},
    "first-aid-m1-l10": {"data_table": table(["Poisoning route", "First action"], [
        ["Ingested", "Do not induce vomiting; call poison control"],
        ["Inhaled", "Move to fresh air"],
        ["Contact", "Remove contaminated clothing, flush skin"],
    ])},
    "first-aid-m1-l11": {"data_table": table(["Environmental emergency", "Key risk"], [
        ["Heat stroke", "Core temperature failure, life-threatening"],
        ["Hypothermia", "Progressive core cooling, cardiac risk"],
    ])},
    "first-aid-m1-l12": {"data_table": table(["Bleeding severity", "Control method"], [
        ["Minor", "Direct pressure and dressing"],
        ["Severe/arterial", "Direct pressure, then tourniquet if uncontrolled"],
    ])},
    "first-aid-m1-l13": {"data_table": table(["Triage category", "Meaning"], [
        ["Immediate (red)", "Life-threatening, treatable"],
        ["Delayed (yellow)", "Serious but stable"],
        ["Minor (green)", "Walking wounded"],
        ["Expectant (black)", "Unsurvivable given resources"],
    ])},
    "first-aid-m1-l14": {"data_table": table(["Age group", "Consideration"], [
        ["Infant", "Higher relative surface area, faster heat/fluid loss"],
        ["Child", "Vital sign norms differ from adults"],
    ])},
    "first-aid-m1-l15": {"data_table": table(["Chronic condition", "Emergency risk"], [
        ["Diabetes", "Hypo/hyperglycemia"],
        ["Asthma/COPD", "Acute respiratory distress"],
        ["Heart disease", "Higher cardiac arrest risk"],
    ])},
    "first-aid-m1-l16": {"data_table": table(["Concept", "Detail"], [
        ["Psychological first aid", "Provides safety, comfort, and connection after a traumatic event"],
    ])},
    "first-aid-m1-l17": {"data_table": table(["Concept", "Detail"], [
        ["Prolonged field care", "Sustains a patient over hours/days when evacuation is delayed"],
    ])},
    "first-aid-m1-l18": {"data_table": table(["Concept", "Detail"], [
        ["First aid program design", "Plans training, equipment, and response protocols for an organization"],
    ])},
    "first-aid-m1-l19": {"data_table": table(["Concept", "Detail"], [
        ["Good Samaritan protection", "Legal protection for those who render aid in good faith"],
    ])},
    "first-aid-m1-l20": {"data_table": table(["Step (CAB)", "Action"], [
        ["C", "Compressions: push hard and fast on the center of the chest"],
        ["A", "Airway: tilt head, lift chin"],
        ["B", "Breathing: give rescue breaths if trained"],
    ])},
    "first-aid-m1-l21": {"data_table": table(["Device", "Use"], [
        ["Windlass tourniquet", "Applied 2-3 inches above the wound, tightened until bleeding stops"],
    ])},
    "first-aid-m1-l22": {"data_table": table(["Technique", "Use"], [
        ["Wound packing", "Fills deep cavity wounds with gauze while maintaining pressure"],
    ])},
    "first-aid-m1-l23": {"data_table": table(["Device", "Use"], [
        ["Supraglottic airway", "Secures the airway above the vocal cords without direct visualization"],
    ])},
    "first-aid-m1-l24": {"data_table": table(["Sign", "Tension pneumothorax"], [
        ["Absent breath sounds one side", "Suggests collapsed lung under pressure"],
        ["Tracheal deviation", "Late, ominous sign"],
    ])},
    "first-aid-m1-l25": {"data_table": table(["Device", "Use"], [
        ["Vented chest seal", "Covers an open chest wound while allowing trapped air to escape"],
    ])},
    "first-aid-m1-l26": {"data_table": table(["Concept", "Detail"], [
        ["Spinal motion restriction", "Limits spine movement in suspected spinal injury"],
    ])},
    "first-aid-m1-l27": {"data_table": table(["Injury", "Splint"], [
        ["Femur fracture", "Traction splint reduces pain and internal bleeding"],
    ])},
    "first-aid-m1-l28": {"data_table": table(["Concept", "Detail"], [
        ["Dislocation reduction", "Restores joint alignment; higher-risk skill needing training"],
    ])},
    "first-aid-m1-l29": {"data_table": table(["Concept", "Detail"], [
        ["Crush syndrome", "Muscle breakdown releasing toxins into circulation after prolonged compression"],
    ])},
    "first-aid-m1-l30": {"data_table": table(["Sign (6 P's)", "Compartment syndrome"], [
        ["Pain, Pallor, Paresthesia", "Early warning signs"],
        ["Pulselessness, Paralysis", "Late, limb-threatening signs"],
    ])},
    "first-aid-m1-l31": {"data_table": table(["Step", "Amputation care"], [
        ["1", "Control bleeding with direct pressure/tourniquet"],
        ["2", "Wrap and cool the amputated part, do not freeze directly"],
    ])},
    "first-aid-m1-l32": {"data_table": table(["Injury", "Action"], [
        ["Avulsed tooth", "Rinse gently, reinsert or store in milk, seek dental care fast"],
    ])},
    "first-aid-m1-l33": {"data_table": table(["Frostbite stage", "Feature"], [
        ["Frostnip", "Numbness, no tissue damage"],
        ["Superficial", "Waxy, firm skin"],
        ["Deep", "Hard, mottled, tissue loss risk"],
    ])},
    "first-aid-m1-l34": {"data_table": table(["Hypothermia stage", "Core temp"], [
        ["Mild", "~35-32C, shivering"],
        ["Moderate-severe", "<32C, shivering stops, risk of arrest"],
    ])},
    "first-aid-m1-l35": {"data_table": table(["Condition", "Key sign"], [
        ["Heat exhaustion", "Heavy sweating, weakness, still alert"],
        ["Heat stroke", "Altered mental status, hot dry or wet skin"],
    ])},
    "first-aid-m1-l36": {"data_table": table(["Condition", "Feature"], [
        ["AMS", "Headache, nausea at altitude"],
        ["HAPE/HACE", "Life-threatening fluid in lungs/brain, needs descent"],
    ])},
    "first-aid-m1-l37": {"data_table": table(["Step", "Drowning response"], [
        ["1", "Remove from water safely"],
        ["2", "Begin rescue breaths/CPR promptly"],
    ])},
    "first-aid-m1-l38": {"data_table": table(["Step", "Snakebite first aid"], [
        ["1", "Keep patient calm and still, limit limb movement"],
        ["2", "Seek antivenom care; do not cut or suck the wound"],
    ])},
    "first-aid-m1-l39": {"data_table": table(["Envenomation", "First aid"], [
        ["Jellyfish", "Rinse with vinegar/hot water depending on species"],
        ["Stingray", "Immerse in hot water for pain control"],
    ])},
    "first-aid-m1-l40": {"data_table": table(["Sign", "Insect sting anaphylaxis"], [
        ["Widespread hives + breathing trouble", "Give epinephrine, call emergency services"],
    ])},
    "first-aid-m1-l41": {"data_table": table(["Concept", "Detail"], [
        ["Rabies risk", "Any mammal bite in an endemic area needs medical evaluation"],
    ])},
    "first-aid-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Status epilepticus", "A seizure lasting over 5 minutes or repeated seizures without recovery"],
    ])},
    "first-aid-m1-l43": {"data_table": table(["Condition", "Sign"], [
        ["Hypoglycemia", "Shaky, sweaty, confused; give fast sugar if conscious"],
        ["Hyperglycemia", "Thirst, fruity breath; needs medical care"],
    ])},
    "first-aid-m1-l44": {"data_table": table(["Sign", "Opioid overdose"], [
        ["Pinpoint pupils, slow/no breathing", "Give naloxone, call emergency services"],
    ])},
    "first-aid-m1-l45": {"data_table": table(["Condition", "Danger"], [
        ["Alcohol withdrawal", "Can progress to seizures or delirium tremens"],
    ])},
    "first-aid-m1-l46": {"data_table": table(["Step", "Choking response"], [
        ["1", "Encourage coughing if air is moving"],
        ["2", "Abdominal thrusts if obstruction is complete"],
    ])},
    "first-aid-m1-l47": {"data_table": table(["Step", "Newborn resuscitation"], [
        ["1", "Dry, warm, and stimulate"],
        ["2", "Assess breathing and heart rate, assist as needed"],
    ])},
    "first-aid-m1-l48": {"data_table": table(["Concept", "Detail"], [
        ["Precipitous delivery", "Very rapid birth with little warning, support the newborn's head"],
    ])},
    "first-aid-m1-l49": {"data_table": table(["Consideration", "Geriatric trauma"], [
        ["Fragile bone/skin", "Lower-force injuries can still be serious"],
    ])},
    "first-aid-m1-l50": {"data_table": table(["CPR type", "Feature"], [
        ["Compression-only", "Recommended for untrained bystanders"],
        ["Conventional (with breaths)", "Preferred when rescuer is trained, especially for children/drowning"],
    ])},
    "first-aid-m1-l51": {"data_table": table(["Step", "AED use"], [
        ["1", "Turn on and follow voice prompts"],
        ["2", "Attach pads, ensure no one touches patient during analysis/shock"],
    ])},
    "first-aid-m1-l52": {"data_table": table(["Chain of survival link", "Action"], [
        ["Early recognition", "Call for help immediately"],
        ["Early CPR", "Start compressions without delay"],
        ["Early defibrillation", "Use an AED as soon as available"],
    ])},
    "first-aid-m1-l53": {"data_table": table(["Triage system", "Feature"], [
        ["START", "Rapid categorization by respiration, perfusion, mental status"],
        ["SALT", "Sort, Assess, Lifesaving interventions, Treatment/transport"],
    ])},
    "first-aid-m1-l54": {"data_table": table(["Setting", "Triage challenge"], [
        ["Wilderness", "Limited resources and delayed evacuation change priorities"],
    ])},
    "first-aid-m1-l55": {"data_table": table(["Rule of Nines region", "% Body surface"], [
        ["Head", "9%"],
        ["Each arm", "9%"],
        ["Each leg", "18%"],
        ["Torso (front)", "18%"],
    ])},
    "first-aid-m1-l56": {"data_table": table(["Concept", "Detail"], [
        ["Electrical injury", "Can cause hidden internal damage and cardiac arrhythmia"],
    ])},
    "first-aid-m1-l57": {"data_table": table(["Blast injury type", "Mechanism"], [
        ["Primary", "Overpressure wave damages air-filled organs"],
        ["Secondary", "Flying debris causes penetrating trauma"],
    ])},
    "first-aid-m1-l58": {"data_table": table(["Priority", "Gunshot wound care"], [
        ["1", "Control massive hemorrhage first"],
        ["2", "Assess for exit wounds and airway/chest involvement"],
    ])},
    "first-aid-m1-l59": {"data_table": table(["GCS component", "Range"], [
        ["Eye opening", "1-4"],
        ["Verbal response", "1-5"],
        ["Motor response", "1-6"],
    ])},
    "first-aid-m1-l60": {"data_table": table(["Concept", "Detail"], [
        ["Concussion", "A mild traumatic brain injury; remove from play and monitor"],
    ])},
    "first-aid-m1-l61": {"data_table": table(["Concept", "Detail"], [
        ["Sudden cardiac arrest in sport", "Often due to underlying heart conditions; needs immediate CPR/AED"],
    ])},
    "first-aid-m1-l62": {"data_table": table(["Concept", "Detail"], [
        ["Exercise-associated collapse", "Post-exercise fainting, usually benign but must rule out cardiac cause"],
    ])},
    "first-aid-m1-l63": {"data_table": table(["Step", "Auto-injector use"], [
        ["1", "Remove safety cap, press firmly into outer thigh"],
        ["2", "Hold in place per device instructions, then call emergency services"],
    ])},
    "first-aid-m1-l64": {"data_table": table(["Sign", "Asthma exacerbation"], [
        ["Wheeze, accessory muscle use", "Assist with rescue inhaler, escalate if not improving"],
    ])},
    "first-aid-m1-l65": {"data_table": table(["Condition", "Sound"], [
        ["Croup", "Barking cough, stridor"],
    ])},
    "first-aid-m1-l66": {"data_table": table(["Sign", "Infant airway obstruction"], [
        ["Sudden coughing/gagging, no sound", "Back blows and chest thrusts, not abdominal thrusts"],
    ])},
    "first-aid-m1-l67": {"data_table": table(["Step", "Chemical ingestion first aid"], [
        ["1", "Do not induce vomiting"],
        ["2", "Call poison control with product info"],
    ])},
    "first-aid-m1-l68": {"data_table": table(["Sign", "CO poisoning"], [
        ["Headache, confusion, cherry-red skin (late)", "Move to fresh air, seek emergency care"],
    ])},
    "first-aid-m1-l69": {"data_table": table(["Concept", "Detail"], [
        ["Acute gastroenteritis", "Focus on hydration; watch for signs of severe dehydration"],
    ])},
    "first-aid-m1-l70": {"data_table": table(["Sign", "Dehydration severity"], [
        ["Mild", "Thirst, dry mouth"],
        ["Severe", "Sunken eyes, lethargy, minimal urine output"],
    ])},
    "first-aid-m1-l71": {"data_table": table(["Concept", "Detail"], [
        ["Sunburn care", "Cool compresses, hydration, moisturizer; blisters should not be popped"],
    ])},
    "first-aid-m1-l72": {"data_table": table(["Sign", "Wound infection"], [
        ["Increasing redness, warmth, pus", "Seek medical evaluation, possible antibiotics"],
    ])},
    "first-aid-m1-l73": {"data_table": table(["Alternative", "Use"], [
        ["Wound closure strips", "Approximate skin edges when suturing is unavailable"],
    ])},
    "first-aid-m1-l74": {"data_table": table(["Step", "Tick removal"], [
        ["1", "Grasp close to skin with fine tweezers"],
        ["2", "Pull upward steadily, avoid twisting"],
    ])},
    "first-aid-m1-l75": {"data_table": table(["Kit item", "High-altitude use"], [
        ["Pulse oximeter", "Monitors oxygen saturation for altitude illness"],
    ])},
    "first-aid-m1-l76": {"data_table": table(["Hazard", "Maritime first aid concern"], [
        ["Hypothermia in water", "Rapid heat loss even in moderate temperatures"],
    ])},
    "first-aid-m1-l77": {"data_table": table(["Phase (TCCC)", "Focus"], [
        ["Care Under Fire", "Stop massive bleeding, return fire if needed"],
        ["Tactical Field Care", "Fuller assessment once safe"],
    ])},
    "first-aid-m1-l78": {"data_table": table(["Concept", "Detail"], [
        ["Search and rescue medical support", "Coordinates field treatment with evacuation logistics"],
    ])},
    "first-aid-m1-l79": {"data_table": table(["Concept", "Detail"], [
        ["Avalanche burial", "Survival odds drop sharply after 15 minutes without an air pocket"],
    ])},
    "first-aid-m1-l80": {"data_table": table(["Concept", "Detail"], [
        ["Cave rescue", "Confined access complicates extrication and hypothermia risk"],
    ])},
    "first-aid-m1-l81": {"data_table": table(["Concept", "Detail"], [
        ["Workplace first aid", "Protocols tailored to site-specific hazards (machinery, chemicals)"],
    ])},
    "first-aid-m1-l82": {"data_table": table(["Concept", "Detail"], [
        ["Confined space rescue", "Requires atmospheric monitoring before entry"],
    ])},
    "first-aid-m1-l83": {"data_table": table(["Concept", "Detail"], [
        ["School emergency planning", "Combines first aid protocols with lockdown/evacuation procedures"],
    ])},
    "first-aid-m1-l84": {"data_table": table(["Concept", "Detail"], [
        ["Automated notification systems", "Alert responders quickly to on-site emergencies"],
    ])},
    "first-aid-m1-l85": {"data_table": table(["Principle (PFA)", "Action"], [
        ["Safety", "Ensure physical and emotional safety"],
        ["Connection", "Link to social support"],
    ])},
    "first-aid-m1-l86": {"data_table": table(["Concept", "Detail"], [
        ["Critical incident stress", "Cumulative psychological toll on responders after traumatic calls"],
    ])},
    "first-aid-m1-l87": {"data_table": table(["Concept", "Detail"], [
        ["BLS instructor training", "Teaches how to deliver and assess CPR/AED skills to learners"],
    ])},
    "first-aid-m1-l88": {"data_table": table(["Environment", "Kit consideration"], [
        ["Wilderness", "Lightweight, durable, splinting materials"],
        ["Workplace", "Chemical/eye-wash supplies matched to hazards"],
    ])},
    "first-aid-m1-l89": {"data_table": table(["Concept", "Detail"], [
        ["Documentation", "Accurate records support care continuity and legal protection"],
    ])},
    "first-aid-m1-l90": {"data_table": table(["Concept", "Detail"], [
        ["Good Samaritan laws", "Protections vary by jurisdiction and may require certification"],
    ])},
    "first-aid-m1-l91": {"data_table": table(["Concept", "Detail"], [
        ["Telemedicine support", "Remote clinicians guide field providers through complex care"],
    ])},
    "first-aid-m1-l92": {"data_table": table(["Concept", "Detail"], [
        ["WFR certification", "Standardizes wilderness first responder training and scope"],
    ])},
    "first-aid-m1-l93": {"data_table": table(["Sign", "Hip fracture in elderly falls"], [
        ["Shortened, externally rotated leg", "Classic sign, immobilize and transport"],
    ])},
    "first-aid-m1-l94": {"data_table": table(["Concept", "Detail"], [
        ["Injury pattern recognition", "Certain patterns raise concern for abuse and require careful reporting"],
    ])},
    "first-aid-m1-l95": {"data_table": table(["Concept", "Detail"], [
        ["Pediatric burn assessment", "Uses child-specific surface-area charts, not adult Rule of Nines"],
    ])},
    "first-aid-m1-l96": {"data_table": table(["Concept", "Detail"], [
        ["Pediatric sepsis", "Rapid recognition and escalation improve survival"],
    ])},
    "first-aid-m1-l97": {"data_table": table(["Concept", "Detail"], [
        ["Biphasic anaphylaxis", "Symptoms can recur hours after initial resolution; monitor"],
    ])},
    "first-aid-m1-l98": {"data_table": table(["Concept", "Detail"], [
        ["High-fidelity simulation", "Realistic scenario training for mass casualty response"],
    ])},
    "first-aid-m1-l99": {"data_table": table(["Concept", "Detail"], [
        ["Traumatic eye injury", "Avoid pressure on the globe, shield rather than patch"],
    ])},
    "first-aid-m1-l100": {"data_table": table(["Concept", "Detail"], [
        ["Non-accidental trauma", "Injury patterns inconsistent with reported mechanism warrant referral"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"first-aid-m1-l{base_n}"
    worked_key = f"first-aid-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["First Aid"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json First Aid: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 First Aid lessons (completing 120/120).")


if __name__ == "__main__":
    main()
