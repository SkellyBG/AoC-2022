#!/bin/python3
import re

def nums(line) -> list:
    return [int(x) for x in line if x.strip()]

def part1():
    f = open("input.txt", "r")
    matrix = []
    for line in f:
        row = []
        for i, c in enumerate(line.strip()):
            row.append(int(c))
        matrix.append(row)
    count = 0

    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            visible = False
            local_visible = True
            for k in range(0, i):
                if matrix[k][j] >= c:
                    local_visible = False
            visible = visible or local_visible
            local_visible = True
            for k in range(i + 1, len(row)):
                if matrix[k][j] >= c:
                    local_visible = False
            visible = visible or local_visible
            local_visible = True
            for k in range(0, j):
                if matrix[i][k] >= c:
                    local_visible = False
            visible = visible or local_visible
            local_visible = True
            for k in range(j + 1, len(row)):
                if matrix[i][k] >= c:
                    local_visible = False
            visible = visible or local_visible

            if visible:
                # print(str(i) + " " + str(j))
                count += 1
    print(count)



def part2():
    f = open("input.txt", "r")
    matrix = []
    for line in f:
        row = []
        for i, c in enumerate(line.strip()):
            row.append(int(c))
        matrix.append(row)
    best = 0

    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            localBest = 1
            count = 0
            for k in range(i - 1, -1, -1):
                count += 1
                if matrix[k][j] >= c:
                    break
            localBest *= count
            count = 0
            for k in range(i + 1, len(row)):
                count += 1
                if matrix[k][j] >= c:
                    break
            localBest *= count
            count = 0
            for k in range(j - 1, -1, -1):
                count += 1
                if matrix[i][k] >= c:
                    break
            localBest *= count
            count = 0
            for k in range(j + 1, len(row)):
                count += 1
                if matrix[i][k] >= c:
                    break
            localBest *= count
            # print(str(i) + " " + str(j) + " " + str(localBest))
            best = max(best, localBest)
    print(best)

part1()
part2()