#!/usr/bin/env python3
"""Depth pass, C1 Big Data: fill in real, hand-checked data_table
content for the 69 C1 Big Data lessons not covered by the earlier
breadth-first batch. Brings C1 Big Data to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_big_data_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "big-data-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Big data", "Datasets too large or complex for traditional data processing tools"],
        ]),
    },
    "big-data-c1-l2": {
        "data_table": table(["Component", "Purpose"], [
            ["HDFS", "Distributed file storage"], ["MapReduce", "Distributed data processing"],
        ]),
    },
    "big-data-c1-l4": {
        "data_table": table(["Aspect", "Big Data", "Traditional Data"], [
            ["Volume", "Very large scale", "Manageable size"],
        ]),
    },
    "big-data-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Distributed computing", "Splitting a workload across multiple connected computers"],
        ]),
    },
    "big-data-c1-l6": {
        "data_table": table(["Type", "Example"], [
            ["Structured", "Relational database table"], ["Semi-structured", "JSON, XML"], ["Unstructured", "Images, free text"],
        ]),
    },
    "big-data-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Data warehouse", "A central repository for structured data used in reporting"],
        ]),
    },
    "big-data-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Data pipeline", "An automated sequence that moves and transforms data from source to destination"],
        ]),
    },
    "big-data-c1-l9": {
        "data_table": table(["Type", "Feature"], [
            ["Batch processing", "Processes large chunks of data at scheduled intervals"], ["Real-time processing", "Processes data as it arrives"],
        ]),
    },
    "big-data-c1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["HDFS", "Hadoop Distributed File System, stores data across many machines"],
        ]),
    },
    "big-data-c1-l11": {
        "data_table": table(["Phase", "Purpose"], [
            ["Map", "Processes and transforms input data in parallel"], ["Reduce", "Aggregates the mapped results"],
        ]),
    },
    "big-data-c1-l12": {
        "data_table": table(["Industry", "Use Case"], [
            ["Healthcare", "Analyzing patient records for treatment patterns"], ["Retail", "Personalizing recommendations from purchase history"],
        ]),
    },
    "big-data-c1-l13": {
        "data_table": table(["Tool", "Purpose"], [
            ["Hadoop", "Distributed storage and processing"], ["Spark", "Fast in-memory data processing"],
        ]),
    },
    "big-data-c1-l14": {
        "data_table": table(["Source", "Example"], [
            ["Sensors/IoT", "Continuous machine-generated readings"], ["Social media", "User-generated posts and interactions"],
        ]),
    },
    "big-data-c1-l15": {
        "data_table": table(["Dimension", "Question"], [
            ["Completeness", "Is any data missing?"], ["Timeliness", "Is the data current?"],
        ]),
    },
    "big-data-c1-l16": {
        "data_table": table(["Storage Type", "Best For"], [
            ["Columnar storage", "Fast analytical queries on specific columns"], ["Row storage", "Fast retrieval of complete records"],
        ]),
    },
    "big-data-c1-l17": {
        "data_table": table(["Format", "Use"], [
            ["JSON", "Human-readable, widely used"], ["Avro/Parquet", "Efficient binary formats for big data"],
        ]),
    },
    "big-data-c1-l18": {
        "data_table": table(["Statistic", "Use"], [
            ["Mean", "Summarizes central tendency at scale"],
        ]),
    },
    "big-data-c1-l19": {
        "data_table": table(["Benefit", "Detail"], [
            ["Elastic scaling", "Cloud resources expand or shrink with data processing demand"],
        ]),
    },
    "big-data-c1-l20": {
        "data_table": table(["Property", "Meaning"], [
            ["Consistency", "All nodes see the same data at the same time"], ["Availability", "Every request receives a response"], ["Partition tolerance", "System continues despite network failures"],
        ]),
    },
    "big-data-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Data lake", "Stores raw data of any format until it's needed"],
        ]),
    },
    "big-data-c1-l22": {
        "data_table": table(["Feature", "Data Lake", "Data Warehouse"], [
            ["Data format", "Raw, any type", "Structured, processed"],
        ]),
    },
    "big-data-c1-l23": {
        "data_table": table(["Process", "Order"], [
            ["ETL", "Extract, Transform, then Load"], ["ELT", "Extract, Load, then Transform"],
        ]),
    },
    "big-data-c1-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Streaming data", "Continuously generated data processed in real time"],
        ]),
    },
    "big-data-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Apache Kafka", "A distributed platform for publishing and streaming real-time data"],
        ]),
    },
    "big-data-c1-l26": {
        "data_table": table(["Type", "Example"], [
            ["Document database", "MongoDB"], ["Key-value store", "Redis"], ["Graph database", "Neo4j"],
        ]),
    },
    "big-data-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Document database", "Stores data as flexible, self-describing documents like JSON"],
        ]),
    },
    "big-data-c1-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Key-value store", "Stores data as simple key-value pairs for fast lookup"],
        ]),
    },
    "big-data-c1-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Graph database", "Stores data as nodes and relationships, ideal for connected data"],
        ]),
    },
    "big-data-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Data partitioning", "Dividing a dataset into distinct parts for parallel processing"],
        ]),
    },
    "big-data-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Sharding", "Splitting a database horizontally across multiple servers"],
        ]),
    },
    "big-data-c1-l32": {
        "data_table": table(["Model", "Meaning"], [
            ["Strong consistency", "All reads reflect the most recent write"], ["Eventual consistency", "Reads may briefly reflect stale data"],
        ]),
    },
    "big-data-c1-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Data governance", "Policies ensuring data quality, security, and proper use at scale"],
        ]),
    },
    "big-data-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Data lineage", "Tracks the origin and transformations of data through a pipeline"],
        ]),
    },
    "big-data-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Master data management", "Maintains a single, authoritative source of key business data"],
        ]),
    },
    "big-data-c1-l36": {
        "data_table": table(["Practice", "Reason"], [
            ["Encryption at rest and in transit", "Protects big data from unauthorized access"],
        ]),
    },
    "big-data-c1-l37": {
        "data_table": table(["Technique", "Purpose"], [
            ["Data masking", "Hides sensitive values while keeping data usable for analysis"],
        ]),
    },
    "big-data-c1-l38": {
        "data_table": table(["Method", "Purpose"], [
            ["Random sampling", "Analyzes a representative subset instead of the full dataset"],
        ]),
    },
    "big-data-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Log analytics", "Analyzing system-generated logs to find patterns or issues"],
        ]),
    },
    "big-data-c1-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Clickstream data", "Records of a user's sequence of clicks and page visits"],
        ]),
    },
    "big-data-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Data catalog", "An organized inventory of an organization's data assets"],
        ]),
    },
    "big-data-c1-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Metadata management", "Organizing information that describes and contextualizes data"],
        ]),
    },
    "big-data-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Data deduplication", "Removing duplicate copies of data to save space and improve accuracy"],
        ]),
    },
    "big-data-c1-l44": {
        "data_table": table(["Application", "Example"], [
            ["Predictive diagnostics", "Analyzing patient data to flag health risks early"],
        ]),
    },
    "big-data-c1-l45": {
        "data_table": table(["Application", "Example"], [
            ["Recommendation engines", "Suggesting products based on purchase history"],
        ]),
    },
    "big-data-c1-l46": {
        "data_table": table(["Application", "Example"], [
            ["Network optimization", "Analyzing call data to improve service coverage"],
        ]),
    },
    "big-data-c1-l47": {
        "data_table": table(["Application", "Example"], [
            ["Fraud detection", "Flagging unusual transaction patterns in real time"],
        ]),
    },
    "big-data-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["IoT data", "Data generated continuously by internet-connected sensors and devices"],
        ]),
    },
    "big-data-c1-l49": {
        "data_table": table(["Method", "Benefit"], [
            ["Data compression", "Reduces storage space and transfer time"],
        ]),
    },
    "big-data-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Data replication", "Copying data across multiple locations for reliability and speed"],
        ]),
    },
    "big-data-c1-l51": {
        "data_table": table(["Language", "Use"], [
            ["HiveQL", "SQL-like querying for Hadoop data"], ["Spark SQL", "SQL querying within Apache Spark"],
        ]),
    },
    "big-data-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Data skew", "Uneven distribution of data across partitions, slowing processing"],
        ]),
    },
    "big-data-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Job scheduling", "Coordinating when and how big data processing tasks run"],
        ]),
    },
    "big-data-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Data observability", "Monitoring the health and reliability of data pipelines"],
        ]),
    },
    "big-data-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Data mesh", "A decentralized approach where teams own their own data domains"],
        ]),
    },
    "big-data-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Lakehouse", "Combines data lake flexibility with data warehouse structure"],
        ]),
    },
    "big-data-c1-l57": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Right-sizing clusters", "Matches compute resources to actual workload, reducing waste"],
        ]),
    },
    "big-data-c1-l58": {
        "data_table": table(["Career", "Focus"], [
            ["Data engineer", "Builds and maintains data pipelines"], ["Big data architect", "Designs the overall data infrastructure"],
        ]),
    },
    "big-data-c1-l59": {
        "data_table": table(["Tool", "Purpose"], [
            ["Apache Spark", "Fast, general-purpose cluster computing"], ["Apache Kafka", "Real-time data streaming"],
        ]),
    },
    "big-data-c1-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Define data sources", "Identifies what data will flow into the pipeline"], ["Design storage layer", "Decides where processed data will live"],
        ]),
    },
    "big-data-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Sizing a big data project", "Estimating storage needs for a sample dataset"],
        ]),
    },
    "big-data-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Tracing a Hadoop job", "Following data through HDFS storage and MapReduce processing"],
        ]),
    },
    "big-data-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Applying the Five V's", "Classifying a sample dataset by volume, velocity, and variety"],
        ]),
    },
    "big-data-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Comparing approaches", "Deciding when a dataset needs big data tools versus a spreadsheet"],
        ]),
    },
    "big-data-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Distributing a workload", "Splitting a large computation across sample worker nodes"],
        ]),
    },
    "big-data-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Classifying data types", "Sorting sample data sources as structured, semi-, or unstructured"],
        ]),
    },
    "big-data-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Designing a warehouse schema", "Structuring a sample sales data warehouse"],
        ]),
    },
    "big-data-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Building a pipeline diagram", "Mapping the stages of a sample data pipeline"],
        ]),
    },
    "big-data-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a processing mode", "Deciding batch versus real-time for a sample use case"],
        ]),
    },
    "big-data-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Tracing HDFS storage", "Following how a large file is split and stored across nodes"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Big Data"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Big Data: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Big Data lessons (completing 70/70).")


if __name__ == "__main__":
    main()
