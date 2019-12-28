from intcode import Intcode


def load_input():
    with open("day17/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


def build_scaffolding(instructions):
    scaffolding = [chr(x) for x in instructions]
    return [list(row) for row in "".join(scaffolding).split("\n") if len(row)]


def display_scaffolding(scaffolding):
    for row in scaffolding:
        print("".join([x.rjust(3) for x in row]))


def get_intersections(scaffolding):
    width, height = len(scaffolding), len(scaffolding[0])
    intersections = []
    for i, row in enumerate(scaffolding):
        for j, value in enumerate(row):
            if (
                    0 < i < width - 1 and
                    0 < j < height - 1 and
                    scaffolding[i][j] == "#" and
                    scaffolding[i - 1][j] == "#" and
                    scaffolding[i + 1][j] == "#" and
                    scaffolding[i][j - 1] == "#" and
                    scaffolding[i][j + 1] == "#"):
                intersections.append((i, j))
    return intersections


def compute_alignment(intersections):
    return sum([intersection[0] * intersection[1] for intersection in intersections])


turns_by_direction = {
    (0, 1): {
        "R": (1, 0),
        "L": (-1, 0)
    },
    (1, 0): {
        "R": (0, -1),
        "L": (0, 1)
    },
    (0, -1): {
        "R": (-1, 0),
        "L": (1, 0)
    },
    (-1, 0): {
        "R": (0, 1),
        "L": (0, -1)
    },
}


def compute_exploration_path(scaffolding):
    scaffolding = [[str(i + 1)] + row + [str(i + 1)] for i, row in enumerate(scaffolding)]
    scaffolding = [[str(i) for i in range(len(scaffolding[0]))]] + scaffolding + [
        [str(i) for i in range(len(scaffolding[0]))]]
    origin = next((i, j) for i, row in enumerate(scaffolding) for j, value in enumerate(row) if value == "^")

    x, y = origin
    path = []
    direction = (-1, 0)
    distance = 0
    should_stop = False

    while should_stop is False:
        if scaffolding[x + direction[0]][y + direction[1]] == "#":
            distance += 1
            x += direction[0]
            y += direction[1]
        else:
            if distance > 0:
                path.append(str(distance))
            if scaffolding[x + turns_by_direction[direction]["L"][0]][y + turns_by_direction[direction]["L"][1]] == "#":
                path.append("L")
                direction = turns_by_direction[direction]["L"]
                x += direction[0]
                y += direction[1]
                distance = 1
            elif scaffolding[x + turns_by_direction[direction]["R"][0]][
                y + turns_by_direction[direction]["R"][1]] == "#":
                path.append("R")
                direction = turns_by_direction[direction]["R"]
                x += direction[0]
                y += direction[1]
                distance = 1
            else:
                should_stop = True

    return path


def enter_instructions(computer):
    # Solved by hand
    main_instructions = [ord(x) for x in "A,A,B,C,A,C,A,B,C,B\n"]
    instructions_a = [ord(x) for x in "R,12,L,8,R,6\n"]
    instructions_b = [ord(x) for x in "R,12,L,6,R,6,R,8,R,6\n"]
    instructions_c = [ord(x) for x in "L,8,R,8,R,6,R,12\n"]
    video_feed_instructions = [ord(x) for x in "n\n"]

    for instructions in [main_instructions, instructions_a, instructions_b, instructions_c, video_feed_instructions]:
        computer.add_inputs(instructions)


if __name__ == "__main__":
    program = load_input()

    computer = Intcode(program)
    computer.execute()
    scaffolding = build_scaffolding(computer.outputs)
    intersections = get_intersections(scaffolding)
    print(compute_alignment(intersections))

    computer = Intcode(program)
    computer.program[0] = 2
    computer.execute()
    scaffolding = build_scaffolding(computer.outputs)
    path = compute_exploration_path(scaffolding[:-1])
    print(",".join(path))

    enter_instructions(computer)
    computer.execute()
    print(computer.outputs[-1])
