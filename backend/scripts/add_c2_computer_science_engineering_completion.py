#!/usr/bin/env python3
"""Depth pass, C2 Computer Science Engineering: fill in real,
hand-checked data_table content for the 69 C2 Computer Science
Engineering lessons not covered by the earlier breadth-first batch.
Brings C2 Computer Science Engineering to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_computer_science_engineering_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "computer-science-engineering-c2-l1": {
        "data_table": table(["Component", "Role"], [
            ["ALU", "Performs arithmetic and logic operations"], ["Control unit", "Directs the operation of the processor and memory"],
        ]),
    },
    "computer-science-engineering-c2-l2": {
        "data_table": table(["Topic", "Application"], [
            ["Set theory", "Modeling collections of data"], ["Graph theory", "Modeling networks and relationships"],
        ]),
    },
    "computer-science-engineering-c2-l4": {
        "data_table": table(["Structure", "Property"], [
            ["Binary search tree", "Left child less than parent, right child greater"],
        ]),
    },
    "computer-science-engineering-c2-l5": {
        "data_table": table(["Representation", "Feature"], [
            ["Adjacency matrix", "Fast edge lookup, O(V^2) space"], ["Adjacency list", "Space-efficient for sparse graphs"],
        ]),
    },
    "computer-science-engineering-c2-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Hash function", "Maps keys to array indices for fast average-case lookup"],
        ]),
        "formulae": ["index = hash(key) % table_size"],
    },
    "computer-science-engineering-c2-l7": {
        "data_table": table(["Component", "Role"], [
            ["Base case", "Stops the recursive calls"], ["Recursive case", "Reduces the problem toward the base case"],
        ]),
    },
    "computer-science-engineering-c2-l8": {
        "data_table": table(["Algorithm", "Complexity"], [
            ["Merge sort", "O(n log n)"], ["Quicksort", "O(n log n) average, O(n^2) worst case"],
        ]),
    },
    "computer-science-engineering-c2-l9": {
        "data_table": table(["Algorithm", "Complexity"], [
            ["Linear search", "O(n)"], ["Binary search", "O(log n), requires sorted data"],
        ]),
    },
    "computer-science-engineering-c2-l10": {
        "data_table": table(["Operation", "Meaning"], [
            ["Union", "Combines elements from two sets"], ["Intersection", "Elements common to both sets"],
        ]),
    },
    "computer-science-engineering-c2-l11": {
        "data_table": table(["Symbol", "Meaning"], [
            ["∀", "For all"], ["∃", "There exists"],
        ]),
    },
    "computer-science-engineering-c2-l12": {
        "data_table": table(["Concept", "Formula"], [
            ["Permutations", "nPr = n! / (n-r)!"], ["Combinations", "nCr = n! / (r!(n-r)!)"],
        ]),
        "formulae": ["nPr = factorial(n) / factorial(n - r)"],
    },
    "computer-science-engineering-c2-l13": {
        "data_table": table(["Application", "Example"], [
            ["Shortest path", "Finding the fastest route in a navigation system"],
        ]),
    },
    "computer-science-engineering-c2-l14": {
        "data_table": table(["Concept", "Meaning"], [
            ["Function", "A relation mapping each input to exactly one output"],
        ]),
    },
    "computer-science-engineering-c2-l15": {
        "data_table": table(["Technique", "Meaning"], [
            ["Mathematical induction", "Proves a statement by establishing a base case and an inductive step"],
        ]),
    },
    "computer-science-engineering-c2-l16": {
        "data_table": table(["Example", "Formula"], [
            ["Fibonacci recurrence", "F(n) = F(n-1) + F(n-2)"],
        ]),
        "formulae": ["F(n) = F(n-1) + F(n-2)"],
    },
    "computer-science-engineering-c2-l17": {
        "data_table": table(["Type", "Feature"], [
            ["RISC", "Simple instructions, fixed length, executes quickly"], ["CISC", "Complex instructions, variable length, fewer instructions per program"],
        ]),
    },
    "computer-science-engineering-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Pipelining", "Overlaps execution stages of multiple instructions to improve throughput"],
        ]),
    },
    "computer-science-engineering-c2-l19": {
        "data_table": table(["Level", "Feature"], [
            ["L1 cache", "Smallest, fastest, closest to the CPU core"], ["L3 cache", "Larger, shared across cores, slower than L1"],
        ]),
    },
    "computer-science-engineering-c2-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Bus", "A shared communication pathway transferring data between components"],
        ]),
    },
    "computer-science-engineering-c2-l21": {
        "data_table": table(["Protocol", "Feature"], [
            ["OSPF", "Uses link-state routing for fast convergence within a network"], ["BGP", "Routes traffic between autonomous systems on the internet"],
        ]),
    },
    "computer-science-engineering-c2-l22": {
        "data_table": table(["Concept", "Meaning"], [
            ["Defense in depth", "Layering multiple independent security controls"],
        ]),
    },
    "computer-science-engineering-c2-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Virtualization", "Running multiple isolated virtual machines on shared physical hardware"],
        ]),
    },
    "computer-science-engineering-c2-l24": {
        "data_table": table(["Component", "Role"], [
            ["Inode", "Stores metadata about a file, like permissions and block locations"],
        ]),
    },
    "computer-science-engineering-c2-l25": {
        "data_table": table(["Stage", "Purpose"], [
            ["Code generation", "Translates intermediate representation into target machine code"],
        ]),
    },
    "computer-science-engineering-c2-l26": {
        "data_table": table(["Technique", "Purpose"], [
            ["Loop unrolling", "Reduces loop overhead by replicating the loop body"],
        ]),
    },
    "computer-science-engineering-c2-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Query optimizer", "Chooses the most efficient execution plan for a database query"],
        ]),
    },
    "computer-science-engineering-c2-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Concurrency control", "Ensures database transactions execute correctly when run simultaneously"],
        ]),
    },
    "computer-science-engineering-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Distributed database", "Data spread across multiple physical locations for scalability and fault tolerance"],
        ]),
    },
    "computer-science-engineering-c2-l30": {
        "data_table": table(["Pattern", "Purpose"], [
            ["Singleton", "Ensures only one instance of a class exists"], ["Observer", "Notifies dependents automatically when an object changes state"],
        ]),
    },
    "computer-science-engineering-c2-l31": {
        "data_table": table(["Metric", "Meaning"], [
            ["Cyclomatic complexity", "Measures the number of independent paths through code"],
        ]),
    },
    "computer-science-engineering-c2-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Finite state machine", "A model with a fixed number of states and defined transitions between them"],
        ]),
    },
    "computer-science-engineering-c2-l33": {
        "data_table": table(["Technique", "Purpose"], [
            ["State minimization", "Reduces the number of states in a sequential circuit while preserving behavior"],
        ]),
    },
    "computer-science-engineering-c2-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Superscalar processor", "Executes multiple instructions per clock cycle using multiple execution units"],
        ]),
    },
    "computer-science-engineering-c2-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Multicore system", "A single chip containing multiple independent processing units"],
        ]),
    },
    "computer-science-engineering-c2-l36": {
        "data_table": table(["Model", "Guarantee"], [
            ["Sequential consistency", "Operations appear to execute in a single, globally agreed order"],
        ]),
    },
    "computer-science-engineering-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["RTOS", "An operating system guaranteeing task completion within strict time constraints"],
        ]),
    },
    "computer-science-engineering-c2-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Hardware-software co-design", "Jointly develops hardware and software to optimize overall system performance"],
        ]),
    },
    "computer-science-engineering-c2-l39": {
        "data_table": table(["Feature", "Detail"], [
            ["GPU architecture", "Uses thousands of simple cores for massively parallel computation"],
        ]),
    },
    "computer-science-engineering-c2-l40": {
        "data_table": table(["Algorithm", "Purpose"], [
            ["Paxos", "Achieves agreement among distributed nodes despite failures"], ["Raft", "A more understandable consensus algorithm with a similar goal"],
        ]),
    },
    "computer-science-engineering-c2-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Fault tolerance", "A system's ability to continue operating despite component failures"],
        ]),
    },
    "computer-science-engineering-c2-l42": {
        "data_table": table(["Type", "Feature"], [
            ["Symmetric cryptography", "Uses one shared key"], ["Asymmetric cryptography", "Uses a public/private key pair"],
        ]),
    },
    "computer-science-engineering-c2-l43": {
        "data_table": table(["Protocol", "Purpose"], [
            ["HTTP", "Transfers web content between client and server"], ["SMTP", "Transfers email between mail servers"],
        ]),
    },
    "computer-science-engineering-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Formal verification", "Mathematically proves a program satisfies its specification"],
        ]),
    },
    "computer-science-engineering-c2-l45": {
        "data_table": table(["Machine Type", "Power"], [
            ["Finite automaton", "Recognizes regular languages"], ["Pushdown automaton", "Recognizes context-free languages"],
        ]),
    },
    "computer-science-engineering-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Turing machine", "A theoretical model capable of simulating any computable algorithm"],
        ]),
    },
    "computer-science-engineering-c2-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Approximation algorithm", "Finds a near-optimal solution efficiently when the exact optimum is too costly to compute"],
        ]),
    },
    "computer-science-engineering-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Randomized algorithm", "Uses random choices to achieve good expected performance or simplicity"],
        ]),
    },
    "computer-science-engineering-c2-l49": {
        "data_table": table(["Structure", "Feature"], [
            ["AVL tree", "Self-balancing binary search tree with strict height balance"], ["Red-black tree", "Self-balancing tree with a looser balance invariant"],
        ]),
    },
    "computer-science-engineering-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Skip list", "A layered linked structure allowing fast probabilistic search"],
        ]),
    },
    "computer-science-engineering-c2-l51": {
        "data_table": table(["Task", "Example"], [
            ["Object detection", "Locating and classifying objects within an image"],
        ]),
    },
    "computer-science-engineering-c2-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Usability engineering", "Systematically designs and tests interfaces for ease of use"],
        ]),
    },
    "computer-science-engineering-c2-l53": {
        "data_table": table(["Stage", "Purpose"], [
            ["Rasterization", "Converts vector graphics into a grid of pixels for display"],
        ]),
    },
    "computer-science-engineering-c2-l54": {
        "data_table": table(["Framework", "Purpose"], [
            ["Selenium", "Automates browser-based UI testing"],
        ]),
    },
    "computer-science-engineering-c2-l55": {
        "data_table": table(["Methodology", "Feature"], [
            ["Agile", "Iterative delivery with short development cycles"], ["Waterfall", "Sequential phases completed one after another"],
        ]),
    },
    "computer-science-engineering-c2-l56": {
        "data_table": table(["Phase", "Purpose"], [
            ["Reconnaissance", "Gathers information about the target before testing"],
        ]),
    },
    "computer-science-engineering-c2-l57": {
        "data_table": table(["Principle", "Meaning"], [
            ["Least privilege", "Grants only the minimum access necessary for a task"],
        ]),
    },
    "computer-science-engineering-c2-l58": {
        "data_table": table(["Generation", "Feature"], [
            ["4G", "High-speed mobile broadband using LTE"], ["5G", "Higher speed and lower latency, enabling new applications"],
        ]),
    },
    "computer-science-engineering-c2-l59": {
        "data_table": table(["Term", "Meaning"], [
            ["Qubit", "A quantum bit that can exist in superposition of 0 and 1"],
        ]),
    },
    "computer-science-engineering-c2-l60": {
        "data_table": table(["Layer", "Consideration"], [
            ["Hardware", "Selecting processor and memory architecture"], ["Software", "Designing the OS and application layers"],
        ]),
    },
    "computer-science-engineering-c2-l61": {
        "data_table": table(["Concept", "Meaning"], [
            ["Undecidability", "Some problems, like the Halting Problem, have no algorithm that always produces a correct yes/no answer"],
        ]),
    },
    "computer-science-engineering-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Tracing an instruction cycle", "Following fetch, decode, execute, and store stages"],
        ]),
    },
    "computer-science-engineering-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Applying set operations", "Solving a problem using union and intersection"],
        ]),
    },
    "computer-science-engineering-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a data structure", "Selecting a queue for a task scheduling system"],
        ]),
    },
    "computer-science-engineering-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Balancing a BST", "Applying rotations to maintain O(log n) height"],
        ]),
    },
    "computer-science-engineering-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Traversing a graph", "Using BFS to find the shortest unweighted path"],
        ]),
    },
    "computer-science-engineering-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Resolving a hash collision", "Applying chaining to store multiple keys at one index"],
        ]),
    },
    "computer-science-engineering-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Writing a recursive function", "Implementing factorial or Fibonacci with a clear base case"],
        ]),
    },
    "computer-science-engineering-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Comparing sort algorithms", "Choosing merge sort for stability versus quicksort for speed"],
        ]),
    },
    "computer-science-engineering-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a search strategy", "Selecting binary search on sorted data for efficiency"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Computer Science Engineering"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Computer Science Engineering: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Computer Science Engineering lessons (completing 70/70).")


if __name__ == "__main__":
    main()
