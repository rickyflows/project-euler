#!/usr/bin/env python3
import numpy as np
from utils.priority_queue import PriorityQueue

def dijkstra(graph: np.ndarray, source: int):
    """Dijkstra's where the graph is given by an adjacency matrix"""
    m = len(graph)
    q = PriorityQueue()
    dist = float('inf') * np.ones((m,))
    prev = -1 * np.ones((m,), dtype=np.int64)
    visited = set()
    dist[source] = 0

    for v in range(m):
        q.put((dist[v], v))

    while len(q):
        _, u = q.pop()
        visited.add(u)
        for v in np.flatnonzero(graph[u]):
            if v in visited:
                continue
            alt = dist[u] + graph[u, v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                q.update_elem(v, (dist[v], v))
    return dist, prev
