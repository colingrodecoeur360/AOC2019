def load_input():
    with open("day9/input.txt") as f:
        instructions = f.read()
    return [int(x) for x in instructions.strip().split(",")]


def compute_intcode(numbers, input_integer):
    position = 0
    relative_base = 0
    numbers = numbers + [0] * 1000
    outputs = []

    while numbers[position] % 100 != 99:
        operation = numbers[position] % 100
        parameters = [int(x) for x in reversed(str(numbers[position] // 100).zfill(3))]

        def get_argument(index):
            if parameters[index] == 0:
                return numbers[position + index + 1]
            elif parameters[index] == 1:
                return position + index + 1
            elif parameters[index] == 2:
                return numbers[position + index + 1] + relative_base
            else:
                raise Exception("Invalid parameter", parameters[index])

        arguments = [get_argument(index) for index in range(3)]

        if operation == 1:
            numbers[arguments[2]] = numbers[arguments[0]] + numbers[arguments[1]]
            position += 4
        elif operation == 2:
            numbers[arguments[2]] = numbers[arguments[0]] * numbers[arguments[1]]
            position += 4
        elif operation == 3:
            numbers[arguments[0]] = input_integer
            position += 2
        elif operation == 4:
            output = numbers[arguments[0]]
            outputs.append(output)
            position += 2
        elif operation == 5:
            if numbers[arguments[0]] != 0:
                position = numbers[arguments[1]]
            else:
                position += 3
        elif operation == 6:
            if numbers[arguments[0]] == 0:
                position = numbers[arguments[1]]
            else:
                position += 3
        elif operation == 7:
            numbers[arguments[2]] = 1 if numbers[arguments[0]] < numbers[arguments[1]] else 0
            position += 4
        elif operation == 8:
            numbers[arguments[2]] = 1 if numbers[arguments[0]] == numbers[arguments[1]] else 0
            position += 4
        elif operation == 9:
            relative_base += numbers[arguments[0]]
            position += 2
        else:
            print("Unsupported operation", operation)
            return
    return outputs


if __name__ == "__main__":
    numbers = load_input()

    print(compute_intcode(numbers, 1)[0])
    print(compute_intcode(numbers, 2)[0])
