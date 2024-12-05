#!/usr/bin/env python

from collections import defaultdict


def p1(page, updates):
    pg_dct = get_pg_dct(page)

    correct_updates_middles = []
    for u in updates.splitlines():
        u = u.split(",")
        is_correct = is_row_correct(pg_dct, u)
        if is_correct:
            correct_updates_middles.append(int(u[len(u) // 2]))
    return sum(correct_updates_middles)


def is_row_correct(pg_dct, u):
    for i in range(len(u) - 1):
        for j in range(i + 1, len(u)):
            if u[j] not in pg_dct[u[i]]:
                return False
    return True


def re_order(u, pg_dct):
    reordered_u = []
    valid_before_dict = {}
    for i in range(len(u)):
        valid_before_count = 0
        for j in range(len(u)):
            x = u[i]
            y = u[j]
            if x in pg_dct[y]:
                valid_before_count += 1
        valid_before_dict[u[i]] = valid_before_count

    reordered_u = sorted(u, key=valid_before_dict.get)
    return reordered_u


def p2(page, updates):
    pg_dct = get_pg_dct(page)

    correct_updates_middles = []
    for u in updates.splitlines():
        u = u.split(",")
        is_correct = is_row_correct(pg_dct, u)
        if not is_correct:
            u = re_order(u, pg_dct)
            correct_updates_middles.append(int(u[len(u) // 2]))
    return sum(correct_updates_middles)


def get_pg_dct(page):
    pg_dct = defaultdict(list)
    for p in page.splitlines():
        ps = p.split("|")
        pg_dct[ps[0]].append(ps[1])
    return pg_dct


# print("ans:", p1(test_page, test_update))
# print("ans:", p1(real_page, real_update))

# print("ans:", p2(test_page, test_update))
# print("ans:", p2(real_page, real_update))
