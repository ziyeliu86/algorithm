"""
Here are data files describing three graphs: g1.txt, g2.txt, g3.txt.
The first line indicates the number of vertices and edges, respectively. Each
subsequent line describes an edge (the first two numbers are its tail and head,
respectively) and its length (the third number).
NOTE: some of the edge lengths are negative.
NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path". Precisely, you must first
identify which, if any, of the three graphs have no negative cycles. For each
such graph, you should compute all-pairs shortest paths and remember the
smallest one.

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the
box below.  If exactly one graph has no negative-cost cycles, then enter the
length of its shortest shortest path in the box below.  If two or more of the
graphs have no negative-cost cycles, then enter the smallest of the lengths of
their shortest shortest paths in the box below.

TODO: need to implement a heap structure for dijkstra's algorithm to process
big graph
"""


def dijkstra(graph, source):

    Q = list(graph.keys())
    dist = [1000000] * len(graph)
    prev = [None] * len(graph)

    dist[source-1] = 0

    while Q:

        distQ = [dist[v-1] for v in Q]
        u = Q[distQ.index(min(distQ))]
        Q.remove(u)

        for e in graph[u]:
            v, lengthuv = e
            alt = dist[u-1] + lengthuv
            if alt < dist[v-1]:
                dist[v-1] = alt
                prev[v-1] = u

    return dist, prev


def bellman_ford(edges, n, source):
    """This implementation takes in a graph, represented as lists of vertices
    (represented as integers [0..n-1]) and edges, and fills two arrays
    (distance and predecessor) holding the shortest path from the source to
    each vertex

    NOTE: vertices start from 0
    Examples:
    >>> edges = [
    >>>    (0, 1, 2), (1, 2, 2), (2, 3, 2),
    >>>    (0, 4, 4), (4, 3, 4), (1, 4, 1)
    >>>    ]
    >>> dist = bellman_ford(edges, 5, 0)
    >>> print(dist)
    [0, 2, 4, 6, 3]

    >>> edges = [
    >>>    (0, 1, 2), (1, 2, 2), (2, 3, 2),
    >>>    (4, 0, 1), (4, 3, 4), (1, 4, -5)
    >>>    ]
    >>> dist = bellman_ford(edges, 5, 0)
    >>> print(dist)
    Graph contains a negative-weight cycle
    None
    """

    # Step 1: initialize graph
    weights = [e[2] for e in edges]
    dist = [max(weights) * n] * n
    predecessor = [None] * n

    dist[0] = 0
    # Step 2: relax edges |V|−1 times
    for i in range(n-1):
        for (u, v, w) in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessor[v] = u
    # Step 3: check for negative-weight cycles
    for (u, v, w) in edges:
        if dist[u] + w < dist[v]:
            print("Graph contains a negative-weight cycle")
            return None

    return dist


def johnson_apsp(edges, n):
    """This function impements a Johnson's algorithm. This algorithm find the
    shortest paths between all pairs of vertices in an edge-weighted, directed
    graph. It allows some of the edge weights to be negative numbers, but no
    negative-weight cycles may exist. It works by using the Bellman–Ford
    algorithm to compute a transformation of the input graph that removes all
    negative weights, allowing Dijkstra's algorithm to be used on the
    transformed graph.
    https://en.wikipedia.org/wiki/Johnson%27s_algorithm

    NOTE: vertices start from 1

    Examples:
    >>> edges = [
    >>>     (1, 2, 2), (2, 3, 2), (3, 4, 2),
    >>>     (1, 5, 4), (5, 4, 4), (2, 5, 1)
    >>>     ]
    >>> dists = johnson_apsp(edges, 5)
    >>> print(dists)
    [[0, 2, 4, 6, 3], [1000000, 0, 2, 4, 1], [1000000, 1000000, 0, 2, 1000000],
    [1000000, 1000000, 1000000, 0, 1000000], [1000000, 1000000, 1000000, 4, 0]]

    >>> edges = [
    >>>    (1, 2, 2), (2, 3, 2), (3, 4, 2),
    >>>    (5, 1, 1), (5, 4, 4), (2, 5, -5)
    >>>    ]
    >>> dist = johnson_apsp(edges, 5)
    >>> print(dist)
    Graph contains a negative-weight cycle
    None
    """
    # Form G' by adding a new vertex s and a new edge (s, v) with length 0
    # for each v ∈ G. Original graph has node starts from 1, extended starts
    # from 0
    edges_extended = edges + [(0, i, 0) for i in range(1, n+1)]

    # Run Bellman-Ford on G' with source vertex s. [If B-F detects a
    # negative-cost cycle in G' (which must lie in G), halt + report this.]
    # For each v ∈ G , define p(v) = length of a shortest s → v path in G'.
    p = bellman_ford(edges_extended, n+1, 0)

    if p:
        edges_reweighted = edges.copy()
        # For each edge e = (u, v) ∈ G, define w'(e) = w(e) + p(u) − p(v)
        for i in range(len(edges)):
            u, v, w = edges[i]
            edges_reweighted[i] = (u, v, w + p[u] - p[v])

        # convert edges presentation to adjacency lists
        graph = {i: [] for i in range(1, n+1)}
        for (u, v, w) in edges_reweighted:
            graph[u].append((v, w))
        # For each vertex u of G : Run Dijkstra’s algorithm in G , with edge
        # lengths w'(e), with source vertex u, to compute the shortest-path
        # distance d'(u, v) for each v ∈ G
        dists = []
        for u in range(1, n+1):
            # print(f"Processing {u}/{n}")
            dist, _ = dijkstra(graph, u)
            # For each pair u, v ∈ G , return the shortest-path distance
            # d(u, v) := d'(u, v) − p(u) + p(v)
            for v in range(1, n+1):
                dist[v-1] = dist[v-1] - p[u-1] + p[v-1]
            dists.append(dist)
        return dists
    else:
        return None


if __name__ == "__main__":
    for file in ["g1.txt", "g2.txt", "g3.txt"]:
        f = open(file)
        lines = f.readlines()
        n, m = (int(s) for s in lines[0].split())
        edges = [[int(s) for s in line.split()] for line in lines[1:]]
        dists = johnson_apsp(edges, n)
        if dists:
            min_dist = min([d for ds in dists for d in ds])
            print(min_dist)

    # TODO: VERY SLOW, NEEDS FURTHER OPTIMIZATION OF CODE
    # f = open("large.txt")
    # lines = f.readlines()
    # n, m = (int(s) for s in lines[0].split())
    # edges = [[int(s) for s in line.split()] for line in lines[1:]]
    # dists = johnson_apsp(edges, n)
    # if dists:
    #     min_dist = min([d for ds in dists for d in ds])
    #     print(min_dist)
