#!/usr/bin/env python3
from utils.sieve import sieve
from numpy import searchsorted
from itertools import accumulate, chain

def binary_search(arr, val):
    idx = searchsorted(arr, val)
    return idx < len(arr) and arr[idx] == val

primes = sieve(10**6)
# Only have to look at primes up to 10**6 / 21 ≈ 47619
sequence_candidates = chain([0], filter(lambda x: x < 10**6 / 21, primes))
partial_sums = list(accumulate(sequence_candidates))

max_seq_length, max_sum = 21, 953
for l, s in enumerate(partial_sums):
    for r, t in enumerate(partial_sums[l+1:]):
        if r - l > max_seq_length and binary_search(primes, t-s):
            max_seq_length = r - l
            max_sum = t - s
print(max_seq_length, max_sum)
