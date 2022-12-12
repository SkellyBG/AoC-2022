#!/bin/python3
import re

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def nums(line) -> list:
    return [int(x) for x in line if x.strip()]

def part1():
    f = open("input.txt", "r")
    count = 0
    registers = [1]
    pc = 1
    for line in f:
        line = line.split()
        if line[0] == "noop":
            if ((pc - 20) % 40) == 0:
                count += pc * registers[0]
            pc += 1
        elif line[0] == "addx":
            if ((pc - 20) % 40) == 0:
                count += pc * registers[0]
            pc += 1
            if ((pc - 20) % 40) == 0:
                count += pc * registers[0]
            pc += 1
            registers[0] += int(line[1])
    print(count)

def part2():
    f = open("input.txt", "r")
    count = 0
    registers = [1]
    pc = 0
    for line in f:
        line = line.split()
        if line[0] == "noop":
            if pc in range(registers[0] - 1, registers[0] + 2):
                print("#", end = "")
            else:
                print(".", end = "")
            pc += 1
            if pc % 40 == 0:
                pc = 0
                print()
        elif line[0] == "addx":
            if pc in range(registers[0] - 1, registers[0] + 2):
                print("#", end = "")
            else:
                print(".", end = "")
            pc += 1
            if pc % 40 == 0:
                pc = 0
                print()
            if pc in range(registers[0] - 1, registers[0] + 2):
                print("#", end = "")
            else:
                print(".", end = "")
            pc += 1
            if pc % 40 == 0:
                pc = 0
                print()
            registers[0] += int(line[1])

part1()
part2()