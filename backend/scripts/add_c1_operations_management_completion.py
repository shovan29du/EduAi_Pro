#!/usr/bin/env python3
"""Depth pass, C1 Operations Management: fill in real, hand-checked
data_table content for the 69 C1 Operations Management lessons not
covered by the earlier breadth-first batch. Brings C1 Operations
Management to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_operations_management_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "operations-management-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Operations management", "Designing, running, and improving the processes that create goods and services"],
        ]),
    },
    "operations-management-c1-l2": {
        "data_table": table(["Element", "Purpose"], [
            ["Process map", "Visualizes the steps, decisions, and flows in a process"],
        ]),
    },
    "operations-management-c1-l4": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Rectangle", "A process step or activity"], ["Diamond", "A decision point"],
        ]),
    },
    "operations-management-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Bottleneck", "The step in a process with the least capacity, limiting overall throughput"],
        ]),
    },
    "operations-management-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Inventory", "Goods and materials a business holds for production or resale"],
        ]),
    },
    "operations-management-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Quality", "The degree to which a product or service meets customer requirements"],
        ]),
    },
    "operations-management-c1-l8": {
        "data_table": table(["Layout Type", "Best For"], [
            ["Process layout", "Low-volume, varied production"], ["Product layout", "High-volume, standardized production"],
        ]),
    },
    "operations-management-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Supply chain", "The network of suppliers, producers, and distributors delivering a product"],
        ]),
    },
    "operations-management-c1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Forecasting", "Predicting future demand using historical data and trends"],
        ]),
    },
    "operations-management-c1-l11": {
        "data_table": table(["Tool", "Purpose"], [
            ["Gantt chart", "Shows tasks against a timeline to track project progress"],
        ]),
    },
    "operations-management-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Statistical process control", "Uses control charts to monitor whether a process stays within limits"],
        ]),
    },
    "operations-management-c1-l13": {
        "data_table": table(["Principle", "Meaning"], [
            ["Eliminating waste", "Removing any activity that doesn't add value for the customer"],
        ]),
    },
    "operations-management-c1-l14": {
        "data_table": table(["Cost Type", "Example"], [
            ["Fixed cost", "Rent, independent of output volume"], ["Variable cost", "Raw materials, scales with output"],
        ]),
    },
    "operations-management-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Procurement", "The process of sourcing and purchasing goods and services"],
        ]),
    },
    "operations-management-c1-l16": {
        "data_table": table(["Factor", "Consideration"], [
            ["Proximity to customers", "Reduces delivery time and shipping cost"],
        ]),
    },
    "operations-management-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Service blueprint", "A diagram mapping customer actions against front-stage and back-stage service steps"],
        ]),
    },
    "operations-management-c1-l18": {
        "data_table": table(["Technology", "Use in Operations"], [
            ["ERP systems", "Integrate planning, inventory, and production data"],
        ]),
    },
    "operations-management-c1-l19": {
        "data_table": table(["Risk Type", "Example"], [
            ["Supply disruption", "A key supplier fails to deliver on time"],
        ]),
    },
    "operations-management-c1-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Defining the problem clearly", "Ensures the case study analysis stays focused"],
        ]),
    },
    "operations-management-c1-l21": {
        "data_table": table(["System Type", "Example"], [
            ["Continuous production", "Oil refining runs nonstop with minimal variation"],
        ]),
    },
    "operations-management-c1-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Job shop", "Produces small batches of highly customized products"], ["Batch production", "Produces groups of similar items together"],
        ]),
    },
    "operations-management-c1-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Mass production", "Produces large volumes of standardized items efficiently"],
        ]),
    },
    "operations-management-c1-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Capacity planning", "Determining the production capacity needed to meet demand"],
        ]),
    },
    "operations-management-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Aggregate planning", "Balancing production, workforce, and inventory over a medium-term horizon"],
        ]),
    },
    "operations-management-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["MRP", "Material Requirements Planning, schedules materials needed based on production plans"],
        ]),
    },
    "operations-management-c1-l27": {
        "data_table": table(["Principle", "Meaning"], [
            ["Just-in-time", "Materials arrive exactly when needed, minimizing inventory holding"],
        ]),
    },
    "operations-management-c1-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Kanban", "A visual signaling system that triggers replenishment when supplies run low"],
        ]),
    },
    "operations-management-c1-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Process capability", "A measure of how well a process output fits within specification limits"],
        ]),
    },
    "operations-management-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Six Sigma", "A data-driven methodology aiming to reduce process defects to near zero"],
        ]),
    },
    "operations-management-c1-l31": {
        "data_table": table(["Phase", "Purpose"], [
            ["Define", "Identify the problem and project goals"], ["Measure", "Collect data on current performance"],
            ["Analyze", "Find root causes of defects"], ["Improve", "Implement solutions"], ["Control", "Sustain the improvement"],
        ]),
    },
    "operations-management-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Total Productive Maintenance", "An approach making equipment upkeep everyone's responsibility to maximize uptime"],
        ]),
    },
    "operations-management-c1-l33": {
        "data_table": table(["Factor", "Consideration"], [
            ["Labor costs", "Varies significantly by region and affects total operating cost"],
        ]),
    },
    "operations-management-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Line balancing", "Distributing tasks evenly across workstations to minimize idle time"],
        ]),
    },
    "operations-management-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Queuing theory", "The mathematical study of waiting lines and service systems"],
        ]),
    },
    "operations-management-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Service operations", "Managing the delivery of intangible, often customer-facing offerings"],
        ]),
    },
    "operations-management-c1-l37": {
        "data_table": table(["Factor", "Effect"], [
            ["Wait time", "Longer waits generally reduce customer satisfaction"],
        ]),
    },
    "operations-management-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Yield management", "Adjusting prices dynamically based on demand to maximize revenue"],
        ]),
    },
    "operations-management-c1-l39": {
        "data_table": table(["Practice", "Benefit"], [
            ["Reducing packaging waste", "Lowers environmental impact and material cost"],
        ]),
    },
    "operations-management-c1-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Reverse logistics", "The process of moving goods from customers back to the seller or manufacturer"],
        ]),
    },
    "operations-management-c1-l41": {
        "data_table": table(["Strategy", "Focus"], [
            ["Global operations strategy", "Coordinating production and sourcing across multiple countries"],
        ]),
    },
    "operations-management-c1-l42": {
        "data_table": table(["Decision", "Consideration"], [
            ["Make", "Produce in-house when it's a core competency"], ["Buy", "Outsource when a supplier is more efficient"],
        ]),
    },
    "operations-management-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Outsourcing", "Contracting work to an external provider"], ["Offshoring", "Relocating operations to another country"],
        ]),
    },
    "operations-management-c1-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Vendor Managed Inventory", "The supplier monitors and replenishes the buyer's stock directly"],
        ]),
    },
    "operations-management-c1-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Cross-docking", "Unloading goods from inbound trucks directly onto outbound trucks with minimal storage"],
        ]),
    },
    "operations-management-c1-l46": {
        "data_table": table(["Factor", "Consideration"], [
            ["Number of distribution centers", "Balances delivery speed against facility and inventory cost"],
        ]),
    },
    "operations-management-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Demand planning", "Forecasting and coordinating future customer demand across the supply chain"],
        ]),
    },
    "operations-management-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["S&OP", "Sales and Operations Planning, aligns sales forecasts with production capacity"],
        ]),
    },
    "operations-management-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Operations analytics", "Using data analysis to improve process efficiency and decision-making"],
        ]),
    },
    "operations-management-c1-l50": {
        "data_table": table(["Step", "Purpose"], [
            ["Asking 'why' repeatedly", "Traces a problem back to its underlying root cause"],
        ]),
    },
    "operations-management-c1-l51": {
        "data_table": table(["Category", "Example"], [
            ["Fishbone diagram", "Groups potential causes into categories like people, methods, and materials"],
        ]),
    },
    "operations-management-c1-l52": {
        "data_table": table(["Principle", "Meaning"], [
            ["Pareto analysis", "About 80% of problems often come from 20% of causes"],
        ]),
    },
    "operations-management-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Kaizen", "A philosophy of continuous, incremental improvement involving all employees"],
        ]),
    },
    "operations-management-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Poka-yoke", "Designing processes or devices to prevent errors before they occur"],
        ]),
    },
    "operations-management-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["SOP", "Standard Operating Procedure, a documented step-by-step method for a task"],
        ]),
    },
    "operations-management-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Scheduling", "Assigning resources and timing to complete tasks efficiently"],
        ]),
    },
    "operations-management-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Bullwhip effect", "Small changes in consumer demand cause amplified swings upstream in the supply chain"],
        ]),
    },
    "operations-management-c1-l58": {
        "data_table": table(["Practice", "Benefit"], [
            ["Building strong supplier relationships", "Improves reliability, pricing, and collaboration"],
        ]),
    },
    "operations-management-c1-l59": {
        "data_table": table(["Metric", "Tracks"], [
            ["On-time delivery rate", "Percentage of orders delivered by the promised date"],
        ]),
    },
    "operations-management-c1-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Cross-functional review", "Aligns design, manufacturing, and marketing before a product launch"],
        ]),
    },
    "operations-management-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a real process", "Applying operations management principles to a case scenario"],
        ]),
    },
    "operations-management-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Redesigning a process map", "Removing redundant steps identified through analysis"],
        ]),
    },
    "operations-management-c1-l63": {
        "data_table": table(["Metric", "Formula"], [
            ["Throughput rate", "Units produced divided by time taken"],
        ]),
        "formulae": ["Throughput = Units Produced / Time"],
    },
    "operations-management-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Mapping a real flowchart", "Documenting the steps of an order fulfillment process"],
        ]),
    },
    "operations-management-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Identifying a bottleneck", "Finding the slowest station in an assembly line"],
        ]),
    },
    "operations-management-c1-l66": {
        "data_table": table(["Metric", "Formula"], [
            ["Inventory turnover", "Cost of goods sold divided by average inventory"],
        ]),
        "formulae": ["Inventory Turnover = COGS / Average Inventory"],
    },
    "operations-management-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Assessing quality issues", "Reviewing defect reports to identify recurring problems"],
        ]),
    },
    "operations-management-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Redesigning a workspace", "Rearranging equipment to shorten worker travel distance"],
        ]),
    },
    "operations-management-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Mapping a supply chain", "Diagramming suppliers, manufacturers, and distributors for a product"],
        ]),
    },
    "operations-management-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Building a demand forecast", "Using past sales data to project next quarter's demand"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Operations Management"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Operations Management: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Operations Management lessons (completing 70/70).")


if __name__ == "__main__":
    main()
