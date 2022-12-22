#!/bin/python3
import re
import functools
from collections import deque

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def nums(line) -> list:
    return [int(x) for x in line if x.strip()]

def query(monkeys: dict, monkey: str):
    if type(monkeys[monkey]) is not list:
        return monkeys[monkey]
    return eval(str(query(monkeys, monkeys[monkey][0])) + monkeys[monkey][1] + str(query(monkeys, monkeys[monkey][2])))

def part1() -> None:
    f = open("input.txt", "r")
    monkeys = {}
    for line in f:
        match = re.fullmatch(r"([a-zA-Z]{4}): (.*)$", line.strip())
        monkeys[match[1]] = match[2].split() if len(match[2].split()) > 1 else int(match[2])
    

def part2() -> None:
    f = open("input.txt", "r")
    monkeys = {}
    for line in f:
        match = re.fullmatch(r"([a-zA-Z]{4}): (.*)$", line.strip())
        monkeys[match[1]] = match[2].split() if len(match[2].split()) > 1 else int(match[2])

    monkeys["root"][1] = "-"
    # print(query(monkeys, monkeys["root"][0]))
    # print(query(monkeys, monkeys["root"][2]))
    # monkeys["humn"] += 1

    # monkeys["humn"] = 1j
    monkeys["humn"] = 3378273370680
    print(query(monkeys, "root"))
        
part1()
part2()