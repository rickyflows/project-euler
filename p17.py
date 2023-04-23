#!/usr/bin/env python3

from num2words import num2words

s = 0
for i in range(1, 1000 + 1):
    s += sum(map(str.isalpha, num2words(i)))
print(s)
