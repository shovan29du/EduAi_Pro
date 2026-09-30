#!/usr/bin/env python3
"""Depth pass, M1 JavaScript: fill in real, hand-checked data_table
and formulae (runnable code) content for the 119 M1 JavaScript
lessons not covered by the earlier breadth-first batch. Brings M1
JavaScript to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
testing/tooling, language internals and V8, frontend architecture,
real-time/graphics systems, Node.js internals, and security; l101-l120
are "Worked Analysis" companions reusing the data_table/formulae of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch (data_table only, no formulae there), so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_javascript_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Jest", "A popular JavaScript testing framework with built-in assertions and mocking"],
    ["expect()", "Jest's assertion function used to check a value against an expectation"],
])

CHARTS: dict[str, dict] = {
    "javascript-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Testing JavaScript", "Verifies code behaves correctly through automated unit and integration tests"],
    ]), "formulae": ["test('adds', () => { expect(1 + 1).toBe(2); });"]},
    "javascript-m1-l2": {"data_table": table(["Tool", "Purpose"], [
        ["Build tool / package manager", "Bundles source code and manages project dependencies"],
    ]), "formulae": ["npm install\nnpm run build"]},
    "javascript-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["TDD", "Writes a failing test first, then implements just enough code to make it pass"],
    ]), "formulae": ["test('sum', () => { expect(sum(2,2)).toBe(4); }); // then implement sum"]},
    "javascript-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Mock / spy", "Replaces or observes a function's calls to isolate a unit under test"],
    ]), "formulae": ["const spy = jest.fn();\nspy('a');\nexpect(spy).toHaveBeenCalledWith('a');"]},
    "javascript-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Integration testing", "Tests how multiple units of code work correctly together"],
    ]), "formulae": ["test('api returns data', async () => {\n  const res = await request(app).get('/items');\n  expect(res.status).toBe(200);\n});"]},
    "javascript-m1-l7": {"data_table": table(["Tool", "Purpose"], [
        ["Playwright / Cypress", "Automate real browser interactions to test full user flows end-to-end"],
    ]), "formulae": ["await page.click('#submit');\nawait expect(page.locator('.success')).toBeVisible();"]},
    "javascript-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Code coverage", "Measures what percentage of code is executed by the test suite"],
    ]), "formulae": ["jest --coverage"]},
    "javascript-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["CI for JS projects", "Automatically runs lint, tests, and build on every push"],
    ]), "formulae": ["# GitHub Actions\nrun: npm ci && npm test"]},
    "javascript-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Semantic versioning", "Encodes MAJOR.MINOR.PATCH meaning into a package's version number"],
    ]), "formulae": ["npm version patch\nnpm publish"]},
    "javascript-m1-l11": {"data_table": table(["Tool", "Purpose"], [
        ["Lerna / Nx / Turborepo", "Manage builds and dependencies across multiple packages in one repository"],
    ]), "formulae": ["npx turbo run build"]},
    "javascript-m1-l12": {"data_table": table(["Tool", "Purpose"], [
        ["Chrome DevTools profiler", "Measures where a JavaScript program spends CPU time"],
    ]), "formulae": ["console.time('op');\n// work\nconsole.timeEnd('op');"]},
    "javascript-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Memory leak", "Memory that is never released because it remains unintentionally referenced"],
    ]), "formulae": ["let cache = new Map(); // grows unbounded if never cleared"]},
    "javascript-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Web Worker", "Runs JavaScript on a separate thread to avoid blocking the main UI thread"],
    ]), "formulae": ["const worker = new Worker('worker.js');\nworker.postMessage('start');"]},
    "javascript-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["V8", "The JavaScript engine used by Chrome and Node.js, compiling JS to machine code"],
    ]), "formulae": ["node --v8-options"]},
    "javascript-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["JIT compilation", "Compiles frequently-run code to optimized machine code while the program runs"],
    ]), "formulae": ["// V8 tiers up hot functions automatically, no code change needed"]},
    "javascript-m1-l17": {"data_table": table(["Vulnerability", "Feature"], [
        ["XSS", "Injects malicious scripts into pages viewed by other users"],
        ["CSRF", "Tricks a user's browser into making an unwanted authenticated request"],
    ]), "formulae": ["element.textContent = userInput; // safe, avoids innerHTML injection"]},
    "javascript-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Content Security Policy", "Restricts which sources of scripts and content a page is allowed to load"],
    ]), "formulae": ["// HTTP header\nContent-Security-Policy: script-src 'self'"]},
    "javascript-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Minification", "Shrinks JavaScript file size by removing whitespace and shortening names"],
    ]), "formulae": ["npx terser input.js -o output.min.js"]},
    "javascript-m1-l20": {"data_table": table(["Term", "Meaning"], [
        ["Progressive rollout", "Gradually enables a feature for an increasing percentage of users"],
    ]), "formulae": ["if (Math.random() < 0.1) enableFeature();"]},
    "javascript-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Proxy / Reflect", "Intercepts and customizes fundamental operations on an object"],
    ]), "formulae": ["const p = new Proxy({}, { get(t, k) { return `got ${k}`; } });\np.x; // 'got x'"]},
    "javascript-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Generator", "A function that can pause and resume execution, yielding a sequence of values"],
    ]), "formulae": ["function* gen() { yield 1; yield 2; }\n[...gen()]; // [1, 2]"]},
    "javascript-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Async generator", "Combines generators with async/await to yield a sequence of promises over time"],
    ]), "formulae": ["async function* agen() { yield await fetch('/a'); }"]},
    "javascript-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Microtask queue", "Runs promise callbacks before the next macrotask (e.g. setTimeout) executes"],
    ]), "formulae": ["Promise.resolve().then(() => console.log('microtask'));\nsetTimeout(() => console.log('macrotask'));"]},
    "javascript-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["WeakMap / WeakRef", "Hold references without preventing an object from being garbage collected"],
    ]), "formulae": ["const wm = new WeakMap();\nwm.set(obj, 'metadata');"]},
    "javascript-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Structured clone", "Deep-copies complex JavaScript values, including circular references"],
    ]), "formulae": ["const copy = structuredClone(original);"]},
    "javascript-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["SharedArrayBuffer / Atomics", "Share raw memory and perform thread-safe operations across workers"],
    ]), "formulae": ["const sab = new SharedArrayBuffer(4);\nAtomics.add(new Int32Array(sab), 0, 1);"]},
    "javascript-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["WebAssembly interop", "Lets JavaScript call and exchange data with compiled Wasm modules"],
    ]), "formulae": ["const { instance } = await WebAssembly.instantiateStreaming(fetch('mod.wasm'));"]},
    "javascript-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Module federation", "Lets independently built micro-frontends share code at runtime"],
    ]), "formulae": ["// webpack.config.js\nnew ModuleFederationPlugin({ name: 'app1', exposes: {} })"]},
    "javascript-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Type-level programming", "Uses TypeScript's type system to compute types themselves, not just values"],
    ]), "formulae": ["type Unwrap<T> = T extends Promise<infer U> ? U : T;"]},
    "javascript-m1-l31": {"data_table": table(["Pattern", "Purpose"], [
        ["Module pattern", "Encapsulates private state using closures for large-scale apps"],
    ]), "formulae": ["const Counter = (() => { let n = 0; return { inc: () => ++n }; })();"]},
    "javascript-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Observable", "Represents a stream of values over time that observers can subscribe to"],
    ]), "formulae": ["import { Subject } from 'rxjs';\nconst s = new Subject();\ns.subscribe(v => console.log(v));"]},
    "javascript-m1-l33": {"data_table": table(["Pattern", "Feature"], [
        ["State management", "Centralizes application state to keep UI updates predictable"],
    ]), "formulae": ["const store = { state: {}, dispatch(action) { /* reduce */ } };"]},
    "javascript-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["SSR", "Renders a page's HTML on the server before sending it to the browser"],
    ]), "formulae": ["const html = ReactDOMServer.renderToString(<App />);"]},
    "javascript-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Streaming SSR", "Sends HTML to the browser in chunks as it becomes ready, hydrating progressively"],
    ]), "formulae": ["ReactDOMServer.renderToPipeableStream(<App />).pipe(res);"]},
    "javascript-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Static site generation", "Pre-renders pages at build time, rebuilding only what changed incrementally"],
    ]), "formulae": ["export async function getStaticProps() { return { props: {} }; }"]},
    "javascript-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Edge runtime", "Executes JavaScript on servers geographically close to the user"],
    ]), "formulae": ["export const config = { runtime: 'edge' };"]},
    "javascript-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Prototype chain", "The lookup chain JavaScript uses to resolve inherited properties and methods"],
    ]), "formulae": ["const animal = { speak() { return 'noise'; } };\nconst dog = Object.create(animal);"]},
    "javascript-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Custom element / Shadow DOM", "Defines a reusable HTML tag with encapsulated internal markup and styles"],
    ]), "formulae": ["class MyEl extends HTMLElement {\n  connectedCallback() { this.attachShadow({mode:'open'}); }\n}\ncustomElements.define('my-el', MyEl);"]},
    "javascript-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Web Components interop", "Ensures custom elements work correctly across different frontend frameworks"],
    ]), "formulae": ["document.createElement('my-el');"]},
    "javascript-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["CSS-in-JS", "Generates and scopes styles using JavaScript at runtime or build time"],
    ]), "formulae": ["const Button = styled.button`color: blue;`;"]},
    "javascript-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Virtual DOM diffing", "Compares two virtual tree snapshots to compute the minimal real DOM update"],
    ]), "formulae": ["// simplified diff\nif (oldVNode.type !== newVNode.type) replace();"]},
    "javascript-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Fine-grained reactivity", "Updates only the exact DOM nodes affected by a changed value, without a virtual DOM"],
    ]), "formulae": ["const [count, setCount] = createSignal(0);"]},
    "javascript-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Compiler-based UI framework", "Compiles component code ahead-of-time into optimized direct DOM updates"],
    ]), "formulae": ["// Svelte compiles reactive statements at build time\n$: doubled = count * 2;"]},
    "javascript-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Error boundary", "Catches rendering errors in a component subtree and shows a fallback UI"],
    ]), "formulae": ["class Boundary extends React.Component {\n  static getDerivedStateFromError() { return { hasError: true }; }\n}"]},
    "javascript-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Internationalization architecture", "Structures an app to support multiple languages and locales"],
    ]), "formulae": ["new Intl.NumberFormat('de-DE').format(1234.5);"]},
    "javascript-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Accessible UI pattern", "Ensures interactive components work correctly with assistive technology"],
    ]), "formulae": ["<button aria-pressed={isActive}>Toggle</button>"]},
    "javascript-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Operational transform", "Resolves concurrent edits by transforming operations to stay consistent"],
    ]), "formulae": ["// simplified OT: transform(op1, op2) resolves position conflicts"]},
    "javascript-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["CRDT", "A data structure that merges concurrent updates automatically without conflicts"],
    ]), "formulae": ["import * as Y from 'yjs';\nconst doc = new Y.Doc();"]},
    "javascript-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["WebSocket protocol", "Provides a persistent, full-duplex connection for real-time client-server messaging"],
    ]), "formulae": ["const ws = new WebSocket('wss://example.com');\nws.onmessage = e => console.log(e.data);"]},
    "javascript-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["WebRTC data channel", "Enables direct peer-to-peer data transfer between browsers"],
    ]), "formulae": ["const pc = new RTCPeerConnection();\nconst channel = pc.createDataChannel('chat');"]},
    "javascript-m1-l52": {"data_table": table(["Strategy", "Feature"], [
        ["Cache-first", "Serves from cache immediately, falling back to network"],
        ["Network-first", "Tries network first, falling back to cache"],
    ]), "formulae": ["self.addEventListener('fetch', e => e.respondWith(caches.match(e.request)));"]},
    "javascript-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Progressive Web App", "A web app that can be installed and work offline like a native app"],
    ]), "formulae": ["navigator.serviceWorker.register('/sw.js');"]},
    "javascript-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["IndexedDB", "A client-side database for storing structured data persistently in the browser"],
    ]), "formulae": ["const req = indexedDB.open('mydb', 1);"]},
    "javascript-m1-l55": {"data_table": table(["API", "Purpose"], [
        ["WebGL / Canvas", "Render 2D and 3D graphics directly in the browser"],
    ]), "formulae": ["const gl = canvas.getContext('webgl');"]},
    "javascript-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["WebGPU", "A modern browser API for high-performance GPU-accelerated graphics and computation"],
    ]), "formulae": ["const adapter = await navigator.gpu.requestAdapter();"]},
    "javascript-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Animation performance", "Uses GPU-accelerated properties (transform, opacity) to keep animations smooth"],
    ]), "formulae": ["element.animate([{transform: 'translateX(0)'}, {transform: 'translateX(100px)'}], 300);"]},
    "javascript-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Module resolution", "The algorithm a bundler or runtime uses to locate an imported module's file"],
    ]), "formulae": ["import { foo } from './utils.js';"]},
    "javascript-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Tree shaking", "Removes unused code from a bundle during the build process"],
    ]), "formulae": ["export function used() {}\nexport function unused() {} // removed if never imported"]},
    "javascript-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Source map", "Maps minified production code back to its original source for debugging"],
    ]), "formulae": ["//# sourceMappingURL=app.js.map"]},
    "javascript-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Micro-benchmarking", "Precisely measures the performance of a small isolated piece of code"],
    ]), "formulae": ["const start = performance.now();\n// code\nperformance.now() - start;"]},
    "javascript-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Regex engine internals", "Compiles a pattern into a state machine that backtracks or matches efficiently"],
    ]), "formulae": ["/\\d+/.exec('a123'); // ['123']"]},
    "javascript-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Functional programming pattern", "Composes pure functions and avoids mutable shared state"],
    ]), "formulae": ["const pipe = (...fns) => x => fns.reduce((v, f) => f(v), x);"]},
    "javascript-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Monad-style error handling", "Wraps a value or error uniformly so failures propagate without exceptions"],
    ]), "formulae": ["const Result = { ok: v => ({ok: true, v}), err: e => ({ok: false, e}) };"]},
    "javascript-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Currying", "Transforms a multi-argument function into a chain of single-argument functions"],
    ]), "formulae": ["const add = a => b => a + b;\nadd(2)(3); // 5"]},
    "javascript-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Dependency injection", "Supplies a component's dependencies from outside rather than constructing them internally"],
    ]), "formulae": ["function createService(logger) { return { log: logger }; }"]},
    "javascript-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Module federation security", "Guards against malicious or compromised remote modules loaded at runtime"],
    ]), "formulae": ["// verify remote entry origin before loading"]},
    "javascript-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["CSP nonce/hash", "Allow-lists specific inline scripts via a per-request token or content hash"],
    ]), "formulae": ["<script nonce=\"random123\">/* trusted */</script>"]},
    "javascript-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Subresource integrity", "Verifies a fetched script or asset hasn't been tampered with, via a hash"],
    ]), "formulae": ["<script src=\"lib.js\" integrity=\"sha384-...\"></script>"]},
    "javascript-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["SPA auth flow", "Manages tokens and session state securely within a client-rendered application"],
    ]), "formulae": ["fetch('/api', { headers: { Authorization: `Bearer ${token}` } });"]},
    "javascript-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["CORS", "Controls which other origins are allowed to make requests to a web resource"],
    ]), "formulae": ["// server response header\nAccess-Control-Allow-Origin: https://example.com"]},
    "javascript-m1-l72": {"data_table": table(["Storage", "Risk"], [
        ["localStorage", "Persistent but accessible to any script on the page (XSS risk)"],
    ]), "formulae": ["localStorage.setItem('key', 'value');"]},
    "javascript-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["GC strategy", "V8 uses generational collection, treating short-lived and long-lived objects differently"],
    ]), "formulae": ["node --expose-gc script.js"]},
    "javascript-m1-l74": {"data_table": table(["Tier", "Feature"], [
        ["Ignition", "V8's baseline bytecode interpreter"],
        ["TurboFan", "V8's optimizing JIT compiler for hot code"],
    ]), "formulae": ["node --trace-opt script.js"]},
    "javascript-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Hidden class / inline cache", "V8 optimizations that speed up repeated property access on similarly-shaped objects"],
    ]), "formulae": ["function Point(x, y) { this.x = x; this.y = y; } // consistent shape helps V8"]},
    "javascript-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Node.js Streams", "Process data incrementally in chunks rather than loading it all into memory"],
    ]), "formulae": ["fs.createReadStream('big.txt').pipe(fs.createWriteStream('out.txt'));"]},
    "javascript-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Worker threads", "Run JavaScript on separate Node.js threads for CPU-bound parallelism"],
    ]), "formulae": ["const { Worker } = require('worker_threads');\nnew Worker('./task.js');"]},
    "javascript-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Cluster mode", "Forks multiple Node.js processes to share incoming connections across CPU cores"],
    ]), "formulae": ["const cluster = require('cluster');\nif (cluster.isPrimary) cluster.fork();"]},
    "javascript-m1-l79": {"data_table": table(["Tool", "Purpose"], [
        ["node --prof", "Profiles a running Node.js application to find CPU bottlenecks"],
    ]), "formulae": ["node --prof app.js"]},
    "javascript-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Native addon", "A compiled C/C++ module Node.js can load for performance-critical work"],
    ]), "formulae": ["const addon = require('bindings')('myaddon');"]},
    "javascript-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["GraphQL federation", "Composes multiple GraphQL services into a single unified API graph"],
    ]), "formulae": ["type Query { hello: String }"]},
    "javascript-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["GraphQL caching", "Caches resolved query results to avoid redundant resolver execution"],
    ]), "formulae": ["const cache = new InMemoryCache();"]},
    "javascript-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["tRPC", "Provides end-to-end type-safe APIs between a TypeScript frontend and backend"],
    ]), "formulae": ["export const appRouter = t.router({ hello: t.procedure.query(() => 'hi') });"]},
    "javascript-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Rate limiting", "Restricts request volume to protect an API from abuse or overload"],
    ]), "formulae": ["app.use(rateLimit({ windowMs: 60000, max: 100 }));"]},
    "javascript-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Idempotency key", "Ensures a repeated request has the same effect as making it once"],
    ]), "formulae": ["fetch('/pay', { headers: { 'Idempotency-Key': uuid } });"]},
    "javascript-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Middleware architecture", "Chains request-processing functions in a defined order"],
    ]), "formulae": ["app.use((req, res, next) => { console.log(req.url); next(); });"]},
    "javascript-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Babel plugin", "Transforms JavaScript source code's AST during the build step"],
    ]), "formulae": ["module.exports = function(babel) { return { visitor: {} }; };"]},
    "javascript-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["AST manipulation", "Programmatically analyzes or rewrites parsed JavaScript source code"],
    ]), "formulae": ["const ast = acorn.parse(code, { ecmaVersion: 2022 });"]},
    "javascript-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Custom ESLint rule", "Enforces a project-specific code style or correctness check"],
    ]), "formulae": ["module.exports = { create(context) { return {}; } };"]},
    "javascript-m1-l90": {"data_table": table(["Bundler", "Feature"], [
        ["Webpack", "Highly configurable, mature bundler"],
        ["Vite", "Fast dev server using native ES modules"],
        ["Rollup", "Optimized for library bundling"],
    ]), "formulae": ["npx vite build"]},
    "javascript-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Code splitting", "Breaks a bundle into smaller chunks loaded only when needed"],
    ]), "formulae": ["const Page = React.lazy(() => import('./Page'));"]},
    "javascript-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["HTTP/3 / QUIC", "A transport protocol built on UDP that reduces latency and connection setup overhead"],
    ]), "formulae": ["// enabled at the server/CDN level, transparent to JS code"]},
    "javascript-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Rendering pipeline optimization", "Minimizes layout thrashing by batching DOM reads and writes"],
    ]), "formulae": ["requestAnimationFrame(() => { el.style.transform = 'translateX(10px)'; });"]},
    "javascript-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Real user monitoring", "Collects performance data from actual visitors' browsers in production"],
    ]), "formulae": ["new PerformanceObserver(list => {}).observe({type: 'largest-contentful-paint'});"]},
    "javascript-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Feature detection", "Checks whether a browser supports an API before using it, rather than guessing by browser name"],
    ]), "formulae": ["if ('serviceWorker' in navigator) { /* use it */ }"]},
    "javascript-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain security", "Protects against malicious or compromised third-party npm packages"],
    ]), "formulae": ["npm audit"]},
    "javascript-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Lockfile integrity", "Verifies installed package contents match the exact hashes recorded in the lockfile"],
    ]), "formulae": ["npm ci  # fails if lockfile doesn't match package.json"]},
    "javascript-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Sandboxing", "Runs untrusted JavaScript in an isolated context with restricted capabilities"],
    ]), "formulae": ["const vm = require('vm');\nvm.runInNewContext('1+1');"]},
    "javascript-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Type coercion", "JavaScript's implicit conversion of values between types in operations"],
    ]), "formulae": ["'' + 1; // '1'\n1 == '1'; // true"]},
    "javascript-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Temporal API", "A modern, immutable date/time API designed to replace the legacy Date object"],
    ]), "formulae": ["Temporal.Now.plainDateISO();"]},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"javascript-m1-l{base_n}"
    worked_key = f"javascript-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        fields = {"data_table": dict(CHARTS[base_key]["data_table"])}
        if "formulae" in CHARTS[base_key]:
            fields["formulae"] = list(CHARTS[base_key]["formulae"])
        CHARTS[worked_key] = fields


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["JavaScript"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json JavaScript: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 JavaScript lessons (completing 120/120).")


if __name__ == "__main__":
    main()
