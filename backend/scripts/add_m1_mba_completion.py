#!/usr/bin/env python3
"""Depth pass, M1 MBA: fill in real, hand-checked data_table content
for the 119 M1 MBA lessons not covered by the earlier breadth-first
batch. Brings M1 MBA to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
corporate strategy and M&A, executive leadership and negotiation,
strategic finance, and applied strategy across industries and
functions; l101-l120 are "Worked Analysis" companions reusing the
data_table of l1-l20 (direct 1:1 mapping). l3 was already completed
by an earlier breadth-first batch, so its data_table is hard-coded
here for reuse (it falls within l1-l20, so it is also reused for
l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_mba_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Framework", "Focus"], [
    ["Porter's Five Forces", "Analyzes industry structure and competitive intensity"],
    ["SWOT", "Assesses a firm's internal strengths/weaknesses and external opportunities/threats"],
])

CHARTS: dict[str, dict] = {
    "mba-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Human resource management", "Manages recruitment, development, and retention of an organization's workforce"],
    ])},
    "mba-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Corporate strategy / M&A", "Sets the overall direction of a firm, including growth through mergers and acquisitions"],
    ])},
    "mba-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Strategic alliance / joint venture", "Two firms combine resources for mutual benefit while remaining independent"],
    ])},
    "mba-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Synergy analysis", "Estimates additional value created by combining two companies beyond their standalone worth"],
    ])},
    "mba-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Brand portfolio management", "Coordinates a company's multiple brands to maximize overall value"],
    ])},
    "mba-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Organizational change leadership", "Guides an organization through significant structural or cultural transformation"],
    ])},
    "mba-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Advanced negotiation strategy", "Uses structured preparation and tactics to secure favorable deal outcomes"],
    ])},
    "mba-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Corporate sustainability strategy", "Integrates environmental and social goals into core business strategy"],
    ])},
    "mba-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Marketing attribution", "Assigns credit for a conversion across the touchpoints that led to it"],
    ])},
    "mba-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Digital business model innovation", "Redesigns how a company creates and captures value using digital technology"],
    ])},
    "mba-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Corporate finance strategy", "Manages how a company raises and allocates capital to support strategic goals"],
    ])},
    "mba-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Strategic workforce planning", "Aligns future talent needs with a company's long-term strategic direction"],
    ])},
    "mba-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Decision analysis under uncertainty", "Structures executive decisions using probability and expected value"],
    ])},
    "mba-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Global value chain strategy", "Optimizes where and how a firm performs value-adding activities worldwide"],
    ])},
    "mba-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["VUCA", "Volatility, Uncertainty, Complexity, Ambiguity; describes a fast-changing business environment"],
    ])},
    "mba-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Corporate governance", "The system of rules and practices directing and controlling a company"],
    ])},
    "mba-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise risk strategy", "Identifies and manages risk across an entire organization's operations"],
    ])},
    "mba-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Scaling ventures globally", "Expands a business model into new international markets sustainably"],
    ])},
    "mba-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Capstone strategy simulation", "Integrates strategic analysis and decision-making into one full business simulation"],
    ])},
    "mba-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Real options valuation", "Values managerial flexibility to adapt an investment as new information arrives"],
    ])},
    "mba-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral finance (corporate)", "Studies how psychological biases affect managers' financial decisions"],
    ])},
    "mba-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Capital structure theory", "Studies how the mix of debt and equity affects a firm's value"],
    ])},
    "mba-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["PE deal structuring", "Designs the financial and legal terms of a private equity acquisition"],
    ])},
    "mba-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Term sheet negotiation", "Negotiates the key terms of a venture capital investment before final documents"],
    ])},
    "mba-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Cross-border M&A integration", "Manages the added complexity of merging companies across national and cultural boundaries"],
    ])},
    "mba-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Strategic divestiture", "Sells or spins off a business unit that no longer fits the core strategy"],
    ])},
    "mba-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Platform business model", "Creates value primarily by connecting two or more distinct user groups"],
    ])},
    "mba-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Disruptive innovation", "A simpler, cheaper offering that eventually displaces established market leaders"],
    ])},
    "mba-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Alliance governance structure", "Defines how decision-making and control are shared in a strategic alliance"],
    ])},
    "mba-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Corporate diversification", "Expands a firm into new products or markets to spread risk or find growth"],
    ])},
    "mba-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic capabilities", "A firm's ability to reconfigure its resources to adapt to changing environments"],
    ])},
    "mba-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Resource-based view", "Argues sustainable advantage comes from valuable, rare, hard-to-imitate resources"],
    ])},
    "mba-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Game-theoretic strategy", "Models competitive decisions as interactions where rivals anticipate each other's moves"],
    ])},
    "mba-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Revenue management", "Dynamically adjusts prices and inventory allocation to maximize revenue"],
    ])},
    "mba-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Customer lifetime value optimization", "Maximizes the total value a customer generates over their relationship with a firm"],
    ])},
    "mba-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Marketing attribution modeling", "Statistically estimates each marketing touchpoint's contribution to a sale"],
    ])},
    "mba-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Brand equity", "The value a brand name adds to a product beyond its functional attributes"],
    ])},
    "mba-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Talent analytics", "Uses data analysis to inform workforce planning and HR decisions"],
    ])},
    "mba-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Organizational ambidexterity", "Balances exploiting current business with exploring new opportunities"],
    ])},
    "mba-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Digital transformation leadership", "Drives organization-wide adoption of digital technology and ways of working"],
    ])},
    "mba-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["ESG integration", "Incorporates environmental, social, and governance factors into corporate strategy"],
    ])},
    "mba-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Impact investing", "Seeks measurable social or environmental benefit alongside financial return"],
    ])},
    "mba-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Crisis leadership", "Guides an organization decisively through unexpected, high-stakes disruption"],
    ])},
    "mba-m1-l45": {"data_table": table(["Approach", "Feature"], [
        ["Integrative bargaining", "Seeks mutual gains by expanding the pie"],
        ["Distributive bargaining", "Divides a fixed pie competitively"],
    ])},
    "mba-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Cross-cultural negotiation", "Adapts negotiation style to differing cultural norms and expectations"],
    ])},
    "mba-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Decision-making under deep uncertainty", "Plans robustly when probabilities and outcomes are largely unknown"],
    ])},
    "mba-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral operations management", "Studies how cognitive biases affect operational decision-making"],
    ])},
    "mba-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Due diligence", "Systematically investigates a target company before completing an acquisition"],
    ])},
    "mba-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Post-merger cultural integration", "Aligns two companies' cultures to realize the value of a merger"],
    ])},
    "mba-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Family business succession", "Plans the orderly transfer of leadership across generations in a family firm"],
    ])},
    "mba-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Strategic human capital development", "Aligns employee skill-building with a company's long-term strategy"],
    ])},
    "mba-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Executive coaching", "Uses structured guidance to develop senior leaders' capabilities"],
    ])},
    "mba-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Culture change management", "Deliberately shifts an organization's shared values and norms"],
    ])},
    "mba-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Innovation portfolio management", "Balances a firm's mix of incremental and breakthrough innovation projects"],
    ])},
    "mba-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Open innovation", "Sources ideas and technology from outside the firm's own boundaries"],
    ])},
    "mba-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Digital ecosystem strategy", "Positions a firm within a network of interdependent digital partners"],
    ])},
    "mba-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Tech sector alliances", "Partnerships technology firms use to access complementary capabilities quickly"],
    ])},
    "mba-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral economics in consumer strategy", "Applies predictable consumer biases to marketing and pricing decisions"],
    ])},
    "mba-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Sovereign risk assessment", "Evaluates political and economic risk when operating in a foreign country"],
    ])},
    "mba-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Corporate venture capital", "A company invests in external startups to access innovation strategically"],
    ])},
    "mba-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Alliance exit planning", "Structures how partners can wind down or dissolve a joint venture cleanly"],
    ])},
    "mba-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Scenario planning", "Explores multiple plausible futures to stress-test long-term strategy"],
    ])},
    "mba-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Competitive intelligence", "Systematically gathers and analyzes information about rivals' strategies"],
    ])},
    "mba-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Platform/subscription pricing", "Sets pricing strategy suited to network effects and recurring-revenue models"],
    ])},
    "mba-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Franchise strategy", "Governs how a brand expands by licensing operations to independent operators"],
    ])},
    "mba-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Omnichannel retail strategy", "Integrates online and physical channels into one seamless customer experience"],
    ])},
    "mba-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Sustainability reporting", "Discloses a company's environmental and social performance to stakeholders"],
    ])},
    "mba-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Leadership succession planning", "Prepares a pipeline of candidates for future senior leadership roles"],
    ])},
    "mba-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Cross-functional team leadership", "Coordinates diverse specialists toward a shared complex project goal"],
    ])},
    "mba-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Executive storytelling", "Uses narrative structure to communicate strategy persuasively to stakeholders"],
    ])},
    "mba-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Change resistance", "Behavioral factors that cause employees to resist organizational change"],
    ])},
    "mba-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["B2B digital marketing strategy", "Applies digital channels to longer, relationship-driven B2B sales cycles"],
    ])},
    "mba-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Healthcare/life sciences alliances", "Partnerships navigating regulatory complexity in medical innovation"],
    ])},
    "mba-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Regulated industry strategy", "Aligns business strategy with heavy compliance and regulatory constraints"],
    ])},
    "mba-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["IP portfolio management", "Strategically manages a company's patents and other intellectual property assets"],
    ])},
    "mba-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Antitrust strategy", "Positions competitive actions to comply with laws limiting market power abuse"],
    ])},
    "mba-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Board decision biases", "Cognitive biases that can distort governance decisions made by corporate boards"],
    ])},
    "mba-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Workforce analytics for restructuring", "Uses data to inform decisions during organizational downsizing or redesign"],
    ])},
    "mba-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Economic profit / EVA", "Measures value creation as profit above the true cost of capital employed"],
    ])},
    "mba-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Emerging market entry alliances", "Partners with local firms to navigate unfamiliar regulatory and cultural terrain"],
    ])},
    "mba-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Circular economy business model", "Designs operations around reuse and regeneration instead of disposal"],
    ])},
    "mba-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Non-market strategy", "Manages a firm's relationship with government, media, and public opinion"],
    ])},
    "mba-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Talent acquisition strategy", "Competes effectively for scarce skilled workers in tight labor markets"],
    ])},
    "mba-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Executive decision biases", "Systematic errors that affect senior leaders' strategic judgment"],
    ])},
    "mba-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["War gaming (strategy)", "Simulates competitor responses to test a strategic plan's robustness"],
    ])},
    "mba-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Zero-based budgeting", "Rebuilds a budget from zero each cycle rather than adjusting the prior one"],
    ])},
    "mba-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Blue Ocean Strategy", "Creates uncontested market space rather than competing in existing crowded markets"],
    ])},
    "mba-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Balanced scorecard (multi-BU)", "Aligns performance metrics across financial, customer, process, and learning views"],
    ])},
    "mba-m1-l90": {"data_table": table(["Decision", "Trade-off"], [
        ["Outsourcing", "Lower cost, less control"],
        ["Vertical integration", "More control, higher investment"],
    ])},
    "mba-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Say-on-pay governance", "Lets shareholders vote on executive compensation to strengthen accountability"],
    ])},
    "mba-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Corporate turnaround", "Restores a distressed company to financial health through decisive intervention"],
    ])},
    "mba-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Three Horizons framework", "Balances managing today's business with building tomorrow's opportunities"],
    ])},
    "mba-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Business Model Canvas", "A one-page visual framework for designing and testing a new venture's model"],
    ])},
    "mba-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Activity-based costing", "Assigns overhead costs based on the actual activities that drive them"],
    ])},
    "mba-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Earnout structuring", "Ties part of an acquisition's price to the target's future performance"],
    ])},
    "mba-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["JV bargaining power", "Determines how equity stakes and control are negotiated in a joint venture"],
    ])},
    "mba-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Director independence", "Assesses whether board members can objectively oversee management"],
    ])},
    "mba-m1-l99": {"data_table": table(["Approach", "Feature"], [
        ["Horizontal M&A", "Combines direct competitors, often for scale"],
        ["Vertical M&A", "Combines firms at different supply chain stages"],
    ])},
    "mba-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Employer branding", "Positions a company as an attractive place to work to retain top executive talent"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"mba-m1-l{base_n}"
    worked_key = f"mba-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["MBA"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json MBA: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 MBA lessons (completing 120/120).")


if __name__ == "__main__":
    main()
