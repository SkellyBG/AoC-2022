#!/bin/python3


def nums(line) -> list:
    return [int(x) for x in line if x.strip()]

def compute_size(root: dict, l: list) -> int:
    cur_size = 0
    for key, value in root.items():
        if (key == ".."):
            continue
        if (type(value) is dict):
            cur_size += compute_size(value, l)
        else:
            cur_size += value
    l.append(cur_size)
    return cur_size

def part1():
    f = open("input.txt", "r")
    root = {}
    cur = root
    for line in f:
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    cur = root
                else:
                    cur = cur[line[2]]
        else:
            if line[0] == "dir":
                cur[line[1]] = {"..": cur}
            else:
                cur[line[1]] = int(line[0])
    l = []
    compute_size(root, l)
    l = [i for i in l if i <= 100000]
    print(sum(l))


def part2():
    f = open("input.txt", "r")
    root = {}
    cur = root
    for line in f:
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    cur = root
                else:
                    cur = cur[line[2]]
        else:
            if line[0] == "dir":
                cur[line[1]] = {"..": cur}
            else:
                cur[line[1]] = int(line[0])
    l = []
    value = 30000000 - (70000000 - compute_size(root, l))
    # print(value)
    l.sort()
    l = [i for i in l if i >= value]
    print(l[0])

part1()
part2()