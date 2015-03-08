import random, cProfile, time, scipy, argparse, math
from numpy import copy
import randomizer
import time
from numpy import copy
import argparse


parser = argparse.ArgumentParser(description='Get input size')
parser.add_argument('-t', dest = 'type', type=int)
parser.add_argument('-s', dest = 'inputSize', type=int)
parser.add_argument('-pt', dest = 'partType', type=int)
parser.add_argument('-c', dest = 'ceiling', type=int)
parser.add_argument('-i', dest = 'asInt', type=int)
parser.add_argument('-piv', dest = 'Pivot', type=int)

args = parser.parse_args()

Gauss = 0
Uniform = 1
Sorted = 2
Reverse = 3
Identical = 4
S25 = 5
S85 = 6



class buhsort:
    name="bottomup_heapsort "
    BASIC=0
    size=0
    PART=0
    SPLITRTIME=0
    TOTALRTIME=0
    PARTITIONRTIME=0
    TOTALSPACE=0
    dpl=0
    toSort=0
    pstr=0
    TOTALRTIME=0
    pivotType='Null'
    ptypes = {
       0: 'gauss',
       1: 'uniform',
       2: 'sorted',
       3: 'reverse',
       4: 'identical',
       5: 's25',
       6: 's85',
       }


    def __init__(self, size, ceiling, asInt, rtype):
        self.size = size
        self.gen  = randomizer.generator(maximum=ceiling, asInt=asInt)
        self.toSort = self.gen.gen(rtype, size)
        end = len(self.toSort)
        #B = [None] * end
        self.name = self.name + self.ptypes[rtype] +str(size)
        start = time.perf_counter()
        self.begin = time.perf_counter()
        self.heapsort(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.PARTITIONRTIME
        self.dump()



    def heapsort(self, A):

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
            self.siftDown(A, start, count - 1)
            start -= 1



    def leafSearch(self, A, i, end):
        j = i
        while (2 * j) >= end:
            if (2 * j + 1) < end and (A[2 * j + 1] > A[2*j]):
                j = 2 * j + 1
            else:
                j = 2 * j
        return j


    def siftDown(self, A, i, end):
        j = self.leafSearch(A, end, i)


        while A[i] > A[j]:
            parent = int(math.floor((j - 1)/2))
            j = parent
        x = A[j]
        A[j] = A[i]
        while j > i:
            x, A[parent] = A[parent], x
            j = parent


    def dump(self):
        pstr = "first/last"
        if (self.pivotType):
            pstr = "random"

        print(self.toSort)
        print("name:                 " + self.name)
        print("basic operations:     " + str(self.BASIC))
        print("size:                 " + str(self.size))
        print("partition operations: " + str(self.PART))
        print("total split time:     " + str(self.SPLITRTIME))
        print("total time:           " + str(self.TOTALRTIME))
        print("total partition:      " + str(self.PARTITIONRTIME))
        print("total space:          " + str(self.TOTALSPACE))
        print("number of duplicates: " + str(self.dpl))
        print("actual length:        " + str(len(self.toSort)))
        print("pivot type   :        " + pstr)
        print("elapsed time = {:.12f} seconds".format(self.TOTALRTIME))


def run():
    partType = Reverse
    size = 10000
    ceiling = 10000
    rtype = Uniform
    # pivotType = True
    pivotType = False
    isInt = True
    if args.inputSize is not None:
        size = args.inputSize
    if args.type is not None:
        rtype = args.type
    if args.partType is not None:
        partType = args.partType
    if args.ceiling is not None:
        ceiling = args.ceiling
    if args.asInt is not None:
        isInt = bool(args.asInt)
    if args.Pivot is not None:
        pivotType = bool(args.Pivot)

    srt = buhsort(size=size, ceiling=ceiling, asInt=isInt, rtype=rtype)


run()

