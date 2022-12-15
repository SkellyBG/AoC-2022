#!/bin/python3
import re
import functools

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def nums(line) -> list:
    return [int(x) for x in line if x.strip()]

def compute_distance(tuple) -> int:
    return abs(tuple[0][0] - tuple[1][0]) + abs(tuple[0][1] - tuple[1][1])

def mergeIntervals(intervals) -> list:
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] - 1 <= i[0] <= stack[-1][-1] + 1:
            stack[-1][0] = min(stack[-1][0], i[0])
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    return stack

def part1() -> None:
    row_query = 10

    f = open("test.txt", "r")
    inputs = []
    for line in f:
        match = re.fullmatch(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line.strip())
        inputs.append(((int(match.group(1)), int(match.group(2))), (int(match.group(3)), int(match.group(4)))))

    intervals = []

    for input in inputs:
        dist = compute_distance(input)
        if input[0][1] < row_query and input[0][1] + dist >= row_query:
            factor = input[0][1] + dist - row_query
        elif input[0][1] > row_query and input[0][1] - dist <= row_query:
            factor = row_query - (input[0][1] - dist)
        else:
            continue
        intervals.append([input[0][0] - factor, input[0][0] + factor])
    print(mergeIntervals(intervals))


def part2() -> None:
    f = open("input.txt", "r")
    inputs = []
    for line in f:
        match = re.fullmatch(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line.strip())
        inputs.append(((int(match.group(1)), int(match.group(2))), (int(match.group(3)), int(match.group(4)))))

    min_x = 0
    max_x = 4000000
    max_y = 4000000

    for i in range(0, max_y + 1):
        row_query = i
        intervals = []
        if i % 100000 == 0:
            print("Iteration: " + str(i))
        for input in inputs:
            dist = compute_distance(input)
            if input[0][1] <= row_query and input[0][1] + dist >= row_query:
                factor = input[0][1] + dist - row_query
            elif input[0][1] >= row_query and input[0][1] - dist <= row_query:
                factor = row_query - (input[0][1] - dist)
            else:
                continue
            intervals.append([input[0][0] - factor, input[0][0] + factor])
        intervals = mergeIntervals(intervals)
        if len(intervals) > 1 or intervals[0][0] > min_x or intervals[0][1] < max_x:
            print(intervals, end = "")
            print(str(i))
            print(((intervals[0][1] + 1) * 4000000) + i)

part1()
part2()