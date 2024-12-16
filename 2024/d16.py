#!/usr/bin/env python

from collections import defaultdict
from dataclasses import dataclass
import enum
import math
from aocd import data

START_TILE = "S"
END_TILE = "E"
WALL = "#"
ROTATE_POINTS = 1000
MOVE_FORWARD_POINT = 1


class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


@dataclass(frozen=True)
class Vertex:
    x: int
    y: int
    direction: Direction


class Graph:
    vertices: set[Vertex]
    start: Vertex
    end: set[Vertex]

    def __init__(self, d: list[str]):
        self.vertices = set()
        self.end = set()
        for r in range(len(d)):
            for c in range(len(d[0])):
                if d[r][c] != WALL:
                    for dir in Direction:
                        vert = Vertex(x=c, y=r, direction=dir)
                        self.vertices.add(vert)
                        if d[r][c] == START_TILE and vert.direction == Direction.EAST:
                            self.start = vert
                        elif d[r][c] == END_TILE:
                            self.end.add(vert)


def edges(u: Vertex, v: Vertex):
    if (
        u.x == v.x
        and u.y == v.y
        and v.direction == Direction((u.direction.value + 1) % 4)
    ):
        return ROTATE_POINTS
    elif (
        u.x == v.x
        and u.y == v.y
        and v.direction == Direction((u.direction.value - 1) % 4)
    ):
        return ROTATE_POINTS
    return MOVE_FORWARD_POINT


def get_neighbours(u: Vertex, g: Graph) -> list[Vertex]:
    neighbours = [
        Vertex(x=u.x, y=u.y, direction=Direction((u.direction.value + 1) % 4)),
        Vertex(x=u.x, y=u.y, direction=Direction((u.direction.value - 1) % 4)),
    ]
    match u.direction:
        case Direction.NORTH:
            neighbour = Vertex(x=u.x, y=u.y - 1, direction=Direction.NORTH)
        case Direction.EAST:
            neighbour = Vertex(x=u.x + 1, y=u.y, direction=Direction.EAST)
        case Direction.SOUTH:
            neighbour = Vertex(x=u.x, y=u.y + 1, direction=Direction.SOUTH)
        case Direction.WEST:
            neighbour = Vertex(x=u.x - 1, y=u.y, direction=Direction.WEST)
    if neighbour in g.vertices:
        neighbours.append(neighbour)
    return neighbours


def find_shortest_paths(graph: Graph, prev, dist, us, s_s):
    for u in us:
        if len(prev[u]) > 0 or u == graph.start:
            s_s.add((u.x, u.y))
            find_shortest_paths(graph, prev, dist, prev[u], s_s)


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
            alt = dist[u] + edges(u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    min_cost = math.inf
    for vert in graph.end:
        if dist[vert] < min_cost:
            min_cost = dist[vert]
    return min_cost


def shortest_path_p2(graph: Graph):
    dist = defaultdict()
    prev = defaultdict(set)
    q = []
    for vert in graph.vertices:
        dist[vert] = math.inf
        prev[vert] = set()
        q.append(vert)
    dist[graph.start] = 0

    while q:
        u = min(q, key=lambda v: dist[v])
        q.remove(u)
        neighbours = get_neighbours(u, graph)
        for v in neighbours:
            alt = dist[u] + edges(u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = {u}
            elif alt == dist[v]:
                prev[v].add(u)

    min_cost = math.inf
    for vert in graph.end:
        if dist[vert] < min_cost:
            min_cost = dist[vert]

    s_s = set()
    ends = set([end for end in graph.end if dist[end] == min_cost])
    find_shortest_paths(graph, prev, dist, ends, s_s)
    return min_cost, len(s_s)


def p1(d):
    graph = Graph(d)
    return shortest_path(graph)


def p2(d):
    graph = Graph(d)
    return shortest_path_p2(graph)


data = data.splitlines()

print(f"p1 ans: {p1(data)}")
print(f"p2 ans: {p2(data)}")
