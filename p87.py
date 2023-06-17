#!/usr/bin/env python3
from utils.sieve import sieve
from itertools import product
import numpy as np

def main():
    LIMIT = 50_000_000
    primes = sieve(int(pow(LIMIT, 1/2)))
    squares = primes**2
    cubes = primes[:np.searchsorted(primes, int(pow(LIMIT, 1/3)))]**3
    quarts = primes[:np.searchsorted(primes, int(pow(LIMIT, 1/4)))]**4

    vals = set()
    for p, q, r in product(squares, cubes, quarts):
        if p + q + r < LIMIT:
            vals.add(p + q + r)
    print(len(vals))

if __name__=='__main__':
    main()
