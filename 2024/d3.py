#!/usr/bin/env python

import re

test = ""
real = ""


def mul(x, y):
    return x * y


def p1(real2):
    matches = re.findall(r"mul\((\d+),(\d+)\)", real2)
    total = 0
    for match in matches:
        total += mul(int(match[0]), int(match[1]))
    return total


def p2(test):
    donts = test.split("don't()")
    total = p1(donts[0])
    donts.pop(0)
    while len(donts) > 0:
        dont = donts.pop(0)
        if "do()" in dont:
            dos = list(dont.partition("do()"))
            if dos:
                total += p1(dos[2])
    return total


def p2_improved(real):
    matches = re.findall(r"(do\(\))|(don't\(\))|(mul\(\d+,\d+\))", real)
    total = 0
    can_do = True
    for do, dont, mul in matches:
        if do:
            can_do = True
        elif dont:
            can_do = False
        elif mul and can_do:
            total += p1(mul)
    return total


print(p2_improved(real))
