#!/usr/bin/env python3
"""Replace placeholder lesson examples with authored real-world cases.

Seven subject libraries (business, civics, critical thinking, environmental
science, health, world politics, world religions) shipped with ~1,050 lessons
whose `example` was one identical sentence ("A professional team applies <Topic>
to a real proposal..."), and 17 core topics with no example at all. This
rewrites them from real_world_case_data.py. Safe to re-run: only placeholders
and missing examples are touched.

    python3 backend/scripts/apply_real_world_examples.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import real_world_case_data as data  # noqa: E402

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
PLACEHOLDER = "A professional team applies"
FILES = {
    "business_studies": "business_studies/business_studies.json",
    "civics": "civics/civics.json",
    "critical_thinking": "critical_thinking/critical_thinking.json",
    "environmental_science": "environmental_science/environmental_science.json",
    "health_education": "health_education/health_education.json",
    "world_politics": "world_politics/world_politics.json",
    "world_religions": "world_religions/world_religions.json",
}


def lessons(node):
    if isinstance(node, dict):
        if "id" in node and "title" in node and ("content" in node or "explanation" in node or "example" in node):
            yield node
        for value in node.values():
            yield from lessons(value)
    elif isinstance(node, list):
        for item in node:
            yield from lessons(item)


def compose(case: str, angle: str, frame: str) -> str:
    return f"{case} For this lesson on {angle.lower()}: {frame[0].upper()}{frame[1:]}"


def main() -> None:
    for lib, rel in FILES.items():
        path = DATA_DIR / rel
        raw = path.read_bytes()
        crlf = b"\r\n" in raw
        doc = json.loads(raw)
        replaced = core = 0
        for lesson in lessons(doc):
            example = lesson.get("example") or ""
            if example.startswith(PLACEHOLDER):
                topic, _, angle = lesson["title"].partition(": ")
                if lib == "world_religions":
                    case = data.RELIGION_CASES[topic][data.RELIGION_ANGLE_CASE[angle]]
                    frame = data.RELIGION_FRAMES[angle]
                else:
                    case = data.CASES[lib][topic][data.GENERIC_ANGLE_CASE[angle]]
                    frame = data.GENERIC_FRAMES[angle]
                lesson["example"] = compose(case, angle, frame)
                replaced += 1
            elif not example and lesson["id"] in data.CORE_EXAMPLES:
                lesson["example"] = data.CORE_EXAMPLES[lesson["id"]]
                core += 1
        text = json.dumps(doc, ensure_ascii=False, indent=2)
        if crlf:
            text = text.replace("\n", "\r\n")
        path.write_bytes(text.encode("utf-8"))
        print(f"{lib:22s} placeholders replaced={replaced:4d} core examples added={core}")


if __name__ == "__main__":
    main()
