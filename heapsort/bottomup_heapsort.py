import random, cProfile, time, scipy, argparse, math
from numpy import copy
import randomizer
import time
from numpy import copy
import argparse
from base import  *


class buhsort(testbase):
    name="bottomup_heapsort "
    bottomup = 0
    filename = "bottomUpHeapsort_results.json"

    def __init__(self, size, ceiling, asInt, rtype):
        self.size = size
        self.gen  = randomizer.generator(maximum=ceiling, asInt=asInt)
        self.toSort = self.gen.gen(rtype,size)
        self.CEILING = ceiling
        self.INT = asInt
        self.PARTITIONTYPE = self.ptypes[rtype]
        start = time.perf_counter()
        self.begin= time.perf_counter()
        self.heapsort(self.toSort)
        # self.toSort = self.mergesort1(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.SORTHELPERRTIME
        # pprint(self.toSort)
        self.setinfo()
        self.dump()


    def swim(self, k, A):
        while True:
            # zero-based indexing
            j = int((k - 1) / 2)
            if (j < 0) or (A[j] >= A[k]):
                break
            A[k], A[j] = A[j], A[k]
            k = j


    def heapify_swim(self, A, N):
        for i in range(1, N):
            self.swim(i, A)

    def heapsort(self, A):
        count = len(A)
        self.heapify_swim(A, count)

        for hi in range(count - 1, 0, -1):
            A[0], A[hi] = A[hi], A[0]
            self.sink(A, 0, hi - 1)


    def sink(self, A, k, high):
        while True:
            j = 2 * k + 1
            if j < high and (A[j] < A[j+1]):
                j += 1
            if j > high or not (A[k] < A[j]):
                break
            A[k], A[j] = A[j], A[k]
            k = j


def run():
    srt = buhsort(size=size, ceiling=ceiling, asInt=isInt, rtype=rtype)


run()

