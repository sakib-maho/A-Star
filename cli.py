"""CLI for running A* pathfinding on a JSON graph file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

from astar import astar_shortest_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run A* shortest path search.")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/sample_graph.json"),
        help="Path to JSON file containing graph, heuristic, start, and goal.",
    )
    return parser.parse_args()


def load_problem(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"input file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    args = parse_args()
    problem = load_problem(args.input)

    path, cost = astar_shortest_path(
        graph=problem["graph"],
        heuristic=problem["heuristic"],
        start=problem["start"],
        goal=problem["goal"],
    )

    print(f"Input file: {args.input}")
    print("Path:", " -> ".join(path))
    print(f"Cost: {cost:g}")


if __name__ == "__main__":
    main()
