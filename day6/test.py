import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from day6.solutions import build_tree, compute_total_distance, compute_number_of_transfers


class Day6(unittest.TestCase):
    def test_build_tree(self):
        self.assertEqual(42, compute_total_distance(build_tree(test_cases["case1"])))
        self.assertEqual(54, compute_total_distance(build_tree(test_cases["case2"])))

    def test_compute_number_of_transfers(self):
        self.assertEqual(4, compute_number_of_transfers(build_tree(test_cases["case2"]), "YOU", "SAN"))


test_cases = {
    "case1": [
        ["COM", "B"],
        ["B", "C"],
        ["C", "D"],
        ["D", "E"],
        ["E", "F"],
        ["B", "G"],
        ["G", "H"],
        ["D", "I"],
        ["E", "J"],
        ["J", "K"],
        ["K", "L"],
    ],
    "case2": [
        ["COM", "B"],
        ["B", "C"],
        ["C", "D"],
        ["D", "E"],
        ["E", "F"],
        ["B", "G"],
        ["G", "H"],
        ["D", "I"],
        ["E", "J"],
        ["J", "K"],
        ["K", "L"],
        ["K", "YOU"],
        ["I", "SAN"],
    ]
}

if __name__ == '__main__':
    unittest.main()
