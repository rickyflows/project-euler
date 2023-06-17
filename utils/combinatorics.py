#!/usr/bin/env python3
from typing import List, Set, Tuple

# def deep_copy(li: List[List]):
#     new_copy = [None] * len(li)
#     for i in range(len(li)):
#         new_copy[i] = li[i].copy()
#     return new_copy

def get_partitions(li: List) -> Set[Tuple[Tuple]]:
    if not li:
        return set()
    partitions = set([((li[0], ), )])
    for el in li[1:]:
        prev_partitions = partitions
        partitions = set()
        for pp in prev_partitions: # pp = previous partition
            singleton_partition = list(pp) + [(el, )]
            partitions.add(tuple(sorted(singleton_partition)))
            for ss in pp: # ss = subset
                join_partition = list(pp)
                join_partition.remove(ss)
                join_partition.append(tuple(list(ss) + [el]))
                partitions.add(tuple(sorted(join_partition)))
    return partitions
