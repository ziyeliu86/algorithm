"""Application of hashing to find the equal sum count
The goal of this problem is to implement a variant of the 2-SUM algorithm
covered in this week's lectures.

The file contains 1 million integers, both positive and negative (there might
be some repetitions!). This is your array of integers, with the i th row of the
file specifying the i th entry of the array.

Your task is to compute the number of target values t in the interval
[-10000,10000] (inclusive) such that there are distinct numbers x,y in the
input file that satisfy x+y=t.
(NOTE: ensuring distinctness requires a one-line addition to the algorithm from
lecture.)
"""


if __name__ == "__main__":
    f = open("algo1-programming_prob-2sum.txt")
    array = [int(line) for line in f]
    bucket = {}
    t = []

    for x in array:
        key = x // 10000
        if key in bucket:
            bucket[key].append(x)
        else:
            bucket[key] = [x]

        for k in [- key - 2, - key - 1, - key, - key + 1]:
            if k in bucket:
                for y in bucket[k]:
                    xysum = x + y
                    if (x != y) and (-10000 <= xysum <= 10000):
                        t.append(xysum)
                        # if xysum not in t:
                        #     t.append(xysum)

    print(len(set(t)))
