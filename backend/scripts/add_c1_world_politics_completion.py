#!/usr/bin/env python3
"""Depth pass, C1 World Politics: fill in real, hand-checked data_table
content for the 99 C1 World Politics lessons not covered by the earlier
breadth-first batch. Brings C1 World Politics to full 100/100 coverage.

Note: this subject has 100 lessons structured as 20 topics x 5 modes:
l1-20 Conceptual Foundations, l21-40 Worked Analysis, l41-60 Evidence
and Data, l61-80 Comparative Case Study, l81-100 Applied Research
Seminar (topic N maps to lessons N, N+20, N+40, N+60, N+80).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_world_politics_completion.py
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
        "name": "States and Sovereignty",
        "foundations": table(["Term", "Meaning"], [["Sovereignty", "A state's supreme authority over its own territory and affairs"]]),
        "worked": table(["Step", "Example"], [["Assessing statehood", "Checking a territory against defined population, government, and recognition"]]),
        "evidence": table(["Metric", "Insight"], [["UN membership count", "Reflects widely recognized sovereign statehood"]]),
        "case_study": table(["Case", "Insight"], [["Taiwan", "Functions as a state but lacks universal diplomatic recognition"]]),
        "seminar": table(["Step", "Focus"], [["Researching a contested sovereignty case", "Weighing arguments for and against recognition"]]),
    },
    {  # 2
        "name": "Power and Legitimacy",
        "foundations": table(["Term", "Meaning"], [["Legitimacy", "The recognized right of a government to rule"]]),
        "worked": table(["Type", "Example"], [["Legal-rational authority", "Power derived from established laws and procedures"]]),
        "evidence": table(["Metric", "Insight"], [["Public trust in government surveys", "Reflects perceived legitimacy over time"]]),
        "case_study": table(["Case", "Insight"], [["Post-revolution government", "Struggles to establish legitimacy after seizing power by force"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a legitimacy crisis", "Identifying what eroded public trust in a real government"]]),
    },
    {  # 3
        "name": "Political Ideologies",
        "foundations": table(["Ideology", "Core Value"], [["Liberalism", "Individual rights and limited government"], ["Socialism", "Collective ownership and equality"]]),
        "worked": table(["Step", "Example"], [["Placing on a spectrum", "Positioning a party's platform along left-right ideology"]]),
        "evidence": table(["Metric", "Insight"], [["Party platform surveys", "Track how ideological positions shift over time"]]),
        "case_study": table(["Country", "Ideology"], [["Nordic countries", "Blend market economies with strong social welfare"]]),
        "seminar": table(["Step", "Focus"], [["Comparing two party manifestos", "Mapping their positions across major policy issues"]]),
    },
    {  # 4
        "name": "Comparative Institutions",
        "foundations": table(["Institution", "Feature"], [["Federal system", "Power shared between national and regional governments"], ["Unitary system", "Power concentrated in a central government"]]),
        "worked": table(["Step", "Example"], [["Comparing institutions", "Contrasting how two countries structure their legislatures"]]),
        "evidence": table(["Metric", "Insight"], [["Institutional strength index", "Measures the durability of a country's governing institutions"]]),
        "case_study": table(["Country Pair", "Insight"], [["Germany vs. France", "Federal versus unitary institutional design"]]),
        "seminar": table(["Step", "Focus"], [["Comparing two constitutions", "Identifying key institutional design differences"]]),
    },
    {  # 5
        "name": "Democratisation",
        "foundations": table(["Term", "Meaning"], [["Democratisation", "The transition of a political system toward democratic governance"]]),
        "worked": table(["Wave", "Example"], [["Third wave of democratization", "Many countries transitioned to democracy in the late 20th century"]]),
        "evidence": table(["Metric", "Insight"], [["Democracy index scores", "Track the progress or reversal of democratization globally"]]),
        "case_study": table(["Country", "Insight"], [["South Korea", "Transitioned from military rule to stable democracy"]]),
        "seminar": table(["Step", "Focus"], [["Tracing a democratic transition", "Identifying key events that enabled a real country's shift"]]),
    },
    {  # 6
        "name": "Authoritarian Politics",
        "foundations": table(["Type", "Feature"], [["Personalist regime", "Power concentrated around a single leader"], ["Single-party state", "Power monopolized by one party"]]),
        "worked": table(["Tool", "Example"], [["Censorship", "Restricts information to maintain political control"]]),
        "evidence": table(["Metric", "Insight"], [["Freedom House ratings", "Track civil liberties and political rights globally"]]),
        "case_study": table(["Case", "Insight"], [["One-party state example", "Maintains control through limited political competition"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing an authoritarian regime", "Identifying its primary tools of political control"]]),
    },
    {  # 7
        "name": "International Relations Theory",
        "foundations": table(["Theory", "Core Idea"], [["Realism", "States act in self-interest within an anarchic system"], ["Liberalism", "Cooperation and institutions can shape state behavior"]]),
        "worked": table(["Step", "Example"], [["Applying a theory", "Explaining an alliance formation through realist logic"]]),
        "evidence": table(["Metric", "Insight"], [["Alliance formation data", "Tests predictions of competing IR theories"]]),
        "case_study": table(["Event", "Insight"], [["Cold War alliance blocs", "Illustrates realist balance-of-power dynamics"]]),
        "seminar": table(["Step", "Focus"], [["Applying IR theory to a current event", "Testing which theoretical lens best explains it"]]),
    },
    {  # 8
        "name": "Diplomacy",
        "foundations": table(["Term", "Meaning"], [["Diplomacy", "The practice of managing relations between states through negotiation"]]),
        "worked": table(["Step", "Example"], [["Negotiating a treaty", "Balancing competing national interests to reach agreement"]]),
        "evidence": table(["Metric", "Insight"], [["Treaty ratification rates", "Reflect the success of diplomatic negotiation processes"]]),
        "case_study": table(["Case", "Insight"], [["Camp David Accords", "Diplomacy brokered a lasting peace agreement"]]),
        "seminar": table(["Step", "Focus"], [["Studying a real negotiation", "Identifying the compromises each side made"]]),
    },
    {  # 9
        "name": "International Law",
        "foundations": table(["Term", "Meaning"], [["International law", "Rules governing relations between sovereign states"]]),
        "worked": table(["Body", "Role"], [["International Court of Justice", "Settles legal disputes between states"]]),
        "evidence": table(["Metric", "Insight"], [["Treaty compliance data", "Shows how consistently states follow international agreements"]]),
        "case_study": table(["Case", "Insight"], [["ICJ border dispute ruling", "Illustrates how international law resolves interstate conflict"]]),
        "seminar": table(["Step", "Focus"], [["Reviewing an ICJ case", "Summarizing its legal reasoning and outcome"]]),
    },
    {  # 10
        "name": "The United Nations",
        "foundations": table(["Body", "Role"], [["UN Security Council", "Maintains international peace and security"], ["UN General Assembly", "Deliberative body of all member states"]]),
        "worked": table(["Step", "Example"], [["Tracing a resolution", "Following a Security Council resolution from proposal to vote"]]),
        "evidence": table(["Metric", "Insight"], [["Security Council veto usage", "Reveals patterns in great power disagreement"]]),
        "case_study": table(["Case", "Insight"], [["UN peacekeeping mission", "Illustrates the UN's role in conflict stabilization"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a UN resolution", "Identifying its goals and measuring its real-world impact"]]),
    },
    {  # 11
        "name": "Security Studies",
        "foundations": table(["Term", "Meaning"], [["National security", "A state's protection of its citizens, territory, and interests"]]),
        "worked": table(["Concept", "Example"], [["Deterrence", "Nuclear arsenals discouraging attack through threat of retaliation"]]),
        "evidence": table(["Metric", "Insight"], [["Military spending data", "Reflects a state's security priorities and posture"]]),
        "case_study": table(["Case", "Insight"], [["Cuban Missile Crisis", "Illustrates high-stakes deterrence and crisis diplomacy"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a security crisis", "Identifying the deterrence dynamics at play"]]),
    },
    {  # 12
        "name": "War and Peace",
        "foundations": table(["Term", "Meaning"], [["Just war theory", "A framework for evaluating the moral justification of war"]]),
        "worked": table(["Step", "Example"], [["Applying just war criteria", "Assessing a conflict against just cause and proportionality"]]),
        "evidence": table(["Metric", "Insight"], [["Conflict casualty data", "Tracks the human cost of ongoing and historical wars"]]),
        "case_study": table(["Case", "Insight"], [["Post-conflict peace agreement", "Illustrates challenges of durable peacebuilding"]]),
        "seminar": table(["Step", "Focus"], [["Studying a peace agreement", "Assessing which provisions helped it hold or fail"]]),
    },
    {  # 13
        "name": "Human Rights",
        "foundations": table(["Document", "Significance"], [["Universal Declaration of Human Rights", "1948, sets out fundamental global rights"]]),
        "worked": table(["Step", "Example"], [["Documenting a violation", "Gathering evidence for a human rights report"]]),
        "evidence": table(["Metric", "Insight"], [["Human rights violation reports", "Track patterns of abuse across regions"]]),
        "case_study": table(["Body", "Role"], [["International Criminal Court", "Prosecutes individuals for serious international crimes"]]),
        "seminar": table(["Step", "Focus"], [["Reviewing a human rights case", "Summarizing evidence and the resulting international response"]]),
    },
    {  # 14
        "name": "Global Political Economy",
        "foundations": table(["Term", "Meaning"], [["Global political economy", "Studies how politics and economics interact across borders"]]),
        "worked": table(["Step", "Example"], [["Analyzing trade policy", "Assessing who benefits and who loses from a tariff"]]),
        "evidence": table(["Metric", "Insight"], [["Global trade volume data", "Reflects the health of international economic integration"]]),
        "case_study": table(["Case", "Insight"], [["WTO trade dispute", "Illustrates how global economic rules are enforced"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a trade dispute", "Assessing the economic and political interests involved"]]),
    },
    {  # 15
        "name": "Development Politics",
        "foundations": table(["Term", "Meaning"], [["Development politics", "Studies how political systems shape economic and social progress"]]),
        "worked": table(["Step", "Example"], [["Evaluating aid effectiveness", "Assessing whether foreign aid achieved its development goals"]]),
        "evidence": table(["Metric", "Insight"], [["Human Development Index", "Tracks health, education, and income across countries"]]),
        "case_study": table(["Country", "Insight"], [["South Korea's development", "Rapid economic growth through targeted state-led policy"]]),
        "seminar": table(["Step", "Focus"], [["Comparing two development strategies", "Assessing their long-term outcomes"]]),
    },
    {  # 16
        "name": "Migration",
        "foundations": table(["Term", "Meaning"], [["Push factor", "A reason people leave their home country"], ["Pull factor", "A reason people are drawn to a destination country"]]),
        "worked": table(["Step", "Example"], [["Analyzing a migration flow", "Identifying push and pull factors driving movement"]]),
        "evidence": table(["Metric", "Insight"], [["Global migration statistics", "Track the scale and direction of international movement"]]),
        "case_study": table(["Case", "Insight"], [["A major refugee crisis", "Illustrates the political and humanitarian challenges of mass displacement"]]),
        "seminar": table(["Step", "Focus"], [["Researching a migration policy", "Assessing its effect on both origin and destination countries"]]),
    },
    {  # 17
        "name": "Regional Organisations",
        "foundations": table(["Organization", "Purpose"], [["European Union", "Economic and political integration among member states"], ["African Union", "Promotes unity and cooperation across Africa"]]),
        "worked": table(["Step", "Example"], [["Assessing integration", "Comparing shared currency versus shared trade policy"]]),
        "evidence": table(["Metric", "Insight"], [["Intra-regional trade share", "Measures how economically integrated a region has become"]]),
        "case_study": table(["Case", "Insight"], [["ASEAN", "Promotes regional cooperation while respecting national sovereignty"]]),
        "seminar": table(["Step", "Focus"], [["Comparing two regional organizations", "Assessing their level of political and economic integration"]]),
    },
    {  # 18
        "name": "Technology and Geopolitics",
        "foundations": table(["Term", "Meaning"], [["Digital sovereignty", "A state's control over its data and technology infrastructure"]]),
        "worked": table(["Step", "Example"], [["Assessing tech competition", "Comparing two nations' investment in semiconductor production"]]),
        "evidence": table(["Metric", "Insight"], [["Global tech investment data", "Reveals shifting centers of technological power"]]),
        "case_study": table(["Case", "Insight"], [["Global semiconductor supply chain", "Illustrates technology's role in modern geopolitical strategy"]]),
        "seminar": table(["Step", "Focus"], [["Researching a tech policy dispute", "Assessing its strategic and economic stakes"]]),
    },
    {  # 19
        "name": "Climate Diplomacy",
        "foundations": table(["Term", "Meaning"], [["Climate diplomacy", "International negotiation aimed at coordinated climate action"]]),
        "worked": table(["Step", "Example"], [["Analyzing a climate accord", "Assessing national commitments against global targets"]]),
        "evidence": table(["Metric", "Insight"], [["National emissions reduction pledges", "Track progress toward global climate goals"]]),
        "case_study": table(["Case", "Insight"], [["Paris Agreement", "A landmark global climate accord with nationally set targets"]]),
        "seminar": table(["Step", "Focus"], [["Reviewing a country's climate pledge", "Assessing its ambition against its historical emissions"]]),
    },
    {  # 20
        "name": "Global Governance",
        "foundations": table(["Term", "Meaning"], [["Global governance", "Coordinated efforts by states and institutions to address shared global problems"]]),
        "worked": table(["Step", "Example"], [["Evaluating a global institution", "Assessing whether it has the authority to enforce its rules"]]),
        "evidence": table(["Metric", "Insight"], [["International institution effectiveness scores", "Measure how well global bodies achieve their mandates"]]),
        "case_study": table(["Case", "Insight"], [["World Health Organization pandemic response", "Illustrates the strengths and limits of global coordination"]]),
        "seminar": table(["Step", "Focus"], [["Evaluating a global institution's response", "Assessing its effectiveness during a real crisis"]]),
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
        lesson_id = f"world-politics-c1-l{lesson_num}"
        CHARTS[lesson_id] = {"data_table": topic[mode]}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Politics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json World Politics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 World Politics lessons (completing 100/100).")


if __name__ == "__main__":
    main()
