antinodes = set()


def get_map(path: str) -> dict:
    map = {}
    width = 0
    height = 0
    with open(path, "r") as f:
        lines = f.readlines()
        width = len(lines)
        height = len(lines[0])
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char != "." and char != "\n":
                    if char not in map.keys():
                        map[char] = [(x, y)]
                    else:
                        map[char].append((x, y))
    return map, width, height


def get_number_of_antinodes(map: dict, width: int, height: int) -> int:
    for antenna_frequency in map.keys():
        elements = map[antenna_frequency]
        num_elements = len(elements)
        for i in range(num_elements):
            for j in range(num_elements):
                if i != j:
                    get_antinodes_in_map(elements[i], elements[j], width, height)

    return len(antinodes)


def get_antinodes_in_map(antenna1: tuple, antenna2: tuple, map_width: int, map_haight: int) -> None:
    x1, y1, x2, y2 = 0, 0, 0, 0
    x1 = antenna2[0] + (antenna2[0] - antenna1[0])
    y1 = antenna2[1] + (antenna2[1] - antenna1[1])
    x2 = antenna1[0] - (antenna2[0] - antenna1[0])
    y2 = antenna1[1] - (antenna2[1] - antenna1[1])
    if (x1 >= 0 and x1 < map_width) and (y1 >= 0 and y1 < map_haight):
        antinodes.add((x1, y1))
    if (x2 >= 0 and x2 < map_width) and (y2 >= 0 and y2 < map_haight):
        antinodes.add((x2, y2))


def main() -> None:
    antennas_map_example, width_example, height_exampple = get_map("j8/test.txt")
    antennas_map_input, width_input, height_input = get_map("j8/input.txt")
    # Part 1
    assert get_number_of_antinodes(antennas_map_example, width_example, height_exampple) == 14
    print(get_number_of_antinodes(antennas_map_input, width_input, height_input))
    # Part 2
    # assert something == XXX
    # print(something())


if __name__ == "__main__":
    main()
