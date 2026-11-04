#!/usr/bin/env python3
"""Run the three independent finite checks; optionally save fresh reports."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir", type=Path,
        help="Write new JSON reports here; committed reference reports are unchanged by default."
    )
    arguments = parser.parse_args()
    directory = Path(__file__).resolve().parent
    for name in ("relative_entropy", "counting", "extraction"):
        command = [sys.executable, str(directory / f"check_{name}.py")]
        if arguments.output_dir:
            command += ["--output", str(arguments.output_dir / f"{name}.json")]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode:
            print(result.stdout, end="")
            print(result.stderr, file=sys.stderr, end="")
            raise SystemExit(result.returncode)
        report = json.loads(result.stdout)
        if report.get("status") != "passed":
            raise RuntimeError(f"Check {name} did not report success.")
        print(f"PASS: {report['check']}")
    print("All finite checks passed. Analytical and infinite-volume claims require the written proofs.")


if __name__ == "__main__":
    main()
