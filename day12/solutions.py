from math import gcd
from functools import reduce


def load_input():
    with open("day12/input.txt") as f:
        lines = f.readlines()
    return lines


def lcm(a, b):
    return a * b // gcd(a, b)


class Moon(object):
    def __init__(self, position):
        self.position = position
        self.velocity = [0, 0, 0]

    def update_position(self):
        self.position = [p + v for p, v in zip(self.position, self.velocity)]

    def __repr__(self):
        return f"pos=<x={self.position[0]}, y={self.position[1]}, z={self.position[2]}>, vel=<x={self.velocity[0]}, y={self.velocity[1]}, z={self.velocity[2]}>"

    @property
    def potential_energy(self):
        return sum(abs(self.position[k]) for k in range(3))

    @property
    def kinetic_energy(self):
        return sum(abs(self.velocity[k]) for k in range(3))

    @property
    def energy(self):
        return self.potential_energy * self.kinetic_energy


class System(object):
    def __init__(self, lines):
        self.moons = self.parse_input(lines)
        self.size = len(self.moons)

    @staticmethod
    def parse_input(lines):
        return [Moon([int(x.split(",")[0]) for x in line.strip()[:-1].split("=")[1:]]) for line in lines]

    def update_velocities(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                for axis in range(3):
                    if self.moons[i].position[axis] > self.moons[j].position[axis]:
                        self.moons[i].velocity[axis] -= 1
                        self.moons[j].velocity[axis] += 1
                    elif self.moons[i].position[axis] < self.moons[j].position[axis]:
                        self.moons[i].velocity[axis] += 1
                        self.moons[j].velocity[axis] -= 1

    def update_positions(self):
        for moon in self.moons:
            moon.update_position()

    def update_state(self):
        self.update_velocities()
        self.update_positions()

    def update_state_multiple_times(self, n):
        for _ in range(n):
            self.update_state()

    @property
    def energy(self):
        return sum(moon.energy for moon in self.moons)

    def compute_period(self):
        initial_state = [[(moon.position[axis], moon.velocity[axis]) for moon in self.moons] for axis in range(3)]
        periods = [False for _ in range(3)]
        n = 0
        while not all(periods):
            self.update_state()
            n += 1
            state = [[(moon.position[axis], moon.velocity[axis]) for moon in self.moons] for axis in range(3)]
            for i in range(3):
                if periods[i] is False and state[i] == initial_state[i]:
                    periods[i] = n
        return reduce(lcm, periods)


if __name__ == "__main__":
    lines = load_input()

    system = System(lines)
    system.update_state_multiple_times(10)
    print(system.energy)

    periods = system.compute_period()
    print(periods)
