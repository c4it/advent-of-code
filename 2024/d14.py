#!/usr/bin/env python

from dataclasses import dataclass
from aocd import data
import re
from PIL import Image


@dataclass
class Postion:
    x: int  # from left wall
    y: int  # from top wall


@dataclass
class Velocity:
    x: int  # horizontal velocity
    y: int  # vertical velocity


@dataclass
class Robot:
    position: Postion
    velocity: Velocity


def get_safety_factor(robots, width, height):
    mid_width = width // 2
    mid_height = height // 2
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        # robots in middle dont count
        if robot.position.x == mid_width or robot.position.y == mid_height:
            continue

        if robot.position.x < mid_width and robot.position.y < mid_height:
            quadrants[0] += 1
        elif robot.position.x < mid_width and robot.position.y > mid_height:
            quadrants[2] += 1
        elif robot.position.x > mid_width and robot.position.y < mid_height:
            quadrants[1] += 1
        elif robot.position.x > mid_width and robot.position.y > mid_height:
            quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def move_robot(robot, width, height):
    robot.position.x = (robot.position.x + robot.velocity.x) % width
    robot.position.y = (robot.position.y + robot.velocity.y) % height


def vis(robots, width, height, it):
    space = []
    for _ in range(height):
        space.append([0 for _ in range(width)])

    for robot in robots:
        space[robot.position.y][robot.position.x] = 255

    im_bytes = bytearray([val for row in space for val in row])
    im = Image.frombytes(mode="L", size=(width, height), data=im_bytes)
    im.save(f"2024/test/{it+1}.png")


def p1(d, width, height):
    robots = parse_data(d)
    for _ in range(100):
        for robot in robots:
            move_robot(robot, width, height)
    return get_safety_factor(robots, width, height)


def p2(d, width, height):
    robots = parse_data(d)
    vis(robots, width, height, 0)
    for it in range(10000):
        for robot in robots:
            move_robot(robot, width, height)
        vis(robots, width, height, it)


def parse_data(d):
    robots = []
    for line in d:
        p, v = line.split()
        pos = re.findall(r"p=([-]{0,1}\d+),([-]{0,1}\d+)", p)[0]
        vel = re.findall(r"v=([-]{0,1}\d+),([-]{0,1}\d+)", v)[0]
        robots.append(
            Robot(
                position=Postion(x=int(pos[0]), y=int(pos[1])),
                velocity=Velocity(x=int(vel[0]), y=int(vel[1])),
            )
        )
    return robots


width, height = 101, 103
data = data.splitlines()

print(f"p1 ans: {p1(data, width, height)}")
print(f"p2 ans: {p2(data, width, height)}")
