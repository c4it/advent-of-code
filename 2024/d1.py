#!/usr/bin/env python

from collections import defaultdict

test = ""
real = ""


def load_data(data):
    a = []
    b = []
    for y in data.splitlines():
        left, right = y.split()
        a.append(int(left))
        b.append(int(right))
    return a, b


# p1
def p1(a, b):
    a.sort()
    b.sort()

    sums = 0
    for i in range(len(a)):
        sums += abs(a[i] - b[i])

    print(sums)


# p2
def p2(a, b):
    b_dict = defaultdict(int)
    for i in b:
        b_dict[i] += 1

    sums = 0
    for i in a:
        sums += i * b_dict.get(i, 0)
    print(sums)


a, b = load_data(test)
# p1(a, b)
# p2(a, b)
