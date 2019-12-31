import unittest
from day16.solutions import fft, fft_n, decode_message


class Day16(unittest.TestCase):
    def test_fft(self):
        self.assertEqual([4, 8, 2, 2, 6, 1, 5, 8], fft([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertEqual([3, 4, 0, 4, 0, 4, 3, 8], fft_n([1, 2, 3, 4, 5, 6, 7, 8], 2))
        self.assertEqual([0, 3, 4, 1, 5, 5, 1, 8], fft_n([1, 2, 3, 4, 5, 6, 7, 8], 3))
        self.assertEqual([0, 1, 0, 2, 9, 4, 9, 8], fft_n([1, 2, 3, 4, 5, 6, 7, 8], 4))

        self.assertEqual([2, 4, 1, 7, 6, 1, 7, 6], fft_n(parse_input("80871224585914546619083218645595"), 100)[:8])
        self.assertEqual([7, 3, 7, 4, 5, 4, 1, 8], fft_n(parse_input("19617804207202209144916044189917"), 100)[:8])
        self.assertEqual([5, 2, 4, 3, 2, 1, 3, 3], fft_n(parse_input("69317163492948606335995924319873"), 100)[:8])

    def test_decode_message(self):
        self.assertEqual("84462026", decode_message(parse_input("03036732577212944063491565474664")))
        self.assertEqual("78725270", decode_message(parse_input("02935109699940807407585447034323")))
        self.assertEqual("53553731", decode_message(parse_input("03081770884921959731165446850517")))


def parse_input(s):
    return [int(x) for x in s]


if __name__ == '__main__':
    unittest.main()
