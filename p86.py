#!/usr/bin/env python3
from utils.general_utils import generate_pythagorean_triplets
from numba import njit

@njit
def helper(cuboid):
    a, b, c, = cuboid
    d = (a + b)**2 + c**2
    return int(d**0.5)**2 == d

def main():
    # Just fiddled with M till I found the answer
    M = 1818
    triplets = generate_pythagorean_triplets(6 * M)
    candidate_cuboids = set()
    for a, b, _ in triplets:
        if b <= M:
            candidates = [(d, a - d, b) for d in range(max(1, a - M), min(M, a // 2 + 1))]
            candidate_cuboids.update(map(lambda x: tuple(sorted(x)), candidates))
        if a <= M:
            candidates = [(d, b - d, a) for d in range(max(1, b - M), min(M, b // 2 + 1))]
            candidate_cuboids.update(map(lambda x: tuple(sorted(x)), candidates))

    print(sum(1 for cuboid in filter(helper, candidate_cuboids)))

if __name__=='__main__':
    main()
