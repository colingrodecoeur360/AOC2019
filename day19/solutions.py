from intcode import Intcode


def load_input():
    with open("day19/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


def display_beam(affected_points):
    array = [["." for _ in range(50)] for _ in range(50)]
    for (i, j) in affected_points:
        array[i][j] = "#"
    for i, row in enumerate(array):
        print("".join([x.rjust(3) for x in row] + [str(i).rjust(3)]))
    print("".join([str(i).rjust(3) for i in range(50)]))


def is_affected_by_beam(i, j, program):
    computer = Intcode(program)
    computer.add_input(i)
    computer.add_input(j)
    computer.execute()
    return computer.outputs[0] == 1


def compute_affected_points(program, square_size):
    affected_points = []
    for i in range(square_size):
        has_met_beam = False
        for j in range(square_size):
            if is_affected_by_beam(i, j, program):
                affected_points.append((i, j))
                has_met_beam = True
            elif has_met_beam is True:
                break
    return affected_points


def compute_closest_fitting_position(program, square_size):
    i = 4
    j = 0
    while True:
        if is_affected_by_beam(i, j, program) and not is_affected_by_beam(i, j + 1, program):
            if (
                    is_affected_by_beam(i, j - square_size + 1, program) and
                    is_affected_by_beam(i + square_size - 1, j, program) and
                    is_affected_by_beam(i + square_size - 1, j - square_size + 1, program)):
                break
            i += 1
        else:
            j += 1
    return i, j - square_size + 1


if __name__ == "__main__":
    program = load_input()

    affected_points = compute_affected_points(program, 50)
    print(len(affected_points))

    (i, j) = compute_closest_fitting_position(program, 100)
    print(i * 10000 + j)
