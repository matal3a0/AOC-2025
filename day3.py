#!/usr/bin/env python3

import sys
import time

data = [ l.strip() for l in sys.stdin.readlines() ]

def combo(line, size):
    n = len(line)
    stack = []

    for i, ch in enumerate(line):
        while stack and stack[-1] < ch and len(stack) - 1 + (n - i) >= size:
            stack.pop()
        if len(stack) < size:
            stack.append(ch)
    return int(''.join(stack))

p1 = 0
p2 = 0

start = time.time()
for d in data:
    c1 = combo(d,2)
    c2 = combo(d,12)
    p1 += c1
    p2 += c2
end = time.time()

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
print(f"Time: {(end-start)*1000:.3f} ms")
