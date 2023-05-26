#!/usr/bin/env python3
from utils.general_utils import gcd
from math import floor, ceil

N = 12000
candidates = set()
for d in range(2, N + 1):
    left =  ceil(d / 3)
    right = floor(d / 2)
    for n in range(left, right + 1):
        g = gcd(n, d)
        candidates.add((n // g, d // g))
# subtract off the endpoints 1/3 and 1/2
print(len(candidates) - 2)

# Incredible ideas: https://projecteuler.net/overview=0073
# - Farey sequence
# - Stern Brocot tree
# - Mobius Inversion
