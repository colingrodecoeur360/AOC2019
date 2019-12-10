import math


def load_input():
    with open("day10/input.txt") as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]


def compute_asteroids_positions(grid):
    asteroids = []
    length, width = len(grid), len(grid[0])
    for x in range(length):
        for y in range(width):
            cell = grid[x][y]
            if cell == "#":
                asteroids.append((x, y))
    return asteroids


def compute_vector(asteroid1, asteroid2):
    delta_x = asteroid2[0] - asteroid1[0]
    delta_y = asteroid2[1] - asteroid1[1]
    distance_squared = delta_x ** 2 + delta_y ** 2
    gcd = math.gcd(abs(delta_x), abs(delta_y))
    direction = (delta_x / gcd, delta_y / gcd)
    return {
        "direction": direction,
        "distance_squared": distance_squared
    }


def compute_visible_asteroids(station, asteroids):
    vectors = {}
    for asteroid in asteroids:
        if asteroid == station:
            continue
        vector = compute_vector(station, asteroid)
        if vector["direction"] not in vectors:
            vectors[vector["direction"]] = [vector["distance_squared"]]
        else:
            vectors[vector["direction"]].append(vector["distance_squared"])
    return {k: list(sorted(v)) for k, v in vectors.items()}


def compute_optimal_station(asteroids):
    optimal_station = None
    optimal_station_visible_asteroids = []
    for station in asteroids:
        visible_asteroids = compute_visible_asteroids(station, asteroids)
        if len(visible_asteroids) > len(optimal_station_visible_asteroids):
            optimal_station_visible_asteroids = visible_asteroids
            optimal_station = station
    return optimal_station, optimal_station_visible_asteroids


def compute_max_visible_asteroids(grid):
    asteroids = compute_asteroids_positions(grid)
    return len(compute_optimal_station(asteroids)[1])


def compute_nth_hit(visible_asteroids, n):
    visible_asteroids = list(sorted(visible_asteroids.items(), key=lambda v: compute_angle(v[0])))
    popped = 0
    current_direction = 0
    while popped < n - 1:
        if visible_asteroids[current_direction]:
            visible_asteroids[current_direction] = visible_asteroids[current_direction][1:]
            popped += 1
        current_direction += 1
        if current_direction == len(visible_asteroids):
            current_direction = 0
    return visible_asteroids[current_direction]


def compute_nth_hit_answer(grid):
    asteroids = compute_asteroids_positions(grid)
    optimal_station, visible_asteroids = compute_optimal_station(asteroids)
    ((x, y), [distance]) = compute_nth_hit(visible_asteroids, 200)
    k = (distance / (x ** 2 + y ** 2)) ** 0.5
    return 100 * (optimal_station[1] + k * y) + optimal_station[0] + k * x


def compute_angle(vector):
    reference = (-1, 0)
    cos = (vector[0] * reference[0] + abs(vector[1]) * reference[1]) / (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    return 2 * math.pi - math.acos(cos) if vector[1] < 0 else math.acos(cos)


if __name__ == "__main__":
    grid = load_input()

    print(compute_max_visible_asteroids(grid))
    print(compute_nth_hit_answer(grid))
