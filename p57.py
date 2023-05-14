#!/usr/bin/env python3

# Call the k-th fraction n_k/d_k. Notice that
# n_k = 2 * n_{k-1} + n_{k-2} and
# d_k = n_{k-1} + d_{k-1}

n_prev_prev, n_prev = 3, 7
d_prev = 5
count = 0
for k in range(3, 1001):
    n = 2 * n_prev + n_prev_prev
    d = n_prev + d_prev
    count += len(str(n)) > len(str(d))
    n_prev_prev, n_prev = n_prev, n
    d_prev = d
print(count)
