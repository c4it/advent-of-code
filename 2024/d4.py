#!/usr/bin/env python

test = ""
real = ""


def p1(test):
    count = 0
    rows = len(test)
    cols = len(test[0])
    r = 0
    c = 0
    for r in range(rows):
        for c in range(cols):
            if test[r][c] == "X":
                # forward
                if r + 3 < rows:
                    if (
                        test[r + 1][c] == "M"
                        and test[r + 2][c] == "A"
                        and test[r + 3][c] == "S"
                    ):
                        count += 1
                if r - 3 > -1:
                    if (
                        test[r - 1][c] == "M"
                        and test[r - 2][c] == "A"
                        and test[r - 3][c] == "S"
                    ):
                        count += 1
                if c + 3 < cols:
                    if (
                        test[r][c + 1] == "M"
                        and test[r][c + 2] == "A"
                        and test[r][c + 3] == "S"
                    ):
                        count += 1
                if c - 3 > -1:
                    if (
                        test[r][c - 1] == "M"
                        and test[r][c - 2] == "A"
                        and test[r][c - 3] == "S"
                    ):
                        count += 1
                if (
                    r + 3 < rows
                    and c + 3 < cols
                    and test[r + 1][c + 1] == "M"
                    and test[r + 2][c + 2] == "A"
                    and test[r + 3][c + 3] == "S"
                ):
                    count += 1
                if (
                    r - 3 >= 0
                    and c - 3 >= 0
                    and test[r - 1][c - 1] == "M"
                    and test[r - 2][c - 2] == "A"
                    and test[r - 3][c - 3] == "S"
                ):
                    count += 1
                if (
                    r - 3 >= 0
                    and c + 3 < cols
                    and test[r - 1][c + 1] == "M"
                    and test[r - 2][c + 2] == "A"
                    and test[r - 3][c + 3] == "S"
                ):
                    count += 1
                if (
                    r + 3 < rows
                    and c - 3 >= 0
                    and test[r + 1][c - 1] == "M"
                    and test[r + 2][c - 2] == "A"
                    and test[r + 3][c - 3] == "S"
                ):
                    count += 1
    return count


def p2(test):
    count = 0
    rows = len(test)
    cols = len(test[0])
    r = 0
    c = 0
    for r in range(rows):
        for c in range(cols):
            if test[r][c] == "A":
                mas = 0
                if r - 1 >= 0 and c - 1 >= 0 and r + 1 < rows and c + 1 < cols:
                    if test[r - 1][c - 1] == "M" and test[r + 1][c + 1] == "S":
                        mas += 1
                    if test[r - 1][c - 1] == "S" and test[r + 1][c + 1] == "M":
                        mas += 1
                    if test[r - 1][c + 1] == "M" and test[r + 1][c - 1] == "S":
                        mas += 1
                    if test[r - 1][c + 1] == "S" and test[r + 1][c - 1] == "M":
                        mas += 1
                if mas == 2:
                    count += 1
    return count


# print("ans:", p1(real.splitlines()))
# print("ans:", p2(real.splitlines()))
