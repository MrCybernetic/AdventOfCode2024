def get_rules_and_orders(path: str) -> tuple:
    separator_found = False
    rules_number = 1
    rules = {}
    order = []
    with open(path, "r") as f:
        text = f.readlines()
        for element in text:
            if element == "\n":
                separator_found = True
            elif not (separator_found):
                rules[rules_number] = element.replace("\n", "").split("|")
                rules_number += 1
            else:
                order.append(element.replace("\n", "").split(","))
    return rules, order


def get_sum_of_middle_page_number(rules: dict, orders: list) -> int:
    correct_orders = []
    for order in orders:
        all_rules_respected = True
        for rule_number, rule in rules.items():
            if not (is_rule_respected(rule, order)):
                all_rules_respected = False
                break
        if all_rules_respected:
            correct_orders.append(order)
    sum = 0
    for correct_order in correct_orders:
        sum += int(correct_order[int(len(correct_order)/2)])
    return sum


def is_rule_respected(rule: list, order: list) -> bool:
    try:
        if (order.index(rule[0]) > order.index(rule[1])):
            return False
    except ValueError:
        return True
    return True


def get_sum_of_middle_page_number_by_reordering(rules: dict, orders: list) -> int:
    corrected_orders = []
    for order in orders:
        original_order = order.copy()
        while True:
            all_rules_respected = True
            for rule_number, rule in rules.items():
                if not is_rule_respected(rule, order):
                    order = reorder(rule, order)
                    all_rules_respected = False
            if all_rules_respected:
                break
        if order != original_order:
            corrected_orders.append(order)
    total_sum = 0
    for corrected_order in corrected_orders:
        total_sum += int(corrected_order[len(corrected_order) // 2])
    return total_sum


def reorder(rule: list, order: list) -> list:
    index_0 = order.index(rule[0])
    index_1 = order.index(rule[1])
    temp_order = order.copy()
    temp_order[index_0], temp_order[index_1] = temp_order[index_1], temp_order[index_0]
    return temp_order


def main() -> None:
    rules_exemple, orders_exemple = get_rules_and_orders("j5/test.txt")
    rules_input, orders_input = get_rules_and_orders("j5/input.txt")
    # Part 1
    assert get_sum_of_middle_page_number(rules_exemple, orders_exemple) == 143
    print(get_sum_of_middle_page_number(rules_input, orders_input))
    # Part 2
    assert get_sum_of_middle_page_number_by_reordering(rules_exemple, orders_exemple) == 123
    print(get_sum_of_middle_page_number_by_reordering(rules_input, orders_input))


if __name__ == "__main__":
    main()
