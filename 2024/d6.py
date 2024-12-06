#!/usr/bin/env python

import copy


test = ""
real = ""


def find_start(test):
    for r in range(len(test)):
        for c in range(len(test[0])):
            if test[r][c] == "^":
                return r, c


def p1(test):
    rows = len(test)
    cols = len(test[0])
    facing = "up"

    r, c = find_start(test)
    test[r][c] = "X"
    while True:
        if facing == "up":
            if test[r - 1][c] != "#":
                r -= 1
                test[r][c] = "X"
            else:
                facing = "right"
        elif facing == "right":
            if test[r][c + 1] != "#":
                c += 1
                test[r][c] = "X"
            else:
                facing = "down"
        elif facing == "down":
            if test[r + 1][c] != "#":
                r += 1
                test[r][c] = "X"
            else:
                facing = "left"
        elif facing == "left":
            if test[r][c - 1] != "#":
                c -= 1
                test[r][c] = "X"
            else:
                facing = "up"
        if r + 1 >= rows or c + 1 >= cols or r - 1 < 0 or c - 1 < 0:
            return


def p1_loop(test):
    rows = len(test)
    cols = len(test[0])
    facing = "up"

    r, c = find_start(test)
    visited = {(r, c, facing)}
    test[r][c] = "X"
    while True:
        if facing == "up":
            if test[r - 1][c] != "#":
                r -= 1
                test[r][c] = "X"
            else:
                facing = "right"
        elif facing == "right":
            if test[r][c + 1] != "#":
                c += 1
                test[r][c] = "X"
            else:
                facing = "down"
        elif facing == "down":
            if test[r + 1][c] != "#":
                r += 1
                test[r][c] = "X"
            else:
                facing = "left"
        elif facing == "left":
            if test[r][c - 1] != "#":
                c -= 1
                test[r][c] = "X"
            else:
                facing = "up"
        if r + 1 >= rows or c + 1 >= cols or r - 1 < 0 or c - 1 < 0:
            return False
        if (r, c, facing) in visited:
            return True
        visited.add((r, c, facing))


def p2(test):
    rows = len(test)
    cols = len(test[0])
    obstacles = set()
    r_, c_ = find_start(test)
    for r in range(rows):
        for c in range(cols):
            test_copy = copy.deepcopy(test)
            if r_ != r or c_ != c:
                test_copy[r][c] = "#"
                if p1_loop(test_copy):
                    obstacles.add((r, c))

    return obstacles


# testl = []
# for t in real.splitlines():
#     testl.append(list(t))

# # p1(testl)
# # count = 0
# # for a in testl:
# #     for x in a:
# #         if x == "X":
# #             count += 1
# # print(f"ans: {count}")

# obst = p2(testl)
# print("ans: ", obst)
# print("ans: ", len(obst))
