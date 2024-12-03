import re


def day3(filename):
    ret = 0
    go = True
    with open(filename) as f:
        data = f.read()
        result = re.findall("(mul\((\d{,3})\,(\d{,3})\))|(don't)|(do)", data)
        for r in result:
            if r[3] == "don't":
                go = False
            elif r[4] == "do":
                go = True
            elif go:
                ret += int(r[1]) * int(r[2])

    return ret


if __name__ == "__main__":
    print(day3("./aoc/aoc_data/memory.txt"))
