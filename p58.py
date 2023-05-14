#!/usr/bin/env python3
from sympy.ntheory import isprime

def main():
    # See p28
    numerator = 0
    denomenator = 1
    step = 2
    val = 1
    while True:
        for c in range(4):
            val += step
            # guaranteed to be correct up to 2**64
            if isprime(val):
                numerator += 1
        denomenator += 4
        if numerator / denomenator < 0.1:
            print(step + 1)
            break
        step += 2

if __name__ == "__main__":
    main()
