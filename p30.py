#!/usr/bin/env python3

def helper(n, p):
    return n == sum(map(compose(lambda x: pow(x, p), int), str(n)))

def compose(f, g):
    def h(x):
        return f(g(x))
    return h

S = 0
for n in range(2, 1000000):
    if helper(n, 5):
        S += n
print(S)

# Comment from the forum:
# No 7-digit or higher number can satisfy the condition because even 7*9^5 = 413343 is much smaller than 9999999.
# Therefore, only up to 6-digit numbers are possible, with the largest possible sum being 6*9^5 = 354294. So we are looking for numbers in the range of 10 to 354294.
# - GerhardS
