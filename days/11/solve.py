#!/bin/python3
import re

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def nums(line) -> list:
    return [int(x) for x in line if x.strip()]

def part1():
    monkeys = []
    monkeys.append([56, 52, 58, 96, 70, 75, 72])
    monkeys.append([75, 58, 86, 80, 55, 81])
    monkeys.append([73, 68, 73, 90])
    monkeys.append([72, 89, 55, 51, 59])
    monkeys.append([76, 76, 91])
    monkeys.append([88])
    monkeys.append([64, 63, 56, 50, 77, 55, 55, 86])
    monkeys.append([79, 58])

    monkey_count = [0 for _ in range(0, 8)]

    for _ in range(0, 20):
        for monkey, list in enumerate(monkeys):
            for worry in list:
                if monkey == 0:
                    worry = worry * 17
                elif monkey == 1:
                    worry += 7
                elif monkey == 2:
                    worry *= worry
                elif monkey == 3:
                    worry += 1
                elif monkey == 4:
                    worry *= 3
                elif monkey == 5:
                    worry += 4
                elif monkey == 6:
                    worry += 8
                elif monkey == 7:
                    worry += 6

                worry = worry // 3

                if monkey == 0:
                    if worry % 11 == 0:
                        monkeys[2].append(worry)
                    else:
                        monkeys[3].append(worry)
                elif monkey == 1:
                    if worry % 3 == 0:
                        monkeys[6].append(worry)
                    else:
                        monkeys[5].append(worry)
                elif monkey == 2:
                    if worry % 5 == 0:
                        monkeys[1].append(worry)
                    else:
                        monkeys[7].append(worry)
                elif monkey == 3:
                    if worry % 7 == 0:
                        monkeys[2].append(worry)
                    else:
                        monkeys[7].append(worry)
                elif monkey == 4:
                    if worry % 19 == 0:
                        monkeys[0].append(worry)
                    else:
                        monkeys[3].append(worry)
                elif monkey == 5:
                    if worry % 2 == 0:
                        monkeys[6].append(worry)
                    else:
                        monkeys[4].append(worry)
                elif monkey == 6:
                    if worry % 13 == 0:
                        monkeys[4].append(worry)
                    else:
                        monkeys[0].append(worry)
                elif monkey == 7:
                    if worry % 17 == 0:
                        monkeys[1].append(worry)
                    else:
                        monkeys[5].append(worry)
                    
                monkey_count[monkey] += 1
            list.clear()
    print("Part 1: ")
    for i, count in enumerate(monkey_count):
        print(f"Monkey {i} inspected items {count} times.")

def part2():
    monkeys = []
    monkeys.append([56, 52, 58, 96, 70, 75, 72])
    monkeys.append([75, 58, 86, 80, 55, 81])
    monkeys.append([73, 68, 73, 90])
    monkeys.append([72, 89, 55, 51, 59])
    monkeys.append([76, 76, 91])
    monkeys.append([88])
    monkeys.append([64, 63, 56, 50, 77, 55, 55, 86])
    monkeys.append([79, 58])

    monkey_count = [0 for _ in range(0, 8)]

    for _ in range(0, 10000):
        for monkey, list in enumerate(monkeys):
            for worry in list:
                if monkey == 0:
                    worry = worry * 17
                elif monkey == 1:
                    worry += 7
                elif monkey == 2:
                    worry *= worry
                elif monkey == 3:
                    worry += 1
                elif monkey == 4:
                    worry *= 3
                elif monkey == 5:
                    worry += 4
                elif monkey == 6:
                    worry += 8
                elif monkey == 7:
                    worry += 6

                worry = worry % (11 * 3 * 5 * 7 * 19 * 2 * 13 * 17)

                if monkey == 0:
                    if worry % 11 == 0:
                        monkeys[2].append(worry)
                    else:
                        monkeys[3].append(worry)
                elif monkey == 1:
                    if worry % 3 == 0:
                        monkeys[6].append(worry)
                    else:
                        monkeys[5].append(worry)
                elif monkey == 2:
                    if worry % 5 == 0:
                        monkeys[1].append(worry)
                    else:
                        monkeys[7].append(worry)
                elif monkey == 3:
                    if worry % 7 == 0:
                        monkeys[2].append(worry)
                    else:
                        monkeys[7].append(worry)
                elif monkey == 4:
                    if worry % 19 == 0:
                        monkeys[0].append(worry)
                    else:
                        monkeys[3].append(worry)
                elif monkey == 5:
                    if worry % 2 == 0:
                        monkeys[6].append(worry)
                    else:
                        monkeys[4].append(worry)
                elif monkey == 6:
                    if worry % 13 == 0:
                        monkeys[4].append(worry)
                    else:
                        monkeys[0].append(worry)
                elif monkey == 7:
                    if worry % 17 == 0:
                        monkeys[1].append(worry)
                    else:
                        monkeys[5].append(worry)
                    
                monkey_count[monkey] += 1
            list.clear()
    print("Part 2: ")
    for i, count in enumerate(monkey_count):
        print(f"Monkey {i} inspected items {count} times.")

part1()
print()
part2()