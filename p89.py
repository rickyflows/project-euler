#!/usr/bin/env python3
import roman

with open('data/0089_roman.txt') as f:
    data = [numeral.strip() for numeral in f.readlines()]

subtractives = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
}
translate = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def from_roman(r):
    n = 0
    for k, v in subtractives.items():
        n += v * r.count(k)
        r = r.replace(k, '')
    for c in r:
        n += translate[c]
    return n

old_len = 0
new_len = 0
for numeral in data:
    old_len += len(numeral)
    new_len += len(roman.toRoman(from_roman(numeral)))
print(old_len - new_len)
