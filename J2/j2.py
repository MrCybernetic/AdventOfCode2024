def get_reports(path: str) -> list:
    reports = {}
    with open(path, "r") as f:
        reports = f.readlines()
    return reports


def get_number_of_safe_reports(reports_list: list) -> int:
    total_safe_reports = len(reports_list)
    for report in reports_list:
        if is_report_bad(report):
            total_safe_reports -= 1
    return total_safe_reports


def is_report_bad(report: list) -> bool:
    levels = report.split()
    is_increasing = False
    is_decreasing = False
    for index, _ in enumerate(levels):
        if index != 0:
            if (int(levels[index])-int(levels[index-1]) > 0):
                is_increasing = True
            elif (int(levels[index])-int(levels[index-1]) < 0):
                is_decreasing = True
            else:
                return True
            if is_increasing and is_decreasing:
                return True
            if (abs(int(levels[index])-int(levels[index-1])) > 3):
                return True
    return False


def is_report_bad_tolerating_a_single_bad_level(report: list) -> bool:
    if not (is_report_bad(report)):
        return False
    else:
        for index, _ in enumerate(report):
            report_copy = report.split()
            if (index < len(report_copy)):
                report_copy.pop(index)
                if not (is_report_bad(" ".join(report_copy))):
                    return False
        return True


def get_number_of_safe_reports_tolerating_a_single_bad_level(reports_list: list) -> int:
    total_safe_reports = len(reports_list)
    for report in reports_list:
        if is_report_bad_tolerating_a_single_bad_level(report):
            total_safe_reports -= 1
    return total_safe_reports


def main() -> None:
    list_of_reports_exemple = get_reports("j2/test.txt")
    list_of_reports_input = get_reports("j2/input.txt")
    # Part 1
    assert get_number_of_safe_reports(list_of_reports_exemple) == 2
    print(get_number_of_safe_reports(list_of_reports_input))
    # Part 2
    assert get_number_of_safe_reports_tolerating_a_single_bad_level(list_of_reports_exemple) == 4
    print(get_number_of_safe_reports_tolerating_a_single_bad_level(list_of_reports_input))


if __name__ == "__main__":
    main()
