#!/usr/bin/env python3
"""Depth pass, C1 Cloud Computing: fill in real, hand-checked
data_table content for the 69 C1 Cloud Computing lessons not covered
by the earlier breadth-first batch. Brings C1 Cloud Computing to full
70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_cloud_computing_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cloud-computing-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud computing", "Delivering computing services over the internet on demand"],
        ]),
    },
    "cloud-computing-c1-l2": {
        "data_table": table(["Model", "Meaning"], [
            ["IaaS", "Infrastructure as a Service, provides raw compute/storage"], ["PaaS", "Platform as a Service, provides a managed runtime"], ["SaaS", "Software as a Service, ready-to-use applications"],
        ]),
    },
    "cloud-computing-c1-l4": {
        "data_table": table(["Type", "Description"], [
            ["Public cloud", "Shared infrastructure, run by a provider"], ["Private cloud", "Dedicated infrastructure for one organization"], ["Hybrid cloud", "Combines public and private"],
        ]),
    },
    "cloud-computing-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Virtual machine", "A software-based emulation of a physical computer"],
        ]),
    },
    "cloud-computing-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Region", "A geographic location containing cloud data centers"], ["Availability zone", "An isolated data center within a region"],
        ]),
    },
    "cloud-computing-c1-l7": {
        "data_table": table(["Model", "Description"], [
            ["Pay-as-you-go", "Charged based on actual usage"], ["Reserved", "Discounted rate for committed usage"],
        ]),
    },
    "cloud-computing-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud identity", "Managing user accounts and permissions in a cloud platform"],
        ]),
    },
    "cloud-computing-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Object storage", "Stores data as discrete objects with metadata, e.g. Amazon S3"],
        ]),
    },
    "cloud-computing-c1-l10": {
        "data_table": table(["Type", "Use Case"], [
            ["Block storage", "Attached storage for a virtual machine, like a hard drive"], ["File storage", "Shared file systems accessed over a network"],
        ]),
    },
    "cloud-computing-c1-l11": {
        "data_table": table(["Tool", "Purpose"], [
            ["AWS CLI", "Command-line interface for managing AWS resources"],
        ]),
        "formulae": ["aws s3 ls"],
    },
    "cloud-computing-c1-l12": {
        "data_table": table(["Interface", "Purpose"], [
            ["Cloud console", "A web-based dashboard for managing cloud resources"],
        ]),
    },
    "cloud-computing-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Resource tagging", "Labeling cloud resources with metadata for organization and billing"],
        ]),
    },
    "cloud-computing-c1-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["SLA", "Service Level Agreement, defines guaranteed uptime and performance"],
        ]),
    },
    "cloud-computing-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Virtual Private Cloud", "An isolated network environment within a public cloud"],
        ]),
    },
    "cloud-computing-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Load balancer", "Distributes incoming traffic across multiple servers"],
        ]),
    },
    "cloud-computing-c1-l17": {
        "data_table": table(["Service", "Purpose"], [
            ["Cloud DNS", "Translates domain names to IP addresses in the cloud"],
        ]),
    },
    "cloud-computing-c1-l18": {
        "data_table": table(["Service", "Purpose"], [
            ["Cloud backup", "Automatically copies data to prevent loss"],
        ]),
    },
    "cloud-computing-c1-l19": {
        "data_table": table(["Party", "Responsibility"], [
            ["Cloud provider", "Secures the underlying infrastructure"], ["Customer", "Secures data, access, and configuration"],
        ]),
    },
    "cloud-computing-c1-l20": {
        "data_table": table(["Strategy", "Description"], [
            ["Lift and shift", "Moving applications to the cloud with minimal changes"], ["Re-architecting", "Redesigning apps to be cloud-native"],
        ]),
    },
    "cloud-computing-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Serverless computing", "Running code without managing the underlying servers"],
        ]),
    },
    "cloud-computing-c1-l22": {
        "data_table": table(["Platform", "Example"], [
            ["FaaS", "AWS Lambda, Google Cloud Functions"],
        ]),
    },
    "cloud-computing-c1-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Compute instance", "A virtual server running in the cloud"],
        ]),
    },
    "cloud-computing-c1-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Elasticity", "Automatically scaling resources up or down based on demand"],
        ]),
    },
    "cloud-computing-c1-l25": {
        "data_table": table(["Practice", "Benefit"], [
            ["Cost monitoring dashboards", "Tracks and controls cloud spending"],
        ]),
    },
    "cloud-computing-c1-l26": {
        "data_table": table(["Tool", "Purpose"], [
            ["Budget alerts", "Notify when spending approaches a set limit"],
        ]),
    },
    "cloud-computing-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Infrastructure as Code", "Managing infrastructure through machine-readable configuration files"],
        ]),
    },
    "cloud-computing-c1-l28": {
        "data_table": table(["Tool", "Purpose"], [
            ["Terraform", "Provisions and manages cloud infrastructure declaratively"], ["Ansible", "Automates configuration management"],
        ]),
    },
    "cloud-computing-c1-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud API", "Programmatic interface for interacting with cloud services"], ["SDK", "Software Development Kit, a library for building against an API"],
        ]),
    },
    "cloud-computing-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Automation script", "Code that automatically performs repeated cloud management tasks"],
        ]),
    },
    "cloud-computing-c1-l31": {
        "data_table": table(["Regulation", "Focus"], [
            ["GDPR", "EU data privacy compliance"],
        ]),
    },
    "cloud-computing-c1-l32": {
        "data_table": table(["State", "Protection"], [
            ["Data at rest", "Encrypted while stored"], ["Data in transit", "Encrypted while being transmitted"],
        ]),
    },
    "cloud-computing-c1-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud IAM", "Controls who can access which cloud resources and what they can do"],
        ]),
    },
    "cloud-computing-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["MFA", "Multi-Factor Authentication, requires two or more verification methods"],
        ]),
    },
    "cloud-computing-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud logging", "Records events for monitoring and troubleshooting"],
        ]),
    },
    "cloud-computing-c1-l36": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Right-sizing instances", "Matches compute resources to actual need, reducing waste"],
        ]),
    },
    "cloud-computing-c1-l37": {
        "data_table": table(["Type", "Feature"], [
            ["Reserved instance", "Discounted rate for a committed term"], ["Spot instance", "Discounted, but can be reclaimed by the provider"],
        ]),
    },
    "cloud-computing-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Snapshot", "A point-in-time copy of a storage volume"],
        ]),
    },
    "cloud-computing-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Disaster recovery", "A plan for restoring systems after a major outage"],
        ]),
    },
    "cloud-computing-c1-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["High availability", "Designing systems to minimize downtime, often via redundancy"],
        ]),
    },
    "cloud-computing-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Fault tolerance", "A system's ability to continue operating despite component failure"],
        ]),
    },
    "cloud-computing-c1-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Multi-cloud strategy", "Using multiple cloud providers to avoid dependency on one"],
        ]),
    },
    "cloud-computing-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Hybrid cloud architecture", "Combines on-premises infrastructure with public cloud services"],
        ]),
    },
    "cloud-computing-c1-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud-native application", "Built specifically to take advantage of cloud computing features"],
        ]),
    },
    "cloud-computing-c1-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Microservices", "Small, independent services that together make up an application"],
        ]),
    },
    "cloud-computing-c1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["API gateway", "Manages, routes, and secures API requests to backend services"],
        ]),
    },
    "cloud-computing-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["CI/CD pipeline", "Automates building, testing, and deploying application code"],
        ]),
    },
    "cloud-computing-c1-l48": {
        "data_table": table(["Environment", "Purpose"], [
            ["Development", "Where new code is written and tested"], ["Production", "The live environment users interact with"],
        ]),
    },
    "cloud-computing-c1-l49": {
        "data_table": table(["Practice", "Benefit"], [
            ["Cost tagging by project", "Clarifies which team or project incurs which cloud costs"],
        ]),
    },
    "cloud-computing-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Vendor lock-in", "Difficulty switching cloud providers due to proprietary dependencies"],
        ]),
    },
    "cloud-computing-c1-l51": {
        "data_table": table(["Certification", "Provider"], [
            ["AWS Certified Cloud Practitioner", "Amazon Web Services"], ["Azure Fundamentals", "Microsoft Azure"],
        ]),
    },
    "cloud-computing-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Egress cost", "The fee charged for data leaving a cloud provider's network"],
        ]),
    },
    "cloud-computing-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Edge location", "A site closer to end users that caches content to reduce latency"],
        ]),
    },
    "cloud-computing-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Data center", "A physical facility housing the servers that power cloud services"],
        ]),
    },
    "cloud-computing-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud sustainability", "Efforts to reduce the environmental impact of data centers"],
        ]),
    },
    "cloud-computing-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["IP addressing", "Assigning unique numerical identifiers to devices on a network"],
        ]),
    },
    "cloud-computing-c1-l57": {
        "data_table": table(["Tier", "Feature"], [
            ["Basic support", "Community forums and documentation"], ["Enterprise support", "24/7 direct access to engineers"],
        ]),
    },
    "cloud-computing-c1-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud marketplace", "A storefront for pre-configured third-party software and services"],
        ]),
    },
    "cloud-computing-c1-l59": {
        "data_table": table(["Pillar", "Focus"], [
            ["Operational excellence", "Running and monitoring systems effectively"], ["Security", "Protecting data and systems"],
        ]),
    },
    "cloud-computing-c1-l60": {
        "data_table": table(["Career", "Focus"], [
            ["Cloud engineer", "Builds and maintains cloud infrastructure"], ["Cloud architect", "Designs overall cloud system architecture"],
        ]),
    },
    "cloud-computing-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a service model", "Deciding between IaaS and SaaS for a sample project"],
        ]),
    },
    "cloud-computing-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Comparing pricing tiers", "Estimating monthly cost for a small versus large workload"],
        ]),
    },
    "cloud-computing-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Comparing provider services", "Matching equivalent services across AWS, Azure, and GCP"],
        ]),
    },
    "cloud-computing-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a deployment type", "Deciding when a hybrid cloud fits a company's needs"],
        ]),
    },
    "cloud-computing-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Launching a virtual machine", "Selecting instance size for a sample web app"],
        ]),
    },
    "cloud-computing-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Planning for redundancy", "Placing resources across multiple availability zones"],
        ]),
    },
    "cloud-computing-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Estimating monthly cost", "Comparing pay-as-you-go versus reserved pricing"],
        ]),
    },
    "cloud-computing-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Setting up user roles", "Assigning least-privilege access for a small team"],
        ]),
    },
    "cloud-computing-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Storing files in the cloud", "Uploading and retrieving an object from cloud storage"],
        ]),
    },
    "cloud-computing-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Choosing storage type", "Deciding between block and file storage for a database server"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cloud Computing"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Cloud Computing: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Cloud Computing lessons (completing 70/70).")


if __name__ == "__main__":
    main()
