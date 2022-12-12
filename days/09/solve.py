#!/bin/python3
import re

dirs = {"L":[1, 0], "R":[-1, 0], "U":[0, 1], "D":[0, -1]}

def nums(line) -> list:
    return [int(x) for x in line if x.strip()]

def is_adjacent(head_row, head_col, tail_row, tail_col) -> bool:
    if tail_row < head_row - 1 or tail_row > head_row + 1 or tail_col > head_col + 1 or tail_col < head_col - 1:
        return False
    return True

def move_tail(head_row, head_col, tail_row, tail_col) -> tuple:
    if tail_row == head_row:
        tail_col += 1 if tail_col < head_col else -1
    elif tail_col == head_col:
        tail_row += 1 if tail_row < head_row else -1
    else:
        tail_col += 1 if tail_col < head_col else -1
        tail_row += 1 if tail_row < head_row else -1
    return tail_row, tail_col


def part1():
    f = open("input.txt", "r")
    head_row = 0
    head_col = 0
    tail_row = 0
    tail_col = 0
    visited = set([(0, 0)])
    for line in f:
        line = line.split()
        for _ in range(0, int(line[1])):
            head_row += dirs[line[0]][0]
            head_col += dirs[line[0]][1]
            if not is_adjacent(head_row, head_col, tail_row, tail_col):
                tail_row, tail_col = move_tail(head_row, head_col, tail_row, tail_col)
            visited.add((tail_row, tail_col))
    print(len(visited))
        


def part2():
    f = open("input.txt", "r")
    knots = [[0, 0] for _ in range(0, 10)]
    visited = set([(0, 0)])
    for line in f:
        line = line.split()
        for _ in range(0, int(line[1])):
            knots[0][0] += dirs[line[0]][0]
            knots[0][1] += dirs[line[0]][1]
            for j in range(1, 10):
                if not is_adjacent(knots[j - 1][0], knots[j - 1][1], knots[j][0], knots[j][1]):
                    knots[j][0], knots[j][1] = move_tail(knots[j - 1][0], knots[j - 1][1], knots[j][0], knots[j][1])
            visited.add((knots[9][0], knots[9][1]))  
    print(len(visited))

part1()
part2()