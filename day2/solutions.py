from intcode import Intcode


def load_input():
    with open("day2/input.txt") as f:
        content = f.read()
    return [int(x) for x in content.split(",")]


def compute_intcode_result(program, noun, verb):
    program_copy = program.copy()
    program_copy[1] = noun
    program_copy[2] = verb
    computer = Intcode(program_copy)
    computer.run()
    return computer.program[0]


def compute_noun_and_verb(program, output):
    for noun in range(100):
        for verb in range(100):
            if compute_intcode_result(program, noun, verb) == output:
                return 100 * noun + verb


if __name__ == "__main__":
    program = load_input()

    print(compute_intcode_result(program, 12, 2))
    print(compute_noun_and_verb(program, 19690720))
