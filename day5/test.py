import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from day5.solutions import compute_intcode


def parse_instructions(instructions):
    return [int(x) for x in instructions.strip().split(",")]


class Day5(unittest.TestCase):
    def test_compute_intcode(self):
        self.assertEqual(0, compute_intcode(parse_instructions("3,9,8,9,10,9,4,9,99,-1,8"), 7))
        self.assertEqual(1, compute_intcode(parse_instructions("3,9,8,9,10,9,4,9,99,-1,8"), 8))
        self.assertEqual(0, compute_intcode(parse_instructions("3,9,8,9,10,9,4,9,99,-1,8"), 9))

        self.assertEqual(1, compute_intcode(parse_instructions("3,9,7,9,10,9,4,9,99,-1,8"), 7))
        self.assertEqual(0, compute_intcode(parse_instructions("3,9,7,9,10,9,4,9,99,-1,8"), 8))
        self.assertEqual(0, compute_intcode(parse_instructions("3,9,7,9,10,9,4,9,99,-1,8"), 9))

        self.assertEqual(0, compute_intcode(parse_instructions("3,3,1108,-1,8,3,4,3,99"), 7))
        self.assertEqual(1, compute_intcode(parse_instructions("3,3,1108,-1,8,3,4,3,99"), 8))
        self.assertEqual(0, compute_intcode(parse_instructions("3,3,1108,-1,8,3,4,3,99"), 9))

        self.assertEqual(1, compute_intcode(parse_instructions("3,3,1107,-1,8,3,4,3,99"), 7))
        self.assertEqual(0, compute_intcode(parse_instructions("3,3,1107,-1,8,3,4,3,99"), 8))
        self.assertEqual(0, compute_intcode(parse_instructions("3,3,1107,-1,8,3,4,3,99"), 9))

        self.assertEqual(0, compute_intcode(parse_instructions("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"), 0))
        self.assertEqual(1, compute_intcode(parse_instructions("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"), 1))
        self.assertEqual(1, compute_intcode(parse_instructions("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"), -1))
        self.assertEqual(1, compute_intcode(parse_instructions("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"), 12))

        self.assertEqual(0, compute_intcode(parse_instructions("3,3,1105,-1,9,1101,0,0,12,4,12,99,1"), 0))
        self.assertEqual(1, compute_intcode(parse_instructions("3,3,1105,-1,9,1101,0,0,12,4,12,99,1"), 1))
        self.assertEqual(1, compute_intcode(parse_instructions("3,3,1105,-1,9,1101,0,0,12,4,12,99,1"), -1))
        self.assertEqual(1, compute_intcode(parse_instructions("3,3,1105,-1,9,1101,0,0,12,4,12,99,1"), 12))

        self.assertEqual(999, compute_intcode(parse_instructions(
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,"
            "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,"
            "1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"), 7))
        self.assertEqual(1000, compute_intcode(parse_instructions(
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,"
            "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,"
            "1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"), 8))
        self.assertEqual(1001, compute_intcode(parse_instructions(
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,"
            "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,"
            "1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"), 9))


if __name__ == '__main__':
    unittest.main()
