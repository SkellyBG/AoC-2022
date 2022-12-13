#!/bin/python3
import re
import functools

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def nums(line) -> list:
    return [int(x) for x in line if x.strip()]

def compare(left: list, right: list) -> int:
    for _, (left_e, right_e) in enumerate(zip(left, right)):
        if isinstance(left_e, int) and isinstance(right_e, int):
            if left_e < right_e:
                return -1
            elif left_e > right_e:
                return 1
        elif isinstance(left_e, list) and isinstance(right_e, list):
            res = compare(left_e, right_e)
            if res != 0:
                return res
        else:
            res = 0
            if isinstance(left_e, int):
                res = compare([left_e], right_e)
            else:
                res = compare(left_e, [right_e])
            if res != 0:
                return res
    if len(left) == len(right):
        return 0
    if len(left) < len(right):
        return -1
    if len(left) > len(right):
        return 1

def part1() -> None:
    f = open("input.txt", "r")
    res = " "
    index = 1
    sum = 0
    while res != "":
        left = eval(f.readline().rstrip("\n"))
        right = eval(f.readline().rstrip("\n"))
        if compare(left, right) == -1:
            sum += index
        res = f.readline()
        index += 1
    print(sum)

        

def part2() -> None:
    f = open("input.txt", "r")
    res = " "
    correct_order = []
    correct_order.append([[2]])
    correct_order.append([[6]])
    while res != "":
        left = eval(f.readline().rstrip("\n"))
        right = eval(f.readline().rstrip("\n"))
        correct_order.append(left)
        correct_order.append(right)
        res = f.readline()
    correct_order = sorted(correct_order, key=functools.cmp_to_key(compare))
    sum = (correct_order.index([[2]]) + 1) * (correct_order.index([[6]]) + 1)
    print(sum)

part1()
part2()