#!/usr/bin/env python3
"""Depth pass, M1 Cloud Computing: fill in real, hand-checked
data_table content for the 119 M1 Cloud Computing lessons not
covered by the earlier breadth-first batch. Brings M1 Cloud
Computing to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
Kubernetes/container internals, cloud networking and security,
reliability engineering, FinOps, and enterprise cloud governance;
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_cloud_computing_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Edge computing", "Processing data near its source rather than in a centralized cloud"],
    ["Latency benefit", "Reduced delay by avoiding round trips to distant servers"],
])

CHARTS: dict[str, dict] = {
    "cloud-computing-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Multi-cloud / hybrid cloud", "Uses more than one cloud provider, or combines cloud with on-premises infrastructure"],
    ])},
    "cloud-computing-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Cloud observability", "Monitors metrics, logs, and traces to understand a cloud system's health"],
    ])},
    "cloud-computing-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Edge CDN delivery", "Serves content from edge locations close to users to reduce latency"],
    ])},
    "cloud-computing-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Kubernetes operator", "Automates operational tasks for a custom resource using Kubernetes' own API"],
    ])},
    "cloud-computing-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Multi-cluster management", "Coordinates deployment and policy across several Kubernetes clusters"],
    ])},
    "cloud-computing-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Service mesh traffic management", "Controls routing, retries, and load balancing between microservices"],
    ])},
    "cloud-computing-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["OpenTelemetry", "A standard for collecting metrics, logs, and traces across cloud-native systems"],
    ])},
    "cloud-computing-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["FinOps", "Practices for managing and optimizing cloud spend across an organization"],
    ])},
    "cloud-computing-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Green computing", "Reduces the energy consumption and carbon footprint of cloud infrastructure"],
    ])},
    "cloud-computing-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise cloud security architecture", "Designs layered security controls across a large-scale cloud deployment"],
    ])},
    "cloud-computing-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Confidential computing", "Processes data in a hardware-isolated trusted execution environment"],
    ])},
    "cloud-computing-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Serverless orchestration (Step Functions)", "Coordinates multiple serverless functions into a defined workflow"],
    ])},
    "cloud-computing-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Data mesh in the cloud", "Decentralizes data ownership to domain teams within a cloud platform"],
    ])},
    "cloud-computing-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Cloud-native ML infrastructure", "Provisions scalable compute and storage tailored for training and serving models"],
    ])},
    "cloud-computing-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["MLOps on cloud platforms", "Applies deployment and monitoring discipline to ML using managed cloud services"],
    ])},
    "cloud-computing-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Multi-cloud networking", "Connects workloads running across different cloud providers"],
    ])},
    "cloud-computing-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Cloud platform governance", "Enforces organization-wide policy and standards across cloud resources"],
    ])},
    "cloud-computing-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Cloud reliability engineering", "Applies SRE practices to keep cloud services available and performant"],
    ])},
    "cloud-computing-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Enterprise cloud migration program", "Plans and executes moving a large organization's workloads to the cloud"],
    ])},
    "cloud-computing-m1-l21": {"data_table": table(["Type", "Feature"], [
        ["Type 1 hypervisor", "Runs directly on hardware for better performance and isolation"],
        ["Type 2 hypervisor", "Runs on top of a host operating system"],
    ])},
    "cloud-computing-m1-l22": {"data_table": table(["Kernel Feature", "Role"], [
        ["Namespaces", "Isolate what a container can see (processes, network, filesystem)"],
        ["cgroups", "Limit and account for a container's resource usage"],
    ])},
    "cloud-computing-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Custom scheduling policy", "Controls how Kubernetes assigns pods to nodes beyond the default algorithm"],
    ])},
    "cloud-computing-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["CNI plugin", "Implements how pods get network connectivity in a Kubernetes cluster"],
    ])},
    "cloud-computing-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Sidecar proxy", "Intercepts a service's network traffic to add observability, security, and routing logic"],
    ])},
    "cloud-computing-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Persistent volume", "Provides durable storage to a container that survives pod restarts"],
    ])},
    "cloud-computing-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Distributed consensus", "Lets nodes in a cloud control plane agree on state despite failures (e.g. Raft)"],
    ])},
    "cloud-computing-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Active-active architecture", "Runs multiple regions simultaneously serving live traffic for resilience"],
    ])},
    "cloud-computing-m1-l29": {"data_table": table(["Layer", "Feature"], [
        ["Layer 4 load balancing", "Routes traffic based on IP and port"],
        ["Layer 7 load balancing", "Routes traffic based on application content like HTTP headers"],
    ])},
    "cloud-computing-m1-l30": {"data_table": table(["Approach", "Feature"], [
        ["Reactive scaling", "Adds capacity after load thresholds are crossed"],
        ["Predictive scaling", "Anticipates demand using historical patterns"],
    ])},
    "cloud-computing-m1-l31": {"data_table": table(["Pricing Model", "Feature"], [
        ["Spot", "Cheapest, but can be reclaimed with little notice"],
        ["Reserved", "Discounted in exchange for a long-term commitment"],
        ["On-demand", "Pay-as-you-go with no commitment"],
    ])},
    "cloud-computing-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Declarative state reconciliation", "Continuously adjusts actual infrastructure to match a desired declared state"],
    ])},
    "cloud-computing-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Terraform state drift", "Occurs when real infrastructure diverges from what Terraform's state file records"],
    ])},
    "cloud-computing-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["GitOps", "Uses a Git repository as the source of truth to drive continuous deployment"],
    ])},
    "cloud-computing-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["CI/CD pipeline hardening", "Secures build and deployment pipelines against tampering or credential leakage"],
    ])},
    "cloud-computing-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["SBOM / provenance", "Documents a software artifact's components and build origin for supply chain security"],
    ])},
    "cloud-computing-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Zero trust in the cloud", "Verifies every request regardless of network origin instead of trusting a perimeter"],
    ])},
    "cloud-computing-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["IAM federation", "Lets identities from an external provider authenticate into a cloud account"],
    ])},
    "cloud-computing-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Cloud key management service", "Manages the lifecycle of cryptographic keys used to protect cloud data"],
    ])},
    "cloud-computing-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Secrets management", "Securely stores and distributes credentials to distributed cloud applications"],
    ])},
    "cloud-computing-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Workload identity", "Issues short-lived credentials tied to a workload rather than long-lived static keys"],
    ])},
    "cloud-computing-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Trusted execution environment", "A hardware-isolated region that protects code and data even from the host operator"],
    ])},
    "cloud-computing-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Homomorphic encryption", "Allows computation directly on encrypted cloud data without decrypting it"],
    ])},
    "cloud-computing-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Micro-segmentation", "Divides a cloud network into small isolated zones to limit lateral movement"],
    ])},
    "cloud-computing-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["DDoS mitigation", "Absorbs or filters distributed denial-of-service traffic before it disrupts a service"],
    ])},
    "cloud-computing-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Circuit breaker pattern", "Stops calling a failing dependency temporarily to prevent cascading failure"],
    ])},
    "cloud-computing-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Chaos engineering", "Deliberately injects failures to test a system's resilience"],
    ])},
    "cloud-computing-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Error budget / SLO", "A defined allowance for unreliability used to balance velocity and stability"],
    ])},
    "cloud-computing-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Distributed tracing", "Follows a single request's path across many microservices to diagnose latency and errors"],
    ])},
    "cloud-computing-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Logging pipeline at scale", "Collects, processes, and stores logs from many cloud services centrally"],
    ])},
    "cloud-computing-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Cold start", "The extra latency incurred when a serverless function starts from an idle state"],
    ])},
    "cloud-computing-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Event-driven architecture", "Services communicate by publishing and reacting to events rather than direct calls"],
    ])},
    "cloud-computing-m1-l53": {"data_table": table(["Guarantee", "Feature"], [
        ["At-least-once delivery", "A message may be delivered more than once but never lost"],
        ["Exactly-once delivery", "A message is delivered and processed exactly one time"],
    ])},
    "cloud-computing-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Distributed caching", "Shares cached data across multiple servers to reduce database load"],
    ])},
    "cloud-computing-m1-l55": {"data_table": table(["Replication", "Feature"], [
        ["Synchronous", "Waits for confirmation from replicas before completing a write"],
        ["Asynchronous", "Completes a write immediately and replicates in the background"],
    ])},
    "cloud-computing-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tenant isolation", "Keeps different customers' data and workloads securely separated within shared infrastructure"],
    ])},
    "cloud-computing-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["API gateway pattern", "A single entry point that routes, authenticates, and rate-limits requests to backend services"],
    ])},
    "cloud-computing-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Rate limiting / throttling", "Restricts request volume to protect a service from overload or abuse"],
    ])},
    "cloud-computing-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Internal developer platform", "Provides self-service tooling that lets developers deploy without deep infra expertise"],
    ])},
    "cloud-computing-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Cost anomaly detection", "Automatically flags unexpected spikes in cloud spending"],
    ])},
    "cloud-computing-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Cloud carbon footprint", "Measures the environmental impact of running workloads on cloud infrastructure"],
    ])},
    "cloud-computing-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Batch processing", "Processes large volumes of data in scheduled jobs rather than continuously"],
    ])},
    "cloud-computing-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Hybrid cloud data sync", "Keeps data consistent between on-premises and cloud environments"],
    ])},
    "cloud-computing-m1-l64": {"data_table": table(["Metric", "Meaning"], [
        ["RTO", "How quickly a system must be restored after a disaster"],
        ["RPO", "How much data loss is acceptable, measured in time"],
    ])},
    "cloud-computing-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Immutable backup", "A backup that cannot be altered or deleted, protecting against ransomware"],
    ])},
    "cloud-computing-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Transit gateway", "Centrally connects multiple cloud networks and on-premises sites"],
    ])},
    "cloud-computing-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Software-defined networking", "Manages network behavior programmatically rather than via manual hardware configuration"],
    ])},
    "cloud-computing-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Container image scanning", "Checks container images for known vulnerabilities before deployment"],
    ])},
    "cloud-computing-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Admission control", "Validates or mutates Kubernetes resources before they are allowed into the cluster"],
    ])},
    "cloud-computing-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Secrets rotation", "Automatically replaces credentials periodically to limit exposure from leaks"],
    ])},
    "cloud-computing-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Data residency / sovereignty", "Ensures data is stored and processed within required legal jurisdictions"],
    ])},
    "cloud-computing-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Feature flag management", "Toggles features on or off in production without redeploying code"],
    ])},
    "cloud-computing-m1-l73": {"data_table": table(["Pattern", "Feature"], [
        ["Canary deployment", "Rolls out to a small subset of users first"],
        ["Blue-green deployment", "Switches all traffic between two identical environments"],
    ])},
    "cloud-computing-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Capacity planning", "Forecasts future infrastructure needs based on expected growth"],
    ])},
    "cloud-computing-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Distributed SQL database", "Provides relational guarantees while scaling horizontally across many nodes"],
    ])},
    "cloud-computing-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Object storage consistency", "Defines how quickly writes to cloud object storage become visible to readers"],
    ])},
    "cloud-computing-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Model serving architecture", "Deploys trained ML models to handle real-time or batch inference requests"],
    ])},
    "cloud-computing-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["GPU resource scheduling", "Allocates scarce GPU resources efficiently across competing cluster workloads"],
    ])},
    "cloud-computing-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Edge-to-cloud pipeline", "Moves data collected at the edge into central cloud storage and processing"],
    ])},
    "cloud-computing-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Cloud-native API versioning", "Manages backward-compatible evolution of APIs across microservices"],
    ])},
    "cloud-computing-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Policy as code", "Encodes governance rules as automatically enforced, version-controlled policy"],
    ])},
    "cloud-computing-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Landing zone", "A pre-configured, secure baseline environment for onboarding new cloud accounts"],
    ])},
    "cloud-computing-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Resource tagging", "Labels cloud resources for cost allocation and organizational tracking"],
    ])},
    "cloud-computing-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Secrets-as-a-service", "Provides secrets management as a shared, centrally governed cloud service"],
    ])},
    "cloud-computing-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Durable function workflow", "Orchestrates long-running, stateful serverless processes reliably"],
    ])},
    "cloud-computing-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Data pipeline cost optimization", "Reduces the compute and storage cost of running data pipelines"],
    ])},
    "cloud-computing-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Cloud-native search infrastructure", "Provides scalable, low-latency full-text search as a cloud service"],
    ])},
    "cloud-computing-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Multi-cloud abstraction layer", "Provides a common interface over multiple cloud providers, trading flexibility for complexity"],
    ])},
    "cloud-computing-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Anycast routing", "Routes a request to the nearest of many servers sharing the same IP address"],
    ])},
    "cloud-computing-m1-l90": {"data_table": table(["State", "Protection"], [
        ["At rest", "Encrypted while stored on disk"],
        ["In transit", "Encrypted while moving across the network"],
    ])},
    "cloud-computing-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Continuous control monitoring", "Automatically checks compliance controls are met on an ongoing basis"],
    ])},
    "cloud-computing-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Chaos testing for Kubernetes", "Deliberately disrupts cluster components to validate workload resilience"],
    ])},
    "cloud-computing-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Elastic compute scaling (warehouse)", "Automatically adjusts data warehouse compute to match query demand"],
    ])},
    "cloud-computing-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Correlating telemetry", "Links metrics, logs, and traces together to speed up incident diagnosis"],
    ])},
    "cloud-computing-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Vendor lock-in mitigation", "Reduces dependency on a single cloud provider's proprietary services"],
    ])},
    "cloud-computing-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Application portability", "Uses open standards so workloads can move between cloud environments easily"],
    ])},
    "cloud-computing-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Incident response runbook", "A documented, often automated, standard procedure for handling a specific incident type"],
    ])},
    "cloud-computing-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Data mesh implementation", "Puts data mesh principles into practice with concrete platform tooling"],
    ])},
    "cloud-computing-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Quantum computing service integration", "Connects classical cloud workloads to managed quantum computing resources"],
    ])},
    "cloud-computing-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["WebAssembly runtime (cloud)", "Runs portable, sandboxed WebAssembly modules as lightweight cloud workloads"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"cloud-computing-m1-l{base_n}"
    worked_key = f"cloud-computing-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cloud Computing"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Cloud Computing: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Cloud Computing lessons (completing 120/120).")


if __name__ == "__main__":
    main()
