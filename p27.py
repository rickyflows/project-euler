#!/usr/bin/env python3
from sympy import sieve

max_consecutive_primes = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        consecutive_primes = 0
        while n**2 + a*n + b in sieve:
            n += 1
            consecutive_primes += 1
        if consecutive_primes > max_consecutive_primes:
            A = a
            B = b
            max_consecutive_primes = consecutive_primes
print(A*B)
