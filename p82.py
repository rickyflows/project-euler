#!/usr/bin/env python3
import numpy as np
from utils.graphs import dijkstra

def in_square(coord, side_length):
    return 0 <= coord[0] < side_length and 0 <= coord[1] < side_length

def unfold(coord, side_length):
    x, y = coord
    return side_length * x + y

def fold(coord, side_length):
    return coord // side_length, coord % side_length

def main():
    data = np.array(
        [list(map(int, line.split(','))) for line in open('data/matrix.txt')]
    )

    m = len(data)
    graph = np.zeros((m**2, m**2))
    for i in range(m):
        for j in range(m):
            up = (i - 1, j)
            right = (i, j + 1)
            down = (i + 1, j)
            for v in filter(lambda u: in_square(u, m), [up, right, down]):
                graph[unfold((i, j), m), unfold(v, m)] = data[v]

    # O(m^5)
    candidates = set()
    for i in range(m):
        source = unfold((i, 0), m)
        dist, _ = dijkstra(graph, source)
        candidate = data[fold(source, m)] + min(dist.reshape(m, m)[:, -1])
        candidates.add(candidate)
    print(min(candidates))

if __name__=="__main__":
    # Some improvements:
    # - https://projecteuler.net/action=quote;post_id=391868 (O(m^3))
    # - https://projecteuler.net/action=quote;post_id=400861 (O(m^3))
    # - https://projecteuler.net/action=quote;post_id=399206 (O(m^2))
    main()
