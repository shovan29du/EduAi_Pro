#!/usr/bin/env python3
"""Depth pass, C2 Cloud Computing: fill in real, hand-checked
data_table/formulae content for the 69 C2 Cloud Computing lessons not
covered by the earlier breadth-first batch. Brings C2 Cloud Computing to
full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_cloud_computing_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cloud-computing-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Virtual machine", "An emulated computer running on shared physical hardware"], ["Container", "A lightweight, isolated process sharing the host OS kernel"],
        ]),
    },
    "cloud-computing-c2-l2": {
        "data_table": table(["Type", "Use Case"], [
            ["Object storage", "Unstructured data like images and backups"], ["Block storage", "Low-latency storage for databases and VM disks"],
        ]),
    },
    "cloud-computing-c2-l4": {
        "data_table": table(["Key", "Purpose"], [
            ["services", "Defines each container in a multi-container app"],
        ]),
        "formulae": ["services:\n  web:\n    build: .\n  db:\n    image: postgres"],
    },
    "cloud-computing-c2-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Container registry", "A repository for storing and distributing container images"],
        ]),
        "formulae": ["docker push myregistry.com/myapp:1.0"],
    },
    "cloud-computing-c2-l6": {
        "data_table": table(["Component", "Role"], [
            ["Control plane", "Manages the overall state of the cluster"], ["Node", "A worker machine running containerized workloads"],
        ]),
    },
    "cloud-computing-c2-l7": {
        "data_table": table(["Object", "Purpose"], [
            ["Pod", "The smallest deployable unit, wrapping one or more containers"], ["Deployment", "Manages replica pods and rolling updates"], ["Service", "Provides stable networking to a set of pods"],
        ]),
    },
    "cloud-computing-c2-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Namespace", "A virtual cluster partition for organizing resources"], ["Resource quota", "Limits resource consumption within a namespace"],
        ]),
    },
    "cloud-computing-c2-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Helm chart", "A packaged, reusable set of Kubernetes resource templates"],
        ]),
        "formulae": ["helm install myapp ./mychart"],
    },
    "cloud-computing-c2-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["VPC", "An isolated virtual network within a cloud provider"],
        ]),
    },
    "cloud-computing-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Subnet", "A segmented range of IP addresses within a larger network"],
        ]),
    },
    "cloud-computing-c2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Security group", "A virtual firewall controlling inbound and outbound traffic to a resource"],
        ]),
    },
    "cloud-computing-c2-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["CDN", "Distributes cached content across geographically distributed edge servers"],
        ]),
    },
    "cloud-computing-c2-l14": {
        "data_table": table(["Policy Type", "Trigger"], [
            ["Target tracking", "Scales to maintain a target metric like CPU utilization"], ["Scheduled scaling", "Scales based on predictable time patterns"],
        ]),
    },
    "cloud-computing-c2-l15": {
        "data_table": table(["Instance Type", "Best For"], [
            ["Compute-optimized", "CPU-intensive workloads"], ["Memory-optimized", "Large in-memory databases"],
        ]),
    },
    "cloud-computing-c2-l16": {
        "data_table": table(["Tier", "Use"], [
            ["Hot storage", "Frequently accessed data"], ["Cold/archive storage", "Rarely accessed, lower-cost long-term data"],
        ]),
    },
    "cloud-computing-c2-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Replication", "Maintaining copies of data across multiple locations for availability"],
        ]),
    },
    "cloud-computing-c2-l18": {
        "data_table": table(["Benefit", "Detail"], [
            ["Managed database service", "Provider handles patching, backups, and scaling"],
        ]),
    },
    "cloud-computing-c2-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Message queue", "Decouples producers and consumers, buffering messages between services"],
        ]),
    },
    "cloud-computing-c2-l20": {
        "data_table": table(["Metric", "Signals"], [
            ["CPU utilization", "Whether an instance needs more or fewer resources"],
        ]),
    },
    "cloud-computing-c2-l21": {
        "data_table": table(["Concept", "Meaning"], [
            ["Infrastructure as Code", "Defines and provisions infrastructure through machine-readable config files"],
        ]),
        "formulae": ["resource \"aws_instance\" \"web\" {\n  ami = \"ami-123\"\n  instance_type = \"t2.micro\"\n}"],
    },
    "cloud-computing-c2-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Ansible playbook", "A declarative script automating configuration across multiple servers"],
        ]),
        "formulae": ["- hosts: web\n  tasks:\n    - name: install nginx\n      apt: name=nginx state=present"],
    },
    "cloud-computing-c2-l23": {
        "data_table": table(["Stage", "Purpose"], [
            ["Continuous Integration", "Automatically builds and tests code changes"], ["Continuous Deployment", "Automatically deploys passing changes to production"],
        ]),
    },
    "cloud-computing-c2-l24": {
        "data_table": table(["Strategy", "Feature"], [
            ["Blue-green deployment", "Switches traffic instantly between two full environments"], ["Canary deployment", "Gradually shifts traffic to the new version"],
        ]),
    },
    "cloud-computing-c2-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Kubernetes Operator", "Extends Kubernetes to automate management of complex applications"],
        ]),
    },
    "cloud-computing-c2-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Service mesh", "A dedicated infrastructure layer managing service-to-service communication"],
        ]),
    },
    "cloud-computing-c2-l27": {
        "data_table": table(["Type", "Scales"], [
            ["Horizontal Pod Autoscaler", "Number of pod replicas"], ["Vertical Pod Autoscaler", "Resource requests per pod"],
        ]),
    },
    "cloud-computing-c2-l28": {
        "data_table": table(["Practice", "Reason"], [
            ["Scanning images for vulnerabilities", "Prevents deploying containers with known security flaws"],
        ]),
    },
    "cloud-computing-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Identity federation", "Allows users to authenticate across systems using one trusted identity provider"],
        ]),
    },
    "cloud-computing-c2-l30": {
        "data_table": table(["Principle", "Meaning"], [
            ["Zero Trust", "Verifies every request regardless of network location"],
        ]),
    },
    "cloud-computing-c2-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["VPC peering", "Directly connects two virtual networks"], ["Transit gateway", "Centrally connects many VPCs through a single hub"],
        ]),
    },
    "cloud-computing-c2-l32": {
        "data_table": table(["Type", "Feature"], [
            ["Layer 4 load balancer", "Routes based on IP and port"], ["Layer 7 load balancer", "Routes based on application content like URL path"],
        ]),
    },
    "cloud-computing-c2-l33": {
        "data_table": table(["Routing Policy", "Behavior"], [
            ["Latency-based routing", "Directs users to the lowest-latency endpoint"], ["Weighted routing", "Splits traffic by configured percentages"],
        ]),
    },
    "cloud-computing-c2-l34": {
        "data_table": table(["Pattern", "Use"], [
            ["Data lake", "Stores raw data at scale for later processing"],
        ]),
    },
    "cloud-computing-c2-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Distributed database", "Spreads data across multiple nodes for scalability and fault tolerance"],
        ]),
    },
    "cloud-computing-c2-l36": {
        "data_table": table(["Technique", "Benefit"], [
            ["Query indexing", "Reduces lookup time for frequently queried columns"],
        ]),
    },
    "cloud-computing-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Event-driven architecture", "Components communicate by producing and reacting to events"],
        ]),
    },
    "cloud-computing-c2-l38": {
        "data_table": table(["Pattern", "Use"], [
            ["Publish-subscribe", "Broadcasts a message to multiple independent subscribers"],
        ]),
    },
    "cloud-computing-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Serverless", "Runs code without managing underlying servers, scaling automatically"],
        ]),
    },
    "cloud-computing-c2-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["FinOps", "A practice for managing and optimizing cloud spending"],
        ]),
    },
    "cloud-computing-c2-l41": {
        "data_table": table(["Benefit", "Detail"], [
            ["Multi-region architecture", "Improves latency and disaster resilience by serving users from multiple regions"],
        ]),
    },
    "cloud-computing-c2-l42": {
        "data_table": table(["Metric", "Meaning"], [
            ["RTO", "Maximum acceptable time to restore service after a failure"], ["RPO", "Maximum acceptable amount of data loss measured in time"],
        ]),
    },
    "cloud-computing-c2-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Chaos engineering", "Deliberately injects failures to test system resilience"],
        ]),
    },
    "cloud-computing-c2-l44": {
        "data_table": table(["Pillar", "Focus"], [
            ["Metrics", "Numeric measurements over time"], ["Logs", "Discrete event records"], ["Traces", "The path of a request across services"],
        ]),
    },
    "cloud-computing-c2-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["SRE", "Applies software engineering practices to operations and reliability"],
        ]),
    },
    "cloud-computing-c2-l46": {
        "data_table": table(["Practice", "Purpose"], [
            ["Policy as code", "Enforces compliance rules automatically across cloud resources"],
        ]),
    },
    "cloud-computing-c2-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["CSPM", "Continuously monitors cloud environments for misconfigurations and risks"],
        ]),
    },
    "cloud-computing-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Key management service", "Centrally manages encryption keys used to protect cloud data"],
        ]),
    },
    "cloud-computing-c2-l49": {
        "data_table": table(["Challenge", "Detail"], [
            ["Multi-cloud networking", "Connecting resources across different cloud providers securely"],
        ]),
    },
    "cloud-computing-c2-l50": {
        "data_table": table(["Strategy", "Meaning"], [
            ["Lift and shift", "Migrates applications with minimal changes"], ["Re-architecting", "Redesigns an application to be cloud-native"],
        ]),
    },
    "cloud-computing-c2-l51": {
        "data_table": table(["Approach", "Meaning"], [
            ["Application modernization", "Updating legacy applications to use cloud-native patterns"],
        ]),
    },
    "cloud-computing-c2-l52": {
        "data_table": table(["Technique", "Purpose"], [
            ["Caching layer", "Reduces latency by storing frequently accessed data closer to users"],
        ]),
    },
    "cloud-computing-c2-l53": {
        "data_table": table(["Step", "Purpose"], [
            ["Forecasting resource demand", "Prevents both over-provisioning cost and under-provisioning outages"],
        ]),
    },
    "cloud-computing-c2-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Pipeline as code", "Defines CI/CD pipelines in version-controlled configuration files"],
        ]),
    },
    "cloud-computing-c2-l55": {
        "data_table": table(["Principle", "Meaning"], [
            ["GitOps", "Uses Git as the single source of truth for infrastructure state"],
        ]),
    },
    "cloud-computing-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Software-defined networking", "Manages network behavior programmatically rather than via physical hardware config"],
        ]),
    },
    "cloud-computing-c2-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Persistent volume", "Cloud-native storage that survives beyond a pod's lifecycle"],
        ]),
    },
    "cloud-computing-c2-l58": {
        "data_table": table(["Factor", "Consideration"], [
            ["Reserved instances", "Lower cost in exchange for a longer usage commitment"],
        ]),
    },
    "cloud-computing-c2-l59": {
        "data_table": table(["Pattern", "Use"], [
            ["Circuit breaker", "Prevents cascading failures by stopping calls to a failing service"],
        ]),
    },
    "cloud-computing-c2-l60": {
        "data_table": table(["Component", "Consideration"], [
            ["Availability", "Designing for redundancy across zones or regions"],
        ]),
    },
    "cloud-computing-c2-l61": {
        "data_table": table(["Stage", "Automation"], [
            ["Automated testing", "Runs on every commit before merging"],
        ]),
    },
    "cloud-computing-c2-l62": {
        "data_table": table(["Rollback Speed", "Strategy"], [
            ["Instant", "Blue-green, by switching the router back"],
        ]),
    },
    "cloud-computing-c2-l63": {
        "data_table": table(["Component", "Role"], [
            ["Event bus", "Routes events from producers to interested consumers"],
        ]),
    },
    "cloud-computing-c2-l64": {
        "data_table": table(["Tool", "Purpose"], [
            ["Fault injection tool", "Simulates failures like latency spikes or service outages"],
        ]),
    },
    "cloud-computing-c2-l65": {
        "data_table": table(["Metric", "Meaning"], [
            ["Error budget", "The acceptable amount of unreliability before halting new releases"],
        ]),
    },
    "cloud-computing-c2-l66": {
        "data_table": table(["Check", "Purpose"], [
            ["Automated configuration scan", "Flags publicly exposed storage buckets or open security groups"],
        ]),
    },
    "cloud-computing-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Comparing VMs and containers", "Choosing the right isolation level for a workload"],
        ]),
    },
    "cloud-computing-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a storage tier", "Selecting hot versus archive storage based on access frequency"],
        ]),
    },
    "cloud-computing-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Writing a Dockerfile", "Building a minimal container image for an application"],
        ]),
        "formulae": ["FROM python:3.11-slim\nCOPY . /app\nCMD [\"python\", \"app.py\"]"],
    },
    "cloud-computing-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Orchestrating multiple services", "Defining a web app and database together with Compose"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cloud Computing"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Cloud Computing: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Cloud Computing lessons (completing 70/70).")


if __name__ == "__main__":
    main()
