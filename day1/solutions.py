def load_input():
    with open("day1/input.txt") as f:
        lines = f.readlines()
    return [int(line.strip()) for line in lines]


def compute_fuel_part1(mass):
    return mass // 3 - 2


def compute_fuel_part2(mass):
    fuel = mass // 3 - 2
    return 0 if fuel <= 0 else fuel + compute_fuel_part2(fuel)


if __name__ == "__main__":
    masses = load_input()

    result_part1 = sum(compute_fuel_part1(mass) for mass in masses)
    print(result_part1)

    result_part2 = sum(compute_fuel_part2(mass) for mass in masses)
    print(result_part2)
