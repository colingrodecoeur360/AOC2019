import math


def load_input():
    with open("day14/input.txt") as f:
        lines = f.readlines()
    return lines


def parse_input(puzzle_input):
    def parse_line(line):
        inputs, output = line.split(" => ")
        output_quantity, output_name = output.split(" ")
        return (output_name, {"units": int(output_quantity),
                              "inputs": {x.split(" ")[1]: int(x.split(" ")[0]) for x in inputs.split(", ")}})

    return dict([parse_line(line.strip()) for line in puzzle_input])


def compute_elements_usage(recipe):
    outputs = {}
    inputs = {}
    for k, v in recipe.items():
        outputs[k] = outputs.get(k, 0) + 1
        for i in v["inputs"].keys():
            inputs[i] = inputs.get(i, 0) + 1
    return inputs


def compute_requirements(puzzle_input, amount_of_fuel=1):
    final_element = "FUEL"

    recipe = parse_input(puzzle_input)
    usages = compute_elements_usage(recipe)
    usages_treated = {k: 0 for k in usages}
    requirements = {k: 0 for k in usages}
    requirements[final_element] = amount_of_fuel
    elements = {final_element}

    while len(elements) > 0:
        element = next(e for e in elements if usages_treated.get(e, 0) == usages.get(e, 0))
        elements.remove(element)
        if element != "ORE":
            for i, quantity in recipe[element]["inputs"].items():
                requirements[i] += quantity * math.ceil(requirements[element] / recipe[element]["units"])
                usages_treated[i] += 1
                elements.add(i)
    return requirements


def compute_ore_requirements(puzzle_input, amount_of_fuel=1):
    requirements = compute_requirements(puzzle_input, amount_of_fuel)
    return requirements["ORE"]


def compute_max_amount_of_fuel(puzzle_input, available_amount_of_ore):
    lower_bound = 1
    upper_bound = available_amount_of_ore

    while upper_bound - lower_bound > 1:
        amount_of_fuel = (lower_bound + upper_bound) // 2
        amount_of_ore = compute_ore_requirements(puzzle_input, amount_of_fuel)
        if amount_of_ore > available_amount_of_ore:
            upper_bound = amount_of_fuel
        else:
            lower_bound = amount_of_fuel
    return lower_bound


if __name__ == "__main__":
    recipe = load_input()

    compute_ore_requirements(recipe)
    print(compute_ore_requirements(recipe))
    print(compute_max_amount_of_fuel(recipe, 1_000_000_000_000))
