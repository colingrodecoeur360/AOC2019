from intcode import Intcode


def load_input():
    with open("day13/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


class Breakout(object):
    def __init__(self, program, mode=None):
        self.program = program
        if mode:
            self.program[0] = mode
        self.computer = Intcode(program)

    def display(self):
        array = [[" " for _ in range(max(self.computer.outputs[::3]) + 1)] + [str(j).rjust(3)] for j in range(max(self.computer.outputs[1::3]) + 1)]

        for (x, y, tile) in zip(self.computer.outputs[::3], self.computer.outputs[1::3], self.computer.outputs[2::3]):
            if (x, y) == (-1, 0):
                continue

            symbols = {0: " ", 1: "/", 2: "#", 3: "_", 4: "O"}
            array[y][x] = symbols[tile]

        for row in array:
            print("".join([x.rjust(3) for x in row]))
        print("".join([str(i).rjust(3) for i in range(len(array[0]))]))

    def get_paddle_position(self):
        paddle = self.computer.outputs[2::3][::-1].index(3)
        return self.computer.outputs[::3][::-1][paddle], self.computer.outputs[1::3][::-1][paddle]

    def get_ball_position(self):
        ball = self.computer.outputs[2::3][::-1].index(4)
        return self.computer.outputs[::3][::-1][ball], self.computer.outputs[1::3][::-1][ball]

    def compute_score(self):
        for x, y, tile in zip(self.computer.outputs[::3][::-1], self.computer.outputs[1::3][::-1], self.computer.outputs[2::3][::-1]):
            if (x, y) == (-1, 0):
                return tile
        return 0

    def count_blocks(self):
        return self.computer.outputs[2::3].count(2)

    def play(self):
        breakout.computer.execute()
        while not self.computer.stopped:
            paddle_position = self.get_paddle_position()
            ball_position = self.get_ball_position()

            if paddle_position[0] > ball_position[0]:
                instruction = -1
            elif paddle_position[0] < ball_position[0]:
                instruction = 1
            else:
                instruction = 0

            self.computer.add_input(instruction)
            self.computer.execute()


if __name__ == "__main__":
    program = load_input()

    breakout = Breakout(program)
    breakout.computer.execute()
    print(breakout.count_blocks())

    breakout = Breakout(program, mode=2)
    breakout.play()
    print(breakout.compute_score())
