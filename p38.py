#!/usr/bin/env python3

digits = set(str(i) for i in range(1,10))
def pandigital_concat_prod(n):
    s = ""
    r = 1
    while len(s) < 9:
        s+= str(n*r)
        r += 1
    if len(s) == 9 and set(s) == digits:
        return int(s)
    return -1


largest_pandigitical_concat_prod = pandigital_concat_prod(9)
for n in range(9180, 9876 + 1):
    largest_pandigitical_concat_prod = max(
        pandigital_concat_prod(n),
        largest_pandigitical_concat_prod
    )
print(largest_pandigitical_concat_prod)
