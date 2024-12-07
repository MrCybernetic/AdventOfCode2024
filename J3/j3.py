import re


def get_program(path: str) -> str:
    program = ""
    with open(path, "r") as f:
        program = f.read()
    return program


def get_sum_of_multiplications(program: str) -> int:
    sum = 0
    operations = []
    pattern = r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)'
    operations = re.findall(pattern, program)
    for operation in operations:
        if (operation != "don\'t()") and (operation != "do()"):
            sum += get_mul_result(operation)
    return sum


def get_mul_result(mul_str: str) -> int:
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    a = int(re.findall(pattern, mul_str)[0][0])
    b = int(re.findall(pattern, mul_str)[0][1])
    return a*b


def get_sum_of_multiplications_taking_care_of_enabling_disabling(program: str) -> int:
    sum = 0
    operations = []
    enable = True
    pattern = r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)'
    operations = re.findall(pattern, program)
    for operation in operations:
        if operation == "don\'t()":
            enable = False
        elif operation == "do()":
            enable = True
        else:
            if enable:
                sum += get_mul_result(operation)
    return sum


def main() -> None:
    program_exemple1 = get_program("j3/test1.txt")
    program_exemple2 = get_program("j3/test2.txt")
    program_input = get_program("j3/input.txt")
    # Part 1
    assert get_sum_of_multiplications(program_exemple1) == 161
    print(get_sum_of_multiplications(program_input))
    # # Part 2
    assert get_sum_of_multiplications_taking_care_of_enabling_disabling(program_exemple2) == 48
    print(get_sum_of_multiplications_taking_care_of_enabling_disabling(program_input))


if __name__ == "__main__":
    main()
