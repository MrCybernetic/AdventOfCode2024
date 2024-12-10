import re


def get_representation(path: str) -> str:
    representation = ""
    with open(path, "r") as f:
        input = f.read()
        id = 0
        for i, digit in enumerate(input):
            if i % 2 == 0:
                representation += int(digit)*str(id)
                id += 1
            else:
                representation += int(digit)*"."
    return representation


def calculate_checksum(representation: str) -> int:
    checksum = 0
    for index, char in enumerate(representation):
        if char != '.':
            checksum += index*int(char)
    return checksum


def get_checksum_compacted(filesystem_representation: str) -> int:
    # get_total_dots = len(re.findall(r".", filesystem_representation))
    while gaps_remaining(filesystem_representation):
        filesystem_representation = move_to_left(filesystem_representation)
        # print(f'{len(re.search(r'\.+$', filesystem_representation).group())}/{get_total_dots}')
    return calculate_checksum(filesystem_representation)


def move_to_left(representation: str) -> str:
    first_dot_index = representation.find('.')
    last_digit_index = max(i for i, c in enumerate(representation) if c.isdigit())
    b = bytearray(representation.encode())
    b[first_dot_index], b[last_digit_index] = b[last_digit_index], b[first_dot_index]
    return b.decode()


def gaps_remaining(representation: str) -> bool:
    pattern = r'\d\.+\d'
    return bool(re.search(pattern, representation))


def main() -> None:
    representation_exemple = get_representation("j9/test.txt")
    representation_input = get_representation("j9/input.txt")
    assert representation_exemple == "00...111...2...333.44.5555.6666.777.888899"
    assert calculate_checksum("0099811188827773336446555566..............") == 1928
    assert gaps_remaining("0099811188827773336446555566..............") is False
    assert gaps_remaining("00998111888277733364.46555566..............") is True
    # Part 1
    assert get_checksum_compacted(representation_exemple) == 1928
    print(get_checksum_compacted(representation_input))
    # Part 2
    # assert something == XXX
    # print(something())


if __name__ == "__main__":
    main()
