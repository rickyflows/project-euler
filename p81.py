#!/usr/bin/env python3

with open('data/matrix.txt') as f:
    data = [[int(x) for x in row.strip().split(',')] for row in f.readlines()]

# data is a square matrix
m = len(data)
# preprocess
for i in range(m - 2, -1, -1):
    data[-1][i] += data[-1][i + 1]
    data[i][-1] += data[i + 1][-1]
# classic dp
for i in range(m - 2, -1, -1):
   for j in range(i, -1, -1):
        data[i][j] += min(data[i + 1][j], data[i][j + 1])
   for j in range(i - 1, -1, -1):
    data[j][i] += min(data[j + 1][i], data[j][i + 1])
print(data[0][0])
