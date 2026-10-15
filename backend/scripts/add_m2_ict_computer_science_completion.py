#!/usr/bin/env python3
"""Depth pass, M2 ICT & Computer Science: fill in real, hand-checked
data_table content for the M2 ICT & Computer Science lessons not
covered by the earlier breadth-first batch. Brings M2 ICT & Computer
Science to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
distributed systems and consensus, compilers and program analysis,
security and cryptography, computer architecture, databases, and
formal methods; l101-l120 are "Worked Analysis" companions reusing the
data_table of l1-l20 (direct 1:1 mapping). l3 was already completed by
an earlier breadth-first batch, so its data_table is hard-coded here
for reuse (it falls within l1-l20, so it is also reused for l103).

Lesson-id quirk (same as M1): l1-l100 use the
"ict-and-computer-science-m2-" prefix while l101-l120 use the shorter
"ict-computer-science-m2-" prefix (no "and").

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_ict_computer_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Byzantine fault", "A node failure where the faulty node can behave arbitrarily, including sending conflicting messages"],
    ["Byzantine fault tolerance", "A consensus protocol's ability to reach agreement despite up to f arbitrarily faulty nodes out of 3f+1"],
])

CHARTS: dict[str, dict] = {
    "ict-and-computer-science-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Advanced computing research", "Graduate-level methods for designing, implementing, and rigorously evaluating systems and algorithms"],
        ["Research topic selection", "Chosen by identifying a genuine gap between current system capabilities and a well-motivated requirement"],
    ])},
    "ict-and-computer-science-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Computer systems fundamentals", "The layered stack of hardware, operating system, and runtime that underlies all higher-level software"],
        ["Systems research method", "Combines building a working prototype with quantitative benchmarking against a clear baseline"],
    ])},
    "ict-and-computer-science-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["CRDT", "A conflict-free replicated data type designed so concurrent updates always converge without coordination"],
        ["Strong eventual consistency", "The guarantee CRDTs provide: replicas that received the same updates end in the same state"],
    ])},
    "ict-and-computer-science-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Model checking", "Exhaustively explores a concurrent program's reachable states to verify a property holds in all of them"],
        ["State explosion", "The central challenge of model checking: reachable state counts grow exponentially with concurrent components"],
    ])},
    "ict-and-computer-science-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Homomorphic encryption", "Allows computation directly on encrypted data, producing an encrypted result that decrypts to the correct answer"],
        ["Fully homomorphic encryption", "Supports arbitrary computation (both addition and multiplication) on ciphertexts, not just one operation"],
    ])},
    "ict-and-computer-science-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["zk-SNARK", "A succinct non-interactive zero-knowledge proof letting a prover convince a verifier a statement is true without revealing why"],
        ["Succinctness", "Proofs are small and fast to verify regardless of the size of the underlying computation"],
    ])},
    "ict-and-computer-science-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Quantum error correction", "Encodes logical qubits redundantly across physical qubits to detect and correct decoherence errors"],
        ["Fault tolerance threshold", "The physical error rate below which increasing code distance actually reduces the logical error rate"],
    ])},
    "ict-and-computer-science-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Software-defined networking", "Separates the network's control plane (decision logic) from its data plane (packet forwarding)"],
        ["Control plane", "A centralized controller programs forwarding behavior across the network via a standard protocol like OpenFlow"],
    ])},
    "ict-and-computer-science-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Side-channel attack", "Extracts secret information from a system's physical implementation (timing, power, cache) rather than a logical flaw"],
        ["Microarchitectural attack", "Exploits shared CPU resources like caches or speculative execution buffers, e.g. Spectre and Meltdown"],
    ])},
    "ict-and-computer-science-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive optimization", "A managed runtime recompiles hot code paths with increasingly aggressive optimizations based on observed profiling data"],
        ["JIT tiering", "Runs code first in an interpreter or baseline compiler, then promotes frequently executed methods to an optimizing compiler"],
    ])},
    "ict-and-computer-science-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Abstract interpretation", "Analyzes a program by executing it over an abstract domain that soundly over-approximates concrete behavior"],
        ["Soundness", "Guarantees the analysis never misses a real bug, at the cost of potential false positives"],
    ])},
    "ict-and-computer-science-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Dependent type theory", "Types that can depend on values, letting a type itself express a precise specification"],
        ["Proof assistant", "A tool (e.g. Coq, Agda) that uses dependent types to let a machine check the correctness of a formal proof"],
    ])},
    "ict-and-computer-science-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Distributed hash table", "A decentralized key-value store where each node is responsible for a portion of the keyspace"],
        ["Overlay network", "A logical network built on top of an existing network, routing among peers by key rather than physical address"],
    ])},
    "ict-and-computer-science-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Paxos", "A consensus protocol proving nodes can agree on a single value despite failures, but notoriously hard to understand"],
        ["Raft", "A consensus protocol designed for understandability, decomposing consensus into leader election, log replication, and safety"],
    ])},
    "ict-and-computer-science-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Memory consistency model", "Defines what values a read is allowed to return in a multiprocessor system with concurrent writes"],
        ["Sequential consistency", "The strongest common model: operations appear to execute in a single global order consistent with each processor's program order"],
    ])},
    "ict-and-computer-science-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Garbage collection", "Automatically reclaims memory no longer reachable by the running program"],
        ["Low-latency GC", "Techniques like concurrent and generational collection minimize pause times for latency-sensitive applications"],
    ])},
    "ict-and-computer-science-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Cost-based query optimization", "Chooses among equivalent query execution plans by estimating and comparing their execution cost"],
        ["Cardinality estimation", "Predicts the number of rows each operator will produce, driving the optimizer's plan cost estimates"],
    ])},
    "ict-and-computer-science-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Column-store", "Stores each column contiguously rather than each row, improving scan performance for analytical queries"],
        ["Analytical workload", "Characterized by scans over few columns across many rows, well-suited to column-store compression and vectorization"],
    ])},
    "ict-and-computer-science-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Vector clock", "A per-node counter vector that tracks causal (happens-before) ordering across a distributed system"],
        ["Causal consistency", "Guarantees that causally related operations are seen in the same order by every replica"],
    ])},
    "ict-and-computer-science-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Sharding", "Partitions a dataset across multiple nodes so each holds only a subset, enabling horizontal scale"],
        ["Sharding strategy", "Range-based, hash-based, and directory-based approaches trade off load balance against range-query efficiency"],
    ])},
    "ict-and-computer-science-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Register allocation", "Assigns a program's variables to a limited set of physical CPU registers"],
        ["Graph coloring", "Models register allocation as coloring an interference graph so no two conflicting variables share a color"],
    ])},
    "ict-and-computer-science-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Static single assignment", "An intermediate representation where each variable is assigned exactly once, simplifying data-flow analysis"],
        ["Phi function", "A construct that merges values from different control-flow predecessors at a join point in SSA form"],
    ])},
    "ict-and-computer-science-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["SAT solver", "Determines whether a boolean formula can be satisfied, used as an engine for many verification tasks"],
        ["SMT solver", "Extends SAT solving to formulas over richer theories, such as arithmetic and arrays, common in hardware verification"],
    ])},
    "ict-and-computer-science-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Capability-based security", "Grants access via unforgeable tokens (capabilities) rather than checking an identity against an access list"],
        ["Principle of least authority", "A process is given only the specific capabilities it needs, limiting the damage from a compromise"],
    ])},
    "ict-and-computer-science-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Kubernetes scheduler", "Assigns newly created pods to nodes based on resource requirements, constraints, and affinity rules"],
        ["Scheduling algorithm", "Filters nodes that satisfy hard constraints, then scores and ranks the remaining candidates to pick the best fit"],
    ])},
    "ict-and-computer-science-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Erasure coding", "Encodes data into fragments with redundancy so the original can be reconstructed from a subset of fragments"],
        ["Storage efficiency", "Achieves fault tolerance comparable to replication with substantially less storage overhead"],
    ])},
    "ict-and-computer-science-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Approximate computing", "Deliberately trades a controlled amount of output accuracy for reduced energy consumption"],
        ["Error-resilient application", "Domains like multimedia and machine learning inference tolerate small approximation errors, making them good candidates"],
    ])},
    "ict-and-computer-science-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["RISC-V", "An open, extensible instruction set architecture allowing custom instruction extensions"],
        ["ISA extension design", "Adds domain-specific instructions (e.g. vector or crypto operations) while preserving the base ISA's compatibility"],
    ])},
    "ict-and-computer-science-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Branch prediction", "Guesses the outcome of a conditional branch before it is resolved to keep the pipeline full"],
        ["Speculative execution", "Executes instructions along the predicted path before confirming correctness, rolling back on misprediction"],
    ])},
    "ict-and-computer-science-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Lattice-based cryptography", "Builds cryptographic hardness on lattice problems believed resistant to both classical and quantum attacks"],
        ["Post-quantum cryptography", "Cryptographic schemes designed to remain secure even against an adversary with a large-scale quantum computer"],
    ])},
    "ict-and-computer-science-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy", "A mathematical guarantee that a query's output changes negligibly whether or not any single individual's data is included"],
        ["Privacy budget", "A parameter (epsilon) bounding the cumulative privacy loss across multiple queries on the same dataset"],
    ])},
    "ict-and-computer-science-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Secure multi-party computation", "Lets multiple parties jointly compute a function over their private inputs without revealing those inputs to each other"],
        ["Threat model", "Protocols are designed against specific adversary assumptions, e.g. semi-honest or actively malicious participants"],
    ])},
    "ict-and-computer-science-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Trusted execution environment", "An isolated, hardware-protected region of a processor that runs code with confidentiality and integrity guarantees"],
        ["Remote attestation", "Lets a TEE prove to a remote party that it is running genuine, unmodified code"],
    ])},
    "ict-and-computer-science-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Software transactional memory", "Manages concurrent memory access using transactions that commit atomically or abort and retry on conflict"],
        ["Optimistic concurrency", "STM assumes conflicts are rare and detects them at commit time rather than locking preemptively"],
    ])},
    "ict-and-computer-science-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Actor model", "Concurrent computation via independent actors that communicate only by asynchronous message passing"],
        ["Let it crash", "Erlang/OTP's fault-tolerance philosophy: isolate failures to a single actor and let a supervisor restart it cleanly"],
    ])},
    "ict-and-computer-science-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Operational semantics", "Defines a program's meaning as a sequence of execution steps over an abstract machine"],
        ["Denotational semantics", "Defines a program's meaning as a mathematical object (a function) independent of any particular execution mechanism"],
    ])},
    "ict-and-computer-science-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Category theory in FP", "Provides abstractions like functors and monads that formalize common patterns of composition in functional programs"],
        ["Monad", "An abstraction for sequencing computations that carry an effect, such as optionality, state, or I/O"],
    ])},
    "ict-and-computer-science-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Verified software development", "Uses a proof-assistant language to write code alongside a machine-checked proof of its correctness"],
        ["Idris and Lean", "Dependently typed languages that let a function's type encode a formal specification the implementation must satisfy"],
    ])},
    "ict-and-computer-science-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Graph neural network", "A neural architecture that learns representations by passing messages along the edges of a graph"],
        ["GNN accelerator", "Specialized hardware exploiting the sparse, irregular memory access pattern of graph message passing"],
    ])},
    "ict-and-computer-science-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Approximate nearest neighbor search", "Finds points close to a query point without guaranteeing the exact nearest neighbor, trading accuracy for speed"],
        ["Scale techniques", "Index structures like HNSW and product quantization enable sub-linear search over billions of vectors"],
    ])},
    "ict-and-computer-science-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Bloom filter", "A space-efficient probabilistic structure testing set membership with possible false positives but no false negatives"],
        ["Beyond Bloom filters", "Structures like Cuckoo filters and count-min sketches support deletion or frequency estimation that plain Bloom filters cannot"],
    ])},
    "ict-and-computer-science-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Consistent hashing", "Maps both data and nodes onto a hash ring so adding or removing a node remaps only a small fraction of keys"],
        ["Load distribution", "Virtual nodes improve balance by giving each physical node multiple positions on the ring"],
    ])},
    "ict-and-computer-science-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["CUBIC", "A loss-based congestion control algorithm that grows the congestion window as a cubic function of time since the last loss"],
        ["BBR", "A model-based congestion control algorithm that estimates bottleneck bandwidth and round-trip time to pace sending directly"],
    ])},
    "ict-and-computer-science-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["SD-WAN", "Applies software-defined networking principles to manage and route traffic across a wide-area network"],
        ["Benefit", "Centralized policy control lets traffic dynamically shift across multiple WAN links based on performance and cost"],
    ])},
    "ict-and-computer-science-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Edge computing", "Moves computation closer to data sources to reduce latency and bandwidth use"],
        ["Resource allocation", "Must balance limited edge-node capacity against the latency benefit of processing locally rather than in the cloud"],
    ])},
    "ict-and-computer-science-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Cold start", "The latency penalty incurred when a serverless platform must initialize a new execution environment for a function"],
        ["Optimization technique", "Pre-warming, snapshotting, and lightweight sandboxing all reduce cold-start latency"],
    ])},
    "ict-and-computer-science-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Chaos engineering", "Deliberately injects failures into a production system to verify it degrades gracefully"],
        ["Distributed resilience", "Validates assumptions about fault tolerance empirically rather than relying solely on design-time analysis"],
    ])},
    "ict-and-computer-science-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["TLA+", "A formal specification language for modeling and model-checking the behavior of concurrent and distributed systems"],
        ["Alloy", "A lightweight formal modeling language that uses constraint solving to find counterexamples to a specification"],
    ])},
    "ict-and-computer-science-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Program synthesis", "Automatically generates a program that satisfies a given specification"],
        ["Syntax-guided synthesis", "Constrains the search to programs expressible within a specified grammar, making synthesis tractable"],
    ])},
    "ict-and-computer-science-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Symbolic execution", "Runs a program with symbolic rather than concrete inputs, collecting path constraints along each explored branch"],
        ["Test generation", "Solving a path's collected constraints yields concrete input values that exercise that specific path"],
    ])},
    "ict-and-computer-science-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Fuzzing", "Automatically generates diverse inputs to a program to discover crashes and vulnerabilities"],
        ["Coverage-guided fuzzing", "Uses code coverage feedback to prioritize mutating inputs that reach previously unexplored code paths"],
    ])},
    "ict-and-computer-science-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic binary instrumentation", "Inserts analysis code into a running binary without access to its source, e.g. via Pin or DynamoRIO"],
        ["Use case", "Enables fine-grained runtime profiling, memory-error detection, and taint tracking on unmodified executables"],
    ])},
    "ict-and-computer-science-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Control-flow integrity", "Restricts a program's indirect control transfers to a precomputed set of legitimate targets"],
        ["Defense goal", "Prevents attackers from hijacking execution flow via techniques such as return-oriented programming"],
    ])},
    "ict-and-computer-science-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Federated learning", "Trains a shared model across decentralized devices without moving their raw data to a central server"],
        ["Communication efficiency", "Techniques like gradient compression and local update aggregation reduce the bandwidth cost of federated training rounds"],
    ])},
    "ict-and-computer-science-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Proof-of-work", "Requires solving a computationally expensive puzzle to propose the next block, securing consensus via wasted energy"],
        ["Beyond proof-of-work", "Proof-of-stake and BFT-style protocols achieve consensus with far lower energy cost by weighting or voting instead"],
    ])},
    "ict-and-computer-science-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Smart contract", "Self-executing code deployed on a blockchain whose logic and state are enforced by the network"],
        ["Formal verification", "Mathematically proves a contract's code satisfies its intended specification, catching bugs before costly deployment"],
    ])},
    "ict-and-computer-science-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Merkle tree", "A tree of hashes where each parent hash commits to its children, letting any leaf be verified against a single root hash"],
        ["Content-addressable storage", "Stores and retrieves data by the hash of its content rather than by a location-based name"],
    ])},
    "ict-and-computer-science-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Real-time scheduling", "Assigns CPU time to tasks so that each meets its deadline, not merely to maximize throughput"],
        ["Rate-monotonic scheduling", "A classic fixed-priority scheme assigning higher priority to tasks with shorter periods"],
    ])},
    "ict-and-computer-science-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Worst-case execution time", "The longest possible time a piece of code can take to execute on given hardware"],
        ["WCET analysis", "Combines control-flow analysis with hardware timing models to derive a safe upper bound, critical for real-time guarantees"],
    ])},
    "ict-and-computer-science-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Hardware-software co-design", "Jointly optimizes an application's algorithm and its custom hardware implementation rather than designing each in isolation"],
        ["Accelerator", "Specialized hardware (e.g. an ASIC or FPGA) built to execute a specific computation far more efficiently than a general CPU"],
    ])},
    "ict-and-computer-science-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Dataflow compiler", "Compiles high-level tensor operations into a dataflow graph optimized for execution on specialized hardware"],
        ["Tensor processing unit", "An accelerator architecture optimized for the matrix-multiply-heavy dataflow common in machine learning workloads"],
    ])},
    "ict-and-computer-science-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Approximate query processing", "Returns a statistically bounded approximate answer to a query far faster than computing the exact result"],
        ["Sampling-based approach", "Runs a query over a representative sample of the data and reports the estimate along with a confidence interval"],
    ])},
    "ict-and-computer-science-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Exactly-once semantics", "Guarantees each input record affects the output state exactly one time, even if the stream processor restarts after a failure"],
        ["Implementation approach", "Achieved via idempotent writes or two-phase commit combined with durable checkpointing of processing state"],
    ])},
    "ict-and-computer-science-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Lambda architecture", "Combines a batch layer for accuracy with a speed layer for low-latency approximate results, later reconciled"],
        ["Kappa architecture", "Simplifies lambda architecture by processing all data, batch and real-time, through a single stream-processing pipeline"],
    ])},
    "ict-and-computer-science-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Graph database", "Stores data as nodes and relationships, optimized for traversal-heavy queries over connected data"],
        ["Query optimization", "Graph query planners must estimate the cost of traversal paths, which differs fundamentally from relational join optimization"],
    ])},
    "ict-and-computer-science-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Information-theoretic security", "Security that holds even against an adversary with unlimited computational power, based on entropy arguments"],
        ["One-time pad", "The classic example: provably unbreakable given a truly random, single-use key as long as the message"],
    ])},
    "ict-and-computer-science-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Physical-layer security", "Exploits the physical properties of a wireless channel (e.g. noise, fading) to secure communication without cryptography"],
        ["Wiretap channel", "A foundational model where secure communication is possible if the eavesdropper's channel is noisier than the legitimate one"],
    ])},
    "ict-and-computer-science-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive radio", "A radio that senses its spectral environment and dynamically adapts its transmission parameters to avoid interference"],
        ["Software-defined radio", "Implements radio signal processing in software rather than fixed hardware, enabling flexible, reconfigurable radios"],
    ])},
    "ict-and-computer-science-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Information-centric networking", "Routes and caches data by content name rather than by the location (IP address) of a host"],
        ["Named data networking", "A prominent ICN architecture where routers can cache and serve named content directly, reducing redundant transfers"],
    ])},
    "ict-and-computer-science-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Access control model", "A formal specification of who may perform which operations on which resources under what conditions"],
        ["RBAC vs. ABAC", "Role-based access control grants permissions via roles; attribute-based access control evaluates policies over dynamic attributes"],
    ])},
    "ict-and-computer-science-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Network intrusion detection", "Monitors network traffic to identify patterns indicating an attack or policy violation"],
        ["Machine learning approach", "Learns a model of normal traffic and flags statistically anomalous behavior, complementing signature-based detection"],
    ])},
    "ict-and-computer-science-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Automated theorem proving", "Software that searches for a formal proof of a logical statement, often over a very large search space"],
        ["Heuristic guidance", "Prunes and orders the proof search using domain heuristics or learned models to make an intractable search feasible"],
    ])},
    "ict-and-computer-science-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Shor's algorithm", "A quantum algorithm that factors large integers in polynomial time, threatening RSA-based cryptography"],
        ["Grover's algorithm", "A quantum algorithm giving a quadratic speedup for unstructured search, halving the effective security of symmetric keys"],
    ])},
    "ict-and-computer-science-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Qubit mapping", "Assigns a quantum circuit's logical qubits to a device's physical qubits, respecting hardware connectivity constraints"],
        ["Quantum circuit compilation", "Transforms and optimizes a circuit for a target device, including inserting SWAP gates to satisfy connectivity"],
    ])},
    "ict-and-computer-science-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["DNA data storage", "Encodes digital data as sequences of nucleotide bases for extremely dense, durable long-term archival storage"],
        ["Encoding scheme", "Must map binary data to DNA bases while avoiding sequences prone to synthesis or sequencing errors"],
    ])},
    "ict-and-computer-science-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Reversible computing", "Computation in which every step can be logically undone, in principle avoiding the energy cost of information erasure"],
        ["Landauer's principle", "Erasing one bit of information necessarily dissipates at least kT ln(2) of energy as heat"],
    ])},
    "ict-and-computer-science-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Self-stabilizing algorithm", "Guarantees a distributed system converges to a correct configuration from any starting state, without external intervention"],
        ["Practical value", "Provides automatic recovery from transient faults such as memory corruption, without needing explicit fault detection"],
    ])},
    "ict-and-computer-science-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Gossip protocol", "Nodes periodically exchange state with a random subset of peers, spreading information epidemically across the network"],
        ["Epidemic dissemination", "Achieves eventual, high-probability delivery to all nodes with a simple, decentralized, fault-tolerant mechanism"],
    ])},
    "ict-and-computer-science-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Software aging", "Gradual degradation of a long-running system's performance or reliability due to resource leaks and state accumulation"],
        ["Software rejuvenation", "Proactively restarting or resetting a system's state before aging leads to failure"],
    ])},
    "ict-and-computer-science-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Verified compiler", "A compiler accompanied by a machine-checked proof that compiled code preserves the semantics of the source program"],
        ["CompCert", "A landmark verified C compiler whose formal correctness proof rules out an entire class of miscompilation bugs"],
    ])},
    "ict-and-computer-science-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Happens-before relation", "A partial order capturing which events in a concurrent execution could have causally affected which others"],
        ["Concurrency bug analysis", "Detects data races and other bugs by checking whether conflicting accesses are unordered by happens-before"],
    ])},
    "ict-and-computer-science-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["GPU memory hierarchy", "Spans registers, shared memory, and global memory, each with very different latency and bandwidth characteristics"],
        ["Optimization goal", "Maximizes reuse of data in fast on-chip memory to avoid the high latency cost of global memory accesses"],
    ])},
    "ict-and-computer-science-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Domain-specific language", "A language with notation and abstractions tailored to a particular problem domain rather than general-purpose use"],
        ["Scientific computing DSL", "Lets domain experts express numerical algorithms concisely while the compiler handles low-level performance optimization"],
    ])},
    "ict-and-computer-science-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Program slicing", "Extracts the subset of a program's statements that could affect the value of a variable at a chosen point"],
        ["Impact analysis", "Uses slicing to estimate which parts of a codebase are affected by a proposed change before making it"],
    ])},
    "ict-and-computer-science-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Architecture recovery", "Reconstructs a system's high-level architectural structure from its source code when documentation is missing or stale"],
        ["Technique", "Clusters modules by dependency and coupling patterns to infer likely architectural boundaries"],
    ])},
    "ict-and-computer-science-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Service mesh", "A dedicated infrastructure layer that manages service-to-service communication for a microservices system"],
        ["Sidecar proxy", "The common implementation pattern: a proxy deployed alongside each service instance handles routing, retries, and observability"],
    ])},
    "ict-and-computer-science-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Consumer-driven contract testing", "Consumers of an API define expectations as contracts that the provider's implementation is automatically tested against"],
        ["Benefit", "Catches breaking API changes before deployment without requiring full end-to-end integration test environments"],
    ])},
    "ict-and-computer-science-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Explainable static analysis", "Produces not just a list of flagged issues but a human-understandable justification for each finding"],
        ["Security auditing value", "Explanations help auditors quickly triage true positives from false positives in large codebases"],
    ])},
    "ict-and-computer-science-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Energy proportionality", "A data center design goal where power consumption scales proportionally with actual utilization"],
        ["Design implication", "Idle and lightly loaded servers should consume dramatically less power than fully utilized ones"],
    ])},
    "ict-and-computer-science-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Thermal-aware scheduling", "Assigns tasks to cores accounting for temperature, not just load, to avoid hotspots and throttling"],
        ["Multi-core benefit", "Balancing heat generation across cores can improve sustained performance by delaying thermal throttling"],
    ])},
    "ict-and-computer-science-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Persistent memory", "Byte-addressable memory that retains data across power loss while offering near-DRAM speed"],
        ["Programming model", "Requires new abstractions to ensure crash consistency, since a program can be interrupted mid-write to persistent state"],
    ])},
    "ict-and-computer-science-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Data provenance", "Tracks the origin and transformation history of data as it moves through a computational pipeline"],
        ["Scientific workflow", "Provenance enables reproducibility by recording exactly which inputs, code versions, and parameters produced a given result"],
    ])},
    "ict-and-computer-science-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Accessibility engineering", "Designs and verifies software so it is usable by people with a wide range of abilities and assistive technologies"],
        ["Formal methods application", "Model checking and specification techniques can verify accessibility properties hold across all reachable UI states"],
    ])},
    "ict-and-computer-science-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Autonomous vehicle verification", "Applies formal and testing-based methods to establish safety guarantees for self-driving software"],
        ["Challenge", "The near-infinite space of real-world driving scenarios makes exhaustive testing infeasible, motivating formal and simulation-based approaches"],
    ])},
    "ict-and-computer-science-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Reproducible build", "A build process that deterministically produces bit-for-bit identical output from the same source, independently verifiable"],
        ["Supply chain security", "Reproducibility lets third parties confirm a distributed binary genuinely corresponds to its published source code"],
    ])},
    "ict-and-computer-science-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Auto-vectorization", "A compiler technique that automatically transforms scalar loop code into SIMD instructions operating on multiple data elements"],
        ["SIMD architecture", "Single-instruction-multiple-data hardware executes the same operation across a vector of values in one cycle"],
    ])},
    "ict-and-computer-science-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Live migration", "Moves a running virtual machine or container between physical hosts with minimal service interruption"],
        ["Technique", "Iteratively copies memory pages while the source keeps running, then performs a brief final pause to transfer remaining state"],
    ])},
    "ict-and-computer-science-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Master's thesis seminar", "A forum for presenting and defending original systems or software research to faculty and peers"],
        ["Systems research", "Emphasizes building and empirically evaluating a working artifact, not just theoretical analysis"],
    ])},
    "ict-and-computer-science-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Neuromorphic computing", "Hardware architectures that mimic the brain's structure, using spiking neurons and event-driven computation"],
        ["Spiking neural network", "A neural model where neurons communicate via discrete timed spikes rather than continuous activations, enabling very low power operation"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"ict-and-computer-science-m2-l{base_n}"
        worked_key = f"ict-computer-science-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 ICT & Computer Science lessons.")


if __name__ == "__main__":
    main()
