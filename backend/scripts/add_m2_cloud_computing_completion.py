#!/usr/bin/env python3
"""Depth pass, M2 Cloud Computing: fill in real, hand-checked
data_table content for the M2 Cloud Computing lessons not covered by
the earlier breadth-first batch. Brings M2 Cloud Computing to full
120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
distributed consensus and consistency, serverless/container runtime
internals, Kubernetes and scheduling, cost optimization (FinOps),
multi-cloud/edge architecture, resilience patterns, cloud security and
governance, cloud-native data architecture, observability at scale,
and cloud ML infrastructure; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so it
is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_cloud_computing_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Byzantine fault tolerance", "A consensus protocol's ability to reach agreement despite arbitrarily faulty or malicious nodes"],
    ["Multi-tenant control plane", "The shared management layer coordinating resources across many cloud tenants, which must remain correct even under partial failures"],
])

CHARTS: dict[str, dict] = {
    "cloud-computing-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Cloud architecture design pattern", "A reusable, well-tested solution to a recurring problem in designing scalable cloud systems"],
        ["Application", "Patterns like circuit breaker and bulkhead provide proven approaches rather than reinventing solutions from scratch"],
    ])},
    "cloud-computing-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Cloud architecture capstone", "An applied culminating project demonstrating end-to-end cloud system design skill"],
        ["Deliverable", "Typically includes an architecture diagram, justified design trade-offs, and a working or simulated implementation"],
    ])},
    "cloud-computing-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Raft consensus", "A consensus protocol decomposing agreement into leader election, log replication, and safety, designed for understandability"],
        ["Geo-distributed optimization", "Tuning Raft's timeouts and quorum configuration for high-latency, geographically distributed metadata stores"],
    ])},
    "cloud-computing-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Active-active replication", "Multiple regions accept writes simultaneously rather than routing all writes through a single primary"],
        ["Conflict resolution", "Requires a strategy (e.g. last-write-wins, CRDTs) to reconcile concurrent conflicting writes across regions"],
    ])},
    "cloud-computing-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Vector clock", "A per-node counter vector that tracks causal (happens-before) ordering across a distributed system"],
        ["Causal consistency", "Guarantees that causally related operations are seen in the same order by every replica in distributed cloud storage"],
    ])},
    "cloud-computing-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Serverless cold start", "The latency penalty incurred when a platform must initialize a new execution environment for a function"],
        ["Predictive prewarming", "Uses traffic pattern forecasts to proactively initialize execution environments before requests arrive"],
    ])},
    "cloud-computing-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Function-as-a-Service", "A serverless compute model where individual functions run on demand without managing underlying servers"],
        ["Resource right-sizing", "Analyzes actual workload profiles to allocate the memory and CPU that best balance cost against performance"],
    ])},
    "cloud-computing-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["gVisor", "A container runtime that intercepts system calls through a userspace kernel to strengthen isolation between containers"],
        ["Kata Containers", "Runs each container inside a lightweight virtual machine, providing stronger isolation than standard container runtimes"],
    ])},
    "cloud-computing-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["eBPF", "A technology allowing sandboxed programs to run directly in the Linux kernel for high-performance monitoring and networking"],
        ["Kernel-level observability", "Enables tracing cloud workload behavior with minimal overhead, without modifying application code"],
    ])},
    "cloud-computing-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Sidecar proxy", "A separate process deployed alongside each service instance to handle networking concerns like routing and telemetry"],
        ["Performance overhead analysis", "Quantifies the added latency and resource cost a service mesh's sidecar introduces to each request"],
    ])},
    "cloud-computing-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Custom Resource Definition", "Extends the Kubernetes API with new, user-defined resource types"],
        ["Controller design pattern", "A controller watches CRD instances and drives cluster state toward the desired state they describe"],
    ])},
    "cloud-computing-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Kubernetes federation", "Coordinates and synchronizes resources across multiple independent Kubernetes clusters"],
        ["Global workload distribution", "Enables placing workloads across clusters in different regions for latency, redundancy, or compliance reasons"],
    ])},
    "cloud-computing-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Kubernetes scheduler extension", "Customizes how the scheduler ranks candidate nodes for a pod beyond the built-in defaults"],
        ["Custom scoring plugin", "Lets operators encode domain-specific placement preferences, such as cost or hardware affinity"],
    ])},
    "cloud-computing-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Bin-packing optimization", "Assigns workloads to servers to minimize the number of servers used while respecting resource constraints"],
        ["Cloud resource scheduling", "A classic combinatorial optimization problem underlying efficient multi-tenant cluster resource allocation"],
    ])},
    "cloud-computing-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Autoscaling policy", "Rules that automatically adjust the number of running instances based on observed load"],
        ["Control-theoretic feedback loop", "Applies formal control theory to design autoscaling that responds smoothly without oscillating or overshooting"],
    ])},
    "cloud-computing-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Predictive autoscaling", "Scales resources ahead of anticipated demand rather than reacting only after load has already increased"],
        ["Time series forecasting", "Uses historical demand patterns to forecast near-future load and provision capacity proactively"],
    ])},
    "cloud-computing-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Spot instance", "Discounted cloud compute capacity that can be reclaimed by the provider with short notice"],
        ["Interruption prediction", "Predicting likely reclamation lets fault-tolerant batch workloads checkpoint and migrate proactively"],
    ])},
    "cloud-computing-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Cost-aware workload placement", "Chooses which instance type and pricing model to run a workload on based on its cost-performance profile"],
        ["Heterogeneous instance types", "Different instance families offer different price-performance trade-offs suited to different workload characteristics"],
    ])},
    "cloud-computing-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["FinOps", "A discipline for managing cloud financial accountability across engineering, finance, and business teams"],
        ["Chargeback model", "Attributes shared cloud costs to individual teams, improving cost visibility and accountability"],
    ])},
    "cloud-computing-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Reserved instance", "A commitment to use cloud capacity for a fixed term in exchange for a substantial discount over on-demand pricing"],
        ["Portfolio optimization", "Balances upfront commitment against workload uncertainty to minimize total expected cloud spend"],
    ])},
    "cloud-computing-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Multi-cloud abstraction layer", "A software layer that presents a unified interface over multiple cloud providers' differing APIs"],
        ["Vendor-neutral deployment", "Reduces lock-in by letting applications be deployed to different providers with minimal code changes"],
    ])},
    "cloud-computing-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Anycast routing", "Routes a request to the topologically nearest of multiple servers sharing the same announced IP address"],
        ["Cross-cloud latency optimization", "Reduces round-trip latency by directing users to the closest available endpoint across providers"],
    ])},
    "cloud-computing-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["CDN cache invalidation", "Removes or refreshes stale cached content across a distributed content delivery network"],
        ["Strategy design", "Must balance invalidation speed against the overhead of propagating changes across many geographically distributed edge nodes"],
    ])},
    "cloud-computing-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Edge computing", "Moves computation closer to data sources to reduce latency and bandwidth use"],
        ["Latency-constrained placement", "Workload placement decisions must account for strict latency budgets that only nearby edge locations can satisfy"],
    ])},
    "cloud-computing-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Fog computing", "Extends cloud computing capabilities to intermediate layers between edge devices and the centralized cloud"],
        ["Hierarchical offloading", "Distributes compute across device, fog, and cloud tiers based on latency, bandwidth, and resource needs"],
    ])},
    "cloud-computing-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Distributed tracing", "Tracks a single request as it flows through multiple services, correlating spans into one coherent trace"],
        ["Sampling strategy", "Balances tracing overhead against observability completeness, since tracing every request is often too costly at scale"],
    ])},
    "cloud-computing-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Chaos engineering", "Deliberately injects failures into a production system to verify it degrades gracefully"],
        ["Resilience validation", "Validates assumptions about fault tolerance empirically rather than relying solely on design-time analysis"],
    ])},
    "cloud-computing-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Circuit breaker pattern", "Stops calling a failing downstream service temporarily, allowing it time to recover instead of overwhelming it further"],
        ["Cascading failure prevention", "Tuning the breaker's thresholds and timeouts prevents one service's failure from propagating through the whole system"],
    ])},
    "cloud-computing-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Bulkhead isolation pattern", "Partitions resources (e.g. thread pools) so failure or overload in one part cannot exhaust resources for others"],
        ["Multi-tenant protection", "Prevents one tenant's excessive resource usage from degrading service for other tenants sharing the same infrastructure"],
    ])},
    "cloud-computing-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Token bucket", "A rate-limiting algorithm allowing bursts up to a bucket capacity while enforcing a steady average rate"],
        ["Sliding window", "A rate-limiting algorithm counting requests within a continuously moving time window, offering smoother enforcement than fixed windows"],
    ])},
    "cloud-computing-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Distributed rate limiting", "Enforces a global rate limit consistently across multiple independent gateway instances"],
        ["Multi-region consistency", "Requires coordinating shared counters across regions, trading off consistency against latency"],
    ])},
    "cloud-computing-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Zero-trust network architecture", "Assumes no implicit trust based on network location; every access request is explicitly verified"],
        ["Cloud implementation", "Applies continuous identity, device, and context verification for every resource access in a cloud environment"],
    ])},
    "cloud-computing-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Workload identity federation", "Lets workloads authenticate to another cloud provider's services without long-lived static credentials"],
        ["Cross-cloud authentication", "Uses short-lived, dynamically issued tokens to reduce the risk of credential leakage across cloud boundaries"],
    ])},
    "cloud-computing-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Secrets management", "Securely stores, distributes, and controls access to sensitive credentials used by cloud-native applications"],
        ["Rotation strategy", "Periodically replaces secrets automatically to limit the window of exposure if a credential is compromised"],
    ])},
    "cloud-computing-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Confidential computing", "Protects data in use by performing computation within a hardware-isolated trusted execution environment"],
        ["Cloud application", "Lets cloud customers process sensitive data even in an environment where the cloud provider itself is not fully trusted"],
    ])},
    "cloud-computing-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Homomorphic encryption", "Allows computation directly on encrypted data, producing an encrypted result that decrypts to the correct answer"],
        ["Privacy-preserving cloud analytics", "Lets a cloud provider process customer data for analytics without ever seeing the data in plaintext"],
    ])},
    "cloud-computing-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Cloud security posture management", "Continuously scans cloud environments for misconfigurations that could create security risk"],
        ["Configuration auditing", "Automated, ongoing checks catch drift from secure baselines faster than periodic manual reviews"],
    ])},
    "cloud-computing-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Attribute-based access control", "Grants access based on evaluated attributes of the user, resource, and context, rather than fixed roles alone"],
        ["Cloud resource governance", "Enables more expressive and dynamic access policies than static role-based access control"],
    ])},
    "cloud-computing-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Software bill of materials", "A comprehensive inventory of components and dependencies included in deployed cloud software"],
        ["Supply chain security", "Enables quickly identifying which deployed cloud workloads are exposed when a vulnerability is disclosed in a component"],
    ])},
    "cloud-computing-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Immutable infrastructure", "Replaces servers with fresh instances built from a known-good image rather than modifying running servers in place"],
        ["Configuration drift prevention", "Eliminates the gradual, undocumented divergence that manual server changes cause over time"],
    ])},
    "cloud-computing-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["GitOps", "Uses a Git repository as the single source of truth for declarative infrastructure and application configuration"],
        ["Reconciliation loop", "A controller continuously compares actual cluster state against the Git-declared desired state and corrects any drift"],
    ])},
    "cloud-computing-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Infrastructure-as-code drift", "Occurs when the actual deployed infrastructure diverges from what the code defines"],
        ["Drift detection and remediation", "Automated tools periodically compare live state against code and can automatically correct unauthorized changes"],
    ])},
    "cloud-computing-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Policy-as-code", "Expresses governance rules as machine-readable code that can be automatically enforced and audited"],
        ["Cloud governance at scale", "Enables consistent policy enforcement across thousands of resources that manual review could not feasibly cover"],
    ])},
    "cloud-computing-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tenant SaaS", "A single application instance serves multiple independent customer organizations (tenants)"],
        ["Data isolation pattern", "Approaches range from separate databases per tenant to shared databases with strict row-level access controls"],
    ])},
    "cloud-computing-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Database sharding", "Partitions a dataset across multiple database nodes so each holds only a subset, enabling horizontal scale"],
        ["Horizontally scaled application", "Sharding strategy choice significantly affects both write throughput and the complexity of cross-shard queries"],
    ])},
    "cloud-computing-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Saga pattern", "Coordinates a sequence of local transactions across services, using compensating actions to undo partial failures"],
        ["Distributed transaction coordination", "Provides an alternative to distributed two-phase commit for maintaining consistency across cloud-native services"],
    ])},
    "cloud-computing-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Event sourcing", "Persists application state as an append-only sequence of events rather than just the current state"],
        ["CQRS", "Command Query Responsibility Segregation separates the models used for writing data from those used for reading it"],
    ])},
    "cloud-computing-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Idempotency key", "A unique identifier attached to a request so retrying it doesn't cause duplicate side effects"],
        ["Reliable distributed operation", "Critical for safely retrying requests over unreliable networks without causing duplicate charges or writes"],
    ])},
    "cloud-computing-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Backpressure", "A mechanism for a slow consumer to signal a fast producer to reduce its data rate, preventing overload"],
        ["Message queue handling", "Prevents a queue from growing unboundedly when downstream processing can't keep pace with incoming messages"],
    ])},
    "cloud-computing-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Exactly-once delivery semantics", "Guarantees each message affects the downstream system's state exactly once, even after failures and retries"],
        ["Distributed streaming platform", "Achieved via idempotent processing or transactional writes combined with durable checkpointing"],
    ])},
    "cloud-computing-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Recovery Point Objective (RPO)", "The maximum acceptable amount of data loss, measured in time, in a disaster recovery scenario"],
        ["Recovery Time Objective (RTO)", "The maximum acceptable time to restore service after a disaster"],
    ])},
    "cloud-computing-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Blue-green deployment", "Runs two identical production environments, switching traffic entirely from the old to the new version at once"],
        ["Canary deployment", "Gradually shifts a small percentage of traffic to a new version, monitoring for issues before a full rollout"],
    ])},
    "cloud-computing-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Feature flag", "A mechanism to toggle functionality on or off in production without a separate code deployment"],
        ["Progressive rollout architecture", "Gradual, monitored rollouts using feature flags reduce the blast radius of a problematic change"],
    ])},
    "cloud-computing-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["High-cardinality metric", "A metric with many possible unique label combinations, which strains naive time series storage systems"],
        ["Observability pipeline design", "Must be architected to efficiently ingest and query high-cardinality data at cloud scale"],
    ])},
    "cloud-computing-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Log aggregation", "Centralizes logs from many distributed sources into a searchable, unified system"],
        ["Petabyte-scale architecture", "Requires tiered storage and efficient indexing strategies to remain cost-effective and queryable at massive scale"],
    ])},
    "cloud-computing-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Unsupervised anomaly detection", "Identifies unusual patterns in telemetry data without requiring labeled examples of past anomalies"],
        ["Cloud infrastructure application", "Flags likely incidents in infrastructure metrics before they escalate into full outages"],
    ])},
    "cloud-computing-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Capacity planning", "Forecasts future resource needs to ensure sufficient infrastructure is provisioned ahead of demand"],
        ["Data center provisioning model", "Balances the cost of excess idle capacity against the risk of insufficient capacity during demand spikes"],
    ])},
    "cloud-computing-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Green cloud computing", "Aims to minimize the environmental impact of cloud infrastructure operation"],
        ["Carbon-aware scheduling", "Shifts flexible workloads to times or regions with lower-carbon electricity generation"],
    ])},
    "cloud-computing-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Power usage effectiveness", "A ratio measuring how much of a data center's total energy goes to computing equipment versus overhead like cooling"],
        ["Optimization strategy", "Improving PUE reduces both operational cost and environmental footprint for a given amount of computing"],
    ])},
    "cloud-computing-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Serverless orchestration", "Coordinates multi-step workflows composed of individual serverless function invocations"],
        ["State machine design", "Explicitly models a long-running workflow's steps and transitions, handling failures and retries at each stage"],
    ])},
    "cloud-computing-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Cold storage tiering", "Automatically moves infrequently accessed data to cheaper, higher-latency storage classes"],
        ["Cost-optimized policy", "Balances storage cost savings against the retrieval latency and cost penalty of accessing cold data"],
    ])},
    "cloud-computing-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Erasure coding", "Encodes data into fragments with redundancy so the original can be reconstructed from a subset of fragments"],
        ["Replication trade-off", "Erasure coding uses less storage overhead than full replication for the same fault tolerance, at the cost of more complex reconstruction"],
    ])},
    "cloud-computing-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Consistent hashing", "Maps both data and nodes onto a hash ring so adding or removing a node remaps only a small fraction of keys"],
        ["Distributed cache load balancing", "Minimizes cache misses caused by node changes compared with naive modulo-based hashing"],
    ])},
    "cloud-computing-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Distributed lock service", "Coordinates mutually exclusive access to a shared resource across multiple nodes in a cluster"],
        ["Cloud-native coordination", "Underpins safe leader election and configuration management in distributed cloud systems"],
    ])},
    "cloud-computing-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Leader election algorithm", "Selects a single coordinating node among a group, with automatic failover if the leader fails"],
        ["Fault-tolerant coordination", "Ensures cluster coordination continues correctly even as individual nodes join, leave, or fail"],
    ])},
    "cloud-computing-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["CAP theorem", "A distributed system can guarantee at most two of consistency, availability, and partition tolerance simultaneously"],
        ["Cloud system trade-off", "Since network partitions are unavoidable at scale, cloud systems must explicitly choose between consistency and availability during a partition"],
    ])},
    "cloud-computing-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Quorum-based consistency", "Requires a minimum number of replicas to agree on a read or write for it to succeed"],
        ["Tuning", "Adjusting read and write quorum sizes trades off consistency strength, availability, and latency"],
    ])},
    "cloud-computing-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["gRPC load balancing", "Distributes RPC calls across multiple service instances, complicated by gRPC's use of long-lived HTTP/2 connections"],
        ["High-throughput strategy", "Client-side or proxy-based load balancing approaches address the connection-multiplexing challenges specific to gRPC"],
    ])},
    "cloud-computing-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["API gateway", "A single entry point that routes requests to backend services while handling cross-cutting concerns centrally"],
        ["Cross-cutting concern centralization", "Handles authentication, rate limiting, and logging once at the gateway rather than duplicating them in each service"],
    ])},
    "cloud-computing-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Service discovery", "Enables services to dynamically find the network location of other services in a changing environment"],
        ["Dynamic cloud environment", "Essential when instances are frequently created and destroyed by autoscaling and deployments"],
    ])},
    "cloud-computing-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Distributed cache coherence", "Ensures multiple cache copies remain consistent as underlying data changes"],
        ["Multi-region deployment", "Coherence protocols must account for higher latency between geographically distributed cache nodes"],
    ])},
    "cloud-computing-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["CI/CD pipeline security", "Protects the automated build and deployment process from being used to introduce malicious code"],
        ["Supply chain attack hardening", "Includes verifying dependencies, signing artifacts, and restricting pipeline permissions"],
    ])},
    "cloud-computing-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Ephemeral build environment", "A fresh, isolated environment created for each build and destroyed afterward"],
        ["Reproducible deployment", "Prevents state from one build from contaminating or influencing subsequent builds"],
    ])},
    "cloud-computing-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Container image layer optimization", "Structures a container image's layers to minimize size and maximize cache reuse across builds"],
        ["Cold start footprint reduction", "Smaller, well-ordered image layers reduce the time needed to pull and start a new container instance"],
    ])},
    "cloud-computing-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["WebAssembly runtime", "A portable, sandboxed execution environment that can run compiled code with near-native performance"],
        ["Lightweight cloud function execution", "Offers faster startup times than traditional containers for certain serverless workloads"],
    ])},
    "cloud-computing-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Noisy neighbor", "A tenant whose heavy resource usage degrades performance for other tenants sharing the same underlying infrastructure"],
        ["Resource quota enforcement", "Sets hard limits on each tenant's resource consumption to prevent noisy-neighbor effects"],
    ])},
    "cloud-computing-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Read replica lag", "The delay between a write to a primary database and its propagation to a read replica"],
        ["Consistency guarantee", "Applications reading from replicas must account for potentially stale data due to replication lag"],
    ])},
    "cloud-computing-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Distributed rate-limited job queue", "Enforces fair resource consumption limits per tenant while processing jobs across a distributed worker pool"],
        ["Fair multi-tenant scheduling", "Prevents any single tenant's job volume from starving other tenants of processing capacity"],
    ])},
    "cloud-computing-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Network function virtualization", "Replaces dedicated network hardware appliances with software running on standard servers"],
        ["Performance benchmarking", "Measures whether virtualized network functions can match the throughput and latency of dedicated hardware"],
    ])},
    "cloud-computing-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Software-defined networking control plane", "The centralized logic making network routing decisions, separate from the data plane that forwards packets"],
        ["Scalability analysis", "Studies how much traffic and how many devices a centralized SDN controller can manage before becoming a bottleneck"],
    ])},
    "cloud-computing-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Network overlay protocol", "Creates a virtual network layer on top of existing physical infrastructure"],
        ["Multi-cluster Kubernetes networking", "Enables pods in different clusters to communicate as if on the same flat network"],
    ])},
    "cloud-computing-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Cloud cost anomaly detection", "Identifies unexpected spikes or patterns in cloud spending that may indicate misconfiguration or abuse"],
        ["Statistical time series model", "Flags spend that deviates significantly from the expected pattern predicted by historical billing data"],
    ])},
    "cloud-computing-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Right-sizing recommendation", "Suggests a more cost-appropriate instance size based on actual observed resource utilization"],
        ["Historical utilization analysis", "Statistical analysis of past usage patterns identifies consistently over-provisioned or under-provisioned resources"],
    ])},
    "cloud-computing-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Kubernetes admission controller", "Intercepts API requests to validate or mutate them before they are persisted to the cluster"],
        ["Automated policy enforcement", "Enforces organizational policies (e.g. required labels, resource limits) automatically at the point of resource creation"],
    ])},
    "cloud-computing-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Multi-cluster service mesh federation", "Extends service mesh capabilities to manage traffic consistently across multiple Kubernetes clusters"],
        ["Cross-cluster traffic management", "Enables unified routing, security, and observability policies spanning clusters, not just within a single cluster"],
    ])},
    "cloud-computing-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Progressive delivery", "Gradually rolls out a change while continuously monitoring key metrics to detect problems early"],
        ["Metrics-driven rollback automation", "Automatically halts or reverts a rollout when monitored metrics cross a defined unhealthy threshold"],
    ])},
    "cloud-computing-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Encryption at rest", "Protects stored data by encrypting it while it resides on disk or in a database"],
        ["Key management architecture", "Securely generates, stores, rotates, and controls access to the cryptographic keys used for encryption"],
    ])},
    "cloud-computing-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Clock synchronization", "Keeps timestamps consistent across distributed nodes despite inherent clock drift"],
        ["TrueTime-style architecture", "Uses specialized hardware (GPS/atomic clocks) to bound clock uncertainty, enabling stronger global consistency guarantees"],
    ])},
    "cloud-computing-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Connection pooling", "Reuses a limited set of database connections across many requests rather than opening a new one each time"],
        ["Serverless architecture challenge", "Serverless functions' rapid scaling can exhaust database connection limits without careful pooling design"],
    ])},
    "cloud-computing-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Cloud migration strategy", "A plan for moving an application from on-premises or legacy infrastructure to the cloud"],
        ["Legacy application modernization", "Approaches range from a simple lift-and-shift to a full re-architecture for cloud-native patterns"],
    ])},
    "cloud-computing-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Hybrid cloud bursting", "Temporarily offloads workload spikes from on-premises infrastructure to the public cloud"],
        ["Capacity overflow architecture", "Provides elastic capacity for peak demand without requiring permanent over-provisioning of on-premises hardware"],
    ])},
    "cloud-computing-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Data gravity", "The tendency for applications and services to be pulled toward the location where their data already resides"],
        ["Multi-cloud architecture consideration", "Moving large datasets between clouds can be costly and slow, influencing where compute should be placed"],
    ])},
    "cloud-computing-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["API rate contract", "A formal agreement specifying the request rate a service commits to supporting for a consumer"],
        ["SLA-backed consumption", "Provides consumers a predictable, contractually guaranteed level of API access"],
    ])},
    "cloud-computing-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Distributed batch job scheduling", "Coordinates the execution of many interdependent batch processing jobs across a cluster"],
        ["Dependency graph resolution", "Ensures jobs run only after their prerequisite jobs have successfully completed"],
    ])},
    "cloud-computing-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Model serving infrastructure", "Deploys trained machine learning models so they can respond to real-time prediction requests"],
        ["Cloud-native design", "Must handle autoscaling, versioning, and latency requirements distinct from typical stateless web services"],
    ])},
    "cloud-computing-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["GPU resource sharing", "Allows multiple workloads to share a single GPU rather than each requiring a dedicated one"],
        ["Fractional allocation", "Divides a GPU's compute and memory among multiple smaller ML workloads to improve overall utilization"],
    ])},
    "cloud-computing-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Cloud compliance automation", "Continuously and automatically verifies that cloud resources meet required regulatory controls"],
        ["Continuous attestation", "Replaces periodic manual audits with ongoing automated evidence collection for compliance reporting"],
    ])},
    "cloud-computing-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Failure domain isolation", "Structures infrastructure so a failure in one region or availability zone doesn't cascade to others"],
        ["Region and availability zone design", "Deploying redundantly across independent failure domains is fundamental to high-availability cloud architecture"],
    ])},
    "cloud-computing-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Thesis-level capstone", "A culminating project requiring original design of a fault-tolerant distributed cloud platform"],
        ["Fault-tolerant platform design", "Requires integrating consensus, replication, and failure-isolation principles into one coherent system design"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cloud Computing"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"cloud-computing-m2-l{base_n}"
        worked_key = f"cloud-computing-m2-l{worked_n}"
        if base_n == 3:
            CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
        elif base_key in CHARTS:
            CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Missing lesson ids: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson or lesson[key] is None:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Cloud Computing lessons.")


if __name__ == "__main__":
    main()
