import random, cProfile, argparse, time
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

class msort:
    name="mergesort"
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
        self.gen  = randomizer.generator(maximum=ceiling,asInt=asInt)
        self.toSort = self.gen.gen(rtype,size)
        end = len(self.toSort)
        B = [None] * end
        self.name = self.name + self.ptypes[rtype] +str(size)
        start = time.perf_counter()
        self.begin= time.perf_counter()
        self.mergesort(self.toSort,B, 0, end - 1)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.PARTITIONRTIME
        self.dump()

    def merge(self, A, B, start, middle, end):
        begin = time.perf_counter()
        B = copy(A)
        self.TOTALSPACE += len(B)
        i = start
        j = middle + 1

        for k in range(start, end + 1):
            if i > middle:
                self.BASIC +=1
                A[k] = B[j]
                j += 1

            elif j > end:
                self.BASIC +=2
                A[k] = B[i]
                i += 1

            elif B[j] < B[i]:
                self.BASIC +=3
                A[k] = B[j]
                j += 1

            else:
                A[k] = B[i]
                i += 1
        end  = time.perf_counter()
        self.PARTITIONRTIME += end - begin

    def mergesort(self, A, B, start, end):
        self.PART += 1
        if (end <= start):
            return
        middle = int(start + (end - start) / 2)
        self.mergesort(A, B, start, middle)
        self.mergesort(A, B, middle + 1, end)
        self.merge(A, B, start, middle, end)

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

    srt = msort(size=size, ceiling=ceiling, asInt=isInt, rtype=rtype)


run()
#cProfile.run('mergesort(list, B, start, end - 1)')
