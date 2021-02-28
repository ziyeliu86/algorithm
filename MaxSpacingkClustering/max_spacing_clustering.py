"""
Question 1
The clustering algorithm from lecture for computing a max-spacing k-clustering.

clustering1.txt describes a distance function (equivalently, a complete graph
with edge costs).  It has the following format:

[number_of_nodes]
[edge 1 node 1] [edge 1 node 2] [edge 1 cost]
[edge 2 node 1] [edge 2 node 2] [edge 2 cost]
...

There is one edge (i,j) for each choice of 1 1≤i<j≤n, where n is the number of
nodes. For example, the third line of the file is "1 3 5250", indicating that
the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3))
is 5250.  You can assume that distances are positive, but you should NOT assume
that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on
this data set, where the target number k of clusters is set to 4.  What is the
maximum spacing of a 4-clustering?

Question 2
The format of clustering_big.txt is:

[# of nodes] [# of n_bits for each node's label]
[first bit of node 1] ... [last bit of node 1]
[first bit of node 2] ... [last bit of node 2]
...

In this question your task is again to run the clustering algorithm from
lecture, but on a MUCH bigger graph. So big, in fact, that the distances
(i.e., edge costs) are only defined implicitly, rather than being provided as
an explicit list.
For example, the third line of the file
"0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 n_bits
associated with node #2.

The distance between two nodes uu and vv in this problem is defined as the
Hamming distance--- the number of differing n_bits --- between the two nodes'
labels.  For example, the Hamming distance between the 24-bit label of node #2
above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3
(since they differ in the 3rd, 7th, and 21st n_bits).

The question is: what is the largest value of kk such that there is a
k-clustering with spacing at least 3?  That is, how many clusters are needed to
ensure that no pair of nodes with all but 2 n_bits in common get split into
different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably
can't write it out explicitly, let alone sort the edges by cost.  So you will
have to be a little creative to complete this part of the question.  For
example, is there some way you can identify the smallest distances without
explicitly looking at every pair of nodes?

NOTE: all node ID in this script starts from 1
"""


class UnionFind():
    """A python implementation of lazy union find data structure
    """
    def __init__(self, num_items):
        self._parents = list(range(1, num_items + 1))
        self._sizes = [1] * num_items
        self._num_group = num_items

    def find(self, i):
        if self._parents[i-1] != i:
            return self.find(self._parents[i-1])
        else:
            return i

    def cluster_num(self):
        return self._num_group

    def union(self, j, k):
        parent_j = self.find(j)
        parent_k = self.find(k)

        if parent_j == parent_k:
            return
        else:
            if self._sizes[parent_j - 1] > self._sizes[parent_k - 1]:
                self._parents[parent_k - 1] = parent_j
                self._sizes[parent_j - 1] += self._sizes[parent_k - 1]
            else:
                self._parents[parent_j - 1] = parent_k
                self._sizes[parent_k - 1] += self._sizes[parent_j - 1]
            self._num_group -= 1


def clustering(edges, n, k):
    # sort edges
    edges.sort(key=lambda x: x[2])

    clusters = UnionFind(n)
    i = 0
    cost = 0
    while clusters.cluster_num() >= k:
        [n1, n2, cost] = edges[i]
        if clusters.find(n1) != clusters.find(n2):
            clusters.union(n1, n2)
            max_spacing = cost
        i += 1
    return max_spacing


def node_mapping(nodes):
    """Convert the bit strings to integers and create a map (=dict) mapping
    from integer number => array of node IDs. Node ID starts from 1.
    """
    n = len(nodes)
    n_bits = len(nodes[1])
    nodes_map = {}
    for i in range(n):
        ints = [nodes[i][j] * (2 ** (n_bits - j - 1)) for j in range(n_bits)]
        mapped = sum(ints)
        if mapped not in nodes_map:
            nodes_map[mapped] = [i + 1]
        else:
            nodes_map[mapped].append(i + 1)
    return nodes_map


def generate_bit_mask(n_bits):
    """Create an array of bit-masks for the distances.
    """
    dist0 = 0
    dist1 = [1 << i for i in range(n_bits)]
    dist2 = []
    for i in range(n_bits-1):
        for j in range(i+1, n_bits):
            mask1 = 1 << i
            mask2 = 1 << j
            dist2.append(mask1 ^ mask2)
    mask = [dist0] + dist1 + dist2
    return mask


# def neighbor(i, nodes, unexplored_nodes):
#     node = nodes[i]
#     c1f24 = []
#     for j in range(n_bits):
#         c1f24.append(node.copy())
#         c1f24[-1][j] = 1 if c1f24[-1][j] == 0 else 0
#     c2f24 = []
#     for j in range(n_bits-1):
#         for k in range(j, n_bits):
#             c2f24.append(node.copy())
#             c2f24[-1][j] = 1 if c2f24[-1][j] == 0 else 0
#             c2f24[-1][k] = 1 if c2f24[-1][k] == 0 else 0
#     neighbors = [node] + c1f24 + c2f24
#     neighbor_nodes = []
#     for j in unexplored_nodes:
#         if nodes[j] in neighbors:
#             neighbor_nodes.append(j)
#     return neighbor_nodes


def clustering_big(nodes):
    n = len(nodes)
    n_bits = len(nodes[0])

    mapped_nodes = node_mapping(nodes)
    masks = generate_bit_mask(n_bits)

    clusters = UnionFind(n)

    for key in mapped_nodes:
        for mask in masks:
            if key ^ mask in mapped_nodes:
                neigh_nodes = mapped_nodes[key ^ mask]
                for node in neigh_nodes:
                    clusters.union(mapped_nodes[key][0], node)
    return clusters.cluster_num()


if __name__ == "__main__":
    f = open("clustering1.txt", "r")
    lines = f.readlines()
    n = int(lines[0])
    edges = [[int(s) for s in line.split()] for line in lines[1:]]
    max_spacing = clustering(edges, n, 4)
    print(max_spacing)

    f = open("clustering_big.txt", "r")
    lines = f.readlines()
    # n, n_bits = (int(s) for s in lines[0].split())
    nodes = [[int(s) for s in line.split()] for line in lines[1:]]
    cluster_num = clustering_big(nodes)
    print(cluster_num)
