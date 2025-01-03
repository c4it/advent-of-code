#!/usr/bin/env python

from collections import defaultdict
from functools import cache
from aocd import data


def first(a):
    b = a * 64
    a = mix(a, b)
    return prune(a)


def second(a):
    b = a // 32
    a = mix(a, b)
    return prune(a)


def third(a):
    b = a * 2048
    a = mix(a, b)
    return prune(a)


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def p1(d):
    total = 0
    for a in d:
        for _ in range(2000):
            a = first(a)
            a = second(a)
            a = third(a)
        total += a
    return total


def calc_changes(x: list[int]):
    y = []
    for i in range(1, len(x)):
        y.append(x[i] - x[i - 1])
    return y


def sequences(x: list[int], x_change):
    seq = {}
    for i in range(len(x_change) - 3):
        t = (x_change[i], x_change[i + 1], x_change[i + 2], x_change[i + 3])
        if t == (-1, -1, 0, 2):
            print
        if t not in seq:
            seq[t] = x[i + 4]
    return seq


def merge_dicts(d1, d2):
    for k, v in d2.items():
        if k in d1:
            d1[k].append(v)
        else:
            d1[k] = [v]


def p2(d):
    secret_numbers_by_seed = defaultdict(list)
    for k in d:
        a = k
        for _ in range(2000):
            a = first(a)
            a = second(a)
            a = third(a)
            secret_numbers_by_seed[k].append(a % 10)

    first_occ_of_seqs = defaultdict(list)
    for k, v in secret_numbers_by_seed.items():
        changes = calc_changes(v)
        seq = sequences(v, changes)
        merge_dicts(first_occ_of_seqs, seq)

    max_sum = 0
    max_seq = None
    max_nums = None
    for k, v in first_occ_of_seqs.items():
        h = sum(v)
        if h > max_sum:
            max_sum = h
            max_seq = k
            max_nums = v
    return max_sum, max_seq, max_nums


def parse_data(d):
    return [int(x) for x in d.splitlines()]


data = parse_data(data)

print(f"p1 ans: {p1(data)}")
print(f"p2 ans: {p2(data)}")
