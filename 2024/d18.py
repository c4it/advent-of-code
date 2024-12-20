#!/usr/bin/env python

from collections import defaultdict
from dataclasses import dataclass
import math
from aocd import data

START = (0, 0)
BYTES = 1024
EXIT = (70, 70)


@dataclass(frozen=True)
class Vertex:
    x: int
    y: int


class Graph:
    vertices: set[Vertex]
    start: Vertex
    end: Vertex

    def __init__(self, d: list[tuple[int]], bytes) -> None:
        self.vertices = set()
        for x in range(EXIT[0] + 1):
            for y in range(EXIT[1] + 1):
                if (x, y) not in d[0:bytes]:
                    vert = Vertex(x=x, y=y)
                    self.vertices.add(vert)
                    if (x, y) == START:
                        self.start = vert
                    elif (x, y) == EXIT:
                        self.end = vert


def get_neighbours(u: Vertex, g: Graph) -> list[Vertex]:
    neighbours = []
    for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        neighbour = Vertex(x=u.x + dir[0], y=u.y + dir[1])
        if neighbour in g.vertices:
            neighbours.append(neighbour)
    return neighbours


def shortest_path(graph: Graph):
    dist = defaultdict()
    prev = defaultdict()
    q = []
    for vert in graph.vertices:
        dist[vert] = math.inf
        prev[vert] = None
        q.append(vert)
    dist[graph.start] = 0

    while q:
        u = min(q, key=lambda v: dist[v])
        q.remove(u)
        neighbours = get_neighbours(u, graph)
        for v in neighbours:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist[graph.end]


def parse_date(d):
    d = d.splitlines()
    d = [tuple(int(y) for y in x.split(",")) for x in d]
    return d


def p1(d):
    return shortest_path(Graph(d, BYTES))


def p2(d):
    inf_byte = None
    max_bytes = len(d)
    min_bytes = BYTES
    byte = (max_bytes - min_bytes) // 2
    seen = set()
    while byte not in seen:
        path = shortest_path(Graph(d, byte))
        print(byte, path)
        seen.add(byte)
        if path == math.inf:
            inf_byte = d[byte - 1]
            max_bytes = byte
            byte = min_bytes + ((max_bytes - min_bytes) // 2)
        else:
            min_bytes = byte
            byte += (max_bytes - min_bytes) // 2

    return inf_byte


data = parse_date(data)

print(f"p1 ans: {p1(data)}")
print(f"p2 ans: {p2(data)}")
