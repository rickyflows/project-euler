#!/usr/bin/env python3
from functools import reduce

def factorize(n):
    factors = []
    div = 2
    max_size = n**0.5
    while n >= div:
        if n % div:
            div += 1
        else:
            factors.append(div)
            n /= div
    return factors

INPUT = 600851475143
factors = factorize(INPUT)
print(factors)
product = reduce(lambda x, y: x * y, factors)
print(product)
