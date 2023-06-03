#!/usr/bin/env python3
import numpy as np

# If I have a w * h grid containing N rectangles then a (w + 1) * h grid will have
# N + (w + 1) * (h + h // 2 + (h - 1) // 2 + ... + h // h) rectangles
# The last sum reduces to the h-th triangle number
def triangle_number(n):
    return (n * (n + 1)) // 2

N = 100
memo = np.zeros((N, N), dtype=np.int64)
memo[1, :] = [triangle_number(k) for k in range(N)]

for row in range(2, N):
    for col in range(row, N):
        memo[row, col] = memo[row - 1, col] + row * triangle_number(col)
target = 2 * 10**6
idx = np.unravel_index(np.argmin(np.abs(memo - target)), memo.shape)
print(idx[0] * idx[1])

# Nice analytical solution https://projecteuler.net/thread=85#613
