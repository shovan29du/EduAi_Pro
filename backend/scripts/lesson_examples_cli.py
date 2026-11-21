#!/usr/bin/env python3
"""Bulk-draft and review real-world lesson examples.

Drafts are written by the AI tutor (needs an Anthropic key saved in Settings
or ANTHROPIC_API_KEY) into data/lesson_examples_pending/. A person then
approves, edits or rejects each one; approved text lands in
data/lesson_examples_vetted/ (commit that directory) and is what students see.

    python3 backend/scripts/lesson_examples_cli.py status 5
    python3 backend/scripts/lesson_examples_cli.py generate 5 --subject Math --limit 50
    python3 backend/scripts/lesson_examples_cli.py review 5
"""
from __future__ import annotations

import argparse
import sys
import textwrap
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import lesson_examples as le  # noqa: E402


def cmd_status(args) -> int:
    vetted, pending = le._read(le.VETTED_DIR, args.level), le._read(le.PENDING_DIR, args.level)
    total = sum(1 for _ in le.iter_lessons(args.level, args.subject))
    print(f"level {args.level}: {total} lessons | {len(vetted)} vetted | {len(pending)} awaiting review")
    return 0


def cmd_generate(args) -> int:
    def progress(done, lesson):
        print(f"  [{done}] {lesson['id']}  {lesson['title']}", flush=True)
        time.sleep(args.delay)

    result = le.pregenerate(args.level, args.subject, args.limit, on_progress=progress)
    print(f"drafted {result['created']}, {result['remaining']} lessons still without an example")
    if result["unavailable"]:
        print("The AI tutor is unavailable (no API key?). Stopped early.")
        return 1
    return 0


def cmd_review(args) -> int:
    pending = le._read(le.PENDING_DIR, args.level)
    if not pending:
        print("Nothing awaiting review.")
        return 0
    for lesson_id, rec in sorted(pending.items(), key=lambda kv: kv[1].get("created_at", 0)):
        print("\n" + "=" * 78)
        print(f"{rec.get('subject', '')} | {rec.get('title', '')}  ({lesson_id})")
        flags = le.review_flags(rec["example"])
        if flags:
            print("CHECK: " + "; ".join(flags))
        print(textwrap.fill(rec["example"], 78))
        choice = input("[a]pprove  [e]dit  [r]eject  [s]kip  [q]uit > ").strip().lower()
        if choice == "q":
            break
        if choice == "a":
            _apply(args.level, lesson_id, "approve", "")
        elif choice == "e":
            new_text = input("New text > ").strip()
            if new_text:
                _apply(args.level, lesson_id, "approve", new_text)
        elif choice == "r":
            _apply(args.level, lesson_id, "reject", "")
    return 0


def _apply(level, lesson_id, action, text) -> None:
    from fastapi import HTTPException

    try:
        le.review_example(le.ReviewIn(level=level, lesson_id=lesson_id, action=action, example=text))
        print(f"  -> {action}d")
    except HTTPException as exc:
        print(f"  ! {exc.detail}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for name, fn in (("status", cmd_status), ("generate", cmd_generate), ("review", cmd_review)):
        p = sub.add_parser(name)
        p.add_argument("level", help="level id, e.g. 5, UG1, M2")
        p.add_argument("--subject", default="", help="limit to one subject")
        p.set_defaults(func=fn)
        if name == "generate":
            p.add_argument("--limit", type=int, default=25)
            p.add_argument("--delay", type=float, default=0.5, help="seconds between AI calls")
    args = parser.parse_args()
    try:
        return args.func(args)
    except FileNotFoundError as exc:
        print(f"No syllabus file: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
