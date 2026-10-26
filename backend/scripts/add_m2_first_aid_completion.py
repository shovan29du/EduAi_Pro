#!/usr/bin/env python3
"""Depth pass, M2 First Aid: fill in real, hand-checked data_table
content for the M2 First Aid lessons not covered by the earlier
breadth-first batch. Brings M2 First Aid to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning trauma
resuscitation science, advanced life support, toxicology/environmental
emergencies, disaster medicine, and EMS systems/education research;
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_first_aid_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["TCCC", "Tactical Combat Casualty Care; battlefield trauma protocols for care under fire"],
    ["Care under fire", "The TCCC phase focused on stopping active threats and controlling massive hemorrhage first"],
])

CHARTS: dict[str, dict] = {
    "first-aid-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Advanced life support concepts", "Graduate-level study of the systems and evidence underlying critical emergency care"],
    ])},
    "first-aid-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Basic first aid & CPR research", "Rigorous scholarly grounding in foundational emergency response principles"],
    ])},
    "first-aid-m2-l4": {"data_table": table(["System", "Feature"], [
        ["START", "Rapid categorization by respiration, perfusion, mental status"],
        ["SALT", "Sort, Assess, Lifesaving interventions, Treatment/transport"],
    ])},
    "first-aid-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Tourniquet efficacy", "Research evidence on windlass tourniquets' effectiveness at controlling limb hemorrhage"],
    ])},
    "first-aid-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Hemostatic dressing", "Gauze impregnated with clotting-promoting agents to control severe bleeding"],
    ])},
    "first-aid-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Permissive hypotension", "Deliberately limits fluid resuscitation to avoid disrupting clot formation before surgical control"],
    ])},
    "first-aid-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Damage control resuscitation", "Prioritizes blood products over crystalloid fluids to prevent trauma-induced coagulopathy"],
    ])},
    "first-aid-m2-l9": {"data_table": table(["Factor", "Effect"], [
        ["Coagulopathy", "Impairs the blood's ability to clot"],
        ["Acidosis", "Disrupts enzyme and clotting function"],
        ["Hypothermia", "Further impairs clotting cascade"],
    ])},
    "first-aid-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Massive transfusion protocol", "A standardized ratio-based blood product delivery system for severe hemorrhage"],
    ])},
    "first-aid-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Prehospital blood administration", "Delivers blood products before hospital arrival to improve trauma survival"],
    ])},
    "first-aid-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["ACLS algorithm evolution", "Traces how evidence-based updates have reshaped advanced cardiac life support guidelines"],
    ])},
    "first-aid-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["PALS", "Pediatric Advanced Life Support; resuscitation protocols adapted for children"],
    ])},
    "first-aid-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Neonatal resuscitation program", "Standardized guidelines for resuscitating newborns immediately after birth"],
    ])},
    "first-aid-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Mechanical CPR device", "Automated chest compression machines, with evidence showing mixed outcome benefits"],
    ])},
    "first-aid-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["ECPR", "Extracorporeal CPR; uses a heart-lung bypass machine during refractory cardiac arrest"],
    ])},
    "first-aid-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Targeted temperature management", "Controlled cooling after cardiac arrest to reduce brain injury"],
    ])},
    "first-aid-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Rapid sequence intubation", "Uses sedative and paralytic drugs together to secure an airway quickly and safely"],
    ])},
    "first-aid-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Surgical cricothyrotomy", "An emergency procedure creating a surgical airway when intubation is not possible"],
    ])},
    "first-aid-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Chest seal (open pneumothorax)", "A vented dressing that covers a chest wound while letting trapped air escape"],
    ])},
    "first-aid-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Spinal motion restriction", "Evolving evidence has shifted care away from routine full-spine immobilization"],
    ])},
    "first-aid-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["TBI prehospital management", "Guidelines for avoiding secondary brain injury (hypoxia, hypotension) after trauma"],
    ])},
    "first-aid-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Cervical spine clinical decision rules", "Validated criteria (e.g. NEXUS, Canadian C-Spine) for ruling out spinal injury without imaging"],
    ])},
    "first-aid-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Parkland formula", "Calculates IV fluid resuscitation volume for burn patients based on body surface area burned"],
    ])},
    "first-aid-m2-l25": {"data_table": table(["Depth", "Feature"], [
        ["Superficial", "Red, painful, no blisters"],
        ["Partial-thickness", "Blisters, moist, very painful"],
        ["Full-thickness", "White/charred, leathery, often painless"],
    ])},
    "first-aid-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Crush syndrome", "Muscle breakdown after prolonged compression releases toxins that can cause kidney failure"],
    ])},
    "first-aid-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Fasciotomy indication", "Surgical release of pressure when compartment syndrome threatens limb viability"],
    ])},
    "first-aid-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["High-altitude illness", "Manages conditions ranging from mild AMS to life-threatening HAPE and HACE"],
    ])},
    "first-aid-m2-l29": {"data_table": table(["Stage", "Core temp"], [
        ["Mild hypothermia", "~35-32C"],
        ["Moderate-severe", "<32C, risk of cardiac arrest"],
    ])},
    "first-aid-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Avalanche burial resuscitation", "Survival odds drop sharply after 15 minutes without an air pocket"],
    ])},
    "first-aid-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Submersion injury management", "Focuses on airway and oxygenation, since drowning outcomes hinge on hypoxia duration"],
    ])},
    "first-aid-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Snakebite protocol", "Keeps the patient calm, immobilizes the limb, and prioritizes rapid antivenom access"],
    ])},
    "first-aid-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Marine toxin exposure", "Management protocols vary by species (jellyfish, stingray, cone snail)"],
    ])},
    "first-aid-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Epinephrine pharmacokinetics", "Intramuscular epinephrine's onset and duration guide anaphylaxis dosing intervals"],
    ])},
    "first-aid-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Naloxone dosing strategy", "Titrates dose to reverse respiratory depression while minimizing withdrawal severity"],
    ])},
    "first-aid-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Organophosphate antidote", "Atropine and pralidoxime counter nerve agent/pesticide poisoning"],
    ])},
    "first-aid-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Hyperbaric therapy (CO poisoning)", "Uses pressurized oxygen to accelerate carbon monoxide clearance from the blood"],
    ])},
    "first-aid-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Cyanide antidote kit", "Uses agents like hydroxocobalamin to neutralize cyanide's blockage of cellular respiration"],
    ])},
    "first-aid-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Decompression sickness", "Nitrogen bubble formation from rapid ascent, treated with hyperbaric oxygen therapy"],
    ])},
    "first-aid-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Rapid cooling (heat stroke)", "Cold water immersion is the most effective technique for rapidly lowering core temperature"],
    ])},
    "first-aid-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Prehospital glucose management", "Protocols for treating hypoglycemia and hyperglycemia before hospital arrival"],
    ])},
    "first-aid-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Prehospital seizure management", "Protocols for airway protection and benzodiazepine use during active seizures"],
    ])},
    "first-aid-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Prehospital stroke scale", "Validated tools (e.g. Cincinnati) for rapidly identifying likely stroke in the field"],
    ])},
    "first-aid-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["12-lead ECG triage", "Prehospital ECG identifies STEMI early to activate rapid cardiac catheterization"],
    ])},
    "first-aid-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Sepsis bundle compliance", "Measures adherence to time-sensitive sepsis care protocols in the field"],
    ])},
    "first-aid-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Field hospital deployment", "Logistics for rapidly establishing emergency medical capacity during a disaster"],
    ])},
    "first-aid-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["CBRN decontamination", "Systematic procedures for removing chemical, biological, radiological, or nuclear contamination"],
    ])},
    "first-aid-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Radiation dosimetry triage", "Estimates radiation exposure to prioritize casualties for treatment"],
    ])},
    "first-aid-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Primary blast lung", "Lung injury caused directly by a blast's pressure wave"],
    ])},
    "first-aid-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Weight-based pediatric dosing", "Tools like length-based tapes standardize medication dosing for children in emergencies"],
    ])},
    "first-aid-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Precipitous delivery", "Very rapid childbirth managed in the field, supporting the newborn's head and body"],
    ])},
    "first-aid-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Postpartum hemorrhage management", "Field techniques (uterine massage, medications) for controlling bleeding after birth"],
    ])},
    "first-aid-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Resuscitative thoracotomy", "An emergency chest-opening procedure for select traumatic cardiac arrest cases"],
    ])},
    "first-aid-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["FAST exam", "A rapid bedside ultrasound protocol for detecting internal bleeding after trauma"],
    ])},
    "first-aid-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Point-of-care lactate", "Elevated lactate levels help triage occult shock severity in trauma patients"],
    ])},
    "first-aid-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["CAT tourniquet design", "Traces the engineering evolution of the widely used combat application tourniquet"],
    ])},
    "first-aid-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Junctional hemorrhage device", "Specialized devices control bleeding at the groin, axilla, and neck where tourniquets can't reach"],
    ])},
    "first-aid-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Wound ballistics", "Studies how projectile physics determines gunshot wound patterns and severity"],
    ])},
    "first-aid-m2-l59": {"data_table": table(["Type", "Feature"], [
        ["Blunt trauma", "Force without penetration, e.g. from a collision"],
        ["Penetrating trauma", "Object breaches the body's surface"],
    ])},
    "first-aid-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Traumatic amputation management", "Controls bleeding first, then manages the amputated part for potential reattachment"],
    ])},
    "first-aid-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Electrical injury", "Can cause hidden internal damage and cardiac arrhythmia disproportionate to visible burns"],
    ])},
    "first-aid-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Lightning strike injury", "Produces distinct injury patterns, often requiring reverse triage due to cardiac arrest risk"],
    ])},
    "first-aid-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Anaphylactic shock differential", "Distinguishes anaphylaxis from other shock states by its rapid allergic trigger and hives"],
    ])},
    "first-aid-m2-l64": {"data_table": table(["Type", "Cause"], [
        ["Hemorrhagic", "Blood loss"],
        ["Cardiogenic", "Heart failing to pump"],
        ["Distributive", "Abnormal vessel dilation"],
        ["Obstructive", "Physical blockage of blood flow"],
    ])},
    "first-aid-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Ketamine analgesia", "Provides pain control in trauma while preserving airway reflexes and blood pressure"],
    ])},
    "first-aid-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Prehospital sedation protocol", "Standardized medication approaches for safely managing agitated patients"],
    ])},
    "first-aid-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Excited delirium syndrome", "A dangerous state of extreme agitation requiring careful medical, not just physical, management"],
    ])},
    "first-aid-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral de-escalation", "Verbal and environmental techniques for calming a behavioral emergency"],
    ])},
    "first-aid-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Bystander CPR training effectiveness", "Research on how training design affects real-world bystander CPR performance"],
    ])},
    "first-aid-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Public access defibrillation", "Program design for placing AEDs where cardiac arrests are most likely to occur"],
    ])},
    "first-aid-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["AED placement optimization", "Uses cardiac arrest data to strategically position defibrillators"],
    ])},
    "first-aid-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Good Samaritan law variation", "Legal protections for bystanders rendering aid differ by jurisdiction"],
    ])},
    "first-aid-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Community paramedicine", "Extends paramedic roles into preventive and follow-up care beyond emergency response"],
    ])},
    "first-aid-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Stop the Bleed evaluation", "Assesses the public health impact of hemorrhage control training campaigns"],
    ])},
    "first-aid-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Wilderness First Responder curriculum", "Designs training for prolonged, resource-limited backcountry medical care"],
    ])},
    "first-aid-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Care under fire doctrine", "Prioritizes stopping the threat and massive hemorrhage before other care in high-threat settings"],
    ])},
    "first-aid-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Prolonged field care", "Sustains a patient over hours/days when evacuation is delayed"],
    ])},
    "first-aid-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Telemedicine-guided prehospital care", "Connects field providers to remote physicians for real-time clinical guidance"],
    ])},
    "first-aid-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Drone medical logistics", "Uses drones to rapidly deliver emergency equipment to remote or inaccessible sites"],
    ])},
    "first-aid-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Bystander naloxone distribution", "Evaluates programs equipping laypeople to reverse opioid overdoses"],
    ])},
    "first-aid-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Pediatric choking technique", "Compares evidence for back blows, chest thrusts, and abdominal thrusts by age"],
    ])},
    "first-aid-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Special population airway obstruction", "Adapts foreign body airway management for pregnant, obese, or disabled patients"],
    ])},
    "first-aid-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Biphasic anaphylaxis", "Symptoms can recur hours after initial resolution, guiding observation protocols"],
    ])},
    "first-aid-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Frostbite field management", "Field protocols avoid refreezing thawed tissue and prioritize controlled rewarming"],
    ])},
    "first-aid-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Near-drowning pulmonary complications", "Requires monitoring for delayed lung injury even after apparent recovery"],
    ])},
    "first-aid-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Traumatic asphyxia", "Severe chest compression causing distinctive facial and neck injury patterns"],
    ])},
    "first-aid-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Prehospital pain scale validation", "Assesses which pain assessment tools work reliably in field trauma settings"],
    ])},
    "first-aid-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Mass gathering medicine", "Plans medical coverage for large public events based on predicted patient volume"],
    ])},
    "first-aid-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Search and rescue medical support", "Coordinates field treatment with evacuation logistics"],
    ])},
    "first-aid-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Confined space rescue", "Requires atmospheric monitoring and specialized medical coordination before entry"],
    ])},
    "first-aid-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["High-angle rescue medical coordination", "Integrates medical care with technical rope rescue systems"],
    ])},
    "first-aid-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Field amputation (entrapment)", "A last-resort procedure when extrication is otherwise impossible and life-threatening"],
    ])},
    "first-aid-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Triage tag systems", "Compares effectiveness of different color-coded systems for mass casualty prioritization"],
    ])},
    "first-aid-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Surge capacity planning", "Prepares healthcare systems to handle sudden spikes in patient volume during disasters"],
    ])},
    "first-aid-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Ethical triage", "Frameworks for making fair allocation decisions when resources cannot meet demand"],
    ])},
    "first-aid-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Simulation-based trauma training", "Uses realistic scenarios to improve trauma team performance and coordination"],
    ])},
    "first-aid-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Human factors in EMS error", "Studies how systemic and cognitive factors contribute to emergency response mistakes"],
    ])},
    "first-aid-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Cold chain management (field medications)", "Maintains required temperature control for medications deployed in field conditions"],
    ])},
    "first-aid-m2-l99": {"data_table": table(["Component", "Purpose"], [
        ["Doctoral thesis seminar", "Presents and defends original research contributing to emergency and first aid care"],
    ])},
    "first-aid-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Globe rupture management", "Field protocols shield rather than pressure a ruptured eye to prevent further damage"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"first-aid-m2-l{base_n}"
    worked_key = f"first-aid-m2-l{worked_n}"
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
        raise SystemExit(f"Lesson ids not found in level_m2.json First Aid: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 First Aid lessons.")


if __name__ == "__main__":
    main()
