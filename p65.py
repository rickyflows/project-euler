#!/usr/bin/env python3

# See p57, the general result for convergents is
# Call the k-th fraction n_k/d_k. Notice that
# n_k = a_k * n_{k-1} + n_{k-2} and
# d_k = a_k * d_{k-1} + d_{k-2}

n_prev_prev, n_prev = 2, 3
d_prev_prev, d_prev = 1, 1
N = 100
for i in range(1, N-1):
    if i % 3 == 1:
        a = 2 * (i // 3 + 1)
    else:
        a = 1
    n = a * n_prev + n_prev_prev
    d = a * d_prev + d_prev_prev
    n_prev_prev, n_prev = n_prev, n
    d_prev_prev, d_prev = d_prev, d
print(sum(map(int, str(n))))
