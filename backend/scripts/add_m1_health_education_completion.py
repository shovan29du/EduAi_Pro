#!/usr/bin/env python3
"""Depth pass, M1 Health Education: fill in real, hand-checked
data_table content for the 99 M1 Health Education lessons not covered
by the earlier breadth-first batch. Brings M1 Health Education to
full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_health_education_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "health-education-m1-l1": {
        "data_table": table(["Field", "Feature"], [
            ["Health systems & policy", "Examines how care is organized, financed, and regulated"],
        ]),
    },
    "health-education-m1-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Advanced health science & epidemiology", "Applies rigorous population-level methods to study disease patterns"],
        ]),
    },
    "health-education-m1-l4": {
        "data_table": table(["Method", "Use"], [
            ["Survival analysis", "Models the time until an event of interest, such as death or relapse"],
        ]),
    },
    "health-education-m1-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Health policy analysis", "Evaluates the design, implementation, and impact of health policy decisions"],
        ]),
    },
    "health-education-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Health financing", "Studies how funds are raised, pooled, and allocated across a health system"],
        ]),
    },
    "health-education-m1-l7": {
        "data_table": table(["Field", "Focus"], [
            ["Implementation science", "Studies methods to promote uptake of evidence-based practice into routine care"],
        ]),
    },
    "health-education-m1-l8": {
        "data_table": table(["Method", "Feature"], [
            ["Mixed-methods research", "Combines qualitative and quantitative approaches within a single study"],
        ]),
    },
    "health-education-m1-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Global health governance", "Coordinates international policy and institutional response to health challenges"],
        ]),
    },
    "health-education-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Theory-based intervention design", "Grounds program strategy in established behavior change theory"],
        ]),
    },
    "health-education-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Advanced policy analysis method", "Applies structured frameworks to evaluate competing policy options"],
        ]),
    },
    "health-education-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Global health diplomacy", "Negotiates health cooperation across national and institutional boundaries"],
        ]),
    },
    "health-education-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Health financing reform", "Restructures funding mechanisms to improve access and system efficiency"],
        ]),
    },
    "health-education-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Implementation framework", "Provides structured models for translating research evidence into practice"],
        ]),
    },
    "health-education-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Causal inference", "Uses rigorous study design to distinguish true causation from mere association"],
        ]),
    },
    "health-education-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Health data science", "Applies machine learning and analytics to large-scale health datasets"],
        ]),
    },
    "health-education-m1-l17": {
        "data_table": table(["Field", "Focus"], [
            ["Public health law", "Examines the legal authority and constraints governing public health action"],
        ]),
    },
    "health-education-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Social determinants of health", "Income, education, and environment shape health outcomes beyond care access"],
        ]),
    },
    "health-education-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Health equity metric", "Quantifies disparities in outcomes across population groups"],
        ]),
    },
    "health-education-m1-l20": {
        "data_table": table(["Concept", "Detail"], [
            ["One Health approach", "Integrates human, animal, and environmental health to prevent zoonotic disease"],
        ]),
    },
    "health-education-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Planetary health", "Links large-scale environmental change directly to human disease risk"],
        ]),
    },
    "health-education-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Nutritional epidemiology", "Studies dietary pattern associations with disease at the population level"],
        ]),
    },
    "health-education-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Adolescent health intervention", "Must account for developmental stage and peer influence in program design"],
        ]),
    },
    "health-education-m1-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Aging population policy", "Health systems must adapt financing and delivery to shifting demographics"],
        ]),
    },
    "health-education-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["NCD surveillance", "Tracks chronic disease trends to guide long-term prevention policy"],
        ]),
    },
    "health-education-m1-l26": {
        "data_table": table(["Step", "Purpose"], [
            ["Outbreak investigation", "Identifies the source and mode of spread to contain a disease cluster"],
        ]),
    },
    "health-education-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Vaccine hesitancy", "Requires tailored communication addressing specific underlying concerns"],
        ]),
    },
    "health-education-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Health communication campaign", "Combines message design and channel selection to shift target audience behavior"],
        ]),
    },
    "health-education-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Social marketing", "Applies commercial marketing techniques to promote beneficial health behavior"],
        ]),
    },
    "health-education-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Health literacy assessment", "Measures a population's capacity to find, understand, and use health information"],
        ]),
    },
    "health-education-m1-l31": {
        "data_table": table(["Method", "Feature"], [
            ["Community-based participatory research", "Involves community members as active partners throughout the research process"],
        ]),
    },
    "health-education-m1-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Health coalition building", "Aligns diverse stakeholders around shared community health goals"],
        ]),
    },
    "health-education-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Occupational health program", "Reduces workplace injury and illness through systematic hazard control"],
        ]),
    },
    "health-education-m1-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Air quality intervention", "Reduces exposure to pollutants linked with respiratory disease burden"],
        ]),
    },
    "health-education-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Mental health promotion", "Builds population-level resilience and wellbeing, not just treating illness"],
        ]),
    },
    "health-education-m1-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["Substance use prevention", "Early education reduces risk of later substance misuse"],
        ]),
    },
    "health-education-m1-l37": {
        "data_table": table(["Policy", "Detail"], [
            ["Tobacco control policy", "Taxation, advertising limits, and smoke-free laws reduce smoking rates"],
        ]),
    },
    "health-education-m1-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["Alcohol harm reduction", "Minimizes negative consequences of alcohol use without requiring full abstinence"],
        ]),
    },
    "health-education-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Reproductive health program design", "Combines education, access, and policy to support informed reproductive choice"],
        ]),
    },
    "health-education-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["HIV prevention evaluation", "Measures reduction in transmission against defined program benchmarks"],
        ]),
    },
    "health-education-m1-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["STI surveillance system", "Tracks infection trends to guide targeted screening and treatment"],
        ]),
    },
    "health-education-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["School health program", "Integrates health services and education directly into the school setting"],
        ]),
    },
    "health-education-m1-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["Workplace health promotion", "Leverages employer settings to deliver preventive health programming at scale"],
        ]),
    },
    "health-education-m1-l44": {
        "data_table": table(["Stage", "Feature"], [
            ["Precontemplation", "Not yet considering behavior change"],
            ["Action", "Actively modifying behavior"],
        ]),
    },
    "health-education-m1-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Social cognitive theory", "Behavior change is shaped by self-efficacy and observational learning"],
        ]),
    },
    "health-education-m1-l46": {
        "data_table": table(["Component", "Detail"], [
            ["Health Belief Model", "Behavior change depends on perceived susceptibility, severity, and benefits"],
        ]),
    },
    "health-education-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Diffusion of innovations", "New health practices spread through a population via identifiable adopter categories"],
        ]),
    },
    "health-education-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Social ecological model", "Addresses individual, interpersonal, community, and policy levels together"],
        ]),
    },
    "health-education-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Motivational interviewing", "A collaborative counseling style that strengthens a person's own motivation to change"],
        ]),
    },
    "health-education-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Health coaching", "Supports individualized behavior change through structured, ongoing guidance"],
        ]),
    },
    "health-education-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Physical activity promotion", "Combines environmental and individual strategies to increase population activity levels"],
        ]),
    },
    "health-education-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Obesity environmental approach", "Targets food and physical activity environments rather than individuals alone"],
        ]),
    },
    "health-education-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Food systems policy", "Shapes population nutrition through agriculture, retail, and regulatory levers"],
        ]),
    },
    "health-education-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Food insecurity measurement", "Standardized survey tools quantify inconsistent access to adequate food"],
        ]),
    },
    "health-education-m1-l55": {
        "data_table": table(["Element", "Purpose"], [
            ["Logic model", "Maps program inputs, activities, and outcomes to guide evaluation"],
        ]),
    },
    "health-education-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Cost-effectiveness analysis", "Compares health programs by outcome achieved per unit of cost"],
        ]),
    },
    "health-education-m1-l57": {
        "data_table": table(["Element", "Purpose"], [
            ["Grant proposal", "Communicates a program's need, plan, and impact to secure funding"],
        ]),
    },
    "health-education-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Global Burden of Disease methodology", "Standardizes comparison of health loss across diseases and regions"],
        ]),
    },
    "health-education-m1-l59": {
        "data_table": table(["Metric", "Meaning"], [
            ["DALY", "Disability-Adjusted Life Year, combining years lost to death and disability"],
            ["QALY", "Quality-Adjusted Life Year, weighting survival by health-related quality of life"],
        ]),
    },
    "health-education-m1-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Public health emergency response", "Coordinates surveillance, care, and resource allocation during a disaster"],
        ]),
    },
    "health-education-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Antimicrobial resistance strategy", "Combines stewardship, surveillance, and innovation to slow resistant pathogen spread"],
        ]),
    },
    "health-education-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Neglected tropical disease control", "Targets diseases disproportionately affecting impoverished populations"],
        ]),
    },
    "health-education-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Health system strengthening", "Builds core capacity across financing, workforce, and service delivery"],
        ]),
    },
    "health-education-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Universal health coverage", "Ensures access to needed health services without financial hardship"],
        ]),
    },
    "health-education-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Alma-Ata Declaration", "A landmark 1978 commitment establishing primary health care as a global goal"],
        ]),
    },
    "health-education-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Telehealth intervention design", "Delivers care remotely while addressing access and technology barriers"],
        ]),
    },
    "health-education-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Mobile health evaluation", "Assesses whether app or SMS-based interventions achieve intended health outcomes"],
        ]),
    },
    "health-education-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Health information interoperability", "Enables different health data systems to exchange information reliably"],
        ]),
    },
    "health-education-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["EHR-based surveillance", "Uses electronic health records to detect population-level health trends"],
        ]),
    },
    "health-education-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Health disparities research", "Documents and explains unequal health outcomes across population groups"],
        ]),
    },
    "health-education-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Rural health delivery model", "Addresses distance and provider shortage barriers to care access"],
        ]),
    },
    "health-education-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["Cultural safety", "Health programs must respect and adapt to indigenous cultural context"],
        ]),
    },
    "health-education-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Refugee health program", "Addresses trauma, language, and legal barriers unique to displaced populations"],
        ]),
    },
    "health-education-m1-l74": {
        "data_table": table(["Concept", "Detail"], [
            ["Inclusive health program design", "Removes physical and communication barriers for people with disabilities"],
        ]),
    },
    "health-education-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Gender-based violence prevention", "Combines survivor support with structural strategies to reduce future incidence"],
        ]),
    },
    "health-education-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["LGBTQ+ cultural competency", "Health providers require specific training to reduce care disparities"],
        ]),
    },
    "health-education-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["School health curriculum", "Sequences age-appropriate health content across grade levels"],
        ]),
    },
    "health-education-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Peer education", "Trained peers often achieve higher credibility with target audiences than outside experts"],
        ]),
    },
    "health-education-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["Health marketing", "Applies consumer behavior insight to promote wellness products and services"],
        ]),
    },
    "health-education-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Corporate wellness program", "Evaluates health outcomes and cost impact of employer-sponsored initiatives"],
        ]),
    },
    "health-education-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Injury prevention program", "Targets modifiable risk factors to reduce unintentional injury rates"],
        ]),
    },
    "health-education-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Road traffic safety intervention", "Combines engineering, enforcement, and education to reduce crash injury"],
        ]),
    },
    "health-education-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Falls prevention", "Targets balance, home hazards, and medication review in older adults"],
        ]),
    },
    "health-education-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Gatekeeper training", "Trains community members to recognize and respond to suicide risk warning signs"],
        ]),
    },
    "health-education-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Health policy advocacy", "Requires understanding the legislative process to influence health law"],
        ]),
    },
    "health-education-m1-l86": {
        "data_table": table(["Body", "Role"], [
            ["Institutional review board", "Oversees research ethics to protect human research subjects"],
        ]),
    },
    "health-education-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Public health surveillance ethics", "Balances population monitoring benefits against individual privacy concerns"],
        ]),
    },
    "health-education-m1-l88": {
        "data_table": table(["Framework", "Purpose"], [
            ["International Health Regulations", "Binding framework coordinating countries' response to global health threats"],
        ]),
    },
    "health-education-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Health system resilience", "A system's capacity to absorb and adapt to sudden external shocks"],
        ]),
    },
    "health-education-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Community resilience building", "Strengthens local capacity to withstand and recover from public health emergencies"],
        ]),
    },
    "health-education-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Public health workforce development", "Trains and retains skilled personnel critical to system function"],
        ]),
    },
    "health-education-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Program sustainability planning", "Secures long-term funding and institutional support beyond initial launch"],
        ]),
    },
    "health-education-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Population health management", "Coordinates care across a defined population to improve aggregate outcomes"],
        ]),
    },
    "health-education-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Stigma reduction", "Menstrual health programs must address cultural taboos alongside practical access"],
        ]),
    },
    "health-education-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental justice", "Maps unequal environmental risk exposure across communities"],
        ]),
    },
    "health-education-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Digital contact tracing ethics", "Balances outbreak control effectiveness against data privacy protection"],
        ]),
    },
    "health-education-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Visual communication design", "Reduces reliance on text literacy for effective health messaging"],
        ]),
    },
    "health-education-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Community health worker scaling", "Extends trusted local health workers' reach across larger populations"],
        ]),
    },
    "health-education-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Climate-resilient health system", "Adapts infrastructure and services to withstand climate-driven health threats"],
        ]),
    },
    "health-education-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Workplace mental health stigma reduction", "Structured programs improve help-seeking behavior among employees"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Term", "Meaning"], [
        ["Incidence", "Number of new cases in a population over a time period"],
        ["Prevalence", "Total number of existing cases at a given time"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"health-education-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"health-education-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"health-education-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Health Education lessons (completing 120/120).")


if __name__ == "__main__":
    main()
