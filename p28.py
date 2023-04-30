#!/usr/bin/env python3

S = 1
val = 1
step = 2
for step in range(2, 1001, 2):
    for c in range(4):
        val += step
        S += val
print(S)
