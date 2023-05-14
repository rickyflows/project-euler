#!/usr/bin/env python3
from itertools import product

max_digit_sum = 0
for a, b in product(range(100), repeat=2):
    max_digit_sum = max(max_digit_sum,
                        sum(map(int, str(pow(a, b)))))
print(max_digit_sum)
