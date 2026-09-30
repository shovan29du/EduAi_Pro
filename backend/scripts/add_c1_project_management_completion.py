#!/usr/bin/env python3
"""Depth pass, C1 Project Management: fill in real, hand-checked
data_table content for the 69 C1 Project Management lessons not
covered by the earlier breadth-first batch. Brings C1 Project
Management to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_project_management_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "project-management-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Project", "A temporary endeavor with a defined start and end to create a unique result"],
        ]),
    },
    "project-management-c1-l2": {
        "data_table": table(["Phase", "Focus"], [
            ["Initiation", "Defining the project and its objectives"], ["Planning", "Detailing how the project will be executed"],
        ]),
    },
    "project-management-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Success criteria", "Measurable conditions that define whether a project succeeded"],
        ]),
    },
    "project-management-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Stakeholder", "Any person or group affected by or invested in the project"],
        ]),
    },
    "project-management-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["WBS", "Work Breakdown Structure, breaks a project into smaller manageable tasks"],
        ]),
    },
    "project-management-c1-l7": {
        "data_table": table(["Chart Element", "Meaning"], [
            ["Bar", "Represents a task's duration on a timeline"],
        ]),
    },
    "project-management-c1-l8": {
        "data_table": table(["Letter", "Meaning"], [
            ["R", "Responsible - does the work"], ["A", "Accountable - approves the work"], ["C", "Consulted"], ["I", "Informed"],
        ]),
    },
    "project-management-c1-l9": {
        "data_table": table(["Constraint", "Example"], [
            ["Scope", "What the project will deliver"], ["Time", "The deadline"], ["Cost", "The budget"],
        ]),
    },
    "project-management-c1-l10": {
        "data_table": table(["Tool", "Purpose"], [
            ["Jira", "Tracks tasks and sprints"], ["Trello", "Visual kanban board for task tracking"],
        ]),
    },
    "project-management-c1-l11": {
        "data_table": table(["Element", "Purpose"], [
            ["Kickoff meeting", "Aligns the team on goals, roles, and timeline at project start"],
        ]),
    },
    "project-management-c1-l12": {
        "data_table": table(["Method", "Description"], [
            ["Three-point estimation", "Averages optimistic, pessimistic, and most likely estimates"],
        ]),
    },
    "project-management-c1-l13": {
        "data_table": table(["Document", "Purpose"], [
            ["Project charter", "Formally authorizes the project"], ["Status report", "Tracks ongoing progress"],
        ]),
    },
    "project-management-c1-l14": {
        "data_table": table(["Role", "Responsibility"], [
            ["Project sponsor", "Provides resources and high-level support"],
        ]),
    },
    "project-management-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Milestone", "A significant point or event in the project timeline"],
        ]),
    },
    "project-management-c1-l16": {
        "data_table": table(["Step", "Purpose"], [
            ["Risk identification", "Finding potential problems before they occur"],
        ]),
    },
    "project-management-c1-l17": {
        "data_table": table(["Element", "Purpose"], [
            ["Communication plan", "Defines who needs what information, when, and how"],
        ]),
    },
    "project-management-c1-l18": {
        "data_table": table(["Activity", "Purpose"], [
            ["Final sign-off", "Formally confirms deliverables are accepted"],
        ]),
    },
    "project-management-c1-l19": {
        "data_table": table(["Stage", "Description"], [
            ["Forming", "Team members get acquainted"], ["Storming", "Conflict as roles are worked out"], ["Norming", "Team establishes norms"], ["Performing", "Team works effectively"],
        ]),
    },
    "project-management-c1-l20": {
        "data_table": table(["Principle", "Meaning"], [
            ["Transparency", "Honest reporting of project status, even when unfavorable"],
        ]),
    },
    "project-management-c1-l21": {
        "data_table": table(["Method", "Description"], [
            ["Bottom-up estimating", "Estimates each task individually, then sums them"],
        ]),
    },
    "project-management-c1-l22": {
        "data_table": table(["Component", "Example"], [
            ["Labor costs", "Wages for the project team"], ["Contingency reserve", "Buffer for unforeseen costs"],
        ]),
    },
    "project-management-c1-l23": {
        "data_table": table(["Metric", "Meaning"], [
            ["Planned Value (PV)", "Budgeted cost of scheduled work"], ["Earned Value (EV)", "Budgeted cost of work actually performed"],
        ]),
    },
    "project-management-c1-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Quality management", "Ensuring the project meets required standards"],
        ]),
    },
    "project-management-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Quality assurance", "Process-focused, prevents defects"], ["Quality control", "Product-focused, detects defects"],
        ]),
    },
    "project-management-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Procurement", "Acquiring goods or services from outside the project team"],
        ]),
    },
    "project-management-c1-l27": {
        "data_table": table(["Contract Type", "Risk"], [
            ["Fixed-price", "Risk falls on the seller"], ["Cost-reimbursable", "Risk falls on the buyer"],
        ]),
    },
    "project-management-c1-l28": {
        "data_table": table(["Criterion", "Example"], [
            ["Price", "Cost competitiveness"], ["Track record", "Past performance and reliability"],
        ]),
    },
    "project-management-c1-l29": {
        "data_table": table(["Activity", "Purpose"], [
            ["Resource planning", "Ensures the right people are available at the right time"],
        ]),
    },
    "project-management-c1-l30": {
        "data_table": table(["Factor", "Effect"], [
            ["Clear goals", "Increases team motivation and focus"],
        ]),
    },
    "project-management-c1-l31": {
        "data_table": table(["Technique", "Approach"], [
            ["Collaboration", "Finding a win-win solution together"], ["Compromise", "Each side gives up something"],
        ]),
    },
    "project-management-c1-l32": {
        "data_table": table(["Strategy", "Meaning"], [
            ["Avoid", "Eliminates the risk"], ["Mitigate", "Reduces the risk's impact or likelihood"], ["Accept", "Acknowledges and monitors the risk"],
        ]),
    },
    "project-management-c1-l33": {
        "data_table": table(["Technique", "Purpose"], [
            ["Probability and impact matrix", "Ranks risks by likelihood and severity"],
        ]),
    },
    "project-management-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Integration management", "Coordinating all parts of a project into a cohesive whole"],
        ]),
    },
    "project-management-c1-l35": {
        "data_table": table(["Document", "Purpose"], [
            ["Project management plan", "Consolidates all subsidiary plans into one document"],
        ]),
    },
    "project-management-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Agile", "An iterative approach to project management emphasizing flexibility"],
        ]),
    },
    "project-management-c1-l37": {
        "data_table": table(["Role", "Responsibility"], [
            ["Scrum Master", "Facilitates the Scrum process"], ["Product Owner", "Represents stakeholder priorities"],
        ]),
    },
    "project-management-c1-l38": {
        "data_table": table(["Column", "Meaning"], [
            ["To Do", "Tasks not yet started"], ["In Progress", "Tasks currently being worked on"], ["Done", "Completed tasks"],
        ]),
    },
    "project-management-c1-l39": {
        "data_table": table(["Approach", "Feature"], [
            ["Waterfall", "Sequential phases, planned upfront"], ["Agile", "Iterative, adapts as it goes"],
        ]),
    },
    "project-management-c1-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["PMO", "Project Management Office, standardizes project practices across an organization"],
        ]),
    },
    "project-management-c1-l41": {
        "data_table": table(["Method", "Description"], [
            ["Weighted scoring model", "Ranks projects by criteria with assigned weights"],
        ]),
    },
    "project-management-c1-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Cost-benefit analysis", "Compares expected costs against expected benefits"],
        ]),
    },
    "project-management-c1-l43": {
        "data_table": table(["Step", "Purpose"], [
            ["Stakeholder engagement plan", "Defines strategies to effectively involve stakeholders"],
        ]),
    },
    "project-management-c1-l44": {
        "data_table": table(["Quadrant", "Strategy"], [
            ["High power, high interest", "Manage closely"], ["Low power, low interest", "Monitor minimally"],
        ]),
    },
    "project-management-c1-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Change management", "Structured approach to transitioning individuals through organizational change"],
        ]),
    },
    "project-management-c1-l46": {
        "data_table": table(["Style", "Description"], [
            ["Transformational", "Inspires and motivates through vision"], ["Servant leadership", "Prioritizes the team's needs"],
        ]),
    },
    "project-management-c1-l47": {
        "data_table": table(["Document", "Purpose"], [
            ["RFP", "Request for Proposal, solicits vendor bids"],
        ]),
    },
    "project-management-c1-l48": {
        "data_table": table(["Cost Type", "Example"], [
            ["Cost of conformance", "Training and quality planning"], ["Cost of non-conformance", "Rework and defects"],
        ]),
    },
    "project-management-c1-l49": {
        "data_table": table(["Skill", "Purpose"], [
            ["Setting an agenda", "Keeps meetings focused and productive"],
        ]),
    },
    "project-management-c1-l50": {
        "data_table": table(["Element", "Purpose"], [
            ["Status report", "Communicates progress, risks, and issues to stakeholders"],
        ]),
    },
    "project-management-c1-l51": {
        "data_table": table(["Tool", "Purpose"], [
            ["Project dashboard", "Visualizes key metrics for quick status checks"],
        ]),
    },
    "project-management-c1-l52": {
        "data_table": table(["Document", "Purpose"], [
            ["Lessons learned register", "Captures insights to improve future projects"],
        ]),
    },
    "project-management-c1-l53": {
        "data_table": table(["Certification", "Provider"], [
            ["PMP", "Project Management Institute"], ["CAPM", "Project Management Institute, entry-level"],
        ]),
    },
    "project-management-c1-l54": {
        "data_table": table(["Structure", "Feature"], [
            ["Functional", "Organized by department"], ["Matrix", "Blends functional and project reporting lines"],
        ]),
    },
    "project-management-c1-l55": {
        "data_table": table(["Structure", "Project Manager Authority"], [
            ["Functional", "Low"], ["Matrix", "Moderate"], ["Projectized", "High"],
        ]),
    },
    "project-management-c1-l56": {
        "data_table": table(["Level", "Focus"], [
            ["Project", "A single temporary endeavor"], ["Program", "Related projects managed together"], ["Portfolio", "All projects and programs aligned to strategy"],
        ]),
    },
    "project-management-c1-l57": {
        "data_table": table(["Letter", "Meaning"], [
            ["S", "Specific"], ["M", "Measurable"], ["A", "Achievable"], ["R", "Relevant"], ["T", "Time-bound"],
        ]),
    },
    "project-management-c1-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Resource allocation", "Assigning available resources to project tasks"],
        ]),
    },
    "project-management-c1-l59": {
        "data_table": table(["Technique", "Purpose"], [
            ["Time blocking", "Dedicates specific time slots to specific tasks"],
        ]),
    },
    "project-management-c1-l60": {
        "data_table": table(["Framework", "Feature"], [
            ["PMBOK", "PMI's comprehensive project management guide"], ["PRINCE2", "Process-based project management method"],
        ]),
    },
    "project-management-c1-l61": {
        "data_table": table(["Technique", "Purpose"], [
            ["Risk probability and impact assessment", "Prioritizes which risks need the most attention"],
        ]),
    },
    "project-management-c1-l62": {
        "data_table": table(["Section", "Purpose"], [
            ["Objectives", "States what the project will achieve"], ["Constraints", "States key limitations"],
        ]),
    },
    "project-management-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Writing a project charter", "Drafting objectives and success criteria for a sample project"],
        ]),
    },
    "project-management-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Mapping the life cycle", "Placing sample tasks into initiation, planning, execution, closure"],
        ]),
    },
    "project-management-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Defining success criteria", "Writing measurable goals for a sample project"],
        ]),
    },
    "project-management-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Setting SMART objectives", "Rewriting a vague goal to be specific and measurable"],
        ]),
    },
    "project-management-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Mapping stakeholders", "Placing sample stakeholders on a power/interest grid"],
        ]),
    },
    "project-management-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Building a WBS", "Breaking a sample project into tasks and subtasks"],
        ]),
    },
    "project-management-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Reading a Gantt chart", "Identifying task dependencies and the critical path"],
        ]),
    },
    "project-management-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Assigning a RACI matrix", "Mapping roles to tasks for a sample project team"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Project Management"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Project Management: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Project Management lessons (completing 70/70).")


if __name__ == "__main__":
    main()
