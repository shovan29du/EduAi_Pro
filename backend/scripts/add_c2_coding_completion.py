#!/usr/bin/env python3
"""Depth pass, C2 Coding: fill in real, hand-checked data_table/formulae
(real runnable code) content for the 69 C2 Coding lessons not covered
by the earlier breadth-first batch. Brings C2 Coding to full 70/70
coverage.

l61-l64 revisit earlier design-pattern lessons as "Foundations 2/3"
lessons; l65-l70 are "Worked Analysis" companions to l1-l6. l3 was
already completed by an earlier breadth-first batch, so its data_table
is hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "coding-c2-l1": {
        "data_table": table(["Structure", "Access Time"], [
            ["Array", "O(1) by index"], ["Linked list", "O(n) sequential"], ["Hash map", "O(1) average by key"],
        ]),
    },
    "coding-c2-l2": {
        "data_table": table(["Practice", "Purpose"], [
            ["Code review", "Catches defects and spreads knowledge before merge"],
            ["Continuous integration", "Automatically builds and tests every change"],
        ]),
    },
    "coding-c2-l4": {
        "data_table": table(["Step", "Action"], [
            ["Divide", "Break problem into smaller subproblems"],
            ["Conquer", "Solve subproblems recursively"],
            ["Combine", "Merge subproblem solutions"],
        ]),
        "formulae": ["def divide_conquer(problem):\n    if base_case(problem):\n        return solve_directly(problem)\n    parts = divide(problem)\n    solved = [divide_conquer(p) for p in parts]\n    return combine(solved)"],
    },
    "coding-c2-l5": {
        "data_table": table(["Algorithm", "Average Time"], [
            ["Merge sort", "O(n log n), stable"], ["Quicksort", "O(n log n) average, in-place"],
        ]),
        "formulae": ["def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    result = []\n    i = j = 0\n    while i < len(left) and j < len(right):\n        if left[i] <= right[j]:\n            result.append(left[i]); i += 1\n        else:\n            result.append(right[j]); j += 1\n    return result + left[i:] + right[j:]"],
    },
    "coding-c2-l6": {
        "data_table": table(["Problem", "Recurrence"], [
            ["Longest common subsequence", "dp[i][j] depends on dp[i-1][j-1], dp[i-1][j], dp[i][j-1]"],
        ]),
        "formulae": ["def lcs(a, b):\n    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]\n    for i in range(1, len(a) + 1):\n        for j in range(1, len(b) + 1):\n            if a[i-1] == b[j-1]:\n                dp[i][j] = dp[i-1][j-1] + 1\n            else:\n                dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n    return dp[-1][-1]"],
    },
    "coding-c2-l7": {
        "data_table": table(["Algorithm", "Use Case"], [
            ["Dijkstra's algorithm", "Shortest path with non-negative edge weights"],
            ["Bellman-Ford", "Shortest path that tolerates negative edge weights"],
        ]),
        "formulae": ["import heapq\ndef dijkstra(graph, start):\n    dist = {start: 0}\n    pq = [(0, start)]\n    while pq:\n        d, u = heapq.heappop(pq)\n        if d > dist.get(u, float('inf')):\n            continue\n        for v, w in graph[u]:\n            nd = d + w\n            if nd < dist.get(v, float('inf')):\n                dist[v] = nd\n                heapq.heappush(pq, (nd, v))\n    return dist"],
    },
    "coding-c2-l8": {
        "data_table": table(["Tree", "Balancing Rule"], [
            ["AVL tree", "Height difference of subtrees at most 1"],
            ["Red-black tree", "Color and rotation rules bound the height at O(log n)"],
        ]),
    },
    "coding-c2-l9": {
        "data_table": table(["Strategy", "Approach"], [
            ["Chaining", "Store colliding entries in a linked list at each bucket"],
            ["Open addressing", "Probe for the next open slot in the array"],
        ]),
    },
    "coding-c2-l10": {
        "data_table": table(["Principle", "Detail"], [
            ["Encapsulation", "Hides internal state behind a controlled interface"],
            ["Abstraction", "Exposes only essential behavior, hiding implementation detail"],
        ]),
        "formulae": ["class Account:\n    def __init__(self, balance):\n        self._balance = balance\n\n    def deposit(self, amount):\n        self._balance += amount"],
    },
    "coding-c2-l11": {
        "data_table": table(["Pattern", "Purpose"], [
            ["Factory method", "Delegates object creation to a subclass or method"],
            ["Singleton", "Ensures a class has only one instance"],
        ]),
    },
    "coding-c2-l12": {
        "data_table": table(["Layer", "Responsibility"], [
            ["Model", "Manages data and business logic"],
            ["View", "Renders the user interface"],
            ["Controller", "Handles input and coordinates Model and View"],
        ]),
    },
    "coding-c2-l13": {
        "data_table": table(["Strategy", "Detail"], [
            ["Feature branching", "Each feature developed in its own branch until ready to merge"],
            ["Trunk-based development", "Small changes merged frequently into a shared main branch"],
        ]),
        "formulae": ["git checkout -b feature/login\ngit push -u origin feature/login\ngit checkout main\ngit merge feature/login"],
    },
    "coding-c2-l14": {
        "data_table": table(["Practice", "Benefit"], [
            ["Descriptive naming", "Reduces the need for explanatory comments"],
            ["Small functions", "Easier to test, review, and reason about"],
        ]),
    },
    "coding-c2-l15": {
        "data_table": table(["Tool", "Use"], [
            ["Breakpoint", "Pauses execution at a specific line to inspect state"],
            ["Watch expression", "Tracks a variable's value across execution steps"],
        ]),
    },
    "coding-c2-l16": {
        "data_table": table(["Step", "Action"], [
            ["Red", "Write a failing test"], ["Green", "Write the minimal code to pass it"], ["Refactor", "Clean up while keeping tests green"],
        ]),
        "formulae": ["def test_add():\n    assert add(2, 3) == 5\n\ndef add(a, b):\n    return a + b"],
    },
    "coding-c2-l17": {
        "data_table": table(["Stage", "Purpose"], [
            ["Build", "Compiles/packages the application"],
            ["Test", "Runs automated test suites"],
            ["Deploy", "Ships the build to an environment"],
        ]),
    },
    "coding-c2-l18": {
        "data_table": table(["Concept", "Risk"], [
            ["Manual memory management", "Enables performance control but risks leaks and dangling pointers"],
        ]),
        "formulae": ["int *p = malloc(sizeof(int));\n*p = 42;\nfree(p);"],
    },
    "coding-c2-l19": {
        "data_table": table(["Primitive", "Purpose"], [
            ["Mutex", "Ensures exclusive access to a shared resource"],
            ["Semaphore", "Limits concurrent access to a fixed number of resources"],
        ]),
    },
    "coding-c2-l20": {
        "data_table": table(["Stage", "Task"], [
            ["Ingest", "Read raw data from a source"],
            ["Transform", "Clean and reshape the data"],
            ["Load", "Write results to a destination store"],
        ]),
    },
    "coding-c2-l21": {
        "data_table": table(["Structure", "Use Case"], [
            ["Trie", "Efficient prefix search over a set of strings"],
        ]),
        "formulae": ["class TrieNode:\n    def __init__(self):\n        self.children = {}\n        self.is_word = False"],
    },
    "coding-c2-l22": {
        "data_table": table(["Structure", "Operation Cost"], [
            ["Binary heap", "O(log n) insert and extract-min"],
        ]),
        "formulae": ["import heapq\nheap = []\nheapq.heappush(heap, 5)\nheapq.heappush(heap, 1)\nheapq.heappop(heap)"],
    },
    "coding-c2-l23": {
        "data_table": table(["Structure", "Use Case"], [
            ["Disjoint Set Union", "Tracks connected components with near-O(1) union/find"],
        ]),
    },
    "coding-c2-l24": {
        "data_table": table(["Algorithm", "Use Case"], [
            ["Topological sort", "Orders tasks in a directed acyclic graph respecting dependencies"],
        ]),
    },
    "coding-c2-l25": {
        "data_table": table(["Algorithm", "Approach"], [
            ["Kruskal's algorithm", "Sorts edges and adds them using union-find to avoid cycles"],
            ["Prim's algorithm", "Grows the tree greedily from a starting vertex"],
        ]),
    },
    "coding-c2-l26": {
        "data_table": table(["Technique", "Use"], [
            ["Bitmask DP", "Represents subsets as bits to solve combinatorial optimization problems"],
        ]),
    },
    "coding-c2-l27": {
        "data_table": table(["Algorithm", "Approach"], [
            ["KMP", "Uses a prefix table to avoid re-scanning matched characters"],
            ["Rabin-Karp", "Uses rolling hashes to find pattern matches"],
        ]),
    },
    "coding-c2-l28": {
        "data_table": table(["Algorithm", "Time Complexity"], [
            ["Heap sort", "O(n log n), in-place"], ["Radix sort", "O(nk) for k-digit keys"],
        ]),
    },
    "coding-c2-l29": {
        "data_table": table(["Class", "Meaning"], [
            ["P", "Solvable in polynomial time"], ["NP-complete", "Hardest problems in NP, no known polynomial solution"],
        ]),
    },
    "coding-c2-l30": {
        "data_table": table(["Method", "Purpose"], [
            ["Amortized analysis", "Averages cost over a sequence of operations, e.g. dynamic array resizing"],
        ]),
    },
    "coding-c2-l31": {
        "data_table": table(["Principle", "Meaning"], [
            ["Single Responsibility", "A class should have only one reason to change"],
            ["Open/Closed", "Open for extension, closed for modification"],
        ]),
    },
    "coding-c2-l32": {
        "data_table": table(["Pattern", "Purpose"], [
            ["Adapter", "Converts one interface into another expected by clients"],
            ["Decorator", "Adds behavior to an object without altering its class"],
        ]),
    },
    "coding-c2-l33": {
        "data_table": table(["Pattern", "Purpose"], [
            ["Observer", "Notifies dependents automatically when subject state changes"],
            ["Strategy", "Encapsulates interchangeable algorithms behind a common interface"],
        ]),
    },
    "coding-c2-l34": {
        "data_table": table(["Layer", "Responsibility"], [
            ["Presentation", "Handles user interaction"], ["Business logic", "Applies domain rules"], ["Data access", "Persists and retrieves data"],
        ]),
    },
    "coding-c2-l35": {
        "data_table": table(["Component", "Role"], [
            ["Event producer", "Emits events describing state changes"],
            ["Event consumer", "Reacts to events asynchronously"],
        ]),
    },
    "coding-c2-l36": {
        "data_table": table(["Test Type", "Scope"], [
            ["Integration test", "Verifies multiple components work together"],
            ["End-to-end test", "Verifies a full user workflow through the system"],
        ]),
    },
    "coding-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Mock", "A test double that verifies interactions occurred"],
            ["Stub", "A test double that returns canned responses"],
        ]),
        "formulae": ["from unittest.mock import Mock\nservice = Mock()\nservice.get_data.return_value = 42\nassert service.get_data() == 42"],
    },
    "coding-c2-l38": {
        "data_table": table(["Tool", "Purpose"], [
            ["Profiler", "Measures where time and memory are spent during execution"],
        ]),
    },
    "coding-c2-l39": {
        "data_table": table(["Operation", "Effect"], [
            ["Rebase", "Replays commits onto a new base, producing a linear history"],
            ["Cherry-pick", "Applies a specific commit from one branch onto another"],
        ]),
        "formulae": ["git rebase main\ngit cherry-pick abc1234"],
    },
    "coding-c2-l40": {
        "data_table": table(["Stage", "Purpose"], [
            ["Lint", "Enforces code style and catches common errors"],
            ["Deploy gate", "Blocks release until all checks pass"],
        ]),
    },
    "coding-c2-l41": {
        "data_table": table(["Strategy", "Detail"], [
            ["Mark-and-sweep", "Marks reachable objects, then frees the rest"],
            ["Reference counting", "Frees an object when its reference count reaches zero"],
        ]),
    },
    "coding-c2-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Thread pool", "Reuses a fixed set of worker threads to execute tasks"],
            ["Async/await", "Non-blocking concurrency using coroutines"],
        ]),
        "formulae": ["import asyncio\nasync def fetch():\n    await asyncio.sleep(1)\n    return 'done'\nasyncio.run(fetch())"],
    },
    "coding-c2-l43": {
        "data_table": table(["Problem", "Cause"], [
            ["Deadlock", "Circular waiting for resources held by other threads"],
            ["Lock-free structure", "Uses atomic operations to avoid locking entirely"],
        ]),
    },
    "coding-c2-l44": {
        "data_table": table(["API Style", "Feature"], [
            ["GraphQL", "Clients request exactly the fields they need in a single query"],
        ]),
        "formulae": ["query { user(id: 1) { name email } }"],
    },
    "coding-c2-l45": {
        "data_table": table(["Practice", "Detail"], [
            ["Resource-based URLs", "Nouns represent resources, HTTP verbs represent actions"],
            ["Versioning", "Prevents breaking existing clients when the API evolves"],
        ]),
    },
    "coding-c2-l46": {
        "data_table": table(["Concept", "Meaning"], [
            ["Authentication", "Verifies who a user is"],
            ["Authorization", "Determines what an authenticated user may do"],
        ]),
    },
    "coding-c2-l47": {
        "data_table": table(["Practice", "Purpose"], [
            ["Input validation", "Rejects malformed or malicious input before it's processed"],
            ["Parameterized queries", "Prevents SQL injection by separating code from data"],
        ]),
    },
    "coding-c2-l48": {
        "data_table": table(["Normal Form", "Rule"], [
            ["1NF", "Atomic column values, no repeating groups"],
            ["3NF", "No transitive dependency on the primary key"],
        ]),
    },
    "coding-c2-l49": {
        "data_table": table(["Concept", "Purpose"], [
            ["Index", "Speeds up lookups at the cost of extra storage and write overhead"],
            ["Query optimization", "Restructures queries and schema for faster execution plans"],
        ]),
    },
    "coding-c2-l50": {
        "data_table": table(["Layer", "Purpose"], [
            ["Cache", "Stores frequently accessed data in fast storage to reduce load"],
        ]),
    },
    "coding-c2-l51": {
        "data_table": table(["Component", "Role"], [
            ["Message queue", "Decouples producers and consumers for asynchronous processing"],
        ]),
    },
    "coding-c2-l52": {
        "data_table": table(["Format", "Use"], [
            ["OpenAPI spec", "Machine-readable description of a REST API's endpoints"],
        ]),
    },
    "coding-c2-l53": {
        "data_table": table(["Practice", "Purpose"], [
            ["Safe refactoring", "Small, test-covered steps preserve behavior while improving structure"],
        ]),
    },
    "coding-c2-l54": {
        "data_table": table(["Practice", "Benefit"], [
            ["Small pull requests", "Easier and faster for reviewers to give meaningful feedback"],
        ]),
    },
    "coding-c2-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Dependency graph", "Determines build order and enables incremental, parallel builds"],
        ]),
    },
    "coding-c2-l56": {
        "data_table": table(["Concept", "Purpose"], [
            ["Container image", "Packages an app with its dependencies for consistent deployment"],
        ]),
        "formulae": ["FROM python:3.12-slim\nCOPY . /app\nWORKDIR /app\nRUN pip install -r requirements.txt\nCMD [\"python\", \"main.py\"]"],
    },
    "coding-c2-l57": {
        "data_table": table(["Ceremony", "Purpose"], [
            ["Sprint planning", "Selects and estimates work for the upcoming iteration"],
            ["Retrospective", "Reflects on process to identify improvements"],
        ]),
    },
    "coding-c2-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Technical debt", "Shortcuts taken now that create extra rework later"],
        ]),
    },
    "coding-c2-l59": {
        "data_table": table(["Step", "Action"], [
            ["Contributing to open source", "Fork, branch, implement, and open a pull request against the upstream project"],
        ]),
    },
    "coding-c2-l60": {
        "data_table": table(["Concern", "Approach"], [
            ["Scalability", "Design services to handle growing load via horizontal scaling"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Case", "Meaning"], [
    ["Best case", "Minimum time/steps needed"],
    ["Worst case", "Maximum time/steps needed"],
    ["Average case", "Expected time/steps over typical input"],
])

# l61-l64 revisit earlier design-pattern lessons.
FOUNDATIONS_MAP = {61: 32, 62: 33, 63: 47, 64: 11}
for worked_n, base_n in FOUNDATIONS_MAP.items():
    base_key = f"coding-c2-l{base_n}"
    CHARTS[f"coding-c2-l{worked_n}"] = {
        "data_table": CHARTS[base_key]["data_table"],
    }

# l65-l70 "Worked Analysis" lessons reuse the data_table of l1-l6.
WORKED_ANALYSIS_MAP = {65: 1, 66: 2, 67: 3, 68: 4, 69: 5, 70: 6}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"coding-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"coding-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"coding-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Coding lessons (completing 70/70).")


if __name__ == "__main__":
    main()
