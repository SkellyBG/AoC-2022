#!/bin/python3
import re
import functools
from collections import deque


dirs = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

def nums(line) -> list:
    return [int(x) for x in line if x.strip()]


def bfs_is_empty(x, y, z, matrix) -> bool:
    highest = len(matrix)
    visited = [[[False for _ in range(0, highest)] for _ in range(0, highest)] for _ in range(0, highest)]
    queue = deque()
    queue.append((x, y, z))
    visited[x][y][z] = True

    while len(queue) != 0:
        x, y, z = queue.pop()
        for dir in dirs:
            new_x = x + dir[0]
            new_y = y + dir[1]
            new_z = z + dir[2]
            if new_x >= len(matrix) or new_x < 0 or new_y >= len(matrix) or new_y < 0 or new_z >= len(matrix) or new_z < 0:
                return True
            if matrix[new_x][new_y][new_z]:
                continue
            if not visited[new_x][new_y][new_z]:
                queue.append((new_x, new_y, new_z))
                visited[new_x][new_y][new_z] = True
    return False

def bfs(x, y, z, matrix, visited) -> int:
    total = 0
    queue = deque()
    queue.append((x, y, z))
    visited[x][y][z] = True

    while len(queue) != 0:
        x, y, z = queue.pop()
        local = 6
        for dir in dirs:
            new_x = x + dir[0]
            new_y = y + dir[1]
            new_z = z + dir[2]
            if new_x >= len(matrix) or new_x < 0 or new_y >= len(matrix) or new_y < 0 or new_z >= len(matrix) or new_z < 0:
                continue
            # if not matrix[new_x][new_y][new_z]: # part 1
            #     continue
            if not matrix[new_x][new_y][new_z] and bfs_is_empty(new_x, new_y, new_z, matrix): # part 2
                continue
            local -= 1
            if not visited[new_x][new_y][new_z] and matrix[new_x][new_y][new_z]:
                queue.append((new_x, new_y, new_z))
                visited[new_x][new_y][new_z] = True
        total += local
    return total

def part1() -> None:
    f = open("input.txt", "r")
    highest = 0
    coords = []
    for line in f:
        coord = tuple(nums(line.split(",")))
        coords.append(coord)
        highest = max(highest, max(coord))
    highest += 1
    matrix = [[[False for _ in range(0, highest)] for _ in range(0, highest)] for _ in range(0, highest)]
    visited = [[[False for _ in range(0, highest)] for _ in range(0, highest)] for _ in range(0, highest)]
    for (x, y, z) in coords:
        matrix[x][y][z] = True
    total = 0
    for (x, y, z) in coords:
        if not visited[x][y][z]:
            total += bfs(x, y, z, matrix, visited)
    print(total)

def part2() -> None:
    f = open("test.txt", "r")
    highest = 0
    coords = []
    for line in f:
        coord = tuple(nums(line.split(",")))
        coords.append(coord)
        highest = max(highest, max(coord))
    highest += 1
    matrix = [[[False for _ in range(0, highest)] for _ in range(0, highest)] for _ in range(0, highest)]
    visited = [[[False for _ in range(0, highest)] for _ in range(0, highest)] for _ in range(0, highest)]
    for (x, y, z) in coords:
        matrix[x][y][z] = True
    total = 0
    for (x, y, z) in coords:
        if not visited[x][y][z]:
            total += bfs(x, y, z, matrix, visited)
    print(total)

part1()
part2()