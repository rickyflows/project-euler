#!/usr/bin/env python3
from utils.general_utils import generate_pythagorean_triplets
from collections import Counter

L = 1_500_000
triplets = generate_pythagorean_triplets(L)
counter = Counter(t.sum() for t in triplets)
print(sum(1 for count in counter.values() if count == 1))
