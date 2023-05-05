#!/usr/bin/env python3
from sympy import sieve

def rotations(n):
    if n < 10:
        return [n]
    rotations = []
    s = str(n)
    for i in range(len(s)):
        rotations.append(s[i:] + s[:i])
    return map(int, rotations)

count = 0
for p in sieve:
    if p > 10**6:
        break
    if p > 5 and set(int(i) for i in str(p)) - set([1,3,7,9]):
        continue
    if all(rotation in sieve for rotation in rotations(p)):
        count += 1
print(count)
