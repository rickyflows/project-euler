#!/usr/bin/env python3
from numba import njit
from numpy import sqrt

@njit
def is_integer(x):
    EPS = 10**-8
    return abs(x - round(x)) < EPS

@njit
def bit_length(n):
    if n == 0:
        return 0
    bits = 0
    while n:
        n >>= 1
        bits += 1
    return bits

@njit
def isqrt(n):
    x = n
    y = (2 ** ((bit_length(n) + 1) // 2)) - 1
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

@njit
def main():
    PERIMETER_LIMIT = 10**9
    ans = 0
    for s in range(3, PERIMETER_LIMIT // 3 + 1, 2):
        for unit in [-1, 1]:
            b = s + unit
            h = isqrt(s**2 - (b // 2)**2)
            if h**2 + (b // 2)**2 == s**2 and is_integer(1/2 * b * h):
                ans += 3 * s + unit
    print(ans)

if __name__=='__main__':
    main()
