#!/usr/bin/env python3
from itertools import combinations, product

# required digits: 0, 1, 2, 3, 4, 5, 6, 8, 9
# total configurations: (10 C 6)**2 ~ 400,000
# 01, 04, 09, 16, 25, 36, 49, 64, 81

squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]
def is_valid(d1, d2):
    for a, b in squares:
        if not ((a in d1 and b in d2) or (b in d1 and a in d2)):
            return False
    return True


digits = (i for i in range(10))
dice = product(combinations(digits, 6), repeat = 2)
flipper = {6: 9, 9: 6}
count = 0
for d1, d2 in dice:
    d1, d2 = set(d1), set(d2)
    for k, v in flipper.items():
        if k in d1: d1.add(v)
        if k in d2: d2.add(v)
    if is_valid(d1, d2):
        count += 1
print(count // 2)
