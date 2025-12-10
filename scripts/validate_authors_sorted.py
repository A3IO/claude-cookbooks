#!/usr/bin/env python3
"""Validate that authors.yaml keys are sorted alphabetically (case-insensitive)."""

import sys
from pathlib import Path

import yaml

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

AUTHORS_FILE = Path(__file__).parent.parent / "authors.yaml"


def main():
    """Check that authors.yaml is sorted alphabetically by username."""
    with open(AUTHORS_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not data:
        print("authors.yaml is empty")
        sys.exit(0)

    keys = list(data.keys())
    sorted_keys = sorted(keys, key=str.lower)

    if keys == sorted_keys:
        print("authors.yaml is sorted correctly")
        sys.exit(0)

    print("authors.yaml is not sorted alphabetically (case-insensitive).")
    print("\nCurrent order:")
    for k in keys:
        print(f"  {k}")

    print("\nExpected order:")
    for k in sorted_keys:
        print(f"  {k}")

    # Show which entries are out of place
    print("\nOut of place entries:")
    for i, (current, expected) in enumerate(zip(keys, sorted_keys)):
        if current != expected:
            print(f"  Position {i}: got '{current}', expected '{expected}'")

    sys.exit(1)


if __name__ == "__main__":
    main()
