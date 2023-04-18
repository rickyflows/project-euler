#!/usr/bin/env python3

def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

palindromes = []
for i in range(999, 99, -1):
    for j in range(999, i-1, -1):
        if is_palindrome(str(i*j)):
            palindromes.append((i*j, i, j))

print(max(palindromes))
