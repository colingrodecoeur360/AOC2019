class Instruction(object):
    number_of_arguments = 0

    def execute(self, intcode, arguments):
        pass


class AddInstruction(Instruction):
    number_of_arguments = 3

    def execute(self, intcode, arguments):
        intcode.set(arguments[2].position, arguments[0].value + arguments[1].value)
        intcode.update_position(intcode.position + self.number_of_arguments + 1)


class MultiplyInstruction(Instruction):
    number_of_arguments = 3

    def execute(self, intcode, arguments):
        intcode.set(arguments[2].position, arguments[0].value * arguments[1].value)
        intcode.update_position(intcode.position + self.number_of_arguments + 1)


class InputInstruction(Instruction):
    number_of_arguments = 1

    def execute(self, intcode, arguments):
        intcode.set(arguments[0].position, intcode.get_input())
        intcode.update_position(intcode.position + self.number_of_arguments + 1)


class OutputInstruction(Instruction):
    number_of_arguments = 1

    def execute(self, intcode, arguments):
        intcode.output = arguments[0].value
        intcode.update_position(intcode.position + self.number_of_arguments + 1)


class JumpIfTrueInstruction(Instruction):
    number_of_arguments = 2

    def execute(self, intcode, arguments):
        new_position = intcode.position + self.number_of_arguments + 1 if arguments[0].value == 0 else arguments[1].value
        intcode.update_position(new_position)


class JumpIfFalseInstruction(Instruction):
    number_of_arguments = 2

    def execute(self, intcode, arguments):
        new_position = intcode.position + self.number_of_arguments + 1 if arguments[0].value != 0 else arguments[1].value
        intcode.update_position(new_position)


class IsLessThanInstruction(Instruction):
    number_of_arguments = 3

    def execute(self, intcode, arguments):
        intcode.set(arguments[2].position, 1 if arguments[0].value < arguments[1].value else 0)
        intcode.update_position(intcode.position + self.number_of_arguments + 1)


class IsEqualInstruction(Instruction):
    number_of_arguments = 3

    def execute(self, intcode, arguments):
        intcode.set(arguments[2].position, 1 if arguments[0].value == arguments[1].value else 0)
        intcode.update_position(intcode.position + self.number_of_arguments + 1)


class StopInstruction(Instruction):
    number_of_arguments = 0

    def execute(self, intcode, arguments):
        intcode.stopped = True


instructions = {
    1: AddInstruction,
    2: MultiplyInstruction,
    3: InputInstruction,
    4: OutputInstruction,
    5: JumpIfTrueInstruction,
    6: JumpIfFalseInstruction,
    7: IsLessThanInstruction,
    8: IsEqualInstruction,
    99: StopInstruction
}


class Argument(object):
    def __init__(self, position, value):
        self.position = position
        self.value = value


class Intcode(object):
    def __init__(self, program, inputs=None):
        self.program = program.copy()
        self.stopped = False
        self.output = None
        self.position = 0
        self.inputs = inputs if inputs else []
        self.output = None

    def get_arguments(self, number_of_arguments):
        arguments = []
        modes = str(self.program[self.position])[:-2].zfill(3)[::-1]
        for i in range(number_of_arguments):
            position = self.program[self.position + i + 1]
            arguments.append(Argument(
                position=position,
                value=self.program[position] if modes[i] == "0" else position
            ))
        return arguments

    def run(self):
        while not self.stopped:
            opcode = self.program[self.position] % 100
            instruction = instructions[opcode]()
            arguments = self.get_arguments(instruction.number_of_arguments)
            instruction.execute(self, arguments)
        return self.output

    def set(self, position, value):
        self.program[position] = value

    def get_input(self):
        return self.inputs.pop()

    def update_position(self, position):
        self.position = position
