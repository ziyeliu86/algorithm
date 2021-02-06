"""
The file scc.txt contains the edges of a directed graph.

Vertices are labeled as positive integers from 1 to 875714.
Every row indicates an edge, the vertex label in first column is the tail and
the vertex label in second column is the head (recall the graph is directed,
and the edges are directed from the first column vertex to the second column
vertex). :So for example, the 11th row looks like : "2 47646". This means that
the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing
strongly connected components (SCCs), and to run this algorithm on given graph.
"""


from itertools import groupby


def dfs_loop(graph, n):
    ne = [False] * n    # if node exlored
    ft = [0] * n        # finishing time
    ln = [0] * n        # lead node
    t = 0

    for i in range(n, 0, -1):
        if i % 50000 == 0:
            print("Processing node {:d}/{:d}".format(n-i, n))
        if not ne[i-1]:
            s = i
            t = dfs(graph, i, ne, ft, ln, t, s)

    return ft, ln


def dfs(graph, i, ne, ft, ln, t, s):
    ne[i-1] = True
    ln[i-1] = s
    Q = [i]
    P = []
    while Q:
        v = Q[-1]
        Q.pop(-1)
        P.append(v)
        ws = graph[v]
        if ws:
            for w in ws:
                if not ne[w-1]:
                    ne[w-1] = True
                    ln[w-1] = s
                    Q.append(w)

    for p in P[::-1]:
        t += 1
        ft[p-1] = t
    return t


def get_sizes(ln):
    sizes = [len(list(group)) for key, group in groupby(sorted(ln))]
    sizes.sort(reverse=True)

    if len(sizes) < 5:
        sizes += [0] * (5 - len(sizes))

    print(sizes[:5])

    return sizes


if __name__ == "__main__":

    # # A SIMPLE CASE TO TEST LOOP1
    # edges = [
    #     [7, 1], [4, 7], [1, 4], [9, 7],
    #     [6, 9], [3, 6], [9, 3], [8, 6],
    #     [2, 8], [5, 2], [8, 5]
    #     ]

    print("Read data")
    f = open("SCC.txt")
    edges = [[int(s) for s in line.split()] for line in f]
    n = max([node for e in edges for node in e])

    print("Get the reverse graph")
    graph = {(i + 1): [] for i in range(n)}
    for e in edges:
        graph[e[1]].append(e[0])

    print("Run DFS-Loop on Grev")
    ft, _ = dfs_loop(graph, n)

    print("Get the re-labeled graph")
    edges2 = [[ft[e[0]-1], ft[e[1]-1]] for e in edges]
    graph = {(i + 1): [] for i in range(n)}
    for e in edges2:
        graph[e[0]].append(e[1])

    print("Run DFS-loop on G")
    _, ln = dfs_loop(graph, n)

    print("Get SCC sizes")
    sizes = get_sizes(ln)
