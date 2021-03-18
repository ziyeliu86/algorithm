"""
This implements a heuristic for the TSP, rather than an exact algorithm, and as
a result will be able to handle much larger problem sizes.  Here is a data file
describing a TSP instance
(original source: http://www.math.uwaterloo.ca/tsp/world/bm33708.tsp).


The first line indicates the number of cities. Each city is a point in the
plane, and each subsequent line indicates the x- and y-coordinates of a single
city.

The distance between two cities is defined as the Euclidean distance --- that
is, two cities at locations (x,y)(x,y) and (z,w)(z,w) have distance
sqrt[(x-z)^2 + (y-w)^2] between them.

1.  Start the tour at the first city.
2.  Repeatedly visit the closest city that the tour hasn't visited yet.
    In case of a tie, go to the closest city with the lowest index.
    For example, if both the third and fifth cities have the same distance from
    the first city (and are closer than any other city), then the tour should
    begin by going from the first city to the third city.
3.  Once every city has been visited exactly once, return to the first city to
    complete the tour.
"""


import numpy as np


def greedy_tsp(coords):
    """This function is an implementation of greedy algorithm for travelling
    sales man problem

    Examples
    >>> coords = np.array([
    >>>    [1, 1, 2],
    >>>    [2, 5, 8],
    >>>    [3, 1, 3],
    >>>    [4, 1, 4],
    >>>    [5, 2, 4]
    >>> ])
    >>> mindist, path = greedy_tsp(coords)
    >>> print(mindist)
    15.21110255092798
    >>> print(path)
    [1, 3, 4, 5, 2, 1]

    """
    mindist = 0
    origin_coord = coords[0, 1:]
    start = 0
    path = [coords[0, 0]]
    while coords.shape[0] > 1:
        start_coord = coords[start, 1:]
        coords = np.delete(coords, start, 0)
        squared_dists = ((coords[:, 1:] - start_coord) ** 2).sum(axis=1)
        start = np.argmin(squared_dists)
        mindist += np.sqrt(squared_dists[start])
        path.append(coords[start, 0])
    end_coord = coords[start, 1:]
    mindist += np.sqrt(((end_coord - origin_coord) ** 2).sum())
    path.append(path[0])
    return mindist, path


if __name__ == "__main__":
    coords = np.loadtxt("nn.txt", skiprows=1)
    mindist, _ = greedy_tsp(coords)
    print(mindist)
