"""
tsp.txt is a data file describing a TSP instance.

The first line indicates the number of cities.  Each city is a point in the
plane, and each subsequent line indicates the x- and y-coordinates of a single
city. The distance between two cities is defined as the Euclidean distance ---
that is, two cities at locations (x,y) and (z,w) have distance
sqrt{(x-z)^2 + (y-w)^2} between them.
"""


import numpy as np
from itertools import combinations


def tsp_dp(distances):
    """
    This function is an implemnation of Held–Karp algorithm.
    https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm

    Args:
        distances(N by N numpy array): distances[m, n] is the distance from
        vertice n to m
    Returns:
        the minium distance to travel all the vertices exactly once
    Examples:
    >>> distances = np.array([
    >>>    [0, 2, 9, 10],
    >>>    [1, 0, 6, 4],
    >>>    [15, 7, 0, 8],
    >>>    [6, 3, 12, 0]])
    >>> mindist = tsp_dp(distances)
    >>> print(mindist)
    21
    """
    C = {}
    n, _ = distances.shape
    # C(S, k) is the minimum distance, starting at city 0, visiting all cities
    # in S and finishing at city k
    for k in range(1, n):
        C[(1 << k, k)] = distances[k, 0]
    for s in range(2, n):
        C2 = {}
        print(f"Processing {s-1}/{n-1}")
        for S in combinations(list(range(1, n)), s):
            bits = 0
            for bit in S:
                bits |= 1 << bit
            for k in S:
                prev = bits & ~(1 << k)
                cskm = []
                for m in S:
                    if m == k:
                        continue
                    cskm.append(C[(prev, m)] + distances[k, m])
                C2[bits, k] = min(cskm)
                # print(C2)
        C = C2
    # print(C)
    bits = (2 ** n - 1) - 1
    fullpath = tuple(range(1, n))
    dists = [C[(bits, k)] + distances[0, k] for k in fullpath]
    return min(dists)


if __name__ == "__main__":
    coord = np.loadtxt("tsp.txt", skiprows=1)
    coord_diff = coord[np.newaxis, :, :] - coord[:, np.newaxis, :]
    distances = np.sqrt((coord_diff ** 2).sum(axis=-1))
    mindist = tsp_dp(distances)
    print(mindist)
