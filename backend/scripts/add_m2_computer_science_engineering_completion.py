#!/usr/bin/env python3
"""Depth pass, M2 Computer Science Engineering: fill in real,
hand-checked data_table content for the M2 Computer Science
Engineering lessons not covered by the earlier breadth-first batch.
Brings M2 Computer Science Engineering to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning advanced
algorithm design and complexity theory, cryptography and blockchain
security, computer architecture and hardware verification, quantum
and neuromorphic computing, operating systems and storage internals,
networking protocol design, distributed algorithms, programming
language theory and formal methods, ML systems theory (adversarial
robustness, federated learning, GNN theory), database internals,
robotics/computer vision algorithms, and algorithmic game theory;
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_computer_science_engineering_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Approximation algorithm", "Efficiently computes a solution provably close to optimal for an NP-hard problem where exact solving is intractable"],
    ["NP-hard combinatorial optimization", "A class of optimization problems believed to have no known efficient exact algorithm, motivating approximation approaches"],
])

CHARTS: dict[str, dict] = {
    "computer-science-engineering-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Advanced algorithms", "Sophisticated algorithmic techniques and analysis methods beyond standard undergraduate coverage"],
        ["Application", "Underlies efficient solutions to computationally demanding problems across systems, ML, and theory"],
    ])},
    "computer-science-engineering-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["CSE capstone project", "An applied culminating project demonstrating end-to-end computer science engineering design and implementation skill"],
        ["Deliverable", "Typically a substantial working system or algorithm with rigorous performance and correctness evaluation"],
    ])},
    "computer-science-engineering-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Parameterized complexity", "Analyzes a problem's complexity with respect to a specific parameter, separate from overall input size"],
        ["Fixed-parameter tractability", "A problem is FPT if it can be solved efficiently when the parameter is small, even if the problem is NP-hard in general"],
    ])},
    "computer-science-engineering-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Streaming algorithm", "Processes a data stream using memory far smaller than the full input, typically in a single pass"],
        ["Sublinear space constraint", "Forces algorithms to maintain only a compact summary rather than storing the entire stream"],
    ])},
    "computer-science-engineering-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Randomized algorithm", "Uses random choices during execution to achieve efficiency or simplicity not easily obtained deterministically"],
        ["Concentration inequality analysis", "Tools like Chernoff bounds prove that a randomized algorithm's outcome is tightly concentrated around its expected value"],
    ])},
    "computer-science-engineering-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Online algorithm", "Makes irrevocable decisions as input arrives sequentially, without knowledge of future input"],
        ["Competitive ratio", "Measures an online algorithm's worst-case performance relative to an optimal algorithm with full knowledge in advance"],
    ])},
    "computer-science-engineering-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Distributed consensus lower bound", "A mathematical proof establishing the minimum resources or conditions required for any distributed consensus protocol"],
        ["Example", "The FLP impossibility result proves no deterministic consensus protocol can guarantee termination in an asynchronous system with even one faulty process"],
    ])},
    "computer-science-engineering-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Communication complexity", "Studies the minimum amount of communication needed for distributed parties to jointly compute a function"],
        ["Lower bound", "Proves fundamental limits on how efficiently certain distributed computations can be performed, regardless of algorithm cleverness"],
    ])},
    "computer-science-engineering-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Property testing", "Determines with high probability whether an input has a property or is far from having it, using far fewer than full-input resources"],
        ["Sublinear-time verification", "Achieves this by examining only a small random sample of the input rather than reading it entirely"],
    ])},
    "computer-science-engineering-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Spectral graph theory", "Studies a graph's properties through the eigenvalues and eigenvectors of matrices associated with it"],
        ["Algorithm design application", "Spectral methods underlie efficient algorithms for graph partitioning, clustering, and expansion analysis"],
    ])},
    "computer-science-engineering-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Graph expansion", "Measures how well-connected a graph is, based on how quickly random walks mix or how hard the graph is to disconnect"],
        ["Sparsification", "Constructs a sparser graph that approximately preserves key structural properties of the original, larger graph"],
    ])},
    "computer-science-engineering-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Submodular function", "A set function exhibiting diminishing returns: adding an element helps less as the set it's added to grows larger"],
        ["Optimization algorithm", "Many submodular maximization problems admit efficient algorithms with strong approximation guarantees, unlike general set optimization"],
    ])},
    "computer-science-engineering-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["PAC learning", "A theoretical framework defining what it means for a learning algorithm to probably approximately correctly learn a concept"],
        ["Framework analysis", "Formalizes the relationship between sample complexity, hypothesis class complexity, and achievable learning accuracy"],
    ])},
    "computer-science-engineering-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["VC dimension", "A measure of a hypothesis class's capacity to fit arbitrary labelings of a set of points"],
        ["Generalization bound derivation", "Relates VC dimension and sample size to a mathematically rigorous bound on a learned model's test error"],
    ])},
    "computer-science-engineering-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["TLA+", "A formal specification language for modeling and model-checking the behavior of concurrent and distributed protocols"],
        ["Formal protocol verification", "Enables mathematically proving that a distributed protocol satisfies its intended safety and liveness properties"],
    ])},
    "computer-science-engineering-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Byzantine agreement", "A consensus protocol reaching agreement despite some nodes behaving arbitrarily or maliciously"],
        ["Partial synchrony", "A network model between fully synchronous and fully asynchronous, where message delays are bounded but the bound is unknown"],
    ])},
    "computer-science-engineering-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Proof-of-stake", "A blockchain consensus mechanism where validators are chosen to propose blocks proportional to their staked assets"],
        ["Security analysis", "Analyzes attack vectors like long-range attacks and nothing-at-stake, distinct from proof-of-work's energy-based security model"],
    ])},
    "computer-science-engineering-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Sharding (blockchain)", "Partitions a blockchain's state and transaction processing across multiple parallel shards"],
        ["Scalable throughput design", "Aims to increase overall transaction throughput while maintaining security guarantees across shard boundaries"],
    ])},
    "computer-science-engineering-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Zero-knowledge proof", "Lets a prover convince a verifier a statement is true without revealing any information beyond its truth"],
        ["Privacy-preserving verification", "Enables verifying claims (like transaction validity) without exposing the underlying sensitive data"],
    ])},
    "computer-science-engineering-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Secure multi-party computation", "Lets multiple parties jointly compute a function over their private inputs without revealing those inputs to each other"],
        ["Protocol design", "Designed against specific adversary assumptions, such as semi-honest or actively malicious participants"],
    ])},
    "computer-science-engineering-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Post-quantum cryptography", "Cryptographic algorithms designed to remain secure even against an adversary with a large-scale quantum computer"],
        ["Algorithm design and security analysis", "Typically built on mathematical problems, like lattice problems, believed hard for both classical and quantum computers"],
    ])},
    "computer-science-engineering-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Homomorphic encryption", "Allows computation directly on encrypted data, producing an encrypted result that decrypts to the correct answer"],
        ["Efficiency trade-off", "Fully homomorphic schemes supporting arbitrary computation remain significantly slower than schemes supporting only limited operations"],
    ])},
    "computer-science-engineering-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Side-channel attack", "Extracts secret information from a system's physical implementation rather than a logical flaw"],
        ["Cryptographic hardware analysis", "Analyzes power consumption, timing, or electromagnetic emissions to potentially recover cryptographic keys"],
    ])},
    "computer-science-engineering-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Differential cryptanalysis", "Analyzes how differences in plaintext inputs propagate through a cipher to differences in ciphertext outputs"],
        ["Block cipher security evaluation", "A foundational technique for assessing a block cipher's resistance to structured chosen-plaintext attacks"],
    ])},
    "computer-science-engineering-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Model checking (hardware)", "Exhaustively explores a hardware design's reachable states to verify a property holds in all of them"],
        ["Formal hardware verification", "Catches design bugs before costly fabrication, especially valuable given hardware's high cost of post-production fixes"],
    ])},
    "computer-science-engineering-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Out-of-order execution", "A processor executes instructions in an order determined by data availability rather than strict program order"],
        ["Hazard resolution", "Requires careful handling of data, control, and structural hazards to maintain correct program semantics despite reordering"],
    ])},
    "computer-science-engineering-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Branch prediction", "Guesses the outcome of a conditional branch before it is resolved to keep the pipeline full"],
        ["Pipeline performance optimization", "Accurate prediction is critical since a mispredicted branch wastes the work of speculatively executed instructions"],
    ])},
    "computer-science-engineering-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Cache coherence protocol", "Ensures multiple processor cores see a consistent view of shared memory despite each having its own local cache"],
        ["Multicore design", "Protocols like MESI define states and rules for coordinating cache line ownership and updates across cores"],
    ])},
    "computer-science-engineering-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Non-uniform memory access", "A multiprocessor memory architecture where access time depends on the memory's physical location relative to a given processor"],
        ["Optimization strategy", "Software should favor local memory access over remote access to avoid the higher latency of NUMA remote accesses"],
    ])},
    "computer-science-engineering-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Hardware-software co-design", "Jointly optimizes an application's algorithm and its custom hardware implementation rather than designing each in isolation"],
        ["Domain-specific accelerator", "Specialized hardware built to execute a specific computation far more efficiently than a general-purpose processor"],
    ])},
    "computer-science-engineering-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Systolic array", "A hardware architecture where processing elements rhythmically compute and pass data to neighbors, efficient for matrix operations"],
        ["Matrix computation acceleration", "Widely used in accelerators like TPUs for the matrix-multiply-heavy computations common in deep learning"],
    ])},
    "computer-science-engineering-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Near-memory computing", "Places computational logic physically close to memory to reduce the data-movement bottleneck"],
        ["Data-intensive workload acceleration", "Particularly beneficial for workloads where moving data dominates the total computation cost"],
    ])},
    "computer-science-engineering-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Neuromorphic computing", "Hardware architectures that mimic the brain's structure, using spiking neurons and event-driven computation"],
        ["Spiking neural model", "Neurons communicate via discrete timed spikes rather than continuous activations, enabling very low power operation"],
    ])},
    "computer-science-engineering-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Quantum circuit design", "Constructs sequences of quantum gates to implement a desired quantum computation"],
        ["Gate decomposition optimization", "Breaks complex quantum operations into sequences of simpler, hardware-supported gates while minimizing circuit depth"],
    ])},
    "computer-science-engineering-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Quantum error correction", "Encodes logical qubits redundantly across physical qubits to detect and correct decoherence errors"],
        ["Fault-tolerant computation", "Necessary because physical qubits are highly error-prone, requiring redundancy to perform reliable long computations"],
    ])},
    "computer-science-engineering-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Variational quantum algorithm", "Combines a parameterized quantum circuit with classical optimization to solve problems on near-term quantum hardware"],
        ["Near-term hardware application", "Designed to tolerate the noise and limited qubit counts of current, pre-fault-tolerant quantum computers"],
    ])},
    "computer-science-engineering-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Reversible computing", "Computation in which every step can be logically undone, in principle avoiding the energy cost of information erasure"],
        ["Energy-efficient logic", "Motivated by Landauer's principle, which links irreversible bit erasure to a fundamental minimum energy dissipation"],
    ])},
    "computer-science-engineering-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Approximate computing", "Deliberately trades a controlled amount of output accuracy for reduced energy consumption"],
        ["Energy-constrained system trade-off", "Well suited to error-resilient applications like multimedia processing where perfect precision isn't required"],
    ])},
    "computer-science-engineering-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Real-time scheduling algorithm", "Assigns CPU time to tasks so each meets its deadline, not merely to maximize average throughput"],
        ["Schedulability analysis", "Mathematically determines whether a given task set can be guaranteed to always meet its deadlines under a scheduling policy"],
    ])},
    "computer-science-engineering-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Mixed-criticality system", "A real-time system running tasks with different levels of assurance and consequence-of-failure requirements together"],
        ["Formal schedulability analysis", "Must guarantee high-criticality task deadlines even under degraded conditions where lower-criticality tasks may be dropped"],
    ])},
    "computer-science-engineering-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Microkernel", "An OS design keeping only minimal essential functionality in the privileged kernel, running most services in user space"],
        ["Kernel isolation architecture", "Improves reliability and security by limiting the amount of code that can cause a full system crash if it fails"],
    ])},
    "computer-science-engineering-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Virtual memory management", "Provides each process an abstracted, isolated view of memory, mapped to physical memory by the OS"],
        ["Page replacement optimization", "Algorithms decide which memory pages to evict when physical memory is full, aiming to minimize costly page faults"],
    ])},
    "computer-science-engineering-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Filesystem journaling", "Records intended filesystem changes in a log before applying them, enabling recovery after a crash"],
        ["Crash consistency guarantee", "Ensures the filesystem can be restored to a consistent state after an unexpected power loss or crash"],
    ])},
    "computer-science-engineering-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Copy-on-write filesystem", "Never overwrites data in place; instead writes changes to new locations, preserving the old version"],
        ["Snapshot and versioning support", "Naturally enables efficient point-in-time snapshots, since old data blocks remain intact until no longer referenced"],
    ])},
    "computer-science-engineering-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Distributed shared memory", "Presents physically separate machines' memory as a single, logically shared address space"],
        ["Consistency model design", "Must define precisely what guarantees the system provides about the order and visibility of memory updates across nodes"],
    ])},
    "computer-science-engineering-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Software-defined storage", "Decouples storage management logic from underlying physical storage hardware, enabling flexible, programmable control"],
        ["Disaggregated data center architecture", "Separates compute and storage resources so each can scale independently rather than being tightly coupled in each server"],
    ])},
    "computer-science-engineering-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Congestion control", "Algorithms that adjust a sender's transmission rate to avoid overwhelming network capacity"],
        ["Stability analysis", "Mathematically analyzes whether a congestion control algorithm converges to a stable, fair rate allocation across competing flows"],
    ])},
    "computer-science-engineering-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["SDN controller placement", "Determines optimal locations for centralized SDN controllers to balance latency, reliability, and cost"],
        ["Optimization", "Must account for the trade-off between controller proximity to switches and overall infrastructure resilience"],
    ])},
    "computer-science-engineering-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Named data networking", "Routes and caches data by content name rather than by the location (IP address) of a host"],
        ["Content-centric communication", "Well suited to content distribution scenarios where the specific data matters more than which server currently hosts it"],
    ])},
    "computer-science-engineering-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Network function virtualization", "Replaces dedicated network hardware appliances with software running on standard servers"],
        ["Service chaining optimization", "Optimizes the ordered sequence of virtual network functions (like firewall, load balancer) a packet flow must traverse"],
    ])},
    "computer-science-engineering-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Low-power IoT wireless protocol", "Communication protocols specifically designed to minimize energy consumption for battery-constrained IoT devices"],
        ["Design consideration", "Trades off data rate and range against the extended battery life needed for many practical IoT deployments"],
    ])},
    "computer-science-engineering-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Mobile ad hoc network", "A self-configuring network of mobile devices connecting without fixed infrastructure"],
        ["Routing under topology churn", "Routing protocols must adapt quickly as devices move, join, and leave, continuously changing the network topology"],
    ])},
    "computer-science-engineering-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Automatic parallelization", "A compiler automatically identifies and transforms sequential code to run in parallel where safe to do so"],
        ["Compiler optimization", "Must prove data-dependence safety to parallelize code correctly without introducing race conditions"],
    ])},
    "computer-science-engineering-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Task scheduling (heterogeneous multicore)", "Assigns tasks to different core types (e.g. performance vs. efficiency cores) to optimize overall system objectives"],
        ["Algorithm design", "Must account for varying core capabilities and power characteristics unique to heterogeneous architectures"],
    ])},
    "computer-science-engineering-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Work-stealing scheduler", "Idle processors dynamically \"steal\" queued tasks from busy processors to balance load"],
        ["Dynamic parallel task system application", "Effectively balances load without requiring centralized coordination, well suited to irregular parallel workloads"],
    ])},
    "computer-science-engineering-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["MapReduce", "A programming model that processes large datasets via parallel map and reduce operations across a distributed cluster"],
        ["Dataflow framework design", "Modern frameworks generalize MapReduce into more flexible directed-acyclic-graph dataflow models for complex pipelines"],
    ])},
    "computer-science-engineering-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Checkpoint-restart", "Periodically saves a computation's full state so it can resume from that point after a failure, rather than restarting entirely"],
        ["Fault-tolerant distributed computing", "Reduces the cost of failures in long-running distributed computations by limiting lost work to time since the last checkpoint"],
    ])},
    "computer-science-engineering-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Self-stabilizing algorithm", "Guarantees a distributed system converges to a correct configuration from any starting state, without external intervention"],
        ["Design", "Provides automatic recovery from transient faults such as memory corruption, without needing explicit fault detection"],
    ])},
    "computer-science-engineering-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Distributed hash table", "A decentralized key-value store where each node is responsible for a portion of the keyspace"],
        ["Scalable peer-to-peer lookup", "Enables efficient key lookup across a large network of peers without any centralized directory"],
    ])},
    "computer-science-engineering-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Gossip protocol", "Nodes periodically exchange state with a random subset of peers, spreading information epidemically across the network"],
        ["Epidemic dissemination design", "Achieves eventual, high-probability delivery to all nodes with a simple, decentralized, fault-tolerant mechanism"],
    ])},
    "computer-science-engineering-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Clock synchronization", "Keeps timestamps consistent across distributed nodes despite inherent clock drift"],
        ["Distributed system algorithm design", "Algorithms like NTP or more advanced protocols bound the maximum clock skew achievable across a distributed system"],
    ])},
    "computer-science-engineering-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Vector clock", "A per-node counter vector that tracks causal (happens-before) ordering across a distributed system"],
        ["Interval tree clock", "A more scalable causality-tracking mechanism that avoids vector clocks' growth proportional to the number of nodes"],
    ])},
    "computer-science-engineering-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Formal semantics (DSL)", "A precise mathematical specification of exactly how a domain-specific language's constructs behave"],
        ["Design application", "Ensures a DSL's behavior is unambiguous and can be reasoned about rigorously, unlike an informally specified language"],
    ])},
    "computer-science-engineering-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Type system soundness", "A guarantee that a well-typed program cannot get stuck or exhibit certain classes of runtime errors"],
        ["Progress and preservation theorems", "Together prove soundness: progress shows a well-typed term isn't stuck, preservation shows evaluation preserves well-typedness"],
    ])},
    "computer-science-engineering-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Automata-theoretic model checking", "Translates a temporal logic specification into an automaton and checks it against a system's behavior automaton"],
        ["Temporal logic specification", "Formally expresses properties like \"eventually X happens\" or \"X always holds,\" which model checking can automatically verify"],
    ])},
    "computer-science-engineering-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Petri net", "A mathematical modeling formalism for concurrent systems using places, transitions, and tokens"],
        ["Reachability analysis", "Determines which system states are reachable from an initial state, useful for verifying concurrent system properties"],
    ])},
    "computer-science-engineering-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Process calculus", "A formal algebraic framework for precisely modeling and reasoning about concurrent communicating processes"],
        ["Concurrent communication semantics", "Provides a rigorous mathematical basis for expressing and comparing different notions of process equivalence"],
    ])},
    "computer-science-engineering-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Static taint analysis", "Tracks how untrusted input data propagates through code without executing it, to detect dangerous uses"],
        ["Information flow violation detection", "Flags cases where tainted (attacker-controlled) data reaches a sensitive operation without proper sanitization"],
    ])},
    "computer-science-engineering-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Information-theoretic security", "Security that holds even against an adversary with unlimited computational power, based on entropy arguments"],
        ["Cryptographic protocol analysis", "Provides the strongest possible security guarantee, though achievable only for a limited class of practical protocols"],
    ])},
    "computer-science-engineering-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Adversarial robustness certification", "Provides a mathematical guarantee that no adversarial perturbation within a bound can change a model's output"],
        ["Technique", "Methods like randomized smoothing or interval bound propagation trade certified radius against computational cost"],
    ])},
    "computer-science-engineering-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Federated learning convergence", "Analyzes whether and how quickly a federated learning process converges to a good shared model"],
        ["Non-IID data distribution", "Convergence is harder to guarantee and generally slower when client data distributions differ significantly from each other"],
    ])},
    "computer-science-engineering-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy mechanism", "A mathematical guarantee that a training procedure's output changes negligibly whether or not any single individual's data is included"],
        ["ML training design", "DP-SGD adds calibrated noise to clipped per-example gradients to provide this formal privacy guarantee during training"],
    ])},
    "computer-science-engineering-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Graph neural network expressiveness", "The theoretical limit on which graph structures a GNN architecture can distinguish"],
        ["Weisfeiler-Lehman test", "Standard message-passing GNNs are provably no more powerful than the 1-WL graph isomorphism test at distinguishing graphs"],
    ])},
    "computer-science-engineering-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Neural architecture search", "Automatically searches a space of network designs to find one that performs well on a target task"],
        ["Automated model discovery", "Search strategies range from reinforcement learning to evolutionary and gradient-based relaxation methods"],
    ])},
    "computer-science-engineering-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Deep learning training dynamics", "Studies how a network's parameters evolve during gradient-based training"],
        ["Computational complexity analysis", "Analyzes the computational and theoretical cost of training dynamics, including convergence rate guarantees"],
    ])},
    "computer-science-engineering-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Formal verification of neural networks", "Mathematically proves a network satisfies a safety property for all inputs in a defined region"],
        ["Robustness property", "A common verified property is that no small input perturbation within a bound can flip the network's classification"],
    ])},
    "computer-science-engineering-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Cost-based query optimization", "Chooses among equivalent query execution plans by estimating and comparing their execution cost"],
        ["Plan selection algorithm", "Uses cardinality and cost estimates to search the space of possible execution plans for the cheapest one"],
    ])},
    "computer-science-engineering-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Concurrency control protocol", "Manages simultaneous access to shared data to maintain correctness in a database system"],
        ["Distributed transaction application", "Must coordinate correctness guarantees across multiple nodes, adding complexity beyond single-node concurrency control"],
    ])},
    "computer-science-engineering-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Multi-version concurrency control", "Maintains multiple versions of data so readers can access a consistent snapshot without blocking concurrent writers"],
        ["Snapshot isolation", "A consistency level MVCC commonly provides, giving each transaction a consistent view of the database as of its start time"],
    ])},
    "computer-science-engineering-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Log-structured merge tree", "A write-optimized data structure that buffers writes in memory and periodically merges them into sorted on-disk structures"],
        ["Storage engine design", "Trades off some read amplification for significantly improved write throughput compared with in-place update structures"],
    ])},
    "computer-science-engineering-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["B-tree", "A balanced tree index structure optimized for in-place updates and range queries on disk-based storage"],
        ["LSM-tree trade-off", "LSM-trees favor write throughput at some read cost, while B-trees favor consistent read performance at some write cost"],
    ])},
    "computer-science-engineering-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Approximate nearest neighbor search", "Finds points close to a query point without guaranteeing the exact nearest neighbor, trading accuracy for speed"],
        ["Query processing algorithm design", "Index structures like HNSW enable sub-linear search over massive high-dimensional vector datasets"],
    ])},
    "computer-science-engineering-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Real-time object tracking", "Continuously locates and follows a moving object across successive video frames"],
        ["Computer vision algorithm design", "Must balance tracking accuracy against strict processing speed requirements for real-time applications"],
    ])},
    "computer-science-engineering-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Simultaneous localization and mapping", "A robot builds a map of an unknown environment while simultaneously tracking its own position within it"],
        ["Autonomous robot algorithm", "A foundational capability for robots operating in environments without pre-existing maps or external positioning"],
    ])},
    "computer-science-engineering-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Motion planning", "Computes a valid path for a robot to move from a start to a goal configuration while avoiding obstacles"],
        ["Sampling-based technique", "Algorithms like RRT and PRM randomly sample the configuration space to efficiently find feasible paths in high dimensions"],
    ])},
    "computer-science-engineering-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Formal safety verification (autonomous systems)", "Mathematically proves an autonomous system's control policy satisfies specified safety properties in all reachable scenarios"],
        ["Application", "Critical for high-stakes autonomous systems like self-driving vehicles where safety failures have severe consequences"],
    ])},
    "computer-science-engineering-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Human-robot interaction protocol", "Structures how a robot communicates and coordinates with human collaborators during a shared task"],
        ["Collaborative task execution", "Must account for human unpredictability and communicate robot intent clearly to maintain safe, effective collaboration"],
    ])},
    "computer-science-engineering-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Long-context reasoning architecture", "Neural network designs specifically addressing the challenge of reasoning over very long input sequences"],
        ["NLP application", "Must handle attention's computational cost and information retention challenges as context length grows"],
    ])},
    "computer-science-engineering-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Acoustic model", "The component of a speech recognition system that maps audio features to phonetic or linguistic units"],
        ["Low-resource condition design", "Must achieve reasonable accuracy despite limited transcribed training data for the target language or domain"],
    ])},
    "computer-science-engineering-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Constraint satisfaction problem dichotomy", "A theorem classifying CSPs into exactly two complexity classes: solvable in polynomial time or NP-complete, with no intermediate cases"],
        ["Computational complexity", "A landmark structural result precisely characterizing when a CSP is tractable based on its allowed constraint types"],
    ])},
    "computer-science-engineering-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Algorithmic mechanism design", "Designs the rules of an interaction so that self-interested, strategic participants are incentivized to act as desired"],
        ["Truthful resource allocation", "A mechanism is truthful if each participant's best strategy is to honestly reveal their true preferences"],
    ])},
    "computer-science-engineering-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Price of anarchy", "Measures how much worse a system's outcome is under selfish, uncoordinated behavior compared with a centrally coordinated optimum"],
        ["Distributed routing game application", "Quantifies the efficiency loss when network routing decisions are made independently by self-interested agents"],
    ])},
    "computer-science-engineering-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Happens-before relation", "A partial order capturing which events in a concurrent execution could have causally affected which others"],
        ["Race analysis", "Detects data races by checking whether conflicting memory accesses are unordered by the happens-before relation"],
    ])},
    "computer-science-engineering-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Software model checking", "Automatically verifies that a software program satisfies a formal specification by exploring its reachable states"],
        ["Infinite-state system verification", "Requires abstraction techniques since software often has infinitely many possible states, unlike finite hardware circuits"],
    ])},
    "computer-science-engineering-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Symbolic model checking", "Represents and explores a system's state space implicitly using symbolic formulas rather than enumerating states explicitly"],
        ["Binary decision diagram", "A compact data structure for representing boolean functions, enabling symbolic model checking to scale to very large state spaces"],
    ])},
    "computer-science-engineering-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Hardware trojan", "A malicious modification inserted into a chip's design or manufacturing process"],
        ["Side-channel detection", "Analyzes subtle power or timing signal anomalies that a hardware trojan's presence may introduce"],
    ])},
    "computer-science-engineering-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Secure boot", "Ensures a device only executes software cryptographically verified as authentic during the boot process"],
        ["Trusted Platform Module", "A dedicated hardware chip providing secure key storage and cryptographic operations to support secure boot and attestation"],
    ])},
    "computer-science-engineering-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Energy-proportional computing", "A design goal where a system's power consumption scales proportionally with its actual utilization"],
        ["Data center efficiency application", "Idle and lightly loaded servers should consume dramatically less power than fully utilized ones"],
    ])},
    "computer-science-engineering-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Thesis-level capstone", "A culminating project requiring original formal design and rigorous analysis of a novel distributed algorithm"],
        ["Novel distributed algorithm design", "Requires identifying a genuine gap in existing distributed algorithms and formally proving the new algorithm's correctness and performance"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Computer Science Engineering"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"computer-science-engineering-m2-l{base_n}"
        worked_key = f"computer-science-engineering-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Computer Science Engineering lessons.")


if __name__ == "__main__":
    main()
