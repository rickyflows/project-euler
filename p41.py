#!/usr/bin/env python3
from utils.sieve import sieve
from typing import List, Set
from time import time


def is_pandigital(n_string: str, digits_array: List[Set[str]]):
    digits = set(n_string)
    return digits == digits_array[len(n_string)]

def main():
    digits_array = [
        set([str(d) for d in range(1, k)]) for k in range(1, 11)
    ]
    t0 = time()
    primes = sieve(7654321 + 1)
    t1 = time()
    print(t1 - t0)

    for p in primes[::-1]:
        if is_pandigital(str(p), digits_array):
            print(p)
            break
    t2 = time()
    print(t2 - t1)

if __name__  == "__main__":
    main()

# From the discussion:
# Note: Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
# Note: Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)
# This speeds up the code from ~30s to ~0.5s
