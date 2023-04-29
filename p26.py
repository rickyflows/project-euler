#!/usr/bin/env python3

# For an arbitrary integer n, the length L(n) of the decimal repetend of 1/n divides φ(n), where φ is the totient function.
# The length is equal to φ(n) if and only if 10 is a primitive root modulo n.
# https://en.wikipedia.org/wiki/Repeating_decimal
# This all seems like overkill, let's try something simpler.

def get_repetend_length(n):
    r = 1
    remainders = []
    while True:
        r = (10 * r) % n
        if r == 0:
            return 0
        if r in remainders:
            return len(remainders) - remainders.index(r)
        remainders.append(r)


max_length = 0
idx = -1
for n in range(1, 1000):
    if get_repetend_length(n) > max_length:
        max_length = get_repetend_length(n)
        idx = n

print(max_length, idx)
