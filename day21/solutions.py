from intcode import Intcode


def load_input():
    with open("day21/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


def read_ascii_output(numbers):
    if numbers[-1] > 128:
        return numbers[-1]
    return "".join([chr(x) for x in numbers])


def build_ascii_input(instruction):
    return [ord(x) for x in instruction + "\n"]


def build_instructions_part1():
    # Jump if there is ground on D and a hole on either A, B or C
    return [
        "NOT J J",
        "AND A J",
        "AND B J",
        "AND C J",
        "NOT J J",
        "AND D J",
        "WALK"
    ]


def build_instructions_part2():
    return [
        # Jump if there is ground on D and a hole on either A, B or C, and if either E or H is ground
        # (Otherwise the springdroid would not be able to jump again after its first jump)
        "NOT J J",
        "AND A J",
        "AND B J",
        "AND C J",
        "NOT J J",
        "AND D J",
        "OR E T",
        "OR H T",
        "AND T J",
        "RUN"
    ]


if __name__ == "__main__":
    program = load_input()

    computer = Intcode(program)
    for instruction in build_instructions_part1():
        computer.add_inputs(build_ascii_input(instruction))
    computer.execute()
    print(read_ascii_output(computer.outputs))

    computer = Intcode(program)
    for instruction in build_instructions_part2():
        computer.add_inputs(build_ascii_input(instruction))
    computer.execute()
    print(read_ascii_output(computer.outputs))
