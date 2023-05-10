import numba
import numpy
from typing import List

# Optimization ideas:
# - Skip evens
@numba.jit(nopython = True, parallel = True, fastmath = True, forceobj = False)
def sieve(n: int) -> numpy.ndarray:
    primes = numpy.full(n, True)
    primes[0], primes[1] = False, False
    for i in numba.prange(2, int(numpy.sqrt(n) + 1)):
        if primes[i]:
            primes[i*i::i] = False
    return numpy.flatnonzero(primes)


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
