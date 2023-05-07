#!/usr/bin/env python3
from math import prod

idigits = [10**k for k in range(7)]

# You can pretty much solve this by hand, but 10**6 isn't too big
total_length = 0
idigit = 0
digits = []
n = 0
while idigit < len(idigits):
    n += 1
    total_length += len(str(n))
    if total_length >= idigits[idigit]:
        idx = total_length - idigits[idigit]
        digit = str(n)[::-1][idx]
        digits.append(int(digit))
        idigit += 1
print(prod(digits))
