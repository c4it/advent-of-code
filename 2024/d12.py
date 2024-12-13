#!/usr/bin/env python

from aocd import data

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_block(r, c, d, block, vis):
    if vis[r][c]:
        return 0
    block.add((r, c))
    vis[r][c] = True

    perimeter = 0
    for dir in dirs:
        if (
            r + dir[0] >= 0
            and r + dir[0] < len(d)
            and c + dir[1] >= 0
            and c + dir[1] < len(d[0])
            and d[r + dir[0]][c + dir[1]] == d[r][c]
        ):
            perimeter += find_block(r + dir[0], c + dir[1], d, block, vis)
        else:
            perimeter += 1
    return perimeter


def find_block_p2(r, c, d, block, vis, perimeter):
    if vis[r][c]:
        return
    block.add((r, c))
    vis[r][c] = True

    for dir in dirs:
        if (
            r + dir[0] >= 0
            and r + dir[0] < len(d)
            and c + dir[1] >= 0
            and c + dir[1] < len(d[0])
            and d[r + dir[0]][c + dir[1]] == d[r][c]
        ):
            find_block_p2(r + dir[0], c + dir[1], d, block, vis, perimeter)
        else:
            perimeter.append((r + dir[0], c + dir[1]))
    return


def p1(d):
    blocks = []
    perimeters = []
    vis = []
    for _ in range(len(d)):
        vis.append([False for _ in range(len(d[0]))])
    for r in range(len(d)):
        for c in range(len(d[0])):
            block = set()
            if not vis[r][c]:
                per = find_block(r, c, d, block, vis)
                blocks.append(block)
                perimeters.append(per)
    total = 0
    for b, p in zip(blocks, perimeters):
        total += len(b) * p
    return total


def find_corners_from_block(block, d):
    corners = 0
    for r, c in block:
        # check the corner and the two sides of the perimeter it touches for each corner type
        #  _ _
        # |   | |_ _|
        corner_types = [
            [(-1, -1), (0, -1), (-1, 0)],
            [(-1, 1), (0, 1), (-1, 0)],
            [(1, -1), (0, -1), (1, 0)],
            [(1, 1), (0, 1), (1, 0)],
        ]
        for p, p1, p2 in corner_types:
            point_out_of_block = (
                r + p[0] < 0
                or r + p[0] >= len(d)
                or c + p[1] < 0
                or c + p[1] >= len(d[0])
            ) or (r + p[0], c + p[1]) not in block
            perimeter1_out_of_block = (
                r + p1[0] < 0
                or r + p1[0] >= len(d)
                or c + p1[1] < 0
                or c + p1[1] >= len(d[0])
            ) or (r + p1[0], c + p1[1]) not in block
            perimeter2_out_of_block = (
                r + p2[0] < 0
                or r + p2[0] >= len(d)
                or c + p2[1] < 0
                or c + p2[1] >= len(d[0])
            ) or (r + p2[0], c + p2[1]) not in block
            if (
                point_out_of_block
                and perimeter1_out_of_block
                and perimeter2_out_of_block
            ):
                corners += 1
            elif point_out_of_block and not (
                perimeter1_out_of_block or perimeter2_out_of_block
            ):
                corners += 1
            # inside corner
            elif (
                not point_out_of_block
                and perimeter1_out_of_block
                and perimeter2_out_of_block
            ):
                corners += 1
    return corners


def p2(d):
    block_chars = []
    blocks = []
    block_pers = []
    vis = []
    for _ in range(len(d)):
        vis.append([False for _ in range(len(d[0]))])
    for r in range(len(d)):
        for c in range(len(d[0])):
            block = set()
            perimeter = []
            if not vis[r][c]:
                find_block_p2(r, c, d, block, vis, perimeter)
                blocks.append(block)
                block_chars.append(d[r][c])
                block_pers.append(perimeter)
    total = 0

    for _a, b in zip(block_chars, blocks):
        total += len(b) * find_corners_from_block(b, d)
    return total


data = data.splitlines()

print(f"p1 ans: {p1(data)}")
print(f"p2 ans: {p2(data)}")
