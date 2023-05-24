#!/usr/bin/env python3
from itertools import permutations, groupby
#         indices
#
#           0
#            \
#             1    2
#           /   \ /
#          3     4
#         / \   /
#        5   6-7--8
#             \
#              9
#


def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

order = [0, 1, 4, 2, 4, 7, 8, 7, 6, 9, 6, 3, 5, 3, 1]
candidates = set()
for perm in permutations(range(1, 11)):
    outer_vals = [perm[i] for i in order[::3]]
    if perm[0] != min(outer_vals) or 10 not in outer_vals:
        continue
    vals = [perm[i] for i in order]
    reduced_vals = [sum(vals[3*i:3*(i+1)]) for i in range(len(vals)//3)]
    if all_equal(reduced_vals):
        candidates.add(int(''.join(map(str, vals))))
print(max(candidates))
