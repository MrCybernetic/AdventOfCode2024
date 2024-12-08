from dataclasses import dataclass
import copy


@dataclass
class Guard:
    coord: tuple[int, int]
    orientation: tuple[int, int]

    def __str__(self):
        return f"Guard at {self.coord} facing {self.orientation}"

    def get_next_coord(self):
        return (self.coord[0] + self.orientation[0], self.coord[1] + self.orientation[1])

    def walk(self):
        self.coord = (self.coord[0] + self.orientation[0], self.coord[1] + self.orientation[1])

    def turn_90(self):
        if self.orientation == (1, 0):
            self.orientation = (0, 1)
        elif self.orientation == (0, 1):
            self.orientation = (-1, 0)
        elif self.orientation == (-1, 0):
            self.orientation = (0, -1)
        elif self.orientation == (0, -1):
            self.orientation = (1, 0)


@dataclass
class Map:
    content: list[list[str]]
    not_looped: bool = True

    def __post_init__(self):
        self.width = len(self.content[0])
        self.height = len(self.content)

    def __str__(self):
        result = ""
        for line in self.content:
            result += "".join(line) + "\n"
        return result

    def get_cell_type(self, x: int, y: int) -> str:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return "out"
        else:
            return self.content[y][x]

    def set_cell_type(self, x: int, y: int, type: str) -> None:
        self.content[y][x] = type


def get_map_guard_and_notes(path: str) -> tuple[Map, Guard, Map]:
    with open(path, "r") as f:
        lines = f.readlines()
        map_instance = Map([list(line.strip()) for line in lines])
        notes = Map([[" " for _ in range(len(lines[0].strip()))] for _ in lines])
        guardian = None
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                if char == "^":
                    guardian = Guard((x, y), (0, -1))
                    notes.content[y][x] = "$"
        return map_instance, guardian, notes


def get_total_distinct_position(map, guard, notes) -> int:
    still_inside = True
    map.not_looped = True
    memory = {}
    while still_inside or map.not_looped:
        next_step_coord = guard.get_next_coord()
        next_step_type = map.get_cell_type(next_step_coord[0], next_step_coord[1])
        match next_step_type:
            case "." | "^":
                guard.walk()
                notes.content[next_step_coord[1]][next_step_coord[0]] = "$"
                if (guard.coord, guard.orientation) not in memory:
                    memory[(guard.coord, guard.orientation)] = 1
                else:
                    map.not_looped = False
                    break
            case "out":
                still_inside = False
                break
            case "#":
                guard.turn_90()
    total_count = sum(row.count("$") for row in notes.content)
    return total_count


def get_number_of_loops(map, notes) -> int:
    number_of_loops = 0
    potential_obstructions = []
    for y, row in enumerate(notes.content):
        for x, char in enumerate(row):
            if char == "$" and map.get_cell_type(x, y) != "^":
                potential_obstructions.append((x, y))
    initial_content = copy.deepcopy(map.content)
    initial_guardian = None
    for y, row in enumerate(map.content):
        for x, char in enumerate(row):
            if char == "^":
                initial_guardian = Guard((x, y), (0, -1))
                break
    for n, coord in enumerate(potential_obstructions):
        map_copy = Map(copy.deepcopy(initial_content))
        guardian_copy = copy.deepcopy(initial_guardian)
        notes_copy = copy.deepcopy(notes)
        map_copy.set_cell_type(coord[0], coord[1], "#")
        get_total_distinct_position(map_copy, guardian_copy, notes_copy)
        if not map_copy.not_looped:
            number_of_loops += 1
        print(f"{n}/{len(potential_obstructions)}")
    return number_of_loops


def main() -> None:
    map_example, guard_example, notes_example = get_map_guard_and_notes("J6/test.txt")
    map, guard, notes = get_map_guard_and_notes("J6/input.txt")
    # Part 1
    assert get_total_distinct_position(map_example, guard_example, notes_example) == 41
    print(get_total_distinct_position(map, guard, notes))
    # Part 2
    assert get_number_of_loops(map_example, notes_example) == 6
    print(get_number_of_loops(map, notes))


if __name__ == "__main__":
    main()
