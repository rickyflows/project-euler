#!/usr/bin/env python3
from collections import defaultdict

def is_subsequence(s, t):
    return all(c in iter(t) for c in s)


with open('data/keylog.txt') as f:
    data = set(map(lambda s: s.strip(), f.readlines()))

passcode_digits = set(''.join(data))
print("Digits in passcode:", passcode_digits)

# Step 1, let's construct a graph
graph = {digit: set() for digit in passcode_digits}
for pin in data:
    a, b, c = pin
    graph[a].update((b, c))
    graph[b].add(c)

# Observe, 0 must be the last digit and 7 the first
print("\nOrdering information:")
for k, v in graph.items():
    print(k, v)

initial_candidate = ''.join(
    k for k, _ in sorted(
        graph.items(), key=lambda x: len(x[1]), reverse=True
    )
)
print("\nInitial candidate", initial_candidate)

print("\nTesting validity...")
if all(is_subsequence(pin, initial_candidate) for pin in data):
    print("Valid ✅")
else:
    print("Invalid ❌")
