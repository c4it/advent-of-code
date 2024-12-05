#!/usr/bin/env python

test = ""
real = ""


def is_safe(row):
    prev = 0
    if sorted(row) != row and sorted(row, reverse=True) != row:
        return 0
    for ind in range(1, len(row)):
        diff = abs(row[prev] - row[ind])
        if diff == 0 or diff > 3:
            return 0
        prev = ind
    return 1


def p1():
    safe = 0
    for row in real.splitlines():
        row_int = [int(x) for x in row.split()]
        safe += is_safe(row_int)
    print(safe)


def p2():
    safe = 0
    for row in real.splitlines():
        row_int = [int(x) for x in row.split()]
        if is_safe(row_int) == 1:
            safe += 1
        else:
            for i in range(len(row_int)):
                row_test = row_int[0:i] + row_int[i + 1 :]
                if is_safe(row_test) == 1:
                    safe += 1
                    break
    print(safe)
