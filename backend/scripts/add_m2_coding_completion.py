#!/usr/bin/env python3
"""Depth pass, M2 Coding: fill in real, hand-checked data_table
content for the M2 Coding lessons not covered by the earlier
breadth-first batch. Brings M2 Coding to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level programming languages
and compilers research topics spanning type theory, program
verification, compiler/runtime construction, concurrency, and
software analysis; l101-l120 are "Worked Analysis" companions
reusing the data_table of l1-l20 (direct 1:1 mapping). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Hindley-Milner", "A classic algorithm for inferring the most general type of an expression without annotations"],
    ["Type inference", "Automatically deduces a program's types rather than requiring explicit declarations"],
])

CHARTS: dict[str, dict] = {
    "coding-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Systems & architecture research", "Systematic methods for studying how software systems are structured and built"],
    ])},
    "coding-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Programming fundamentals research", "Rigorous study of the core principles underlying how programs compute"],
    ])},
    "coding-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Dependent type theory", "Types that can depend on values, enabling machine-checked correctness proofs"],
    ])},
    "coding-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Linear type system", "Ensures a resource is used exactly once, preventing leaks and double-use bugs"],
    ])},
    "coding-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Effect system", "Tracks a function's side effects (I/O, exceptions) directly within its type"],
    ])},
    "coding-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Gradual typing soundness", "Proves that mixing statically and dynamically typed code cannot silently violate type safety"],
    ])},
    "coding-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Abstract interpretation", "A theory for building sound static analyzers by approximating a program's runtime behavior"],
    ])},
    "coding-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Symbolic execution", "Runs a program with symbolic rather than concrete inputs to explore all execution paths"],
    ])},
    "coding-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Concolic testing", "Combines concrete execution with symbolic constraints to generate high-coverage test inputs"],
    ])},
    "coding-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["SMT solver", "Automatically checks satisfiability of logical formulas, used to power program verification tools"],
    ])},
    "coding-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Hoare logic", "A formal system using pre/postconditions to prove a program's correctness"],
    ])},
    "coding-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Separation logic", "Extends Hoare logic to reason precisely about programs that mutate heap memory"],
    ])},
    "coding-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Refinement type", "A base type restricted by a logical predicate, encoding precise specifications"],
    ])},
    "coding-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Compiler IR design", "The internal program representation that enables analysis and optimization passes"],
    ])},
    "coding-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["SSA form", "Static Single Assignment; a compiler IR where each variable is assigned exactly once"],
    ])},
    "coding-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Graph-coloring register allocation", "Assigns variables to limited CPU registers by treating it as a graph coloring problem"],
    ])},
    "coding-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Tiered JIT compilation", "Progressively applies more aggressive optimization to code that runs more frequently"],
    ])},
    "coding-m2-l19": {"data_table": table(["Type", "Feature"], [
        ["Generational GC", "Collects young, short-lived objects more frequently than old ones"],
        ["Concurrent GC", "Runs collection alongside the program to reduce pause times"],
    ])},
    "coding-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Escape analysis", "Determines whether an object can be stack-allocated instead of heap-allocated"],
    ])},
    "coding-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Profile-guided optimization", "Uses collected runtime execution data to guide compiler optimization decisions"],
    ])},
    "coding-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Superoptimization", "Searches exhaustively or via synthesis for a provably minimal instruction sequence"],
    ])},
    "coding-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Program synthesis (examples)", "Automatically generates a program satisfying given input-output example pairs"],
    ])},
    "coding-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Type-directed synthesis", "Uses refinement types to prune the search space when synthesizing correct programs"],
    ])},
    "coding-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Neural program synthesis", "Uses differentiable, trainable models to learn to generate or execute programs"],
    ])},
    "coding-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Coverage-guided fuzzing", "Mutates inputs guided by code coverage to find new program paths and bugs"],
    ])},
    "coding-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Mutation testing", "Introduces small code bugs to check whether the test suite catches them"],
    ])},
    "coding-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Differential testing", "Compares outputs of multiple implementations of the same specification to find bugs"],
    ])},
    "coding-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Metamorphic testing", "Tests programs lacking a known correct answer by checking relationships between outputs"],
    ])},
    "coding-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Shrinking (property testing)", "Automatically reduces a failing random test case to its simplest reproducing form"],
    ])},
    "coding-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Formal specification language", "A precise, machine-checkable notation for defining an API's expected contract"],
    ])},
    "coding-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Model checking", "Exhaustively explores a system's state space to verify a property holds in every state"],
    ])},
    "coding-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Bounded model checking", "Checks a property only up to a fixed number of execution steps, trading completeness for speed"],
    ])},
    "coding-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Data race detection", "Identifies unsynchronized concurrent memory accesses that can cause undefined behavior"],
    ])},
    "coding-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Lock-order graph analysis", "Detects potential deadlocks by finding cycles in the order locks are acquired"],
    ])},
    "coding-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Software transactional memory", "Manages concurrent memory access using transactions that abort and retry on conflict"],
    ])},
    "coding-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Compare-and-swap", "An atomic hardware primitive used to build lock-free concurrent data structures"],
    ])},
    "coding-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Wait-free algorithm", "Guarantees every thread completes its operation in a bounded number of steps"],
    ])},
    "coding-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Memory consistency model", "Formally defines what values a concurrent read may observe from prior writes"],
    ])},
    "coding-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Actor model", "Isolates state within independent actors that communicate only via messages, aiding fault isolation"],
    ])},
    "coding-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Continuation-based control flow", "Represents 'the rest of the computation' explicitly to implement coroutines and control operators"],
    ])},
    "coding-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Algebraic effect handler", "A composable mechanism for defining and interpreting custom control-flow effects"],
    ])},
    "coding-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Parser combinator", "Builds complex parsers by composing small reusable parsing functions"],
    ])},
    "coding-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["LR parsing table", "A bottom-up parsing table constructed to efficiently parse context-free grammars"],
    ])},
    "coding-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Incremental parsing", "Re-parses only the changed portion of code for responsive real-time editor tooling"],
    ])},
    "coding-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Tree-sitter style parsing", "Maintains an incrementally updated syntax tree efficiently as source code is edited"],
    ])},
    "coding-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Language Server Protocol", "A standard letting one language analysis backend serve many different code editors"],
    ])},
    "coding-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Call graph construction", "Builds a graph of which functions call which others across an entire program"],
    ])},
    "coding-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Points-to analysis", "Determines which memory locations a pointer variable could possibly reference"],
    ])},
    "coding-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Interprocedural data flow analysis", "Tracks how data propagates across function call boundaries in a whole program"],
    ])},
    "coding-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Taint analysis", "Tracks untrusted data flow through a program to find potential injection vulnerabilities"],
    ])},
    "coding-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Control flow graph recovery", "Reconstructs a program's branching structure from compiled binary code"],
    ])},
    "coding-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Deobfuscation", "Reverses techniques used to disguise malicious or protected code's true behavior"],
    ])},
    "coding-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["AST-based refactoring", "Automatically transforms code by manipulating its parsed abstract syntax tree"],
    ])},
    "coding-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Clone detection", "Identifies duplicated or near-duplicate code fragments across a codebase"],
    ])},
    "coding-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Technical debt quantification", "Measures accumulated code quality shortcuts using static analysis metrics"],
    ])},
    "coding-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Automated program repair", "Automatically generates candidate patches to fix a detected software bug"],
    ])},
    "coding-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Spectrum-based fault localization", "Uses patterns of passing/failing tests to statistically pinpoint a likely buggy line"],
    ])},
    "coding-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Change impact analysis", "Predicts which parts of a codebase are affected by a given code change"],
    ])},
    "coding-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Test selection (CI)", "Runs only the tests likely affected by a change to speed up continuous integration"],
    ])},
    "coding-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Build dependency graph optimization", "Structures build dependencies to minimize unnecessary recompilation"],
    ])},
    "coding-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Distributed build caching", "Shares compiled build artifacts across machines to avoid redundant work in large monorepos"],
    ])},
    "coding-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Merge conflict resolution algorithm", "Automatically or semi-automatically resolves conflicting concurrent code edits"],
    ])},
    "coding-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Operational transformation", "Resolves concurrent edits by transforming operations to stay consistent"],
    ])},
    "coding-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["CRDT (collaborative editing)", "A data structure that merges concurrent code edits automatically without conflicts"],
    ])},
    "coding-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Embedded DSL design", "Principles for building a domain-specific language that reuses a host language's syntax"],
    ])},
    "coding-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Macro system", "Enables compile-time code generation and transformation before normal compilation"],
    ])},
    "coding-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Reflection trade-offs", "Runtime metaprogramming offers flexibility at the cost of predictability and performance"],
    ])},
    "coding-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Bytecode verification", "Statically checks compiled bytecode for safety before a managed runtime executes it"],
    ])},
    "coding-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["WebAssembly instruction set", "A compact, portable, sandboxed binary format for compiled code execution"],
    ])},
    "coding-m2-l71": {"data_table": table(["Approach", "Trade-off"], [
        ["Ahead-of-time compilation", "Faster startup, no runtime profiling"],
        ["Just-in-time compilation", "Adapts to actual runtime behavior for peak performance"],
    ])},
    "coding-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Tail call optimization", "Reuses the current stack frame for a tail call, enabling constant-space recursion"],
    ])},
    "coding-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Persistent data structure", "An immutable structure that efficiently shares memory between its old and new versions"],
    ])},
    "coding-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Monad transformer", "Composes multiple monadic effects into a single stacked, layered computation type"],
    ])},
    "coding-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Thunk", "A deferred, unevaluated computation used to implement lazy evaluation"],
    ])},
    "coding-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Pattern match compilation", "Compiles a pattern-matching construct into an efficient decision tree"],
    ])},
    "coding-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Row polymorphism", "A type system feature letting functions accept records with extra unspecified fields"],
    ])},
    "coding-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Session type", "Statically verifies that a communication protocol between processes is followed correctly"],
    ])},
    "coding-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Capability-based security (language design)", "Grants access via unforgeable object references rather than ambient permissions"],
    ])},
    "coding-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Sandboxed plugin execution", "Runs untrusted extension code with restricted access to the host application"],
    ])},
    "coding-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["JIT specialization", "Generates optimized code paths tailored to a dynamic language's observed runtime types"],
    ])},
    "coding-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Polyglot runtime interoperability", "Lets multiple languages interoperate efficiently via a shared intermediate representation"],
    ])},
    "coding-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Source-to-source transpiler", "Translates code from one language into another at the source level"],
    ])},
    "coding-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Automatic differentiation", "Computes exact derivatives of numerical code automatically, used to train ML models"],
    ])},
    "coding-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["JIT vectorization", "Automatically rewrites loops to use SIMD instructions for parallel numerical computation"],
    ])},
    "coding-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["GPU kernel compilation", "Compiles code for execution on GPU hardware within a heterogeneous computing pipeline"],
    ])},
    "coding-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["JIT query compilation", "Compiles database queries into optimized native code at execution time"],
    ])},
    "coding-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Interactive theorem prover", "A tool that lets humans construct and machine-check formal mathematical proofs"],
    ])},
    "coding-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Certified compilation", "Formally proves a compiler itself preserves the meaning of the programs it compiles"],
    ])},
    "coding-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Randomized testing oracle", "Generates random programs to check a compiler's correctness against expected behavior"],
    ])},
    "coding-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Use-after-free detection", "Static analysis that flags memory accessed after it has already been freed"],
    ])},
    "coding-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Borrow checker", "Statically enforces memory safety rules about ownership and references at compile time"],
    ])},
    "coding-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Region-based memory management", "Groups allocations into regions freed together, avoiding per-object garbage collection"],
    ])},
    "coding-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Software diversification", "Randomizes program layout or code to make exploits harder to reliably reproduce"],
    ])},
    "coding-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Control flow integrity", "Restricts a program's execution to only its legitimate, intended control flow paths"],
    ])},
    "coding-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Automated patch backporting", "Applies a security fix to older code versions using program analysis to locate matches"],
    ])},
    "coding-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Software composition analysis", "Scans transitive dependencies for known vulnerabilities"],
    ])},
    "coding-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["LLM code generation evaluation", "Systematic methodology for measuring the correctness of AI-generated code"],
    ])},
    "coding-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Static analysis in CI/CD", "Integrates automated code analysis tools directly into the software delivery pipeline"],
    ])},
    "coding-m2-l100": {"data_table": table(["Component", "Purpose"], [
        ["Thesis-level capstone", "Designs and formally verifies a novel programming language feature as original research"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"coding-m2-l{base_n}"
    worked_key = f"coding-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Coding lessons.")


if __name__ == "__main__":
    main()
