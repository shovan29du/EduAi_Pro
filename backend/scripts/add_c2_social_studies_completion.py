#!/usr/bin/env python3
"""Depth pass, C2 Social Studies: fill in real, hand-checked
data_table content for the 69 C2 Social Studies lessons not covered
by the earlier breadth-first batch. Brings C2 Social Studies to full
70/70 coverage.

l61-l70 are "Worked Analysis" companions to l1-l10. l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "social-studies-c2-l1": {
        "data_table": table(["Concept", "Detail"], [
            ["Culture & identity", "Shared beliefs, practices, and symbols shape group and individual identity"],
        ]),
    },
    "social-studies-c2-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["Comparative social systems", "Societies organize labor, family, and authority in differing structures"],
        ]),
    },
    "social-studies-c2-l4": {
        "data_table": table(["Concept", "Function"], [
            ["Ritual", "Reinforces shared meaning and group cohesion through repeated symbolic action"],
        ]),
    },
    "social-studies-c2-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Social mobility", "Movement between social class positions across or within generations"],
        ]),
    },
    "social-studies-c2-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Ethnic boundary", "Socially constructed distinction marking who belongs to a group"],
        ]),
    },
    "social-studies-c2-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["Gender socialization", "Process by which individuals learn gender norms from family, media, and peers"],
        ]),
    },
    "social-studies-c2-l8": {
        "data_table": table(["Concept", "Detail"], [
            ["Conformity", "Adjusting behavior or belief to align with a group's perceived norms"],
        ]),
    },
    "social-studies-c2-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Collective action", "Coordinated group effort toward a shared social or political goal"],
        ]),
    },
    "social-studies-c2-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Community life", "Local social ties shape trust, support networks, and civic participation"],
        ]),
    },
    "social-studies-c2-l11": {
        "data_table": table(["Structure", "Feature"], [
            ["Nuclear family", "Two parents and children forming an independent household"],
            ["Extended family", "Multiple generations or relatives sharing close ties or a household"],
        ]),
    },
    "social-studies-c2-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Labeling theory", "Deviance is shaped by how behavior is socially defined and reacted to"],
        ]),
    },
    "social-studies-c2-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Cultural hybridity", "Blending of cultural elements through global exchange and migration"],
        ]),
    },
    "social-studies-c2-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Random sampling", "Selects participants so every individual has an equal chance of inclusion"],
        ]),
    },
    "social-studies-c2-l15": {
        "data_table": table(["Structure", "Feature"], [
            ["Age pyramid", "Visualizes population distribution by age and sex"],
        ]),
    },
    "social-studies-c2-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Media framing", "How an issue is presented shapes public perception and opinion"],
        ]),
    },
    "social-studies-c2-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Hidden curriculum", "Schools transmit social norms and values beyond stated academic content"],
        ]),
    },
    "social-studies-c2-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Labor union", "Organized workers negotiating collectively for pay and conditions"],
        ]),
    },
    "social-studies-c2-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Religious institution", "Organizes belief and practice while shaping community identity"],
        ]),
    },
    "social-studies-c2-l20": {
        "data_table": table(["Model", "Feature"], [
            ["Social-democratic welfare model", "Broad universal benefits funded through high taxation"],
            ["Liberal welfare model", "Means-tested benefits with reliance on market provision"],
        ]),
    },
    "social-studies-c2-l21": {
        "data_table": table(["Institution", "Function"], [
            ["Comparative political institution", "Structures how power is distributed and exercised across systems"],
        ]),
    },
    "social-studies-c2-l22": {
        "data_table": table(["Theory", "View of the State"], [
            ["Pluralist theory", "Power is distributed among competing interest groups"],
            ["Elite theory", "Power concentrates among a small, cohesive group"],
        ]),
    },
    "social-studies-c2-l23": {
        "data_table": table(["Theory", "Focus"], [
            ["Rational choice voting", "Voters choose based on perceived self-interest"],
        ]),
    },
    "social-studies-c2-l24": {
        "data_table": table(["Theory", "Core Idea"], [
            ["Realism", "States act primarily out of self-interest and power competition"],
            ["Liberalism (IR)", "Cooperation and institutions can moderate state conflict"],
        ]),
    },
    "social-studies-c2-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Global governance", "Coordination among states and institutions without a central world government"],
        ]),
    },
    "social-studies-c2-l26": {
        "data_table": table(["Mechanism", "Role"], [
            ["Human rights enforcement", "Relies on treaties, courts, and international pressure rather than a single authority"],
        ]),
    },
    "social-studies-c2-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Marginal utility", "The added satisfaction from consuming one more unit of a good"],
        ]),
    },
    "social-studies-c2-l28": {
        "data_table": table(["Tool", "Purpose"], [
            ["Monetary policy", "Central bank adjusts interest rates to influence inflation and growth"],
        ]),
    },
    "social-studies-c2-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Behavioral economics", "Studies how psychological biases shape real economic decision-making"],
        ]),
    },
    "social-studies-c2-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Development economics", "Examines growth, poverty, and institutions in lower-income economies"],
        ]),
    },
    "social-studies-c2-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Advanced urban geography", "Examines spatial patterns of inequality and land use in cities"],
        ]),
    },
    "social-studies-c2-l32": {
        "data_table": table(["Theory", "Focus"], [
            ["Migration push-pull theory", "Explains movement through factors driving departure and attraction"],
        ]),
    },
    "social-studies-c2-l33": {
        "data_table": table(["Theory", "Core Idea"], [
            ["Strain theory", "Crime results from a gap between societal goals and legitimate means to achieve them"],
        ]),
    },
    "social-studies-c2-l34": {
        "data_table": table(["Approach", "Detail"], [
            ["Restorative justice", "Focuses on repairing harm through dialogue rather than solely punishment"],
        ]),
    },
    "social-studies-c2-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Welfare policy analysis", "Evaluates trade-offs between coverage, cost, and work incentives"],
        ]),
    },
    "social-studies-c2-l36": {
        "data_table": table(["Regime Type", "Feature"], [
            ["Conservative welfare regime", "Benefits tied to employment status and family structure"],
        ]),
    },
    "social-studies-c2-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Social capital", "Networks of trust and reciprocity that enable collective action"],
        ]),
    },
    "social-studies-c2-l38": {
        "data_table": table(["Model", "Feature"], [
            ["Comparative education policy", "Countries balance access, equity, and quality differently"],
        ]),
    },
    "social-studies-c2-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental justice", "Examines unequal exposure to environmental harm across social groups"],
        ]),
    },
    "social-studies-c2-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Political economy of development", "Examines how power and institutions shape economic outcomes"],
        ]),
    },
    "social-studies-c2-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Institutional analysis", "Examines how formal and informal rules shape social outcomes"],
        ]),
    },
    "social-studies-c2-l42": {
        "data_table": table(["Method", "Detail"], [
            ["Participant observation", "Researcher engages directly within a community to gather data"],
        ]),
    },
    "social-studies-c2-l43": {
        "data_table": table(["Theory", "Core Idea"], [
            ["Bourdieu's capital theory", "Class reproduction operates through economic, social, and cultural capital"],
        ]),
    },
    "social-studies-c2-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Ethnic conflict", "Group boundaries can be politicized and mobilized toward violence"],
        ]),
    },
    "social-studies-c2-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Life course theory", "Individual trajectories are shaped by historical timing and social context"],
        ]),
    },
    "social-studies-c2-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Intergenerational equity", "Balances resource allocation and obligations across age cohorts"],
        ]),
    },
    "social-studies-c2-l47": {
        "data_table": table(["Model", "Feature"], [
            ["Social model of disability", "Locates disability in societal barriers rather than individual impairment"],
        ]),
    },
    "social-studies-c2-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Immigrant integration", "Measured across economic, social, and civic participation dimensions"],
        ]),
    },
    "social-studies-c2-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Consumer culture", "Identity and status become expressed through consumption patterns"],
        ]),
    },
    "social-studies-c2-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Popular culture analysis", "Examines media's role in shaping and reflecting social values"],
        ]),
    },
    "social-studies-c2-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Social network analysis", "Maps relationships to study influence and information flow"],
        ]),
    },
    "social-studies-c2-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Nonprofit governance", "Balances mission accountability with sustainable funding and oversight"],
        ]),
    },
    "social-studies-c2-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Social determinants of health", "Income, education, and environment shape health outcomes"],
        ]),
    },
    "social-studies-c2-l54": {
        "data_table": table(["Approach", "Detail"], [
            ["Conflict resolution", "Uses mediation and negotiation to de-escalate disputes"],
        ]),
    },
    "social-studies-c2-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Indigenous sovereignty", "Self-governance rights rooted in prior and continuing occupancy of land"],
        ]),
    },
    "social-studies-c2-l56": {
        "data_table": table(["Method", "Detail"], [
            ["Regression analysis", "Estimates the relationship between variables in quantitative research"],
        ]),
    },
    "social-studies-c2-l57": {
        "data_table": table(["Method", "Detail"], [
            ["Grounded theory", "Builds theory inductively from qualitative data patterns"],
        ]),
    },
    "social-studies-c2-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Program evaluation", "Systematically assesses whether a policy achieves its intended outcomes"],
        ]),
    },
    "social-studies-c2-l59": {
        "data_table": table(["Method", "Detail"], [
            ["Comparative case study", "Analyzes similarities and differences across a small set of political systems"],
        ]),
    },
    "social-studies-c2-l60": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone research seminar", "Applies social science methods to an original research question"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Sociological Perspective", "Core Idea"], [
    ["Functionalism", "Society is a system of interdependent parts working together"],
    ["Conflict theory", "Society is shaped by competition over scarce resources"],
    ["Symbolic interactionism", "Society is built from everyday interactions and meaning-making"],
])

# l61-l70 "Worked Analysis" lessons reuse the data_table of l1-l10.
WORKED_ANALYSIS_MAP = {61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"social-studies-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"social-studies-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"social-studies-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Social Studies lessons (completing 70/70).")


if __name__ == "__main__":
    main()
