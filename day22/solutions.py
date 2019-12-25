import math


def load_input():
    with open("day22/input.txt") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def compute_inverse(n, a):
    (r, u, r2, u2) = (a, 1, n, 0)
    while r2 != 0:
        q = r // r2
        (r, u, r2, u2) = (r2, u2, r - q * r2, u - q * u2)
    return u + n * math.ceil(-u / n)


def compute_power(root, exponent, n):
    binary_exponent = [int(x) for x in str(bin(exponent))[2:]]
    power = 1
    r = root
    for i, coefficient in enumerate(binary_exponent[::-1]):
        power *= r ** coefficient
        power = power % n
        r = (r ** 2) % n
    return power


class Deck(object):
    def __init__(self, number_of_cards):
        self.number_of_cards = number_of_cards
        self.shuffle = (1, 0)

    def get_card_position(self, x):
        a, b = self.shuffle
        return (a * x + b) % self.number_of_cards

    def get_deck_state(self):
        return [self.get_card_position(x) for x in range(self.number_of_cards)]

    def apply_shuffle(self, shuffle):
        a1, b1 = self.shuffle
        a2, b2 = shuffle
        a = a1 * a2 % self.number_of_cards
        b = (a1 * b2 + b1) % self.number_of_cards
        self.shuffle = (a, b)

    def deal(self):
        shuffle = (-1, self.number_of_cards - 1)
        self.apply_shuffle(shuffle)

    def cut(self, n):
        shuffle = (1, n)
        self.apply_shuffle(shuffle)

    def deal_with_increment(self, increment):
        shuffle = (compute_inverse(self.number_of_cards, increment), 0)
        self.apply_shuffle(shuffle)

    def apply_instructions(self, instructions):
        for instruction in instructions:
            words = instruction.split(" ")
            if " ".join(words[:-1]) == "deal with increment":
                self.deal_with_increment(int(words[-1]))
            elif instruction == "deal into new stack":
                self.deal()
            else:
                self.cut(int(words[-1]))

    def get_position_of_card(self, card):
        a, b = self.shuffle
        return compute_inverse(self.number_of_cards, a) * (card - b) % self.number_of_cards

    def get_card_at_position(self, position):
        a, b = self.shuffle
        return (a * position + b) % self.number_of_cards

    def apply_shuffle_repeatedly(self, n):
        a, b = self.shuffle
        if a == 1:
            self.shuffle = (1, (b * n) % self.number_of_cards)
        else:
            power = compute_power(a, n, self.number_of_cards)
            b = (compute_inverse(self.number_of_cards, a - 1) * (power - 1) * b) % self.number_of_cards
            a = power % self.number_of_cards
            self.shuffle = a, b


if __name__ == "__main__":
    instructions = load_input()

    deck = Deck(10007)
    deck.apply_instructions(instructions)
    print(deck.get_position_of_card(2019))

    deck = Deck(119315717514047)
    deck.apply_instructions(instructions)
    deck.apply_shuffle_repeatedly(101741582076661)
    print(deck.get_card_at_position(2020))
