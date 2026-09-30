#!/usr/bin/env python3
"""Depth pass, M1 Coding: fill in real, hand-checked data_table content
for the 99 M1 Coding lessons not covered by the earlier breadth-first
batch. Brings M1 Coding to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "coding-m1-l1": {
        "data_table": table(["Concept", "Detail"], [
            ["Software engineering practice", "Encompasses process, tooling, and discipline in building maintainable software"],
        ]),
    },
    "coding-m1-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["Systems architecture", "Structures how major components of a software system interact at scale"],
        ]),
    },
    "coding-m1-l4": {
        "data_table": table(["Technique", "Detail"], [
            ["Recursion tree analysis", "Bounds algorithm runtime by summing costs across recursive call levels"],
        ]),
    },
    "coding-m1-l5": {
        "data_table": table(["Algorithm", "Property"], [
            ["Quickselect", "Finds the k-th order statistic in expected linear time"],
        ]),
    },
    "coding-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Optimal substructure", "A problem's optimal solution can be built from optimal solutions to subproblems"],
        ]),
    },
    "coding-m1-l7": {
        "data_table": table(["Algorithm", "Use Case"], [
            ["Max-flow min-cut", "Determines maximum flow through a network via its minimum cut"],
        ]),
    },
    "coding-m1-l8": {
        "data_table": table(["Structure", "Feature"], [
            ["B-tree", "Balanced tree optimized for block-based storage and disk access"],
        ]),
    },
    "coding-m1-l9": {
        "data_table": table(["Structure", "Use Case"], [
            ["Consistent hashing", "Minimizes redistribution when nodes are added/removed in a distributed system"],
        ]),
    },
    "coding-m1-l10": {
        "data_table": table(["Critique", "Detail"], [
            ["Over-application of SOLID", "Excessive abstraction can reduce readability without proportional benefit"],
        ]),
    },
    "coding-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Pattern language", "A structured vocabulary of interrelated design patterns for a domain"],
        ]),
    },
    "coding-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Distributed architecture", "Coordinates independent components across machines with network-aware design"],
        ]),
    },
    "coding-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Distributed version control", "Each contributor holds a full repository copy rather than depending on a central server"],
        ]),
    },
    "coding-m1-l14": {
        "data_table": table(["Practice", "Purpose"], [
            ["Static analysis in CI", "Catches quality issues automatically before code reaches production"],
        ]),
    },
    "coding-m1-l15": {
        "data_table": table(["Technique", "Purpose"], [
            ["Distributed tracing", "Follows a request across multiple services to pinpoint failure or latency sources"],
        ]),
    },
    "coding-m1-l16": {
        "data_table": table(["Method", "Purpose"], [
            ["Formal verification", "Mathematically proves a program satisfies its specification"],
        ]),
    },
    "coding-m1-l17": {
        "data_table": table(["Practice", "Purpose"], [
            ["Release engineering", "Manages the safe, repeatable process of shipping software to production"],
        ]),
    },
    "coding-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Systems programming", "Writes low-level software that manages hardware resources directly"],
        ]),
    },
    "coding-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Distributed computation", "Coordinates parallel work across independent, network-connected nodes"],
        ]),
    },
    "coding-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone contribution", "Delivers an original engineering or research artifact demonstrating mastery"],
        ]),
    },
    "coding-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Curry-Howard correspondence", "Establishes a direct link between logical proofs and typed programs"],
        ]),
    },
    "coding-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Dependent type", "A type that depends on a value, enabling more precise program specifications"],
        ]),
    },
    "coding-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Functor/Monad", "Category-theoretic abstractions structuring composable functional computation"],
        ]),
    },
    "coding-m1-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Monad transformer", "Composes multiple monadic effects into a single stacked computation"],
        ]),
    },
    "coding-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Lazy evaluation", "Delays computing a value until it is actually needed"],
        ]),
    },
    "coding-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Linear type", "Ensures a resource is used exactly once, preventing leaks or double-use"],
        ]),
    },
    "coding-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Session type", "Statically verifies that a communication protocol's message sequence is followed correctly"],
        ]),
    },
    "coding-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Abstract interpretation", "Analyzes program behavior using approximated, sound abstract values"],
        ]),
    },
    "coding-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Symbolic execution", "Explores program paths using symbolic rather than concrete input values"],
        ]),
    },
    "coding-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Model checking", "Exhaustively verifies a finite-state system against a formal specification"],
        ]),
    },
    "coding-m1-l31": {
        "data_table": table(["Tool", "Use"], [
            ["SMT solver", "Determines satisfiability of logical formulas over structured theories"],
        ]),
    },
    "coding-m1-l32": {
        "data_table": table(["Concept", "Formula"], [
            ["Hoare triple", "{P} C {Q} states precondition P and command C guarantee postcondition Q"],
        ]),
        "formulae": ["{P} C {Q}"],
    },
    "coding-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Separation logic", "Extends Hoare logic to reason precisely about disjoint mutable memory regions"],
        ]),
    },
    "coding-m1-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["SSA form", "Each variable is assigned exactly once, simplifying compiler optimization analysis"],
        ]),
    },
    "coding-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["JIT compilation", "Compiles code at runtime to balance startup speed with execution performance"],
        ]),
    },
    "coding-m1-l36": {
        "data_table": table(["Type", "Feature"], [
            ["Generational GC", "Collects young, short-lived objects more frequently than old ones"],
            ["Concurrent GC", "Runs collection alongside the application to reduce pause times"],
        ]),
    },
    "coding-m1-l37": {
        "data_table": table(["Algorithm", "Purpose"], [
            ["Graph coloring register allocation", "Assigns variables to limited physical registers by avoiding conflicts"],
        ]),
    },
    "coding-m1-l38": {
        "data_table": table(["Technique", "Purpose"], [
            ["Loop unrolling", "Reduces loop overhead by replicating the loop body"],
            ["Vectorization", "Executes the same operation on multiple data elements simultaneously"],
        ]),
    },
    "coding-m1-l39": {
        "data_table": table(["Principle", "Detail"], [
            ["DSL design", "Trades general-purpose flexibility for expressiveness within a narrow problem domain"],
        ]),
    },
    "coding-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Parser combinator", "Builds complex parsers by composing small, reusable parsing functions"],
        ]),
    },
    "coding-m1-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Actor model", "Isolated actors communicate exclusively through asynchronous messages"],
        ]),
    },
    "coding-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Software transactional memory", "Manages concurrent memory access using transaction-like commit/rollback semantics"],
        ]),
    },
    "coding-m1-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["Lock-free structure", "Uses atomic operations to guarantee system-wide progress without locking"],
        ]),
    },
    "coding-m1-l44": {
        "data_table": table(["Model", "Detail"], [
            ["Memory consistency model", "Defines the guarantees for how memory operations appear across multiple cores"],
        ]),
    },
    "coding-m1-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Raft consensus", "Elects a leader and replicates a log to keep distributed nodes in agreement"],
        ]),
    },
    "coding-m1-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["CRDT", "A data structure that merges concurrent updates deterministically without conflict"],
        ]),
    },
    "coding-m1-l47": {
        "data_table": table(["Pattern", "Detail"], [
            ["Event sourcing", "Persists state as a sequence of events rather than a mutable snapshot"],
            ["CQRS", "Separates read and write models to optimize each independently"],
        ]),
    },
    "coding-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Bounded context", "Defines a clear boundary within which a domain model's terms have consistent meaning"],
        ]),
    },
    "coding-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Fitness function", "An automated check that continuously validates an architectural quality attribute"],
        ]),
    },
    "coding-m1-l50": {
        "data_table": table(["Practice", "Purpose"], [
            ["Refactoring to patterns", "Applies established design patterns incrementally to improve existing code"],
        ]),
    },
    "coding-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Static analysis tool design", "Balances detection sensitivity against false positive rate"],
        ]),
    },
    "coding-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Mutation testing", "Injects small code faults to check whether the test suite catches them"],
        ]),
    },
    "coding-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Property-based testing", "Generates random inputs to check that general properties always hold"],
        ]),
        "formulae": ["@given(st.integers(), st.integers())\ndef test_add_commutative(a, b):\n    assert add(a, b) == add(b, a)"],
    },
    "coding-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Fuzz testing", "Feeds malformed or random input to uncover crashes and vulnerabilities"],
        ]),
    },
    "coding-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Design by contract", "Specifies preconditions, postconditions, and invariants a component must honor"],
        ]),
    },
    "coding-m1-l56": {
        "data_table": table(["Smell", "Detail"], [
            ["Long method", "A method doing too much is harder to test and understand"],
        ]),
    },
    "coding-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Technical debt", "Shortcuts taken now that create extra rework later"],
        ]),
    },
    "coding-m1-l58": {
        "data_table": table(["Metric", "Meaning"], [
            ["Cyclomatic complexity", "Counts independent paths through code, indicating testing difficulty"],
        ]),
    },
    "coding-m1-l59": {
        "data_table": table(["Practice", "Detail"], [
            ["Trunk-based development", "Small changes merged frequently into a shared main branch"],
        ]),
    },
    "coding-m1-l60": {
        "data_table": table(["Technique", "Purpose"], [
            ["Feature toggle", "Ships code in a disabled state, enabling safer incremental rollout"],
        ]),
    },
    "coding-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Idempotency", "Repeating an API call produces the same result as calling it once"],
        ]),
    },
    "coding-m1-l62": {
        "data_table": table(["Algorithm", "Detail"], [
            ["Token bucket", "Allows bursts of requests up to a capped rate over time"],
        ]),
    },
    "coding-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Trace context propagation", "Passes a request identifier across service boundaries for observability"],
        ]),
    },
    "coding-m1-l64": {
        "data_table": table(["Technique", "Purpose"], [
            ["Code generation", "Automatically produces repetitive boilerplate from a higher-level specification"],
        ]),
    },
    "coding-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Metaprogramming", "Writes code that manipulates or generates other code at compile or runtime"],
        ]),
    },
    "coding-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Macro hygiene", "Prevents unintended variable capture when a macro expands into surrounding code"],
        ]),
    },
    "coding-m1-l67": {
        "data_table": table(["Technique", "Purpose"], [
            ["Bytecode instrumentation", "Injects monitoring logic into compiled code without modifying source"],
        ]),
    },
    "coding-m1-l68": {
        "data_table": table(["Tool", "Purpose"], [
            ["Flame graph", "Visualizes stack traces to identify performance hotspots"],
        ]),
    },
    "coding-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Cache-conscious design", "Arranges data layout to maximize CPU cache hit rates"],
        ]),
    },
    "coding-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["SIMD", "Executes the same instruction across multiple data elements in parallel"],
        ]),
    },
    "coding-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["GPU kernel", "A function executed in parallel across thousands of GPU threads"],
        ]),
    },
    "coding-m1-l72": {
        "data_table": table(["Tool", "Purpose"], [
            ["TLA+", "A formal specification language for modeling and verifying concurrent system designs"],
        ]),
    },
    "coding-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Distributed invariant testing", "Verifies properties that must hold across all nodes of a distributed system"],
        ]),
    },
    "coding-m1-l74": {
        "data_table": table(["Algorithm", "Detail"], [
            ["Hindley-Milner inference", "Automatically deduces the most general type for an expression without annotations"],
        ]),
    },
    "coding-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Gradual typing", "Allows static and dynamic typing to coexist within the same codebase"],
        ]),
    },
    "coding-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Effect system", "Tracks a function's side effects statically as part of its type"],
        ]),
    },
    "coding-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Packrat parsing", "Memoizes parse results to guarantee linear-time PEG parsing"],
        ]),
    },
    "coding-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Self-adjusting computation", "Efficiently recomputes only the parts of a result affected by an input change"],
        ]),
    },
    "coding-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["Reactive stream", "Models asynchronous data as a composable sequence of events over time"],
        ]),
    },
    "coding-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Reproducible build", "Guarantees identical output from identical source, verifying supply chain integrity"],
        ]),
    },
    "coding-m1-l81": {
        "data_table": table(["Technique", "Purpose"], [
            ["Reverse engineering", "Analyzes compiled binaries to recover program logic and behavior"],
        ]),
    },
    "coding-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Control flow integrity", "Restricts program execution to a valid set of control flow paths to block exploits"],
        ]),
    },
    "coding-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Taint analysis", "Tracks how untrusted input flows through a program to detect vulnerabilities"],
        ]),
    },
    "coding-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Software composition analysis", "Scans dependencies for known vulnerabilities and license risk"],
        ]),
    },
    "coding-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Language Server Protocol", "Standardizes editor-language tooling communication like autocomplete and diagnostics"],
        ]),
    },
    "coding-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["AST transformation pipeline", "Applies a sequence of tree rewrites to analyze or modify source code"],
        ]),
    },
    "coding-m1-l87": {
        "data_table": table(["Bug Class", "Detail"], [
            ["Data race", "Unsynchronized concurrent access to shared memory produces undefined behavior"],
        ]),
    },
    "coding-m1-l88": {
        "data_table": table(["Concept", "Detail"], [
            ["Smart contract verification", "Applies formal methods to catch costly bugs before contract deployment"],
        ]),
    },
    "coding-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Runtime sandboxing", "Restricts a program's permitted operations to limit potential damage"],
        ]),
    },
    "coding-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Data-oriented design", "Organizes data layout around access patterns rather than object hierarchies"],
        ]),
    },
    "coding-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Architecture decision record", "Documents a significant design decision and its rationale for future reference"],
        ]),
    },
    "coding-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Polyglot interoperability", "Enables components written in different languages to communicate reliably"],
        ]),
    },
    "coding-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Continuous fuzzing", "Runs fuzz testing persistently in CI to catch regressions early"],
        ]),
    },
    "coding-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Static site generation", "Pre-builds HTML pages at build time for fast, cacheable delivery"],
        ]),
    },
    "coding-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Internationalization architecture", "Separates locale-specific content from application logic for easy adaptation"],
        ]),
    },
    "coding-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Contract testing", "Verifies that a service's API meets the expectations of its consumers"],
        ]),
    },
    "coding-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Grammar ambiguity resolution", "Uses precedence and associativity rules to resolve conflicting parse interpretations"],
        ]),
    },
    "coding-m1-l98": {
        "data_table": table(["Method", "Purpose"], [
            ["Empirical software engineering study", "Collects real-world data to test hypotheses about development practice"],
        ]),
    },
    "coding-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Persistent data structure", "Preserves previous versions of itself when modified, via structural sharing"],
        ]),
    },
    "coding-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Content-addressable storage", "Identifies stored data by its content hash rather than a location, as in Git"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Complexity Class", "Meaning"], [
        ["P", "Problems solvable in polynomial time"],
        ["NP", "Problems whose solutions can be verified in polynomial time"],
        ["NP-complete", "The hardest problems in NP"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table/formulae of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"coding-m1-l{base_n}"
    if base_key in CHARTS:
        fields = {"data_table": CHARTS[base_key]["data_table"]}
        if "formulae" in CHARTS[base_key]:
            fields["formulae"] = CHARTS[base_key]["formulae"]
        CHARTS[f"coding-m1-l{worked_n}"] = fields
    elif base_n == 3:
        CHARTS[f"coding-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Coding lessons (completing 120/120).")


if __name__ == "__main__":
    main()
