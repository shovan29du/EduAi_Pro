#!/usr/bin/env python3
"""Write the authored `real_world` connection into every STEM Lab experiment.

Idempotent; fails if any experiment has no authored entry.

    python3 backend/scripts/apply_stem_real_world.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from stem_real_world_data import REAL_WORLD  # noqa: E402

PATH = Path(__file__).resolve().parent.parent / "data" / "stem_lab" / "stem_lab.json"


def main() -> None:
    raw = PATH.read_bytes()
    crlf = b"\r\n" in raw
    doc = json.loads(raw)
    seen = set()
    for discipline in doc["disciplines"].values():
        for exp in discipline["experiments"]:
            if exp["id"] not in REAL_WORLD:
                raise SystemExit(f"No real-world connection authored for {exp['id']}")
            exp["real_world"] = REAL_WORLD[exp["id"]]
            seen.add(exp["id"])
    unused = set(REAL_WORLD) - seen
    if unused:
        raise SystemExit(f"Entries with no matching experiment: {sorted(unused)}")
    text = json.dumps(doc, ensure_ascii=False, indent=2)
    if crlf:
        text = text.replace("\n", "\r\n")
    if raw.endswith(b"\n"):
        text += "\r\n" if crlf else "\n"
    PATH.write_bytes(text.encode("utf-8"))
    print(f"real_world set on {len(seen)} experiments")


if __name__ == "__main__":
    main()
