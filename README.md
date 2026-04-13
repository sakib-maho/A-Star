# A* Pathfinding Showcase

<!-- BrandCloud:readme-standard -->
[![Maintained](https://img.shields.io/badge/Maintained-yes-brightgreen.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Showcase](https://img.shields.io/badge/Portfolio-Showcase-blue.svg)](#)

_Part of the `sakib-maho` project showcase series with consistent documentation and quality standards._

Clean and reusable implementation of the A* shortest path algorithm with:

- reusable Python module
- CLI runner with JSON input
- unit tests
- Jupyter notebook demo

## Project Goals

This repository demonstrates algorithmic problem-solving and clean Python project structure using the A* search algorithm.

## Features

- Priority-queue based A* implementation (`astar/algorithm.py`)
- Input validation for missing nodes and heuristics
- CLI interface for running custom graph problems
- Sample graph file for quick execution
- Unit tests for core behavior and edge cases
- Notebook for interactive explanation and execution

## Project Structure

```text
.
├── astar/
│   ├── __init__.py
│   └── algorithm.py
├── data/
│   └── sample_graph.json
├── tests/
│   └── test_astar.py
├── A_star.ipynb
├── a_star.py
└── cli.py
```

## Quick Start

```bash
git clone https://github.com/sakib-maho/A-Star.git
cd A-Star
python3 -m venv .venv
source .venv/bin/activate
```

No third-party dependencies are required.

## Run from CLI

```bash
python cli.py --input data/sample_graph.json
```

Example output:

```text
Input file: data/sample_graph.json
Path: S -> A -> B -> C -> D
Cost: 8
```

Backward-compatible entrypoint:

```bash
python a_star.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Input JSON Format

```json
{
  "graph": {
    "S": { "A": 1, "B": 4 },
    "A": { "B": 2, "C": 5, "D": 12 },
    "B": { "C": 2 },
    "C": { "D": 3 },
    "D": {}
  },
  "heuristic": {
    "S": 7,
    "A": 6,
    "B": 2,
    "C": 1,
    "D": 0
  },
  "start": "S",
  "goal": "D"
}
```

## License

MIT License - see [LICENSE](LICENSE).
