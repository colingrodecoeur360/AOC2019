from intcode import Intcode
import math
import sys

sys.setrecursionlimit(2000)


def load_input():
    with open("day15/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


directions = {
    (0, 1): 1,
    (0, -1): 2,
    (-1, 0): 3,
    (1, 0): 4,
}

WALL = 0
EMPTY_CELL = 1
OXYGEN_TANK = 2


class Robot(object):
    def __init__(self, program):
        self.computer = Intcode(program)
        self.area_map = {(0, 0): (EMPTY_CELL, 0)}
        self.position = (0, 0)
        self.tank_position = None

    def explore(self, previous_moves=None):
        if previous_moves is None:
            previous_moves = []
        has_moved = False
        for direction, code in directions.items():
            new_position = (self.position[0] + direction[0], self.position[1] + direction[1])
            if new_position in self.area_map:
                continue
            self.computer.add_input(code)
            output = self.computer.run()
            if output == 0:
                self.area_map[new_position] = (WALL, None)
            if output == 2:
                self.tank_position = new_position
                self.area_map[new_position] = (OXYGEN_TANK, len(previous_moves) + 1)
                has_moved = True
                self.position = new_position
                self.explore(previous_moves=previous_moves + [direction])
            if output == 1:
                self.area_map[new_position] = (EMPTY_CELL, len(previous_moves) + 1)
                has_moved = True
                self.position = new_position
                self.explore(previous_moves=previous_moves + [direction])
        if not has_moved and previous_moves:
            last_move = previous_moves.pop()
            direction = (-last_move[0], -last_move[1])
            self.computer.add_input(directions[direction])
            self.computer.run()
            self.position = (self.position[0] + direction[0], self.position[1] + direction[1])
            self.explore(previous_moves)

    def compute_area_matrix(self):
        cells = self.area_map.keys()

        min_x, min_y = min(cells, key=lambda x: x[0])[0], min(cells, key=lambda x: x[1])[1]
        max_x, max_y = max(cells, key=lambda x: x[0])[0], max(cells, key=lambda x: x[1])[1]
        matrix = [[" " for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

        for (x, y), (code, distance) in self.area_map.items():
            if code == WALL:
                matrix[y - min_y][x - min_x] = "#"
            elif code == EMPTY_CELL:
                matrix[y - min_y][x - min_x] = " "
            elif code == OXYGEN_TANK:
                matrix[y - min_y][x - min_x] = "O"
            if x == y == 0:
                matrix[y - min_y][x - min_x] = "S"
        return matrix

    def display_area(self):
        for row in self.compute_area_matrix():
            print("".join(row))

    def compute_shortest_paths(self):
        grid = self.compute_area_matrix()
        oxygen_tank_position = next((i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if value == "O")

        graph = {}
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value != "#":
                    for (x, y) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][j + y] != "#":
                            if (i, j) in graph:
                                graph[(i, j)].append((i + x, j + y))
                            else:
                                graph[(i, j)] = [(i + x, j + y)]

        distances = {node: math.inf for node in graph}
        previous_nodes = {node: None for node in graph}
        distances[oxygen_tank_position] = 0
        queue = {node for node in graph}

        while len(queue) > 0:
            node = min(queue, key=lambda node: distances[node])
            queue.remove(node)
            for neighbor in graph[node]:
                t = distances[node] + 1
                if t < distances[neighbor]:
                    distances[neighbor] = t
                    previous_nodes[neighbor] = node
        return distances


if __name__ == "__main__":
    program = load_input()

    robot = Robot(program)
    robot.explore()
    print(robot.area_map[robot.tank_position][1])
    print(max(robot.compute_shortest_paths().values()))
