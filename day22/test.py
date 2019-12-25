import unittest
from day22.solutions import Deck


class Day22(unittest.TestCase):
    def test_deal(self):
        deck = Deck(10)
        deck.deal()
        self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], deck.get_deck_state())

    def test_cut(self):
        deck = Deck(10)
        deck.cut(3)
        self.assertEqual([3, 4, 5, 6, 7, 8, 9, 0, 1, 2], deck.get_deck_state())

    def test_cut_negative(self):
        deck = Deck(10)
        deck.cut(-4)
        self.assertEqual([6, 7, 8, 9, 0, 1, 2, 3, 4, 5], deck.get_deck_state())

    def test_increment(self):
        deck = Deck(10)
        deck.deal_with_increment(3)
        self.assertEqual([0, 7, 4, 1, 8, 5, 2, 9, 6, 3], deck.get_deck_state())

        deck = Deck(10)
        deck.deal_with_increment(7)
        self.assertEqual([0, 3, 6, 9, 2, 5, 8, 1, 4, 7], deck.get_deck_state())

        deck = Deck(11)
        deck.deal_with_increment(3)
        self.assertEqual([0, 4, 8, 1, 5, 9, 2, 6, 10, 3, 7], deck.get_deck_state())

        deck = Deck(11)
        deck.deal_with_increment(7)
        self.assertEqual([0, 8, 5, 2, 10, 7, 4, 1, 9, 6, 3], deck.get_deck_state())

    def test_compute_deck_state(self):
        deck = Deck(10)
        deck.apply_instructions(test_cases[0])
        self.assertEqual([0, 3, 6, 9, 2, 5, 8, 1, 4, 7], deck.get_deck_state())

        deck = Deck(10)
        deck.apply_instructions(test_cases[1])
        self.assertEqual([3, 0, 7, 4, 1, 8, 5, 2, 9, 6], deck.get_deck_state())

        deck = Deck(10)
        deck.apply_instructions(test_cases[2])
        self.assertEqual([6, 3, 0, 7, 4, 1, 8, 5, 2, 9], deck.get_deck_state())

        deck = Deck(10)
        deck.apply_instructions(test_cases[3])
        self.assertEqual([9, 2, 5, 8, 1, 4, 7, 0, 3, 6], deck.get_deck_state())


test_cases = {
    0: """deal with increment 7
deal into new stack
deal into new stack""".split("\n"),
    1: """cut 6
deal with increment 7
deal into new stack""".split("\n"),
    2: """deal with increment 7
deal with increment 9
cut -2""".split("\n"),
    3: """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1""".split("\n"),
}

if __name__ == '__main__':
    unittest.main()
