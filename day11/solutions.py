from intcode import Intcode


def load_input():
    with open("day11/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


def paint_area(program, initial_color):
    area = {}
    position = (0, 0)
    direction = (0, 1)
    computer = Intcode(program)

    while True:
        color = area.get(position, initial_color)
        computer.add_input(color)
        paint = computer.run()

        if paint is None:
            break

        area[position] = paint
        turn = computer.run()
        direction = compute_direction_after_turn(direction, turn)
        position = compute_position_after_forward_move(position, direction)

    return area


def compute_direction_after_turn(direction, turn):
    left_turns = {
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0),
        (1, 0): (0, 1),
    }
    right_turns = {v: k for k, v in left_turns.items()}
    return {0: left_turns, 1: right_turns}[turn][direction]


def compute_position_after_forward_move(position, direction):
    return position[0] + direction[0], position[1] + direction[1]


def display_area(area):
    points = area.keys()
    min_x, min_y = min(points, key=lambda x: x[0])[0], min(points, key=lambda x: x[1])[1]
    max_x, max_y = max(points, key=lambda x: x[0])[0], max(points, key=lambda x: x[1])[1]

    array = [[" " for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for (x, y), value in area.items():
        if value == 1:
            array[y - min_y][x - min_x] = "#"

    for row in array[::-1]:
        print("".join(row))


if __name__ == "__main__":
    numbers = load_input()

    area = paint_area(numbers, 0)
    print(len(area))

    area = paint_area(numbers, 1)
    display_area(area)
