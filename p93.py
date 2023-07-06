#!/usr/bin/env python3
from itertools import permutations, combinations, product

# There are 5 ways to parenthesize using 3 pairs of parenthesis.
# Coincidentally the Catalan number C_3 = 5.
# (((a ~ b) ~ c) ~ d)
# ((a ~ (b ~ c)) ~ d)
# (a ~ ((b ~ c) ~ d))
# (a ~ (b ~ (c ~ d)))
# ((a ~ b) ~ (c ~ d))

def main():
    max_seq = -1
    for digits in combinations(range(1, 10), 4):
        vals = set()
        for a, b, c, d in permutations(digits):
            for x, y, z in product(['+', '-', '*', '/'], repeat=3):
                expressions = [
                    f'((({a} {x} {b}) {y} {c}) {z} {d})',
                    f'(({a} {x} ({b} {y} {c})) {z} {d})',
                    f'({a} {x} (({b} {y} {c}) {z} {d}))',
                    f'({a} {x} ({b} {y} ({c} {z} {d})))',
                    f'(({a} {x} {b}) {y} ({c} {z} {d}))',
                ]
                vals.update(map(int, filter(is_target, map(my_eval, expressions))))
        i = 1
        while i in vals:
            i += 1
        if i - 1 > max_seq:
            max_seq = i - 1
            max_seq_digits = digits
    print(max_seq, sorted(max_seq_digits))

def is_target(x):
    return x > 0 and abs(x - round(x)) < 1e-8

def my_eval(s):
    try:
        return eval(s)
    except ZeroDivisionError:
        return 0

if __name__=='__main__':
    main()
