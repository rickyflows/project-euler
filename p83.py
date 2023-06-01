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
            left = (i, j - 1)
            for v in filter(lambda u: in_square(u, m), [up, right, down, left]):
                graph[unfold((i, j), m), unfold(v, m)] = data[v]

    source = unfold((0, 0), m)
    dist, _ = dijkstra(graph, source)
    print(dist[-1] + data[0, 0])

if __name__=="__main__":
    main()
