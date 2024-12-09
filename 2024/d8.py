#!/usr/bin/env python

from aocd import data


def should_add(r_bound, c_bound, r, c):
    return (0 <= r < r_bound) and (0 <= c < c_bound)


def find_antinodes(ar, ac, freq, d, nodes: set):
    for r in range(len(d)):
        for c in range(len(d[0])):
            if (r, c) == (ar, ac):
                continue
            if d[r][c] == freq:
                rdist = ar - r
                cdist = ac - c
                if should_add(len(d), len(d[0]), ar + rdist, ac + cdist):
                    nodes.add((ar + rdist, ac + cdist))
                if should_add(len(d), len(d[0]), r - rdist, c - cdist):
                    nodes.add((r - rdist, c - cdist))


def find_antinodes_p2(ar, ac, freq, d, nodes: set):
    for r in range(len(d)):
        for c in range(len(d[0])):
            if (r, c) == (ar, ac):
                continue
            if d[r][c] == freq:
                nodes.add((r, c))
                rdist = ar - r
                cdist = ac - c
                while should_add(len(d), len(d[0]), ar + rdist, ac + cdist):
                    nodes.add((ar + rdist, ac + cdist))
                    rdist += ar - r
                    cdist += ac - c
                rdist = ar - r
                cdist = ac - c
                while should_add(len(d), len(d[0]), r - rdist, c - cdist):
                    nodes.add((r - rdist, c - cdist))
                    rdist -= ar - r
                    cdist -= ac - c


def p1(d):
    nodes = set()
    for r in range(len(d)):
        for c in range(len(d[0])):
            if d[r][c] not in {"."}:
                find_antinodes(r, c, d[r][c], d, nodes)
    return nodes


def p2(d):
    nodes = set()
    for r in range(len(d)):
        for c in range(len(d[0])):
            if d[r][c] not in {"."}:
                find_antinodes_p2(r, c, d[r][c], d, nodes)
    return nodes


def vis(d, nodes):
    for node in nodes:
        node = list(node)
        if d[node[0]][node[1]] == ".":
            d[node[0]][node[1]] = "#"
    for i in d:
        print("".join(i))


nodes_p1 = p1(data.splitlines())
nodes_p2 = p2(data.splitlines())
vis([list(d) for d in data.splitlines()], nodes_p1)
print()
vis([list(d) for d in data.splitlines()], nodes_p2)
print()
print(f"p1 ans: {len(nodes_p1)}")
print(f"p2 ans: {len(nodes_p2)}")

# Improvements:
# Instead of looping through `d` twice:
# Find position of all antennas first and loop through:  e.g. [(1,1,A), (2,2,A)]
# For each antenna find all antennas of the same frequency and apply the same logic
# to find the anti nodes
