import re


def day2(filename):
    m1 = {}
    m2 = {}
    with open(filename) as f:
        data = f.read().splitlines()
        for d in data:
            res = re.split("\s+", d)
            i1 = int(res[0])
            i2 = int(res[1])

            if i1 in m1:
                m1[i1] = m1[i1] + 1
            else:
                m1[i1] = 1

            if i2 in m2:
                m2[i2] = m2[i2] + 1
            else:
                m2[i2] = 1

    score = 0
    for k1 in m1.keys():
        if k1 in m2:
            score += k1 * m2[k1]

    return score


if __name__ == "__main__":
    print(day2("./aoc/aoc_data/distances.txt"))
