#!/usr/bin/env python3
"""Depth pass, M1 Project Management: fill in real, hand-checked
data_table content for the 119 M1 Project Management lessons not
covered by the earlier breadth-first batch. Brings M1 Project
Management to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
portfolio/program management, quantitative risk and scheduling,
stakeholder and change leadership, and applied domains (construction,
IT, megaprojects); l101-l120 are "Worked Analysis" companions reusing
the data_table of l1-l20 (direct 1:1 mapping). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_project_management_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Prioritization Framework", "Basis for Prioritization"], [
    ["MoSCoW", "Must have, Should have, Could have, Won't have"],
    ["Weighted scoring", "Numeric scores across weighted criteria"],
])

CHARTS: dict[str, dict] = {
    "project-management-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Portfolio management", "Selects and balances a set of projects to maximize strategic value"],
    ])},
    "project-management-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Program management", "Coordinates a group of related projects to achieve benefits not available individually"],
    ])},
    "project-management-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Portfolio balancing", "Allocates limited resources across projects to optimize overall portfolio value"],
    ])},
    "project-management-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Benefits realization management", "Ensures a project's intended business benefits are actually achieved and tracked"],
    ])},
    "project-management-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Program governance", "Defines decision rights and oversight structures across a program's projects"],
    ])},
    "project-management-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Program roadmap", "Sequences a program's projects and milestones over time"],
    ])},
    "project-management-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Interdependency management", "Tracks and coordinates dependencies between related projects"],
    ])},
    "project-management-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["PMO", "A Project Management Office that standardizes practices and governance across projects"],
    ])},
    "project-management-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["PMO maturity model", "Assesses how advanced an organization's project management office capabilities are"],
    ])},
    "project-management-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Organizational PM maturity", "Measures how consistently an organization applies effective project practices"],
    ])},
    "project-management-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Strategic alignment", "Ensures every project directly supports the organization's business goals"],
    ])},
    "project-management-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Business case", "Justifies a project's investment by weighing its expected costs and benefits"],
    ])},
    "project-management-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise PM tool selection", "Evaluates project software against organizational scale and integration needs"],
    ])},
    "project-management-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["AI/automation in PM", "Uses AI tools to assist scheduling, risk prediction, and status reporting"],
    ])},
    "project-management-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Data-driven portfolio decisions", "Uses quantitative evidence rather than intuition to prioritize projects"],
    ])},
    "project-management-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Multi-vendor program management", "Coordinates deliverables and risk across several external vendors"],
    ])},
    "project-management-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Global/multi-site program management", "Manages coordination challenges across geographically distributed teams"],
    ])},
    "project-management-m1-l19": {"data_table": table(["Certification", "Focus"], [
        ["PMP", "Broad, process-based project management certification"],
        ["PRINCE2", "Structured, stage-gated project management methodology"],
    ])},
    "project-management-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Multi-project simulation", "Practices delivering several interdependent projects within one program"],
    ])},
    "project-management-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Earned value management", "Measures project performance by comparing planned, earned, and actual costs"],
    ])},
    "project-management-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Monte Carlo schedule simulation", "Runs many randomized scenarios to estimate the range of possible schedule outcomes"],
    ])},
    "project-management-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Decision tree risk analysis", "Maps sequential risk decisions and their probable outcomes"],
    ])},
    "project-management-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Wagile", "Combines waterfall's upfront planning with agile's iterative delivery"],
    ])},
    "project-management-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["SAFe", "Scaled Agile Framework; coordinates agile teams across a large enterprise"],
    ])},
    "project-management-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Kanban", "Visualizes and limits work-in-progress to optimize continuous flow of delivery"],
    ])},
    "project-management-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Lean portfolio management", "Applies lean principles to fund and govern a portfolio of agile initiatives"],
    ])},
    "project-management-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Stakeholder salience modeling", "Ranks stakeholders by their power, legitimacy, and urgency"],
    ])},
    "project-management-m1-l29": {"data_table": table(["Axis", "Meaning"], [
        ["Power-interest grid", "Plots stakeholders by influence and level of interest to guide engagement strategy"],
    ])},
    "project-management-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Conflict resolution framework", "A structured approach for resolving disagreements within a project team"],
    ])},
    "project-management-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Negotiation theory", "Studies principled approaches to reaching mutually acceptable agreements"],
    ])},
    "project-management-m1-l32": {"data_table": table(["Contract Type", "Risk allocation"], [
        ["Fixed-price", "Places cost overrun risk on the vendor"],
        ["Cost-reimbursable", "Places cost overrun risk on the buyer"],
    ])},
    "project-management-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Claims management", "Formally resolves disputes over contract obligations and compensation"],
    ])},
    "project-management-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Earned schedule", "Extends earned value management to report schedule performance in time units"],
    ])},
    "project-management-m1-l35": {"data_table": table(["Technique", "Feature"], [
        ["Resource leveling", "Delays tasks to resolve resource over-allocation, possibly extending the schedule"],
        ["Resource smoothing", "Adjusts tasks within slack to balance resource use without changing the end date"],
    ])},
    "project-management-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Theory of constraints", "Focuses improvement effort on the single bottleneck limiting overall throughput"],
    ])},
    "project-management-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Systems thinking", "Views a project as an interconnected system rather than isolated tasks"],
    ])},
    "project-management-m1-l38": {"data_table": table(["Domain", "Feature"], [
        ["Cynefin framework", "Categorizes problems as simple, complicated, complex, or chaotic to guide decision approach"],
    ])},
    "project-management-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Project complexity assessment", "Systematically rates factors that make a project harder to manage"],
    ])},
    "project-management-m1-l40": {"data_table": table(["Model", "Feature"], [
        ["Kotter's 8-step", "A sequential process for leading large-scale organizational change"],
        ["ADKAR", "Focuses change on individual Awareness, Desire, Knowledge, Ability, Reinforcement"],
    ])},
    "project-management-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Virtual team leadership", "Manages coordination, trust, and communication across a distributed team"],
    ])},
    "project-management-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Psychological safety", "A team climate where members feel safe to speak up without fear of punishment"],
    ])},
    "project-management-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Servant leadership", "Prioritizes removing obstacles and supporting the team over directing them"],
    ])},
    "project-management-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Project governance and ethics", "Establishes accountable decision-making structures and ethical standards"],
    ])},
    "project-management-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Fraud detection in project finance", "Identifies irregular financial controls that may indicate misuse of funds"],
    ])},
    "project-management-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Project auditing", "Independently reviews a project's processes and controls for compliance and effectiveness"],
    ])},
    "project-management-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["ISO 21500/21502", "International standards providing guidance on project management practice"],
    ])},
    "project-management-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Six Sigma DMAIC", "Define, Measure, Analyze, Improve, Control; a structured quality improvement process"],
    ])},
    "project-management-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Configuration management", "Tracks and controls changes to a project's deliverables and baselines"],
    ])},
    "project-management-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Requirements traceability matrix", "Links each requirement to its source and verification to ensure nothing is missed"],
    ])},
    "project-management-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Systems engineering integration", "Aligns project management with the technical rigor of systems engineering"],
    ])},
    "project-management-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Megaproject cost overrun theory", "Studies why very large projects systematically exceed budget and schedule"],
    ])},
    "project-management-m1-l53": {"data_table": table(["Model", "Feature"], [
        ["PPP", "Public-Private Partnership; shares infrastructure delivery risk between sectors"],
        ["DBFO", "Design-Build-Finance-Operate; a single contractor delivers the full project lifecycle"],
    ])},
    "project-management-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Construction scheduling technique", "Applies methods like critical path to sequence physical build activities"],
    ])},
    "project-management-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["IT project risk factors", "Common causes of failure specific to software and technology delivery"],
    ])},
    "project-management-m1-l56": {"data_table": table(["Method", "Feature"], [
        ["COCOMO", "Estimates software effort from lines-of-code and project attributes"],
        ["Function points", "Estimates effort from a system's functional complexity"],
    ])},
    "project-management-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Vendor performance management", "Systematically evaluates and manages supplier delivery and quality"],
    ])},
    "project-management-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain risk integration", "Incorporates supplier and logistics risk directly into project planning"],
    ])},
    "project-management-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Crisis management / business continuity", "Prepares a project to continue functioning through major disruption"],
    ])},
    "project-management-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["ESG integration", "Incorporates environmental, social, and governance criteria into project decisions"],
    ])},
    "project-management-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Carbon footprint assessment", "Measures a project's greenhouse gas emissions across its delivery"],
    ])},
    "project-management-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Benefits management (extended)", "Manages benefits beyond initial realization, including sustaining value over time"],
    ])},
    "project-management-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Value engineering", "Systematically improves a design's value by optimizing function relative to cost"],
    ])},
    "project-management-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Cost-benefit analysis", "Weighs a capital project's expected costs against its expected benefits"],
    ])},
    "project-management-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Real options analysis", "Values the flexibility to adapt an investment decision as new information arrives"],
    ])},
    "project-management-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Linear programming (portfolio)", "Mathematically optimizes project selection under resource constraints"],
    ])},
    "project-management-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["RCPSP", "Resource-Constrained Project Scheduling Problem; schedules tasks under limited resource availability"],
    ])},
    "project-management-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Multi-project critical path", "Extends critical path analysis across several interdependent projects sharing resources"],
    ])},
    "project-management-m1-l69": {"data_table": table(["Model", "Focus"], [
        ["OPM3", "Assesses organizational project management maturity"],
        ["P3M3", "Assesses portfolio, program, and project management maturity"],
    ])},
    "project-management-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Lessons learned knowledge management", "Captures and reuses insights from past projects to improve future ones"],
    ])},
    "project-management-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Community of practice", "A group sharing project management knowledge and best practice across an organization"],
    ])},
    "project-management-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral economics in PM", "Applies predictable human biases to understand project decision-making"],
    ])},
    "project-management-m1-l73": {"data_table": table(["Bias", "Effect"], [
        ["Optimism bias", "Systematically underestimates project cost and duration"],
    ])},
    "project-management-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Escalation of commitment", "Continuing to invest in a failing project because of prior sunk investment"],
    ])},
    "project-management-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["PMO value demonstration", "Quantifies the tangible benefit a project management office delivers"],
    ])},
    "project-management-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Balanced scorecard (project)", "Tracks project performance across financial, customer, process, and learning views"],
    ])},
    "project-management-m1-l77": {"data_table": table(["Metric", "Measures"], [
        ["Velocity", "Amount of work an agile team completes per iteration"],
        ["Burn-down", "Remaining work over time toward a deadline"],
    ])},
    "project-management-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Hybrid governance (digital transformation)", "Combines agile and traditional oversight for large transformation programs"],
    ])},
    "project-management-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Technical debt in programs", "Accumulated shortcuts that slow future delivery within a long-running program"],
    ])},
    "project-management-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Stage-gate process", "Reviews an innovation project at defined checkpoints before it proceeds to the next phase"],
    ])},
    "project-management-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["R&D portfolio management", "Balances research investments across risk levels and time horizons"],
    ])},
    "project-management-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["New product development framework", "Structures the stages from idea generation to product launch"],
    ])},
    "project-management-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["M&A integration project management", "Coordinates combining two organizations' systems, teams, and processes"],
    ])},
    "project-management-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Post-merger integration governance", "Oversees the structured execution of merging two organizations"],
    ])},
    "project-management-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Crisis communication planning", "Prepares clear, timely messaging for stakeholders during a program disruption"],
    ])},
    "project-management-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Risk appetite and tolerance", "Defines how much risk a portfolio is willing to accept in pursuit of its goals"],
    ])},
    "project-management-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise risk management integration", "Aligns project-level risk management with organization-wide risk oversight"],
    ])},
    "project-management-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Scenario planning (strategic)", "Explores multiple plausible futures to stress-test a program's strategy"],
    ])},
    "project-management-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Digital twin (project simulation)", "A virtual model of a project used to simulate and monitor real-world performance"],
    ])},
    "project-management-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Blockchain in contract management", "Uses distributed ledgers to record and verify contract terms and milestones"],
    ])},
    "project-management-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["AI-assisted scheduling optimization", "Uses AI to suggest more efficient project schedules than manual planning"],
    ])},
    "project-management-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["NLP for status reporting", "Automatically summarizes project updates from unstructured text sources"],
    ])},
    "project-management-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Predictive risk forecasting", "Uses historical data models to anticipate project risks before they occur"],
    ])},
    "project-management-m1-l94": {"data_table": table(["Industry", "Constraint"], [
        ["Pharma/aerospace PM", "Must satisfy strict regulatory approval processes throughout delivery"],
    ])},
    "project-management-m1-l95": {"data_table": table(["Standard", "Origin"], [
        ["PMI", "United States-based project management body of knowledge"],
        ["IPMA / PRINCE2", "European-originated competency and methodology frameworks"],
    ])},
    "project-management-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Advanced retrospective facilitation", "Guides teams through structured reflection to improve future delivery"],
    ])},
    "project-management-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Agile outcome-based contract", "Ties vendor payment to delivered value rather than fixed deliverables"],
    ])},
    "project-management-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Space systems project delivery", "Manages the extreme technical risk and long timelines of satellite programs"],
    ])},
    "project-management-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Public project stakeholder communication", "Manages messaging for politically sensitive, publicly funded projects"],
    ])},
    "project-management-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge transfer during turnover", "Preserves critical project knowledge when team members leave"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"project-management-m1-l{base_n}"
    worked_key = f"project-management-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Project Management"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Project Management: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Project Management lessons (completing 120/120).")


if __name__ == "__main__":
    main()
