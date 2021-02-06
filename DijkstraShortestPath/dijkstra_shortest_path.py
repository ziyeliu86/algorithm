# -*- coding: utf-8 -*-
"""
The file contains an adjacency list representation of an undirected weighted
graph with 200 vertices labeled 1 to 200.  Each row consists of the node tuples
that are adjacent to that particular vertex along with the length of that edge.
For example, the 6th row has 6 as the first entry indicating that this row
corresponds to the vertex labeled 6. The next entry of this row "141,8200"
indicates that there is an edge between vertex 6 and vertex 141 that has length
8200.  The rest of the pairs of this row indicate the other vertices adjacent
to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1
(the first vertex) as the source vertex, and to compute the shortest-path
distances between 1 and every other vertex of the graph. If there is no path
between a vertex vv and vertex 1, we'll define the shortest-path distance
between 1 and vv to be 1000000.
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


if __name__ == "__main__":
    f = open("dijkstraData.txt")
    graph = {}
    for line in f:
        s = line.split()
        v = int(s[0])
        cs = [c.split(",") for c in s[1:]]
        es = [(int(c[0]), int(c[1])) for c in cs]
        graph[v] = es

    dist, prev = dijkstra(graph, 1)

    targets = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

    answers = [''] * len(targets)
    for i in range(len(targets)):
        answers[i] = str(dist[targets[i]-1])
    answer = ','.join(answers)
    print(answer)
