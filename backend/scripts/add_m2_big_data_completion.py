#!/usr/bin/env python3
"""Depth pass, M2 Big Data: fill in real, hand-checked data_table
content for the M2 Big Data lessons not covered by the earlier
breadth-first batch. Brings M2 Big Data to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning streaming
architecture (Lambda/Kappa, exactly-once semantics, watermarking),
data lakehouse and table formats, distributed query processing and
optimization, data governance/quality/security at scale, distributed
systems foundations applied to data platforms (consensus, CAP theorem,
consistency models), data mesh architecture, and cost/capacity
engineering for petabyte-scale systems.

Offset quirk (same pattern as M2 Machine Learning): l101 is a
standalone lesson ("Streaming SQL Semantics and Continuous Query
Languages") with no l1-l20 counterpart, and l102-l120 are "Worked
Analysis" companions reusing the data_table of l1-l19 with a shifted
1:1 mapping (base_n = worked_n - 101, valid for worked_n 102-120). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it maps to l104).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_big_data_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Lambda architecture", "Combines a batch layer for accuracy with a speed layer for low-latency approximate results, later reconciled"],
    ["Kappa architecture", "Simplifies lambda architecture by processing all data, batch and real-time, through a single stream-processing pipeline"],
])

CHARTS: dict[str, dict] = {
    "big-data-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Big data architecture design", "The overall structure and technology choices for systems handling data at massive volume, velocity, and variety"],
        ["Application", "Balances trade-offs among throughput, latency, cost, and consistency across the entire data platform"],
    ])},
    "big-data-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Big data capstone", "An applied culminating project demonstrating end-to-end big data system design and implementation skill"],
        ["Deliverable", "Typically includes a working pipeline or platform component with justified architectural trade-offs"],
    ])},
    "big-data-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Exactly-once semantics", "Guarantees each record affects the output state exactly once, even after failures and restarts"],
        ["Distributed stream processing", "Achieved via idempotent writes or transactional commits combined with durable checkpointing of processing state"],
    ])},
    "big-data-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Watermarking", "A timestamp indicating that no more events with an earlier event-time are expected to arrive"],
        ["Event-time processing", "Enables correctly handling out-of-order events while still eventually producing timely, complete windowed results"],
    ])},
    "big-data-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Data mesh", "A decentralized data architecture where domain teams own and serve their own data products"],
        ["Domain-oriented ownership", "Contrasts with a single centralized data team owning all pipelines, aiming to improve scalability and accountability"],
    ])},
    "big-data-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Data lakehouse table format", "Adds transactional guarantees and schema management on top of files stored in a data lake"],
        ["Delta Lake, Iceberg, Hudi", "Three leading open table formats, differing in approach to metadata management, concurrency control, and ecosystem integration"],
    ])},
    "big-data-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Consistency model", "Defines what guarantees a distributed system makes about the order and visibility of data updates"],
        ["Distributed data store application", "Choosing an appropriate consistency model balances correctness guarantees against latency and availability"],
    ])},
    "big-data-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["CAP theorem", "A distributed system can guarantee at most two of consistency, availability, and partition tolerance simultaneously"],
        ["Large-scale system design implication", "Since network partitions are unavoidable at scale, systems must explicitly choose between consistency and availability during a partition"],
    ])},
    "big-data-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Distributed query optimization", "Chooses an efficient execution plan for a query spanning multiple, possibly heterogeneous data sources"],
        ["Federated data source application", "Must account for network cost and each source's differing query capabilities when planning a federated query"],
    ])},
    "big-data-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Approximate query processing", "Returns a statistically bounded approximate answer to a query far faster than computing the exact result"],
        ["Sketching algorithm", "Compact probabilistic data structures (like HyperLogLog) enable fast approximate aggregate queries over massive datasets"],
    ])},
    "big-data-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Pregel model", "A vertex-centric graph processing model where computation proceeds in synchronized supersteps of message passing"],
        ["GraphX", "A graph processing framework built on Spark's RDD abstraction, integrating graph and dataflow-style computation"],
    ])},
    "big-data-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Data skew", "An uneven distribution of data across partitions, causing some workers to handle disproportionately more work"],
        ["Distributed join mitigation", "Techniques like salting and adaptive skew join handling redistribute skewed keys to balance load across workers"],
    ])},
    "big-data-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Columnar storage format", "Stores each column contiguously rather than each row, improving compression and scan performance for analytical queries"],
        ["Predicate pushdown", "Filters data as early as possible, often at the storage layer, avoiding unnecessary reads of irrelevant rows"],
    ])},
    "big-data-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Change data capture", "Detects and streams changes made to a source database in near real time"],
        ["Real-time data integration", "Enables downstream systems to stay synchronized with operational data as it changes, without costly full re-extraction"],
    ])},
    "big-data-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Data quality framework", "A structured set of automated checks ensuring data flowing through a pipeline meets defined quality standards"],
        ["Automated pipeline validation", "Catches data quality issues early, before they propagate downstream to dependent systems and reports"],
    ])},
    "big-data-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Schema evolution", "Allows a data schema to change over time as requirements evolve"],
        ["Backward compatibility", "Ensures consumers using an older schema version can still correctly read data written under a newer schema"],
    ])},
    "big-data-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Data governance framework", "Formal policies and processes ensuring data is managed consistently, securely, and in compliance with regulations"],
        ["Large-scale metadata management", "Requires systematic cataloging of data assets to make governance policies enforceable across a large organization"],
    ])},
    "big-data-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tenant resource isolation", "Ensures one tenant's workload cannot degrade performance or access data for other tenants sharing the same cluster"],
        ["Shared big data cluster", "Requires resource quotas and scheduling policies to prevent noisy-neighbor effects across tenants"],
    ])},
    "big-data-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Cost-based query optimization", "Chooses among equivalent query execution plans by estimating and comparing their execution cost"],
        ["Massively parallel processing engine", "Must account for data distribution and network shuffle cost across many nodes when estimating plan cost"],
    ])},
    "big-data-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Vectorized query execution", "Processes batches of column values together using SIMD instructions, rather than one row at a time"],
        ["SIMD acceleration", "Exploits CPU-level parallelism to dramatically speed up analytical query processing compared with row-at-a-time execution"],
    ])},
    "big-data-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Data lineage tracking", "Records the origin and transformation history of data as it moves through a pipeline"],
        ["Regulatory compliance at scale", "Enables demonstrating to regulators exactly how a reported number was derived from source data across a large data platform"],
    ])},
    "big-data-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Two-phase commit", "A distributed transaction protocol ensuring all participants either commit or abort together, using a coordinator"],
        ["Saga pattern", "Coordinates a sequence of local transactions with compensating actions, avoiding two-phase commit's blocking coordinator dependency"],
    ])},
    "big-data-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Serverless data processing", "Runs data processing jobs on auto-scaling, pay-per-use infrastructure without managing dedicated servers"],
        ["Cost and performance modeling", "Requires modeling how job characteristics translate into serverless billing, which differs from traditional fixed-cluster economics"],
    ])},
    "big-data-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Data deduplication", "Identifies and removes or merges duplicate records within a dataset"],
        ["Petabyte-scale algorithm", "Requires efficient approximate matching techniques since exact pairwise comparison is infeasible at this scale"],
    ])},
    "big-data-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive query execution", "Adjusts a query's execution plan at runtime based on actual observed data statistics, rather than only initial estimates"],
        ["Modern distributed engine", "Corrects for cost-estimation errors that a purely static, plan-time optimizer would carry through the entire query execution"],
    ])},
    "big-data-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Multi-model database", "Supports multiple data models (document, graph, key-value) within a single database system"],
        ["Polyglot persistence", "Uses different specialized data stores for different parts of an application based on each data type's access patterns"],
    ])},
    "big-data-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Time-series database", "Optimized for storing and querying data indexed by timestamp, such as metrics"],
        ["High-cardinality metric design", "Must efficiently handle metrics with many unique label combinations, which strain naive time series storage"],
    ])},
    "big-data-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Data partitioning", "Divides a large dataset into smaller, more manageable segments distributed across storage nodes"],
        ["Petabyte-scale warehouse strategy", "Partition key choice significantly affects both query performance and data skew across the distributed warehouse"],
    ])},
    "big-data-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Streaming machine learning", "Trains or updates a machine learning model incrementally as new data arrives, rather than in periodic batch retraining"],
        ["Online model update at scale", "Requires careful design to update model parameters efficiently without reprocessing the full historical dataset"],
    ])},
    "big-data-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Feature store", "A centralized system for storing, versioning, and serving machine learning features consistently across training and serving"],
        ["Large-scale ML pipeline application", "Prevents training-serving skew by ensuring the same feature computation logic is used in both contexts"],
    ])},
    "big-data-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Data observability", "Monitors the health of data pipelines, tracking signals like freshness, volume, and schema"],
        ["Schema drift monitoring", "Detects unexpected schema changes that could silently break downstream consumers if left unmonitored"],
    ])},
    "big-data-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Raft", "A consensus protocol decomposing agreement into leader election, log replication, and safety, designed for understandability"],
        ["Paxos (data systems)", "An earlier, more theoretically foundational consensus protocol underlying many production data systems' replication logic"],
    ])},
    "big-data-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Bloom filter", "A space-efficient probabilistic structure testing set membership with possible false positives but no false negatives"],
        ["Variant for large-scale testing", "Structures like Cuckoo filters and counting Bloom filters extend the basic idea with deletion support or frequency counting"],
    ])},
    "big-data-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Cloud-native data warehouse cost optimization", "Strategies for minimizing spend on elastic, usage-based cloud data warehouse platforms"],
        ["Strategy", "Includes right-sizing compute, optimizing storage tiering, and reducing unnecessary query scan volume"],
    ])},
    "big-data-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Privacy-preserving aggregation", "Computes aggregate statistics across data while limiting exposure of any individual record"],
        ["Scale technique", "Combines techniques like differential privacy or secure aggregation with distributed computation frameworks"],
    ])},
    "big-data-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Real-time anomaly detection", "Identifies unusual patterns in data as it arrives, without waiting for batch processing"],
        ["High-velocity stream application", "Must balance detection accuracy against the strict low-latency requirements of streaming data"],
    ])},
    "big-data-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Distributed hash table", "A decentralized key-value store where each node is responsible for a portion of the keyspace"],
        ["Scalable key-value storage design", "Enables horizontally scaling storage capacity and throughput by adding more nodes to the ring"],
    ])},
    "big-data-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Data replication (geo-distributed)", "Maintains copies of data across geographically distributed locations"],
        ["Strategy", "Balances latency benefits of local reads/writes against the complexity of maintaining consistency across regions"],
    ])},
    "big-data-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Workload-aware auto-scaling", "Adjusts cluster capacity based on observed or predicted characteristics of the current data processing workload"],
        ["Elastic cluster application", "More sophisticated than simple threshold-based scaling, anticipating resource needs from workload patterns"],
    ])},
    "big-data-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Data compression algorithm", "Reduces the storage size of data by encoding it more efficiently"],
        ["Analytical workload trade-off", "Balances compression ratio against decompression speed, which affects analytical query performance"],
    ])},
    "big-data-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Materialized view", "A precomputed query result stored for fast subsequent access, rather than recomputed on each request"],
        ["Maintenance (large-scale analytics)", "Must efficiently update the materialized view as underlying data changes, without full recomputation"],
    ])},
    "big-data-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Query result caching", "Stores the results of previously executed queries for reuse by identical or similar future queries"],
        ["Distributed analytics platform strategy", "Must handle cache invalidation correctly as underlying data changes to avoid serving stale results"],
    ])},
    "big-data-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Fine-grained access control", "Restricts data access at a granular level, such as specific rows, columns, or cells"],
        ["Big data security at scale", "Must enforce these policies efficiently even as query volume and data size grow substantially"],
    ])},
    "big-data-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["DAG scheduling", "Orders and executes data pipeline tasks according to their dependency structure, represented as a directed acyclic graph"],
        ["Enterprise-scale orchestration", "Must efficiently schedule and monitor potentially thousands of interdependent pipeline tasks across an organization"],
    ])},
    "big-data-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Vector database indexing", "Structures for efficiently finding similar high-dimensional vectors, such as embeddings"],
        ["Large-scale similarity search", "Index structures like HNSW enable sub-linear search over billions of vectors, essential at big data scale"],
    ])},
    "big-data-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Multi-cloud data architecture", "Distributes data infrastructure across multiple cloud providers rather than relying on a single vendor"],
        ["Portability challenge", "Must address differing native services and data formats across providers to enable genuine workload portability"],
    ])},
    "big-data-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Distributed sorting algorithm", "Sorts data too large to fit on a single machine by coordinating the sort across many nodes"],
        ["Massive dataset application", "Requires careful partitioning and merging strategies to achieve a globally sorted result efficiently"],
    ])},
    "big-data-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Data archival", "Moves infrequently accessed data to lower-cost, longer-term storage"],
        ["Cold storage tiering strategy", "Balances storage cost savings against the retrieval latency and cost penalty of accessing archived data"],
    ])},
    "big-data-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Real-time join processing", "Combines data from multiple streams as events arrive, without waiting for batch processing"],
        ["Streaming analytics engine application", "Must manage state efficiently to match related events arriving at different times across streams"],
    ])},
    "big-data-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["TPC-DS", "A standardized decision-support benchmark used to evaluate big data analytical system performance"],
        ["Benchmark design", "Well-designed benchmarks must represent realistic query patterns and data distributions to yield meaningful comparisons"],
    ])},
    "big-data-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Data mesh interoperability standard", "Common conventions enabling data products from different domain teams to be discovered and combined consistently"],
        ["Cross-domain application", "Without shared standards, a decentralized data mesh risks fragmenting into incompatible domain-specific silos"],
    ])},
    "big-data-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Explainable data lineage", "Presents a data lineage trace in a way that's understandable and actionable for auditors, not just raw technical logs"],
        ["ML model auditing application", "Helps trace exactly which upstream data influenced a specific machine learning model's training and predictions"],
    ])},
    "big-data-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Parameter server", "A distributed architecture where worker nodes compute gradients and a central server aggregates and updates shared model parameters"],
        ["Distributed ML application", "Enables training models too large or with too much data to fit on a single machine"],
    ])},
    "big-data-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Skew-aware load balancing", "Dynamically redistributes work to compensate for uneven data distribution across stream processing partitions"],
        ["Distributed stream processing application", "Prevents a small number of overloaded partitions from becoming a bottleneck for the entire streaming pipeline"],
    ])},
    "big-data-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tenancy cost attribution", "Accurately assigns shared infrastructure costs to individual tenants based on their actual resource consumption"],
        ["Shared data platform model", "Enables fair chargeback and improves cost visibility across teams sharing the same underlying platform"],
    ])},
    "big-data-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Data virtualization", "Provides a unified query interface over multiple underlying data sources without physically consolidating the data"],
        ["Unified query access layer", "Lets users query across heterogeneous sources as if they were a single logical database"],
    ])},
    "big-data-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Entity resolution", "Identifies records across different datasets that likely refer to the same real-world entity"],
        ["Scalable record linkage technique", "Must efficiently match records across billions of entries, well beyond naive pairwise comparison"],
    ])},
    "big-data-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Graph database query optimization", "Chooses efficient traversal strategies for queries over graph-structured data"],
        ["Billion-edge network application", "Query planning for graphs differs fundamentally from relational join optimization at this scale"],
    ])},
    "big-data-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Data contract", "A formal agreement specifying the expected schema and semantics of data exchanged between a producer and consumer"],
        ["Enforcement", "Automated contract checks prevent producer changes from silently breaking downstream consumer pipelines"],
    ])},
    "big-data-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Real-time feature engineering", "Computes machine learning features from data as it streams in, rather than in periodic batch jobs"],
        ["Streaming ML pipeline application", "Enables models to use the freshest possible feature values for time-sensitive predictions"],
    ])},
    "big-data-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Distributed snapshot algorithm", "Captures a consistent global state of a distributed system despite ongoing concurrent activity"],
        ["Consistent state checkpointing", "Enables reliably resuming a distributed computation from a known-good state after a failure"],
    ])},
    "big-data-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["GDPR right-to-erasure", "A regulatory requirement that individuals can request deletion of their personal data"],
        ["Big data scale compliance", "Efficiently locating and deleting all copies of a specific individual's data across a large, distributed data platform is a significant engineering challenge"],
    ])},
    "big-data-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Cost-aware query planning", "Considers the differing cost of accessing data stored on different storage tiers when planning a query"],
        ["Heterogeneous storage tier application", "Balances query performance against the cost implications of accessing data on hot versus cold storage tiers"],
    ])},
    "big-data-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Distributed rate limiting", "Enforces a consistent overall rate limit across multiple distributed ingestion endpoints"],
        ["High-throughput ingestion application", "Prevents any single high-volume source from overwhelming shared downstream processing capacity"],
    ])},
    "big-data-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Data product", "Treats a well-defined, discoverable dataset as a product with clear ownership, quality guarantees, and documentation"],
        ["Productization in data mesh", "Central to data mesh's philosophy of domain teams delivering data as a first-class product, not a byproduct"],
    ])},
    "big-data-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic big data generation", "Creates artificial datasets that mimic real data's statistical and volume characteristics"],
        ["Pipeline load testing application", "Enables realistic performance testing of a data pipeline without needing access to actual sensitive production data"],
    ])},
    "big-data-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Multi-version concurrency control", "Maintains multiple versions of data so readers can access a consistent snapshot without blocking concurrent writers"],
        ["Distributed analytical database application", "Enables long-running analytical queries to see a consistent view of data despite concurrent writes"],
    ])},
    "big-data-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive compression codec selection", "Automatically chooses the most appropriate compression algorithm based on the specific data's characteristics"],
        ["Mixed analytical workload application", "No single codec is optimal for all data types, so adaptive selection improves overall storage efficiency"],
    ])},
    "big-data-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Data sovereignty", "Legal requirements that data about a country's citizens be stored and processed within that country's borders"],
        ["Cross-border transfer architecture", "Requires careful data platform design to comply with varying, sometimes conflicting, national data residency laws"],
    ])},
    "big-data-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Tumbling window", "Fixed-size, non-overlapping time windows used to aggregate streaming data"],
        ["Sliding and session windows", "Sliding windows overlap at a fixed step; session windows group events based on periods of inactivity rather than fixed time"],
    ])},
    "big-data-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Distributed caching layer", "A shared, distributed cache accelerating repeated data access across a cluster"],
        ["High-throughput analytics design", "Reduces load on the underlying data store by serving frequently accessed data directly from a faster cache tier"],
    ])},
    "big-data-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Data pipeline testing", "Verifies a data pipeline's correctness at unit, integration, and system levels"],
        ["Chaos testing", "Deliberately injects failures into a pipeline to verify it degrades gracefully and recovers correctly"],
    ])},
    "big-data-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Automated data quality anomaly alert", "Automatically flags data that deviates from expected quality patterns"],
        ["Explainability", "Providing a clear explanation for why an alert fired helps analysts quickly triage true issues from false positives"],
    ])},
    "big-data-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Data egress cost modeling", "Estimates the cost of transferring data out of a cloud provider's network"],
        ["Petabyte-scale multi-cloud application", "Egress costs can become a dominant expense at scale, significantly shaping multi-cloud architecture decisions"],
    ])},
    "big-data-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Streaming lookup join", "Enriches streaming events by joining them against a reference dataset in real time"],
        ["Real-time data enrichment application", "Must balance lookup latency against the freshness and completeness of the reference data being joined"],
    ])},
    "big-data-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Data pipeline bottleneck analysis", "Identifies which stage of a data pipeline limits overall throughput"],
        ["Distributed deep learning training application", "Data loading is a common bottleneck that can leave expensive GPU compute idle if not properly optimized"],
    ])},
    "big-data-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Encryption at rest", "Protects stored data by encrypting it while it resides on disk"],
        ["Encryption in transit trade-off", "Both add computational overhead, requiring performance trade-off analysis at big data scale"],
    ])},
    "big-data-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Metadata catalog", "A searchable inventory of an organization's data assets, including schema, ownership, and lineage information"],
        ["Enterprise data discovery design", "Enables users to find and understand relevant datasets across a large, otherwise opaque data platform"],
    ])},
    "big-data-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Backpressure", "A mechanism for a slow consumer to signal a fast producer to reduce its data rate, preventing overload"],
        ["Streaming architecture handling", "Prevents unbounded memory growth when downstream processing can't keep pace with incoming data"],
    ])},
    "big-data-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Hybrid transactional-analytical processing", "A system design supporting both transactional (OLTP) and analytical (OLAP) workloads on the same data without separate ETL"],
        ["System design", "Eliminates the latency and complexity of maintaining separate transactional and analytical copies of data"],
    ])},
    "big-data-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Cross-region data consistency", "Maintains consistent data views for applications operating across geographically distributed regions"],
        ["Globally distributed application design", "Must balance strong consistency guarantees against the latency cost of coordinating across distant regions"],
    ])},
    "big-data-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Automated data pipeline cost anomaly detection", "Flags unexpected spikes in the cost of running a data pipeline"],
        ["Application", "Helps catch inefficient queries or misconfigurations before they accumulate into significant unexpected spend"],
    ])},
    "big-data-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Data lakehouse governance", "Applies access control and policy enforcement to data stored in a lakehouse architecture"],
        ["Fine-grained table access policy", "Enables restricting access at the row, column, or cell level within lakehouse tables, not just entire datasets"],
    ])},
    "big-data-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Exactly-once sink connector", "Ensures streaming output written to an external system is delivered exactly once, even after failures"],
        ["External system application", "Requires coordinating the streaming engine's checkpointing with the target system's transactional or idempotency guarantees"],
    ])},
    "big-data-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Queueing theory", "Mathematical study of waiting lines, modeling arrival rates, service rates, and resulting wait times"],
        ["Capacity planning application", "Uses queueing models to determine the infrastructure capacity needed to keep processing latency within target service levels"],
    ])},
    "big-data-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Distributed tracing", "Tracks a single request or record as it flows through multiple pipeline stages, correlating spans into one coherent trace"],
        ["Multi-stage pipeline debugging application", "Enables diagnosing latency and error sources across complex, multi-stage data pipelines"],
    ])},
    "big-data-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Idempotency (data pipeline)", "The property that reprocessing the same data multiple times produces the same final result as processing it once"],
        ["Design pattern", "Critical for safely retrying failed pipeline stages without causing duplicate or inconsistent downstream effects"],
    ])},
    "big-data-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Scalable A/B testing infrastructure", "Systems reliably running and analyzing many concurrent controlled experiments at big data scale"],
        ["Big data platform application", "Must handle consistent user bucketing and statistical analysis across enormous volumes of experiment data"],
    ])},
    "big-data-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Column-level data masking", "Obscures sensitive data values in specific columns while preserving the data's overall usability"],
        ["Sensitive field protection at scale", "Must apply masking policies consistently and efficiently across enormous datasets and many downstream consumers"],
    ])},
    "big-data-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Query federation", "Executes a single logical query across multiple, separately located data sources"],
        ["Cloud and on-premises performance", "Must account for the significant latency difference between querying cloud-native versus on-premises data sources"],
    ])},
    "big-data-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Pipeline dependency graph optimization", "Restructures a data pipeline's task dependencies to minimize overall end-to-end latency"],
        ["Reduced latency application", "Identifies opportunities for increased parallelism or eliminated unnecessary sequential dependencies"],
    ])},
    "big-data-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Real-time data deduplication", "Identifies and removes duplicate events as they arrive in a streaming pipeline"],
        ["Event-driven architecture application", "Must deduplicate efficiently within the constraints of limited streaming state and processing time"],
    ])},
    "big-data-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Bias propagation", "How biases present in source data can be amplified or compounded as data flows through aggregation and processing stages"],
        ["Large-scale aggregation ethics", "A significant concern since big data aggregation can systematically obscure or worsen biases present in underlying source data"],
    ])},
    "big-data-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Time-travel query", "Queries a table's data as it existed at a specific point in the past, not just its current state"],
        ["Table format storage support", "Modern lakehouse table formats natively support this by retaining historical snapshots of table versions"],
    ])},
    "big-data-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Distributed query engine fault tolerance", "Ensures a query completes correctly despite individual worker node failures during execution"],
        ["Speculative execution", "Proactively re-executes slow-running tasks on other nodes, taking whichever result finishes first, to mitigate straggler effects"],
    ])},
    "big-data-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Multi-region disaster recovery", "A plan and architecture for restoring data platform operations after a regional outage"],
        ["Data platform architecture application", "Requires careful trade-offs between recovery time objective, recovery point objective, and the cost of cross-region redundancy"],
    ])},
    "big-data-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Storage format migration", "The process of converting data from one storage format to another"],
        ["Cost-efficient petabyte-scale migration", "Requires careful phased planning to migrate enormous datasets without excessive downtime or cost"],
    ])},
    "big-data-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Thesis-level capstone", "A culminating project requiring original design of a novel distributed data processing system"],
        ["Novel system design", "Requires identifying a genuine gap in existing big data processing approaches and rigorously designing and evaluating a new solution"],
    ])},
    "big-data-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Data governance maturity model", "A structured framework assessing an organization's data governance capability against progressive maturity levels"],
        ["Large organization application", "Enables benchmarking current governance practices and identifying a roadmap toward more mature data management"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Big Data"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    CHARTS["big-data-m2-l101"] = {"data_table": table(["Term", "Meaning"], [
        ["Streaming SQL", "Extends SQL semantics to continuously running queries over unbounded data streams"],
        ["Continuous query language", "Lets analysts express streaming logic declaratively, similar to batch SQL, rather than writing custom stream-processing code"],
    ])}

    for worked_n in range(102, 121):
        base_n = worked_n - 101
        base_key = f"big-data-m2-l{base_n}"
        worked_key = f"big-data-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Big Data lessons.")


if __name__ == "__main__":
    main()
