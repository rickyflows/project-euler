#!/usr/bin/env python3
from itertools import product

with open('data/p059_cipher.txt') as f:
    data = list(map(int, f.readlines()[0].split(',')))

alphabet = [i for i in range(ord('a'), ord('z') + 1)]
# minor trial and error
common_words = ['the', 'and', 'that']
for password in product(alphabet, repeat=3):
    decoder = (password * (len(data) // 3))[:len(data)]
    decoded_data = ''.join([chr(a ^ b)for a, b in zip(decoder, data)])
    if all(word in decoded_data for word in common_words):
        print(''.join(map(chr, password)))
        print(decoded_data)
        print(sum(map(ord, decoded_data)))
