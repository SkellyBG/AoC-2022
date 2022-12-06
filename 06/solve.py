#!/bin/python3

f = open("input.txt", "r")

for line in f:
    # print(len("qmgbljsphdztnv"))
    # print(len(set("qmgbljsphdztnv")))
    for i in range(0, len(line)):
        if len(line[i:i+14]) == len(set(line[i:i+14])):
            print(line[i:i+14])
            print(i + 14)
            break