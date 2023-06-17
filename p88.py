#!/usr/bin/env python3
from utils.sieve import sieve
from utils.sieve import prime_factorize_with_sieve as factorize
from utils.combinatorics import get_partitions
from math import isqrt, prod

def unpack(factors):
    return [factor for p, r in factors for factor in [p] * r]

def main():
    K = 12001
    N = 13000
    primes = sieve(isqrt(N))
    data = [float('inf')] * K
    for n in range(2, N):
        factors = unpack(factorize(n, primes))
        for p in get_partitions(factors):
            if len(p) == 1:
                continue
            k = len(p) + n - sum(map(prod, p))
            if k < K:
                data[k] = min(data[k], n)
    sum_set = set(data[2:K])
    print("ans:", sum(sum_set))

main()
