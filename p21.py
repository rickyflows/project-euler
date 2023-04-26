#!/usr/bin/env python3
from math import sqrt

def get_divisors(N):
    lower_divisors = []
    for i in range(1, int(sqrt(N)) + 1):
        if N % i == 0:
            lower_divisors.append(i)
    upper_divisors = []
    for d in reversed(lower_divisors):
        if d*d != N and d != 1:
            upper_divisors.append(N//d)
    return lower_divisors + upper_divisors

limit = 10000
S = 0
for a in range(1, 10000):
    b = sum(get_divisors(a))
    if b > a and sum(get_divisors(b)) == a:
        S += a + b

print(S)
