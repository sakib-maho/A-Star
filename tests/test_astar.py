import unittest

from astar.algorithm import astar_shortest_path


class AStarTests(unittest.TestCase):
    def test_returns_expected_path_and_cost(self):
        graph = {
            "S": {"A": 1, "B": 4},
            "A": {"B": 2, "C": 5, "D": 12},
            "B": {"C": 2},
            "C": {"D": 3},
            "D": {},
        }
        heuristic = {"S": 7, "A": 6, "B": 2, "C": 1, "D": 0}

        path, cost = astar_shortest_path(graph, heuristic, "S", "D")

        self.assertEqual(path, ["S", "A", "B", "C", "D"])
        self.assertEqual(cost, 8)

    def test_raises_for_missing_start(self):
        graph = {"A": {"B": 1}, "B": {}}
        heuristic = {"A": 1, "B": 0}

        with self.assertRaises(ValueError):
            astar_shortest_path(graph, heuristic, "S", "B")

    def test_raises_when_no_path_exists(self):
        graph = {"S": {"A": 1}, "A": {}, "D": {}}
        heuristic = {"S": 1, "A": 1, "D": 0}

        with self.assertRaises(ValueError):
            astar_shortest_path(graph, heuristic, "S", "D")


if __name__ == "__main__":
    unittest.main()
