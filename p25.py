#!/usr/bin/env python3
from numpy import sqrt

# The closed form formula defaults to float64s which are bounded by ~300 digits.
# Vanilla python supports integers of unbounded length, so I'll be using
# the standard definition of the Fibonacci numbers.
def F_n(n):
    return 1/sqrt(5) * ( pow((1 + sqrt(5))/2, n) - pow((1 - sqrt(5))/2, n) )

f_n_prev = 1
f_n_prev_prev = 1
f_n = 2
idx = 3
while len(str(f_n)) < 1000:
    f_n_prev_prev = f_n_prev
    f_n_prev = f_n
    f_n = f_n_prev + f_n_prev_prev
    idx += 1
print(idx)
