#!/usr/bin/env python3
"""Depth pass, M2 JavaScript: fill in real, hand-checked data_table
content for the M2 JavaScript lessons not covered by the earlier
breadth-first batch. Brings M2 JavaScript to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning V8/JS
engine internals (hidden classes, GC, JIT, deoptimization), advanced
TypeScript type-level programming, build tooling internals (Babel,
bundlers, tree shaking), frontend framework internals (React fiber,
Svelte/SolidJS reactivity), web platform APIs (Streams, WebRTC,
IndexedDB, Web Components), advanced testing and observability,
runtime internals (Deno/Bun, module resolution), formal
language/specification analysis (ECMAScript semantics, prototype
chain, TDZ), and applied performance/security engineering; l101-l120
are "Worked Analysis" companions reusing the data_table of l1-l20
(direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_javascript_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Hidden class", "V8's internal representation tracking an object's shape (property layout) to enable fast property access"],
    ["Inline cache", "Caches the result of a property lookup at a call site, dramatically speeding up repeated accesses of the same object shape"],
])

CHARTS: dict[str, dict] = {
    "javascript-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Advanced JavaScript pattern", "Sophisticated code organization techniques addressing complex state, composition, and architecture problems"],
        ["Application", "Includes patterns like the module pattern, mixins, and advanced closures for building maintainable large-scale applications"],
    ])},
    "javascript-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["JavaScript capstone project", "An applied culminating project demonstrating end-to-end advanced JavaScript system design and implementation skill"],
        ["Deliverable", "Typically a substantial working application demonstrating mastery of performance, architecture, or engine-level concepts"],
    ])},
    "javascript-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Generational garbage collection", "Separates newly created objects (young generation) from long-lived ones, since most objects die young"],
        ["Incremental marking", "Spreads garbage collection work across multiple smaller steps to avoid long pauses that would freeze the application"],
    ])},
    "javascript-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["JIT compilation pipeline", "Modern JS engines progressively compile hot code paths through multiple tiers of increasingly optimized machine code"],
        ["Tiered compilation", "Starts with an interpreter or baseline compiler, then promotes frequently executed code to more aggressive optimizing compilers"],
    ])},
    "javascript-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Deoptimization", "V8 falls back from optimized machine code to slower, more general code when a speculative assumption is violated"],
        ["Speculative optimization", "The JIT compiler optimizes code based on observed type patterns, which can be wrong and require deoptimization"],
    ])},
    "javascript-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Microtask", "A queued task (like Promise callbacks) processed to completion before the event loop continues to the next macrotask"],
        ["Macrotask ordering", "Macrotasks (like setTimeout callbacks) run one at a time, with all pending microtasks drained fully between them"],
    ])},
    "javascript-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["WeakRef", "Holds a reference to an object without preventing that object from being garbage collected"],
        ["FinalizationRegistry", "Lets code register a callback to run after an object has been garbage collected, for cleanup of associated external resources"],
    ])},
    "javascript-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Proxy", "Wraps an object to intercept and customize fundamental operations like property access or assignment"],
        ["Reflect", "Provides methods mirroring the default behavior of the operations Proxy can intercept, useful within trap implementations"],
    ])},
    "javascript-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Tail call optimization", "Reuses the current stack frame for a tail-position function call, avoiding stack growth for deeply recursive calls"],
        ["Engine support status", "Despite being specified in ECMAScript, proper tail call optimization remains inconsistently implemented across major JS engines"],
    ])},
    "javascript-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["SharedArrayBuffer", "Allows multiple JavaScript contexts (main thread and workers) to share the same underlying memory"],
        ["Atomics", "Provides low-level synchronization primitives for safely coordinating access to shared memory across threads"],
    ])},
    "javascript-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Async generator", "A generator function combining async/await with yield, producing values asynchronously across multiple await points"],
        ["Advanced pattern", "Enables elegant lazy, asynchronous data streaming patterns like paginated API consumption"],
    ])},
    "javascript-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Custom iterator", "An object implementing the Symbol.iterator method to define custom iteration behavior for for-of loops"],
        ["Iteration protocol internals", "Requires correctly implementing next() to return {value, done} pairs matching the specification"],
    ])},
    "javascript-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Structural typing challenge", "TypeScript's structural type system can produce surprising compatibility results in large codebases with many similar shapes"],
        ["Large-scale codebase", "Requires careful type design discipline to avoid unintended structural compatibility between logically distinct types"],
    ])},
    "javascript-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Conditional type", "A TypeScript type that resolves differently based on a type-level condition, similar to an if-statement for types"],
        ["Mapped type", "Transforms each property of an existing type according to a specified rule, generating a new derived type"],
    ])},
    "javascript-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Variance (generics)", "Describes how subtyping relationships between type parameters affect subtyping of the generic types built from them"],
        ["Type inference (generics)", "TypeScript's compiler automatically infers generic type parameters from usage context, following specific inference rules"],
    ])},
    "javascript-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Abstract syntax tree transformation", "Programmatically modifies a parsed code representation before it is converted back to source or bytecode"],
        ["Babel plugin", "A module that defines specific AST transformation rules, letting Babel compile modern or custom syntax to compatible JavaScript"],
    ])},
    "javascript-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Source map", "A file mapping transpiled/bundled code positions back to their original source locations"],
        ["Debugging transpiled code", "Enables debugging tools to show original source code even when running transformed, minified production code"],
    ])},
    "javascript-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Tree shaking", "Statically analyzes module dependencies to eliminate code that is never actually imported or used"],
        ["Dead code elimination", "Reduces final bundle size by removing unreachable or unused code paths identified during the build process"],
    ])},
    "javascript-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Module bundler", "Combines and transforms JavaScript modules into optimized output files for browser deployment"],
        ["Dependency graph", "Bundlers like Webpack build a graph of module dependencies to determine what code to include and how to split it"],
    ])},
    "javascript-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Code splitting", "Divides application code into smaller chunks loaded on demand rather than one large upfront bundle"],
        ["Single-page application strategy", "Careful chunk boundaries reduce initial load time while avoiding excessive small-file request overhead"],
    ])},
    "javascript-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Reactive programming", "A declarative paradigm for working with asynchronous data streams that emit values over time"],
        ["RxJS Observable", "A composable stream abstraction from the RxJS library that other code can subscribe to for a sequence of values or events"],
    ])},
    "javascript-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Virtual DOM diffing", "Compares a new virtual DOM tree against the previous version to compute the minimal set of real DOM updates needed"],
        ["Algorithm design", "Balances diffing accuracy against computational cost, typically using heuristics like keyed list reconciliation"],
    ])},
    "javascript-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Fiber architecture", "React's internal reconciliation engine that breaks rendering work into interruptible units"],
        ["Concurrent rendering", "Allows React to pause, resume, or abandon rendering work to keep the UI responsive during large updates"],
    ])},
    "javascript-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Custom hook composition", "Combining multiple React hooks into reusable custom hooks encapsulating shared stateful logic"],
        ["Common pitfall", "Improper dependency arrays or hook ordering can introduce subtle bugs like stale closures or infinite render loops"],
    ])},
    "javascript-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Hydration mismatch", "Occurs when server-rendered HTML doesn't match what the client would render, causing hydration errors"],
        ["Debugging", "Requires identifying sources of nondeterminism (like date formatting or random values) that differ between server and client rendering"],
    ])},
    "javascript-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Streaming server-side rendering", "Sends HTML to the browser progressively as it's generated, rather than waiting for the entire page to render"],
        ["Architecture benefit", "Reduces time-to-first-byte and lets the browser start displaying content before the full response completes"],
    ])},
    "javascript-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Islands architecture", "Renders most of a page as static HTML, hydrating only small interactive \"islands\" of JavaScript"],
        ["Partial hydration", "Reduces the amount of JavaScript shipped and hydrated compared with hydrating an entire page"],
    ])},
    "javascript-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Content Security Policy", "A browser security mechanism restricting which sources of content a page is allowed to load or execute"],
        ["JavaScript application design", "Well-designed CSP significantly mitigates the impact of cross-site scripting vulnerabilities even if they occur"],
    ])},
    "javascript-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Prototype pollution", "An attack that maliciously modifies Object.prototype, affecting the behavior of all objects in the application"],
        ["Mitigation", "Includes using Object.create(null), Map instead of plain objects, and validating keys during deep merges"],
    ])},
    "javascript-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Closure (encapsulation)", "A function retaining access to its defining scope's variables, usable to create private state"],
        ["Memoization pattern", "Uses a closure to cache the results of expensive function calls, returning the cached result for repeated identical inputs"],
    ])},
    "javascript-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Currying", "Transforms a function taking multiple arguments into a sequence of functions each taking a single argument"],
        ["Function composition", "Combines multiple functions so the output of one becomes the input of the next, building complex behavior from simple pieces"],
    ])},
    "javascript-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Immutable data structure", "A data structure that cannot be modified after creation; changes produce a new structure instead"],
        ["Structural sharing", "An efficient implementation technique where unchanged parts of a data structure are shared between old and new versions"],
    ])},
    "javascript-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Service worker lifecycle", "The distinct install, activate, and fetch phases a service worker passes through, each with specific timing guarantees"],
        ["Offline-first architecture", "Designs an application to function without network connectivity by leveraging service worker caching from the start"],
    ])},
    "javascript-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["IndexedDB", "A browser API for storing significant amounts of structured data client-side, with transactional guarantees"],
        ["Transaction model", "Groups related read/write operations atomically, ensuring data consistency even if the browser crashes mid-operation"],
    ])},
    "javascript-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["WebSocket", "A protocol providing a persistent, full-duplex connection between browser and server for real-time bidirectional communication"],
        ["Server-Sent Events", "A simpler protocol for one-way server-to-client streaming over standard HTTP, sufficient when the client doesn't need to send data back"],
    ])},
    "javascript-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["WebRTC peer connection", "Enables direct browser-to-browser communication for audio, video, or data without routing through a central server"],
        ["NAT traversal", "Techniques like STUN and TURN help establish direct peer connections despite the network address translation many users are behind"],
    ])},
    "javascript-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Regular expression backtracking", "The process by which a regex engine retries alternative matches after a partial match fails"],
        ["Complexity", "Certain regex patterns can suffer catastrophic exponential-time backtracking on specific malicious or pathological inputs"],
    ])},
    "javascript-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Unicode handling", "Correctly processing text that may include characters outside the basic multilingual plane, like emoji"],
        ["Internationalization (strings)", "JavaScript string operations must account for surrogate pairs and grapheme clusters to handle Unicode text correctly"],
    ])},
    "javascript-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Temporal API", "A modern JavaScript proposal providing a more robust, less error-prone replacement for the legacy Date object"],
        ["Advanced date/time handling", "Addresses long-standing pain points like time zone handling and mutable date objects in the original Date API"],
    ])},
    "javascript-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Error boundary", "A React component that catches JavaScript errors in its child component tree and displays a fallback UI"],
        ["Fault isolation pattern", "Prevents a single component's crash from taking down the entire application UI"],
    ])},
    "javascript-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["State machine", "A formal model representing an application as a finite set of states and the transitions between them"],
        ["XState", "A JavaScript library for building explicit, visualizable state machines to manage complex UI logic reliably"],
    ])},
    "javascript-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Dependency injection", "Supplies a component's dependencies from outside rather than having it construct them internally"],
        ["Frontend architecture pattern", "Improves testability and modularity by decoupling components from concrete implementations of their dependencies"],
    ])},
    "javascript-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Micro-frontend", "Splits a large web application into independently developed and deployed frontend modules"],
        ["Runtime composition", "Combines separately built micro-frontends into a single cohesive application at runtime rather than build time"],
    ])},
    "javascript-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Property-based testing", "Generates many random test inputs to verify general properties hold, rather than testing fixed example cases"],
        ["JavaScript application", "Libraries generate diverse inputs to a function under test, automatically finding edge cases manual tests might miss"],
    ])},
    "javascript-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Mutation testing", "Deliberately introduces small bugs (mutants) into code to check whether the test suite actually catches them"],
        ["Test suite quality (JavaScript)", "A surviving mutant that no test catches reveals a gap in the test suite's actual coverage of behavior"],
    ])},
    "javascript-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Visual regression testing", "Automatically compares screenshots of UI components against a baseline to detect unintended visual changes"],
        ["Testing pipeline", "Catches subtle CSS or layout regressions that functional tests alone would not detect"],
    ])},
    "javascript-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Chrome DevTools Protocol", "A protocol allowing external tools to instrument, inspect, and profile a Chromium-based browser programmatically"],
        ["Performance profiling", "Enables automated, scriptable performance analysis beyond manually using the DevTools UI"],
    ])},
    "javascript-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Memory leak", "Memory that is no longer needed but remains referenced, preventing garbage collection and causing memory usage to grow"],
        ["Long-running application detection", "Especially important in single-page applications that stay open for extended periods, where leaks accumulate over time"],
    ])},
    "javascript-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Module federation", "A runtime mechanism letting separately built JavaScript bundles share code and dependencies dynamically"],
        ["Micro-frontend bundling", "Avoids duplicating common libraries across independently deployed micro-frontends, reducing total bundle size"],
    ])},
    "javascript-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Compiler-based reactivity", "Shifts reactivity analysis to build time rather than runtime, generating optimized update code ahead of time"],
        ["Svelte build pipeline", "Svelte's compiler analyzes reactive dependencies at compile time, producing highly optimized vanilla JavaScript with no runtime framework overhead"],
    ])},
    "javascript-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Fine-grained reactivity", "Updates only the specific parts of the UI that depend on a changed value, rather than re-rendering larger component trees"],
        ["SolidJS signal graph", "SolidJS builds a dependency graph of signals at runtime, enabling surgical, precise DOM updates without a virtual DOM diff"],
    ])},
    "javascript-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Custom JavaScript runtime", "An alternative JavaScript execution environment outside the browser, such as Deno or Bun"],
        ["Runtime internals", "Each offers different security models, module systems, and performance characteristics compared with Node.js"],
    ])},
    "javascript-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Package manager resolution algorithm", "Determines which specific version of each dependency (and its transitive dependencies) to install"],
        ["Advanced resolution", "Must satisfy potentially conflicting version constraints across a large dependency tree, often via SAT-solving-like approaches"],
    ])},
    "javascript-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Monorepo", "A single repository containing multiple related projects or packages"],
        ["Build orchestration and caching", "Tools optimize monorepo builds by caching unchanged package outputs and only rebuilding what actually changed"],
    ])},
    "javascript-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["ESLint rule authoring", "Writing custom linting rules to enforce project-specific code quality or style conventions"],
        ["AST-based linting", "Custom rules analyze a file's abstract syntax tree to detect patterns that violate the desired convention"],
    ])},
    "javascript-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["JavaScript engine benchmarking", "Measures and compares the performance of JavaScript code across different engines or engine versions"],
        ["Methodology", "Requires careful control of warm-up effects, JIT optimization state, and statistical variance for reliable results"],
    ])},
    "javascript-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Type-safe variadic function", "A function accepting a variable number of arguments while still preserving precise type information for each"],
        ["Advanced currying application", "TypeScript's advanced generic features can express curried functions with fully type-safe variadic argument handling"],
    ])},
    "javascript-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["ECMAScript specification", "The formal standard defining the JavaScript language's syntax and semantics"],
        ["Formal semantics", "The specification uses precise, algorithmic pseudocode to define exact language behavior, resolving engine implementation ambiguity"],
    ])},
    "javascript-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Symbol", "A unique, immutable primitive value often used as a non-colliding property key"],
        ["Protocol-based programming", "Well-known symbols (like Symbol.iterator) let objects opt into language-level protocols without name collisions"],
    ])},
    "javascript-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Streams API", "A web platform API for processing data incrementally as it becomes available, rather than all at once"],
        ["Backpressure", "The API includes built-in mechanisms for a slow consumer to signal a producer to reduce its rate, preventing overload"],
    ])},
    "javascript-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Promise combinator", "Functions like Promise.all and Promise.race that combine multiple promises according to different completion semantics"],
        ["Cancellation pattern", "Native Promises lack built-in cancellation, requiring patterns like AbortController to achieve cancellable async operations"],
    ])},
    "javascript-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Custom element", "A web standard for defining new, reusable HTML tags with custom behavior"],
        ["Shadow DOM encapsulation", "Provides a scoped DOM and CSS subtree for a custom element, isolating its internal structure and styles from the rest of the page"],
    ])},
    "javascript-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Declarative Shadow DOM", "Allows Shadow DOM to be declared directly in server-rendered HTML rather than only attached via JavaScript"],
        ["Web component server rendering", "Enables web components to render correctly on the server without requiring client-side JavaScript to construct the shadow root"],
    ])},
    "javascript-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["CSS-in-JS", "Writes component styles directly in JavaScript, often generating CSS dynamically at runtime"],
        ["Runtime performance trade-off", "Runtime style generation carries a performance cost compared with static CSS, motivating build-time CSS-in-JS alternatives"],
    ])},
    "javascript-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Atomic CSS", "Generates single-purpose utility classes, each applying one specific style property"],
        ["Build-time generation engine", "Tools scan source code and generate only the specific atomic CSS classes actually used, minimizing final stylesheet size"],
    ])},
    "javascript-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Accessibility tree", "A parallel tree derived from the DOM that assistive technologies use to understand and navigate a page"],
        ["ARIA semantics", "Attributes providing additional semantic information to the accessibility tree beyond what native HTML elements convey"],
    ])},
    "javascript-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Formal verification (JS type safety)", "Mathematically proves that JavaScript or TypeScript code satisfies specific type-correctness properties"],
        ["Approach", "Given JavaScript's dynamic nature, formal verification typically applies to a restricted, more analyzable subset or the TypeScript layer"],
    ])},
    "javascript-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Conditional export", "Lets a package define different module entry points depending on the consuming environment (Node, browser, etc.)"],
        ["Import map", "A browser mechanism mapping bare module specifiers to actual URLs, enabling native ES module resolution without a bundler"],
    ])},
    "javascript-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Edge runtime", "A constrained JavaScript execution environment running at network edge locations for low-latency serverless functions"],
        ["Serverless constraint", "Edge runtimes typically restrict available APIs and execution time compared with full Node.js server environments"],
    ])},
    "javascript-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Async stack trace", "A stack trace spanning across multiple await boundaries, showing the logical call chain of asynchronous code"],
        ["Debugging challenge", "Async execution can obscure the original call site, making bugs harder to trace without proper async stack trace support"],
    ])},
    "javascript-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Content-addressable caching", "Caches build artifacts keyed by a hash of their content, so identical inputs always produce cache hits"],
        ["Module caching in build tools", "Enables highly efficient incremental builds by skipping recompilation of modules whose content hasn't changed"],
    ])},
    "javascript-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["State synchronization", "Keeps application state consistent across a client that goes offline and later reconnects to a server"],
        ["Offline-first application", "Requires conflict resolution strategies for changes made independently while offline before they can be merged with server state"],
    ])},
    "javascript-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Formal grammar design", "Specifies the precise syntax rules for a new language or notation"],
        ["Domain-specific language in JS", "Building a DSL embedded in or compiled from JavaScript requires designing and implementing a grammar tailored to the target domain"],
    ])},
    "javascript-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Layout thrashing", "Occurs when code repeatedly reads and writes layout-affecting properties, forcing the browser to recalculate layout many times unnecessarily"],
        ["Prevention", "Batching all layout reads before all layout writes avoids forcing repeated synchronous layout recalculation"],
    ])},
    "javascript-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["GPU-accelerated compositing", "Offloads certain rendering operations to the GPU, enabling smoother animations that don't block the main thread"],
        ["CSS Paint API", "Allows defining custom paint logic in JavaScript that the browser can execute during the compositing stage"],
    ])},
    "javascript-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Subresource integrity", "Lets a browser verify that a fetched resource (like a CDN script) hasn't been tampered with, via a cryptographic hash"],
        ["Trusted Types", "A browser API preventing DOM-based cross-site scripting by requiring dangerous sink assignments to use vetted, typed values"],
    ])},
    "javascript-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Prototype chain", "The linked sequence of objects JavaScript searches through to resolve a property that isn't found on an object directly"],
        ["Resolution formal model", "Property lookup walks up the prototype chain until the property is found or the chain ends at null"],
    ])},
    "javascript-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Worker pool", "A managed set of Web Workers that distributes computational tasks across them for parallel execution"],
        ["Task scheduling (JavaScript)", "Efficient scheduling balances load across available workers while managing task queuing and result collection"],
    ])},
    "javascript-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Custom compiler (JSX/template DSLs)", "Transforms specialized syntax like JSX or template literal tagged strings into standard JavaScript"],
        ["Design", "Requires parsing the custom syntax and generating equivalent, efficient JavaScript output code"],
    ])},
    "javascript-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Differential loading", "Serves modern JavaScript syntax to capable browsers and a transpiled, polyfilled bundle to legacy browsers"],
        ["Legacy browser support", "Avoids penalizing modern browser users with unnecessary transpilation overhead just to support older browsers"],
    ])},
    "javascript-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Event delegation", "Attaches a single event listener to a parent element to handle events from many child elements via bubbling"],
        ["Performance trade-off", "Reduces the number of listeners needed but requires careful target checking within the delegated handler"],
    ])},
    "javascript-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Distributed tracing", "Tracks a single request as it flows through multiple services, correlating spans into one coherent trace"],
        ["Node.js observability application", "Enables diagnosing latency and error sources across complex, multi-service Node.js backend systems"],
    ])},
    "javascript-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Static site generator", "Converts source content into a set of pre-built static HTML pages at build time"],
        ["Incremental build", "Rebuilds only the pages affected by a content change rather than regenerating the entire site from scratch"],
    ])},
    "javascript-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Recursive conditional type", "A TypeScript conditional type that references itself, enabling type-level computation over recursively structured types"],
        ["Type-level programming", "Advanced TypeScript can express surprisingly sophisticated compile-time computations purely through its type system"],
    ])},
    "javascript-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Race condition", "A bug where the outcome depends on the unpredictable timing of concurrent operations"],
        ["Formal verification (Node.js async)", "Formal analysis techniques can systematically identify race conditions in asynchronous Node.js code that testing might miss"],
    ])},
    "javascript-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Module graph visualization", "Displays a project's dependency structure visually to aid understanding of its architecture"],
        ["Cycle detection", "Identifies circular dependencies between modules, which can cause subtle initialization order bugs"],
    ])},
    "javascript-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Runtime sandboxing", "Runs untrusted JavaScript code in a restricted environment that limits its access to system resources"],
        ["Untrusted execution", "Necessary when executing user-submitted JavaScript code, since the language itself has no built-in security sandbox"],
    ])},
    "javascript-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Streaming JSON parsing", "Parses JSON incrementally as data arrives, rather than requiring the complete payload before parsing begins"],
        ["Large payload application", "Reduces memory usage and enables processing to begin before an entire large JSON response has finished downloading"],
    ])},
    "javascript-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["JavaScript Realm", "An isolated global environment with its own set of intrinsic objects, such as a separate iframe or worker"],
        ["Compartment proposal", "A proposed mechanism for creating lightweight, secure sub-environments within a single realm for sandboxing untrusted code"],
    ])},
    "javascript-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Nested layout (client-side routing)", "Allows different route segments to render within a shared, persistent layout structure"],
        ["Data loader", "A routing pattern where each route segment declares its own data-fetching logic, executed before or during navigation"],
    ])},
    "javascript-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Custom framework-specific linting", "Linting rules tailored to catch anti-patterns specific to a particular framework, like React or Vue"],
        ["Application", "Catches framework-specific mistakes (like missing dependency array entries) that general-purpose linters wouldn't know to check"],
    ])},
    "javascript-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["JIT optimization failure", "Cases where the engine's optimizing compiler cannot successfully optimize a code path, falling back to slower execution"],
        ["Profiling", "Specialized profiling tools can reveal which specific code patterns are preventing JIT optimization"],
    ])},
    "javascript-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Structured clone algorithm", "The browser's built-in algorithm for deep-copying complex JavaScript values, used by postMessage and structuredClone"],
        ["Formal semantics", "Precisely defines which value types can be cloned and how circular references and special objects are handled"],
    ])},
    "javascript-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Optional chaining", "Safely accesses a potentially null or undefined property chain, short-circuiting to undefined instead of throwing"],
        ["Nullish coalescing", "Provides a default value only when the left operand is null or undefined, unlike the logical OR operator's broader falsy check"],
    ])},
    "javascript-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Custom transpiler pipeline", "A build pipeline compiling experimental JavaScript syntax not yet supported natively by browsers"],
        ["TC39 proposal application", "Lets developers experiment with proposed future JavaScript features before they reach standardization and native engine support"],
    ])},
    "javascript-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Master's thesis seminar", "A forum for presenting and defending original JavaScript engineering research to faculty and peers"],
        ["Original research", "Emphasizes a clearly stated hypothesis, appropriate baselines, and rigorous experimental or formal evaluation"],
    ])},
    "javascript-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["WebAssembly Component Model", "A proposed standard for composing WebAssembly modules written in different languages into interoperable components"],
        ["Cross-language interoperability", "Enables Rust, C++, and other WebAssembly-compiled languages to interoperate cleanly with JavaScript and each other"],
    ])},
    "javascript-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Import assertion", "Syntax specifying the expected type of an imported module, such as asserting a JSON module import"],
        ["JSON module loading", "Enables natively importing JSON files as modules with appropriate type-checking assertions"],
    ])},
    "javascript-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Temporal Dead Zone", "The period between entering a scope and a let/const variable's declaration, during which accessing it throws an error"],
        ["Lexical scoping formal analysis", "A deliberate design choice preventing use of a variable before its declaration, unlike var's hoisting-and-undefined behavior"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["JavaScript"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"javascript-m2-l{base_n}"
        worked_key = f"javascript-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 JavaScript lessons.")


if __name__ == "__main__":
    main()
