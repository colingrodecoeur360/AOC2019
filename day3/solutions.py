def load_input():
    with open("day3/input.txt") as f:
        lines = f.readlines()
    return [line.strip().split(",") for line in lines]


VERTICAL_MOVES = {"U": 1, "D": -1}
HORIZONTAL_MOVES = {"R": 1, "L": -1}


def compute_points_crossed(wire):
    points_crossed = dict()
    steps = 0
    x, y = 0, 0
    for move in wire:
        direction = move[0]
        distance = int(move[1:])
        vertical_move = VERTICAL_MOVES.get(direction, 0)
        horizontal_move = HORIZONTAL_MOVES.get(direction, 0)
        for step in range(distance):
            steps += 1
            y += vertical_move
            x += horizontal_move
            points_crossed[(x, y)] = points_crossed.get((x, y)) or steps
    return points_crossed


def compute_distance_of_closest_intersection(wires):
    points_crossed1, points_crossed2 = [compute_points_crossed(wire) for wire in wires]
    intersections = [point for point in points_crossed1 if point in points_crossed2]
    manhattan_distances = [abs(point[0]) + abs(point[1]) for point in intersections]
    return min(manhattan_distances)


def compute_minimum_total_steps_to_intersection(wires):
    points_crossed1, points_crossed2 = [compute_points_crossed(wire) for wire in wires]
    intersections = [point for point in points_crossed1 if point in points_crossed2]
    intersections_total_steps = [points_crossed1[point] + points_crossed2[point] for point in intersections]
    return min(intersections_total_steps)


if __name__ == "__main__":
    wires = load_input()
    print(compute_distance_of_closest_intersection(wires))
    print(compute_minimum_total_steps_to_intersection(wires))
