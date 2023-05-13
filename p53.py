#!/usr/bin/env python3

LIMIT = 10**6
memo = [[0]*101 for _ in range(101)]
for n in range(101):
    memo[n][0] = 1

for n in range(1, 101):
    for k in range(1, n + 1):
        if memo[n-1][k] + memo[n-1][k-1] > LIMIT:
            memo[n][k] = LIMIT + 1
        else:
            memo[n][k] = memo[n-1][k] + memo[n-1][k-1]

count = sum(x > LIMIT for row in memo for x in row)
print(count)
