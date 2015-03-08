import random, cProfile, time, scipy, argparse
from numpy import copy
import randomizer
import time
from numpy import copy
from base import *



class mbupsort(testbase):
    name="BottomUpmergesort"
    #Declare test type just to stay consistent
    mergesort = 0
    mergesort1 = 1

    def __init__(self, size, ceiling, asInt, rtype):
        self.size = size
        self.gen  = randomizer.generator(maximum=ceiling,asInt=asInt)
        self.toSort = self.gen.gen(rtype,size)
        self.CEILING = ceiling
        self.INT = asInt
        self.PARTITIONTYPE = self.ptypes[rtype]
        end = len(self.toSort)
        B = [None] * end
        start = time.perf_counter()
        self.begin= time.perf_counter()
        self.bottomupsort(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.SORTHELPERRTIME
        self.setinfo()
        self.dump()

# list = random.sample(range(size), size)
# cProfile.run('bottomupsort(list)')

    def bottomupmerge(self, A, B, start, middle, end):
        self.SPLITS += 1
        begin = time.perf_counter()
        B = copy(A)

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
        self.TOTALSPACE += len(B)

    def bottomupsort(self, A):
        # do ln N passes of pairwise merges

        length = len(A)
        B = [None] * length

        size = 1
        while size < length:
            start = 0
            while start < (length - size):
                self.BASIC +=1
                self.bottomupmerge(A, B, start, start + size - 1, min(start + size + size - 1, length - 1))
                start += size + size
            size = size + size



def run():
    #All variables are initialized at the end of base.py
    srt = mbupsort(size=size, ceiling=ceiling, asInt=isInt, rtype=rtype)


run()

