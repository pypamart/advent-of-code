from typing import List


def upload_reports(filepath: str) -> List[List[int]]:
    with open(filepath, "r") as f:
        lines = f.readlines()
    reports = [line.strip().split() for line in lines]
    reports = [list(map(int, report)) for report in reports]
    return reports

# Gérer le cas d'un report avec 1 seul élément
def is_all_increasing_report(report: List[int]):
    return report == sorted(report)


def is_all_decreasing_report(report: List[int]):
    return report == sorted(report, reverse=True)


def is_2_adjacents_levels_is_between_1_and_3(report: List[int]):
    for i in range(len(report) - 1):
        if not (1 <= abs(report[i] - report[i + 1]) <= 3):
            return False
    return True


def is_safe_report_v1(report: List[int]):
    return (
        is_all_increasing_report(report) or is_all_decreasing_report(report)
    ) and is_2_adjacents_levels_is_between_1_and_3(report)


def is_safe_report_v2(report: List[int]):
    for i in range(len(report)):
        sub_report = report[:i] + report[i + 1 :]
        if is_safe_report_v1(sub_report):
            return True

    return False


if __name__ == "__main__":
    reports = upload_reports("input.txt")

    nb_safe_reports_v1 = 0
    nb_safe_reports_v2 = 0
    for report in reports:
        nb_safe_reports_v1 += 1 if is_safe_report_v1(report) else 0
        nb_safe_reports_v2 += 1 if is_safe_report_v2(report) else 0

    print(nb_safe_reports_v1)
    print(nb_safe_reports_v2)