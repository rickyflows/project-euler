#!/usr/bin/env python3
from math import sqrt

def get_half_divisors(N):
    divisors = []
    for i in range(1, int(sqrt(N)) + 1):
        if N % i == 0:
            divisors.append(i)
    return divisors

TARGET = 500
s = 0
n = 1
while True:
    s += n
    if len(get_half_divisors(s)) > TARGET//2:
        print(s, n)
        print(get_half_divisors(s))
        break
    n += 1
