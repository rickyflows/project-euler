#!/usr/bin/env python3
from utils.sieve import sieve, totient_with_sieve
from utils.general_utils import integer_anagram

def main():
    N = 10**7
    primes = sieve(N)
    prime_set = set(sieve(N))
    candidates = set()
    for n in range(2, N):
        if n in prime_set:
            continue
        totient = totient_with_sieve(n, primes)
        if integer_anagram(n, totient):
            candidates.add((n / totient, n))
    print(min(candidates))

if __name__=="__main__":
    main()
