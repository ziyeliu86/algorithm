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
        C[(tuple([k]), k)] = distances[k, 0]
    for s in range(2, n):
        subset = combinations(list(range(1, n)), s)
        for S in subset:
            for k in S:
                cskm = []
                for m in S:
                    if m != k:
                        sm = list(S).copy()
                        sm.remove(k)
                        sm = tuple(sm)
                        cskm.append(C[(sm, m)] + distances[k, m])
                        print(f"\nsm={sm}, k={k}, m={m}, C[(sm, m)]={C[(sm, m)]}, distances[k, m]={distances[k, m]}")
                C[tuple(S), k] = min(cskm)
                print(f"S={S}, k={k}, dist={min(cskm)}")
    print(C)
    fullpath = tuple(range(1, n))
    dists = [C[(fullpath, k)] + distances[0, k] for k in fullpath]
    return min(dists)


if __name__ == "__main__":
    # coord = np.loadtxt("tsp.txt", skiprows=1)
    # coord_diff = coord[np.newaxis, :, :] - coord[:, np.newaxis, :]
    # distances = np.sqrt((coord_diff ** 2).sum(axis=-1))
    # mindist = tsp_dp(distances)
    # print(mindist)

    distances = np.array([
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]])
    mindist = tsp_dp(distances)
    print(mindist)
