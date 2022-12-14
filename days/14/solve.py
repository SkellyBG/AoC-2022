#!/bin/python3
import re
import functools

dirs = [[0, 1], [-1, 1] , [1, 1]]

def nums(line) -> list:
    return [int(x) for x in line if x.strip()]

def part1() -> None:
    f = open("input.txt", "r")  
    min_x = 500
    max_x = 500
    max_y = 0
    paths = []
    for line in f:
        line = [(int(i.split(",")[0]), int(i.split(",")[1])) for i in re.split(r" -> ", line.strip())]
        paths.append(line)
        for x, y in line:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    matrix = [["." for _ in range(min_x, max_x + 1)] for _ in range(0, max_y + 1)]
    for path in paths:
        prev_x, prev_y = path[0]
        for cur_x, cur_y in path:
            if prev_x == cur_x:
                for i in range(min(prev_y, cur_y), max(prev_y, cur_y) + 1):
                    matrix[i][cur_x - min_x] = '#'
            else:
                for i in range(min(prev_x, cur_x), max(prev_x, cur_x) + 1):
                    matrix[cur_y][i - min_x] = '#'
            prev_x, prev_y = cur_x, cur_y
    # [print(line) for line in matrix]

    count = 0
    outer_flag = True
    while outer_flag:
        inner_flag = True
        cur_x = 500
        cur_y = 0
        while inner_flag:
            inner_flag = False
            for dir in dirs:
                new_x = cur_x + dir[0]
                new_y = cur_y + dir[1]
                if new_x - min_x < 0 or new_x - min_x >= len(matrix[0]) or new_y >= len(matrix):
                    outer_flag = False
                    break
                if matrix[new_y][new_x - min_x] == '.':
                    cur_x = new_x
                    cur_y = new_y
                    inner_flag = True
                    break
            if not inner_flag:
                matrix[cur_y][cur_x - min_x] = 'o'
        count += 1
    print(count - 1)
        

def part2() -> None:
    f = open("test.txt", "r")  
    min_x = 500
    max_x = 500
    max_y = 0
    paths = []
    for line in f:
        line = [(int(i.split(",")[0]), int(i.split(",")[1])) for i in re.split(r" -> ", line.strip())]
        paths.append(line)
        for x, y in line:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    matrix = [["." for _ in range(min_x, max_x + 1)] for _ in range(0, max_y + 2)]
    matrix.append(["#" for _ in range(min_x, max_x + 1)])
    for path in paths:
        prev_x, prev_y = path[0]
        for cur_x, cur_y in path:
            if prev_x == cur_x:
                for i in range(min(prev_y, cur_y), max(prev_y, cur_y) + 1):
                    matrix[i][cur_x - min_x] = '#'
            else:
                for i in range(min(prev_x, cur_x), max(prev_x, cur_x) + 1):
                    matrix[cur_y][i - min_x] = '#'
            prev_x, prev_y = cur_x, cur_y
    # [print(line) for line in matrix]

    count = 0
    outer_flag = True
    while outer_flag:
        inner_flag = True
        cur_x = 500
        cur_y = 0
        while inner_flag:
            inner_flag = False
            for dir in dirs:
                new_x = cur_x + dir[0]
                new_y = cur_y + dir[1]
                if new_x - min_x < 0 or new_x - min_x >= len(matrix[0]):
                    [line.insert(0, ".") for line in matrix[:-1]]
                    [line.append(".") for line in matrix[:-1]]
                    matrix[max_y + 2].insert(0, "#")
                    matrix[max_y + 2].append("#")
                    min_x -= 1
                if matrix[new_y][new_x - min_x] == '.':
                    cur_x = new_x
                    cur_y = new_y
                    inner_flag = True
                    break
            if not inner_flag:
                matrix[cur_y][cur_x - min_x] = 'o'
                if cur_x == 500 and cur_y == 0:
                    outer_flag = False
        count += 1
    print(count)
    # for line in matrix:
    #     [print(i, end="") for i in line]
    #     print()

part1()
part2()