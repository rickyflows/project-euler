#!/usr/bin/env python3
from utils.sieve import sieve
from sympy.ntheory import isprime
from itertools import combinations, chain

def concat_helper(p, q):
    concat_a = int(str(p) + str(q))
    concat_b = int(str(q) + str(p))
    return isprime(concat_a) and isprime(concat_b)

def precompute_pairs(primes):
    pairs = set()
    for pair in combinations(primes, 2):
        if concat_helper(*pair):
            pairs.add(frozenset(pair))
    return pairs

primes = sieve(10000)
valid_pairs = precompute_pairs(primes)
candidates = valid_pairs

for _ in range(1, 4):
    next_candidates = set()
    for candidate in candidates:
        for p in primes:
            if all(frozenset((p, q)) in valid_pairs for q in candidate):
                next_candidates.add(frozenset(chain(candidate, [p])))
    candidates = next_candidates
print(candidates)
