import unittest
from intcode import Intcode


class Day9(unittest.TestCase):
    def test_compute_intcode(self):
        computer = Intcode([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99])
        computer.execute()
        self.assertEqual([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99], computer.outputs)

        computer = Intcode([1102, 34915192, 34915192, 7, 4, 7, 99, 0])
        computer.add_input(1)
        output = computer.execute()
        self.assertEqual(1219070632396864, output)

        computer = Intcode([104, 1125899906842624, 99])
        computer.add_input(1)
        output = computer.execute()
        self.assertEqual(1125899906842624, output)


if __name__ == '__main__':
    unittest.main()
