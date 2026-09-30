#!/usr/bin/env python3
"""Depth pass, C2 Big Data: fill in real, hand-checked data_table
content for the 69 C2 Big Data lessons not covered by the earlier
breadth-first batch. Brings C2 Big Data to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_big_data_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "big-data-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Apache Spark", "A distributed computing engine for fast, large-scale data processing"],
        ]),
    },
    "big-data-c2-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Distributed file system", "Stores data across many machines while presenting a unified file interface"],
        ]),
    },
    "big-data-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Replication factor", "The number of copies of each data block stored across the cluster"],
        ]),
    },
    "big-data-c2-l5": {
        "data_table": table(["Phase", "Purpose"], [
            ["Map", "Processes input data in parallel into key-value pairs"], ["Reduce", "Aggregates the mapped results by key"],
        ]),
    },
    "big-data-c2-l6": {
        "data_table": table(["Component", "Role"], [
            ["ResourceManager", "Allocates cluster resources to applications"], ["NodeManager", "Manages resources on an individual node"],
        ]),
    },
    "big-data-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Hive", "Provides a SQL-like interface for querying data stored in Hadoop"],
        ]),
        "formulae": ["SELECT category, COUNT(*) FROM sales GROUP BY category;"],
    },
    "big-data-c2-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Pig Latin", "A high-level scripting language for expressing data transformation pipelines on Hadoop"],
        ]),
    },
    "big-data-c2-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["HBase", "A distributed, column-family NoSQL database built on top of HDFS"],
        ]),
    },
    "big-data-c2-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Sqoop", "Transfers bulk data between Hadoop and relational databases"],
        ]),
    },
    "big-data-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Oozie", "Schedules and coordinates multi-step Hadoop workflow jobs"],
        ]),
    },
    "big-data-c2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["RDD", "Resilient Distributed Dataset, Spark's core immutable, fault-tolerant data abstraction"],
        ]),
    },
    "big-data-c2-l13": {
        "data_table": table(["Type", "Feature"], [
            ["Transformation", "Lazily defines a new RDD, like map or filter"], ["Action", "Triggers computation and returns a result, like count or collect"],
        ]),
    },
    "big-data-c2-l14": {
        "data_table": table(["Manager", "Feature"], [
            ["YARN", "Hadoop's native resource manager"], ["Kubernetes", "Container-based orchestration increasingly used to run Spark"],
        ]),
    },
    "big-data-c2-l15": {
        "data_table": table(["Setting", "Purpose"], [
            ["spark.executor.memory", "Controls how much memory each executor process can use"],
        ]),
    },
    "big-data-c2-l16": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Hash partitioning", "Distributes data evenly across partitions based on key hash"],
        ]),
    },
    "big-data-c2-l17": {
        "data_table": table(["System", "Feature"], [
            ["MapReduce", "Writes intermediate results to disk between stages"], ["Spark", "Processes data in memory, often much faster for iterative workloads"],
        ]),
    },
    "big-data-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["ZooKeeper", "Coordinates configuration and synchronization across distributed systems"],
        ]),
    },
    "big-data-c2-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Data locality", "Scheduling computation near where the data physically resides to reduce network transfer"],
        ]),
    },
    "big-data-c2-l20": {
        "data_table": table(["Mechanism", "Purpose"], [
            ["Block replication", "Ensures data survives individual node failures"],
        ]),
    },
    "big-data-c2-l21": {
        "data_table": table(["Component", "Role"], [
            ["Producer", "Publishes messages to a Kafka topic"], ["Consumer", "Reads messages from a Kafka topic"],
        ]),
    },
    "big-data-c2-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Kafka Streams", "A library for building real-time stream processing applications on Kafka"],
        ]),
    },
    "big-data-c2-l23": {
        "data_table": table(["Feature", "Detail"], [
            ["Apache Flink", "A stream processing framework emphasizing low-latency, stateful computation"],
        ]),
    },
    "big-data-c2-l24": {
        "data_table": table(["Window Type", "Feature"], [
            ["Tumbling window", "Fixed, non-overlapping time intervals"], ["Sliding window", "Overlapping intervals that update more frequently"],
        ]),
    },
    "big-data-c2-l25": {
        "data_table": table(["Semantic", "Guarantee"], [
            ["Exactly-once processing", "Each record affects the final result exactly one time, even after failures"],
        ]),
    },
    "big-data-c2-l26": {
        "data_table": table(["Architecture", "Feature"], [
            ["Lambda architecture", "Maintains separate batch and speed layers"], ["Kappa architecture", "Uses a single stream-processing layer for both"],
        ]),
    },
    "big-data-c2-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Delta Lake", "Adds ACID transactions and versioning on top of data lake storage"],
        ]),
    },
    "big-data-c2-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Apache Iceberg", "An open table format supporting schema evolution and time travel for large datasets"],
        ]),
    },
    "big-data-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Trino/Presto", "Distributed SQL query engines for fast interactive analytics across data sources"],
        ]),
    },
    "big-data-c2-l30": {
        "data_table": table(["Feature", "Benefit"], [
            ["Cloud-native warehouse", "Separates storage and compute for independent, elastic scaling"],
        ]),
    },
    "big-data-c2-l31": {
        "data_table": table(["Format", "Feature"], [
            ["Parquet", "Columnar format optimized for analytical queries"], ["ORC", "Columnar format optimized for Hive workloads"],
        ]),
    },
    "big-data-c2-l32": {
        "data_table": table(["Change Type", "Consideration"], [
            ["Adding a column", "Usually backward-compatible"], ["Removing a column", "Can break downstream consumers"],
        ]),
    },
    "big-data-c2-l33": {
        "data_table": table(["Dimension", "Check"], [
            ["Completeness", "Are required fields populated?"], ["Consistency", "Do values match expected formats and ranges?"],
        ]),
    },
    "big-data-c2-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Airflow DAG", "Defines a workflow as a directed graph of dependent tasks"],
        ]),
    },
    "big-data-c2-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["dbt", "Transforms data already loaded into a warehouse using version-controlled SQL"],
        ]),
    },
    "big-data-c2-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Change Data Capture", "Tracks and streams row-level changes from a source database in real time"],
        ]),
    },
    "big-data-c2-l37": {
        "data_table": table(["Technique", "Purpose"], [
            ["Predicate pushdown", "Filters data as early as possible to reduce data scanned"],
        ]),
    },
    "big-data-c2-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Data skew", "Uneven distribution of data across partitions, causing some tasks to run much slower"],
        ]),
    },
    "big-data-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Approximate query processing", "Trades small accuracy loss for dramatically faster query results on huge datasets"],
        ]),
    },
    "big-data-c2-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Bloom filter", "A space-efficient probabilistic structure testing set membership with no false negatives"],
        ]),
    },
    "big-data-c2-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["HyperLogLog", "Estimates the number of distinct elements in a huge dataset using minimal memory"],
        ]),
    },
    "big-data-c2-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Pregel model", "Processes large graphs through iterative message-passing between vertices"],
        ]),
    },
    "big-data-c2-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["ML pipeline at scale", "Automates data prep, training, and evaluation across distributed compute"],
        ]),
    },
    "big-data-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Feature store", "A centralized repository for storing and serving ML features consistently"],
        ]),
    },
    "big-data-c2-l45": {
        "data_table": table(["Feature", "Purpose"], [
            ["Real-time dashboard", "Continuously visualizes metrics as streaming data updates"],
        ]),
    },
    "big-data-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Data contract", "A formal agreement defining the schema and expectations between data producers and consumers"],
        ]),
    },
    "big-data-c2-l47": {
        "data_table": table(["Challenge", "Detail"], [
            ["Multi-cloud data movement", "Requires careful cost and latency management across providers"],
        ]),
    },
    "big-data-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Cost-based optimizer", "Chooses a query execution plan based on estimated resource cost"],
        ]),
    },
    "big-data-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Data versioning", "Tracks changes to large datasets over time, enabling rollback and reproducibility"],
        ]),
    },
    "big-data-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Differential privacy", "Adds calibrated noise to query results to protect individual privacy while preserving aggregate accuracy"],
        ]),
    },
    "big-data-c2-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Data mesh", "Decentralizes data ownership to domain teams rather than a central data platform team"],
        ]),
    },
    "big-data-c2-l52": {
        "data_table": table(["Metric", "Meaning"], [
            ["RTO", "Maximum acceptable time to restore a big data platform after a failure"],
        ]),
    },
    "big-data-c2-l53": {
        "data_table": table(["Step", "Purpose"], [
            ["Forecasting cluster growth", "Prevents both under-provisioning outages and wasted over-provisioned spend"],
        ]),
    },
    "big-data-c2-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Data SLA", "A formal commitment on data freshness, quality, or availability"],
        ]),
    },
    "big-data-c2-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Serverless big data processing", "Runs large-scale jobs without provisioning or managing underlying servers"],
        ]),
    },
    "big-data-c2-l56": {
        "data_table": table(["Approach", "Feature"], [
            ["Data mesh", "Decentralized domain ownership"], ["Data fabric", "A unified architecture layer connecting distributed data sources"],
        ]),
    },
    "big-data-c2-l57": {
        "data_table": table(["Metric", "Purpose"], [
            ["Query throughput", "Measures how many queries a system can process per unit time"],
        ]),
    },
    "big-data-c2-l58": {
        "data_table": table(["Regulation", "Requirement"], [
            ["GDPR", "Requires data minimization and the right to be forgotten"],
        ]),
    },
    "big-data-c2-l59": {
        "data_table": table(["Step", "Consideration"], [
            ["Choosing storage architecture", "Balancing cost, latency, and scalability requirements"],
        ]),
    },
    "big-data-c2-l60": {
        "data_table": table(["Trend", "Detail"], [
            ["Lakehouse architecture", "Combines data lake flexibility with data warehouse reliability"],
        ]),
    },
    "big-data-c2-l61": {
        "data_table": table(["Feature", "Detail"], [
            ["Queue-based scheduling", "YARN allocates cluster capacity fairly across competing applications"],
        ]),
    },
    "big-data-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Choosing Spark over MapReduce", "Selecting the engine best suited for an iterative machine learning job"],
        ]),
    },
    "big-data-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Comparing storage systems", "Weighing HDFS against a cloud object store for a new pipeline"],
        ]),
    },
    "big-data-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Tracing a file write", "Following how the NameNode coordinates DataNode block writes"],
        ]),
    },
    "big-data-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Recovering from node failure", "Explaining how replication restores a lost data block"],
        ]),
    },
    "big-data-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Writing a MapReduce job", "Counting word frequency across a large text corpus"],
        ]),
    },
    "big-data-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing resource contention", "Diagnosing why a YARN application is queued"],
        ]),
    },
    "big-data-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Writing a Hive query", "Aggregating sales data using GROUP BY across a large table"],
        ]),
    },
    "big-data-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Writing a Pig script", "Filtering and transforming a large dataset with LOAD and FILTER"],
        ]),
    },
    "big-data-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Designing an HBase schema", "Choosing a row key that avoids hotspotting"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Big Data"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Big Data: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Big Data lessons (completing 70/70).")


if __name__ == "__main__":
    main()
