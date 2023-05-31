#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 105

N = 100
S = 0
for i in range(1, N + 1):
    if int(i**0.5)**2 == i:
        continue
    square_root = Decimal(i).sqrt()
    digits = str(square_root).replace('.', '')[:N]
    S += sum(map(int, digits))
print(S)
