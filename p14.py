#!/usr/bin/env python3

N = 10**6
memo = [0]*(N+1)
memo[0] = 2
memo[1] = 1

for i in range(2, N + 1):
    hailstone = i
    steps = 1
    while hailstone >= i:
        if hailstone % 2 == 0:
            hailstone //= 2
        else:
            hailstone = 3 * hailstone + 1
        steps += 1
    memo[i] = steps + memo[hailstone]

print(max(memo), memo.index(max(memo)))
