# -*- coding: utf-8 -*-
"""
Programming Assignment #3

The goal of this problem is to implement the "Median Maintenance" algorithm
(covered in the Week 3 lecture on heap applications).
Two heaps are used. The min heap is used to store all the number larger than
median, the max heap is used to store all the number smaller than the median.

The text file contains a list of the integers from 1 to 10000 in unsorted order
you should treat this as a stream of numbers, arriving one by one.  Letting xi
denote the i th number of the file, the k th median mk is defined as the median
of the numbers x1, ..., xk. (So, if k is odd, then mk is ((k+1)/2)th smallest
number among x1, ..., xk. If k is even, then mk is the (k/2)th smallest number
among x1, ..., xk.


You should compute (m1 + m2 + m3 + ... + m10000) mod 10000.

import random
h = MedianHeap()
for i in range(300):
    h.insert(random.randint(1, 200))
    for a in h.small_half._queue:
        if a > h.small_half._queue[0]:
            print("Some thing wrong with small half")
    for a in h.large_half._queue:
        if a < h.small_half._queue[0]:
            print("Something wrong with large half")
    if h.small_half.length() < h.large_half.length():
        print("The length is not correct")

@author: ZIYE
"""


class MedianHeap():
    def __init__(self):
        self.small_half = Heap("max")  # numbers smaller than median, min heap
        self.large_half = Heap("min")  # numbers larger than median, max heap

    def median(self):
        return self.small_half.top()

    def insert(self, item):
        """insert item onto heap, maintaining the heap invariant."""

        if self.small_half.length() == 0:
            self.small_half.insert(item)

        else:
            # item <= median, add to samll half
            if item <= self.median():
                self.small_half.insert(item)
                if self.small_half.length() > self.large_half.length() + 1:
                    item2 = self.small_half.extract()
                    self.large_half.insert(item2)

            # item > median, add to large half
            else:
                self.large_half.insert(item)
                if self.large_half.length() > self.small_half.length():
                    item2 = self.large_half.extract()
                    self.small_half.insert(item2)
        # print(self.small_half._queue)
        # print(self.large_half._queue)


class Heap():
    def __init__(self, heap_type):
        self._queue = []
        self._heap_type = heap_type

    def length(self):
        return len(self._queue)

    def top(self):
        return self._queue[0]

    def insert(self, item):
        self._queue.append(item)
        pos = len(self._queue) - 1
        while pos > 0:
            parentpos = (pos - 1) >> 1
            if self._is_violated(pos, parentpos):
                # Swap item and parent
                self._queue[pos], self._queue[parentpos] = \
                    self._queue[parentpos], self._queue[pos]
                pos = parentpos
            else:
                break

    def _is_violated(self, pos, parentpos):
        if self._heap_type == "min":
            if self._queue[parentpos] > self._queue[pos]:
                return True
            else:
                return False
        else:
            if self._queue[parentpos] < self._queue[pos]:
                return True
            else:
                return False

    def extract(self, verbose=False):
        item = self._queue[0]
        self._queue[0] = self._queue[-1]
        self._queue.pop()
        pos = 0
        while pos < len(self._queue):
            left = pos * 2 + 1
            right = pos * 2 + 2
            swap = pos

            if left <= self.length() - 1:
                if self._is_violated(left, pos):
                    swap = left

            if right <= self.length() - 1:
                if self._is_violated(right, swap):
                    swap = right

            if swap != pos:
                self._queue[pos], self._queue[swap] = \
                    self._queue[swap], self._queue[pos]
                pos = swap
            else:
                break

        return item


if __name__ == "__main__":
    h = MedianHeap()
    f = open("Median.txt")
    array = [int(line) for line in f]
    medium_sum = 0
    for a in array:
        h.insert(a)
        medium_sum += h.median()
    print(medium_sum % 10000)
