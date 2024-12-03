import re


def day3(filename):
    ret = 0
    with open(filename) as f:
        data = f.read()
        result = re.findall("mul\((\d{,3})\,(\d{,3})\)", data)
        for r in result:
            ret += int(r[0]) * int(r[1])

    return ret


if __name__ == "__main__":
    print(day3("./aoc/aoc_data/memory.txt"))
