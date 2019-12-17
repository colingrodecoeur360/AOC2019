import unittest


class Instruction(object):
    number_of_arguments = 0

    def execute(self, intcode, arguments):
        pass

    def update_position(self, intcode):
        intcode.position = intcode.position + self.number_of_arguments + 1


class AddInstruction(Instruction):
    number_of_arguments = 3

    def execute(self, intcode, arguments):
        intcode.set(arguments[2].position, arguments[0].value + arguments[1].value)
        self.update_position(intcode)


class MultiplyInstruction(Instruction):
    number_of_arguments = 3

    def execute(self, intcode, arguments):
        intcode.set(arguments[2].position, arguments[0].value * arguments[1].value)
        self.update_position(intcode)


class StopInstruction(Instruction):
    number_of_arguments = 0

    def execute(self, intcode, arguments):
        intcode.stopped = True


instructions = {
    1: AddInstruction,
    2: MultiplyInstruction,
    99: StopInstruction
}


class Argument(object):
    def __init__(self, position, value):
        self.position = position
        self.value = value


class Intcode(object):
    def __init__(self, program):
        self.program = program
        self.stopped = False
        self.output = None
        self.position = 0

    def get_arguments(self, number_of_arguments):
        arguments = []
        for i in range(number_of_arguments):
            position = self.program[self.position + i + 1]
            arguments.append(Argument(position=position, value=self.program[position]))
        return arguments

    def run(self):
        while not self.stopped:
            opcode = self.program[self.position] % 100
            instruction = instructions[opcode]()
            arguments = self.get_arguments(instruction.number_of_arguments)
            instruction.execute(self, arguments)

    def set(self, position, value):
        self.program[position] = value


if __name__ == "__main__":
    unittest.main()