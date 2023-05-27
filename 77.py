#!/usr/bin/env python3
from utils.general_utils import coin_change
from utils.sieve import sieve

primes = sieve(1000)
for n in range(1000):
    if coin_change(n, primes) > 5000:
        print(n, coin_change(n, primes))
        break
