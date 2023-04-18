#!/usr/bin/env python3

primes = [2]
n = 3
N = 10001
while len(primes) < N:
    primality = map(lambda p: n % p != 0, primes)
    if all(primality):
        primes.append(n)
    n += 2
print(primes[-1])
