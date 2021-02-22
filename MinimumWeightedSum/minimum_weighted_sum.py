"""
In this programming problem and the next you'll code up the greedy algorithms
from lecture for minimizing the weighted sum of completion times..
This file describes a set of jobs with positive and integral weights and
lengths.  It has the format

[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...

For example, the third line of the file is "74 59", indicating that the second
job has weight 74 and length 59.
You should NOT assume that edge weights or lengths are distinct.

1. Your task in this problem is to run the greedy algorithm that schedules jobs
in decreasing order of the difference (weight - length).  Recall from lecture
that this algorithm is not always optimal.  IMPORTANT: if two jobs have equal
difference (weight - length), you should schedule the job with higher weight
first.  Beware: if you break ties in a different way, you are likely to get the
wrong answer. You should report the sum of weighted completion times of the
resulting schedule --- a positive integer.

Your task now is to run the greedy algorithm that schedules jobs (optimally) in
decreasing order of the ratio (weight/length).  In this algorithm, it does not
matter how you break ties.  You should report the sum of weighted completion
times of the resulting schedule --- a positive integer.
"""


def minimum_weighted_sum(weight, length, criterion):
    if criterion == "difference":
        orderby = [weight[i] - length[i] for i in range(len(weight))]
    if criterion == "ratio":
        orderby = [weight[i] / length[i] for i in range(len(weight))]

    order = [[orderby[i], weight[i], length[i]] for i in range(len(weight))]
    order.sort(reverse=True)    # sort by difference or ratio

    # initialize
    time = 0
    cost = 0
    for i in range(len(order)):
        time += order[i][2]     # cumulative time
        cost += time * order[i][1]      # cost += time * weight

    return cost


if __name__ == "__main__":
    f = open("jobs.txt")
    lines = f.readlines()
    weight = []
    length = []
    for line in lines[1:]:
        s = line.split()
        weight.append(int(s[0]))
        length.append(int(s[1]))

    print("Cost using difference as criterion: ")
    cost1 = minimum_weighted_sum(weight, length, "difference")
    print(cost1)

    print("Cost using ratio as criterion: ")
    cost2 = minimum_weighted_sum(weight, length, "ratio")
    print(cost2)
