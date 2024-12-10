vizu = []


def display():
    for row in vizu:
        for element in row:
            print(element, end=" ")


def get_map(path: str) -> dict:
    map = {}
    width = 0
    height = 0
    with open(path, "r") as f:
        lines = f.readlines()
        width = len(lines[0].replace("\n", ""))
        height = len(lines)
        for y, line in enumerate(lines):
            vizu.append([])
            for x, char in enumerate(line):
                vizu[y].append(char)
                if char != "." and char != "\n":
                    if char not in map.keys():
                        map[char] = [(x, y)]
                    else:
                        map[char].append((x, y))
    return map, width, height


def get_number_of_antinodes(map: dict, width: int, height: int, part_number: int) -> int:
    antinodes = set()
    for antenna_frequency in map.keys():
        elements = map[antenna_frequency]
        num_elements = len(elements)
        for i in range(num_elements):
            for j in range(num_elements):
                if i != j:
                    if part_number == 1:
                        get_antinodes_in_map(antinodes, elements[i], elements[j], width, height)
                    elif part_number == 2:
                        get_antinodes_in_map_part2(antinodes, elements[i], elements[j], width, height)
    return len(antinodes)


def get_antinodes_in_map(antinodes: set, antenna1: tuple, antenna2: tuple, map_width: int, map_haight: int) -> None:
    x1, y1, x2, y2 = 0, 0, 0, 0
    dx = antenna2[0] - antenna1[0]
    dy = antenna2[1] - antenna1[1]
    x1 = antenna2[0] + dx
    y1 = antenna2[1] + dy
    x2 = antenna1[0] - dx
    y2 = antenna1[1] - dy
    if (0 <= x1 < map_width) and (0 <= y1 < map_haight):
        antinodes.add((x1, y1))
    if (0 <= x2 < map_width) and (0 <= y2 < map_haight):
        antinodes.add((x2, y2))


def get_antinodes_in_map_part2(antinodes: set, antenna1: tuple, antenna2: tuple, map_width: int, map_height: int) -> None:
    x1, y1, x2, y2 = 0, 0, 0, 0
    dx = antenna2[0] - antenna1[0]
    dy = antenna2[1] - antenna1[1]
    x1, y1 = antenna2
    x2, y2 = antenna1
    antinodes.add(antenna1)
    antinodes.add(antenna2)
    while (0 <= x1 < map_width) and (0 <= y1 < map_height):
        antinodes.add((int(x1), int(y1)))
        vizu[y1][x1] = "#"
        x1 = x1 + dx
        y1 = y1 + dy
    while (0 <= x2 < map_width) and (0 <= y2 < map_height):
        antinodes.add((x2, y2))
        vizu[y2][x2] = "#"
        x2 = x2 - dx
        y2 = y2 - dy


def main() -> None:
    antennas_map_example, width_example, height_example = get_map("j8/test.txt")
    antennas_map_input, width_input, height_input = get_map("j8/input.txt")
    # Part 1
    assert get_number_of_antinodes(antennas_map_example, width_example, height_example, 1) == 14
    print(get_number_of_antinodes(antennas_map_input, width_input, height_input, 1))
    # Part 2
    assert get_number_of_antinodes(antennas_map_example, width_example, height_example, 2) == 34
    print(get_number_of_antinodes(antennas_map_input, width_input, height_input, 2))


if __name__ == "__main__":
    main()
