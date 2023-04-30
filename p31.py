#!/usr/bin/env python3

limit = 200 + 1
coins = [1,2,5,10,20,50,100,200]
memo = [[0 for p in range(limit)] for c in coins]
memo[0] = [0] + [1 for p in range(1,limit)]
for i, c in enumerate(coins):
    for p in range(1, limit):
        if p % c == 0:
            memo[i][p] = 1

for i, c in enumerate(coins[1:], start=1):
    for p in range(c, limit):
        k = 0
        s = 0
        while p - k * c >= 0:
            memo[i][p] += memo[i-1][p-k*c]
            k += 1

print(memo[-1][-1])
