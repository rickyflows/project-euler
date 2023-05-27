#!/usr/bin/env python3

def memo_helper(idx, memo):
    if idx < 0:
        return 0
    return memo[idx]

# due to Euler/Skiena
def partition(n, memo):
    S = 0
    for k in range(1, n + 1):
        idx1 = n - (k * (3 * k - 1)) // 2
        idx2 = n - (k * (3 * k + 1)) // 2
        S += pow(-1, k + 1) * (memo_helper(idx1, memo) + memo_helper(idx2, memo))
    return S

memo = [0 for _ in range(101)]
memo[0] = 1
for i in range(1, 101):
    memo[i] = partition(i, memo)
print(memo[100] - 1)
