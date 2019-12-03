import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from day1.solutions import compute_fuel_part1, compute_fuel_part2


class Day1(unittest.TestCase):
    def test_compute_fuel_part1(self):
        self.assertEqual(compute_fuel_part1(12), 2)
        self.assertEqual(compute_fuel_part1(14), 2)
        self.assertEqual(compute_fuel_part1(1969), 654)
        self.assertEqual(compute_fuel_part1(100756), 33583)

    def test_compute_fuel_part2(self):
        self.assertEqual(compute_fuel_part2(12), 2)
        self.assertEqual(compute_fuel_part2(14), 2)
        self.assertEqual(compute_fuel_part2(1969), 966)
        self.assertEqual(compute_fuel_part2(100756), 50346)


if __name__ == '__main__':
    unittest.main()
