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
        self.gen  = randomizer.generator(maximum=ceiling,asInt=asInt)
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

    def heapsort(self, A):
        self.SPLITS +=1
        count = len(A)
        self.heapify(A, count)

        end = count - 1
        while end > 0:
            #swap A[end] and A[0]
            A[end], A[0] = A[0], A[end]

            #reduce heap size by 1
            end -= 1

            self.siftDown(A, 0, end)


    #common in-place heap construction routine
    def heapify(self, A, count):
        start = int(math.floor((count - 1) / 2))
        while start >= 0:
            self.BASIC += 1
            self.siftDown(A, start, count - 1)
            start -= 1



    def leafSearch(self, A, i, end):
        j = i
        while (2 * j) >= end:
            if (2 * j + 1) < end and (A[2 * j + 1] > A[2*j]):
                self.BASIC += 2
                j = 2 * j + 1
            else:
                self.BASIC += 2
                j = 2 * j
        return j

    def siftDown(self, A, i, end):
        j = self.leafSearch(A, end, i)

        while A[i] > A[j]:
            self.BASIC += 1
            parent = int(math.floor((j - 1)/2))
            j = parent
        x = A[j]
        A[j] = A[i]
        while j > i:
            self.BASIC += 1
            x, A[parent] = A[parent], x
            j = parent




def run():
    srt = buhsort(size=size, ceiling=ceiling, asInt=isInt, rtype=rtype)


run()

