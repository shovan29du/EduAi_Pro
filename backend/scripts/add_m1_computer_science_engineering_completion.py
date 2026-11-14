#!/usr/bin/env python3
"""Depth pass, M1 Computer Science Engineering: fill in real,
hand-checked data_table content for the 119 M1 Computer Science
Engineering lessons not covered by the earlier breadth-first batch.
Brings M1 Computer Science Engineering to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
computer architecture, operating systems and distributed systems,
hardware security, embedded/cyber-physical systems, and emerging
computing paradigms (quantum, neuromorphic); l101-l120 are "Worked
Analysis" companions reusing the data_table of l1-l20 (direct 1:1
mapping). l3 was already completed by an earlier breadth-first batch,
so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_computer_science_engineering_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Encryption", "Transforms readable data into unreadable form using a key"],
    ["Hashing", "One-way transformation used to verify integrity, not to be reversed"],
])

CHARTS: dict[str, dict] = {
    "computer-science-engineering-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Computer security fundamentals", "Protects the confidentiality, integrity, and availability of computer systems"],
    ])},
    "computer-science-engineering-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Embedded system", "A computer built into a device to perform a dedicated function"],
    ])},
    "computer-science-engineering-m1-l4": {"data_table": table(["Type", "Feature"], [
        ["Symmetric encryption", "Same key encrypts and decrypts, fast but requires secure key sharing"],
        ["Asymmetric encryption", "Public/private key pair, slower but avoids key-sharing problem"],
    ])},
    "computer-science-engineering-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Access control model", "Defines rules for who can perform which actions on which resources"],
    ])},
    "computer-science-engineering-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Network attack vector", "A specific method attackers use to gain unauthorized network access"],
    ])},
    "computer-science-engineering-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Secure software development", "Builds security checks into every stage of the development lifecycle"],
    ])},
    "computer-science-engineering-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Embedded systems programming", "Writes resource-constrained code that interacts directly with hardware"],
    ])},
    "computer-science-engineering-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["RTOS", "Real-Time Operating System; guarantees tasks complete within strict timing deadlines"],
    ])},
    "computer-science-engineering-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Microcontroller architecture", "A compact chip combining a processor, memory, and I/O for embedded control"],
    ])},
    "computer-science-engineering-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Sensor interfacing / IoT", "Connects physical-world sensors to embedded systems and networks"],
    ])},
    "computer-science-engineering-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Parallel computing architecture", "Executes multiple computations simultaneously across processing units"],
    ])},
    "computer-science-engineering-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Concurrent programming model", "Structures a program to correctly manage multiple simultaneous execution paths"],
    ])},
    "computer-science-engineering-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["CUDA", "NVIDIA's platform for writing programs that run on GPU cores"],
    ])},
    "computer-science-engineering-m1-l15": {"data_table": table(["Level", "Scope"], [
        ["Unit test", "Tests a single function or component in isolation"],
        ["Integration test", "Tests how components work together"],
        ["System test", "Tests the entire assembled system"],
    ])},
    "computer-science-engineering-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Test automation framework", "Runs test suites automatically as part of the development workflow"],
    ])},
    "computer-science-engineering-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Scalable system design", "Structures a system to handle growing load through horizontal or vertical scaling"],
    ])},
    "computer-science-engineering-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["System design interview", "Evaluates a candidate's ability to design large-scale systems under constraints"],
    ])},
    "computer-science-engineering-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Professional ethics in engineering", "Standards guiding responsible conduct in engineering practice"],
    ])},
    "computer-science-engineering-m1-l20": {"data_table": table(["Trend", "Detail"], [
        ["Emerging CS engineering trends", "Includes hardware-software co-design, quantum computing, and AI accelerators"],
    ])},
    "computer-science-engineering-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Out-of-order execution", "Executes instructions as operands become ready rather than strictly in program order"],
    ])},
    "computer-science-engineering-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Branch prediction", "Guesses the outcome of a conditional branch to keep the pipeline full"],
    ])},
    "computer-science-engineering-m1-l23": {"data_table": table(["Protocol", "Feature"], [
        ["MESI", "Tracks cache line state (Modified, Exclusive, Shared, Invalid) to keep caches coherent"],
    ])},
    "computer-science-engineering-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Multi-level cache", "Uses progressively larger, slower cache tiers to balance speed and capacity"],
    ])},
    "computer-science-engineering-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Superscalar design", "Issues and executes multiple instructions per clock cycle"],
    ])},
    "computer-science-engineering-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["SIMD", "Single Instruction, Multiple Data; applies one operation across many data elements at once"],
    ])},
    "computer-science-engineering-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Network-on-chip", "An on-chip communication fabric connecting cores in a multicore processor"],
    ])},
    "computer-science-engineering-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["FPGA", "A reconfigurable chip whose logic can be reprogrammed after manufacturing"],
    ])},
    "computer-science-engineering-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["ASIC design flow", "The process of designing a chip customized for one specific application"],
    ])},
    "computer-science-engineering-m1-l30": {"data_table": table(["Language", "Purpose"], [
        ["Verilog / VHDL", "Describe digital hardware circuit behavior for simulation and synthesis"],
    ])},
    "computer-science-engineering-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Formal hardware verification", "Mathematically proves a hardware design meets its specification"],
    ])},
    "computer-science-engineering-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Power-aware architecture", "Designs processors to minimize energy consumption alongside performance"],
    ])},
    "computer-science-engineering-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Dark silicon", "The growing fraction of a chip that can't be powered simultaneously due to heat limits"],
    ])},
    "computer-science-engineering-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Processing-in-memory", "Performs computation directly within or near memory to reduce data movement"],
    ])},
    "computer-science-engineering-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["ML accelerator", "Hardware custom-designed to speed up machine learning computation"],
    ])},
    "computer-science-engineering-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Multi-level feedback queue", "A scheduling algorithm that adjusts process priority based on observed behavior"],
    ])},
    "computer-science-engineering-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Page replacement algorithm", "Decides which memory page to evict when physical memory is full"],
    ])},
    "computer-science-engineering-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Journaling file system", "Logs pending changes before applying them to recover cleanly after a crash"],
    ])},
    "computer-science-engineering-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Distributed file system", "Stores and replicates files across many machines, balancing consistency and availability"],
    ])},
    "computer-science-engineering-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["RTOS scheduling guarantee", "Provably meets task deadlines under defined worst-case conditions"],
    ])},
    "computer-science-engineering-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Device driver", "Software that lets the OS communicate with a specific hardware device"],
    ])},
    "computer-science-engineering-m1-l42": {"data_table": table(["Kernel", "Feature"], [
        ["Microkernel", "Minimal core, most services run in user space"],
        ["Monolithic kernel", "Most services run in kernel space for speed"],
    ])},
    "computer-science-engineering-m1-l43": {"data_table": table(["Mechanism", "Feature"], [
        ["Container", "Shares the host OS kernel, lightweight isolation"],
        ["Virtual machine", "Emulates full hardware, stronger isolation"],
    ])},
    "computer-science-engineering-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["TCP congestion control", "Adjusts sending rate to avoid overwhelming the network"],
    ])},
    "computer-science-engineering-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["SDN control plane", "Centralizes network routing decisions in software separate from the hardware forwarding"],
    ])},
    "computer-science-engineering-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Medium access control", "Coordinates how devices share a wireless network's radio spectrum"],
    ])},
    "computer-science-engineering-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Network function virtualization", "Runs network services like firewalls as software instead of dedicated hardware"],
    ])},
    "computer-science-engineering-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Replication protocol", "Keeps multiple copies of data consistent to tolerate node failures"],
    ])},
    "computer-science-engineering-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Byzantine fault tolerance", "Keeps a system correct even if some nodes behave arbitrarily or maliciously"],
    ])},
    "computer-science-engineering-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Distributed hash table", "Distributes key-value lookups across peer nodes without central coordination"],
    ])},
    "computer-science-engineering-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Zero-knowledge proof", "Proving a statement is true without revealing the underlying information"],
    ])},
    "computer-science-engineering-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Post-quantum cryptography", "Cryptographic algorithms believed resistant to attacks by future quantum computers"],
    ])},
    "computer-science-engineering-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Side-channel attack", "Extracts secrets by measuring physical signals like timing or power use"],
    ])},
    "computer-science-engineering-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["HSM / TPM", "Dedicated hardware that securely generates and stores cryptographic keys"],
    ])},
    "computer-science-engineering-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Secure boot", "Verifies each stage of startup software before allowing it to run"],
    ])},
    "computer-science-engineering-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Return-oriented programming", "Chains existing code fragments to execute malicious logic despite non-executable memory"],
    ])},
    "computer-science-engineering-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Firmware fuzzing", "Feeds embedded firmware random or malformed input to discover vulnerabilities"],
    ])},
    "computer-science-engineering-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Hardware Trojan", "A malicious modification inserted into a chip's design or manufacturing"],
    ])},
    "computer-science-engineering-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Cyber-physical system safety", "Uses formal methods to verify systems that interact directly with the physical world"],
    ])},
    "computer-science-engineering-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Sensor fusion", "Combines data from multiple sensors for a more reliable perception estimate"],
    ])},
    "computer-science-engineering-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Real-time control system", "Computes control actions within strict timing deadlines for robotics"],
    ])},
    "computer-science-engineering-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Low-power embedded design", "Minimizes energy use to extend battery life in embedded devices"],
    ])},
    "computer-science-engineering-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Wireless sensor network routing", "Moves data efficiently across a network of battery-powered sensor nodes"],
    ])},
    "computer-science-engineering-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Digital signal processing", "Manipulates sampled signals mathematically for embedded applications"],
    ])},
    "computer-science-engineering-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Hardware-software co-design", "Jointly designs hardware and software to optimize a system together"],
    ])},
    "computer-science-engineering-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["System-on-chip integration", "Combines multiple functional blocks onto a single chip"],
    ])},
    "computer-science-engineering-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Formal protocol specification", "Mathematically defines a communication protocol's expected behavior"],
    ])},
    "computer-science-engineering-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Qubit error correction", "Protects fragile quantum information from noise and decoherence"],
    ])},
    "computer-science-engineering-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Gate decomposition", "Breaks a complex quantum operation into a sequence of basic quantum gates"],
    ])},
    "computer-science-engineering-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Neuromorphic hardware", "Chips designed to mimic the brain's spiking neural computation"],
    ])},
    "computer-science-engineering-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Approximate computing", "Trades small accuracy losses for large gains in energy efficiency"],
    ])},
    "computer-science-engineering-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Heterogeneous compiler design", "Targets code generation across mixed CPU/GPU/accelerator hardware"],
    ])},
    "computer-science-engineering-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Distributed-memory parallel algorithm", "Designs algorithms where processors communicate explicitly, without shared memory"],
    ])},
    "computer-science-engineering-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["GPU memory hierarchy", "Balances fast but small on-chip memory against slower but larger global memory"],
    ])},
    "computer-science-engineering-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["HPC interconnect", "High-speed networking connecting nodes in a supercomputing cluster"],
    ])},
    "computer-science-engineering-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Fault-tolerant computing", "Keeps mission-critical systems operating correctly despite component failures"],
    ])},
    "computer-science-engineering-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Safety-critical software verification", "Formally proves software meets its safety requirements before deployment"],
    ])},
    "computer-science-engineering-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Model-based systems engineering", "Uses formal models rather than documents to design complex systems"],
    ])},
    "computer-science-engineering-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Digital twin", "A virtual model of a physical system used to simulate and monitor its real-world performance"],
    ])},
    "computer-science-engineering-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Vision hardware acceleration", "Custom hardware that speeds up image and video processing computations"],
    ])},
    "computer-science-engineering-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Autonomous system safety certification", "Formal frameworks for certifying self-driving and robotic systems are safe"],
    ])},
    "computer-science-engineering-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Blockchain consensus mechanism", "The protocol nodes use to agree on the valid state of a shared ledger"],
    ])},
    "computer-science-engineering-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Smart contract vulnerability", "A code flaw in a blockchain contract that can be exploited"],
    ])},
    "computer-science-engineering-m1-l84": {"data_table": table(["Topology", "Feature"], [
        ["Fat-tree", "A common data center topology providing high bisection bandwidth"],
        ["Clos", "A multi-stage switching topology minimizing blocking"],
    ])},
    "computer-science-engineering-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Software-defined storage", "Decouples storage management from underlying hardware, controlled by software"],
    ])},
    "computer-science-engineering-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Edge computing", "Processes data near its source to reduce latency for time-sensitive applications"],
    ])},
    "computer-science-engineering-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Time-sensitive networking", "Guarantees deterministic, low-latency delivery for industrial control traffic"],
    ])},
    "computer-science-engineering-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Formal threat modeling", "Systematically identifies and analyzes potential threats to a system's design"],
    ])},
    "computer-science-engineering-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Hardware-assisted virtualization", "Uses CPU features to run virtual machines with near-native performance"],
    ])},
    "computer-science-engineering-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Memory safety enforcement", "Language or hardware mechanisms that prevent out-of-bounds memory access bugs"],
    ])},
    "computer-science-engineering-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Capability-based security", "Grants access via unforgeable tokens rather than identity-based permission checks"],
    ])},
    "computer-science-engineering-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Sharding (distributed ledgers)", "Splits a blockchain's state and processing across multiple parallel partitions"],
    ])},
    "computer-science-engineering-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Dual-use technology ethics", "Considers that engineering research can serve both beneficial and harmful purposes"],
    ])},
    "computer-science-engineering-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["MTBF", "Mean Time Between Failures; a reliability metric estimating expected uptime between failures"],
    ])},
    "computer-science-engineering-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Thermal management", "Dissipates heat effectively in densely packed computing hardware"],
    ])},
    "computer-science-engineering-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Silicon photonics", "Uses light instead of electricity to move data at very high bandwidth"],
    ])},
    "computer-science-engineering-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Autonomous vehicle software verification", "Formally verifies safety-critical decision-making software in self-driving cars"],
    ])},
    "computer-science-engineering-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Research methods in systems engineering", "Applies rigorous experimental methodology to computer systems research"],
    ])},
    "computer-science-engineering-m1-l99": {"data_table": table(["Vulnerability", "Feature"], [
        ["Spectre", "Exploits speculative execution to leak data across security boundaries"],
        ["Meltdown", "Exploits out-of-order execution to read protected kernel memory"],
    ])},
    "computer-science-engineering-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Persistent memory", "Byte-addressable memory that retains data across power loss, like DRAM speed with disk durability"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"computer-science-engineering-m1-l{base_n}"
    worked_key = f"computer-science-engineering-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Computer Science Engineering"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Computer Science Engineering: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Computer Science Engineering lessons (completing 120/120).")


if __name__ == "__main__":
    main()
