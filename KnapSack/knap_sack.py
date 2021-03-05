"""
Question 1
knapsack1.txt describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]
[value_1] [weight_1]
[value_2] [weight_2]
...

For example, the third line of the file is "50074 659", indicating that the
second item has value 50074 and size 659, respectively.

You can assume that all numbers are positive.  You should assume that item
weights and the knapsack capacity are integers.

Question 2
knapsack_big.txt describes a knapsack instance, and it has the following
format:

[knapsack_size][number_of_items]
[value_1] [weight_1]
[value_2] [weight_2]
...

For example, the third line of the file is "50074 834558", indicating that
the second item has value 50074 and size 834558, respectively.  As before,
you should assume that item weights and the knapsack capacity are integers.

This instance is so big that the straightforward iterative implemetation uses
an infeasible amount of time and space.  So you will have to be creative to
compute an optimal solution.  One idea is to go back to a recursive
implementation, solving subproblems --- and, of course, caching the results to
avoid redundant work --- only on an "as needed" basis.  Also, be sure to think
about appropriate data structures for storing and looking up solutions to
subproblems.
"""

import sys


def knapsack(knapsack_size, items):
    n = len(items)
    A = [[0 for i in range(knapsack_size+1)] for j in range(n+1)]

    for i in range(1, n+1):
        v = items[i-1][0]
        w = items[i-1][1]
        for x in range(knapsack_size+1):
            if x - w < 0:
                A[i][x] = A[i-1][x]
            else:
                A[i][x] = max(A[i-1][x], A[i-1][x-w] + v)
    return A[-1][-1]


def big_knapsack(knapsack_size, items, A={}):
    n = len(items)

    if n not in A:
        A[n] = {}
    if n == 0:
        if knapsack_size not in A[n]:
            A[n][knapsack_size] = 0
        return A[n][knapsack_size]
    if n in A:
        if knapsack_size in A[n]:
            return A[n][knapsack_size]

    if n - 1 not in A:
        A[n-1] = {}
    v = items[-1][0]
    w = items[-1][1]
    if knapsack_size not in A[n-1]:
        A[n-1][knapsack_size] = big_knapsack(knapsack_size, items[:-1], A)
    if knapsack_size > w:
        if knapsack_size - w not in A[n-1]:
            A[n-1][knapsack_size-w] = big_knapsack(
                knapsack_size-w, items[:-1], A)
        A[n][knapsack_size] = max(
            A[n-1][knapsack_size],
            A[n-1][knapsack_size-w] + v
            )
    else:
        A[n][knapsack_size] = A[n-1][knapsack_size]
    return A[n][knapsack_size]


if __name__ == "__main__":
    # items = [[3, 4], [2, 3], [4, 2], [4, 3]]
    # knapsack_size = 6
    f = open("knapsack1.txt", "r")
    lines = f.readlines()
    knapsack_size, _ = (int(s) for s in lines[0].split())
    items = [[int(s) for s in line.split()] for line in lines[1:]]
    max_value = knapsack(knapsack_size, items)
    print(max_value)
    sys.setrecursionlimit(2000000)
    f = open("knapsack_big.txt", "r")
    lines = f.readlines()
    knapsack_size, _ = (int(s) for s in lines[0].split())
    items = [[int(s) for s in line.split()] for line in lines[1:]]
    max_value = big_knapsack(knapsack_size, items)
    print(max_value)
