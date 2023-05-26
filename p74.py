#!/usr/bin/env python3
from math import factorial

# see p34
def digits(num):
    return map(int, str(num))

loop_numbers = {
    1: 1,
    2: 1,
    145: 1,
    40585: 1,
    871: 2,
    45361: 2,
    872: 2,
    45362: 2,
    169: 3,
    363600: 3,
    1454: 3,
}
fac = {k: factorial(k) for k in range(10)}

N = 1000000
memo = {}
count = 0
for x in range(1, N):
    seq = 0
    y = x
    while True:
        y = sum(map(lambda d: fac[d], digits(y)))
        seq += 1
        if y in loop_numbers:
            memo[x] = seq + loop_numbers[y]
            break
        elif y in memo:
            memo[x] = seq + memo[y]
            break
    count += int(memo[x] == 60)
print(count)
