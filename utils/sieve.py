#!/usr/bin/env python3
import numba
import numpy

@numba.jit(nopython = True, parallel = True, fastmath = True, forceobj = False)
def sieve (n: int) -> numpy.ndarray:
    primes = numpy.full(n, True)
    primes[0], primes[1] = False, False
    for i in numba.prange(2, int(numpy.sqrt(n) + 1)):
        if primes[i]:
            primes[i*i::i] = False
    return numpy.flatnonzero(primes)
