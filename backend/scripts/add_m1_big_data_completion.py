#!/usr/bin/env python3
"""Depth pass, M1 Big Data: fill in real, hand-checked data_table
content for the 119 M1 Big Data lessons not covered by the earlier
breadth-first batch. Brings M1 Big Data to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning cloud
big data platforms, stream/batch processing architectures, data
lakehouse and storage internals, distributed systems theory for data,
data governance, and applied big data domains; l101-l120 are "Worked
Analysis" companions reusing the data_table of l1-l20 (direct 1:1
mapping). l3 was already completed by an earlier breadth-first batch,
so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_big_data_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Layer", "Control"], [
    ["Network", "Firewalls and VPCs restrict who can reach the cluster"],
    ["Data", "Encryption and access control protect data itself"],
])

CHARTS: dict[str, dict] = {
    "big-data-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Cloud-based big data platform", "Provides managed, elastically scalable infrastructure for large-scale data processing"],
    ])},
    "big-data-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Big data security & privacy", "Protects large-scale datasets from unauthorized access and misuse"],
    ])},
    "big-data-m1-l4": {"data_table": table(["State", "Protection"], [
        ["At rest", "Encrypted while stored on disk"],
        ["In transit", "Encrypted while moving across the network"],
    ])},
    "big-data-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Fine-grained access control", "Governs permissions at the table, column, or row level (e.g. Ranger, Sentry)"],
    ])},
    "big-data-m1-l6": {"data_table": table(["Technique", "Feature"], [
        ["Anonymization", "Irreversibly removes identifying information"],
        ["Masking", "Obscures sensitive values while preserving format"],
    ])},
    "big-data-m1-l7": {"data_table": table(["Warehouse", "Feature"], [
        ["Redshift/BigQuery/Snowflake", "Managed cloud data warehouses separating storage and compute for analytics"],
    ])},
    "big-data-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Managed Spark service", "Runs Apache Spark clusters without the customer managing the underlying infrastructure"],
    ])},
    "big-data-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Serverless big data processing", "Runs data jobs without provisioning or managing servers directly"],
    ])},
    "big-data-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Cost optimization", "Reduces cloud spend on big data workloads through sizing and scheduling choices"],
    ])},
    "big-data-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Capacity planning", "Forecasts future cluster resource needs based on expected data growth"],
    ])},
    "big-data-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Cluster sizing", "Determines the right number and type of nodes for a workload's requirements"],
    ])},
    "big-data-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Observability", "Monitors metrics, logs, and traces to understand a big data system's health"],
    ])},
    "big-data-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Disaster recovery", "Plans and tests how a big data platform recovers from major outages"],
    ])},
    "big-data-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tenancy", "Isolates different teams' workloads while sharing the same underlying cluster"],
    ])},
    "big-data-m1-l16": {"data_table": table(["Domain", "Use Case"], [
        ["Retail/e-commerce", "Personalization, inventory forecasting, and clickstream analysis"],
    ])},
    "big-data-m1-l17": {"data_table": table(["Domain", "Use Case"], [
        ["Healthcare/finance", "Clinical analytics and fraud detection at large scale"],
    ])},
    "big-data-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Real-time fraud detection", "Flags suspicious transactions within milliseconds using streaming data"],
    ])},
    "big-data-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Recommendation system at scale", "Serves personalized suggestions to millions of users with low latency"],
    ])},
    "big-data-m1-l20": {"data_table": table(["Trend", "Detail"], [
        ["Future big data trends", "Includes lakehouse convergence, real-time ML, and data mesh adoption"],
    ])},
    "big-data-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Lambda architecture", "Runs parallel batch and speed layers, merging results for both accuracy and low latency"],
    ])},
    "big-data-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Kappa architecture", "Treats all data as a stream, avoiding a separate batch layer entirely"],
    ])},
    "big-data-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Kafka partitioning/replication", "Splits a topic across partitions and replicates them for throughput and durability"],
    ])},
    "big-data-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Exactly-once semantics", "Guarantees each event is processed and reflected in output exactly one time"],
    ])},
    "big-data-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Watermarking", "Tracks event-time progress in a stream to decide when a window's results are complete"],
    ])},
    "big-data-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Checkpointing", "Periodically saves streaming application state so it can recover after a failure"],
    ])},
    "big-data-m1-l27": {"data_table": table(["Format", "Feature"], [
        ["Delta Lake / Iceberg", "Add ACID transactions and schema management on top of a data lake"],
    ])},
    "big-data-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Schema evolution", "Allows a data pipeline's schema to change over time without breaking consumers"],
    ])},
    "big-data-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Data partitioning", "Splits a large dataset into segments to speed up distributed query execution"],
    ])},
    "big-data-m1-l30": {"data_table": table(["Format", "Feature"], [
        ["Parquet / ORC", "Columnar storage formats optimized for fast analytical query scans"],
    ])},
    "big-data-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Cost-based optimizer", "Chooses a query execution plan based on estimated data statistics and costs"],
    ])},
    "big-data-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Data skew", "Uneven data distribution across partitions that slows down distributed processing"],
    ])},
    "big-data-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Change data capture", "Streams incremental changes from a source database as they happen"],
    ])},
    "big-data-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Deduplication at scale", "Identifies and removes duplicate records across very large datasets"],
    ])},
    "big-data-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Sketch algorithm", "Approximates aggregate statistics using much less memory than exact computation"],
    ])},
    "big-data-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Bloom filter", "A probabilistic structure that quickly tests whether an item is possibly in a set"],
    ])},
    "big-data-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Two-phase commit", "Coordinates a distributed transaction's commit across multiple nodes atomically"],
    ])},
    "big-data-m1-l38": {"data_table": table(["Algorithm", "Purpose"], [
        ["Raft / Paxos", "Achieve consensus on a single value among distributed nodes despite failures"],
    ])},
    "big-data-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["CAP theorem", "A distributed system can guarantee at most two of Consistency, Availability, Partition tolerance"],
    ])},
    "big-data-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Eventual consistency", "Replicas converge to the same value over time, without guaranteeing it instantly"],
    ])},
    "big-data-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Data mesh", "Decentralizes data ownership to domain teams rather than one central data team"],
    ])},
    "big-data-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Data fabric", "Provides a unified layer for accessing data across disparate sources and locations"],
    ])},
    "big-data-m1-l43": {"data_table": table(["Framework", "Purpose"], [
        ["Pregel / GraphX", "Process very large graphs using distributed vertex-centric computation"],
    ])},
    "big-data-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Time-series database", "Optimized for storing and querying high-velocity, timestamped data"],
    ])},
    "big-data-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Data compression", "Reduces storage footprint and I/O cost for large-scale datasets"],
    ])},
    "big-data-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Data catalog", "An organized inventory of an organization's datasets and their metadata"],
    ])},
    "big-data-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Data lineage", "Traces the origin and transformations a piece of data underwent through a pipeline"],
    ])},
    "big-data-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Master data management", "Maintains a single, authoritative source of an organization's core data entities"],
    ])},
    "big-data-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Data quality framework", "Automatically validates data against defined correctness rules"],
    ])},
    "big-data-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Data versioning", "Tracks changes to large datasets over time for reproducible analytics"],
    ])},
    "big-data-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Catalyst optimizer", "Spark's query optimizer that rewrites logical plans into efficient physical execution"],
    ])},
    "big-data-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Predicate pushdown", "Filters data as early as possible, ideally at the storage layer, to reduce I/O"],
    ])},
    "big-data-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Distributed ML training", "Trains a model by splitting data or the model itself across many machines"],
    ])},
    "big-data-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["DAG scheduling", "Orders and runs pipeline tasks respecting their dependency graph"],
    ])},
    "big-data-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Idempotency (pipelines)", "Ensures re-running a pipeline step produces the same result without duplication"],
    ])},
    "big-data-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Backpressure", "Signals upstream producers to slow down when downstream consumers can't keep up"],
    ])},
    "big-data-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Data sharding", "Splits a dataset horizontally across multiple servers to scale storage and throughput"],
    ])},
    "big-data-m1-l58": {"data_table": table(["Tier", "Feature"], [
        ["Hot data", "Frequently accessed, kept on fast expensive storage"],
        ["Cold data", "Rarely accessed, moved to cheap slow storage"],
    ])},
    "big-data-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Query federation", "Queries multiple heterogeneous data sources as if they were one unified system"],
    ])},
    "big-data-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Data observability", "Monitors data freshness, volume, and schema for unexpected anomalies"],
    ])},
    "big-data-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Windowed aggregation", "Groups streaming events into time windows to compute rolling statistics"],
    ])},
    "big-data-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Data governance", "Policies and processes ensuring data is accurate, secure, and properly used"],
    ])},
    "big-data-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy", "Adds calibrated noise so individual records cannot be reverse-engineered"],
    ])},
    "big-data-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic data for testing", "Generates artificial big-data-scale test data mimicking real statistical properties"],
    ])},
    "big-data-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Data mesh interoperability", "Standardizes formats so different domain teams' data products can be combined"],
    ])},
    "big-data-m1-l66": {"data_table": table(["Domain", "Use Case"], [
        ["Genomics", "Runs variant-calling pipelines across massive sequencing datasets"],
    ])},
    "big-data-m1-l67": {"data_table": table(["Domain", "Use Case"], [
        ["Telecommunications", "Analyzes network traffic at internet scale for performance and security"],
    ])},
    "big-data-m1-l68": {"data_table": table(["Domain", "Use Case"], [
        ["Smart cities", "Integrates data from citywide sensor networks for planning and services"],
    ])},
    "big-data-m1-l69": {"data_table": table(["Domain", "Use Case"], [
        ["Climate science", "Processes massive simulation output for climate modeling"],
    ])},
    "big-data-m1-l70": {"data_table": table(["Schema", "Feature"], [
        ["Star schema", "A central fact table linked directly to dimension tables"],
        ["Snowflake schema", "Normalizes dimension tables into sub-dimensions"],
    ])},
    "big-data-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Slowly changing dimension", "A dimension table strategy for tracking how attribute values change over time"],
    ])},
    "big-data-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Federated computational governance", "Allows domain teams autonomy while enforcing shared organization-wide policy"],
    ])},
    "big-data-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Real-time personalization", "Serves individualized content or recommendations with sub-second latency at scale"],
    ])},
    "big-data-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Anomaly detection (telemetry)", "Flags unusual patterns in high-volume streaming monitoring data"],
    ])},
    "big-data-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Geographic replication", "Copies data across regions for durability, latency, and compliance"],
    ])},
    "big-data-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tenant resource isolation", "Prevents one tenant's workload from starving another's on a shared cluster"],
    ])},
    "big-data-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Pipeline testing", "Applies unit and integration testing discipline to data transformation logic"],
    ])},
    "big-data-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Cost-aware query planning", "Chooses query execution strategies that account for cloud compute cost, not just speed"],
    ])},
    "big-data-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Workload benchmarking", "Systematically measures big data system performance under representative workloads"],
    ])},
    "big-data-m1-l80": {"data_table": table(["Approach", "Trade-off"], [
        ["Data mesh", "Decentralized ownership, more organizational complexity"],
        ["Data lakehouse", "Centralized platform, simpler governance"],
    ])},
    "big-data-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Streaming SQL", "Runs continuously updating SQL queries over an unbounded data stream"],
    ])},
    "big-data-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Encryption key management at scale", "Securely generates, rotates, and revokes keys across a large data platform"],
    ])},
    "big-data-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Serverless streaming cost model", "Charges based on actual event processing rather than provisioned capacity"],
    ])},
    "big-data-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Data contract", "A formal agreement defining the schema and guarantees of data shared between teams"],
    ])},
    "big-data-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Distributed caching layer", "Accelerates repeated big data queries by caching hot results across nodes"],
    ])},
    "big-data-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Log analytics architecture", "Ingests and indexes massive log volumes for fast search and analysis"],
    ])},
    "big-data-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Vectorized query execution", "Processes data in batches of columns rather than row-by-row for speed"],
    ])},
    "big-data-m1-l88": {"data_table": table(["Approach", "Order"], [
        ["ETL", "Transform data before loading it into the warehouse"],
        ["ELT", "Load raw data first, then transform it inside the warehouse"],
    ])},
    "big-data-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Data as a product", "Treats each dataset as a product with an owner, SLAs, and documented interface"],
    ])},
    "big-data-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Multi-modal data fusion", "Combines structured and unstructured data types into a unified analysis"],
    ])},
    "big-data-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Cluster autoscaling", "Automatically adjusts cluster size to match current processing demand"],
    ])},
    "big-data-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Feature engineering pipeline (distributed)", "Computes ML input features at scale across a distributed dataset"],
    ])},
    "big-data-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Immutable audit log", "Records system actions in a tamper-evident way for compliance auditing"],
    ])},
    "big-data-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Cross-cluster synchronization", "Keeps data consistent across multiple independent big data clusters"],
    ])},
    "big-data-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Chaos engineering (big data)", "Deliberately injects failures to test a data platform's resilience"],
    ])},
    "big-data-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Schema registry", "Centrally stores and validates data schemas shared across producers and consumers"],
    ])},
    "big-data-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Cost attribution / chargeback", "Allocates shared big data infrastructure costs back to individual teams"],
    ])},
    "big-data-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Streaming model updates", "Continuously refreshes a deployed ML model as new data arrives"],
    ])},
    "big-data-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Ethics of large-scale profiling", "Considers fairness and consent when building detailed profiles from big data"],
    ])},
    "big-data-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Vector database indexing", "Enables fast approximate nearest-neighbor search across billions of embeddings"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"big-data-m1-l{base_n}"
    worked_key = f"big-data-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Big Data"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Big Data: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Big Data lessons (completing 120/120).")


if __name__ == "__main__":
    main()
