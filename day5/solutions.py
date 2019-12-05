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
            argument1 = numbers[numbers[position + 1]] if parameters[0] == 0 else numbers[position + 1]
            argument2 = numbers[numbers[position + 2]] if parameters[1] == 0 else numbers[position + 2]
            numbers[numbers[position + 3]] = argument1 + argument2
            position += 4
        elif operation == 2:
            argument1 = numbers[numbers[position + 1]] if parameters[0] == 0 else numbers[position + 1]
            argument2 = numbers[numbers[position + 2]] if parameters[1] == 0 else numbers[position + 2]
            numbers[numbers[position + 3]] = argument1 * argument2
            position += 4
        elif operation == 3:
            numbers[numbers[position + 1]] = input_integer
            position += 2
        elif operation == 4:
            argument = numbers[numbers[position + 1]] if parameters[0] == 0 else numbers[position + 1]
            output = argument
            position += 2
        elif operation == 5:
            argument1 = numbers[numbers[position + 1]] if parameters[0] == 0 else numbers[position + 1]
            argument2 = numbers[numbers[position + 2]] if parameters[1] == 0 else numbers[position + 2]
            if argument1 != 0:
                position = argument2
            else:
                position += 3
        elif operation == 6:
            argument1 = numbers[numbers[position + 1]] if parameters[0] == 0 else numbers[position + 1]
            argument2 = numbers[numbers[position + 2]] if parameters[1] == 0 else numbers[position + 2]
            if argument1 == 0:
                position = argument2
            else:
                position += 3
        elif operation == 7:
            argument1 = numbers[numbers[position + 1]] if parameters[0] == 0 else numbers[position + 1]
            argument2 = numbers[numbers[position + 2]] if parameters[1] == 0 else numbers[position + 2]
            numbers[numbers[position + 3]] = 1 if argument1 < argument2 else 0
            position += 4
        elif operation == 8:
            argument1 = numbers[numbers[position + 1]] if parameters[0] == 0 else numbers[position + 1]
            argument2 = numbers[numbers[position + 2]] if parameters[1] == 0 else numbers[position + 2]
            numbers[numbers[position + 3]] = 1 if argument1 == argument2 else 0
            position += 4
    return output


if __name__ == "__main__":
    numbers = load_input()

    print(compute_intcode(numbers.copy(), 1))
    print(compute_intcode(numbers.copy(), 5))
