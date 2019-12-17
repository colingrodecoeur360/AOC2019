import unittest
from day4.solutions import meets_condition_part_1, meets_condition_part_2, has_isolated_zero


class Day4(unittest.TestCase):
    def test_meets_condition_part_1(self):
        self.assertEqual(meets_condition_part_1(111111), True)
        self.assertEqual(meets_condition_part_1(223450), False)
        self.assertEqual(meets_condition_part_1(123789), False)

    def test_meets_condition_part_2(self):
        self.assertEqual(meets_condition_part_2(112233), True)
        self.assertEqual(meets_condition_part_2(123444), False)
        self.assertEqual(meets_condition_part_2(111122), True)
        self.assertEqual(meets_condition_part_2(111111), False)
        self.assertEqual(meets_condition_part_2(110001), False)

    def test_has_isolated_zero(self):
        self.assertEqual(has_isolated_zero([0, 1, 0, 1, 0]), True)
        self.assertEqual(has_isolated_zero([0, 1, 1, 1, 1]), True)
        self.assertEqual(has_isolated_zero([1, 1, 1, 1, 0]), True)
        self.assertEqual(has_isolated_zero([1, 1, 0, 1, 1]), True)


if __name__ == '__main__':
    unittest.main()
