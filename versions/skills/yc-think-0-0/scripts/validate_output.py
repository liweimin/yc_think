#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_MARKERS = [
    "Fit judgment",
    "Original problem",
    "Support layer",
    "Round 1",
    "Final result",
    "Coaching notes",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_output.py <markdown-file>")
        return 1

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 1

    text = path.read_text(encoding="utf-8")
    missing = [marker for marker in REQUIRED_MARKERS if marker not in text]

    if missing:
        print("Output validation failed.")
        print("Missing markers:")
        for marker in missing:
            print(f"- {marker}")
        return 1

    if "0.5Why" not in text:
        print("Output validation warning: no explicit 0.5Why record found.")
        return 1

    print("Output looks structurally complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
