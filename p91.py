#!/usr/bin/env python3
from numba import njit

@njit
def mydot(v, w):
    return v[0] * w[0] + v[1] * w[1]

@njit
def right_angle_helper(coord_pair):
    p, q = coord_pair
    r = mydot(p, q)
    return r == 0 or mydot(p, p) == r or mydot(q, q) == r

@njit
def main():
    N = 50
    coords = []
    for x in range(N + 1):
        for y in range(N + 1):
            coords.append((x, y))
    coords = coords[1:] # skip (0, 0)

    count = 0
    for i in range(len(coords)):
        for j in range(i):
            p, q = coords[i], coords[j]
            count += right_angle_helper((p, q))
    print(count)

if __name__ == '__main__':
    main()
