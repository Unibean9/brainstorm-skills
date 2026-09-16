"""Validate recorded live runs against the English golden data."""

from pathlib import Path
import re
import sys

import yaml


ROOT = Path(__file__).resolve().parent
DATA = yaml.safe_load((ROOT / "golden-data.yaml").read_text(encoding="utf-8"))


def output_list(value):
    return value if isinstance(value, list) else [value]


def check_case(case):
    run_dir = ROOT / "runs" / case["id"]
    expected_entry = next(item for item in case["expected"] if "output" in item)
    expected = output_list(expected_entry["output"])
    failures = []

    if not run_dir.is_dir():
        return [f"missing run directory: {run_dir}"]

    if len(case["turns"]) != 19:
        failures.append(f"golden turns={len(case['turns'])}, expected 19")

    transcript = run_dir / "transcript.md"
    numbered_turns = re.findall(r"^\s*\d+\.\s+", transcript.read_text(encoding="utf-8"), re.MULTILINE) if transcript.exists() else []
    if len(numbered_turns) != 19:
        failures.append(f"recorded turns={len(numbered_turns)}, expected 19")

    prd = run_dir / "prd.md"
    prd_text = prd.read_text(encoding="utf-8").lower() if prd.exists() else ""
    if not prd_text:
        failures.append("missing prd.md")
    if "status: final" not in prd_text:
        failures.append("PRD is not marked status: final")
    required_prd_signals = [
        "executive", "problem", "target", "job", "glossary", "journey",
        "solution", "feature", "functional requirement", "non-functional",
        "scope", "success", "risk", "open", "assumption", "acceptance",
    ]
    for signal in required_prd_signals:
        if signal not in prd_text:
            failures.append(f"PRD missing signal: {signal}")

    html_files = sorted(run_dir.rglob("*.html"))
    actual_names = {path.relative_to(run_dir).as_posix() for path in html_files}
    expected_names = set(expected)
    if actual_names != expected_names:
        failures.append(f"HTML outputs={sorted(actual_names)}, expected={sorted(expected_names)}")

    if "landing-page.html" in expected_names:
        landing = run_dir / "landing-page.html"
        landing_text = landing.read_text(encoding="utf-8").lower() if landing.exists() else ""
        for signal in ("<!doctype html>", "<style", "<body"):
            if signal not in landing_text:
                failures.append(f"landing page missing {signal}")
        section_count = len(re.findall(r"<section\b", landing_text))
        if section_count < 6:
            failures.append(f"landing sections={section_count}, minimum=6")
        for signal in (":focus-visible", "prefers-reduced-motion", "@media", "--"):
            if signal not in landing_text:
                failures.append(f"landing page missing UI signal: {signal}")
        if not re.search(r"(diagram|journey|mechanism|how it works|how-it-works|step|trace|signal)", landing_text):
            failures.append("landing page missing a product-specific visual/mechanism signal")

    if "deck.html" in expected_names:
        deck = run_dir / "deck.html"
        deck_text = deck.read_text(encoding="utf-8") if deck.exists() else ""
        slides = len(re.findall(r'<section class="(?:slide|s)"', deck_text))
        if slides < 10:
            failures.append(f"deck slides={slides}, minimum=10")
        notes = len(re.findall(r"(class=\"notes\"|speaker note|speaker-note|data-notes)", deck_text, re.IGNORECASE))
        if notes < 4:
            failures.append(f"deck speaker notes={notes}, minimum=4")
        if "@media print" not in deck_text:
            failures.append("deck missing print/PDF styles")
        visual_modes = sum(bool(re.search(pattern, deck_text, re.IGNORECASE)) for pattern in ("grid", "diagram", "timeline", "table", "chart", "flow", "svg"))
        if visual_modes < 4:
            failures.append(f"deck visual modes={visual_modes}, minimum=4")

    return failures


def main():
    failures = []
    if DATA.get("language") != "en":
        failures.append("golden data language is not en")

    print(f"Golden: {DATA['name']} | language={DATA['language']}")
    for case in DATA["cases"]:
        case_failures = check_case(case)
        if case_failures:
            failures.extend(f"{case['id']}: {item}" for item in case_failures)
            print(f"FAIL  {case['id']}")
            for item in case_failures:
                print(f"      - {item}")
        else:
            expected_entry = next(item for item in case["expected"] if "output" in item)
            print(f"PASS  {case['id']} | 19 turns | PRD | {', '.join(output_list(expected_entry['output']))}")

    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print(f"\nPASS  {len(DATA['cases'])} cases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
