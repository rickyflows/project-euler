#!/usr/bin/env python3
from itertools import product

print(len(set(pow(a,b) for a, b in product(range(2,101), repeat=2))))
