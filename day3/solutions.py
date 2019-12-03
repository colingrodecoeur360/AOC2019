def load_input():
    with open("day3/input.txt") as f:
        lines = f.readlines()
    return [line.strip().split(",") for line in lines]


def compute_points_crossed(wire):
    points_crossed = dict()
    steps = 0
    x, y = 0, 0
    for move in wire:
        direction = move[0]
        distance = int(move[1:])
        if direction == "U":
            for step in range(distance):
                steps += 1
                points_crossed[(x, y + step + 1)] = points_crossed.get((x, y + step + 1)) or steps
            y += distance
        if direction == "D":
            for step in range(distance):
                steps += 1
                points_crossed[(x, y - step - 1)] = points_crossed.get((x, y - step - 1)) or steps
            y -= distance
        if direction == "R":
            for step in range(distance):
                steps += 1
                points_crossed[(x + step + 1, y)] = points_crossed.get((x + step + 1, y)) or steps
            x += distance
        if direction == "L":
            for step in range(distance):
                steps += 1
                points_crossed[(x - step - 1, y)] = points_crossed.get((x - step - 1, y)) or steps
            x -= distance
    return points_crossed


def compute_distance_of_closest_intersection(wires):
    points_crossed1 = compute_points_crossed(wires[0])
    points_crossed2 = compute_points_crossed(wires[1])
    intersections = [point for point in points_crossed1 if point in points_crossed2]
    manhattan_distances = [abs(x[0]) + abs(x[1]) for x in list(intersections)]
    return min(manhattan_distances)


def compute_minimum_total_steps_to_intersection(wires):
    points_crossed1 = compute_points_crossed(wires[0])
    points_crossed2 = compute_points_crossed(wires[1])
    intersections = [point for point in points_crossed1 if point in points_crossed2]
    intersections_total_steps = {point: points_crossed1[point] + points_crossed2[point] for point in intersections}
    return min(intersections_total_steps.values())


if __name__ == "__main__":
    wires = load_input()
    print(compute_distance_of_closest_intersection(wires))
    print(compute_minimum_total_steps_to_intersection(wires))
