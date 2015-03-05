import random, cProfile, argparse, time
import randomizer
import time
from numpy import copy
import argparse
from base import *
from heapq import merge


parser = argparse.ArgumentParser(description='Test harness arguments parser')
parser.add_argument('-t', dest = 'type', type=int, help= 'Test type, can be empty')
parser.add_argument('-s', dest = 'inputSize', type=int, help='Array size')
parser.add_argument('-pt', dest = 'partType', type=int, help = 'Partition Type')
parser.add_argument('-c', dest = 'ceiling', type=int, help='Ceiling of values to be created for our array, if ceiling is less than input size, and type is set as integer, then by pigeon principle array will have duplicates')
parser.add_argument('-i', dest = 'asInt', type=int, help='Array content type, if 1 then content is integers, 0 for floats')
parser.add_argument('-piv', dest = 'Pivot', type=int, help='This is valuable only for quick sort, if 1 - random, else if 0 - first/last')
args = parser.parse_args()


class msort(testbase):
    name="mergesort"
    #Declare test type just to stay consistent
    margesort = 0

    def __init__(self, size, ceiling, asInt, rtype):
        self.size = size
        self.gen  = randomizer.generator(maximum=ceiling,asInt=asInt)
        self.toSort = self.gen.gen(rtype,size)
        self.CEILING = ceiling
        self.INT = asInt
        self.PARTITIONTYPE = self.ptypes[rtype]
        end = len(self.toSort)
        B = [None] * end
        self.filename = self.name + "_test_results.json"
        start = time.perf_counter()
        self.begin= time.perf_counter()
        # self.mergesort(self.toSort,B, 0, end - 1)
        self.toSort = self.mergesort1(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.SORTHELPERRTIME
        # pprint(self.toSort)
        self.setinfo()
        pprint(self.info)
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
        self.SORTHELPERRTIME += end - begin

    def mergesort(self, A, B, start, end):
        self.SPLITS += 1
        if (end <= start):
            return
        middle = int(start + (end - start) / 2)
        self.mergesort(A, B, start, middle)
        self.mergesort(A, B, middle + 1, end)
        self.merge(A, B, start, middle, end)

    def merge1(self, A, B):
        begin = time.perf_counter()
        l1 = len(A)
        l2 = len(B)
        # C = list(merge(A,B)) #Fixme! no way to count basic operations, implement merge!
        C = []
        i = 0
        j = 0
        while i < l1 and j < l2:
            if A[i] <= B[j]:
                self.BASIC +=1
                C.append(A[i])
                i += 1
            else:
                self.BASIC +=1
                C.append(B[j])
                j += 1
        while i < l1:
            self.BASIC +=1
            C.append(A[i])
            i += 1
        while j < l2:
            self.BASIC +=1
            C.append(B[j])
            j += 1
        end  = time.perf_counter()
        self.SORTHELPERRTIME += end - begin
        self.TOTALSPACE += len(C)
        return C

    def mergesort1(self, A):
        self.SPLITS += 1
        if (len(A) <= 1):
            return A
        start = 0
        end = len(A) - 1
        middle = int(start + (end - start) / 2)
        l = self.mergesort1(A[start:middle+1])
        r = self.mergesort1(A[middle + 1: end+1])
        return self.merge1(l, r)



def run():
    partType = Uniform
    size = 1000000
    ceiling = 100
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

    srt = msort(size=size, ceiling=ceiling, asInt=isInt, rtype=partType)


run()
#cProfile.run('mergesort(list, B, start, end - 1)')
