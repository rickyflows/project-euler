#!/usr/bin/env python3
from sympy import sieve

def is_truncatable(p_string):
    return is_left_truncatable(p_string[1:]) and is_right_truncatable(p_string[:-1])

def is_left_truncatable(p_string):
    if len(p_string) == 0: return True
    return int(p_string) in sieve and is_left_truncatable(p_string[1:])

def is_right_truncatable(p_string):
    if len(p_string) == 0: return True
    return int(p_string) in sieve and is_right_truncatable(p_string[:-1])

truncatables = []
for p in sieve:
    if p < 10: continue
    if len(truncatables) == 11: break
    if is_truncatable(str(p)):
        truncatables.append(p)
print(truncatables)
print(sum(truncatables))
