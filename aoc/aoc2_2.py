import re


def is_safe(report, max_fails=1):
    last_level = report[0]
    if report[0] > report[len(report) - 1]:
        direction_d = True
    elif report[0] < report[len(report) - 1]:
        direction_d = False
    else:
        return 0

    fail_count = 0
    for i in range(1, len(report)):
        curr_level = report[i]

        if (
            (direction_d and last_level < curr_level)
            or (not direction_d and last_level > curr_level)
            or abs(last_level - curr_level) > 3
            or abs(last_level - curr_level) == 0
        ):
            fail_count += 1
        else:
            last_level = curr_level

        if fail_count == max_fails:
            return 0

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
        sub_lists = []
        for i in range(1, len(report) - 1):
            sub_lists.append(report[0:i] + report[i + 1 : len(report)])
        sub_lists.append(report[1:])
        sub_lists.append(report[:-1])

        max_count = 0
        for sub_list in sub_lists:
            max_count = max(max_count, is_safe(sub_list))
        safe_count += max_count

    return safe_count


if __name__ == "__main__":
    print(day2("./aoc/aoc_data/reports.txt"))
