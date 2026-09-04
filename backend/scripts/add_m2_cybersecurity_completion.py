#!/usr/bin/env python3
"""Depth pass, M2 Cybersecurity: fill in real, hand-checked data_table
content for the M2 Cybersecurity lessons not covered by the earlier
breadth-first batch. Brings M2 Cybersecurity to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning applied
cryptography (post-quantum, MPC, ZK proofs), hardware/side-channel
security, binary and software security analysis, adversarial ML,
blockchain security, cloud-native and zero-trust architecture, malware
analysis and digital forensics, OT/IoT/automotive security, network
and PKI security, social engineering and threat hunting, supply chain
security, cyber risk/policy, and authentication technologies;
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_cybersecurity_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Formal verification (cryptography)", "Mathematically proves a cryptographic protocol satisfies its intended security properties"],
    ["Cryptographic protocol", "A structured sequence of message exchanges designed to achieve a security goal like key agreement or authentication"],
])

CHARTS: dict[str, dict] = {
    "cybersecurity-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Advanced threat intelligence", "Systematically collects, analyzes, and disseminates information about active and emerging cyber threats"],
        ["Application", "Informs proactive defense priorities based on adversary tactics, techniques, and procedures actually observed in the wild"],
    ])},
    "cybersecurity-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Cybersecurity capstone", "An applied culminating project demonstrating end-to-end security analysis or defense system design"],
        ["Deliverable", "Typically includes threat modeling, a working proof-of-concept defense or exploit, and rigorous evaluation"],
    ])},
    "cybersecurity-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Provable security", "Establishes a cryptographic scheme's security by formally reducing an attack on it to solving a hard mathematical problem"],
        ["Reduction proof", "Shows that breaking the scheme would imply an efficient algorithm for a problem believed to be computationally hard"],
    ])},
    "cybersecurity-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Lattice-based cryptography", "Builds cryptographic hardness on lattice problems believed resistant to both classical and quantum attacks"],
        ["Post-quantum cryptography", "Designed to remain secure even against an adversary with a large-scale quantum computer"],
    ])},
    "cybersecurity-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Isogeny-based cryptography", "Builds cryptographic hardness on the difficulty of finding maps (isogenies) between elliptic curves"],
        ["Post-quantum construction", "Offers compact key sizes as an alternative post-quantum approach, though historically with more complex security analysis"],
    ])},
    "cybersecurity-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Fully homomorphic encryption", "Allows arbitrary computation directly on encrypted data, producing an encrypted result that decrypts correctly"],
        ["Scheme design", "Balances computational overhead against the range of operations supported on ciphertexts"],
    ])},
    "cybersecurity-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Secure multi-party computation", "Lets multiple parties jointly compute a function over their private inputs without revealing those inputs to each other"],
        ["Protocol design", "Designed against specific adversary assumptions, e.g. semi-honest or actively malicious participants"],
    ])},
    "cybersecurity-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Zero-knowledge proof", "Lets a prover convince a verifier a statement is true without revealing any information beyond its truth"],
        ["zk-SNARK", "A succinct, non-interactive variant whose proofs are small and fast to verify regardless of computation size"],
    ])},
    "cybersecurity-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy", "A mathematical guarantee that a query's output changes negligibly whether or not any single individual's data is included"],
        ["Formal mechanism", "Achieved by adding calibrated noise to query results, with the privacy budget quantifying cumulative privacy loss"],
    ])},
    "cybersecurity-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Side-channel attack", "Extracts secret information from a system's physical implementation rather than a logical flaw"],
        ["Power analysis", "Infers secret key bits by statistically analyzing a device's power consumption during cryptographic operations"],
    ])},
    "cybersecurity-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Electromagnetic emanation analysis", "Extracts secret information by measuring electromagnetic radiation emitted during a device's computation"],
        ["Side-channel risk", "Can succeed even without physical contact, making it a significant threat for embedded and IoT devices"],
    ])},
    "cybersecurity-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Timing attack", "Infers secret information by measuring how long a cryptographic operation takes to execute"],
        ["Implementation vulnerability", "Constant-time implementation practices are required to eliminate secret-dependent timing variation"],
    ])},
    "cybersecurity-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Fault injection attack", "Deliberately induces hardware errors (via voltage, clock glitches, or lasers) to force exploitable incorrect behavior"],
        ["Secure hardware", "Must include fault-detection countermeasures since a single induced error can leak an entire cryptographic key"],
    ])},
    "cybersecurity-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Hardware trojan", "A malicious modification inserted into a chip's design or manufacturing process"],
        ["Supply chain integrity", "Verifying hardware trustworthiness requires securing every stage from design through fabrication and distribution"],
    ])},
    "cybersecurity-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Trusted execution environment", "An isolated, hardware-protected region of a processor that runs code with confidentiality and integrity guarantees"],
        ["Architectural limits", "Remains vulnerable to certain side-channel and speculative-execution style attacks despite hardware isolation"],
    ])},
    "cybersecurity-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Spectre", "A speculative execution vulnerability that tricks a CPU into speculatively accessing and leaking secret data via a side channel"],
        ["Meltdown", "A related vulnerability that breaks the isolation between user applications and the operating system kernel memory"],
    ])},
    "cybersecurity-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Return-oriented programming", "An exploitation technique that chains together existing code fragments (gadgets) to execute arbitrary logic without injecting new code"],
        ["Exploitation approach", "Bypasses defenses like non-executable memory by reusing legitimate code already present in the target program"],
    ])},
    "cybersecurity-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Control-flow integrity", "Restricts a program's indirect control transfers to a precomputed set of legitimate targets"],
        ["Enforcement mechanism", "Prevents attackers from hijacking execution flow via techniques such as return-oriented programming"],
    ])},
    "cybersecurity-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Fuzzing", "Automatically generates diverse inputs to a program to discover crashes and vulnerabilities"],
        ["Binary vulnerability discovery", "Coverage-guided fuzzing prioritizes mutating inputs that reach previously unexplored code paths in a target binary"],
    ])},
    "cybersecurity-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Symbolic execution", "Runs a program with symbolic rather than concrete inputs, collecting path constraints along each explored branch"],
        ["Security analysis", "Solving a path's collected constraints can reveal concrete inputs that trigger a specific vulnerability"],
    ])},
    "cybersecurity-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Concolic testing", "Combines concrete execution with symbolic constraint tracking to guide exploration toward unexecuted paths"],
        ["Hybrid analysis", "Balances the scalability of concrete execution against the completeness of pure symbolic execution"],
    ])},
    "cybersecurity-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Taint analysis", "Tracks how untrusted input data propagates through a program to detect dangerous uses"],
        ["Information flow tracking", "Flags when tainted (attacker-controlled) data reaches a sensitive operation without proper sanitization"],
    ])},
    "cybersecurity-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Language-based information flow security", "Uses a programming language's type system to statically enforce confidentiality and integrity policies"],
        ["Formal guarantee", "Provides compile-time assurance that information cannot flow from secret to public channels in violation of policy"],
    ])},
    "cybersecurity-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Advanced persistent threat", "A sophisticated, sustained intrusion campaign typically attributed to a well-resourced adversary"],
        ["Attribution methodology", "Combines technical indicators, infrastructure analysis, and behavioral patterns to link an intrusion to a specific actor"],
    ])},
    "cybersecurity-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Cyber threat intelligence sharing", "Distributing indicators and analysis of threats across organizations to improve collective defense"],
        ["Sharing standard", "Formats like STIX/TAXII enable structured, machine-readable exchange of threat intelligence between organizations"],
    ])},
    "cybersecurity-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Deception technology", "Deploys decoy systems and data to detect and mislead attackers who interact with them"],
        ["Honeypot", "A deliberately vulnerable-looking system designed to attract and study attacker behavior in a controlled environment"],
    ])},
    "cybersecurity-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Moving target defense", "Continuously changes a system's attack surface (e.g. addresses, configurations) to increase the difficulty of reconnaissance"],
        ["Strategy rationale", "Denies attackers the stable, predictable target environment that traditional static defenses inadvertently provide"],
    ])},
    "cybersecurity-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Adversarial machine learning", "Studies how ML systems can be manipulated by an adversary"],
        ["Evasion attack", "Crafts inputs at inference time specifically designed to cause a trained model to misclassify"],
    ])},
    "cybersecurity-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Data poisoning attack", "An attacker inserts manipulated examples into training data to degrade or control the resulting model's behavior"],
        ["Adversarial ML risk", "Poisoning can be especially dangerous when models are continuously retrained on user-contributed data"],
    ])},
    "cybersecurity-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Model extraction attack", "Reconstructs a functionally similar copy of a proprietary model by querying its API and observing outputs"],
        ["Membership inference attack", "Determines whether a specific data point was part of a model's training set from its output behavior"],
    ])},
    "cybersecurity-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Explainable AI (security)", "Methods that make a security-relevant model's decisions understandable to human analysts"],
        ["Security operations application", "Helps analysts trust, verify, and act on machine-generated alerts more efficiently"],
    ])},
    "cybersecurity-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Graph-based anomaly detection", "Models network entities and their relationships as a graph to identify structurally unusual behavior"],
        ["Network security application", "Can surface coordinated or lateral-movement attacks that appear normal when entities are examined in isolation"],
    ])},
    "cybersecurity-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Byzantine fault tolerance", "A consensus protocol's ability to reach agreement despite arbitrarily faulty or malicious nodes"],
        ["Blockchain consensus security", "Underlies many blockchain systems' resistance to nodes that behave dishonestly or send conflicting messages"],
    ])},
    "cybersecurity-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Smart contract vulnerability", "A coding flaw in blockchain contract logic that an attacker can exploit, such as reentrancy"],
        ["Analysis approach", "Combines manual audit with automated tools to identify vulnerabilities before contract deployment"],
    ])},
    "cybersecurity-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Formal verification of smart contracts", "Mathematically proves a contract's code satisfies its intended specification"],
        ["Benefit", "Catches bugs before costly, often irreversible, deployment on a public blockchain"],
    ])},
    "cybersecurity-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Cross-chain bridge", "A system enabling asset or data transfer between separate blockchain networks"],
        ["Bridge vulnerability", "Bridges have historically been high-value targets due to concentrated custody of locked assets and complex trust assumptions"],
    ])},
    "cybersecurity-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Quantum key distribution", "Uses quantum mechanical properties to establish a shared secret key with detectable eavesdropping"],
        ["Protocol security", "Security relies on physical principles rather than computational hardness assumptions"],
    ])},
    "cybersecurity-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Quantum computing threat", "A sufficiently powerful quantum computer could break widely deployed public-key cryptography via Shor's algorithm"],
        ["Public-key infrastructure risk", "Motivates migration planning for certificate authorities and protocols relying on vulnerable algorithms"],
    ])},
    "cybersecurity-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Cryptographic agility", "Designing systems to support swapping cryptographic algorithms without major architectural changes"],
        ["Migration planning", "Essential for a smooth transition to post-quantum algorithms as current schemes become vulnerable"],
    ])},
    "cybersecurity-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Multi-cloud architecture", "Distributes workloads across multiple cloud providers rather than relying on a single vendor"],
        ["Secure design", "Must consistently enforce security policy across providers with differing native security tooling"],
    ])},
    "cybersecurity-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Container escape", "An exploit that lets a process break out of its container's isolation boundary to affect the host or other containers"],
        ["Isolation weakness", "Arises from shared kernel resources between containers, unlike the stronger isolation of separate virtual machines"],
    ])},
    "cybersecurity-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Kubernetes cluster security", "Encompasses securing the API server, network policies, and workload configurations of a Kubernetes deployment"],
        ["Hardening", "Includes enforcing least-privilege role-based access control and restricting default overly permissive settings"],
    ])},
    "cybersecurity-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Service mesh", "A dedicated infrastructure layer managing service-to-service communication for a microservices system"],
        ["Security architecture", "Can enforce mutual TLS and fine-grained authorization policies uniformly across all services"],
    ])},
    "cybersecurity-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Zero trust architecture", "Assumes no implicit trust based on network location; every access request is explicitly verified"],
        ["Formal model", "Formalizes continuous verification of identity, device posture, and context for every resource access"],
    ])},
    "cybersecurity-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Software-defined perimeter", "Dynamically creates individualized, encrypted network access boundaries per authenticated user or device"],
        ["Implementation", "Hides protected resources from unauthenticated network scanning, unlike traditional perimeter firewalls"],
    ])},
    "cybersecurity-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Malware unpacking", "Reverses obfuscation techniques malware uses to hide its actual code from static analysis"],
        ["Deobfuscation", "Recovers the malware's true logic so analysts can understand its behavior and develop detections"],
    ])},
    "cybersecurity-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Rootkit", "Malware designed to hide its own presence and that of other malicious activity from detection"],
        ["Kernel-level detection", "Requires examining low-level system structures, since rootkits often subvert standard OS reporting mechanisms"],
    ])},
    "cybersecurity-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Ransomware", "Malware that encrypts a victim's data and demands payment for the decryption key"],
        ["Encryption scheme analysis", "Studying the specific cryptographic implementation can sometimes reveal recoverable weaknesses without paying the ransom"],
    ])},
    "cybersecurity-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Botnet", "A network of compromised devices controlled remotely by an attacker"],
        ["Command-and-control infrastructure", "The communication channel a botnet operator uses to issue instructions to infected devices"],
    ])},
    "cybersecurity-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Domain generation algorithm", "Malware technique that algorithmically generates many candidate domain names to evade static blocklists"],
        ["Detection strategy", "Analyzes domain naming patterns and query volumes to flag likely algorithmically generated domains"],
    ])},
    "cybersecurity-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Fast-flux DNS", "Rapidly rotates the IP addresses associated with a malicious domain to evade takedown and blocklisting"],
        ["Detection", "Identifies abnormally high DNS record change rates characteristic of fast-flux infrastructure"],
    ])},
    "cybersecurity-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Digital forensics", "The scientific process of collecting, preserving, and analyzing digital evidence"],
        ["Memory analysis", "Examines a system's volatile memory snapshot to recover running processes, network connections, and injected code"],
    ])},
    "cybersecurity-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Timeline reconstruction", "Assembles a chronological sequence of system events from forensic artifacts"],
        ["Forensic methodology", "Correlates timestamps across multiple evidence sources to build an accurate picture of an incident"],
    ])},
    "cybersecurity-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Anti-forensic technique", "Methods attackers use to hinder forensic investigation, such as log deletion or timestamp manipulation"],
        ["Detection countermeasure", "Forensic tools and practices designed to detect signs that anti-forensic techniques were used"],
    ])},
    "cybersecurity-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Cloud forensics", "Applies digital forensic methodology to evidence residing in cloud infrastructure"],
        ["Multi-tenant challenge", "Shared infrastructure and provider-controlled logging complicate evidence collection compared with on-premises systems"],
    ])},
    "cybersecurity-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Mobile device forensics", "Extracts and analyzes digital evidence from smartphones and tablets"],
        ["iOS and Android architecture", "Each platform's distinct security model and file system structure requires different forensic extraction techniques"],
    ])},
    "cybersecurity-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["IoT firmware reverse engineering", "Analyzes an embedded device's firmware to understand its functionality and find vulnerabilities"],
        ["Approach", "Combines binary analysis with hardware interfacing to extract and disassemble firmware images"],
    ])},
    "cybersecurity-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Industrial control system", "Computer systems that monitor and control physical industrial processes"],
        ["SCADA vulnerability", "Legacy protocols in supervisory control and data acquisition systems often lack modern authentication and encryption"],
    ])},
    "cybersecurity-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Programmable logic controller", "An industrial computer that controls physical machinery based on programmed logic"],
        ["Security hardening", "Requires network segmentation and firmware integrity checks since PLCs often run outdated, unpatched software"],
    ])},
    "cybersecurity-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["CAN bus", "A vehicle's internal communication network connecting electronic control units"],
        ["Automotive vulnerability", "The CAN protocol historically lacks built-in authentication, allowing a compromised component to send forged messages"],
    ])},
    "cybersecurity-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Medical device security", "Protects connected medical devices from compromise that could harm patients or leak sensitive health data"],
        ["Regulatory framework", "Agencies increasingly require manufacturers to demonstrate cybersecurity controls before device approval"],
    ])},
    "cybersecurity-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Satellite cybersecurity", "Protects satellite command, telemetry, and payload systems from unauthorized access or disruption"],
        ["Space system risk", "Legacy satellite systems often have limited ability to receive security patches once deployed in orbit"],
    ])},
    "cybersecurity-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["5G network slicing", "Partitions a physical 5G network into multiple isolated virtual networks for different use cases"],
        ["Security architecture", "Must ensure isolation between slices so a compromise in one slice cannot affect others"],
    ])},
    "cybersecurity-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Software-defined networking", "Separates the network's control plane from its data plane, centralizing routing decisions in software"],
        ["Security vulnerability", "A compromised centralized controller can potentially manipulate traffic across the entire network it manages"],
    ])},
    "cybersecurity-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["BGP hijacking", "An attacker illegitimately announces ownership of IP address ranges, redirecting internet traffic through their network"],
        ["Mitigation", "Route origin validation (RPKI) helps networks verify that BGP announcements come from legitimate address holders"],
    ])},
    "cybersecurity-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["DNSSEC", "Adds cryptographic signatures to DNS records to verify their authenticity and integrity"],
        ["Deployment challenge", "Requires coordinated adoption across the DNS hierarchy, slowing real-world deployment despite security benefits"],
    ])},
    "cybersecurity-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Certificate transparency", "Publicly logs issued TLS certificates so mis-issuance can be detected and audited"],
        ["PKI trust failure", "Addresses historical incidents where certificate authorities issued fraudulent certificates undetected for extended periods"],
    ])},
    "cybersecurity-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Business email compromise", "A social engineering attack impersonating a trusted party to trick an organization into fraudulent payments or data disclosure"],
        ["Advanced phishing tactic", "Often involves careful reconnaissance and highly targeted, context-aware messaging rather than generic phishing"],
    ])},
    "cybersecurity-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Social engineering", "Manipulates human psychology to bypass technical security controls"],
        ["Psychological manipulation framework", "Exploits principles like authority, urgency, and reciprocity to induce compliance with an attacker's request"],
    ])},
    "cybersecurity-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Purple teaming", "Structured collaboration between offensive (red team) and defensive (blue team) security functions"],
        ["Integrating offense and defense", "Aims to translate attack findings directly into improved detection and response capability"],
    ])},
    "cybersecurity-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["MITRE ATT&CK framework", "A structured knowledge base of adversary tactics and techniques observed in real-world intrusions"],
        ["Advanced application", "Used to map defensive coverage, prioritize detection engineering, and structure threat hunting hypotheses"],
    ])},
    "cybersecurity-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Threat hunting", "Proactively searches for signs of undetected compromise rather than waiting for automated alerts"],
        ["Hypothesis testing", "Structured hunts start from a specific hypothesis about likely adversary behavior, then seek confirming or refuting evidence"],
    ])},
    "cybersecurity-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Security orchestration, automation, and response", "Automates repetitive incident response tasks to reduce analyst workload and response time"],
        ["Design", "Coordinates alerts, enrichment, and automated remediation actions across multiple security tools"],
    ])},
    "cybersecurity-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Insider threat", "Risk posed by individuals with authorized access who misuse it maliciously or negligently"],
        ["Behavioral analytics detection", "Establishes a baseline of normal user behavior and flags statistically significant deviations from it"],
    ])},
    "cybersecurity-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Data loss prevention", "Systems that monitor and control the movement of sensitive data to prevent unauthorized exfiltration"],
        ["Architecture", "Combines content inspection with policy enforcement across endpoints, network, and cloud storage"],
    ])},
    "cybersecurity-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Secure software development lifecycle", "Integrates security practices at every stage of the software development process"],
        ["Governance", "Requires organizational policy, training, and tooling to ensure secure practices are consistently followed"],
    ])},
    "cybersecurity-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Software bill of materials", "A comprehensive inventory of components and dependencies included in a piece of software"],
        ["Supply chain risk", "Enables organizations to quickly identify exposure when a vulnerability is disclosed in a widely used component"],
    ])},
    "cybersecurity-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Dependency confusion", "An attack that tricks a build system into pulling a malicious public package instead of an intended internal one"],
        ["Package repository attack", "Exploits naming collisions between internal and public package registries"],
    ])},
    "cybersecurity-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Reproducible build", "A build process that deterministically produces bit-for-bit identical output from the same source, independently verifiable"],
        ["Build provenance verification", "Lets third parties confirm a distributed binary genuinely corresponds to its published source code"],
    ])},
    "cybersecurity-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["FAIR methodology", "Factor Analysis of Information Risk, a quantitative framework for measuring and expressing cyber risk in financial terms"],
        ["Quantitative risk assessment", "Enables comparing security investments against expected loss reduction using a consistent numerical framework"],
    ])},
    "cybersecurity-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Game-theoretic model of cyber conflict", "Analyzes attacker-defender interactions as a strategic game with payoffs and equilibria"],
        ["Application", "Helps predict rational adversary responses to specific defensive investments or postures"],
    ])},
    "cybersecurity-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["National cyber doctrine", "A country's official strategy and stated policy for cyber defense and offense"],
        ["Deterrence theory", "Applies classical deterrence concepts to cyberspace, complicated by challenges in reliable attack attribution"],
    ])},
    "cybersecurity-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Cyber warfare case study", "Detailed analysis of a real-world state-linked cyberattack and its strategic context"],
        ["Critical infrastructure attack", "Attacks on power grids and industrial systems illustrate the potential physical-world consequences of cyber operations"],
    ])},
    "cybersecurity-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["International law and cyber operations", "Examines how existing legal frameworks (armed conflict, sovereignty) apply to state-sponsored cyber activity"],
        ["Open question", "Significant ambiguity remains about when a cyber operation legally constitutes an act of war"],
    ])},
    "cybersecurity-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Privacy-enhancing technology", "Techniques that let organizations gain insight from data while limiting exposure of individual information"],
        ["Secure aggregation", "Computes an aggregate statistic across many parties' data without revealing any individual party's contribution"],
    ])},
    "cybersecurity-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Anonymous communication network", "A system that hides the identity and location of communicating parties from observers"],
        ["Onion routing", "Encrypts traffic in multiple layers routed through several relays, so no single relay knows both the source and destination"],
    ])},
    "cybersecurity-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Traffic analysis", "Infers information about communication content or parties from patterns in network traffic, even when encrypted"],
        ["Deanonymization technique", "Exploits timing or volume patterns to link anonymized traffic back to its originating source"],
    ])},
    "cybersecurity-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Biometric spoofing", "An attack that presents a fake biometric sample (e.g. a photo or mold) to fool an authentication system"],
        ["Liveness detection", "Verifies the biometric sample comes from a live, present individual rather than a static replica"],
    ])},
    "cybersecurity-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Continuous authentication", "Ongoing verification of a user's identity throughout a session, not just at initial login"],
        ["Behavioral biometrics", "Uses patterns like typing rhythm or mouse movement as an ongoing identity signal"],
    ])},
    "cybersecurity-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Post-compromise recovery", "The process of restoring a system to a trustworthy state after a confirmed security breach"],
        ["Clean-state restoration", "Ensures no persistent attacker access remains, since simply removing known malware may leave hidden backdoors"],
    ])},
    "cybersecurity-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Regulatory compliance (cybersecurity)", "Ensures an organization's security practices meet applicable legal and industry requirements"],
        ["Cross-jurisdictional analysis", "Multinational organizations must reconcile potentially conflicting requirements across different countries' regulations"],
    ])},
    "cybersecurity-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Security metrics", "Quantitative measures used to assess and communicate an organization's security posture"],
        ["Maturity model", "A structured framework for benchmarking an organization's security program against progressively advanced capability levels"],
    ])},
    "cybersecurity-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Formal methods for access control", "Uses mathematical models to specify and verify that an access control policy behaves as intended"],
        ["Policy verification", "Can prove properties like the absence of unintended privilege escalation paths before deployment"],
    ])},
    "cybersecurity-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Attribute-based encryption", "Encrypts data such that only users whose attributes satisfy a specified policy can decrypt it"],
        ["Fine-grained access control", "Enables expressive access policies without needing to encrypt separately for each individual recipient"],
    ])},
    "cybersecurity-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Secure enclave", "An isolated, hardware-protected execution environment within a processor"],
        ["Attestation protocol", "Lets an enclave cryptographically prove to a remote party that it is running genuine, unmodified code"],
    ])},
    "cybersecurity-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Quantum-safe TLS migration", "Transitioning Transport Layer Security deployments to use post-quantum cryptographic algorithms"],
        ["Migration challenge", "Requires balancing larger post-quantum key and signature sizes against performance and compatibility constraints"],
    ])},
    "cybersecurity-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Doctoral thesis seminar", "A capstone forum for presenting and defending an original contribution to cybersecurity research"],
        ["Original contribution", "Requires identifying a genuine gap in existing security methods and offering a novel, rigorously evaluated resolution"],
    ])},
    "cybersecurity-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Voice deepfake", "AI-synthesized audio that convincingly mimics a specific person's voice"],
        ["Vishing mitigation", "Detection methods analyze subtle acoustic artifacts to distinguish synthesized speech from genuine human voice calls"],
    ])},
    "cybersecurity-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["FIDO2/WebAuthn", "A passwordless authentication standard using public-key cryptography and phishing-resistant hardware or platform authenticators"],
        ["Security analysis", "Eliminates password-related attack vectors like credential stuffing and phishing that steal shared secrets"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cybersecurity"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"cybersecurity-m2-l{base_n}"
        worked_key = f"cybersecurity-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Cybersecurity lessons.")


if __name__ == "__main__":
    main()
