#!/bin/python3

f = open("input.txt", "r")

line = f.readline()

score = 0

given = ['A', 'B', 'C']
choice = ['X', 'Y', 'Z']

matrix = [
    # R P S
    [3, 6, 0],
    [0, 3, 6],
    [6, 0 ,3]
]

# while line:
#     line = line.strip().split(" ")
#     score += choice.index(line[1]) + 1
#     score += matrix[given.index(line[0])][choice.index(line[1])]
#     line = f.readline()

# print(score)
    
while line:
    line = line.strip().split(" ")
    score += matrix[1][choice.index(line[1])]
    score += (given.index(line[0]) + choice.index(line[1]) - 1) % 3 + 1
    line = f.readline()

print(score)




    
