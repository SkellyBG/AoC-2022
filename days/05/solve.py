#!/bin/python3
import re

f = open("input.txt", "r")

list = []
for i in range(0, 9):
    list.append([])
flag = False

for line in f:
    if line == '\n':
        flag = True
    if not flag:
        _ = [list[i//4].append(c) for i, c in enumerate(line) if c.strip() and c not in ["[", "]"]] 

        # for i in range(1, 36, 4):
        #     if (line[i - 1] != ' '):
        #         list[i // 4].append(line[i])
    elif line != '\n':
        line = [int(x.strip()) for x in re.split(r"move | from | to ", line) if x.strip()]
        temp = []
        for i in range(0, line[0]):
            temp.insert(0, list[line[1] - 1].pop(0))
        # temp.reverse()
        for i in range(0, line[0]):
            list[line[2] - 1].insert(0, temp.pop(0))
for i in range(0, 9):
    print(list[i][0], end='')
print()

