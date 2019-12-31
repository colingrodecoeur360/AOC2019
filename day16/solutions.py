def load_input():
    with open("day16/input.txt") as f:
        numbers = f.read()
    return [int(number) for number in list(numbers.strip())]


def fft(numbers):
    def f(i):
        pattern = []
        while len(pattern) <= n:
            pattern.extend([0] * i)
            pattern.extend([1] * i)
            pattern.extend([0] * i)
            pattern.extend([-1] * i)
        return int(str(sum(number * phase for number, phase in zip(numbers, pattern[1:(n + 1)])))[-1])

    n = len(numbers)
    return [f(i) for i in range(1, n + 1)]


def fft_n(numbers, n):
    for _ in range(n):
        numbers = fft(numbers)
    return numbers


def decode_message(numbers):
    offset = int("".join([str(x) for x in numbers[:7]]))
    input_length = len(numbers) * 10000

    repeats = (input_length - offset) // len(numbers) + 1
    digits = ([int(x) for x in numbers] * repeats)[::-1]
    for _ in range(100):
        for i in range(len(digits) - 1):
            digits[i + 1] = (digits[i + 1] + digits[i]) % 10
    return "".join([str(x) for x in digits[(input_length - offset) - 8:(input_length - offset)][::-1]])


if __name__ == "__main__":
    numbers = load_input()
    print("".join([str(x) for x in fft_n(numbers, 100)[:8]]))
    print(decode_message(numbers))
