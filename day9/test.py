import unittest
from day9.solutions import compute_intcode


def parse_instructions(instructions):
    return [int(x) for x in instructions.strip().split(",")]


class Day5(unittest.TestCase):
    def test_compute_intcode(self):
        self.assertEqual([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99], compute_intcode(
            parse_instructions("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"), None))
        self.assertEqual(1219070632396864, compute_intcode(
            parse_instructions("1102,34915192,34915192,7,4,7,99,0"), 1)[-1])
        self.assertEqual(1125899906842624, compute_intcode(
            parse_instructions("104,1125899906842624,99"), 1)[-1])


if __name__ == '__main__':
    unittest.main()
