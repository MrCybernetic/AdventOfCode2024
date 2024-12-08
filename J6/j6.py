from dataclasses import dataclass


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
    width: int
    height: int
    content: list[list[str]]

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


def get_map_guard_and_notes(path: str) -> tuple[Map, Guard, Map]:
    with open(path, "r") as f:
        lines = f.readlines()
        map_instance = Map(len(lines[0].strip()), len(lines), [list(line.strip()) for line in lines])
        notes = Map(len(lines[0].strip()), len(lines), [[" " for _ in range(len(lines[0].strip()))] for _ in lines])
        guardian = None
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                if char == "^":
                    guardian = Guard((x, y), (0, -1))  # Changed to (0, -1) since ^ points up
                    notes.content[y][x] = "$"
        return map_instance, guardian, notes


def get_total_distinct_position(map, guard, notes) -> int:
    still_inside = True
    while still_inside:
        next_step_coord = guard.get_next_coord()
        next_step_type = map.get_cell_type(next_step_coord[0], next_step_coord[1])
        match next_step_type:
            case "." | "^":
                guard.walk()
                notes.content[next_step_coord[1]][next_step_coord[0]] = "$"
            case "out":
                still_inside = False
                break
            case "#":
                guard.turn_90()
    total_count = sum(row.count("$") for row in notes.content)
    return total_count


def main() -> None:
    map_example, guard_example, notes_example = get_map_guard_and_notes("J6/test.txt")
    map, guard, notes = get_map_guard_and_notes("J6/input.txt")
    # Part 1
    assert get_total_distinct_position(map_example, guard_example, notes_example) == 41
    print(get_total_distinct_position(map, guard, notes))


if __name__ == "__main__":
    main()
