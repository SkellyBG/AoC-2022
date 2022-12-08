#!/bin/python3
from queue import PriorityQueue

f = open("input.txt", "r");

globalMax = 0;
localMax = 0;

q = PriorityQueue();

line = f.readline()
while line:
    if not line.strip():
        q.put(0 - localMax)
        localMax = 0
    else:
        localMax += int(line.strip())
    line = f.readline()

print(-1 * (q.get() + q.get() + q.get()));
