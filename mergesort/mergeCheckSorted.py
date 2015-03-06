import random, cProfile, argparse
from numpy import copy
from base import *


import random, cProfile, time, scipy
from numpy import copy

class msort(testbase):


    # list = random.sample(range(size*10), size)
    # start = 0
    # end = len(list)
    # B = [None] * end
    # mergesort(list, B, start, end - 1)


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
        self.mergesort(self.toSort,B, 0, end - 1)
        # self.toSort = self.mergesort(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.SORTHELPERRTIME
        # pprint(self.toSort)
        self.setinfo()
        self.dump()

    def merge(self, A, B, start, middle, end):
        B = copy(A)

        i = start
        j = middle + 1

        for k in range(start, end + 1):
            if i > middle:
                A[k] = B[j]
                j += 1

            elif j > end:
                A[k] = B[i]
                i += 1

            elif B[j] < B[i]:
                A[k] = B[j]
                j += 1

            else:
                A[k] = B[i]
                i += 1



    def mergesort(self, A, B, start, end):
        if (end <= start):
            return
        middle = int(start + (end - start) / 2)
        self.mergesort(A, B, start, middle)
        self.mergesort(A, B, middle + 1, end)
        if(A[middle + 1] >= A[middle]):
            #print("sorted")
            return
        self.merge(A, B, start, middle, end)




def run():
    srt = msort(size=size, ceiling=ceiling, asInt=isInt, rtype=partType)


run()
#cProfile.run('mergesort(list, B, start, end - 1)')
