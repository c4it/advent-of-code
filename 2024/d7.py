#!/usr/bin/env python

import itertools
from aocd import data

ops = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}

ops2 = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "||": lambda x, y: int(str(x) + str(y)),
}


def combo(digits, ans, ops):
    combos = itertools.product(ops.keys(), repeat=len(digits) - 1)
    for combo in combos:
        i = 1
        total = digits[0]
        for op in combo:
            total = ops[op](total, digits[i])
            i += 1
        if total == ans:
            return True
    return False


def p1(test):
    sums = []
    for line in test.splitlines():
        ans, digits = line.split(":")
        ans = int(ans)
        digits = [int(x) for x in digits.strip().split()]
        if combo(digits, ans, ops):
            sums.append(ans)
    return sum(sums)


def p2(test):
    sums = []
    for line in test.splitlines():
        ans, digits = line.split(":")
        ans = int(ans)
        digits = [int(x) for x in digits.strip().split()]
        if combo(digits, ans, ops2):
            sums.append(ans)
    return sum(sums)


print(f"p1 ans: {p1(data)}")
print(f"p2 ans: {p2(data)}")
