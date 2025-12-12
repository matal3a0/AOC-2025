#!/usr/bin/env python3

import sys

def add_range(optimal_ranges, new):
    start, end = new
    result = []

    for a, b in optimal_ranges:
        if end < a - 1:
            result.append((start, end))
            start, end = a, b
        elif b < start - 1:
            result.append((a, b))
        else:
            start = min(start, a)
            end = max(end, b)

    result.append((start, end))
    result.sort()
    return result

p1 = 0
p2 = 0
ranges = []
ids = []
optimal_ranges = []

data = [line.strip() for line in sys.stdin.readlines()]

for d in data:
    if '-' in d:
        ranges.append([int(x) for x in d.split('-')])
    elif d != '':
        ids.append(int(d))

for r in ranges:
    optimal_ranges = add_range(optimal_ranges,r)

for id in ids:
    for r in optimal_ranges:
        if id in range(int(r[0]),int(r[1])+1):
            p1 += 1
            break

for r in optimal_ranges:
    p2 += (r[1] - r[0]+1)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
