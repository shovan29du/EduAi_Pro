"""Replace resource URLs confirmed broken by the live link audit."""

from __future__ import annotations

import json
from pathlib import Path

SYLLABUS_DIR = Path(__file__).resolve().parents[1] / "syllabus"

REPLACEMENTS = {
    "https://code.org/courses": "https://studio.code.org/catalog",
    "https://kids.nationalgeographic.com/geography/article/continents": "https://education.nationalgeographic.org/resource/continent/",
    "https://education.nationalgeographic.org/resource/continent/": "https://education.nationalgeographic.org/resource/Continent/",
    "https://kids.nationalgeographic.com/geography/article/plate-tectonics": "https://education.nationalgeographic.org/resource/plate-tectonics/",
    "https://www.bbc.co.uk/bitesize/math/cc-sixth-grade-math/cc-6th-negative-number-topic": "https://downloads.bbc.co.uk/skillswise/maths/ma05nega/factsheet/ma05nega-e3-f-what-are-negative-numbers.pdf",
    "https://www.bbc.co.uk/bitesize/math/cc-kindergarten-math/cc-kindergarten-counting-10": "https://www.khanacademy.org/math/cc-kindergarten-math/cc-kindergarten-counting",
    "https://www.bbc.co.uk/bitesize/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic": "https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic",
    "https://www.bbc.co.uk/bitesize/math/cc-fourth-grade-math/cc-4th-div": "https://www.khanacademy.org/math/cc-fourth-grade-math/division",
    "https://www.bbc.co.uk/bitesize/examspecs/z8xgm34": "https://www.bbc.co.uk/bitesize/subjects/zr9d7ty",
    "https://www.bbc.co.uk/bitesize/science/ap-physics-1": "https://www.khanacademy.org/science/ap-college-physics-1",
    "https://www.bbc.co.uk/bitesize/math/algebra-basics": "https://www.khanacademy.org/math/algebra-basics",
    "https://spaceplace.nasa.gov/water-cycle/": "https://gpm.nasa.gov/education/lesson-plans/water-cycle",
    "https://www.bbc.co.uk/bitesize/college-careers-more/personal-finance": "https://www.khanacademy.org/college-careers-more/financial-literacy",
    "https://www.bbc.co.uk/bitesize/computing/computer-programming": "https://www.khanacademy.org/computing/computer-programming",
    "https://www.bbc.co.uk/bitesize/economics-finance-domain": "https://www.khanacademy.org/economics-finance-domain",
    "https://www.bbc.co.uk/bitesize/economics-finance-domain/ap-macroeconomics": "https://www.khanacademy.org/economics-finance-domain/ap-macroeconomics",
    "https://www.bbc.co.uk/bitesize/economics-finance-domain/ap-microeconomics": "https://www.khanacademy.org/economics-finance-domain/ap-microeconomics",
    "https://www.bbc.co.uk/bitesize/economics-finance-domain/macroeconomics": "https://www.khanacademy.org/economics-finance-domain/macroeconomics",
    "https://www.bbc.co.uk/bitesize/economics-finance-domain/microeconomics": "https://www.khanacademy.org/economics-finance-domain/microeconomics",
    "https://www.bbc.co.uk/bitesize/humanities/ap-us-government-and-politics": "https://www.khanacademy.org/humanities/ap-us-government-and-politics",
    "https://www.bbc.co.uk/bitesize/humanities/art-history": "https://www.khanacademy.org/humanities/art-history",
    "https://www.bbc.co.uk/bitesize/humanities/geography": "https://education.nationalgeographic.org/",
    "https://www.bbc.co.uk/bitesize/humanities/music": "https://www.classicsforkids.com/",
    "https://www.bbc.co.uk/bitesize/humanities/us-government-and-civics": "https://www.khanacademy.org/humanities/us-government-and-civics",
    "https://www.bbc.co.uk/bitesize/humanities/world-history": "https://www.khanacademy.org/humanities/world-history",
    "https://www.bbc.co.uk/bitesize/humanities/world-history-project-ap": "https://www.khanacademy.org/humanities/whp-ap",
    "https://www.bbc.co.uk/bitesize/math/algebra": "https://www.khanacademy.org/math/algebra",
    "https://www.bbc.co.uk/bitesize/math/algebra2": "https://www.khanacademy.org/math/algebra2",
    "https://www.bbc.co.uk/bitesize/math/cc-2nd-grade-math/cc-2nd-add-subtract-200": "https://www.khanacademy.org/math/cc-2nd-grade-math/add-and-subtract-within-20",
    "https://www.bbc.co.uk/bitesize/math/cc-fifth-grade-math/cc-5th-fractions-topic": "https://www.khanacademy.org/math/cc-fifth-grade-math/imp-fractions-3",
    "https://www.bbc.co.uk/bitesize/math/cc-fifth-grade-math/cc-5th-volume": "https://www.khanacademy.org/math/cc-fifth-grade-math/5th-volume",
    "https://www.bbc.co.uk/bitesize/math/cc-third-grade-math/cc-3rd-mult-div-topic": "https://www.khanacademy.org/math/cc-third-grade-math/intro-to-multiplication",
    "https://www.bbc.co.uk/bitesize/math/geometry": "https://www.khanacademy.org/math/geometry",
    "https://www.bbc.co.uk/bitesize/math/pre-algebra": "https://www.khanacademy.org/math/pre-algebra",
    "https://www.bbc.co.uk/bitesize/math/precalculus": "https://www.khanacademy.org/math/precalculus",
    "https://www.bbc.co.uk/bitesize/science/biology": "https://www.khanacademy.org/science/high-school-biology",
    "https://www.bbc.co.uk/bitesize/science/chemistry": "https://www.khanacademy.org/science/hs-chemistry",
    "https://www.bbc.co.uk/bitesize/science/physics": "https://www.khanacademy.org/science/highschool-physics",
    "https://www.bbc.co.uk/bitesize/subjects/z33rkqt": "https://www.khanacademy.org/science/hs-chemistry",
    "https://www.bbc.co.uk/bitesize/subjects/z3kbgwx": "https://www.khanacademy.org/science/high-school-biology",
    "https://www.bbc.co.uk/bitesize/subjects/z6srwmn": "https://www.khanacademy.org/science",
    "https://www.bbc.co.uk/bitesize/subjects/zhg9q6f": "https://www.tate.org.uk/kids",
    "https://www.bbc.co.uk/bitesize/subjects/zinhfg8": "https://www.open.edu/openlearn/history-the-arts/religious-studies",
    "https://www.bbc.co.uk/bitesize/subjects/zvr9wmn": "https://www.khanacademy.org/humanities/grammar",
    "https://www.bbc.co.uk/bitesize/topics/zb48q6f": "https://quran.com/",
    "https://www.bbc.co.uk/bitesize/topics/zd17xfr": "https://www.khanacademy.org/humanities/grammar",
    "https://www.bbc.co.uk/bitesize/topics/zd4cwmn": "https://www.khanacademy.org/humanities/grammar",
    "https://www.math-salamanders.com/fraction-chart.html": "https://www.math-salamanders.com/comparing-fractions-worksheet.html",
    "https://www.math-salamanders.com/order-of-operations-worksheets.html": "https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-arithmetic-operations",
    "https://www.math-salamanders.com/ratio-and-proportion-worksheets.html": "https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic",
}


def replace(value, counts: dict[str, int]):
    if isinstance(value, dict):
        return {key: replace(child, counts) for key, child in value.items()}
    if isinstance(value, list):
        return [replace(child, counts) for child in value]
    if isinstance(value, str):
        for old, new in REPLACEMENTS.items():
            occurrences = value.count(old)
            if occurrences:
                counts[old] += occurrences
                value = value.replace(old, new)
    return value


def main() -> None:
    counts = {url: 0 for url in REPLACEMENTS}
    changed_files = 0
    for path in sorted(SYLLABUS_DIR.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        updated = replace(payload, counts)
        if updated != payload:
            path.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed_files += 1
    print(f"Updated {sum(counts.values())} occurrences across {changed_files} files")
    for old, count in counts.items():
        print(f"{count:4}  {old} -> {REPLACEMENTS[old]}")


if __name__ == "__main__":
    main()
