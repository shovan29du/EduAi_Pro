#!/usr/bin/env python3
"""Depth pass, C2 Cybersecurity: fill in real, hand-checked data_table
content for the 69 C2 Cybersecurity lessons not covered by the earlier
breadth-first batch. Brings C2 Cybersecurity to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_cybersecurity_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cybersecurity-c2-l1": {
        "data_table": table(["Control", "Purpose"], [
            ["Access control lists", "Restrict which users or processes can access resources"],
        ]),
    },
    "cybersecurity-c2-l2": {
        "data_table": table(["Type", "Feature"], [
            ["Symmetric encryption", "Uses one shared key for encryption and decryption"], ["Asymmetric encryption", "Uses a public/private key pair"],
        ]),
    },
    "cybersecurity-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["DMZ", "A buffer network zone isolating public-facing servers from the internal network"],
        ]),
    },
    "cybersecurity-c2-l5": {
        "data_table": table(["Algorithm", "Use"], [
            ["SHA-256", "Produces a fixed-size hash to verify data hasn't been altered"],
        ]),
    },
    "cybersecurity-c2-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["PKI", "A system of certificates and keys that manages secure digital identities"],
        ]),
    },
    "cybersecurity-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital signature", "Cryptographically proves a message's origin and integrity"],
        ]),
    },
    "cybersecurity-c2-l8": {
        "data_table": table(["Technology", "Method"], [
            ["Signature-based detection", "Identifies known malware by matching known patterns"], ["Behavior-based detection", "Flags suspicious activity patterns even from unknown threats"],
        ]),
    },
    "cybersecurity-c2-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["SIEM", "Aggregates and analyzes security event data across an organization"],
        ]),
    },
    "cybersecurity-c2-l10": {
        "data_table": table(["Step", "Purpose"], [
            ["Correlating log entries", "Reveals attack patterns invisible in a single log source"],
        ]),
    },
    "cybersecurity-c2-l11": {
        "data_table": table(["Practice", "Reason"], [
            ["Disabling unused services", "Reduces the attack surface on a Linux system"],
        ]),
    },
    "cybersecurity-c2-l12": {
        "data_table": table(["Practice", "Reason"], [
            ["Applying Group Policy restrictions", "Enforces consistent security settings across Windows machines"],
        ]),
    },
    "cybersecurity-c2-l13": {
        "data_table": table(["Step", "Purpose"], [
            ["Testing patches before deployment", "Prevents updates from breaking production systems"],
        ]),
    },
    "cybersecurity-c2-l14": {
        "data_table": table(["Protocol", "Purpose"], [
            ["SSH", "Provides secure encrypted remote command-line access"], ["TLS", "Encrypts data in transit over a network connection"],
        ]),
    },
    "cybersecurity-c2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Ethical hacking", "Authorized security testing to find vulnerabilities before attackers do"],
        ]),
    },
    "cybersecurity-c2-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Vulnerability scan", "An automated process identifying known weaknesses in systems"],
        ]),
    },
    "cybersecurity-c2-l17": {
        "data_table": table(["Vulnerability", "Example"], [
            ["Injection", "Untrusted input executed as part of a command or query"], ["Broken access control", "Users able to act outside their intended permissions"],
        ]),
    },
    "cybersecurity-c2-l18": {
        "data_table": table(["Protocol", "Feature"], [
            ["WPA2", "Uses AES encryption, widely deployed standard"], ["WPA3", "Adds stronger protection against offline password guessing"],
        ]),
    },
    "cybersecurity-c2-l19": {
        "data_table": table(["Record", "Purpose"], [
            ["SPF", "Specifies which servers may send email for a domain"], ["DKIM", "Cryptographically signs outgoing email to verify integrity"], ["DMARC", "Tells receivers how to handle SPF/DKIM failures"],
        ]),
    },
    "cybersecurity-c2-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Security baseline", "A minimum set of required security configurations for a system"],
        ]),
    },
    "cybersecurity-c2-l21": {
        "data_table": table(["Phase", "Purpose"], [
            ["Reconnaissance", "Gathers information about the target before testing"], ["Exploitation", "Attempts to actively exploit discovered vulnerabilities"],
        ]),
    },
    "cybersecurity-c2-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Buffer overflow", "Writing more data to a buffer than it can hold, corrupting adjacent memory"],
        ]),
    },
    "cybersecurity-c2-l23": {
        "data_table": table(["Type", "Example"], [
            ["Vertical privilege escalation", "Gaining higher-level access than originally granted"], ["Horizontal privilege escalation", "Accessing another user's resources at the same privilege level"],
        ]),
    },
    "cybersecurity-c2-l24": {
        "data_table": table(["Technique", "Purpose"], [
            ["Static analysis", "Examines malware code without executing it"], ["Dynamic analysis", "Observes malware behavior by running it in a sandbox"],
        ]),
    },
    "cybersecurity-c2-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Reverse engineering", "Analyzing compiled software to understand its inner workings"],
        ]),
    },
    "cybersecurity-c2-l26": {
        "data_table": table(["Step", "Purpose"], [
            ["TLS handshake", "Negotiates encryption parameters before a secure session begins"],
        ]),
    },
    "cybersecurity-c2-l27": {
        "data_table": table(["Property", "Security Benefit"], [
            ["Distributed ledger", "No single point of failure for attackers to target"],
        ]),
    },
    "cybersecurity-c2-l28": {
        "data_table": table(["Technique", "Purpose"], [
            ["Packet capture analysis", "Reveals suspicious patterns in network traffic"],
        ]),
    },
    "cybersecurity-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Threat hunting", "Proactively searching for hidden threats not caught by automated tools"],
        ]),
    },
    "cybersecurity-c2-l30": {
        "data_table": table(["Phase", "Purpose"], [
            ["Containment", "Limits the spread of an active security incident"], ["Eradication", "Removes the root cause of the incident"],
        ]),
    },
    "cybersecurity-c2-l31": {
        "data_table": table(["Team", "Role"], [
            ["Red team", "Simulates attacks to test defenses"], ["Blue team", "Defends against and detects the simulated attacks"],
        ]),
    },
    "cybersecurity-c2-l32": {
        "data_table": table(["Technique", "Purpose"], [
            ["Fuzzing", "Feeds malformed input to discover unexpected application behavior"],
        ]),
    },
    "cybersecurity-c2-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["SOAR", "Automates repetitive security response tasks across multiple tools"],
        ]),
    },
    "cybersecurity-c2-l34": {
        "data_table": table(["Feature", "Detail"], [
            ["Advanced Persistent Threat", "A prolonged, targeted intrusion typically by well-resourced actors"],
        ]),
    },
    "cybersecurity-c2-l35": {
        "data_table": table(["Control", "Purpose"], [
            ["Shared responsibility model", "Divides security duties between cloud provider and customer"],
        ]),
    },
    "cybersecurity-c2-l36": {
        "data_table": table(["Practice", "Reason"], [
            ["Scanning container images", "Catches known vulnerabilities before deployment"],
        ]),
    },
    "cybersecurity-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Single Sign-On", "Lets a user authenticate once for access to multiple systems"],
        ]),
    },
    "cybersecurity-c2-l38": {
        "data_table": table(["System", "Risk"], [
            ["ICS/SCADA", "Legacy industrial systems often lack modern security controls"],
        ]),
    },
    "cybersecurity-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Cryptanalysis", "The study of methods for breaking cryptographic systems"],
        ]),
    },
    "cybersecurity-c2-l40": {
        "data_table": table(["Step", "Purpose"], [
            ["Manual secure code review", "Catches logic flaws automated scanners often miss"],
        ]),
    },
    "cybersecurity-c2-l41": {
        "data_table": table(["Attack", "Method"], [
            ["Evil twin", "A rogue access point mimicking a legitimate wireless network"],
        ]),
    },
    "cybersecurity-c2-l42": {
        "data_table": table(["Technique", "Purpose"], [
            ["Memory forensics", "Extracts evidence from a system's volatile RAM"],
        ]),
    },
    "cybersecurity-c2-l43": {
        "data_table": table(["Technique", "Purpose"], [
            ["Disk imaging", "Creates an exact forensic copy of a storage device for analysis"],
        ]),
    },
    "cybersecurity-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Pretexting", "Creating a fabricated scenario to manipulate a target into revealing information"],
        ]),
    },
    "cybersecurity-c2-l45": {
        "data_table": table(["Component", "Focus"], [
            ["Governance", "Sets organizational security policy and accountability"], ["Compliance", "Ensures adherence to legal and regulatory requirements"],
        ]),
    },
    "cybersecurity-c2-l46": {
        "data_table": table(["Framework", "Categories"], [
            ["STRIDE", "Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation"],
        ]),
    },
    "cybersecurity-c2-l47": {
        "data_table": table(["Principle", "Meaning"], [
            ["Zero Trust", "Never trust, always verify, regardless of network location"],
        ]),
    },
    "cybersecurity-c2-l48": {
        "data_table": table(["State", "Protection"], [
            ["Data at rest", "Encrypted storage on disk"], ["Data in transit", "Encrypted network transmission"],
        ]),
    },
    "cybersecurity-c2-l49": {
        "data_table": table(["Practice", "Benefit"], [
            ["Scripting repetitive security checks", "Reduces manual effort and human error"],
        ]),
    },
    "cybersecurity-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["DevSecOps", "Integrates security practices throughout the software development lifecycle"],
        ]),
    },
    "cybersecurity-c2-l51": {
        "data_table": table(["Indicator", "Detail"], [
            ["Unusual data access patterns", "A common signal of insider threat activity"],
        ]),
    },
    "cybersecurity-c2-l52": {
        "data_table": table(["Vulnerability", "Detail"], [
            ["Insecure data storage", "A common mobile app vulnerability exposing sensitive local data"],
        ]),
    },
    "cybersecurity-c2-l53": {
        "data_table": table(["Challenge", "Detail"], [
            ["Attribution difficulty", "Attackers routinely obscure their identity through proxies and false flags"],
        ]),
    },
    "cybersecurity-c2-l54": {
        "data_table": table(["Risk", "Mitigation"], [
            ["Broken object level authorization", "Enforce strict per-object access checks on every API call"],
        ]),
    },
    "cybersecurity-c2-l55": {
        "data_table": table(["Step", "Purpose"], [
            ["Tuning SIEM rules", "Reduces false positives while preserving true threat detection"],
        ]),
    },
    "cybersecurity-c2-l56": {
        "data_table": table(["Concept", "Meaning"], [
            ["Responsible disclosure", "Reporting vulnerabilities privately to allow time for a fix before public release"],
        ]),
    },
    "cybersecurity-c2-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Cyber insurance", "Financial coverage transferring some risk of a security incident's costs"],
        ]),
    },
    "cybersecurity-c2-l58": {
        "data_table": table(["Risk", "Example"], [
            ["Compromised third-party vendor", "Can introduce vulnerabilities into an otherwise secure organization"],
        ]),
    },
    "cybersecurity-c2-l59": {
        "data_table": table(["Component", "Purpose"], [
            ["Security Operations Center", "A centralized team monitoring and responding to security events 24/7"],
        ]),
    },
    "cybersecurity-c2-l60": {
        "data_table": table(["Layer", "Purpose"], [
            ["Defense-in-depth", "Combines multiple overlapping security controls so no single failure is catastrophic"],
        ]),
    },
    "cybersecurity-c2-l61": {
        "data_table": table(["Mitigation", "Detail"], [
            ["Stack canaries", "Detect buffer overflow attempts before they can overwrite return addresses"],
        ]),
    },
    "cybersecurity-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a malware sample", "Identifying its behavior in an isolated sandbox environment"],
        ]),
    },
    "cybersecurity-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Disassembling a binary", "Reading assembly code to understand a program's logic"],
        ]),
    },
    "cybersecurity-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Automating an incident response playbook", "Triggering containment actions automatically on detection"],
        ]),
    },
    "cybersecurity-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing an APT case study", "Tracing the attack's kill chain from entry to exfiltration"],
        ]),
    },
    "cybersecurity-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Hardening a Kubernetes cluster", "Applying network policies to restrict pod communication"],
        ]),
    },
    "cybersecurity-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating a disclosure decision", "Weighing legal and ethical duties when reporting a found vulnerability"],
        ]),
    },
    "cybersecurity-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Tuning an IDS", "Reducing false positives while catching real intrusion attempts"],
        ]),
    },
    "cybersecurity-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Auditing OS security settings", "Comparing a system's configuration against a hardening checklist"],
        ]),
    },
    "cybersecurity-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Choosing an encryption approach", "Deciding between symmetric and asymmetric encryption for a use case"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cybersecurity"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Cybersecurity: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Cybersecurity lessons (completing 70/70).")


if __name__ == "__main__":
    main()
