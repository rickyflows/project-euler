import numba
import numpy as np
from typing import List


@numba.jit(nopython = True, parallel = True, fastmath = True)
def sieve(n: int) -> np.ndarray:
    primes = np.full(n, True)
    primes[0], primes[1] = False, False
    for i in numba.prange(2, int(np.sqrt(n) + 1)):
        if primes[i]:
            primes[i*i::i] = False
    return np.flatnonzero(primes)


@numba.jit(nopython = True, fastmath = True, forceobj = False)
def prime_factorize(n: int) -> List:
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors


@numba.jit(nopython = True)
def prime_factorize_with_sieve(n: int, primes: np.ndarray):
    factors = []
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            if len(factors) and factors[-1][0] == p:
                count = factors[-1][1]
                factors[-1] = (p, count + 1)
            else:
                factors.append((p, 1))
            n //= p
    if n > 1:
        factors.append((n, 1))
    return factors


@numba.jit(nopython = True)
def totient_with_sieve(n: int, primes: np.ndarray):
    factors = prime_factorize_with_sieve(n, primes)
    product = 1
    for p, k in factors:
        product *= np.power(p, k - 1) * (p - 1)
    return product
