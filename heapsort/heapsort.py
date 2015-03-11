import random, cProfile
import math
from base import *


class sort(testbase):
    name="heapsort"
    #Declare test type just to stay consistent
    heapsort = 0

    def __init__(self, size, ceiling, asInt, rtype):
        self.size = size
        self.gen  = randomizer.generator(maximum=ceiling,asInt=asInt)
        self.toSort = self.gen.gen(rtype,size)
        self.CEILING = ceiling
        self.INT = asInt
        self.PARTITIONTYPE = self.ptypes[rtype]
        start = time.perf_counter()
        self.begin= time.perf_counter()
        #pprint(self.toSort)
        self.heapsort(self.toSort)
        # self.toSort = self.mergesort1(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.SORTHELPERRTIME
        # pprint(self.toSort)
        self.setinfo()
        self.dump()





    def heapsort(self, A):
        self.SPLITS += 1
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
        start = int(math.floor((count - 2) / 2))

        while start >= 0:
            self.siftDown(A, start, count - 1)
            start -= 1



    def siftDown(self, A, start, end):
        s = time.perf_counter()
        root = start

        while root * 2 + 1 <= end:
            child = root * 2 + 1
            toSwap = root

            if A[toSwap] < A[child]:
                self.BASIC += 1
                toSwap = child

            #if a larger right child exists
            if child + 1 <= end and A[toSwap] < A[child + 1]:
                self.BASIC += 1
                toSwap = child + 1

            if toSwap == root:
                self.BASIC += 1
                # the root holds the largest element
                return

            else:
                self.BASIC += 1
                A[root], A[toSwap] = A[toSwap], A[root]
                root = toSwap



def run():
    srt = sort(size=size, ceiling=ceiling, asInt=isInt, rtype=partType)

run()
