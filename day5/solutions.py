def load_input():
    with open("day5/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


def compute_intcode(numbers, input_integer):
    position = 0
    output = None

    while numbers[position] % 100 != 99:
        operation = numbers[position] % 100
        parameters = [int(x) for x in reversed(str(numbers[position] // 100).zfill(3))]
        if operation == 1:
            arguments = parse_n_arguments(numbers, position, parameters, 2)
            numbers[numbers[position + 3]] = arguments[0] + arguments[1]
            position += 4
        elif operation == 2:
            arguments = parse_n_arguments(numbers, position, parameters, 2)
            numbers[numbers[position + 3]] = arguments[0] * arguments[1]
            position += 4
        elif operation == 3:
            numbers[numbers[position + 1]] = input_integer
            position += 2
        elif operation == 4:
            output = parse_argument(numbers, position, parameters, 0)
            position += 2
        elif operation == 5:
            arguments = parse_n_arguments(numbers, position, parameters, 2)
            if arguments[0] != 0:
                position = arguments[1]
            else:
                position += 3
        elif operation == 6:
            arguments = parse_n_arguments(numbers, position, parameters, 2)
            if arguments[0] == 0:
                position = arguments[1]
            else:
                position += 3
        elif operation == 7:
            arguments = parse_n_arguments(numbers, position, parameters, 2)
            numbers[numbers[position + 3]] = 1 if arguments[0] < arguments[1] else 0
            position += 4
        elif operation == 8:
            arguments = parse_n_arguments(numbers, position, parameters, 2)
            numbers[numbers[position + 3]] = 1 if arguments[0] == arguments[1] else 0
            position += 4
        else:
            print("Unsupported operation", operation)
            return
    return output


def parse_argument(numbers, position, parameters, index):
    return numbers[numbers[position + index + 1]] if parameters[index] == 0 else numbers[position + index + 1]


def parse_n_arguments(numbers, position, parameters, n):
    return [parse_argument(numbers, position, parameters, index) for index in range(n)]


if __name__ == "__main__":
    numbers = load_input()

    print(compute_intcode(numbers.copy(), 1))
    print(compute_intcode(numbers.copy(), 5))
