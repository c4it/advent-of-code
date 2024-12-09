#!/usr/bin/env python

from aocd import data


def split_data(d):
    cd = []
    id = 0
    for ind, x in enumerate(d):
        # file
        if ind % 2 == 0:
            for _ in range(int(x)):
                cd.append(id)
            id += 1
        else:
            for _ in range(int(x)):
                cd.append(".")
    return cd


def shift_data(cd: list):
    free_space = cd.count(".")
    while free_space > 0:
        num = cd.pop()
        cd[cd.index(".")] = num
        free_space -= 1


def checksum(cd):
    total = 0
    for ind, x in enumerate(cd):
        if x != ".":
            total += ind * x
    return total


def split_data_blocks(d):
    cd = []
    id = 0
    for ind, x in enumerate(d):
        # file
        block = []
        if ind % 2 == 0:
            for _ in range(int(x)):
                block.append(id)
            id += 1
        else:
            for _ in range(int(x)):
                block.append(".")
        if block:
            cd.append(block)
    return cd


def merge(cd, ind):
    try:
        if cd[ind - 1][0] == ".":
            cd[ind - 1].extend(cd[ind])
            cd.pop(ind)
    except:
        pass
    try:
        if cd[ind + 1][0] == ".":
            cd[ind].extend(cd[ind + 1])
            cd.pop(ind + 1)
    except:
        pass


def split(cd, ind, block_len):
    old = cd[ind]
    cd[ind] = old[0:block_len]
    cd.insert(ind + 1, old[block_len:])


def swap(cd, ind1, ind2):
    if len(cd[ind1]) > len(cd[ind2]):
        split(cd, ind1, len(cd[ind2]))
    cd[ind1], cd[ind2] = cd[ind2], cd[ind1]
    merge(cd, ind2)


def shift_data_block(cd: list):
    cd_ind = -1
    while abs(cd_ind) < len(cd):
        block = cd[cd_ind]
        if block == [8, 8, 8, 8]:
            print
        if block[0] != ".":
            for ind in range(0, len(cd) + cd_ind):
                x = cd[ind]
                if x[0] == "." and len(block) <= len(x):
                    swap(cd, ind, cd_ind)
                    cd_ind += 1
                    break
        cd_ind -= 1


def p1(d):
    cd = split_data(d)
    print(cd)
    shift_data(cd)
    print(cd)
    return checksum(cd)


def p2(d):
    cd = split_data_blocks(d)
    print(cd)
    shift_data_block(cd)
    print(cd)
    cd2 = []
    for c in cd:
        for x in c:
            cd2.append(x)

    return checksum(cd2)


# file/free space alternating
# id starting at 0

print(f"p1 ans: {p1(data)}")
print(f"p2 ans: {p2(data)}")
