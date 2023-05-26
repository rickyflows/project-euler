#!/usr/bin/env python3
import numba
import numpy as np

@numba.njit
def integer_anagram(n1, n2):
    counter = np.zeros(10)
    while n1:
       counter[n1 % 10] += 1
       n1 //= 10
    while n2:
        counter[n2 % 10] -= 1
        n2 //= 10
    for c in counter:
        if c:
            return False
    return True

@numba.njit
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
