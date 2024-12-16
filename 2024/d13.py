#!/usr/bin/env python

from collections import defaultdict
from aocd import data
import re
from fractions import Fraction

move_cost = {"A": 3, "B": 1}


def get_cost(a: int, b: int):
    return (a * move_cost["A"]) + (b * move_cost["B"])


def p1(d):
    d = parse_data(d)
    return find_total_cost(d)


def p2(d):
    d = parse_data(d, True)
    return find_total_cost(d)


def find_total_cost(d):
    total_cost = 0
    for machine in d:
        x, y = machine["prize"]
        ax, ay = machine["A"]
        bx, by = machine["B"]
        b_times = (((x * ay) / ax) - y) / (((ay * bx) / ax) - (by))
        if b_times < 0 or b_times.denominator != 1:
            continue
        a_times = (x - (b_times * bx)) / ax
        if a_times < 0 or a_times.denominator != 1:
            continue
        total_cost += get_cost(a_times.numerator, b_times.numerator)
    return total_cost


def parse_data(d, p2=False):
    machines = []
    machine = defaultdict(Fraction)
    add = 0
    if p2:
        add = 10000000000000
    for line in d:
        if "Button" in line:
            line_splt = line.split(":")
            button = line_splt[0].split()[1]
            x_moves = re.findall(r"X\+(\d+)", line_splt[1])
            y_moves = re.findall(r"Y\+(\d+)", line_splt[1])
            machine[button] = (Fraction(x_moves[0]), Fraction(y_moves[0]))
        elif "Prize" in line:
            machine["prize"] = (
                Fraction(int(re.findall(r"X=(\d+)", line)[0]) + add),
                Fraction(int(re.findall(r"Y=(\d+)", line)[0]) + add),
            )
            machines.append(machine)
            machine = defaultdict(Fraction)
    return machines


data = data.splitlines()

print(f"p1 ans: {p1(data)}")
print(f"p2 ans: {p2(data)}")
