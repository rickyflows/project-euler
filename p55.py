#!/usr/bin/env python3

def is_palindrome(s):
    return s == s[::-1]

def reverse(n):
    return int(str(n)[::-1])

N = 10000
iter_max = 50
count = 0
for n in range(N):
    val = n
    for k in range(iter_max):
        val = val + reverse(val)
        if is_palindrome(str(val)):
            count += 1
            break
print(N - count)
