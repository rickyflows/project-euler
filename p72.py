#!/usr/bin/env python3
from utils.sieve import sieve, totient_with_sieve

N = 10**6
primes = sieve(N)
print(sum(totient_with_sieve(d, primes) for d in range(2, N + 1)))
