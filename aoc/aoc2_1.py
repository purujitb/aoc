import re


def is_safe(report):
    last_level = report[0]
    if report[0] > report[len(report) - 1]:
        direction_d = True
    else:
        direction_d = False

    for i in range(1, len(report)):
        curr_level = report[i]

        if (direction_d and last_level < curr_level) or (
            not direction_d and last_level > curr_level
        ):
            return 0
        if abs(last_level - curr_level) > 3 or abs(last_level - curr_level) == 0:
            return 0

        last_level = curr_level

    return 1


def day2(filename):
    reports = []

    with open(filename) as f:
        data = f.read().splitlines()
        for d in data:
            res = re.split("\s+", d)
            levels = []
            for r in res:
                levels.append(int(r))
            reports.append(levels)

    safe_count = 0
    for report in reports:
        safe_count += is_safe(report)

    return safe_count


if __name__ == "__main__":
    print(day2("./aoc/aoc_data/reports.txt"))
