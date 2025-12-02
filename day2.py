#!/usr/bin/env python3

import sys

def partitions(s):
    n = len(s)
    result = []

    for size in range(1, n):
        if n % size == 0:
            groups = [s[i:i+size] for i in range(0, n, size)]
            result.append(groups)

    return result

data = sys.stdin.readline().strip().split(',')

p1 = 0
p2 = 0

for d in data:
    s = [int(x) for x in d.split('-')]

    for i in range(s[0],s[1]+1):
        i = str(i)

        if not len(i) % 2:
            a = i[:len(i)//2]
            b = i[len(i)//2:]
            if a == b:
                p1 += int(i)

        for p in partitions(i):
            if len(set(p)) == 1:
                p2 += int(i)
                break

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
