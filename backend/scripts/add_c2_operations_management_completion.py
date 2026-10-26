#!/usr/bin/env python3
"""Depth pass, C2 Operations Management: fill in real, hand-checked
data_table/formulae content for the 69 C2 Operations Management lessons
not covered by the earlier breadth-first batch. Brings C2 Operations
Management to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_operations_management_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "operations-management-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Supply chain", "The network moving a product from raw material to end customer"],
        ]),
    },
    "operations-management-c2-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Inventory management", "Balances holding costs against the risk of stockouts"],
        ]),
    },
    "operations-management-c2-l4": {
        "data_table": table(["Term", "Formula"], [
            ["Little's Law", "Inventory = Throughput x Flow Time"],
        ]),
        "formulae": ["inventory = throughput * flow_time"],
    },
    "operations-management-c2-l5": {
        "data_table": table(["Term", "Formula"], [
            ["EOQ", "sqrt(2 x demand x order_cost / holding_cost)"],
        ]),
        "formulae": ["EOQ = sqrt(2 * demand * order_cost / holding_cost)"],
    },
    "operations-management-c2-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Safety stock", "Extra inventory held to buffer against demand or supply variability"], ["Reorder point", "The inventory level that triggers a new order"],
        ]),
    },
    "operations-management-c2-l7": {
        "data_table": table(["Principle", "Meaning"], [
            ["Total Quality Management", "Continuous, organization-wide commitment to quality improvement"],
        ]),
    },
    "operations-management-c2-l8": {
        "data_table": table(["Chart Type", "Use"], [
            ["X-bar chart", "Monitors the process mean over time"], ["R-chart", "Monitors process variability over time"],
        ]),
    },
    "operations-management-c2-l9": {
        "data_table": table(["Layout Type", "Best For"], [
            ["Process layout", "Low-volume, varied production"], ["Product layout", "High-volume, standardized production"],
        ]),
    },
    "operations-management-c2-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Bill of materials", "A structured list of raw materials and components needed to build a product"],
        ]),
    },
    "operations-management-c2-l11": {
        "data_table": table(["Tool", "Purpose"], [
            ["Gantt chart", "Shows task schedules and dependencies against a timeline"],
        ]),
    },
    "operations-management-c2-l12": {
        "data_table": table(["Criterion", "Consideration"], [
            ["Cost", "Total price including hidden costs"], ["Reliability", "Consistency of on-time, quality delivery"],
        ]),
    },
    "operations-management-c2-l13": {
        "data_table": table(["S", "Meaning"], [
            ["Sort", "Remove unnecessary items"], ["Set in order", "Organize remaining items efficiently"], ["Shine", "Keep the workspace clean"],
        ]),
    },
    "operations-management-c2-l14": {
        "data_table": table(["Technique", "Purpose"], [
            ["Eliminating non-value-added steps", "Directly reduces total cycle time"],
        ]),
    },
    "operations-management-c2-l15": {
        "data_table": table(["Function", "Purpose"], [
            ["Receiving", "Verifies and logs incoming inventory"], ["Picking", "Retrieves items to fulfill an order"],
        ]),
    },
    "operations-management-c2-l16": {
        "data_table": table(["Mode", "Feature"], [
            ["Air freight", "Fastest, most expensive"], ["Ocean freight", "Slowest, most cost-effective for bulk"],
        ]),
    },
    "operations-management-c2-l17": {
        "data_table": table(["Element", "Consideration"], [
            ["Customer contact point", "Determines how much of the process is visible to the customer"],
        ]),
    },
    "operations-management-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["ERP", "An integrated software system managing core business processes across departments"],
        ]),
    },
    "operations-management-c2-l19": {
        "data_table": table(["Factor", "Consideration"], [
            ["Likelihood", "How probable a disruption is"], ["Impact", "How severe the disruption would be"],
        ]),
    },
    "operations-management-c2-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Applying frameworks to a real case", "Tests theoretical operations concepts against a realistic scenario"],
        ]),
    },
    "operations-management-c2-l21": {
        "data_table": table(["Strategy", "Feature"], [
            ["Chase strategy", "Adjusts workforce to match demand fluctuations"], ["Level strategy", "Maintains stable output, absorbing demand swings with inventory"],
        ]),
    },
    "operations-management-c2-l22": {
        "data_table": table(["Technique", "Feature"], [
            ["Lot-for-lot", "Orders exactly what's needed each period"], ["Economic order quantity", "Orders a fixed optimal batch size"],
        ]),
    },
    "operations-management-c2-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Heijunka", "Levels production volume and mix to reduce waste and variability"],
        ]),
    },
    "operations-management-c2-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Multi-stage Kanban", "Uses signal cards across several linked production stages to control flow"],
        ]),
    },
    "operations-management-c2-l25": {
        "data_table": table(["Index", "Formula"], [
            ["Cp", "(USL - LSL) / (6 x std dev)"], ["Cpk", "Accounts for how centered the process is within the spec limits"],
        ]),
        "formulae": ["Cp = (USL - LSL) / (6 * std_dev)"],
    },
    "operations-management-c2-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Design for Six Sigma", "Builds quality into a product or process from the earliest design stage"],
        ]),
    },
    "operations-management-c2-l27": {
        "data_table": table(["Chart Type", "Use"], [
            ["p-chart", "Monitors the proportion of defective items"], ["c-chart", "Monitors the count of defects per unit"],
        ]),
    },
    "operations-management-c2-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Reliability-centered maintenance", "Prioritizes maintenance activities based on failure consequences and likelihood"],
        ]),
    },
    "operations-management-c2-l29": {
        "data_table": table(["Method", "Purpose"], [
            ["Center-of-gravity method", "Finds a facility location minimizing total weighted transportation distance"],
        ]),
    },
    "operations-management-c2-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Precedence diagramming", "Sequences tasks respecting their required order for line balancing"],
        ]),
    },
    "operations-management-c2-l31": {
        "data_table": table(["Model", "Feature"], [
            ["Multi-server queue", "Multiple parallel service channels reduce customer wait time"],
        ]),
    },
    "operations-management-c2-l32": {
        "data_table": table(["Element", "Purpose"], [
            ["Line of visibility", "Separates front-stage actions customers see from back-stage support processes"],
        ]),
    },
    "operations-management-c2-l33": {
        "data_table": table(["Metric", "Meaning"], [
            ["Net Promoter Score", "Measures customer likelihood to recommend a company"],
        ]),
    },
    "operations-management-c2-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Dynamic pricing", "Adjusts prices in real time based on predicted demand"],
        ]),
    },
    "operations-management-c2-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Closed-loop supply chain", "Integrates forward and reverse flows, including recycling and remanufacturing"],
        ]),
    },
    "operations-management-c2-l36": {
        "data_table": table(["Decision", "Consideration"], [
            ["Network configuration", "Balances proximity to markets against production cost across global sites"],
        ]),
    },
    "operations-management-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Total cost of ownership", "Accounts for all costs of an option, not just the initial purchase price"],
        ]),
    },
    "operations-management-c2-l38": {
        "data_table": table(["Risk", "Mitigation"], [
            ["Vendor lock-in", "Diversifying suppliers or negotiating clear exit terms"],
        ]),
    },
    "operations-management-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Collaborative planning", "Suppliers and buyers share forecasts to jointly optimize inventory"],
        ]),
    },
    "operations-management-c2-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Cross-docking", "Transfers goods directly from inbound to outbound transport with minimal storage"],
        ]),
    },
    "operations-management-c2-l41": {
        "data_table": table(["Decision", "Consideration"], [
            ["Number of distribution centers", "Balances delivery speed against facility and inventory cost"],
        ]),
    },
    "operations-management-c2-l42": {
        "data_table": table(["Model", "Best For"], [
            ["Moving average", "Stable demand with little trend or seasonality"], ["Exponential smoothing", "Demand with a trend"],
        ]),
    },
    "operations-management-c2-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["S&OP", "Aligns sales forecasts, production capacity, and financial plans across departments"],
        ]),
    },
    "operations-management-c2-l44": {
        "data_table": table(["Type", "Answers"], [
            ["Descriptive analytics", "What happened?"], ["Prescriptive analytics", "What should we do?"],
        ]),
    },
    "operations-management-c2-l45": {
        "data_table": table(["Tool", "Purpose"], [
            ["Five Whys", "Repeatedly asks why to trace a problem to its root cause"], ["Fault tree analysis", "Maps out all potential causes leading to a failure"],
        ]),
    },
    "operations-management-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Design of experiments", "Systematically varies inputs to identify which factors most affect an outcome"],
        ]),
    },
    "operations-management-c2-l47": {
        "data_table": table(["Class", "Feature"], [
            ["A items", "High value, tightly controlled"], ["C items", "Low value, loosely controlled"],
        ]),
    },
    "operations-management-c2-l48": {
        "data_table": table(["Combination", "Benefit"], [
            ["Lean Six Sigma", "Combines waste elimination with statistical defect reduction"],
        ]),
    },
    "operations-management-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Poka-yoke", "Designs a process so errors are physically prevented or immediately obvious"],
        ]),
    },
    "operations-management-c2-l50": {
        "data_table": table(["Term", "Benefit"], [
            ["Digital work instructions", "Ensures consistent execution and easy updates across a workforce"],
        ]),
    },
    "operations-management-c2-l51": {
        "data_table": table(["Rule", "Meaning"], [
            ["Shortest processing time", "Prioritizes jobs that take the least time first"],
        ]),
    },
    "operations-management-c2-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Bullwhip effect", "Small changes in consumer demand cause amplified swings upstream in the supply chain"],
        ]),
    },
    "operations-management-c2-l53": {
        "data_table": table(["Tier", "Strategy"], [
            ["Strategic suppliers", "Deep, collaborative partnership"], ["Transactional suppliers", "Managed for cost and efficiency"],
        ]),
    },
    "operations-management-c2-l54": {
        "data_table": table(["Perspective", "Focus"], [
            ["Financial", "Cost and revenue outcomes"], ["Internal process", "Operational efficiency and quality"],
        ]),
    },
    "operations-management-c2-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Concurrent engineering", "Runs design and manufacturing planning in parallel to speed up product launch"],
        ]),
    },
    "operations-management-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Supply chain resilience", "The ability to absorb and recover quickly from disruptions"],
        ]),
    },
    "operations-management-c2-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital twin", "A virtual replica of a physical operation used to simulate and optimize performance"],
        ]),
    },
    "operations-management-c2-l58": {
        "data_table": table(["Technology", "Benefit"], [
            ["Automated guided vehicles", "Move materials without manual labor, increasing warehouse throughput"],
        ]),
    },
    "operations-management-c2-l59": {
        "data_table": table(["Term", "Meaning"], [
            ["Focused factory", "A facility optimized narrowly for a specific product or process, sacrificing flexibility for efficiency"],
        ]),
    },
    "operations-management-c2-l60": {
        "data_table": table(["Component", "Purpose"], [
            ["Capstone synthesis", "Integrates operations concepts across a full real-world case study"],
        ]),
    },
    "operations-management-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Calculating an optimal order quantity", "Applying EOQ to minimize total inventory cost"],
        ]),
        "formulae": ["EOQ = sqrt(2 * demand * order_cost / holding_cost)"],
    },
    "operations-management-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Applying TQM in a real process", "Reducing defects through continuous employee-driven improvement"],
        ]),
    },
    "operations-management-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Reading a control chart", "Identifying when a process has gone out of statistical control"],
        ]),
    },
    "operations-management-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Mapping a real supply chain", "Tracing a product from raw material to customer delivery"],
        ]),
    },
    "operations-management-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Setting a reorder point", "Balancing stockout risk against holding cost for a real product"],
        ]),
    },
    "operations-management-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Identifying a bottleneck", "Finding the slowest step in a mapped process"],
        ]),
    },
    "operations-management-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Applying Little's Law", "Estimating flow time from throughput and work-in-process inventory"],
        ]),
        "formulae": ["flow_time = inventory / throughput"],
    },
    "operations-management-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Comparing ordering policies", "Weighing EOQ against just-in-time replenishment for a given item"],
        ]),
    },
    "operations-management-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Setting safety stock levels", "Balancing service level targets against holding costs"],
        ]),
    },
    "operations-management-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Diagnosing a quality issue", "Applying TQM principles to trace a recurring defect"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Operations Management"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Operations Management: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Operations Management lessons (completing 70/70).")


if __name__ == "__main__":
    main()
