"""
huffman.txt describes an instance of the problem. It has the following format:

[number_of_symbols]
[weight of symbol #1]
[weight of symbol #2]
...

For example, the third line of the file is "6852892," indicating that the
weight of the second symbol of the alphabet is 6852892.  (We're using weights
instead of frequencies, like in the "A More Complex Example" video.)

Your task in this problem is to run the Huffman coding algorithm from lecture
on this data set. What is the maximum and minimum length of a codeword in the
resulting Huffman code?
"""


import heapq


def huffman_coding(weights):
    n = len(weights)
    # nodes = weight, index
    nodes = [[weights[i], i] for i in range(n)]
    heapq.heapify(nodes)

    parents = [None] * n
    max_node = n
    while len(nodes) > 1:
        node1 = heapq.heappop(nodes)
        node2 = heapq.heappop(nodes)
        node = [node1[0] + node2[0], max_node]
        parents[node1[1]] = max_node
        parents[node2[1]] = max_node
        parents.append(None)

        heapq.heappush(nodes, node)
        max_node += 1

    code_length = [0] * n
    for i in range(n):
        parent = parents[i]
        while parent:
            parent = parents[parent]
            code_length[i] += 1

    return max(code_length), min(code_length)


if __name__ == "__main__":
    f = open("huffman.txt", "r")
    lines = f.readlines()
    weights = [int(line) for line in lines[1:]]
    max_length, min_length = huffman_coding(weights)
    print(max_length, min_length)
