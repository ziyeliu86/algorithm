"""
mwis.txt describes the weights of the vertices in a path graph (with the
weights listed in the order in which vertices appear in the path). It has the
following format:

[number_of_vertices]
[weight of first vertex]
[weight of second vertex]
...

For example, the third line of the file is "6395702," indicating that the
weight of the second vertex of the graph is 6395702.

Your task in this problem is to run the dynamic programming algorithm (and the
reconstruction procedure) from lecture on this data set.
The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones
belong to the maximum-weight independent set?  (By "vertex 1" we mean the first
vertex of the graph---there is no vertex 0.)   In the box below, enter a 8-bit
string, where the ith bit should be 1 if the ith of these 8 vertices is in the
maximum-weight independent set, and 0 otherwise. For example, if you think that
the vertices 1, 4, 17, and 517 are in the maximum-weight independent set and
the other four vertices are not, then you should enter the string 10011010 in
the box below.
"""


def max_weight_independent_set(weights):
    n = len(weights)
    A = [0] * (n + 1)
    A[1] = weights[0]
    for i in range(1, n):
        A[i+1] = max(A[i], A[i-1] + weights[i])

    indset = []
    i = n
    while i >= 1:
        if A[i-1] >= A[i-2] + weights[i-1]:
            i -= 1
        else:
            indset.append(i-1)
            i -= 2
    return indset


if __name__ == "__main__":
    f = open("mwis.txt", "r")
    lines = f.readlines()
    weights = [int(line) for line in lines[1:]]
    indset = max_weight_independent_set(weights)
    checklist = [1, 2, 3, 4, 17, 117, 517, 997]
    out1 = [str(int(i-1 in indset)) for i in checklist]
    out2 = "".join(out1)
    print(out2)
