#!/usr/bin/env python3

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def generate_primitive_pythagorean_triplets(P):
    primitives = set()
    for m in range(1, int(P**0.5)+1):
        for n in range(1, m):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if a + b % 2 == 0 or gcd(m,n) > 1:
                continue
            if a + b + c <= P:
                primitives.add((a,b,c))
    return primitives

P = 1000
primitives = generate_primitive_pythagorean_triplets(1000)
non_primitives = set()
for tri in primitives:
    k = 2
    while k * sum(tri) <= P:
        non_primitives.add(tuple(map(lambda x: k * x, tri)))
        k += 1

perimeter = [0 for i in range(1001)]
for tri in primitives | non_primitives:
    perimeter[sum(tri)] += 1
print(perimeter.index(max(perimeter)))
