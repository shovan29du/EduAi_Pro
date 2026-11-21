#!/usr/bin/env python3
"""Depth pass, C1 Civics: fill in real, hand-checked data_table content
for the 99 C1 Civics lessons not covered by the earlier breadth-first
batch. Brings C1 Civics to full 100/100 coverage.

Note: this subject has 100 lessons structured as 20 topics x 5 modes:
l1-20 Conceptual Foundations, l21-40 Worked Analysis, l41-60 Evidence
and Data, l61-80 Comparative Case Study, l81-100 Applied Research
Seminar (topic N maps to lessons N, N+20, N+40, N+60, N+80).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_civics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


TOPICS: list[dict] = [
    {  # 1
        "name": "Citizenship",
        "foundations": table(["Term", "Meaning"], [["Citizenship", "Legal membership in a state, with associated rights and duties"]]),
        "worked": table(["Right", "Corresponding Duty"], [["Right to vote", "Duty to stay informed about candidates and issues"]]),
        "evidence": table(["Metric", "Insight"], [["Voter turnout rate", "Indicates the level of civic participation in a country"]]),
        "case_study": table(["Country", "Citizenship Path"], [["United States", "Birthright and naturalization citizenship"], ["Japan", "Primarily citizenship by descent"]]),
        "seminar": table(["Step", "Focus"], [["Comparing naturalization requirements", "Researching two countries' paths to citizenship"]]),
    },
    {  # 2
        "name": "Constitutions",
        "foundations": table(["Term", "Meaning"], [["Constitution", "The foundational legal document establishing a government's structure and limits"]]),
        "worked": table(["Type", "Feature"], [["Written constitution", "Codified in a single formal document, e.g. the US"], ["Unwritten constitution", "Based on customs and statutes, e.g. the UK"]]),
        "evidence": table(["Metric", "Insight"], [["Amendment frequency", "Reflects how easily a constitution can be changed"]]),
        "case_study": table(["Country", "Feature"], [["India", "One of the world's longest written constitutions"]]),
        "seminar": table(["Step", "Focus"], [["Comparing amendment processes", "Contrasting how two constitutions can be changed"]]),
    },
    {  # 3
        "name": "Rule of Law",
        "foundations": table(["Term", "Meaning"], [["Rule of law", "The principle that everyone, including government, is subject to the law"]]),
        "worked": table(["Principle", "Example"], [["Due process", "A fair legal procedure before depriving someone of rights"]]),
        "evidence": table(["Metric", "Insight"], [["Rule of Law Index", "Ranks countries by judicial independence and legal accountability"]]),
        "case_study": table(["Scenario", "Insight"], [["Executive overreach case", "Courts checking a government action exceeding its authority"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a real court ruling", "Identifying how it constrained government power"]]),
    },
    {  # 4
        "name": "Separation of Powers",
        "foundations": table(["Branch", "Function"], [["Legislative", "Makes laws"], ["Executive", "Enforces laws"], ["Judicial", "Interprets laws"]]),
        "worked": table(["Mechanism", "Example"], [["Checks and balances", "A veto lets the executive check the legislature"]]),
        "evidence": table(["Metric", "Insight"], [["Judicial review rate", "Shows how often courts strike down laws or executive actions"]]),
        "case_study": table(["Country", "System"], [["United States", "Strong separation with an independent judiciary"], ["United Kingdom", "Fusion of executive and legislative branches"]]),
        "seminar": table(["Step", "Focus"], [["Tracing a check-and-balance case", "Following a real dispute between two branches of government"]]),
    },
    {  # 5
        "name": "Legislatures",
        "foundations": table(["Type", "Feature"], [["Unicameral legislature", "A single legislative chamber"], ["Bicameral legislature", "Two legislative chambers"]]),
        "worked": table(["Step", "Example"], [["Bill process", "A proposal moves through committee, floor vote, and signature"]]),
        "evidence": table(["Metric", "Insight"], [["Bill passage rate", "Shows how much proposed legislation actually becomes law"]]),
        "case_study": table(["Country", "Structure"], [["United States", "Bicameral: House and Senate"], ["New Zealand", "Unicameral parliament"]]),
        "seminar": table(["Step", "Focus"], [["Tracking a real bill", "Following its progress through committee and floor votes"]]),
    },
    {  # 6
        "name": "Executives",
        "foundations": table(["Type", "Feature"], [["Presidential system", "Executive elected separately from the legislature"], ["Parliamentary system", "Executive drawn from the legislature"]]),
        "worked": table(["Power", "Example"], [["Executive order", "A directive from the head of government with the force of law"]]),
        "evidence": table(["Metric", "Insight"], [["Approval rating trends", "Tracks public confidence in executive leadership over time"]]),
        "case_study": table(["Country", "System"], [["France", "Semi-presidential system combining both models"]]),
        "seminar": table(["Step", "Focus"], [["Comparing executive powers", "Contrasting presidential and prime ministerial authority"]]),
    },
    {  # 7
        "name": "Judiciaries",
        "foundations": table(["Term", "Meaning"], [["Judicial independence", "Courts able to rule free from political interference"]]),
        "worked": table(["Step", "Example"], [["Judicial review", "A court determines whether a law is constitutional"]]),
        "evidence": table(["Metric", "Insight"], [["Case backlog", "Indicates strain on a judicial system's capacity"]]),
        "case_study": table(["Country", "Model"], [["United States", "Lifetime-appointed Supreme Court justices"], ["Germany", "Fixed-term constitutional court judges"]]),
        "seminar": table(["Step", "Focus"], [["Reading a landmark court decision", "Identifying its reasoning and lasting impact"]]),
    },
    {  # 8
        "name": "Elections and Voting",
        "foundations": table(["System", "Feature"], [["First-past-the-post", "Winner takes all in a single district"], ["Proportional representation", "Seats allocated by vote share"]]),
        "worked": table(["Step", "Example"], [["Redistricting", "Redrawing electoral boundaries after a census"]]),
        "evidence": table(["Metric", "Insight"], [["Voter turnout by demographic", "Reveals participation gaps across groups"]]),
        "case_study": table(["Country", "System"], [["United Kingdom", "First-past-the-post"], ["Germany", "Mixed-member proportional"]]),
        "seminar": table(["Step", "Focus"], [["Comparing two voting systems", "Assessing how each affects representation"]]),
    },
    {  # 9
        "name": "Political Parties",
        "foundations": table(["Term", "Meaning"], [["Political party", "An organization seeking to gain and exercise governmental power"]]),
        "worked": table(["System", "Feature"], [["Two-party system", "Two dominant parties, e.g. the US"], ["Multi-party system", "Several competitive parties, e.g. many parliamentary democracies"]]),
        "evidence": table(["Metric", "Insight"], [["Party membership trends", "Reflects shifting public engagement with formal party politics"]]),
        "case_study": table(["Country", "System"], [["United States", "Two-party dominance"], ["Netherlands", "Highly fragmented multi-party system"]]),
        "seminar": table(["Step", "Focus"], [["Comparing party platforms", "Analyzing two parties' stated policy positions"]]),
    },
    {  # 10
        "name": "Local Government",
        "foundations": table(["Term", "Meaning"], [["Local government", "Governance closest to citizens, e.g. city or county level"]]),
        "worked": table(["Service", "Example"], [["Municipal service", "Waste collection, local policing, zoning"]]),
        "evidence": table(["Metric", "Insight"], [["Local election turnout", "Typically lower than national election turnout"]]),
        "case_study": table(["Country", "Structure"], [["United States", "Highly decentralized local governance"], ["France", "More centralized national oversight"]]),
        "seminar": table(["Step", "Focus"], [["Attending a local council meeting", "Observing real local policy decisions being made"]]),
    },
    {  # 11
        "name": "Public Administration",
        "foundations": table(["Term", "Meaning"], [["Public administration", "The implementation of government policy through agencies and civil service"]]),
        "worked": table(["Step", "Example"], [["Policy implementation", "A health agency rolling out a new vaccination program"]]),
        "evidence": table(["Metric", "Insight"], [["Government efficiency index", "Measures how effectively agencies deliver services"]]),
        "case_study": table(["Country", "Model"], [["Singapore", "Known for a highly efficient civil service"]]),
        "seminar": table(["Step", "Focus"], [["Evaluating a government service", "Assessing efficiency of a real public agency process"]]),
    },
    {  # 12
        "name": "Civil Liberties",
        "foundations": table(["Term", "Meaning"], [["Civil liberties", "Individual freedoms protected from government interference"]]),
        "worked": table(["Right", "Example"], [["Freedom of speech", "Protects expression, including unpopular opinions"]]),
        "evidence": table(["Metric", "Insight"], [["Press freedom index", "Tracks the degree of media independence across countries"]]),
        "case_study": table(["Scenario", "Insight"], [["Landmark free speech case", "Defines the limits of protected expression"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a civil liberties case", "Weighing individual rights against public interest claims"]]),
    },
    {  # 13
        "name": "Human Rights",
        "foundations": table(["Document", "Significance"], [["Universal Declaration of Human Rights", "1948, sets out fundamental rights for all people"]]),
        "worked": table(["Category", "Example"], [["Civil and political rights", "Freedom of speech and assembly"], ["Economic and social rights", "Right to education and healthcare"]]),
        "evidence": table(["Metric", "Insight"], [["Human rights reports", "Track violations and progress across countries"]]),
        "case_study": table(["Body", "Role"], [["UN Human Rights Council", "Monitors and addresses global human rights issues"]]),
        "seminar": table(["Step", "Focus"], [["Reviewing a human rights report", "Summarizing findings on a specific country or issue"]]),
    },
    {  # 14
        "name": "Media and Public Opinion",
        "foundations": table(["Term", "Meaning"], [["Agenda-setting", "Media's influence over which issues the public considers important"]]),
        "worked": table(["Step", "Example"], [["Framing analysis", "Comparing how two outlets describe the same event differently"]]),
        "evidence": table(["Metric", "Insight"], [["Public opinion polling", "Tracks shifts in attitudes over time"]]),
        "case_study": table(["Scenario", "Insight"], [["Coverage of an election", "Different outlets emphasize different candidate traits"]]),
        "seminar": table(["Step", "Focus"], [["Comparing news coverage", "Analyzing framing differences across two sources on one story"]]),
    },
    {  # 15
        "name": "Civil Society",
        "foundations": table(["Term", "Meaning"], [["Civil society", "Organizations and associations independent of government and business"]]),
        "worked": table(["Type", "Example"], [["Advocacy group", "Lobbies for a specific policy change"], ["Community organization", "Provides local services or support"]]),
        "evidence": table(["Metric", "Insight"], [["NGO density", "Reflects the strength of a country's civil society sector"]]),
        "case_study": table(["Organization", "Impact"], [["Amnesty International", "Advocates globally for human rights protections"]]),
        "seminar": table(["Step", "Focus"], [["Researching a local NGO", "Documenting its mission and community impact"]]),
    },
    {  # 16
        "name": "Public Policy",
        "foundations": table(["Stage", "Focus"], [["Agenda setting", "Identifying which issues deserve government attention"], ["Implementation", "Putting a policy into practice"]]),
        "worked": table(["Step", "Example"], [["Policy evaluation", "Assessing whether a program achieved its intended outcomes"]]),
        "evidence": table(["Metric", "Insight"], [["Program outcome data", "Measures whether a policy achieved its stated goals"]]),
        "case_study": table(["Policy", "Outcome"], [["Public smoking bans", "Associated with measurable declines in respiratory illness"]]),
        "seminar": table(["Step", "Focus"], [["Evaluating a real policy", "Assessing outcome data against original policy goals"]]),
    },
    {  # 17
        "name": "Taxation and Public Budgets",
        "foundations": table(["Term", "Meaning"], [["Progressive tax", "Tax rate increases as income increases"], ["Regressive tax", "Tax takes a larger share of lower incomes"]]),
        "worked": table(["Step", "Example"], [["Reading a budget", "Comparing revenue sources against planned spending"]]),
        "evidence": table(["Metric", "Insight"], [["Budget deficit trend", "Shows whether government spending exceeds revenue over time"]]),
        "case_study": table(["Country", "Approach"], [["Nordic countries", "High taxation funding extensive public services"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a public budget", "Identifying the largest spending categories in a real budget"]]),
    },
    {  # 18
        "name": "Community Organising",
        "foundations": table(["Term", "Meaning"], [["Community organizing", "Building collective power to advocate for shared community goals"]]),
        "worked": table(["Step", "Example"], [["Building a coalition", "Uniting multiple groups around a shared local issue"]]),
        "evidence": table(["Metric", "Insight"], [["Campaign outcome data", "Tracks whether organizing efforts achieved policy change"]]),
        "case_study": table(["Movement", "Outcome"], [["Civil rights movement organizing", "Grassroots coordination led to major legislative change"]]),
        "seminar": table(["Step", "Focus"], [["Studying a real campaign", "Identifying the organizing tactics that drove its outcome"]]),
    },
    {  # 19
        "name": "Digital Citizenship",
        "foundations": table(["Term", "Meaning"], [["Digital citizenship", "Responsible and informed participation in online civic life"]]),
        "worked": table(["Practice", "Reason"], [["Verifying sources online", "Reduces the spread of misinformation"]]),
        "evidence": table(["Metric", "Insight"], [["Misinformation spread rate", "Shows how quickly false claims travel on social platforms"]]),
        "case_study": table(["Scenario", "Insight"], [["Viral misinformation event", "Illustrates the civic cost of unchecked online claims"]]),
        "seminar": table(["Step", "Focus"], [["Fact-checking a viral claim", "Tracing its origin and verifying its accuracy"]]),
    },
    {  # 20
        "name": "Democratic Resilience",
        "foundations": table(["Term", "Meaning"], [["Democratic backsliding", "A gradual erosion of democratic institutions and norms"]]),
        "worked": table(["Indicator", "Example"], [["Warning sign", "Attacks on judicial independence or a free press"]]),
        "evidence": table(["Metric", "Insight"], [["Democracy index scores", "Tracks the health of democratic institutions over time"]]),
        "case_study": table(["Country", "Insight"], [["Historical case study", "Illustrates how institutional checks resisted democratic erosion"]]),
        "seminar": table(["Step", "Focus"], [["Tracking a democracy index", "Analyzing a country's trend over the past decade"]]),
    },
]

MODE_TO_OFFSET = {
    "foundations": 0,
    "worked": 20,
    "evidence": 40,
    "case_study": 60,
    "seminar": 80,
}

CHARTS: dict[str, dict] = {}
for idx, topic in enumerate(TOPICS, start=1):
    for mode, offset in MODE_TO_OFFSET.items():
        lesson_num = idx + offset
        lesson_id = f"civics-c1-l{lesson_num}"
        CHARTS[lesson_id] = {"data_table": topic[mode]}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Civics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Civics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Civics lessons (completing 100/100).")


if __name__ == "__main__":
    main()
