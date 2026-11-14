#!/usr/bin/env python3
"""Depth pass, M1 Operations Management: fill in real, hand-checked
data_table content for the 119 M1 Operations Management lessons not
covered by the earlier breadth-first batch. Brings M1 Operations
Management to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
enterprise operations strategy, quantitative operations research
(queueing, scheduling, inventory), supply chain design and
resilience, and applied operations across industries; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls
within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_operations_management_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Model", "Purpose"], [
    ["Network optimization", "Finds the lowest-cost configuration of facilities and flows across a supply network"],
    ["Linear programming", "A common mathematical technique used to solve these optimization models"],
])

CHARTS: dict[str, dict] = {
    "operations-management-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Operations analytics", "Applies data analysis to improve operational decision-making"],
    ])},
    "operations-management-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Global operations management", "Coordinates production and logistics across multiple countries"],
    ])},
    "operations-management-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Multi-site capacity planning", "Allocates production capacity optimally across several facility locations"],
    ])},
    "operations-management-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Stochastic inventory theory", "Models optimal inventory policy under random, uncertain demand"],
    ])},
    "operations-management-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Design for Six Sigma", "Builds quality into a product or process from the initial design stage"],
    ])},
    "operations-management-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise lean transformation", "Leads organization-wide adoption of lean principles to eliminate waste"],
    ])},
    "operations-management-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Global operations risk governance", "Oversees risk management across an internationally distributed operations network"],
    ])},
    "operations-management-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Revenue management", "Dynamically adjusts prices and capacity allocation to maximize revenue"],
    ])},
    "operations-management-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Digital transformation of operations", "Applies digital technology to modernize operational processes"],
    ])},
    "operations-management-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Complex service systems design", "Structures multi-step service processes to deliver consistent quality"],
    ])},
    "operations-management-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Predictive asset management", "Forecasts equipment maintenance needs from sensor and usage data"],
    ])},
    "operations-management-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Sustainable operations strategy", "Integrates environmental impact reduction into core operational decisions"],
    ])},
    "operations-management-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Supplier ecosystem management", "Strategically manages relationships across an entire supplier network"],
    ])},
    "operations-management-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Operations research", "Applies mathematical modeling to optimize complex operational decisions"],
    ])},
    "operations-management-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Theory of constraints (enterprise)", "Focuses improvement on the single bottleneck limiting a whole system's output"],
    ])},
    "operations-management-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["ML in operations", "Applies machine learning to forecasting, quality control, and process optimization"],
    ])},
    "operations-management-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Global trade and regulatory strategy", "Navigates tariffs, customs, and cross-border compliance in operations"],
    ])},
    "operations-management-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Operations strategy in transformation", "Aligns operational capability changes with broader corporate transformation"],
    ])},
    "operations-management-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Capstone improvement project", "Applies operations methods to a real end-to-end process improvement"],
    ])},
    "operations-management-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Queueing theory", "Models wait times and server utilization in systems where customers arrive randomly"],
    ])},
    "operations-management-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Newsvendor model", "Determines optimal order quantity for a product with uncertain, one-time demand"],
    ])},
    "operations-management-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Vendor-managed inventory", "The supplier manages and replenishes a customer's inventory levels directly"],
    ])},
    "operations-management-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Bullwhip effect", "Small demand fluctuations amplify into large swings further up the supply chain"],
    ])},
    "operations-management-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain contract design", "Structures pricing and risk-sharing terms between supply chain partners"],
    ])},
    "operations-management-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Facility location modeling", "Determines optimal placement of plants and warehouses to minimize cost"],
    ])},
    "operations-management-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Network flow optimization", "Finds the most efficient way to move goods through a logistics network"],
    ])},
    "operations-management-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Vehicle routing problem", "Finds the most efficient set of delivery routes for a fleet of vehicles"],
    ])},
    "operations-management-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Cross-docking", "Transfers goods directly from inbound to outbound transport with minimal storage"],
    ])},
    "operations-management-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Warehouse slotting", "Optimizes item placement within a warehouse to minimize picking time"],
    ])},
    "operations-management-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Advanced demand forecasting", "Uses statistical and ML methods to predict future product demand accurately"],
    ])},
    "operations-management-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["S&OP integration", "Aligns sales forecasts with production and inventory planning across the business"],
    ])},
    "operations-management-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Capacity planning under uncertainty", "Sizes production capacity to hedge against unpredictable future demand"],
    ])},
    "operations-management-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Job shop scheduling", "Sequences varied jobs through different machines to minimize completion time"],
    ])},
    "operations-management-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Flexible manufacturing system", "A production system that adapts quickly to different products or volumes"],
    ])},
    "operations-management-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Toyota Production System", "A foundational lean system emphasizing waste elimination and continuous flow"],
    ])},
    "operations-management-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Statistical process control", "Uses control charts to monitor and maintain manufacturing process quality"],
    ])},
    "operations-management-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Reliability engineering", "Designs and maintains equipment to minimize failure and downtime"],
    ])},
    "operations-management-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Total Productive Maintenance", "Engages all employees in proactive equipment maintenance to maximize uptime"],
    ])},
    "operations-management-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Quality Function Deployment", "Translates customer requirements into specific engineering design characteristics"],
    ])},
    "operations-management-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Six Sigma DMAIC", "Define, Measure, Analyze, Improve, Control; a structured quality improvement process"],
    ])},
    "operations-management-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Process capability", "Measures how well a process's output fits within specification limits"],
    ])},
    "operations-management-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Service experience design", "Structures service operations specifically around delivering a quality customer experience"],
    ])},
    "operations-management-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Yield management", "Maximizes revenue in capacity-constrained industries like airlines and hotels"],
    ])},
    "operations-management-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Simulation modeling", "Models a complex operational system computationally to test scenarios safely"],
    ])},
    "operations-management-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Digital twin (manufacturing)", "A virtual model of a production system used to simulate and monitor performance"],
    ])},
    "operations-management-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Additive manufacturing strategy", "Uses 3D printing to enable new operational and supply chain models"],
    ])},
    "operations-management-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Robotics and automation", "Uses machines to perform physical production tasks with reduced human labor"],
    ])},
    "operations-management-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Human-robot collaboration", "Designs production systems where people and robots work safely side by side"],
    ])},
    "operations-management-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Circular supply chain", "Designs supply chains around reuse, refurbishment, and recycling"],
    ])},
    "operations-management-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Reverse logistics", "Manages the flow of returned products back through the supply chain"],
    ])},
    "operations-management-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Closed-loop supply chain", "Coordinates forward and reverse flows so returned products re-enter production"],
    ])},
    "operations-management-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Sustainable operations metrics", "Tracks and reports environmental performance indicators for operations"],
    ])},
    "operations-management-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Carbon footprint optimization (logistics)", "Reduces emissions from transportation and distribution networks"],
    ])},
    "operations-management-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Global sourcing risk assessment", "Evaluates supplier risk across geographically dispersed sourcing networks"],
    ])},
    "operations-management-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain resilience", "Builds a supply chain's ability to withstand and recover from disruptions"],
    ])},
    "operations-management-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Theory of constraints applications", "Applies bottleneck-focused improvement across varied operational contexts"],
    ])},
    "operations-management-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Constraint-based scheduling", "Sequences production around the system's binding bottleneck resource"],
    ])},
    "operations-management-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Mass customization", "Delivers individually tailored products at near mass-production efficiency"],
    ])},
    "operations-management-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Modular product architecture", "Designs products from interchangeable components to simplify operations"],
    ])},
    "operations-management-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Critical Chain Method", "Schedules projects accounting for resource constraints and buffers, not just task order"],
    ])},
    "operations-management-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["RCPSP optimization", "Schedules project tasks optimally under limited resource availability"],
    ])},
    "operations-management-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Integer programming", "Optimization where some decision variables must take whole-number values"],
    ])},
    "operations-management-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Stochastic programming", "Optimizes decisions that must be made before uncertain parameters are known"],
    ])},
    "operations-management-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Robust optimization", "Finds solutions that perform well across a range of possible uncertain scenarios"],
    ])},
    "operations-management-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Data-driven operations decisions", "Bases operational choices on quantitative analysis rather than intuition"],
    ])},
    "operations-management-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Predictive maintenance (sensors)", "Uses real-time sensor data to forecast equipment failure before it happens"],
    ])},
    "operations-management-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Healthcare operations analytics", "Applies operations methods to improve hospital efficiency and patient outcomes"],
    ])},
    "operations-management-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Patient flow modeling", "Models how patients move through hospital resources to reduce bottlenecks"],
    ])},
    "operations-management-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Airline operations management", "Optimizes fleet, crew, and gate scheduling under complex regulatory constraints"],
    ])},
    "operations-management-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Assortment and space planning", "Optimizes which products and how much shelf space to allocate in retail"],
    ])},
    "operations-management-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Omnichannel fulfillment", "Coordinates inventory and delivery across online and physical retail channels"],
    ])},
    "operations-management-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Last-mile delivery optimization", "Minimizes cost and time for the final delivery leg to the customer"],
    ])},
    "operations-management-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Perishable goods operations", "Manages inventory and logistics for products with a limited shelf life"],
    ])},
    "operations-management-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Cold chain logistics", "Maintains required temperature control throughout a perishable product's journey"],
    ])},
    "operations-management-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Pharmaceutical supply chain compliance", "Meets strict regulatory requirements for drug handling and traceability"],
    ])},
    "operations-management-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Humanitarian logistics", "Delivers aid efficiently under urgent, uncertain, and resource-constrained conditions"],
    ])},
    "operations-management-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral operations", "Studies how cognitive biases affect real-world operational decision-making"],
    ])},
    "operations-management-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Game-theoretic supply chain models", "Models strategic interactions between supply chain partners with competing interests"],
    ])},
    "operations-management-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Capacity allocation in service networks", "Distributes limited service capacity across locations or customer segments"],
    ])},
    "operations-management-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Subscription service operations", "Manages capacity and fulfillment for recurring-delivery business models"],
    ])},
    "operations-management-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Bottleneck analysis", "Identifies the process step limiting overall system throughput"],
    ])},
    "operations-management-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Lean Six Sigma in services", "Combines waste elimination and variation reduction methods in service industries"],
    ])},
    "operations-management-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Operations risk management framework", "Systematically identifies and mitigates risks to operational continuity"],
    ])},
    "operations-management-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Business continuity planning", "Prepares operations to keep functioning through major disruptions"],
    ])},
    "operations-management-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Make-or-buy analysis", "Decides whether to produce a component internally or purchase it externally"],
    ])},
    "operations-management-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Supplier development", "Actively works with suppliers to improve their performance and capability"],
    ])},
    "operations-management-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Total cost of ownership", "Accounts for all costs of a purchase, not just its purchase price"],
    ])},
    "operations-management-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Distribution network design", "Structures warehouses and transport routes to serve customers efficiently"],
    ])},
    "operations-management-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["E-commerce fulfillment operations", "Manages the picking, packing, and shipping unique to online order volumes"],
    ])},
    "operations-management-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Micro-fulfillment center", "A small, localized warehouse designed for rapid urban order fulfillment"],
    ])},
    "operations-management-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Heijunka", "Levels production volume and mix to smooth workflow and reduce waste"],
    ])},
    "operations-management-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Renewable energy operations", "Manages the unique scheduling and grid-integration challenges of renewable production"],
    ])},
    "operations-management-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Blockchain in supply chain traceability", "Uses distributed ledgers to verify a product's chain of custody"],
    ])},
    "operations-management-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Inventory pooling", "Consolidates inventory across locations to reduce total safety stock needed"],
    ])},
    "operations-management-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Build-to-order systems", "Begins production only after receiving a confirmed customer order"],
    ])},
    "operations-management-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Postponement strategy", "Delays final product customization until closer to actual demand is known"],
    ])},
    "operations-management-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Capacity investment timing", "Decides when to add production capacity given uncertain future demand"],
    ])},
    "operations-management-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Operations ethics", "Considers fair labor practices and working conditions across a firm's operations"],
    ])},
    "operations-management-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Data center capacity/cooling optimization", "Balances compute capacity growth against energy and cooling constraints"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"operations-management-m1-l{base_n}"
    worked_key = f"operations-management-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Operations Management"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Operations Management: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Operations Management lessons (completing 120/120).")


if __name__ == "__main__":
    main()
