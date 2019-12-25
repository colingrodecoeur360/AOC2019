import math


def load_input():
    with open("day20/input.txt") as f:
        lines = f.readlines()
    return [list(line.replace("\n", "")) for line in lines]


def compute_matching_doors(grid):
    doors = {}
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == ".":
                for (x, y) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if grid[i + x][j + y].isalpha() and grid[i + 2 * x][j + 2 * y].isalpha():
                        door = grid[min(i + x, i + 2 * x)][min(j + y, j + 2 * y)] + grid[max(i + x, i + 2 * x)][
                            max(j + y, j + 2 * y)]
                        if door in doors:
                            doors[door].append((i, j))
                        else:
                            doors[door] = [(i, j)]

    matching_doors = {}
    start_position = None
    end_position = None
    for door, positions in doors.items():
        if len(positions) == 2:
            matching_doors[positions[0]] = positions[1]
            matching_doors[positions[1]] = positions[0]
        if door == "AA":
            start_position = positions[0]
        if door == "ZZ":
            end_position = positions[0]
    return matching_doors, start_position, end_position


def compute_shortest_path(grid):
    matching_doors, start_position, end_position = compute_matching_doors(grid)
    graph = {}
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == ".":
                for (x, y) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if grid[i + x][j + y] == ".":
                        if (i, j) in graph:
                            graph[(i, j)].append((i + x, j + y))
                        else:
                            graph[(i, j)] = [(i + x, j + y)]
                    if grid[i + x][j + y].isalpha() and (i, j) in matching_doors:
                        matching_door = matching_doors[(i, j)]
                        if (i, j) in graph:
                            graph[(i, j)].append(matching_door)
                        else:
                            graph[(i, j)] = [matching_door]

    distances = {node: math.inf for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start_position] = 0
    queue = {node for node in graph}

    while len(queue) > 0:
        node = min(queue, key=lambda node: distances[node])
        queue.remove(node)
        for neighbor in graph[node]:
            t = distances[node] + 1
            if t < distances[neighbor]:
                distances[neighbor] = t
                previous_nodes[neighbor] = node
    return distances[end_position]


if __name__ == "__main__":
    grid = load_input()

    print(compute_shortest_path(grid))
