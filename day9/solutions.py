from intcode import Intcode


def load_input():
    with open("day9/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


if __name__ == "__main__":
    program = load_input()

    computer = Intcode(program)
    computer.add_input(1)
    print(computer.execute())

    computer = Intcode(program)
    computer.add_input(2)
    print(computer.execute())
