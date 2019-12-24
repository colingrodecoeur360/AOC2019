def load_input():
    with open("day24/input.txt") as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]


class Planet1(object):
    def __init__(self, initial_state):
        self.state = initial_state
        self.size = (len(self.state), len(self.state[0]))
        self.history = {self.to_string()}

    def to_string(self):
        return "".join([x for row in self.state for x in row])

    def display_state(self):
        for row in self.state:
            print("".join(row))
        print("\n")

    def update_state(self):
        state = [row.copy() for row in self.state]
        for i, row in enumerate(self.state):
            for j, value in enumerate(row):
                adjacent_bugs = 0
                if i > 0 and self.state[i - 1][j] == "#":
                    adjacent_bugs += 1
                if i < self.size[0] - 1 and self.state[i + 1][j] == "#":
                    adjacent_bugs += 1
                if j > 0 and self.state[i][j - 1] == "#":
                    adjacent_bugs += 1
                if j < self.size[1] - 1 and self.state[i][j + 1] == "#":
                    adjacent_bugs += 1
                if adjacent_bugs != 1 and value == "#":
                    state[i][j] = "."
                if adjacent_bugs in (1, 2) and value == ".":
                    state[i][j] = "#"
        self.state = state

    def mutate(self):
        while True:
            self.update_state()
            if self.to_string() in self.history:
                break
            self.history.add(self.to_string())

    @property
    def biodiversity_rating(self):
        return sum(2 ** i for i, x in enumerate(self.to_string()) if x == "#")


class Planet2(object):
    def __init__(self, initial_state=None):
        self.state = initial_state or [["."] * 5] * 5
        self.size = (5, 5)

    def to_string(self):
        return "".join([x for row in self.state for x in row])

    def display_state(self):
        for row in self.state:
            print("".join(row))
        print("\n")

    def update_state(self, parent_planet=None, child_planet=None):
        state = [row.copy() for row in self.state]
        for i, row in enumerate(self.state):
            for j, value in enumerate(row):
                if i == j == 2:
                    continue
                adjacent_bugs = 0
                if i > 0 and self.state[i - 1][j] == "#" and (i - 1, j) != (2, 2):
                    adjacent_bugs += 1
                if i < self.size[0] - 1 and self.state[i + 1][j] == "#" and (i + 1, j) != (2, 2):
                    adjacent_bugs += 1
                if j > 0 and self.state[i][j - 1] == "#" and (i, j - 1) != (2, 2):
                    adjacent_bugs += 1
                if j < self.size[1] - 1 and self.state[i][j + 1] == "#" and (i, j + 1) != (2, 2):
                    adjacent_bugs += 1

                if parent_planet is not None:
                    adjacent_bugs += (i == 0 and parent_planet.state[1][2] == "#")
                    adjacent_bugs += (i == 4 and parent_planet.state[3][2] == "#")
                    adjacent_bugs += (j == 0 and parent_planet.state[2][1] == "#")
                    adjacent_bugs += (j == 4 and parent_planet.state[2][3] == "#")

                if child_planet is not None:
                    adjacent_bugs += (i, j) == (1, 2) and sum(x == "#" for x in child_planet.state[0])
                    adjacent_bugs += (i, j) == (2, 1) and sum(row[0] == "#" for row in child_planet.state)
                    adjacent_bugs += (i, j) == (2, 3) and sum(row[4] == "#" for row in child_planet.state)
                    adjacent_bugs += (i, j) == (3, 2) and sum(x == "#" for x in child_planet.state[4])

                if adjacent_bugs != 1 and value == "#":
                    state[i][j] = "."
                if adjacent_bugs in (1, 2) and value == ".":
                    state[i][j] = "#"
        return state

    @property
    def outer_cells(self):
        return {(i, j): value
                for i, row in enumerate(self.state)
                for (j, value) in enumerate(row)
                if i in (0, 4) or j in (0, 4)}

    @property
    def inner_cells(self):
        return {(i, j): value
                for i, row in enumerate(self.state)
                for (j, value) in enumerate(row)
                if (i, j) in ((1, 2), (2, 1), (2, 3), (3, 2))}

    def count_bugs(self):
        return sum(x == "#" for x in self.to_string())


class System(object):
    def __init__(self, initial_state):
        self.planets = [Planet2(initial_state)]

    def display_state(self):
        for i, planet in enumerate(self.planets):
            print("Planet", i)
            planet.display_state()

    def should_append_larger_planet(self):
        planet = self.planets[0]
        return any([x == "#" for x in planet.outer_cells.values()])

    def should_append_smaller_planet(self):
        planet = self.planets[-1]
        return any([x == "#" for x in planet.inner_cells.values()])

    def append_larger_planet(self):
        self.planets = [Planet2([["."] * 5] * 5)] + self.planets

    def append_smaller_planet(self):
        self.planets = self.planets + [Planet2([["."] * 5] * 5)]

    def update_state(self):
        if self.should_append_larger_planet():
            self.append_larger_planet()
        if self.should_append_smaller_planet():
            self.append_smaller_planet()
        new_states = []

        for idx, planet in enumerate(self.planets):
            if idx == 0:
                new_state = planet.update_state(child_planet=self.planets[idx + 1])
            elif idx < len(self.planets) - 1:
                new_state = planet.update_state(parent_planet=self.planets[idx - 1], child_planet=self.planets[idx + 1])
            else:
                new_state = planet.update_state(parent_planet=self.planets[idx - 1])
            new_states.append(new_state)

        for idx, planet in enumerate(self.planets):
            planet.state = new_states[idx]

    def count_bugs(self):
        return sum(planet.count_bugs() for planet in self.planets)


if __name__ == "__main__":
    initial_state = load_input()
    planet = Planet1(initial_state)
    planet.mutate()
    print(planet.biodiversity_rating)

    system = System(initial_state)
    for _ in range(200):
        system.update_state()
    print(system.count_bugs())
