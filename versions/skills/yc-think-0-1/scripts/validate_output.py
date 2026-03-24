#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


TURN_MARKERS = [
    "适配判断",
    "当前步骤",
    "暂定理解",
    "请你回答",
]

FINAL_MARKERS = [
    "适配判断",
    "原始问题",
    "支撑层",
    "第 1 轮",
    "最终结果",
    "教练说明",
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
    turn_missing = [marker for marker in TURN_MARKERS if marker not in text]
    final_missing = [marker for marker in FINAL_MARKERS if marker not in text]

    if not turn_missing:
        print("Output looks like a valid interactive-turn response.")
        return 0

    if not final_missing:
        if "0.5Why" not in text:
            print("Output validation warning: no explicit 0.5Why record found in final output.")
            return 1
        print("Output looks like a valid final structured response.")
        return 0

    print("Output validation failed.")
    print("Missing turn markers:")
    for marker in turn_missing:
        print(f"- {marker}")
    print("Missing final markers:")
    for marker in final_missing:
        print(f"- {marker}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
