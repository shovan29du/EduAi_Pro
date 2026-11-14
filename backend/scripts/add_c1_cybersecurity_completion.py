#!/usr/bin/env python3
"""Depth pass, C1 Cybersecurity: fill in real, hand-checked data_table
content for the 69 C1 Cybersecurity lessons not covered by the earlier
breadth-first batch. Brings C1 Cybersecurity to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_cybersecurity_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cybersecurity-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Cybersecurity", "Protecting computer systems and data from unauthorized access or damage"],
        ]),
    },
    "cybersecurity-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["IP address", "A numerical label identifying a device on a network"], ["Port", "A numbered endpoint for network communication"],
        ]),
    },
    "cybersecurity-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Firewall", "A system that filters incoming and outgoing network traffic"],
        ]),
    },
    "cybersecurity-c1-l5": {
        "data_table": table(["Practice", "Reason"], [
            ["Use unique, long passwords", "Makes accounts harder to guess or crack"],
        ]),
    },
    "cybersecurity-c1-l6": {
        "data_table": table(["Tactic", "Example"], [
            ["Pretexting", "Creating a fabricated scenario to gain trust"],
        ]),
    },
    "cybersecurity-c1-l7": {
        "data_table": table(["Warning Sign", "Detail"], [
            ["Urgent, threatening language", "Common tactic in phishing emails"],
        ]),
    },
    "cybersecurity-c1-l8": {
        "data_table": table(["Type", "Behavior"], [
            ["Virus", "Attaches to files and spreads when executed"], ["Worm", "Spreads independently across networks"], ["Trojan", "Disguises itself as legitimate software"],
        ]),
    },
    "cybersecurity-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Security policy", "A documented set of rules governing an organization's security practices"],
        ]),
    },
    "cybersecurity-c1-l10": {
        "data_table": table(["Control", "Example"], [
            ["Physical security", "Locks, badges, and surveillance protecting physical access"],
        ]),
    },
    "cybersecurity-c1-l11": {
        "data_table": table(["Model", "Description"], [
            ["Role-based access control", "Access is granted based on job role"],
        ]),
    },
    "cybersecurity-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Symmetric encryption", "Uses the same key to encrypt and decrypt data"],
        ]),
    },
    "cybersecurity-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Asymmetric encryption", "Uses a public key to encrypt and a private key to decrypt"],
        ]),
    },
    "cybersecurity-c1-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["VPN", "Virtual Private Network, encrypts traffic over a public network"],
        ]),
    },
    "cybersecurity-c1-l15": {
        "data_table": table(["Protocol", "Security Level"], [
            ["WPA3", "Current strongest Wi-Fi security standard"], ["WEP", "Outdated, easily broken"],
        ]),
    },
    "cybersecurity-c1-l16": {
        "data_table": table(["Goal", "Benefit"], [
            ["Security awareness training", "Reduces human error, a leading cause of breaches"],
        ]),
    },
    "cybersecurity-c1-l17": {
        "data_table": table(["Practice", "Reason"], [
            ["Regular backups", "Enables recovery after data loss or ransomware"],
        ]),
    },
    "cybersecurity-c1-l18": {
        "data_table": table(["Framework", "Purpose"], [
            ["NIST Cybersecurity Framework", "Provides guidelines to identify, protect, detect, respond, and recover"],
        ]),
    },
    "cybersecurity-c1-l19": {
        "data_table": table(["Level", "Example"], [
            ["Public", "Marketing materials"], ["Confidential", "Customer financial data"],
        ]),
    },
    "cybersecurity-c1-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Report promptly", "Limits damage and enables faster response"],
        ]),
    },
    "cybersecurity-c1-l21": {
        "data_table": table(["Actor", "Motivation"], [
            ["Cybercriminal", "Financial gain"], ["Hacktivist", "Political or social cause"], ["Nation-state", "Espionage or sabotage"],
        ]),
    },
    "cybersecurity-c1-l22": {
        "data_table": table(["Stage", "Description"], [
            ["Reconnaissance", "Gathering information about the target"], ["Exploitation", "Executing the attack"],
        ]),
    },
    "cybersecurity-c1-l23": {
        "data_table": table(["Port", "Protocol"], [
            ["80", "HTTP"], ["443", "HTTPS"], ["22", "SSH"],
        ]),
    },
    "cybersecurity-c1-l24": {
        "data_table": table(["Layer", "Function"], [
            ["Network layer", "Routing data between devices"], ["Application layer", "Interfaces with software applications"],
        ]),
    },
    "cybersecurity-c1-l25": {
        "data_table": table(["Factor", "Example"], [
            ["Something you know", "Password"], ["Something you have", "Security token"], ["Something you are", "Fingerprint"],
        ]),
    },
    "cybersecurity-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["MFA", "Multi-Factor Authentication, combines two or more authentication factors"],
        ]),
    },
    "cybersecurity-c1-l27": {
        "data_table": table(["Step", "Purpose"], [
            ["Identify assets", "Determines what needs protection"], ["Assess likelihood and impact", "Prioritizes risks"],
        ]),
    },
    "cybersecurity-c1-l28": {
        "data_table": table(["Step", "Purpose"], [
            ["Scan for vulnerabilities", "Identifies weaknesses before attackers do"], ["Patch", "Fixes known vulnerabilities"],
        ]),
    },
    "cybersecurity-c1-l29": {
        "data_table": table(["Regulation", "Focus"], [
            ["GDPR", "EU data privacy law"], ["HIPAA", "US healthcare data privacy"],
        ]),
    },
    "cybersecurity-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Dark web", "Encrypted part of the internet not indexed by standard search engines"],
        ]),
    },
    "cybersecurity-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["DoS attack", "Floods a system with traffic to disrupt service"], ["DDoS", "A DoS attack from multiple sources"],
        ]),
    },
    "cybersecurity-c1-l32": {
        "data_table": table(["Term", "Prevention"], [
            ["SQL injection", "Inserting malicious SQL through input fields; prevent with parameterized queries"],
        ]),
    },
    "cybersecurity-c1-l33": {
        "data_table": table(["Term", "Prevention"], [
            ["XSS", "Injecting malicious scripts into webpages; prevent by escaping user input"],
        ]),
    },
    "cybersecurity-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Man-in-the-middle attack", "An attacker intercepts communication between two parties"],
        ]),
    },
    "cybersecurity-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Ransomware", "Malware that encrypts files and demands payment for the decryption key"],
        ]),
    },
    "cybersecurity-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Botnet", "A network of infected devices controlled remotely by an attacker"],
        ]),
    },
    "cybersecurity-c1-l37": {
        "data_table": table(["Practice", "Reason"], [
            ["Enable device encryption", "Protects data if a mobile device is lost or stolen"],
        ]),
    },
    "cybersecurity-c1-l38": {
        "data_table": table(["Concept", "Meaning"], [
            ["Shared responsibility model", "Cloud provider and customer each secure different parts of the system"],
        ]),
    },
    "cybersecurity-c1-l39": {
        "data_table": table(["Purpose", "Benefit"], [
            ["Security audit", "Independently verifies that controls are working as intended"],
        ]),
    },
    "cybersecurity-c1-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital forensics", "Investigating digital evidence after a security incident"],
        ]),
    },
    "cybersecurity-c1-l41": {
        "data_table": table(["Practice", "Reason"], [
            ["Verify sender before clicking links", "Reduces risk of phishing compromise"],
        ]),
    },
    "cybersecurity-c1-l42": {
        "data_table": table(["Challenge", "Detail"], [
            ["Weak default credentials", "A common IoT security weakness"],
        ]),
    },
    "cybersecurity-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["IAM", "Identity and Access Management, controls who can access what resources"],
        ]),
    },
    "cybersecurity-c1-l44": {
        "data_table": table(["Principle", "Meaning"], [
            ["Least privilege", "Users get only the access necessary for their role"],
        ]),
    },
    "cybersecurity-c1-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Data loss prevention", "Tools and policies that stop sensitive data from leaving an organization"],
        ]),
    },
    "cybersecurity-c1-l46": {
        "data_table": table(["Metric", "Measures"], [
            ["Mean time to detect", "How quickly a threat is identified"],
        ]),
    },
    "cybersecurity-c1-l47": {
        "data_table": table(["Practice", "Reason"], [
            ["Input validation", "Prevents malicious data from being processed by an application"],
        ]),
    },
    "cybersecurity-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Insider threat", "A security risk originating from within an organization"],
        ]),
    },
    "cybersecurity-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Business continuity plan", "Ensures critical operations continue during a disruption"],
        ]),
    },
    "cybersecurity-c1-l50": {
        "data_table": table(["Certification", "Focus"], [
            ["CompTIA Security+", "Foundational cybersecurity knowledge"], ["CISSP", "Advanced security management"],
        ]),
    },
    "cybersecurity-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Steganography", "Hiding data within another file, like an image, so it's not obviously visible"],
        ]),
    },
    "cybersecurity-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Session hijacking", "Taking over a valid user session to gain unauthorized access"],
        ]),
    },
    "cybersecurity-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Zero-day vulnerability", "A flaw unknown to the vendor with no patch available yet"],
        ]),
    },
    "cybersecurity-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Hardware security key", "A physical device used as a strong authentication factor"],
        ]),
    },
    "cybersecurity-c1-l55": {
        "data_table": table(["Practice", "Reason"], [
            ["Checking sender addresses carefully", "Catches spoofed email domains"],
        ]),
    },
    "cybersecurity-c1-l56": {
        "data_table": table(["Practice", "Reason"], [
            ["Keeping the browser updated", "Patches known security vulnerabilities"],
        ]),
    },
    "cybersecurity-c1-l57": {
        "data_table": table(["Skill", "Purpose"], [
            ["Clear policy writing", "Ensures staff understand and can follow security rules"],
        ]),
    },
    "cybersecurity-c1-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Threat intelligence", "Information about current and emerging threats used to inform defense"],
        ]),
    },
    "cybersecurity-c1-l59": {
        "data_table": table(["Term", "Meaning"], [
            ["Security culture", "Shared attitudes and behaviors that prioritize security across an organization"],
        ]),
    },
    "cybersecurity-c1-l60": {
        "data_table": table(["Principle", "Meaning"], [
            ["Confidentiality", "Only authorized people can access data"], ["Integrity", "Data is accurate and unaltered"], ["Availability", "Data is accessible when needed"],
        ]),
    },
    "cybersecurity-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Identifying a phishing email", "Spotting red flags in a sample email"],
        ]),
    },
    "cybersecurity-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Tracing a network path", "Following how data travels from client to server"],
        ]),
    },
    "cybersecurity-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Applying the CIA triad", "Evaluating which principle a specific control protects"],
        ]),
    },
    "cybersecurity-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Configuring firewall rules", "Deciding which ports to allow or block for a sample server"],
        ]),
    },
    "cybersecurity-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating password strength", "Comparing weak and strong password examples"],
        ]),
    },
    "cybersecurity-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Spotting social engineering", "Analyzing a suspicious phone call script"],
        ]),
    },
    "cybersecurity-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Reporting a phishing attempt", "Following the correct escalation steps"],
        ]),
    },
    "cybersecurity-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Classifying malware", "Matching a described behavior to virus, worm, or trojan"],
        ]),
    },
    "cybersecurity-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Drafting a security policy", "Writing an acceptable use policy outline"],
        ]),
    },
    "cybersecurity-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Assessing physical security", "Identifying gaps in an office's access controls"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cybersecurity"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Cybersecurity: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Cybersecurity lessons (completing 70/70).")


if __name__ == "__main__":
    main()
