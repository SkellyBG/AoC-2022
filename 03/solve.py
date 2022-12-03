#!/bin/python3

def intersection(lst1, lst2, lst3):
    res = [value for value in lst1 if value in lst2]
    res = [value for value in res if value in lst3]
    return res

f = open("input.txt", "r")

sum = 0

# while line:
#     line = line.strip()
#     list = []
#     count = 0
#     for i in range(0, len(line) // 2):
#         list.append(line[i])
#     for i in range(len(line) // 2, len(line)):
#         if list.count(line[i]) != 0:
#             # print(line[i], end=" ")
#             count += ord(line[i].lower()) - ord("a") + 1
#             # print(count)
#             if line[i].isupper():
#                 count += 26
#             break
#     sum += count
#     # print(count)
#     line = f.readline()
# print(sum)

while True:
    letter = intersection(f.readline().strip(), f.readline().strip(), f.readline().strip())[0]
    sum += ord(letter.lower()) - ord("a") + 1
    if letter.isupper():
        sum += 26
    print(sum)
