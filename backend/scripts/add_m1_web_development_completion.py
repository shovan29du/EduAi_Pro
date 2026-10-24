#!/usr/bin/env python3
"""Depth pass, M1 Web Development: fill in real, hand-checked
data_table content for the 119 M1 Web Development lessons not
covered by the earlier breadth-first batch. Brings M1 Web
Development to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
production-scale frontend architecture, performance, protocols,
security, infrastructure, and DevOps for web platforms; l101-l120
are "Worked Analysis" companions reusing the data_table of l1-l20
(direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_web_development_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["React Hook/Tool", "Purpose"], [
    ["useMemo", "Memoizes a computed value"],
    ["useCallback", "Memoizes a function reference"],
    ["React.memo", "Prevents re-render if props are unchanged"],
])

CHARTS: dict[str, dict] = {
    "web-development-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Caching", "Stores computed results so repeated requests can be served faster"],
    ])},
    "web-development-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["QA testing", "Systematically verifies a web application behaves correctly before release"],
    ])},
    "web-development-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Streaming rendering", "Sends parts of a page to the browser as they become ready, rather than all at once"],
    ])},
    "web-development-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Signals/atoms", "Fine-grained reactive state primitives that update only the UI parts that depend on them"],
    ])},
    "web-development-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Micro-frontend", "Splits a large web app into independently deployable frontend modules"],
    ])},
    "web-development-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["GraphQL federation", "Composes multiple GraphQL services into a single unified API graph"],
    ])},
    "web-development-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Event-driven architecture", "Services communicate by publishing and reacting to events rather than direct calls"],
    ])},
    "web-development-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Distributed tracing", "Follows a single request's path across many services to diagnose latency and errors"],
    ])},
    "web-development-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Passkeys / WebAuthn", "Enables phishing-resistant authentication using public-key cryptography instead of passwords"],
    ])},
    "web-development-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Zero-downtime deployment", "Releases new code without interrupting live user traffic"],
    ])},
    "web-development-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Edge/CDN caching", "Serves cached content from servers geographically close to the user"],
    ])},
    "web-development-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Performance budget", "A defined limit on page weight or load time enforced during development"],
    ])},
    "web-development-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Accessibility engineering", "Builds interfaces usable by people relying on assistive technology"],
    ])},
    "web-development-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Headless CMS", "Manages content through an API, decoupled from how it is presented"],
    ])},
    "web-development-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["API gateway", "A single entry point that routes, authenticates, and rate-limits requests to backend services"],
    ])},
    "web-development-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Security auditing", "Systematically reviews a web application for vulnerabilities before or after release"],
    ])},
    "web-development-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Scalable database architecture", "Structures data storage to handle growing web application load"],
    ])},
    "web-development-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["DevOps for web teams", "Integrates development and operations practices to ship web software reliably"],
    ])},
    "web-development-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Production-grade platform", "Integrates frontend, backend, deployment, and monitoring into one working system"],
    ])},
    "web-development-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["WebAssembly", "Runs near-native-speed compiled code in the browser alongside JavaScript"],
    ])},
    "web-development-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Rust-to-Wasm compilation", "Compiles Rust code into WebAssembly for high-performance browser execution"],
    ])},
    "web-development-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Service worker", "A background script enabling offline caching and network interception for a web app"],
    ])},
    "web-development-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Background sync / push", "Lets a PWA defer network actions and receive notifications even when not open"],
    ])},
    "web-development-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Web worker", "Runs JavaScript on a separate thread to avoid blocking the main UI thread"],
    ])},
    "web-development-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Module federation", "Lets independently built micro-frontends share code at runtime"],
    ])},
    "web-development-m1-l27": {"data_table": table(["Approach", "Feature"], [
        ["Hydration", "Re-attaches interactivity to server-rendered HTML by re-running app code"],
        ["Resumability", "Serializes app state so the client resumes without re-executing all initialization"],
    ])},
    "web-development-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Server-side rendering", "Renders a page's HTML on the server before sending it to the browser"],
    ])},
    "web-development-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Edge functions", "Run application logic on servers close to the user rather than a central data center"],
    ])},
    "web-development-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["WebSockets at scale", "Maintains many concurrent persistent connections for real-time bidirectional communication"],
    ])},
    "web-development-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["WebRTC", "Enables direct peer-to-peer audio, video, and data communication in the browser"],
    ])},
    "web-development-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["HTTP/3 / QUIC", "A transport protocol built on UDP that reduces latency and connection setup overhead"],
    ])},
    "web-development-m1-l33": {"data_table": table(["Header", "Purpose"], [
        ["Cache-Control", "Directs how and for how long a response may be cached"],
    ])},
    "web-development-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Content Security Policy", "Restricts which sources of scripts and content a page is allowed to load"],
    ])},
    "web-development-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Subresource integrity", "Verifies that a fetched script or asset hasn't been tampered with, via a hash"],
    ])},
    "web-development-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["CORS", "Controls which other origins are allowed to make requests to a web resource"],
    ])},
    "web-development-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["OAuth 2.1 / OIDC", "Standard protocols for delegated authorization and identity verification"],
    ])},
    "web-development-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Zero-trust architecture", "Verifies every request regardless of network origin instead of trusting an internal perimeter"],
    ])},
    "web-development-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Rate limiting / DDoS mitigation", "Restricts request volume to protect a service from abuse or overload"],
    ])},
    "web-development-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Pub/sub WebSocket infrastructure", "Broadcasts real-time messages to many subscribed clients at scale"],
    ])},
    "web-development-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Database sharding", "Splits a database horizontally across multiple servers to scale writes and storage"],
    ])},
    "web-development-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Read replica", "A copy of a database used to serve read traffic and reduce load on the primary"],
    ])},
    "web-development-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Cache stampede", "Many requests simultaneously recompute an expired cache entry, overloading the backend"],
    ])},
    "web-development-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["CDN", "A distributed network of servers that caches and delivers content close to users"],
    ])},
    "web-development-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Responsive image delivery", "Serves appropriately sized images per device to reduce load time"],
    ])},
    "web-development-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Font loading strategy", "Controls how and when custom fonts appear to avoid layout shift and blocked rendering"],
    ])},
    "web-development-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Critical rendering path", "The sequence of steps a browser takes to convert HTML/CSS/JS into pixels on screen"],
    ])},
    "web-development-m1-l48": {"data_table": table(["Metric", "Measures"], [
        ["Core Web Vitals (LCP, INP, CLS)", "Real-world loading, interactivity, and visual stability performance"],
    ])},
    "web-development-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Custom performance dashboard", "Visualizes collected performance metrics for a team to monitor over time"],
    ])},
    "web-development-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Real user monitoring", "Collects performance data from actual visitors' browsers in production"],
    ])},
    "web-development-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic monitoring", "Simulates user visits from controlled locations to proactively check site health"],
    ])},
    "web-development-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Feature flag", "Toggles a feature on or off without redeploying code"],
    ])},
    "web-development-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Canary deployment", "Rolls out a new version to a small subset of users before a full release"],
    ])},
    "web-development-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Blue-green deployment", "Switches traffic between two identical environments to enable instant rollback"],
    ])},
    "web-development-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["CI/CD pipeline", "Automates building, testing, and deploying code changes"],
    ])},
    "web-development-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Infrastructure as code", "Defines and provisions infrastructure using version-controlled configuration files"],
    ])},
    "web-development-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Container orchestration", "Automates deployment, scaling, and management of containerized applications"],
    ])},
    "web-development-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Serverless architecture", "Runs backend code in managed functions that scale automatically without server management"],
    ])},
    "web-development-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tenant SaaS", "Serves multiple customers from one shared application instance with isolated data"],
    ])},
    "web-development-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Zero-downtime migration", "Changes a database schema without interrupting live application traffic"],
    ])},
    "web-development-m1-l61": {"data_table": table(["Approach", "Feature"], [
        ["Event sourcing", "Stores state as a sequence of events rather than the current value alone"],
        ["CQRS", "Separates the models used for writing data from those used for reading it"],
    ])},
    "web-development-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Message queue (Kafka/RabbitMQ)", "Decouples services by passing messages asynchronously between them"],
    ])},
    "web-development-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["API versioning", "Manages backward-compatible evolution of a long-lived web API"],
    ])},
    "web-development-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["HATEOAS", "Embeds links in API responses so clients can discover available actions dynamically"],
    ])},
    "web-development-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["GraphQL schema design", "Structures types and relationships for maintainability at large scale"],
    ])},
    "web-development-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Query complexity analysis", "Limits or costs GraphQL queries to prevent excessively expensive requests"],
    ])},
    "web-development-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["tRPC", "Provides end-to-end type-safe APIs between a TypeScript frontend and backend"],
    ])},
    "web-development-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["TypeScript patterns at scale", "Uses advanced typing techniques to keep large codebases safe and maintainable"],
    ])},
    "web-development-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Monorepo build system", "Manages multiple related packages in one repository with shared, cached builds"],
    ])},
    "web-development-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Contract testing", "Verifies that a service and its consumers agree on the API's expected behavior"],
    ])},
    "web-development-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Visual regression testing", "Detects unintended UI changes by comparing rendered screenshots over time"],
    ])},
    "web-development-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["E2E testing at scale", "Runs full browser-based tests reliably across a large application and test suite"],
    ])},
    "web-development-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Load testing", "Simulates high traffic to measure how a system performs under stress"],
    ])},
    "web-development-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Active-active architecture", "Runs multiple regions simultaneously serving live traffic for resilience"],
    ])},
    "web-development-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Distributed session management", "Keeps user session state consistent across multiple servers"],
    ])},
    "web-development-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Web application firewall", "Filters and blocks malicious HTTP traffic before it reaches an application"],
    ])},
    "web-development-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Bot detection", "Distinguishes automated traffic from genuine human users"],
    ])},
    "web-development-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Secure file upload", "Validates and isolates user-uploaded files to prevent malicious payloads"],
    ])},
    "web-development-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Internationalization architecture", "Structures an app to support multiple languages and locales"],
    ])},
    "web-development-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["RTL layout engineering", "Adapts a web interface's layout for right-to-left reading languages"],
    ])},
    "web-development-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Accessibility testing automation", "Runs automated checks against accessibility standards as part of CI"],
    ])},
    "web-development-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Design system component library", "A shared, reusable set of UI components used consistently across an organization"],
    ])},
    "web-development-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Container queries / cascade layers", "Modern CSS features enabling component-based responsive styling with clear precedence"],
    ])},
    "web-development-m1-l84": {"data_table": table(["Approach", "Trade-off"], [
        ["CSS-in-JS", "Colocates styles with components but can add runtime overhead"],
    ])},
    "web-development-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Animation performance", "Uses GPU-accelerated properties to keep animations smooth in the browser"],
    ])},
    "web-development-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Shadow DOM", "Encapsulates a web component's markup and styles from the rest of the page"],
    ])},
    "web-development-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Browser rendering engine internals", "How a browser parses, lays out, paints, and composites a page"],
    ])},
    "web-development-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Memory leak debugging", "Finds and fixes objects that are never released, causing a page to slow over time"],
    ])},
    "web-development-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["V8 internals", "Understanding the JavaScript engine's compilation and optimization pipeline"],
    ])},
    "web-development-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Custom bundler", "Builds tooling that packages application code and assets for deployment"],
    ])},
    "web-development-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Tree shaking", "Removes unused code from a bundle during the build process"],
    ])},
    "web-development-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Dependency graph optimization", "Analyzes module relationships to reduce bundle size and build time"],
    ])},
    "web-development-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Headless e-commerce", "Decouples the storefront frontend from the commerce backend via APIs"],
    ])},
    "web-development-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Payment gateway integration", "Connects a web app securely to a payment processor for transactions"],
    ])},
    "web-development-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["GDPR/CCPA compliance architecture", "Designs data handling to meet legal privacy requirements"],
    ])},
    "web-development-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Web3/blockchain integration", "Connects a web app to decentralized wallets and smart contracts"],
    ])},
    "web-development-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Streaming LLM UI", "Displays AI-generated text incrementally as it is produced, rather than all at once"],
    ])},
    "web-development-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Site reliability engineering", "Applies software engineering practices to keep a web platform reliable at scale"],
    ])},
    "web-development-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["CRDT sync engine", "Merges offline edits from multiple clients automatically without conflicts"],
    ])},
    "web-development-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["WebGPU", "A modern browser API for high-performance GPU-accelerated graphics and computation"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"web-development-m1-l{base_n}"
    worked_key = f"web-development-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Web Development"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Web Development: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Web Development lessons (completing 120/120).")


if __name__ == "__main__":
    main()
