#!/usr/bin/env python3

def is_palindrome(s):
    return s == s[::-1]

S = 0
for n in range(10**6):
    if is_palindrome(str(n)) and is_palindrome(str(bin(n))[2:]):
        S += n
print(S)
