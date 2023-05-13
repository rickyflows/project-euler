#!/usr/bin/env python3
from collections import Counter

multiples = [2, 3, 4, 5, 6]
n = 0
while True:
    n += 1
    digits = (Counter(str(n * m)) for m in multiples)
    if all(C == Counter(str(n)) for C in digits):
        print(n)
        break
