#!/usr/bin/env python3
from sympy import sieve
from itertools import product

N = 1000
sieve.extend_to_no(N)
squares = [2*n**2 for n in range(1, N + 1)]
# Really leaning on my cpu here
vals = set(a + b for a, b in product(sieve._list, squares))

for n in range(9, sieve._list[-1] + 2*squares[-1] + 1, 2):
    if n in sieve: continue
    if n not in vals:
        print(n)
        break
