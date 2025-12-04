#!/usr/bin/env python3

import sys

data = [[c for c in l.strip()] for l in sys.stdin.readlines()]

p1 = 0
p2 = 0
removed = False
first = True

while not removed:
    removed = True
    remove = []

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '@':
                adjacent = 0
                for y1 in range(y-1,y+2):
                    for x1 in range(x-1,x +2):
                        if 0 <= y1 < len(data) and 0 <= x1 < len(data[0]) and data[y1][x1] == '@':
                            adjacent += 1
                if adjacent <= 4:
                    remove.append([y,x])
                    if first:
                        p1 += 1

    for r in remove:
        data[r[0]][r[1]] = 'x'
        removed = False
        p2 += 1
    first = False

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
