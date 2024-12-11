#!/usr/bin/env python

from collections import defaultdict
from functools import cache
from aocd import data


def p1(d: list, its):
    for it in range(its):
        i = 0
        while i < len(d):
            if d[i] == "0":
                d[i] = "1"
            elif len(d[i]) % 2 == 0:
                l = len(d[i]) // 2
                d_i_split_0, d_i_split_1 = d[i][0:l], str(int(d[i][l:]))
                d.pop(i)
                d.insert(i, d_i_split_0)
                i += 1
                d.insert(i, d_i_split_1)
            else:
                d[i] = str(int(d[i]) * 2024)
            i += 1


cache_stones = defaultdict(lambda: defaultdict(int))


def p2(d, it):
    if it == 0:
        cache_stones[d][it] = 1
        return 1
    if d in cache_stones:
        if it in cache_stones[d]:
            return cache_stones[d][it]
    if d == "0":
        ans = p2("1", it - 1)
        cache_stones[d][it] = ans
        return ans
    elif len(d) % 2 == 0:
        l = len(d) // 2
        ans = p2(d[0:l], it - 1) + p2(str(int(d[l:])), it - 1)
        cache_stones[d][it] = ans
        return ans
    else:
        ans = p2(str(int(d) * 2024), it - 1)
        cache_stones[d][it] = ans
        return ans


@cache
def p2_improved(d, it):
    if it == 0:
        return 1
    if d == 0:
        return p2_improved(1, it - 1)
    elif len(str(d)) % 2 == 0:
        str_d = str(d)
        l = len(str_d) // 2
        return p2_improved(int(str_d[0:l]), it - 1) + p2_improved(
            int(str_d[l:]), it - 1
        )
    else:
        return p2_improved(d * 2024, it - 1)


data2 = data.split()
p1(data2, 25)
print(f"p1 ans: {len(data2)}")

data = data.split()
stones = 0
for d in data:
    stones += p2(d, 75)
print(f"p2 ans: {stones}")

# probably could have transformed to ints earlier to avoid the str(int(d[i][l:]))
# also can make use of @cache from functools instead of dict
stones = 0
data = [int(x) for x in data]
for d in data:
    stones += p2_improved(d, 75)
print(f"p2 improved ans: {stones}")
