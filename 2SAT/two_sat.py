"""
This is an implementation of solving 2SAT problem using strongly connected
cycles.
"""


def dfs_loop(graph, n):
    ne = [False] * n    # if node exlored
    ft = [0] * n        # finishing time
    ln = [0] * n        # lead node
    t = 0

    for i in range(n, 0, -1):
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


def get_node_label(literal, n):
    """node label 1, 2, ..., n for literal 1, 2, ..., n
    nodel label n+1, n+2, ..., 2n for literal -1, -2, ..., -n
    """
    if literal > 0:
        return literal
    else:
        return (- literal + n)


def solve_2sat_scc(n, clauses):
    """This function implements a strongly connected component algorithm for
    2SAT problem
    Args:
        n: number of literals
        clauses: a list of clauses for the literals to satisfy

    Examples:
    >>> clauses = [[1, 2], [-1, 2], [1, -2], [-1, -2]]
    >>> has_solution = solve_2sat_scc(2, clauses)
    Run DFS-Loop on gt
    Get the re-labeled graph
    Run DFS-loop on g
    Check if instance satisfiable
    Instance is not statisfiable.

    >>> clauses = [[1, -2], [-1, 2], [-1, -2], [1, -3]]
    >>> has_solution = solve_2sat_scc(3, clauses)
    Run DFS-Loop on gt
    Get the re-labeled graph
    Run DFS-loop on g
    Check if instance satisfiable
    Instance is not statisfiable.
    """
    # convert clauses to implication graph
    g = {(i + 1): [] for i in range(n * 2)}
    gt = {(i + 1): [] for i in range(n * 2)}
    for c in clauses:
        gt[get_node_label(c[0], n)].append(get_node_label(-c[1], n))
        gt[get_node_label(c[1], n)].append(get_node_label(-c[0], n))

    print("Run DFS-Loop on gt")
    ft, _ = dfs_loop(gt, n * 2)

    print("Get the re-labeled graph")
    for c in clauses:
        g[ft[get_node_label(-c[0], n)-1]].append(ft[get_node_label(c[1], n)-1])
        g[ft[get_node_label(-c[1], n)-1]].append(ft[get_node_label(c[0], n)-1])

    print("Run DFS-loop on g")
    _, ln = dfs_loop(g, n * 2)
    # Get the lead node of the original node labels
    lno = [ln[ft[i]-1] for i in range(2*n)]

    print("Check if instance satisfiable")
    for i in range(n):
        if lno[i] == lno[i+n]:
            print("Instance is not statisfiable.\n")
            return False
    print("Instance is statisfiable.\n")
    return True


if __name__ == "__main__":
    has_solutions = [""] * 6
    for i in range(1, 7):
        file = "2sat{:d}.txt".format(i)
        print("Read data from {:s}".format(file))
        f = open(file)
        lines = f.readlines()
        n = int(lines[0])
        clauses = [[int(s) for s in line.split()] for line in lines[1:]]
        has_solutions[i-1] = str(int(solve_2sat_scc(n, clauses)))
    answer = "".join(has_solutions)
    print("\n\nAnswer is ", answer)
