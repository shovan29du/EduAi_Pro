#!/usr/bin/env python3
"""Depth pass, M1 Cybersecurity: fill in real, hand-checked
data_table content for the 119 M1 Cybersecurity lessons not covered
by the earlier breadth-first batch. Brings M1 Cybersecurity to full
120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning offensive
security, forensics, cryptography, threat intelligence, infrastructure
hardening, and security governance; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_cybersecurity_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Zero-knowledge proof", "Proving a statement is true without revealing the underlying information"],
    ["Prover", "The party proving a claim"],
    ["Verifier", "The party checking the proof"],
])

CHARTS: dict[str, dict] = {
    "cybersecurity-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Digital forensics", "Recovers and analyzes digital evidence for investigation"],
    ])},
    "cybersecurity-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Vulnerability management", "Continuously identifies, prioritizes, and remediates security weaknesses"],
    ])},
    "cybersecurity-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Post-quantum cryptography", "Cryptographic algorithms believed resistant to attacks by future quantum computers"],
    ])},
    "cybersecurity-m1-l5": {"data_table": table(["Framework", "Focus"], [
        ["STRIDE", "Categorizes threats as Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation"],
        ["PASTA", "A risk-centric, business-aligned threat modeling process"],
    ])},
    "cybersecurity-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Malware reverse engineering", "Disassembles malicious code to understand its behavior and origin"],
    ])},
    "cybersecurity-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Anti-forensics", "Techniques attackers use to hide or destroy evidence of their activity"],
    ])},
    "cybersecurity-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Cyber threat intelligence", "Analyzes data on adversary tactics to inform proactive defense"],
    ])},
    "cybersecurity-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["SOC automation", "Uses automated tooling to speed up detection and response in a security operations center"],
    ])},
    "cybersecurity-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Adversarial machine learning", "Studies how attackers manipulate ML models used in security systems"],
    ])},
    "cybersecurity-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Critical infrastructure security", "Protects power, water, and other essential systems from cyberattack"],
    ])},
    "cybersecurity-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["ICS/SCADA security", "Protects industrial control systems that manage physical processes"],
    ])},
    "cybersecurity-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Cloud-native security", "Secures applications built using containers, microservices, and managed cloud services"],
    ])},
    "cybersecurity-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Identity and access governance", "Manages who has access to what, and ensures it stays appropriate over time"],
    ])},
    "cybersecurity-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Risk quantification", "Expresses cybersecurity risk in measurable, often monetary, terms"],
    ])},
    "cybersecurity-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Incident response leadership", "Coordinates people and process during a major security incident"],
    ])},
    "cybersecurity-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Cybersecurity policy", "National and international rules and norms governing cyberspace behavior"],
    ])},
    "cybersecurity-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Cyber warfare", "State-sponsored or nation-state cyberattacks used as a tool of conflict"],
    ])},
    "cybersecurity-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Responsible disclosure", "Reports discovered vulnerabilities privately to vendors before public release"],
    ])},
    "cybersecurity-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Enterprise security program", "Integrates policy, technology, and people into one organization-wide security posture"],
    ])},
    "cybersecurity-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Coverage-guided fuzzing", "Mutates inputs guided by code coverage to find new program paths and bugs"],
    ])},
    "cybersecurity-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Return-oriented programming", "Chains existing code fragments to execute malicious logic despite non-executable memory"],
    ])},
    "cybersecurity-m1-l23": {"data_table": table(["Defense", "Purpose"], [
        ["Stack canary", "Detects buffer overflow by checking a sentinel value before returning"],
        ["ASLR", "Randomizes memory addresses to make exploitation harder"],
    ])},
    "cybersecurity-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Kernel exploitation", "Attacks the operating system kernel to gain the highest level of system privilege"],
    ])},
    "cybersecurity-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["SSRF", "Tricks a server into making unauthorized requests to internal or external systems"],
    ])},
    "cybersecurity-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["GraphQL security", "Addresses risks like query depth abuse and over-permissive introspection in GraphQL APIs"],
    ])},
    "cybersecurity-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Blind SQL injection", "Extracts database information via true/false or timing responses when output isn't directly visible"],
    ])},
    "cybersecurity-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Container escape", "Breaks out of a container's isolation to access the host system"],
    ])},
    "cybersecurity-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Kubernetes hardening", "Applies pod security standards to reduce a cluster's attack surface"],
    ])},
    "cybersecurity-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Zeek", "An open-source network security monitor that analyzes traffic for anomalies"],
    ])},
    "cybersecurity-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Deep packet inspection", "Examines the content of network packets, not just headers, for threats"],
    ])},
    "cybersecurity-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["DNSSEC", "Cryptographically signs DNS records to prevent spoofing and tampering"],
    ])},
    "cybersecurity-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["BGP hijacking", "Maliciously reroutes internet traffic by announcing false routing information"],
    ])},
    "cybersecurity-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["WPA3 attacks", "Exploits weaknesses in the latest Wi-Fi security protocol"],
    ])},
    "cybersecurity-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Bluetooth/IoT exploitation", "Attacks vulnerabilities in wireless protocols used by connected devices"],
    ])},
    "cybersecurity-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Firmware reverse engineering", "Analyzes embedded device software to find vulnerabilities or backdoors"],
    ])},
    "cybersecurity-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Hardware security module / TPM", "Dedicated hardware that securely generates and stores cryptographic keys"],
    ])},
    "cybersecurity-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Side-channel attack", "Extracts secrets by measuring physical signals like timing or power use"],
    ])},
    "cybersecurity-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Fault injection attack", "Deliberately induces hardware errors to bypass security checks"],
    ])},
    "cybersecurity-m1-l40": {"data_table": table(["Method", "Feature"], [
        ["Differential cryptanalysis", "Studies how input differences affect output differences"],
        ["Linear cryptanalysis", "Finds linear approximations of a cipher's behavior"],
    ])},
    "cybersecurity-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Homomorphic encryption", "Allows computation directly on encrypted data without decrypting it"],
    ])},
    "cybersecurity-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Secure multi-party computation", "Lets multiple parties jointly compute a result without revealing their private inputs"],
    ])},
    "cybersecurity-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Public key infrastructure", "Issues and manages digital certificates that bind identities to public keys"],
    ])},
    "cybersecurity-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Certificate transparency", "Publicly logs issued certificates to detect misissuance"],
    ])},
    "cybersecurity-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Ransomware analysis", "Studies how ransomware encrypts and spreads to inform recovery strategy"],
    ])},
    "cybersecurity-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["SBOM", "A software bill of materials listing all components in an application for supply chain security"],
    ])},
    "cybersecurity-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Software composition analysis", "Scans dependencies for known vulnerabilities"],
    ])},
    "cybersecurity-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["ML-based phishing detection", "Uses machine learning to identify phishing emails and sites"],
    ])},
    "cybersecurity-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Business email compromise", "Investigates fraud where attackers impersonate executives to redirect funds"],
    ])},
    "cybersecurity-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Vishing", "Voice-based social engineering used to manipulate victims into revealing information"],
    ])},
    "cybersecurity-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["User and entity behavior analytics", "Detects anomalies by modeling normal user and system behavior"],
    ])},
    "cybersecurity-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["SIEM correlation rules", "Combine multiple log events to detect complex attack patterns"],
    ])},
    "cybersecurity-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Threat hunting", "Proactively searches for undetected threats rather than waiting for alerts"],
    ])},
    "cybersecurity-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["MITRE ATT&CK", "A knowledge base of adversary tactics and techniques used to structure defense"],
    ])},
    "cybersecurity-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Purple teaming", "Coordinates offensive (red) and defensive (blue) teams to improve detection together"],
    ])},
    "cybersecurity-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Penetration testing methodology", "A structured process for legally simulating attacks to find weaknesses"],
    ])},
    "cybersecurity-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["BloodHound", "Maps Active Directory attack paths by analyzing relationships between accounts and permissions"],
    ])},
    "cybersecurity-m1-l58": {"data_table": table(["Attack", "Target"], [
        ["Kerberoasting", "Extracts service account credentials via Kerberos ticket requests"],
        ["Golden ticket", "Forges Kerberos tickets after compromising the domain's key"],
    ])},
    "cybersecurity-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["EDR evasion", "Techniques attackers use to avoid detection by endpoint detection and response tools"],
    ])},
    "cybersecurity-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Living-off-the-land", "Attackers abuse legitimate system binaries to avoid deploying detectable malware"],
    ])},
    "cybersecurity-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Memory forensics (Volatility)", "Analyzes a system's RAM snapshot to recover evidence of malicious activity"],
    ])},
    "cybersecurity-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Anti-debugging", "Techniques malware uses to detect and resist analysis tools"],
    ])},
    "cybersecurity-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Rootkit detection", "Identifies malware that hides itself by manipulating kernel-level integrity"],
    ])},
    "cybersecurity-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Botnet C2 infrastructure", "Analyzes the command-and-control servers that coordinate compromised devices"],
    ])},
    "cybersecurity-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["DDoS mitigation architecture", "Absorbs or filters distributed denial-of-service traffic before it disrupts a service"],
    ])},
    "cybersecurity-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Zero trust implementation", "Continuously verifies every request instead of trusting an internal network perimeter"],
    ])},
    "cybersecurity-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Micro-segmentation", "Divides a network into small isolated zones to limit lateral attacker movement"],
    ])},
    "cybersecurity-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Shift-left security", "Integrates security checks earlier in the CI/CD development pipeline"],
    ])},
    "cybersecurity-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["IaC security scanning", "Checks infrastructure-as-code templates for misconfigurations before deployment"],
    ])},
    "cybersecurity-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Container image signing", "Cryptographically verifies that a container image hasn't been tampered with"],
    ])},
    "cybersecurity-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Confidential computing", "Processes data in a hardware-isolated trusted execution environment"],
    ])},
    "cybersecurity-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Smart contract vulnerability analysis", "Audits blockchain code for exploitable logic flaws"],
    ])},
    "cybersecurity-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Cryptocurrency forensics", "Traces transactions across a blockchain to link addresses to real activity"],
    ])},
    "cybersecurity-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Digital rights management", "Restricts unauthorized copying or use of digital content"],
    ])},
    "cybersecurity-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Data loss prevention", "Detects and blocks unauthorized transfer of sensitive data"],
    ])},
    "cybersecurity-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy", "Adds calibrated noise so individual records cannot be reverse-engineered"],
    ])},
    "cybersecurity-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["GDPR technical compliance", "Implements systems that enforce data subject rights and retention rules"],
    ])},
    "cybersecurity-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["STIX/TAXII", "Standardized formats and protocols for sharing cyber threat intelligence"],
    ])},
    "cybersecurity-m1-l79": {"data_table": table(["Metric", "Purpose"], [
        ["CVSS", "Scores a vulnerability's technical severity"],
        ["EPSS", "Estimates the probability a vulnerability will actually be exploited"],
    ])},
    "cybersecurity-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Bug bounty triage", "Reviews and validates externally reported vulnerabilities for reward and remediation"],
    ])},
    "cybersecurity-m1-l81": {"data_table": table(["Method", "Feature"], [
        ["SAST", "Analyzes source code for vulnerabilities without running it"],
        ["DAST", "Tests a running application from the outside for vulnerabilities"],
    ])},
    "cybersecurity-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Secure SDLC metrics", "Measures how well security is integrated throughout the development lifecycle"],
    ])},
    "cybersecurity-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["SAML / OIDC attack surface", "Federated identity protocols that can be exploited if improperly configured"],
    ])},
    "cybersecurity-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["FIDO2/WebAuthn", "Enables passwordless authentication using public-key cryptography"],
    ])},
    "cybersecurity-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["MFA bypass techniques", "Methods attackers use to circumvent multi-factor authentication protections"],
    ])},
    "cybersecurity-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Cloud security posture management", "Continuously monitors cloud environments for misconfigurations"],
    ])},
    "cybersecurity-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Serverless security", "Addresses unique risks in functions-as-a-service architectures"],
    ])},
    "cybersecurity-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["API gateway security", "Enforces authentication, throttling, and validation at the API entry point"],
    ])},
    "cybersecurity-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Security chaos engineering", "Deliberately injects failures to test a system's security resilience"],
    ])},
    "cybersecurity-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["SOAR playbook", "Automates a standardized incident response sequence across security tools"],
    ])},
    "cybersecurity-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Chain of custody", "Documents every handling step of digital evidence to preserve its legal admissibility"],
    ])},
    "cybersecurity-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Mobile application security", "Protects mobile apps from reverse engineering, tampering, and data leakage"],
    ])},
    "cybersecurity-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["BYOD security", "Manages the risk of personal devices accessing corporate resources"],
    ])},
    "cybersecurity-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Satellite/space cybersecurity", "Protects space-based systems and their ground infrastructure from attack"],
    ])},
    "cybersecurity-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Connected vehicle security", "Protects automotive systems from remote and physical cyberattacks"],
    ])},
    "cybersecurity-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Medical device cybersecurity", "Secures connected medical devices against attacks that could endanger patients"],
    ])},
    "cybersecurity-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Cross-sector threat intelligence sharing", "Coordinates threat information exchange across industries"],
    ])},
    "cybersecurity-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Cyber insurance risk modeling", "Estimates likely losses from cyber incidents to price insurance policies"],
    ])},
    "cybersecurity-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Board-level security reporting", "Communicates cybersecurity risk in business terms for executive decision-making"],
    ])},
    "cybersecurity-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Sigstore/Cosign", "Cryptographically signs and verifies container images to confirm their origin"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"cybersecurity-m1-l{base_n}"
    worked_key = f"cybersecurity-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cybersecurity"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Cybersecurity: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Cybersecurity lessons (completing 120/120).")


if __name__ == "__main__":
    main()
