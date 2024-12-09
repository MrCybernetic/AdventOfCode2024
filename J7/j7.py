from itertools import product
operations = ["+", "*"]
operations_part2 = ["+", "*", "||"]


def get_test_value(line: str) -> str:
    return int(line.split(":")[0])


def get_number_in_equations(line: str) -> str:
    return line.split(":")[1].replace("\n", "").split(" ")[1::]


def get_calib(path: str) -> list:
    calib_equations = []
    with open(path, "r") as f:
        lines = f.readlines()
    for line in lines:
        calib_equations.append((get_test_value(line), get_number_in_equations(line)))
    return calib_equations


def evaluate_expression(numbers, operators):
    result = int(numbers[0])
    for i in range(len(operators)):
        if operators[i] == '+':
            result += int(numbers[i + 1])
        elif operators[i] == '*':
            result *= int(numbers[i + 1])
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result


def get_total_calibration_result(calibration_equations: list) -> int:
    total = 0
    for equation in calibration_equations:
        expected_result = equation[0]
        number_in_equations = equation[1]
        num_operator_slots = len(number_in_equations) - 1

        # Generate all possible combinations of operators
        for operators in product(operations, repeat=num_operator_slots):
            result = evaluate_expression(number_in_equations, operators)
            if result == expected_result:
                total += expected_result
                break
    return total


def get_total_calibration_result_part_2(calibration_equations: list) -> int:
    total = 0
    for equation in calibration_equations:
        expected_result = equation[0]
        number_in_equations = equation[1]
        num_operator_slots = len(number_in_equations) - 1

        # Generate all possible combinations of operators
        for operators in product(operations_part2, repeat=num_operator_slots):
            result = evaluate_expression(number_in_equations, operators)
            if result == expected_result:
                total += expected_result
                break
    return total


def main() -> None:
    calibration_equations_exemple = get_calib("j7/test.txt")
    calibration_equations = get_calib("j7/input.txt")
    # Part 1
    assert get_total_calibration_result(calibration_equations_exemple) == 3749
    print(get_total_calibration_result(calibration_equations))
    # Part 2
    assert get_total_calibration_result_part_2(calibration_equations_exemple) == 11387
    print(get_total_calibration_result_part_2(calibration_equations))


if __name__ == "__main__":
    main()
