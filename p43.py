#!/usr/bin/env python3
from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]
def divisiblity_helper(l):
    for i in range(len(primes)):
        if int(''.join(l[i+1:i+4])) % primes[i]:
            return 0
    return int(''.join(l))

digits = [str(i) for i in range(10)]
print(sum(map(divisiblity_helper, permutations(digits))))
