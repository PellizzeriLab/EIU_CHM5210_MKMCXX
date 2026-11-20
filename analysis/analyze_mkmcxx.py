#!/usr/bin/env python3
"""Summarize a CSV trajectory produced by mkmcxx."""

import argparse
import csv
import json
from pathlib import Path


def summarize(path):
    with Path(path).open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError("trajectory contains no observations")
    species = [name for name in rows[0] if name != "time"]
    return {
        "observations": len(rows),
        "events": len(rows) - 1,
        "final_time": float(rows[-1]["time"]),
        "final_counts": {name: int(float(rows[-1][name])) for name in species},
        "mean_counts": {
            name: sum(float(row[name]) for row in rows) / len(rows)
            for name in species
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trajectory", type=Path)
    parser.add_argument("-o", "--output", type=Path, help="write JSON instead of stdout")
    args = parser.parse_args()
    result = json.dumps(summarize(args.trajectory), indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(result + "\n")
    else:
        print(result)


if __name__ == "__main__":
    main()
