#!/usr/bin/env python3
from numba import jit

@jit(nopython = True)
def is_pentagonal(x):
    n = ((24*x + 1)**0.5 + 1) / 6
    return n == int(n)

@jit(nopython = True)
def main():
    pentagonal_numbers = []
    k = 0
    while True:
        k += 1
        a = (k * (3 * k - 1)) // 2
        pentagonal_numbers.append(a)
        for b in pentagonal_numbers[:-1]:
            if is_pentagonal(a + b) and is_pentagonal(a - b):
                return a - b

if __name__ == "__main__":
    print(main())
