#!/bin/python3
import re

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def nums(line) -> list:
    return [int(x) for x in line if x.strip()]

def part1():
    f = open("input.txt", "r")
    matrix = []
    starting_row = 0
    starting_col = 0
    end_row = 0
    end_col = 0
    for i, line in enumerate(f):
        row = []
        for j, c in enumerate(line.strip()):
            if c.islower():
                row.append(ord(c) - ord("a"))
            elif c == "S":
                row.append(ord("a") - ord("a"))
                starting_row = i
                starting_col = j
            elif c == "E":
                row.append(ord("z") - ord("a"))
                end_row = i
                end_col = j
        matrix.append(row)
    
    visited = [[False for _ in matrix[0]] for _ in matrix]
    visited[starting_row][starting_col] = True
    
    queue = []
    step = 0
    queue.append((starting_row, starting_col))
    while len(queue) > 0:
        size = len(queue)
        for _ in range(0, size):
            cur_row, cur_col = queue.pop(0)
            if cur_row == end_row and cur_col == end_col:
                print(step)
                break
            for dir in dirs:
                next_row = cur_row + dir[0]
                next_col = cur_col + dir[1]
                if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]) or visited[next_row][next_col] or matrix[next_row][next_col] > matrix[cur_row][cur_col] + 1:
                    continue
                queue.append((next_row, next_col))
                visited[next_row][next_col] = True
        step += 1        


def part2():
    f = open("input.txt", "r")
    matrix = []
    starting_row = 0
    starting_col = 0
    end_row = 0
    end_col = 0
    for i, line in enumerate(f):
        row = []
        for j, c in enumerate(line.strip()):
            if c.islower():
                row.append(ord(c) - ord("a"))
            elif c == "S":
                row.append(ord("a") - ord("a"))
                starting_row = i
                starting_col = j
            elif c == "E":
                row.append(ord("z") - ord("a"))
                end_row = i
                end_col = j
        matrix.append(row)
    
    best = 10000000
    
    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            if c == 0:
                starting_row = i
                starting_col = j
                queue = []
                step = 0
                visited = [[False for _ in matrix[0]] for _ in matrix]
                visited[starting_row][starting_col] = True
                queue.append((starting_row, starting_col))
                while len(queue) > 0:
                    size = len(queue)
                    for _ in range(0, size):
                        cur_row, cur_col = queue.pop(0)
                        if cur_row == end_row and cur_col == end_col:
                            best = min(best, step)
                            break
                        for dir in dirs:
                            next_row = cur_row + dir[0]
                            next_col = cur_col + dir[1]
                            if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]) or visited[next_row][next_col] or matrix[next_row][next_col] > matrix[cur_row][cur_col] + 1:
                                continue
                            queue.append((next_row, next_col))
                            visited[next_row][next_col] = True
                    step += 1     
    print(best)   

part1()
part2()