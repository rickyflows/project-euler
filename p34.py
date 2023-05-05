#!/usr/bin/env python3
from math import factorial

def digits(num):
    return map(int, str(num))

fac = {k: factorial(k) for k in range(10)}

# 10e7 is a loose upper bound because 7*9! << 10e7
S = 0
for i in range(3, 10**7):
    if i == sum(map(lambda x: fac[x], digits(i))):
        S += i
print(S)
