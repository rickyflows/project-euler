#!/usr/bin/env python3
from math import sqrt
from itertools import chain
flatten = chain.from_iterable

def get_divisors(N):
    return set(flatten((i, N//i) for i in range(1, int(sqrt(N)) + 1) if N % i == 0))

def get_proper_divisors(N):
    return get_divisors(N).difference({N})

LIMIT = 28123 + 1

abundant_numbers = set()
for n in range(LIMIT):
    if sum(get_proper_divisors(n)) > n:
        abundant_numbers.add(n)

S = 0
for n in range(LIMIT):
    if not any(n - a in abundant_numbers for a in abundant_numbers):
        S += n

print(S)
