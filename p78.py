#!/usr/bin/env python3
from math import sqrt

# Copied from p76
# due to Euler/Skiena
def partition(n, memo):
    S = 0
    limit = int((sqrt(24 * n + 1)  + 1) / 6) + 1
    for k in range(1, limit):
        idx1 = n - (k * (3 * k - 1)) // 2
        idx2 = n - (k * (3 * k + 1)) // 2
        S += pow(-1, k + 1) * (memo[idx1] + memo[idx2])
    return S

N = 100000
memo = [0 for _ in range(N)]
memo[0] = 1
for i in range(1, N):
    memo[i] = partition(i, memo)
    if memo[i] % pow(10, 6) == 0:
        print(i, memo[i])
        break
