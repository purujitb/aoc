import heapq
import re


def day1(filename):
    l1 = []
    l2 = []
    with open(filename) as f:
        data = f.read().splitlines()
        for d in data:
            res = re.split("\s+", d)
            heapq.heappush(l1, int(res[0]))
            heapq.heappush(l2, int(res[1]))

    dist = 0
    for _ in range(len(l1)):
        i1 = heapq.heappop(l1)
        i2 = heapq.heappop(l2)
        dist += abs(i1 - i2)

    return dist


if __name__ == "__main__":
    print(day1("./aoc/aoc_data/distances.txt"))
