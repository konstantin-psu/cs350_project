import random, cProfile, time, scipy, argparse, math
from numpy import copy
import time
from numpy import copy
from base import *


class hsort(testbase):
    name="Ternary heapsort "
    def __init__(self, size, ceiling, asInt, rtype):
        self.size = size
        self.gen  = randomizer.generator(maximum=ceiling,asInt=asInt)
        self.toSort = self.gen.gen(rtype,size)
        self.CEILING = ceiling
        self.INT = asInt
        self.PARTITIONTYPE = self.ptypes[rtype]
        #B = [None] * end
        start = time.perf_counter()
        self.begin = time.perf_counter()
        self.ternaryheapsort(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.SORTHELPERRTIME
        self.setinfo()
        self.dump()



    def heapify(self, A, end, i):
        self.BASIC  += 1
        firstChild = 3 * i + 1
        lastChild = min(firstChild + 3, end)
        children = list(range(firstChild, lastChild))
        maxElement = max((A[j], j) for j in [i] + children)
        #maxValue, \
        maxIndex = maxElement[1]
        if maxIndex != i:
            A[i], A[maxIndex] = A[maxIndex], A[i]
            self.heapify(A, end, maxIndex)

    def ternaryheapsort(self, A):
        end = len(A)
        start = end // 2
        for i in reversed(range(start)):
            self.heapify(A, end, i)
        for i in reversed(range(end)):
            A[i], A[0] = A[0], A[i]
            self.heapify(A, i, 0)


def run():
    srt = hsort(size=size, ceiling=ceiling, asInt=isInt, rtype=rtype)


run()