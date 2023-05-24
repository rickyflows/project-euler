#!/usr/bin/env python3
with open('data/p067_triangle.txt') as f:
    raw_data = f.readlines()
data = [list(map(int, row.split())) for row in raw_data]

# Copy pasted from p18
memo = [[0 for col in row] for row in data]
memo[0][0] = data[0][0]
for i in range(1, len(data)):
    memo[i][0] = memo[i-1][0] + data[i][0]
    memo[i][-1] = memo[i-1][-1] + data[i][-1]

for i in range(1, len(data)):
    for j in range(1, len(data[i])-1):
        memo[i][j] = max(memo[i-1][j], memo[i-1][j-1]) + data[i][j]

print(max(memo[-1]))
