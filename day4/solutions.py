def meets_condition_part_1(number):
    digits = [int(x) for x in str(number)]
    differences = [x - y for x, y in zip(digits[1:], digits[:-1])]
    return 0 in differences and all([difference >= 0 for difference in differences])


def meets_condition_part_2(number):
    digits = [int(x) for x in str(number)]
    differences = [x - y for x, y in zip(digits[1:], digits[:-1])]
    return 0 in differences and all([difference >= 0 for difference in differences]) and has_isolated_zero(differences)


def has_isolated_zero(digits):
    if digits[0] == 0 and digits[1] != 0:
        return True
    if digits[-1] == 0 and digits[-2] != 0:
        return True
    for i in range(1, len(digits) - 1):
        if digits[i] == 0 and digits[i - 1] != 0 and digits[i + 1] != 0:
            return True
    return False


if __name__ == "__main__":
    bounds = (271973, 785961)
    print(sum(meets_condition_part_1(number) for number in range(*bounds)))
    print(sum(meets_condition_part_2(number) for number in range(*bounds)))
