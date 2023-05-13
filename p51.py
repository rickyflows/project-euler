#!/usr/bin/env python3
from sympy import sieve
from itertools import combinations

# 1 digit replacement is impossible because sum of digits will be divisible by 3
# Since we are looking for 8 prime value families, only need to consider
# replacing 0s, 1s, and 2s
def count_replacements(p_string, d):
    indices = [i for i, c in enumerate(p_string) if c == d]
    for subset_size in range(2, len(indices) + 1):
        for subset in combinations(indices, subset_size):
            if count_replacements_helper(list(p_string), d, subset) >= 8:
                print(p_string, d, subset)
                exit()

def count_replacements_helper(p_list, d, subset):
    count = 1
    for new_d in range(int(d) + 1, 10):
        for i in subset:
            p_list[i] = str(new_d)
        if int(''.join(p_list)) in sieve:
            count += 1
    return count

for p in sieve:
    for d in '012':
        if str(p).count(d) > 1:
            r = count_replacements(str(p), d)
