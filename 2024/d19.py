#!/usr/bin/env python

from functools import cache
from aocd import data


def parse_data(d):
    d = d.splitlines()
    patterns = d.pop(0).split(", ")
    # blank line
    d.pop(0)
    return d, set(patterns)


designs, patterns = parse_data(data)


@cache
def design_possible(design):
    if design == "":
        return 1
    count = 0
    for ind in range(1, len(design) + 1):
        if design[:ind] in patterns:
            count += design_possible(design[ind:])
    return count


def p1(designs):
    possible = 0
    for design in designs:
        if design_possible(design) > 0:
            possible += 1
    return possible


def p2(designs):
    possible = 0
    for design in designs:
        possible += design_possible(design)
    return possible


print(f"p1 ans: {p1(designs)}")
print(f"p2 ans: {p2(designs)}")
