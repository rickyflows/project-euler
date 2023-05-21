#!/usr/bin/env python3
from math import floor, isqrt, sqrt

# This problem is secretly about continued fractions!
# Here is a gentle reference:
# https://math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/Yang.pdf

def continued_fraction_coefficients(D):
    # Compute the continued fraction coefficients of sqrt(D) (c.f. p64)
    yield (a0 := floor(sqrt(D)))
    p_prev, q_prev = a0, 1
    while True:
        q = (D - p_prev**2) // q_prev
        a = (p_prev + a0) // q
        p = a * q - p_prev
        p_prev, q_prev = p, q
        yield(a)

def find_minimal_solution(D):
    """
    Returns the minimal solution for x**2 - D * y**2 = 1 for a non-square D > 0.
    On a high level, solutions to Pell's equation are rational approximations of
    sqrt(D). There is a well-known result from rational approximations theory
    which states that if a rational approximation is 'good enough' then it must
    be a convergent produced by the continued fraction expansion of sqrt(D).
    The solutions to Pell's equation meet that bar.
    """
    coefs = continued_fraction_coefficients(D)
    n_prev_prev, n_prev = 0, 1
    d_prev_prev, d_prev = 1, 0
    while True:
        # Compute the numerator and denominator of the next convergent (c.f. p65)
        a = next(coefs)
        n = a * n_prev + n_prev_prev
        d = a * d_prev + d_prev_prev
        n_prev_prev, n_prev = n_prev, n
        d_prev_prev, d_prev = d_prev, d
        # Check if solution satisfies Pell's equation
        if n**2 - D * d**2 == 1:
            return n, d, D

non_squares = [i for i in range(2, 1001) if isqrt(i)**2 != i]
print(max(map(find_minimal_solution, non_squares)))
