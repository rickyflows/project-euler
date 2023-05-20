#!/usr/bin/env python3
from math import floor, sqrt, isqrt

def helper(n):
    """
    Calculates the continued fraction expansion of sqrt(n) using the integer
    algorithm from https://math.stackexchange.com/a/2216011 (no floating point
    error!). As soon as a (p, q) pair repeat we have finished 1 period, return
    length of that period
    """
    pq_pairs = set()
    seq_length = 0
    p_prev, q_prev = (m := floor(sqrt(n))), 1
    while True:
        q = (n - p_prev**2) // q_prev
        d = (p_prev + m) // q
        p = d * q - p_prev
        if (p, q) in pq_pairs:
            return seq_length
        pq_pairs.add((p, q))
        seq_length += 1
        p_prev, q_prev = p, q

S = 0
for n in range(10001):
    if n == isqrt(n)**2:
        continue
    if helper(n) % 2:
        S += 1
print(S)
