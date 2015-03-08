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



class hsort:
    name="Ternary heapsort "
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
        self.ternaryheapsort(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.PARTITIONRTIME
        self.dump()



    def heapify(self, A, end, i):
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
        #print (A)


    def dump(self):
        pstr = "first/last"
        if (self.pivotType):
            pstr = "random"

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
    size = 100000
    ceiling = 100000
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

    srt = hsort(size=size, ceiling=ceiling, asInt=isInt, rtype=rtype)


run()