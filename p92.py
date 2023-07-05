#!/usr/bin/env python3
from utils.general_utils import get_digits
from numba import njit
import numpy as np
from time import time

@njit
def ends_in_eighty_nine(n, chain_type):
    while chain_type[n] == -1:
        n = np.sum(np.square(get_digits(n)))
    return chain_type[n]

@njit
def main():
    N = 10**7
    chain_type = -1 * np.ones(N, dtype=np.int32)
    chain_type[0], chain_type[1], chain_type[89] = 0, 0, 1
    for i in range(1, N):
        chain_type[i] = ends_in_eighty_nine(i, chain_type)
    print(np.sum(chain_type))

if __name__ == '__main__':
    t0 = time()
    main()
    print(time() - t0)
