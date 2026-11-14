#!/usr/bin/env python3
"""Depth pass, M2 Python: fill in real, hand-checked data_table
content for the M2 Python lessons not covered by the earlier
breadth-first batch. Brings M2 Python to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning CPython
internals (bytecode, frames, GC, memory allocation), type system and
metaprogramming internals, async/concurrency internals (asyncio, free
threading, subinterpreters), native extension development (C API,
Cython, Rust/PyO3), profiling and testing (property-based testing,
fuzzing, formal verification), distributed systems patterns in Python,
packaging and supply chain security, numerical/data computing
internals (NumPy, Pandas, PyTorch), language implementation (parsers,
VMs, interpreters), and advanced security/observability patterns;
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_python_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Bytecode compilation", "CPython compiles source code into an intermediate bytecode representation before execution"],
    ["Compilation pipeline", "Source is parsed into an AST, then compiled to bytecode, which the interpreter's evaluation loop executes"],
])

CHARTS: dict[str, dict] = {
    "python-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Concurrency", "Structures a program to handle multiple tasks that can be in progress at overlapping times"],
        ["Python approach", "Python offers threading, multiprocessing, and asyncio, each suited to different concurrency scenarios"],
    ])},
    "python-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Python capstone project", "An applied culminating project demonstrating end-to-end advanced Python system design and implementation skill"],
        ["Deliverable", "Typically a substantial working system demonstrating mastery of internals, performance, or architecture concepts"],
    ])},
    "python-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Custom bytecode optimization", "Modifying or generating bytecode directly to improve execution performance for specific patterns"],
        ["Application", "Requires deep understanding of the bytecode instruction set and evaluation loop semantics"],
    ])},
    "python-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Frame object", "Represents the execution context (local variables, instruction pointer) of a single function call"],
        ["Evaluation loop", "CPython's core interpreter loop that fetches and executes bytecode instructions one frame at a time"],
    ])},
    "python-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Reference counting", "CPython's primary memory management technique, tracking how many references point to each object"],
        ["Cycle-detecting garbage collection", "A supplementary collector that identifies and reclaims reference cycles that reference counting alone cannot free"],
    ])},
    "python-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["pymalloc", "CPython's specialized small-object memory allocator, optimized for the many small allocations typical of Python programs"],
        ["Custom allocator", "Understanding pymalloc's arena and pool structure is needed to write compatible custom allocation strategies"],
    ])},
    "python-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Metaclass", "A class whose instances are themselves classes, controlling how classes are created and behave"],
        ["Framework design application", "Metaclasses let framework authors automatically customize class creation behavior across many subclasses"],
    ])},
    "python-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Descriptor protocol", "Defines how attribute access is intercepted via __get__, __set__, and __delete__ methods"],
        ["Internals", "Underlies core Python features like properties, methods, and class attribute access"],
    ])},
    "python-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Abstract base class", "Defines a common interface that concrete subclasses must implement"],
        ["Protocol (structural typing)", "Defines an interface based purely on an object's shape/methods, without requiring explicit inheritance"],
    ])},
    "python-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["TypeVar", "Represents a generic type parameter that can be specialized differently across different uses"],
        ["ParamSpec", "Captures and forwards an entire callable's parameter signature, enabling generic decorators to preserve type information"],
    ])},
    "python-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Static type checker", "Analyzes Python code's type annotations without running it to catch type errors before execution"],
        ["mypy architecture", "Parses code into an AST, builds a type environment, and performs type inference and checking against declared annotations"],
    ])},
    "python-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Structural pattern matching", "Python's match statement that destructures and matches data against structural patterns"],
        ["Internals", "Compiled to specialized bytecode instructions that efficiently test pattern structure and bind matched values"],
    ])},
    "python-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Domain-specific language", "A language with notation tailored to a specific problem domain, often embedded within a host language"],
        ["AST manipulation", "Building a DSL in Python can involve directly parsing or transforming Python's own abstract syntax tree"],
    ])},
    "python-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Source-to-source transformation", "Automatically rewrites source code into a modified version of the same language"],
        ["libcst", "A library preserving exact formatting and comments while enabling programmatic code transformation, useful for large-scale refactoring"],
    ])},
    "python-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Import hook", "Custom code that intercepts and customizes Python's module import process"],
        ["Finder", "The component responsible for locating a module's source given its name, which custom hooks can override"],
    ])},
    "python-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Lazy module loading", "Defers actually importing a module's code until it is first genuinely used"],
        ["Import time optimization", "Reduces a program's startup time by avoiding unnecessary upfront imports of rarely used modules"],
    ])},
    "python-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Asyncio event loop", "The core scheduler that manages and executes asynchronous tasks and callbacks"],
        ["Internals", "Understanding the loop's task scheduling and I/O polling mechanics is essential for advanced async debugging"],
    ])},
    "python-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Event loop policy", "Controls how asyncio creates and manages event loop instances across a program"],
        ["Custom policy", "Allows customizing loop behavior for specialized deployment environments or testing scenarios"],
    ])},
    "python-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Structured concurrency", "Ensures concurrent tasks are scoped so a parent task cannot complete until all its child tasks finish or are cancelled"],
        ["anyio and Trio", "Libraries implementing structured concurrency principles, offering more predictable task lifecycle management than raw asyncio"],
    ])},
    "python-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Async generator", "A generator function using async def and yield, producing values asynchronously across await points"],
        ["Async context manager", "Implements __aenter__ and __aexit__ to manage asynchronous setup and teardown within an async with block"],
    ])},
    "python-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Backpressure", "A mechanism for a slow consumer to signal a fast producer to reduce its data rate, preventing overload"],
        ["Flow control (async pipeline)", "Prevents unbounded memory growth when data production outpaces an async pipeline's processing capacity"],
    ])},
    "python-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["PEP 703", "The proposal for a free-threaded CPython build that removes the Global Interpreter Lock"],
        ["GIL removal", "Enables true multi-core parallelism for Python threads, addressing a longstanding limitation of CPython's threading model"],
    ])},
    "python-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Subinterpreter", "A largely isolated Python execution environment running within the same process"],
        ["PEP 554", "Proposes a standard API for creating and communicating between subinterpreters, enabling isolated parallel execution"],
    ])},
    "python-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Shared-memory multiprocessing", "Allows separate processes to access the same block of memory directly, avoiding costly data serialization"],
        ["multiprocessing.shared_memory", "A standard library module providing this shared-memory capability for efficient inter-process data sharing"],
    ])},
    "python-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["CPython C API", "The interface allowing C code to create, manipulate, and embed Python objects and interpreters"],
        ["C extension", "Native code modules built against this API can significantly speed up performance-critical Python code"],
    ])},
    "python-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Cython", "A superset of Python that compiles to C, allowing gradual addition of static types for performance"],
        ["Typed memoryview", "A Cython feature providing efficient, type-safe direct access to array-like memory buffers"],
    ])},
    "python-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Numba", "A just-in-time compiler that translates a subset of Python and NumPy code into fast machine code"],
        ["JIT compilation (numerical kernels)", "Particularly effective for numerical loops that would otherwise run slowly in pure interpreted Python"],
    ])},
    "python-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["PyO3", "A Rust library for building native Python extension modules with Rust's safety and performance"],
        ["Rust extension", "Lets developers write performance-critical Python extensions in Rust instead of C, gaining memory safety guarantees"],
    ])},
    "python-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["ctypes", "A standard library module for calling functions in shared libraries without writing a compiled extension"],
        ["cffi", "A more flexible foreign function interface library offering better performance and a cleaner API than ctypes for many use cases"],
    ])},
    "python-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Sampling profiler", "Periodically samples a program's call stack to estimate where time is spent, with low overhead"],
        ["Tracing profiler", "Records every function call and return precisely, giving exact timing at the cost of higher overhead"],
    ])},
    "python-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Memory profiling", "Measures how a program's memory usage changes over time to identify inefficiencies"],
        ["Leak detection", "Identifies objects that remain unexpectedly referenced and are never freed, causing memory usage to grow unbounded"],
    ])},
    "python-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Decorator composition", "Applying multiple decorators to a single function, each wrapping the result of the previous one"],
        ["Stacking order", "Decorators apply bottom-to-top in the source but execute outer-to-inner at call time, a common source of confusion"],
    ])},
    "python-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Context variable", "A variable whose value is scoped to the current execution context, correctly isolated across concurrent async tasks"],
        ["contextvars application", "Solves the problem that thread-local storage doesn't correctly isolate state across asyncio tasks running on the same thread"],
    ])},
    "python-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Context manager", "An object implementing __enter__ and __exit__ to manage setup and cleanup within a with block"],
        ["contextlib.contextmanager", "A decorator that lets you write a context manager as a generator function instead of a full class"],
    ])},
    "python-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Plugin architecture", "A software design allowing new functionality to be added via discoverable, independently packaged extensions"],
        ["Entry points", "A packaging mechanism letting installed packages register themselves as discoverable plugins for a host application"],
    ])},
    "python-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Dependency injection", "Supplies a component's dependencies from outside rather than having it construct them internally"],
        ["Python pattern", "Improves testability by allowing dependencies to be swapped for test doubles without modifying the dependent code"],
    ])},
    "python-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Event sourcing", "Persists application state as an append-only sequence of events rather than just the current state"],
        ["Python implementation", "Requires careful design of event schemas and replay logic to reconstruct current state from the event log"],
    ])},
    "python-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["ORM query compiler", "Translates high-level object-relational mapper query expressions into executable SQL"],
        ["Custom implementation", "Requires understanding query optimization and SQL generation to build an efficient custom compiler"],
    ])},
    "python-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["SQLAlchemy Core", "A lower-level, expression-based SQL toolkit distinct from SQLAlchemy's higher-level ORM layer"],
        ["Expression language", "Provides fine-grained, composable control over generated SQL for cases where the full ORM abstraction isn't needed"],
    ])},
    "python-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Connection pooling", "Reuses a limited set of database connections across many requests rather than opening a new one each time"],
        ["Internals", "Must handle connection health checking, timeout, and safe concurrent access to the shared pool"],
    ])},
    "python-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["WSGI", "A standard synchronous interface between Python web applications and web servers"],
        ["ASGI", "An asynchronous successor to WSGI, supporting async applications and protocols like WebSockets"],
    ])},
    "python-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Protocol Buffers", "A language-neutral binary serialization format commonly used with gRPC for efficient structured data exchange"],
        ["gRPC service design", "Defines strongly typed remote procedure call interfaces, generating client and server code from a shared schema"],
    ])},
    "python-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Apache Arrow", "A columnar in-memory data format designed for efficient analytics and cross-language data sharing"],
        ["Zero-copy serialization", "Allows data to be shared between processes or languages without the overhead of copying and re-parsing"],
    ])},
    "python-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Custom pickle reducer", "Customizes how an object is serialized and reconstructed by Python's pickle module"],
        ["Security implication", "Unpickling untrusted data can execute arbitrary code, making pickle a significant security risk for untrusted input"],
    ])},
    "python-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Property-based testing", "Generates many random test inputs to verify general properties hold, rather than testing fixed example cases"],
        ["Hypothesis", "A popular Python library implementing property-based testing, automatically finding and shrinking failing examples"],
    ])},
    "python-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Mutation testing", "Deliberately introduces small bugs (mutants) into code to check whether the test suite actually catches them"],
        ["Test suite quality", "A surviving mutant that no test catches reveals a gap in the test suite's actual coverage of behavior"],
    ])},
    "python-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Fuzz testing", "Automatically generates diverse, often malformed inputs to discover crashes and vulnerabilities"],
        ["Atheris", "A coverage-guided fuzzing engine for Python, adapted from Google's libFuzzer"],
    ])},
    "python-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Formal verification (contracts)", "Mathematically or systematically checks that a function's behavior satisfies specified pre/post-conditions"],
        ["icontract", "A Python library implementing design-by-contract, checking preconditions and postconditions at runtime"],
    ])},
    "python-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Static analysis tool", "Examines source code without executing it to detect bugs, style issues, or security problems"],
        ["ast module", "Python's standard library module for parsing and analyzing Python source code as an abstract syntax tree"],
    ])},
    "python-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Type narrowing", "A static type checker refines a variable's inferred type based on control-flow checks like isinstance"],
        ["TypeGuard function", "A user-defined function that a type checker recognizes as performing a custom type-narrowing check"],
    ])},
    "python-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Runtime type checking", "Validates data types and structure at actual program execution time, not just via static analysis"],
        ["Pydantic core validator", "Pydantic's efficient Rust-based validation engine that enforces type and data constraints at runtime"],
    ])},
    "python-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Dataclass field metadata", "Additional descriptive information attached to a dataclass field beyond its type and default value"],
        ["Post-init processing", "The __post_init__ method allows custom logic to run immediately after a dataclass's generated __init__ completes"],
    ])},
    "python-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Custom serialization framework", "A system for converting Python objects to and from a storage or transmission format"],
        ["Design consideration", "Must handle versioning, custom types, and security concerns like avoiding arbitrary code execution during deserialization"],
    ])},
    "python-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Celery", "A distributed task queue system for Python, executing background jobs across worker processes"],
        ["Reliability pattern", "Includes retry policies, acknowledgment semantics, and dead-letter handling to ensure tasks aren't silently lost"],
    ])},
    "python-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Idempotent job processing", "Ensures that processing the same job multiple times (e.g. due to a retry) produces the same result as processing it once"],
        ["Distributed application", "Critical in distributed systems where at-least-once delivery semantics make duplicate job execution likely"],
    ])},
    "python-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Distributed lock manager", "Coordinates mutually exclusive access to a shared resource across multiple processes or machines"],
        ["Custom implementation", "Must handle failure scenarios like a lock holder crashing without releasing the lock"],
    ])},
    "python-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Structured logging", "Emits log entries as machine-parseable structured data rather than unstructured free text"],
        ["OpenTelemetry integration", "A standardized framework for collecting distributed traces, metrics, and logs across a Python service"],
    ])},
    "python-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Chaos engineering", "Deliberately injects failures into a running system to verify it degrades gracefully"],
        ["Python service application", "Tools can simulate network failures, latency, or process crashes to test a Python service's resilience"],
    ])},
    "python-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Reproducible wheel", "A Python package build that deterministically produces bit-for-bit identical output from the same source"],
        ["Packaging application", "Enables independently verifying that a distributed wheel genuinely corresponds to its published source code"],
    ])},
    "python-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Vendoring", "Bundling a copy of a dependency's source code directly within a project rather than relying on an installed package"],
        ["Dependency isolation strategy", "Avoids version conflicts with other packages that might require a different version of the same dependency"],
    ])},
    "python-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain security", "Protects against malicious or compromised dependencies being introduced into a software project"],
        ["Python package application", "Includes verifying package signatures, pinning exact dependency versions, and auditing transitive dependencies"],
    ])},
    "python-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Sandboxing", "Runs untrusted code in a restricted environment that limits its access to system resources"],
        ["Untrusted code execution", "Necessary when executing user-submitted Python code, since the language has no built-in security sandbox"],
    ])},
    "python-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Numerical stability", "Ensures computations produce accurate results despite floating-point rounding error accumulation"],
        ["NumPy application", "Careful algorithm choice (e.g. avoiding catastrophic cancellation) is needed for numerically stable large-scale computation"],
    ])},
    "python-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["ufunc", "A NumPy universal function that operates element-wise on arrays with optimized, vectorized C implementations"],
        ["Custom ufunc in C", "Writing a custom ufunc in C lets developers add new, highly optimized element-wise operations to NumPy"],
    ])},
    "python-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Out-of-core computation", "Processes datasets too large to fit entirely in memory by operating on them in chunks"],
        ["Dask task graph", "Represents a large computation as a graph of smaller tasks that can be scheduled and executed in chunks, potentially in parallel"],
    ])},
    "python-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Pandas BlockManager", "The internal data structure organizing a DataFrame's columns into type-homogeneous memory blocks"],
        ["Extension array", "Allows custom data types to integrate with Pandas' internals beyond the built-in NumPy-backed types"],
    ])},
    "python-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Vectorization", "Expresses operations as array-wide operations rather than explicit element-by-element Python loops"],
        ["Loop elimination strategy", "Vectorized NumPy/Pandas operations run in optimized compiled code, dramatically faster than equivalent Python loops"],
    ])},
    "python-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Scikit-learn estimator", "A standardized interface (fit, predict) that scikit-learn's tools and pipelines expect models to implement"],
        ["Custom compatible estimator", "Building a custom estimator following this interface lets it interoperate seamlessly with scikit-learn's ecosystem"],
    ])},
    "python-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian hyperparameter search", "Builds a probabilistic surrogate model of the objective to intelligently choose which hyperparameters to try next"],
        ["Framework", "Libraries implementing this approach minimize the number of costly model training runs needed to find good hyperparameters"],
    ])},
    "python-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["PyTorch autograd", "PyTorch's automatic differentiation engine that computes gradients for backpropagation"],
        ["Custom autograd function", "Lets developers define custom forward and backward computation logic not expressible with standard PyTorch operations alone"],
    ])},
    "python-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Distributed training", "Splits model training work across multiple machines or devices to handle larger models and datasets"],
        ["Orchestration in Python", "Requires coordinating data distribution, gradient synchronization, and fault tolerance across the training cluster"],
    ])},
    "python-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Model serving architecture", "Infrastructure for deploying trained ML models to respond to real-time prediction requests"],
        ["Batching and latency optimization", "Groups multiple prediction requests together to improve throughput, balanced against added per-request latency"],
    ])},
    "python-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Regular expression engine", "The underlying algorithm that matches text patterns against a regex specification"],
        ["Internals", "Understanding backtracking behavior helps explain why certain regex patterns can suffer catastrophic performance on certain inputs"],
    ])},
    "python-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Recursive descent parser", "A top-down parsing technique using a set of mutually recursive functions, one per grammar rule"],
        ["Python implementation", "A common, relatively straightforward approach to hand-writing a parser for a language's grammar"],
    ])},
    "python-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Bytecode virtual machine", "An abstract machine that executes a program by interpreting a stream of simple bytecode instructions"],
        ["Building in Python", "Implementing a small VM in Python is a classic exercise for understanding how interpreters like CPython itself work"],
    ])},
    "python-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Tree-walking interpreter", "Executes a program by directly traversing and evaluating its abstract syntax tree, without compiling to bytecode"],
        ["Implementation", "Simpler to implement than a bytecode-based interpreter, though generally slower at runtime"],
    ])},
    "python-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Monadic pattern", "A functional programming pattern for sequencing computations that carry an effect, such as optionality or error handling"],
        ["Python application", "Can be implemented in Python to express error handling or optional-value chains more compositionally"],
    ])},
    "python-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Lazy evaluation", "Defers computing a value until it is actually needed, rather than computing it immediately"],
        ["Generator-based pipeline", "Python generators naturally implement lazy evaluation, processing data one item at a time without materializing the full sequence"],
    ])},
    "python-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Custom iterator", "A class implementing __iter__ and __next__ to define custom iteration behavior"],
        ["Advanced protocol compliance", "Correctly handling edge cases like StopIteration and re-entrancy requires careful adherence to the full iterator protocol"],
    ])},
    "python-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Exception group", "PEP 654's ExceptionGroup allows multiple unrelated exceptions to be raised and handled together as a single unit"],
        ["Application", "Especially useful for concurrent code where multiple independent tasks might fail with different exceptions simultaneously"],
    ])},
    "python-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Retry pattern", "Automatically re-attempts a failed operation, often with backoff, to handle transient failures"],
        ["Circuit breaker pattern", "Stops calling a failing operation temporarily, allowing it time to recover instead of overwhelming it further"],
    ])},
    "python-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Deserialization vulnerability", "Occurs when deserializing untrusted data allows an attacker to execute arbitrary code or manipulate program state"],
        ["Prevention", "Avoiding formats like pickle for untrusted data, and using safe, schema-validated formats, mitigates this risk"],
    ])},
    "python-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Static taint analysis", "Tracks how untrusted input data propagates through code without executing it, to detect dangerous uses"],
        ["Tool for Python", "Building such a tool requires analyzing the AST to trace data flow from sources (input) to sinks (dangerous operations)"],
    ])},
    "python-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Cryptographic primitive", "A well-studied, low-level cryptographic algorithm like a cipher or hash function"],
        ["Common misuse pattern", "Errors like reusing a nonce or using a non-cryptographic hash for passwords are common, security-critical mistakes"],
    ])},
    "python-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Contract testing", "Verifies that a service's API meets the expectations defined by its consumers"],
        ["Microservices application", "Catches breaking API changes before deployment without requiring full end-to-end integration test environments"],
    ])},
    "python-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Reproducible scientific computing environment", "A computational environment that can be precisely recreated to reproduce a scientific result"],
        ["Application", "Requires pinning exact package versions and often containerization to eliminate environment-dependent result variation"],
    ])},
    "python-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Jupyter kernel", "The computational engine that executes code submitted from a Jupyter notebook interface"],
        ["Custom kernel architecture", "Building a custom kernel lets other languages or specialized execution environments integrate with the Jupyter interface"],
    ])},
    "python-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["IPython magic command", "Special commands (prefixed with %) providing enhanced interactive functionality beyond plain Python code"],
        ["Custom magic command", "Developers can define new magic commands to add specialized interactive shortcuts for their own workflows"],
    ])},
    "python-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Data validation pipeline", "Systematically checks data quality and conformance to expectations as it flows through a processing system"],
        ["Great Expectations", "A Python library for defining, running, and documenting automated data quality validation checks"],
    ])},
    "python-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Static site generator", "Converts source content (like Markdown) into a set of static HTML pages at build time"],
        ["Custom implementation", "Building one in Python requires template rendering, content parsing, and a build pipeline design"],
    ])},
    "python-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Internationalization", "Designs software to be adaptable to different languages and regions"],
        ["Locale-aware processing", "Handles locale-specific formatting for dates, numbers, and currency correctly across different regional settings"],
    ])},
    "python-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Bytecode disassembler", "Converts compiled bytecode back into a human-readable representation of the underlying instructions"],
        ["Application", "Python's built-in dis module provides this functionality, useful for understanding and debugging compiled code behavior"],
    ])},
    "python-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Async application profiling", "Measures performance of asynchronous code, which is more complex than profiling synchronous code due to interleaved execution"],
        ["Advanced technique", "Must account for time spent waiting on I/O versus actual CPU computation within concurrently running coroutines"],
    ])},
    "python-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Custom logging handler", "Extends Python's logging module to route log records to a specific destination or format"],
        ["Distributed system application", "Custom handlers can forward logs to centralized aggregation systems with proper structured context"],
    ])},
    "python-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Feature flag framework", "A system for toggling functionality on or off in production without a separate code deployment"],
        ["Experimentation framework", "Often integrated with feature flags to run controlled A/B tests on new functionality before full rollout"],
    ])},
    "python-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Dependency resolver", "An algorithm that finds a compatible set of package versions satisfying all of a project's dependency constraints"],
        ["Algorithm", "Modern resolvers typically use backtracking or SAT-solving-based approaches to handle complex, potentially conflicting constraints"],
    ])},
    "python-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Deadlock", "A situation where two or more concurrent processes are each waiting for a resource held by the other, blocking indefinitely"],
        ["Concurrency debugging", "Specialized tools can detect deadlock conditions in running concurrent Python programs, which are notoriously hard to reproduce"],
    ])},
    "python-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Configuration management system", "Manages an application's settings across different environments (development, staging, production)"],
        ["Custom implementation", "Must handle precedence between configuration sources like environment variables, files, and defaults"],
    ])},
    "python-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Thesis-level capstone", "A culminating project requiring original design and implementation of a novel Python runtime feature"],
        ["Novel runtime feature design", "Requires deep understanding of CPython internals to propose and prototype a genuinely new interpreter-level capability"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Python"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"python-m2-l{base_n}"
        worked_key = f"python-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Python lessons.")


if __name__ == "__main__":
    main()
