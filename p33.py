#!/usr/bin/env python3
from functools import reduce

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

digit_cancelling_fractions = set()
# To be improved
for n in range(10, 99):
    for d in range(n + 1, 100):
        if d % 10 == 0:
            continue
        ns = set(str(n))
        ds = set(str(d))
        if len(ds) == 1 or len(ns) == 1:
            continue
        if len(ns & ds) == 1:
            v = ns & ds
            if int((ns - v).pop())/int((ds - v).pop()) == n/d:
                digit_cancelling_fractions.add((n, d))

product = reduce(lambda p, x: (p[0]*x[0], p[1]*x[1]), digit_cancelling_fractions)
print(product[1] // gcd(*product))
