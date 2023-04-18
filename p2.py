#!/usr/bin/env python3

f_n = 2
f_n_minus_1 = 1
f_n_minus_2 = 1
s = 0

while f_n < 4*10**6:
    f_n = f_n_minus_1 + f_n_minus_2
    if f_n % 2 == 0:
        s += f_n
    f_n_minus_2 = f_n_minus_1
    f_n_minus_1 = f_n

print(s)
