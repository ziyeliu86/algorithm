import random


def random_contract(vertices, edges):
    vertices = vertices.copy()
    edges = edges.copy()

    while len(vertices) > 2:
        # random select an edge
        edge = random.choice(edges)

        # delete that edge
        while edge in edges:
            edges.remove(edge)
        while edge[::-1] in edges:
            edges.remove(edge[::-1])

        # merge nodes together
        v1 = edge[0]
        v2 = edge[1]

        vertices.remove(v2)

        for e in edges:
            if e[0] == v2:
                e[0] = v1
            if e[1] == v2:
                e[1] = v1

    return len(edges) // 2


if __name__ == "__main__":
    f = open("KargerMinCut.txt")
    array = [[int(s) for s in line.split()] for line in f]
    f.close()
    vs = [a[0] for a in array]
    # it should be noted that each edges has two records here [node A, node B]
    # and [Node B, Node A]
    es = [[a[0], a[i]] for a in array for i in range(1, len(a))]

    N = 2000
    min_cut = [0] * N

    for i in range(N):
        vs = [a[0] for a in array]
        # it should be noted that each edges has two records here
        # [node A, node B] and [Node B, Node A]
        es = [[a[0], a[i]] for a in array for i in range(1, len(a))]
        min_cut[i] = random_contract(vs, es)

    f = open("min_cut.txt", "w")
    f.write(str(min(min_cut)))
    f.close()
