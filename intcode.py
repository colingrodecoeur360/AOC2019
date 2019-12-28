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
        if arguments[0].value == 0:
            intcode.update_position(intcode.position + self.number_of_arguments + 1)
        else:
            intcode.update_position(arguments[1].value)


class JumpIfFalseInstruction(Instruction):
    number_of_arguments = 2

    def execute(self, intcode, arguments):
        if arguments[0].value != 0:
            intcode.update_position(intcode.position + self.number_of_arguments + 1)
        else:
            intcode.update_position(arguments[1].value)


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


class AdjustRelativeBaseInstruction(Instruction):
    number_of_arguments = 1

    def execute(self, intcode, arguments):
        intcode.update_relative_base(arguments[0].value)
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
    9: AdjustRelativeBaseInstruction,
    99: StopInstruction
}


class Argument(object):
    def __init__(self, position, value):
        self.position = position
        self.value = value


class Intcode(object):
    def __init__(self, program, inputs=None):
        self.program = program.copy()
        self.inputs = inputs if inputs else []
        self.output = None
        self.outputs = []
        self.position = 0
        self.relative_base = 0
        self.memory = {}
        self.stopped = False
        self.is_waiting_for_input = False

    def get_arguments(self, number_of_arguments):
        arguments = []
        modes = str(self.program[self.position])[:-2].zfill(3)[::-1]
        for i in range(number_of_arguments):
            position = self.get(self.position + i + 1)
            if modes[i] == "0":
                argument = Argument(
                    position=position,
                    value=self.get(position)
                )
            elif modes[i] == "1":
                argument = Argument(
                    position=position,
                    value=position
                )
            elif modes[i] == "2":
                argument = Argument(
                    position=position + self.relative_base,
                    value=self.get(position + self.relative_base)
                )
            else:
                raise Exception("Unsupported mode" + modes[i])
            arguments.append(argument)
        return arguments

    def run(self):
        self.output = None
        while not self.stopped and self.output is None:
            opcode = self.program[self.position] % 100
            if opcode == 3 and len(self.inputs) == 0:
                self.is_waiting_for_input = True
                break
            instruction = instructions[opcode]()
            arguments = self.get_arguments(instruction.number_of_arguments)
            instruction.execute(self, arguments)
        if self.output is not None:
            self.outputs.append(self.output)
        return self.output

    def execute(self):
        while not self.stopped and not self.is_waiting_for_input:
            self.run()
        return self.outputs[-1]

    def get(self, position):
        if position >= len(self.program):
            return self.memory.get(position, 0)
        else:
            return self.program[position]

    def set(self, position, value):
        if position >= len(self.program):
            self.memory[position] = value
        else:
            self.program[position] = value

    def get_input(self):
        return self.inputs.pop()

    def update_position(self, position):
        self.position = position

    def update_relative_base(self, offset):
        self.relative_base += offset

    def add_input(self, value):
        self.is_waiting_for_input = False
        self.inputs = [value] + self.inputs

    def add_inputs(self, values):
        for value in values:
            self.add_input(value)
