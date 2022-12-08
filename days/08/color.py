#!/bin/python3

f = open("input.txt", "r")
matrix = []
for line in f:
    row = []
    for i, c in enumerate(line.strip()):
        row.append(int(c))
    matrix.append(row)

for i, row in enumerate(matrix):
    for j, c in enumerate(row):
        if c == 7:
            print(c, end = " ")
        else:
            print("", end = " ")
    print()
