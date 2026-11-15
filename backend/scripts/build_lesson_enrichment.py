#!/usr/bin/env python3
"""Build backend/data/lesson_enrichment/enrichment.json for Master's Year 1/2.

Every lesson gets its subject's reference pack (stored once) plus any topic
rules whose pattern matches the lesson title (rule ids stored per lesson).
Fails if a subject has no pack or a pack is thin, so coverage can't rot.

    python3 backend/scripts/build_lesson_enrichment.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(BACKEND / "scripts"))

from app.lesson_enrichment import topic_query  # noqa: E402
from enrich_data import PACKS, RULES  # noqa: E402

OUT = BACKEND / "data" / "lesson_enrichment" / "enrichment.json"
LEVELS = ("m1", "m2")


def validate_pack(name, pack):
    problems = []
    if len(pack["formulas"]) < 2:
        problems.append("needs at least 2 formulas/equations")
    if not pack["tables"] or any(len(r) != len(t["headers"]) for t in pack["tables"] for r in t["rows"]):
        problems.append("needs a table with consistent columns")
    if len(pack["cases"]) < 2:
        problems.append("needs at least 2 cases")
    for c in pack["cases"]:
        if not (c["title"] and c["when"] and c["summary"] and c["takeaway"] and c["wiki"]):
            problems.append(f"incomplete case {c['title']!r}")
    return [f"{name}: {p}" for p in problems]


def main():
    rules, compiled = {}, []
    for rule in RULES:
        if rule["id"] in rules:
            raise SystemExit(f"duplicate rule id {rule['id']}")
        rules[rule["id"]] = {k: v for k, v in rule.items() if k not in ("id", "pattern", "subjects") and v}
        compiled.append((rule["id"], re.compile(rule["pattern"], re.I), rule["subjects"]))

    lessons, subjects, problems = {}, set(), []
    for level in LEVELS:
        data = json.loads((BACKEND / "syllabus" / f"level_{level}.json").read_text(encoding="utf-8"))
        for subject, content in data["subjects"].items():
            subjects.add(subject)
            for lesson in content.get("lessons") or []:
                hits = [rid for rid, rx, subs in compiled
                        if (subs is None or subject in subs) and rx.search(lesson["title"])]
                entry = {"s": subject, "q": topic_query(lesson["title"])}
                if hits:
                    entry["r"] = hits
                lessons[lesson["id"]] = entry

    for name in sorted(subjects):
        if name not in PACKS:
            problems.append(f"{name}: no pack")
        else:
            problems += validate_pack(name, PACKS[name])
    for name in PACKS:
        if name not in subjects:
            problems.append(f"{name}: pack for unknown subject")
    used = {rid for e in lessons.values() for rid in e.get("r", [])}
    problems += [f"rule {rid} matches no lesson" for rid in rules if rid not in used]
    if problems:
        raise SystemExit("\n".join(problems))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"packs": PACKS, "rules": rules, "lessons": lessons},
                              ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")
    with_rule = sum(1 for e in lessons.values() if e.get("r"))
    print(f"{len(lessons)} lessons, {len(PACKS)} subject packs, {len(rules)} topic rules "
          f"({with_rule} lessons with topic-specific content), wrote {OUT.relative_to(BACKEND.parent)}")


if __name__ == "__main__":
    main()
