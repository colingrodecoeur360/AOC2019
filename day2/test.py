import unittest
from intcode import Intcode


class Day2(unittest.TestCase):
    def test_1(self):
        computer = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        computer.run()
        self.assertEqual(computer.program, [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])

    def test_2(self):
        computer = Intcode([1, 0, 0, 0, 99])
        computer.run()
        self.assertEqual(computer.program, [2, 0, 0, 0, 99])

    def test_3(self):
        computer = Intcode([2, 3, 0, 3, 99])
        computer.run()
        self.assertEqual(computer.program, [2, 3, 0, 6, 99])

    def test_4(self):
        computer = Intcode([2, 4, 4, 5, 99, 0])
        computer.run()
        self.assertEqual(computer.program, [2, 4, 4, 5, 99, 9801])

    def test_5(self):
        computer = Intcode([1, 1, 1, 4, 99, 5, 6, 0, 99])
        computer.run()
        self.assertEqual(computer.program, [30, 1, 1, 4, 2, 5, 6, 0, 99])


if __name__ == '__main__':
    unittest.main()
