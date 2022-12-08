#!/bin/python3

import re

f = open("input.txt", "r")

line = f.readline()

count = 0

while line:
    line = line.strip()
    line = [int(x) for x in re.split("[,-]", line)]
    # if ((line[0] <= line[2] and line[1] >= line[3]) or (line[0] >= line[2] and line[1] <= line[3])):
    #     print(line)
    #     count += 1

    if (((line[0] >= line[2] and line[0] <= line[3]) or (line[1] >= line[2] and line[1] <= line[3]))
    or ((line[2] >= line[0] and line[2] <= line[1]) or (line[3] >= line[0] and line[3] <= line[1]))):
        print(line)
        count += 1

    line = f.readline()
print(count)
