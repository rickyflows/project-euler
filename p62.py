#!/usr/bin/env python3
from collections import defaultdict
from itertools import chain

N = 100000
cubes = [pow(n, 3) for n in range(1, N)]

memo = defaultdict(list)
for c in cubes:
    key = ''.join(sorted(str(c)))
    memo[key].append(c)

print(min(chain(*filter(lambda li: len(li) == 5, memo.values()))))
