def load_input():
    with open("day2/input.txt") as f:
        content = f.read()
    return [int(x) for x in content.split(",")]


def compute_intcode(numbers):
    position = 0
    while numbers[position] != 99:
        operation = numbers[position]
        arguments = (numbers[numbers[position + 1]], numbers[numbers[position + 2]])
        replaced_position = numbers[position + 3]
        if operation == 1:
            numbers[replaced_position] = arguments[0] + arguments[1]
        elif operation == 2:
            numbers[replaced_position] = arguments[0] * arguments[1]
        position += 4
    return numbers


def compute_intcode_result(numbers, noun, verb):
    numbers[1] = noun
    numbers[2] = verb
    return compute_intcode(numbers)[0]


def compute_noun_and_verb(numbers, output):
    for noun in range(100):
        for verb in range(100):
            if compute_intcode_result(numbers.copy(), noun, verb) == output:
                return 100 * noun + verb


if __name__ == "__main__":
    numbers = load_input()

    print(compute_intcode_result(numbers.copy(), 12, 2))
    print(compute_noun_and_verb(numbers.copy(), 19690720))
