#!/usr/bin/env python3

S = 0
MOD = pow(10, 10)
for x in range(1, 1001):
    S += pow(x, x, MOD)
print(S % MOD)
