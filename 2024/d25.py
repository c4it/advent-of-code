#!/usr/bin/env python

from itertools import product
from aocd import data


def p1(locks, keys):
    fit = 0
    for lock, key in product(locks, keys):
        if not any(x + y > 5 for x, y in zip(lock, key)):
            fit += 1
    return fit


def transpose(x):
    return [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]


def parse_data(d):
    keys = []
    locks = []
    current = []
    is_lock = False
    is_key = False
    index = 0
    d = d.splitlines()
    while index <= len(d):
        line = d[index] if index < len(d) else ""
        if line == "":
            if set(current[0]) == {"#"}:
                is_lock = True
                is_key = False
                current.pop(0)
            else:
                is_key = True
                is_lock = False
                current.pop(-1)
            current_transpose = transpose(current)
            if is_lock:
                lock = ()
                for a in current_transpose:
                    lock += (a.count("#"),)
                locks.append(lock)
            elif is_key:
                key = ()
                for a in current_transpose:
                    key += (a.count("#"),)
                keys.append(key)
            is_lock = False
            is_key = False
            current = []
            index += 1
            continue

        current.append(list(line))
        index += 1
    return locks, keys


locks, keys = parse_data(data)

print(f"p1 ans: {p1(locks, keys)}")
