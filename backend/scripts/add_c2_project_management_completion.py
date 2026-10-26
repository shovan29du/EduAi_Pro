#!/usr/bin/env python3
"""Depth pass, C2 Project Management: fill in real, hand-checked
data_table content for the 69 C2 Project Management lessons not covered
by the earlier breadth-first batch. Brings C2 Project Management to full
70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_project_management_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "project-management-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Scope management", "Defines and controls what is and isn't included in a project"],
        ]),
    },
    "project-management-c2-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Schedule management", "Plans, sequences, and controls the timing of project activities"],
        ]),
    },
    "project-management-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Scope creep", "Uncontrolled expansion of project scope without corresponding adjustments"],
        ]),
    },
    "project-management-c2-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Work package", "The smallest unit of work in a work breakdown structure"],
        ]),
    },
    "project-management-c2-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Critical path", "The longest sequence of dependent tasks determining the minimum project duration"],
        ]),
    },
    "project-management-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Critical chain", "Manages project schedules by accounting for resource constraints, not just task dependencies"],
        ]),
    },
    "project-management-c2-l8": {
        "data_table": table(["Technique", "Meaning"], [
            ["Crashing", "Adds resources to shorten a schedule, increasing cost"], ["Fast-tracking", "Runs sequential tasks in parallel, increasing risk"],
        ]),
    },
    "project-management-c2-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Precedence diagramming method", "Visualizes task dependencies using nodes and connecting arrows"],
        ]),
    },
    "project-management-c2-l10": {
        "data_table": table(["Technique", "Purpose"], [
            ["Resource leveling", "Adjusts a schedule to resolve resource over-allocation"], ["Resource smoothing", "Adjusts within available float without changing the critical path"],
        ]),
    },
    "project-management-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Baseline", "The approved original plan used as a reference point for measuring performance"],
        ]),
    },
    "project-management-c2-l12": {
        "data_table": table(["Step", "Purpose"], [
            ["Change control board review", "Evaluates and approves or rejects proposed project changes"],
        ]),
    },
    "project-management-c2-l13": {
        "data_table": table(["Step", "Purpose"], [
            ["Scope verification", "Formally confirms deliverables meet requirements before acceptance"],
        ]),
    },
    "project-management-c2-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Milestone", "A significant point or event marking progress in a project"],
        ]),
    },
    "project-management-c2-l15": {
        "data_table": table(["Type", "Meaning"], [
            ["Finish-to-start dependency", "A task cannot start until its predecessor finishes"],
        ]),
    },
    "project-management-c2-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Schedule buffer", "Extra time added to protect against delays in dependent tasks"],
        ]),
    },
    "project-management-c2-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Rolling wave planning", "Plans near-term work in detail while leaving distant work at a high level"],
        ]),
    },
    "project-management-c2-l18": {
        "data_table": table(["Element", "Purpose"], [
            ["Scope statement", "Defines project deliverables, boundaries, and exclusions clearly"],
        ]),
    },
    "project-management-c2-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Network diagram", "Visualizes task sequence and dependencies across a project schedule"],
        ]),
    },
    "project-management-c2-l20": {
        "data_table": table(["Practice", "Reason"], [
            ["Accurate time tracking", "Improves future estimation and project cost accountability"],
        ]),
    },
    "project-management-c2-l21": {
        "data_table": table(["Metric", "Formula"], [
            ["Cost Performance Index", "Earned Value / Actual Cost"], ["Schedule Performance Index", "Earned Value / Planned Value"],
        ]),
        "formulae": ["CPI = EV / AC", "SPI = EV / PV"],
    },
    "project-management-c2-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Monte Carlo simulation", "Runs many random scenarios to estimate the probability of hitting a schedule deadline"],
        ]),
    },
    "project-management-c2-l23": {
        "data_table": table(["Technique", "Purpose"], [
            ["Sensitivity analysis", "Identifies which risk factors most affect project outcomes"],
        ]),
    },
    "project-management-c2-l24": {
        "data_table": table(["Field", "Purpose"], [
            ["Risk register", "Tracks identified risks, their likelihood, impact, and mitigation plans"],
        ]),
    },
    "project-management-c2-l25": {
        "data_table": table(["Contract Type", "Risk Allocation"], [
            ["Fixed-price", "Puts cost risk primarily on the vendor"], ["Cost-reimbursable", "Puts cost risk primarily on the buyer"],
        ]),
    },
    "project-management-c2-l26": {
        "data_table": table(["Metric", "Purpose"], [
            ["Vendor scorecard", "Tracks supplier performance against agreed criteria over time"],
        ]),
    },
    "project-management-c2-l27": {
        "data_table": table(["Strategy", "Purpose"], [
            ["BATNA", "Establishes a fallback position that strengthens negotiating leverage"],
        ]),
    },
    "project-management-c2-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Release plan", "Outlines which features ship in which upcoming release cycle"],
        ]),
    },
    "project-management-c2-l29": {
        "data_table": table(["Framework", "Feature"], [
            ["SAFe", "Coordinates agile practices across multiple teams at enterprise scale"],
        ]),
    },
    "project-management-c2-l30": {
        "data_table": table(["Step", "Purpose"], [
            ["Sprint retrospective", "Reflects on the past sprint to identify process improvements"],
        ]),
    },
    "project-management-c2-l31": {
        "data_table": table(["Metric", "Meaning"], [
            ["Velocity", "The amount of work a team completes per sprint, used for forecasting"],
        ]),
    },
    "project-management-c2-l32": {
        "data_table": table(["Approach", "Feature"], [
            ["Hybrid project management", "Combines predictive and agile methods within one project"],
        ]),
    },
    "project-management-c2-l33": {
        "data_table": table(["Tool", "Purpose"], [
            ["Stakeholder engagement matrix", "Maps stakeholders by influence and interest to guide communication"],
        ]),
    },
    "project-management-c2-l34": {
        "data_table": table(["Challenge", "Mitigation"], [
            ["Time zone differences", "Establishing overlapping working hours or asynchronous workflows"],
        ]),
    },
    "project-management-c2-l35": {
        "data_table": table(["Factor", "Consideration"], [
            ["Communication style", "Directness expectations vary significantly across cultures"],
        ]),
    },
    "project-management-c2-l36": {
        "data_table": table(["Style", "Feature"], [
            ["Collaborating", "Seeks a win-win solution through open discussion"], ["Compromising", "Both sides give up something to reach agreement"],
        ]),
    },
    "project-management-c2-l37": {
        "data_table": table(["Principle", "Meaning"], [
            ["Servant leadership", "The leader's primary role is removing obstacles and supporting the team"],
        ]),
    },
    "project-management-c2-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Portfolio management", "Aligns a collection of projects and programs with organizational strategy"],
        ]),
    },
    "project-management-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Benefits realization", "Ensures a program's outcomes deliver the value it was intended to produce"],
        ]),
    },
    "project-management-c2-l40": {
        "data_table": table(["Method", "Formula"], [
            ["Estimate at Completion", "Actual Cost + (Budget at Completion - Earned Value) / CPI"],
        ]),
        "formulae": ["EAC = AC + (BAC - EV) / CPI"],
    },
    "project-management-c2-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Value engineering", "Systematically improves value by optimizing function relative to cost"],
        ]),
    },
    "project-management-c2-l42": {
        "data_table": table(["Tool", "Purpose"], [
            ["Control chart", "Monitors whether a process stays within acceptable quality limits"],
        ]),
    },
    "project-management-c2-l43": {
        "data_table": table(["Phase", "Focus"], [
            ["DMAIC", "Define, Measure, Analyze, Improve, Control — a Six Sigma improvement cycle"],
        ]),
    },
    "project-management-c2-l44": {
        "data_table": table(["Principle", "Meaning"], [
            ["Eliminating waste", "A core Lean principle removing any non-value-adding activity"],
        ]),
    },
    "project-management-c2-l45": {
        "data_table": table(["Model", "Feature"], [
            ["Supportive PMO", "Provides templates and best practices with low control"], ["Directive PMO", "Directly manages projects with high control"],
        ]),
    },
    "project-management-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Maturity model", "Assesses an organization's project management capability across defined levels"],
        ]),
    },
    "project-management-c2-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Change control board", "A formal group that reviews and approves proposed project changes"],
        ]),
    },
    "project-management-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Configuration management", "Tracks and controls changes to a project's deliverables and documentation"],
        ]),
    },
    "project-management-c2-l49": {
        "data_table": table(["Constraint", "Tradeoff"], [
            ["Iron triangle", "Scope, time, and cost are interdependent constraints"],
        ]),
    },
    "project-management-c2-l50": {
        "data_table": table(["Technique", "Purpose"], [
            ["Resource optimization", "Maximizes team output within fixed resource constraints"],
        ]),
    },
    "project-management-c2-l51": {
        "data_table": table(["Step", "Purpose"], [
            ["Rapid impact assessment", "Determines the scope of damage during a project crisis"],
        ]),
    },
    "project-management-c2-l52": {
        "data_table": table(["Step", "Purpose"], [
            ["Post-implementation review", "Assesses whether a completed project achieved its intended benefits"],
        ]),
    },
    "project-management-c2-l53": {
        "data_table": table(["Task", "Purpose"], [
            ["Contract administration", "Ensures both parties meet their contractual obligations throughout delivery"],
        ]),
    },
    "project-management-c2-l54": {
        "data_table": table(["Principle", "Meaning"], [
            ["Professional responsibility", "Maintaining honesty, fairness, and accountability throughout a project"],
        ]),
    },
    "project-management-c2-l55": {
        "data_table": table(["Element", "Purpose"], [
            ["Communication plan", "Defines who needs what information, how often, and through which channel"],
        ]),
    },
    "project-management-c2-l56": {
        "data_table": table(["Practice", "Purpose"], [
            ["Backlog grooming", "Continuously refines and reprioritizes scope in an agile environment"],
        ]),
    },
    "project-management-c2-l57": {
        "data_table": table(["Skill", "Purpose"], [
            ["Active facilitation", "Keeps diverse stakeholder discussions productive and on track"],
        ]),
    },
    "project-management-c2-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Project governance", "The framework of policies and decision rights guiding project oversight"],
        ]),
    },
    "project-management-c2-l59": {
        "data_table": table(["Decision", "Consideration"], [
            ["Make-or-buy analysis", "Weighs producing in-house against outsourcing"],
        ]),
    },
    "project-management-c2-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Portfolio prioritization", "Ranks projects by strategic value and resource availability"],
        ]),
    },
    "project-management-c2-l61": {
        "data_table": table(["Contract Type", "Detail"], [
            ["Time and materials", "Blends cost-reimbursable and fixed elements, moderate risk sharing"],
        ]),
    },
    "project-management-c2-l62": {
        "data_table": table(["Element", "Detail"], [
            ["Hybrid governance", "Applies predictive controls to fixed-scope work and agile controls to flexible work"],
        ]),
    },
    "project-management-c2-l63": {
        "data_table": table(["Behavior", "Detail"], [
            ["Removing blockers", "A core servant leadership responsibility for the team's daily progress"],
        ]),
    },
    "project-management-c2-l64": {
        "data_table": table(["Item", "Detail"], [
            ["Configuration item", "Any deliverable or artifact placed under formal version control"],
        ]),
    },
    "project-management-c2-l65": {
        "data_table": table(["Notation", "Detail"], [
            ["Activity-on-node", "Represents each task as a node connected by dependency arrows"],
        ]),
    },
    "project-management-c2-l66": {
        "data_table": table(["Constraint", "Detail"], [
            ["Resource over-allocation", "Occurs when one resource is assigned to more work than time allows"],
        ]),
    },
    "project-management-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Writing a scope statement", "Defining clear inclusions and exclusions for a real project"],
        ]),
    },
    "project-management-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Building a project schedule", "Sequencing tasks and estimating durations for a timeline"],
        ]),
    },
    "project-management-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Running stakeholder interviews", "Extracting clear, testable requirements from stakeholder input"],
        ]),
    },
    "project-management-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Detecting early scope creep", "Flagging an unapproved feature request before it derails the timeline"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Project Management"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Project Management: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Project Management lessons (completing 70/70).")


if __name__ == "__main__":
    main()
