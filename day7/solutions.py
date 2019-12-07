from itertools import permutations


def load_input():
    with open("day7/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


class Amplifier(object):
    def __init__(self, phase, program):
        self.phase = phase
        self.program = program.copy()
        self.position = 0
        self.has_already_used_phase = False
        self.has_reached_stop_opcode = False
        self.output = None

    def compute_intcode(self, input_integer):
        position = self.position
        program = self.program
        output = None
        while program[position] % 100 != 99:
            operation = program[position] % 100
            parameters = [int(x) for x in reversed(str(program[position] // 100).zfill(3))]
            if operation == 1:
                arguments = parse_n_arguments(program, position, parameters, 2)
                program[program[position + 3]] = arguments[0] + arguments[1]
                position += 4
            elif operation == 2:
                arguments = parse_n_arguments(program, position, parameters, 2)
                program[program[position + 3]] = arguments[0] * arguments[1]
                position += 4
            elif operation == 3:
                if self.has_already_used_phase:
                    program[program[position + 1]] = input_integer
                else:
                    program[program[position + 1]] = self.phase
                    self.has_already_used_phase = True
                position += 2
            elif operation == 4:
                output = parse_argument(program, position, parameters, 0)
                position += 2
                self.program = program
                self.position = position
                self.output = output
                return output
            elif operation == 5:
                arguments = parse_n_arguments(program, position, parameters, 2)
                if arguments[0] != 0:
                    position = arguments[1]
                else:
                    position += 3
            elif operation == 6:
                arguments = parse_n_arguments(program, position, parameters, 2)
                if arguments[0] == 0:
                    position = arguments[1]
                else:
                    position += 3
            elif operation == 7:
                arguments = parse_n_arguments(program, position, parameters, 2)
                program[program[position + 3]] = 1 if arguments[0] < arguments[1] else 0
                position += 4
            elif operation == 8:
                arguments = parse_n_arguments(program, position, parameters, 2)
                program[program[position + 3]] = 1 if arguments[0] == arguments[1] else 0
                position += 4
            else:
                print("Unsupported operation", operation)
                return
        self.has_reached_stop_opcode = True
        return output


def parse_argument(program, position, parameters, index):
    return program[program[position + index + 1]] if parameters[index] == 0 else program[position + index + 1]


def parse_n_arguments(program, position, parameters, n):
    return [parse_argument(program, position, parameters, index) for index in range(n)]


def amplify_signal_part1(program, phases, input_number):
    out = input_number
    for i in range(5):
        a = Amplifier(phases[i], program)
        out = a.compute_intcode(out)
    return out


def amplify_signal_part2(program, phases, input_number):
    a0 = Amplifier(phases[0], program)
    a1 = Amplifier(phases[1], program)
    a2 = Amplifier(phases[2], program)
    a3 = Amplifier(phases[3], program)
    a4 = Amplifier(phases[4], program)

    out = input_number
    while not a4.has_reached_stop_opcode:
        out = a0.compute_intcode(out)
        out = a1.compute_intcode(out)
        out = a2.compute_intcode(out)
        out = a3.compute_intcode(out)
        out = a4.compute_intcode(out)
    return a4.output


if __name__ == "__main__":
    program = load_input()

    print(max(amplify_signal_part1(program, permutation, 0) for permutation in permutations([0, 1, 2, 3, 4])))
    print(max(amplify_signal_part2(program, permutation, 0) for permutation in permutations([5, 6, 7, 8, 9])))
