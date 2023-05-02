#!/usr/bin/env python3
from itertools import permutations

def int_join(li):
    return int("".join(li))

def split(nums, len_a, len_b, len_c):
    a = int_join(perm[:len_a])
    b = int_join(perm[len_a:len_a+len_b])
    c = int_join(perm[len_a+len_b:len_a+len_b+len_c])
    return a, b, c

pandigital_products = set()
nums = [str(i) for i in range(1, 10)]
for perm in permutations(nums):
    # 2,3,4 and 1,4,5 are the only options
    a, b, c = split(perm, 2, 3, 4)
    x, y, z = split(perm, 1, 4, 5)
    if a * b == c:
        pandigital_products.add(c)
    if x * y == z:
        pandigital_products.add(z)
print(sum(pandigital_products))
