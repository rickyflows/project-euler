#!/usr/bin/env python3
from utils.general_utils import gcd

N = 10**6
candidates = set()
for d in range(2, N + 1):
    if d % 7 == 0:
        continue
    n = (3 * d) // 7
    g = gcd(n, d)
    candidates.add((n // g, d // g))
print(max(map(lambda x: (x[0]/ x[1], x[0], x[1]), candidates)))
