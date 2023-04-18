#!/usr/bin/env python3
from functools import reduce

def sieve(N):
    # consider using bitarrays
    # consider getting rid of even numbers
    arr = [True]*(N+1)
    arr[0] = arr[1] = False
    for i in range(int((N+1)**0.5)):
        if arr[i]:
            for k in range(i, N // i + 1):
                arr[k*i] = False
    return arr

primes = sieve(2*10**6)
sum_of_primes = reduce(lambda s, val: s + val[0] if val[1] else s, enumerate(primes), 0)
print(sum_of_primes)
