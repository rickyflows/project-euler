#!/usr/bin/env python3
from collections import defaultdict
from itertools import permutations

def figurate(s, N):
    numbers = []
    i = 1
    while (val:= ((s - 2) * i**2 - (s - 4) * i) // 2) < N:
        numbers.append((val, i))
        i += 1
    return numbers

def prefix(n):
    return int(str(n)[:2])

def suffix(n):
    return int(str(n)[2:])

memo = []
N = 10000
for s in range(3, 9):
    four_digit_figurates = filter(lambda x: x[0] > 999, figurate(s, N))
    preprocess = defaultdict(list)
    for val, idx in four_digit_figurates:
        preprocess[prefix(val)].append((val, idx))
    memo.append(preprocess)


# This can be better solved with a DFS
for perm in permutations(memo):
    for pre in perm[0]:
        for a, i in perm[0][pre]:
            for b, j in perm[1][suffix(a)]:
                for c, k in perm[2][suffix(b)]:
                    for d, l in perm[3][suffix(c)]:
                        for e, m in perm[4][suffix(d)]:
                            for f, n in perm[5][suffix(e)]:
                                if suffix(f) == pre and len(set([i, j, k, l, m, n])) == 6:
                                    print(sum([a, b, c, d, e, f]))
                                    exit()
