#!/usr/bin/env python3

powers = set()
for n in range(10):
    k = 1
    while len(str(pow(n, k))) == k:
        k += 1
        powers.add(pow(n, k))
print(len(powers))
