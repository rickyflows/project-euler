#!/usr/bin/env python3
from utils.sieve import prime_factorize

i = 1
combo = 0
while True:
    i += 1
    if len(set(prime_factorize(i))) == 4:
        combo += 1
    else:
        combo = 0
    if combo == 4:
        print(i-3)
        break
