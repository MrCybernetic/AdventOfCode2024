def get_lists(lists_path: str) -> tuple:
    list1 = []
    list2 = []
    with open(lists_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            list1.append(int(line.split("   ")[0]))
            list2.append(int(line.split("   ")[1].replace("\n", "")))
    return list1, list2


def get_total_distance(list1:  list, list2: list) -> int:
    total = 0
    list1_copy = list1.copy()
    list2_copy = list2.copy()
    list1_copy.sort()
    list2_copy.sort()
    for index, element in enumerate(list1_copy):
        total += abs(element-list2_copy[index])
    return total


def get_total_similarities(list1:  list, list2: list) -> int:
    total = 0
    for element in list1:
        total += element * list2.count(element)
    return total


def main() -> None:
    list1_exemple, list2_exemple = get_lists("J1/test.txt")
    list1, list2 = get_lists("J1/input.txt")
    # Part 1
    assert get_total_distance(list1_exemple, list2_exemple) == 11
    print(get_total_distance(list1, list2))
    # Part 2
    assert get_total_similarities(list1_exemple, list2_exemple) == 31
    print(get_total_similarities(list1, list2))


if __name__ == "__main__":
    main()
