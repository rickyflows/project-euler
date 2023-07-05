#!/usr/bin/env python3
from numba import njit
import numpy as np

@njit
def get_digits(n):
    digits = np.zeros(len(str(n)), dtype=np.int32)
    for i in range(len(digits) - 1, -1, -1):
        n, digits[i] = divmod(n, 10)
    return digits

@njit
def integer_anagram(n1, n2):
    counter = np.zeros(10)
    while n1:
       counter[n1 % 10] += 1
       n1 //= 10
    while n2:
        counter[n2 % 10] -= 1
        n2 //= 10
    for c in counter:
        if c:
            return False
    return True

@njit
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

@njit
def generate_primitive_pythagorean_triplets(P):
    """ Generate all primitive pythagorean triplets
    with a + b + c <= P """
    primitives = []
    for m in range(1, int(P**0.5) + 1):
        for n in range(1, m):
            if gcd(m, n) > 1 or (m - n) % 2 == 0:
                continue
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if a + b + c <= P:
                triplet = np.array(sorted((a, b, c)))
                primitives.append(triplet)
    return primitives

@njit
def generate_pythagorean_triplets(P):
    """ Generate all pythagorean triplets with a + b + c <= P """
    triplets = []
    primitives = generate_primitive_pythagorean_triplets(P)
    for p in primitives:
        k = 1
        while k * p.sum() <= P:
            triplets.append(k * p)
            k += 1
    return triplets


@njit
def coin_change(target: int, coins: np.ndarray) -> int:
    ways = np.zeros(target + 1, dtype=np.int64)
    ways[::coins[0]] = 1
    for c in coins[1:]:
        if c > target:
            break
        for j in range(c, target + 1):
            ways[j] += ways[j - c]
    return ways[target]
