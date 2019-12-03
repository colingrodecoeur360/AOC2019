import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from day3.solutions import compute_distance_of_closest_intersection, compute_minimum_total_steps_to_intersection


class Day3(unittest.TestCase):
    def test_compute_distance_of_closest_intersection(self):
        self.assertEqual(compute_distance_of_closest_intersection([
            "R8,U5,L5,D3".split(","),
            "U7,R6,D4,L4".split(",")]),
            6)
        self.assertEqual(compute_distance_of_closest_intersection([
            "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","),
            "U62,R66,U55,R34,D71,R55,D58,R83".split(",")]),
            159)
        self.assertEqual(compute_distance_of_closest_intersection([
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","),
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")]),
            135)

    def test_compute_minimum_total_steps_to_intersection(self):
        self.assertEqual(compute_minimum_total_steps_to_intersection([
            "R8,U5,L5,D3".split(","),
            "U7,R6,D4,L4".split(",")]),
            30)
        self.assertEqual(compute_minimum_total_steps_to_intersection([
            "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","),
            "U62,R66,U55,R34,D71,R55,D58,R83".split(",")]),
            610)
        self.assertEqual(compute_minimum_total_steps_to_intersection([
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","),
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")]),
            410)


if __name__ == '__main__':
    unittest.main()
