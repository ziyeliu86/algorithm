"""
Prim's minimum spanning tree algorithm.

This file job.txt describes an undirected graph with integer edge costs. It has
the format

[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...

For example, the third line of the file is "2 3 -8874", indicating that there
is an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that
they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You
should report the overall cost of a minimum spanning tree --- an integer, which
may or may not be negative.

This graph is small enough that the straightforward O(mn) time implementation
of Prim's algorithm should work fine.
TO DO: Implementing a heap-based version.
The simpler approach, which should already give you a healthy speed-up, is to
maintain relevant edges in a heap (with keys = edge costs).  The superior
approach stores the unprocessed vertices in the heap, as described in lecture.
Note this requires a heap that supports deletions, and you'll probably need to
maintain some kind of mapping between vertices and their positions in the heap.
"""

import random


def prim_minimum_span(n, m, edges):
    # some initialization
    random_vertice = random.randint(1, n+1)
    X = [random_vertice]    # spanned by tree T
    T = []                  # tree
    cost = 0

    # an edge dictionary to easy find edges associated with a vertice
    edge_dict = {i: [] for i in range(1, n+1)}
    for e in edges:
        edge_dict[e[0]].append((e[0], e[1], e[2]))
        edge_dict[e[1]].append((e[1], e[0], e[2]))

    # A dictionary of vertices which have edges associated with the front of X
    # q_dict[v] = (cost, u) where v in V-X, and u in X
    inf_cost = max([e[2] for e in edges]) + 1
    q_dict = {i: (inf_cost, 0) for i in range(1, n + 1) if i != random_vertice}

    for e in edge_dict[random_vertice]:
        q_dict[e[1]] = (e[2], e[0])

    while len(X) != n:
        # Get the node in V-X with the least distance to X
        v = min(q_dict, key=q_dict.get)
        c, u = q_dict[v]
        q_dict.pop(v)
        cost += c

        X.append(v)
        T.append((u, v))

        # find all v-> w
        vw = edge_dict[v]   # all the edges associated with v
        for e in vw:
            w = e[1]
            if w not in X:
                # find key[w]
                if e[2] < q_dict[w][0]:
                    q_dict[w] = (e[2], v)
    return T, cost


if __name__ == "__main__":
    f = open("edges.txt", "r")
    lines = f.readlines()
    n, m = (int(s) for s in lines[0].split())
    edges = [[int(s) for s in line.split()] for line in lines[1:]]
    _, cost = prim_minimum_span(n, m, edges)
    print(cost)
