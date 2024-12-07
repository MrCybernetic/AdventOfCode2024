def get_puzzle(path: str) -> dict:
    puzzle = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            puzzle.append([letter for letter in line if letter != '\n'])
    return puzzle


def get_coord_if_letter_present_around_coord(puzzle: list, coord: tuple, letter: str) -> dict:
    x, y = coord
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    matches = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(puzzle[0]) and 0 <= ny < len(puzzle):
            if puzzle[ny][nx] == letter:
                matches.append((nx, ny))
    return matches


def get_number_of_word(puzzle: list, word_to_search: str) -> int:
    count = 0
    for y, line in enumerate(puzzle):
        for x, letter in enumerate(line):
            if letter == word_to_search[0]:
                potential_match_first_letter = (x, y)
                potential_second_matches = get_coord_if_letter_present_around_coord(puzzle, potential_match_first_letter, word_to_search[1])
                for potential_match in potential_second_matches:
                    direction = (potential_match[0] - potential_match_first_letter[0], potential_match[1] - potential_match_first_letter[1])
                    match = True
                    for i in range(2, len(word_to_search)):
                        next_x = potential_match_first_letter[0] + direction[0] * i
                        next_y = potential_match_first_letter[1] + direction[1] * i
                        if not (0 <= next_x < len(puzzle[0]) and 0 <= next_y < len(puzzle)):
                            match = False
                            break
                        if puzzle[next_y][next_x] != word_to_search[i]:
                            match = False
                            break
                    if match:
                        count += 1
    return count


def main() -> None:
    puzzle_exemple = get_puzzle("j4/test.txt")
    puzzle_input = get_puzzle("j4/input.txt")
    # Part 1
    assert get_number_of_word(puzzle_exemple, "XMAS") == 18
    print(get_number_of_word(puzzle_input, "XMAS"))
    # # Part 2
    # assert get_sum_of_multiplications_taking_care_of_enabling_disabling(program_exemple2) == 48
    # print(get_sum_of_multiplications_taking_care_of_enabling_disabling(program_input))


if __name__ == "__main__":
    main()
