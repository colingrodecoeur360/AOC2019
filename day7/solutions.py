from itertools import permutations
from intcode import Intcode


def load_input():
    with open("day7/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


class Amplifier(object):
    def __init__(self, program, phase):
        self.computer = Intcode(program, [phase])
        self.phase = phase


def amplify_signal_part1(program, phases, input_number):
    a0 = Amplifier(program, phases[0])
    a1 = Amplifier(program, phases[1])
    a2 = Amplifier(program, phases[2])
    a3 = Amplifier(program, phases[3])
    a4 = Amplifier(program, phases[4])

    a0.computer.add_input(input_number)
    out0 = a0.computer.run()

    a1.computer.add_input(out0)
    out1 = a1.computer.run()

    a2.computer.add_input(out1)
    out2 = a2.computer.run()

    a3.computer.add_input(out2)
    out3 = a3.computer.run()

    a4.computer.add_input(out3)
    out4 = a4.computer.run()

    return out4


def amplify_signal_part2(program, phases, input_number):
    a0 = Amplifier(program, phases[0])
    a1 = Amplifier(program, phases[1])
    a2 = Amplifier(program, phases[2])
    a3 = Amplifier(program, phases[3])
    a4 = Amplifier(program, phases[4])

    a0.computer.add_input(input_number)
    out0 = a0.computer.run()

    while not a0.computer.stopped:
        a1.computer.add_input(out0)
        out1 = a1.computer.run()

        a2.computer.add_input(out1)
        out2 = a2.computer.run()

        a3.computer.add_input(out2)
        out3 = a3.computer.run()

        a4.computer.add_input(out3)
        out4 = a4.computer.run()

        a0.computer.add_input(out4)
        out0 = a0.computer.run()

    return a4.computer.output


if __name__ == "__main__":
    program = load_input()

    print(max(amplify_signal_part1(program, permutation, 0) for permutation in permutations([0, 1, 2, 3, 4])))
    print(max(amplify_signal_part2(program, permutation, 0) for permutation in permutations([5, 6, 7, 8, 9])))
