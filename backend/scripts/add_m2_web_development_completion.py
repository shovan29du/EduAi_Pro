#!/usr/bin/env python3
"""Depth pass, M2 Web Development: fill in real, hand-checked
data_table content for the M2 Web Development lessons not covered by
the earlier breadth-first batch. Brings M2 Web Development to full
120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning frontend
framework internals (reconciliation, reactivity, compilers), formal
security models, distributed/multi-region web systems, API and
backend architecture, rendering performance, browser engine internals,
authentication/authorization protocols, and observability/deployment
infrastructure; l101-l120 are "Worked Analysis" companions reusing the
data_table of l1-l20 (direct 1:1 mapping). l3 was already completed by
an earlier breadth-first batch, so its data_table is hard-coded here
for reuse (it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_web_development_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Type coercion", "JavaScript's implicit conversion of a value from one type to another during an operation"],
    ["Formal semantics", "A precise mathematical specification of exactly how coercion rules behave for every operator and type pair"],
])

CHARTS: dict[str, dict] = {
    "web-development-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["DevOps", "Practices unifying software development and IT operations to enable faster, more reliable releases"],
        ["Deployment", "The process of releasing new application code to a production environment safely and repeatably"],
    ])},
    "web-development-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Full-stack capstone", "An applied culminating project demonstrating end-to-end web development skill across frontend and backend"],
        ["Deliverable", "Typically includes a working deployed application, architecture rationale, and evaluation of design trade-offs"],
    ])},
    "web-development-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["JavaScript bundler", "A build tool that combines and transforms modules into optimized output files for the browser"],
        ["Compiler design", "Modern bundlers apply compiler techniques like tree-shaking, minification, and dependency graph analysis"],
    ])},
    "web-development-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Virtual DOM", "An in-memory representation of the UI that a framework diffs against the previous version to compute minimal updates"],
        ["Reconciliation algorithm", "Determines the minimal set of real DOM changes needed to match the new virtual DOM tree"],
    ])},
    "web-development-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Fiber architecture", "React's internal reconciliation engine that breaks rendering work into interruptible units"],
        ["Incremental rendering", "Allows the browser to pause and resume rendering work, keeping the UI responsive during large updates"],
    ])},
    "web-development-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Reactive programming", "A declarative paradigm for working with asynchronous data streams that emit values over time"],
        ["Observable", "A composable stream abstraction that other code can subscribe to for a sequence of values or events"],
    ])},
    "web-development-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Signal", "A reactive primitive that tracks its own dependents so updates propagate automatically without a virtual DOM diff"],
        ["Fine-grained reactivity", "Updates only the specific DOM nodes that depend on a changed value, rather than re-rendering a larger component tree"],
    ])},
    "web-development-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Compiler-based UI framework", "Shifts reactivity analysis to build time rather than runtime, generating optimized update code ahead of time"],
        ["Ahead-of-time optimization", "Produces smaller and faster runtime code since less reactivity bookkeeping needs to run in the browser"],
    ])},
    "web-development-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Gradual typing", "Allows a codebase to mix statically typed and dynamically typed code, with type checking applied incrementally"],
        ["TypeScript type system", "Formal models of gradual typing analyze soundness trade-offs made to interoperate smoothly with plain JavaScript"],
    ])},
    "web-development-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Generic type inference", "Automatically determines type parameters for generic functions or classes from how they are used"],
        ["Statically typed web language", "Advanced inference reduces the annotation burden on developers while preserving type safety"],
    ])},
    "web-development-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Formal verification (smart contracts)", "Mathematically proves a contract's code satisfies its intended specification before deployment"],
        ["Web interface", "Verifying the web frontend's interaction logic with a smart contract helps prevent costly integration bugs"],
    ])},
    "web-development-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Content Security Policy", "A browser security mechanism restricting which sources of content a page is allowed to load or execute"],
        ["Defense-in-depth", "CSP acts as one layer among several, mitigating the impact of vulnerabilities like cross-site scripting even if they occur"],
    ])},
    "web-development-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Threat modeling", "Systematically identifies potential attackers, attack vectors, and assets at risk for a system"],
        ["Web application architecture", "Applied early in design to surface security requirements before implementation, not just after an incident"],
    ])},
    "web-development-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["End-to-end encryption", "Ensures only communicating endpoints, not intermediate servers, can read message content"],
        ["Cryptographic protocol design", "Requires careful key exchange and forward secrecy guarantees to remain secure over time"],
    ])},
    "web-development-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Zero-knowledge proof", "Lets a prover convince a verifier a statement is true without revealing any information beyond its truth"],
        ["Web authentication integration", "Can let a user prove identity or eligibility without exposing the underlying private credential to the server"],
    ])},
    "web-development-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["WebAssembly", "A portable, near-native-speed binary instruction format that runs in the browser alongside JavaScript"],
        ["Runtime sandboxing", "Executes WebAssembly code within a memory-safe, isolated sandbox to prevent it from accessing arbitrary browser or system resources"],
    ])},
    "web-development-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Linear memory", "WebAssembly's flat, contiguous memory model that modules read and write within a sandboxed bounds-checked region"],
        ["Memory safety guarantee", "The sandbox ensures a module cannot read or write memory outside its allocated linear memory space"],
    ])},
    "web-development-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Service worker", "A background script that can intercept network requests and manage caching independently of the page"],
        ["Caching strategy", "Patterns like stale-while-revalidate and cache-first trade off freshness against offline availability and speed"],
    ])},
    "web-development-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Eventual consistency", "A guarantee that, absent new updates, all replicas will eventually converge to the same state"],
        ["Offline-first web app", "Must reconcile local changes made while offline with the server state once connectivity is restored"],
    ])},
    "web-development-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["CRDT", "A conflict-free replicated data type designed so concurrent updates always converge without coordination"],
        ["Collaborative web editing", "Enables multiple users to edit the same document simultaneously with automatic, conflict-free merging"],
    ])},
    "web-development-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Operational transformation", "Transforms concurrent operations so they can be applied in different orders while still converging to the same result"],
        ["Real-time collaboration", "An alternative to CRDTs for building collaborative editors, historically used in tools like Google Docs"],
    ])},
    "web-development-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Distributed systems theory", "Studies how independent computers coordinate and remain correct despite failures and network delays"],
        ["Multi-region web backend", "Applies distributed systems principles to serve users from geographically distributed data centers"],
    ])},
    "web-development-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Consistency model", "Defines what guarantees a distributed system makes about the order and visibility of updates"],
        ["Distributed session state", "Choosing an appropriate consistency model for session data balances correctness against latency and availability"],
    ])},
    "web-development-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Query optimization", "Chooses among equivalent query execution plans by estimating and comparing their execution cost"],
        ["Web-scale OLTP", "High-throughput transactional workloads require carefully tuned indexes and query plans to maintain low latency"],
    ])},
    "web-development-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Sharding", "Partitions a dataset across multiple database nodes so each holds only a subset, enabling horizontal scale"],
        ["Partitioning strategy", "Range-based, hash-based, and directory-based approaches trade off load balance against range-query efficiency"],
    ])},
    "web-development-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Cache invalidation", "Determines when cached data has become stale and must be refreshed or removed"],
        ["Distributed web system", "Coordinating invalidation across multiple cache nodes is a notoriously difficult distributed systems problem"],
    ])},
    "web-development-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Edge computing", "Moves computation closer to end users to reduce latency and bandwidth use"],
        ["Latency-sensitive web application", "Serving requests from edge locations near the user significantly reduces round-trip latency"],
    ])},
    "web-development-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["GraphQL query complexity", "The computational cost of resolving a client-specified GraphQL query, which can vary widely by query shape"],
        ["Cost estimation", "Servers estimate query cost before execution to prevent overly expensive or abusive queries from overwhelming the backend"],
    ])},
    "web-development-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Schema federation", "Combines multiple independently developed GraphQL schemas into a single unified graph"],
        ["Distributed GraphQL system", "Lets different teams own separate services while presenting a coherent API to clients"],
    ])},
    "web-development-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["API contract", "A formal specification of an API's expected inputs, outputs, and behavior"],
        ["Compatibility verification", "Formally checks that a new API version remains compatible with existing consumers before deployment"],
    ])},
    "web-development-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Event-driven microservice", "A service architecture where components communicate primarily through asynchronous events rather than direct calls"],
        ["Web backend architecture", "Improves decoupling and scalability at the cost of increased complexity in tracing and consistency"],
    ])},
    "web-development-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Saga pattern", "Coordinates a sequence of local transactions across services, using compensating actions to undo partial failures"],
        ["Distributed transaction consistency", "Provides an alternative to distributed two-phase commit for maintaining consistency across microservices"],
    ])},
    "web-development-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Idempotency", "The property that performing an operation multiple times produces the same result as performing it once"],
        ["Distributed API design", "Critical for safely retrying requests over unreliable networks without causing duplicate side effects"],
    ])},
    "web-development-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Rate limiting", "Restricts how many requests a client can make within a given time window"],
        ["High-throughput API", "Algorithms like token bucket and sliding window balance fairness, burst tolerance, and implementation efficiency"],
    ])},
    "web-development-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Load balancing algorithm", "Distributes incoming traffic across multiple servers to optimize resource use and response time"],
        ["Formal model", "Algorithms like weighted round-robin and least-connections have different theoretical fairness and latency properties"],
    ])},
    "web-development-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["HTTP/3", "The latest major HTTP version, built on the QUIC transport protocol instead of TCP"],
        ["QUIC", "A UDP-based transport protocol offering faster connection setup and improved handling of packet loss than TCP"],
    ])},
    "web-development-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Critical rendering path", "The sequence of steps a browser must complete to render the first pixels of a page"],
        ["Performance modeling", "Formally modeling each stage's cost helps identify the highest-impact optimizations for perceived load speed"],
    ])},
    "web-development-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Core Web Vitals", "A standardized set of metrics measuring loading, interactivity, and visual stability from a user's perspective"],
        ["Statistical validity", "Field measurement requires accounting for variability across devices and network conditions when interpreting results"],
    ])},
    "web-development-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Bundle splitting", "Divides application code into smaller chunks loaded on demand rather than one large upfront bundle"],
        ["Large-scale application strategy", "Careful chunk boundaries reduce initial load time while avoiding excessive small-file request overhead"],
    ])},
    "web-development-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Hydration", "The process of attaching interactive JavaScript behavior to server-rendered static HTML in the browser"],
        ["Performance model", "Hydration cost scales with the amount of interactive UI, motivating techniques to reduce or avoid unnecessary hydration"],
    ])},
    "web-development-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Streaming server-side rendering", "Sends HTML to the browser progressively as it's generated, rather than waiting for the entire page to render"],
        ["Architecture benefit", "Reduces time-to-first-byte and lets the browser start displaying content before the full response is ready"],
    ])},
    "web-development-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Islands architecture", "Renders most of a page as static HTML, hydrating only small interactive \"islands\" of JavaScript"],
        ["Partial hydration", "Reduces the amount of JavaScript shipped and hydrated compared with hydrating an entire page"],
    ])},
    "web-development-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Resumability", "Serializes framework execution state on the server so the browser can resume without replaying setup logic"],
        ["Hydration comparison", "Contrasts with hydration, which re-executes component logic in the browser to attach interactivity"],
    ])},
    "web-development-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Accessibility tree", "A parallel tree derived from the DOM that assistive technologies use to understand and navigate a page"],
        ["Tree construction analysis", "Formal analysis of how browsers compute the accessibility tree helps developers predict and debug assistive-technology behavior"],
    ])},
    "web-development-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["ARIA live region", "A page region marked so assistive technologies announce dynamic content updates to users automatically"],
        ["Dynamic content accessibility", "Ensures screen reader users are notified of changes that occur without a full page reload"],
    ])},
    "web-development-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Progressive enhancement", "Builds a baseline experience that works everywhere, then layers on enhanced functionality for capable browsers"],
        ["Architecture model", "Ensures core functionality remains usable even if JavaScript or advanced features fail or are unavailable"],
    ])},
    "web-development-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Internationalization architecture", "Structures an application to support multiple languages, locales, and cultural formatting conventions"],
        ["Global web platform", "Must handle text direction, pluralization rules, and locale-specific formatting consistently across the app"],
    ])},
    "web-development-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["State machine", "A formal model representing an application as a finite set of states and the transitions between them"],
        ["Web application state", "Modeling UI logic as an explicit state machine makes valid and invalid transitions clearer than ad hoc boolean flags"],
    ])},
    "web-development-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Statechart", "Extends finite state machines with hierarchy, parallel states, and history to model complex UI behavior"],
        ["Interaction flow architecture", "Well suited to modeling complex multi-step interaction flows like checkout wizards or onboarding"],
    ])},
    "web-development-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["State management reducer", "A pure function that computes a new application state from the current state and an action"],
        ["Formal verification", "Reducers' purity makes them amenable to rigorous testing and even formal proof of correctness properties"],
    ])},
    "web-development-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Dependency injection", "Supplies a component's dependencies from outside rather than having it construct them internally"],
        ["Frontend architecture", "Improves testability and modularity by decoupling components from concrete implementations of their dependencies"],
    ])},
    "web-development-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Micro-frontend", "Splits a large web application into independently developed and deployed frontend modules"],
        ["Independent deployability", "Allows different teams to ship their portion of the UI without coordinating a single monolithic release"],
    ])},
    "web-development-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Module federation", "A runtime mechanism letting separately built JavaScript bundles share code and dependencies dynamically"],
        ["Shared dependency architecture", "Avoids duplicating common libraries across micro-frontends, reducing total bundle size"],
    ])},
    "web-development-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["CSS cascade", "The algorithm determining which conflicting style rule ultimately applies to an element"],
        ["Specificity resolution", "A formal weighting scheme (based on selector type) that decides precedence among competing style rules"],
    ])},
    "web-development-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Container query", "Applies styles to a component based on the size of its containing element, not the overall viewport"],
        ["Component-level responsive design", "Enables truly reusable components that adapt correctly regardless of where they're placed in a layout"],
    ])},
    "web-development-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Flexbox and Grid", "CSS layout systems that arrange elements along one axis (Flexbox) or in a two-dimensional grid"],
        ["Constraint solving", "Both systems can be formally understood as solving a system of layout constraints to determine element positions and sizes"],
    ])},
    "web-development-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Compositor thread", "A separate browser thread that combines rendered layers into the final displayed frame"],
        ["Animation performance", "Animating properties handled entirely on the compositor thread avoids expensive main-thread layout and paint work"],
    ])},
    "web-development-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Just-in-time compilation", "Compiles JavaScript to native machine code during execution based on observed runtime behavior"],
        ["JavaScript engine model", "Formal models describe how engines progressively optimize hot code paths through multiple compilation tiers"],
    ])},
    "web-development-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Garbage collection", "Automatically reclaims memory no longer reachable by the running program"],
        ["Long-running application", "Poor garbage collection behavior can cause noticeable pauses in applications that stay open for extended periods"],
    ])},
    "web-development-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Event loop", "The mechanism by which JavaScript processes queued tasks and callbacks one at a time on a single thread"],
        ["Task prioritization", "Distinguishes macrotasks and microtasks, which are scheduled and interleaved according to specific ordering rules"],
    ])},
    "web-development-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Web Worker", "Runs JavaScript on a separate background thread, off the main UI thread"],
        ["Parallel computation", "Enables CPU-intensive work to proceed without blocking the responsiveness of the main page"],
    ])},
    "web-development-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["SharedArrayBuffer", "Allows multiple JavaScript contexts (e.g. main thread and workers) to share the same underlying memory"],
        ["Atomics", "Provides low-level synchronization primitives for safely coordinating access to shared memory across threads"],
    ])},
    "web-development-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Cross-Origin Resource Sharing", "A browser mechanism that controls which origins are allowed to make requests to a given server"],
        ["Formal security analysis", "Misconfigured CORS policies can inadvertently expose sensitive data to untrusted origins"],
    ])},
    "web-development-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Subresource integrity", "Lets a browser verify that a fetched resource (like a CDN script) hasn't been tampered with, via a cryptographic hash"],
        ["Supply chain attack mitigation", "Protects against a compromised third-party dependency silently injecting malicious code"],
    ])},
    "web-development-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["OAuth 2.0", "An authorization framework letting a user grant a third-party application limited access to their resources"],
        ["OpenID Connect", "An identity layer built on top of OAuth 2.0 that adds standardized user authentication"],
    ])},
    "web-development-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["JSON Web Token", "A compact, signed token format commonly used to represent authentication claims"],
        ["Revocation strategy", "Since JWTs are typically stateless, revoking a token before its expiry requires additional mechanisms like a denylist"],
    ])},
    "web-development-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Session fixation", "An attack where an adversary tricks a victim into using a known session identifier, then hijacks the authenticated session"],
        ["Countermeasure", "Regenerating the session identifier upon login is a standard defense against session fixation"],
    ])},
    "web-development-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Passkey", "A phishing-resistant credential based on public-key cryptography that replaces traditional passwords"],
        ["WebAuthn", "The web standard enabling passkey-based authentication using platform or hardware authenticators"],
    ])},
    "web-development-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Same-origin policy", "Restricts how a document or script from one origin can interact with resources from another origin"],
        ["Enforcement model", "The foundational browser security boundary that many other web security mechanisms build upon"],
    ])},
    "web-development-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Web application firewall", "Filters and monitors HTTP traffic to detect and block malicious requests before they reach the application"],
        ["Rule design", "Effective rules must balance catching real attacks against generating excessive false positives on legitimate traffic"],
    ])},
    "web-development-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["SQL injection", "An attack that manipulates a malicious input into being executed as part of a database query"],
        ["Prevention", "Parameterized queries and input validation are the standard defenses against SQL and NoSQL injection"],
    ])},
    "web-development-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Server-side request forgery", "An attack tricking a server into making unintended requests to internal or restricted resources"],
        ["Attack surface analysis", "Identifies which server-side functionality that fetches URLs could be abused to reach unintended internal targets"],
    ])},
    "web-development-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Denial-of-service mitigation", "Techniques to keep a service available despite traffic intended to overwhelm it"],
        ["Rate-limited mitigation", "Combines rate limiting with anomaly detection to distinguish and throttle abusive traffic patterns"],
    ])},
    "web-development-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Continuous deployment pipeline", "Automatically builds, tests, and deploys code changes to production with minimal manual intervention"],
        ["Pipeline architecture", "Balances deployment speed against safety through automated gates like tests and canary releases"],
    ])},
    "web-development-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Feature flag", "A mechanism to toggle functionality on or off in production without a separate code deployment"],
        ["Rollout risk analysis", "Gradual, monitored rollouts using feature flags reduce the blast radius of a problematic change"],
    ])},
    "web-development-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Chaos engineering", "Deliberately injects failures into a production system to verify it degrades gracefully"],
        ["Infrastructure resilience", "Validates assumptions about fault tolerance empirically rather than relying solely on design-time analysis"],
    ])},
    "web-development-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Distributed tracing", "Tracks a single request as it flows through multiple services, correlating spans into one coherent trace"],
        ["Observability architecture", "Enables diagnosing latency and error sources across complex, multi-service web systems"],
    ])},
    "web-development-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Structured logging", "Emits log entries as machine-parseable structured data rather than unstructured free text"],
        ["Log aggregation architecture", "Centralizes structured logs from many services to enable efficient search, filtering, and alerting"],
    ])},
    "web-development-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Service level objective", "A target reliability threshold (e.g. 99.9% availability) that a service commits to meeting"],
        ["Error budget", "The allowed amount of unreliability under the SLO, which teams can spend on releasing risky changes"],
    ])},
    "web-development-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Container orchestration", "Automates the deployment, scaling, and management of containerized applications"],
        ["Web deployment architecture", "Coordinates scheduling, networking, and health checks across a fleet of containers running a web service"],
    ])},
    "web-development-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Infrastructure-as-code", "Manages infrastructure configuration through versioned code rather than manual changes"],
        ["Idempotency verification", "Ensures applying the same infrastructure code repeatedly produces the same end state without unintended side effects"],
    ])},
    "web-development-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Content delivery network", "A distributed network of servers that caches and serves content from locations near end users"],
        ["Cache hierarchy design", "Multi-tier caching (edge, regional, origin) balances hit rate against storage cost and freshness"],
    ])},
    "web-development-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["DNS resolution", "The process of translating a human-readable domain name into an IP address"],
        ["Latency optimization", "Techniques like DNS prefetching and shorter TTLs balance resolution speed against caching efficiency"],
    ])},
    "web-development-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["WebSocket", "A protocol providing a persistent, full-duplex connection between browser and server for real-time communication"],
        ["Scaling architecture", "Requires careful connection management and sticky routing when scaling across many backend server instances"],
    ])},
    "web-development-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Backpressure", "A mechanism for a slow consumer to signal a fast producer to reduce its data rate, preventing overload"],
        ["Streaming data pipeline", "Essential for preventing memory exhaustion when downstream processing can't keep pace with incoming data"],
    ])},
    "web-development-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Full-text search ranking", "Orders search results by estimated relevance to the user's query"],
        ["Web platform architecture", "Combines relevance signals like term frequency with business signals like popularity or recency"],
    ])},
    "web-development-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Recommendation system integration", "Embeds personalized recommendation logic directly into web UI components and flows"],
        ["Formal model", "Must balance recommendation latency requirements against the complexity of the underlying ranking model"],
    ])},
    "web-development-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Model serving architecture", "Infrastructure for deploying trained ML models so they can respond to real-time prediction requests"],
        ["Web application integration", "Must handle latency, versioning, and scaling requirements distinct from typical web backend services"],
    ])},
    "web-development-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Client-side inference", "Runs a trained machine learning model directly in the browser rather than on a remote server"],
        ["Browser ML formal model", "Trades server round-trip latency and cost for constraints on model size and available compute"],
    ])},
    "web-development-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Privacy-preserving analytics", "Measures user behavior and product performance while minimizing exposure of individually identifiable data"],
        ["Web platform architecture", "Techniques include aggregation, differential privacy, and on-device computation of analytics signals"],
    ])},
    "web-development-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Consent management platform", "Manages and records user consent choices for data collection and processing across a web platform"],
        ["Formal architecture", "Must reliably propagate consent state to every downstream system that processes the user's data"],
    ])},
    "web-development-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tenant SaaS", "A single application instance serves multiple independent customer organizations (tenants)"],
        ["Data isolation architecture", "Must strictly prevent one tenant's data from being accessible to another, even under application bugs"],
    ])},
    "web-development-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Database migration safety", "Ensures schema changes can be applied without corrupting data or breaking currently running application code"],
        ["Zero-downtime deployment", "Requires backward- and forward-compatible migration steps so old and new code can run simultaneously during rollout"],
    ])},
    "web-development-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Event sourcing", "Persists application state as an append-only sequence of events rather than just the current state"],
        ["Web application state architecture", "Enables reconstructing past states and provides a complete audit trail of all changes"],
    ])},
    "web-development-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["CQRS", "Command Query Responsibility Segregation separates the models used for writing data from those used for reading it"],
        ["Consistency boundary", "Read models may lag behind writes, requiring explicit reasoning about acceptable staleness in each part of the system"],
    ])},
    "web-development-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["API gateway", "A single entry point that routes requests to backend services while handling cross-cutting concerns centrally"],
        ["Cross-cutting concern", "Includes authentication, rate limiting, and logging, handled once at the gateway rather than duplicated in each service"],
    ])},
    "web-development-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Circuit breaker pattern", "Stops calling a failing downstream service temporarily, allowing it time to recover instead of overwhelming it further"],
        ["Reliability formal model", "Models the transition between closed, open, and half-open states based on observed failure rates"],
    ])},
    "web-development-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Threat intelligence integration", "Incorporates external feeds of known malicious indicators into a web application's security defenses"],
        ["Application security", "Enables proactively blocking traffic from sources already known to be associated with malicious activity"],
    ])},
    "web-development-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Thesis-level capstone", "A culminating project requiring original design and evaluation of a novel web systems contribution"],
        ["Original research investigation", "Requires identifying a genuine gap in existing web systems approaches and rigorously evaluating a proposed solution"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Web Development"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"web-development-m2-l{base_n}"
        worked_key = f"web-development-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Web Development lessons.")


if __name__ == "__main__":
    main()
