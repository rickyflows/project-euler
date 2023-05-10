#!/usr/bin/env python3
def is_pentagonal(x):
    n = ((24*x + 1)**0.5 + 1) / 6
    return n == int(n)

def triangle(n):
    return (n * (n + 1)) // 2

# Remark: every hexagonal number is triangular, and the odd triangle numbers are hexagonal
n = 287
while not is_pentagonal(triangle(n)):
    n += 2
print(triangle(n), n)
