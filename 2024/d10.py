#!/usr/bin/env python

from aocd import data


def find_nines(r, c, nines, d):
    if d[r][c] == 9:
        nines.add((r, c))
        return 1

    count = 0
    if r + 1 < len(d) and d[r + 1][c] == d[r][c] + 1:
        count += find_nines(r + 1, c, nines, d)
    if r - 1 >= 0 and d[r - 1][c] == d[r][c] + 1:
        count += find_nines(r - 1, c, nines, d)
    if c + 1 < len(d[0]) and d[r][c + 1] == d[r][c] + 1:
        count += find_nines(r, c + 1, nines, d)
    if c - 1 >= 0 and d[r][c - 1] == d[r][c] + 1:
        count += find_nines(r, c - 1, nines, d)

    return count


def p1(d):
    nines = []
    for r in range(len(d)):
        for c in range(len(d[0])):
            if d[r][c] == 0:
                nine_count = set()
                find_nines(r, c, nine_count, d)
                nines.append(nine_count)
    return sum(len(x) for x in nines)


def p2(d):
    nines = []
    paths = 0
    for r in range(len(d)):
        for c in range(len(d[0])):
            if d[r][c] == 0:
                nine_count = set()
                paths += find_nines(r, c, nine_count, d)
                nines.append(nine_count)
    return sum(len(x) for x in nines), paths


data = data.splitlines()
data = [list(int(x) for x in y) for y in data]

print(f"p1 ans: {p1(data)}")
print(f"p2 ans: {p2(data)}")
