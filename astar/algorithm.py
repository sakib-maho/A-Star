"""Reusable A* shortest path implementation."""

from __future__ import annotations

from heapq import heappop, heappush
from itertools import count
from math import inf
from typing import Dict, Iterable, List, Tuple

Graph = Dict[str, Dict[str, float]]
Heuristic = Dict[str, float]


def astar_shortest_path(
    graph: Graph,
    heuristic: Heuristic,
    start: str,
    goal: str,
) -> Tuple[List[str], float]:
    """Return the shortest path and cost from ``start`` to ``goal`` using A*.

    Raises:
        ValueError: If inputs are invalid or no path exists.
    """
    if start not in graph:
        raise ValueError(f"start node '{start}' is not present in graph")
    if goal not in graph:
        raise ValueError(f"goal node '{goal}' is not present in graph")

    for node in graph:
        if node not in heuristic:
            raise ValueError(f"heuristic value missing for node '{node}'")

    frontier: List[tuple[float, int, str, float]] = []
    seq = count()
    heappush(frontier, (heuristic[start], next(seq), start, 0.0))

    g_score: Dict[str, float] = {node: inf for node in graph}
    g_score[start] = 0.0
    came_from: Dict[str, str] = {}
    while frontier:
        _, _, current, current_cost = heappop(frontier)
        if current_cost > g_score[current]:
            continue

        if current == goal:
            path = _reconstruct_path(came_from, goal)
            return path, g_score[goal]

        for neighbor, weight in _neighbors(graph, current):
            tentative_cost = g_score[current] + float(weight)
            if tentative_cost < g_score.get(neighbor, inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_cost
                f_score = tentative_cost + float(heuristic.get(neighbor, inf))
                heappush(frontier, (f_score, next(seq), neighbor, tentative_cost))

    raise ValueError(f"no path found from '{start}' to '{goal}'")


def _neighbors(graph: Graph, node: str) -> Iterable[Tuple[str, float]]:
    return graph.get(node, {}).items()


def _reconstruct_path(came_from: Dict[str, str], goal: str) -> List[str]:
    path = [goal]
    current = goal
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
