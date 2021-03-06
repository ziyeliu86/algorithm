"""
Problem:
Sorted set of keys k1, k2, ..., kn
Key probabilities: p1, p2, ..., pn
What tree structure has lowest expected cost?
Cost of searching for node i: cost(ki) = depth(ki) + 1
"""


def optimal_bst(p, i, j, C={}):
    if (i, j) in C:
        return C[(i, j)]
    if i > j:
        return 0
    elif i == j:
        return p[i]
    else:
        minC = 1000
        for k in range(i, j+1):
            C[(i, k - 1)] = optimal_bst(p, i, k - 1, C)
            C[(k + 1, j)] = optimal_bst(p, k + 1, j, C)
            minC = min(minC, C[(i, k - 1)] + C[(k + 1, j)] + sum(p[i:j+1]))
        return minC


if __name__ == "__main__":
    # p = [0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25]
    p = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
    min_cost = optimal_bst(p, 0, len(p)-1)
    print(min_cost)
