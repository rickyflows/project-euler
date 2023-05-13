#!/usr/bin/env python3
from sympy import sieve

sieve.extend(10**4)
four_digit_primes = list(filter(lambda x: x > 1000, sieve._list))

for i, p in enumerate(four_digit_primes):
    for j, q in enumerate(four_digit_primes[i+1:]):
        r = q + (q - p)
        if r in sieve and sorted(str(p)) == sorted(str(q)) == sorted(str(r)):
            print(p, q, r)
