import random, cProfile, argparse
from numpy import copy

import random, cProfile, time, scipy
from numpy import copy
import randomizer
from base import *



class misort(testbase):
    name="mergeInsertionSort"
    def __init__(self, size, ceiling, asInt, rtype, cutOff):
        self.size = size
        self.gen  = randomizer.generator(maximum=ceiling,asInt=asInt)
        self.CEILING = ceiling
        self.INT = asInt
        self.PARTITIONTYPE = self.ptypes[rtype]
        self.toSort = self.gen.gen(rtype,size)
        self.cutoff = cutOff
        end = len(self.toSort)
        B = [None] * end
        self.name = self.name + self.ptypes[rtype] +str(size)
        start = time.perf_counter()
        self.mergesort(self.toSort,B, 0, end - 1)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.SORTHELPERRTIME - self.ALTSORTRTIME
        self.setinfo()
        self.dump()


    def merge(self, A, B, start, middle, end):
        begin = time.perf_counter()
        B = copy(A)

        i = start
        j = middle + 1

        for k in range(start, end + 1):
            if i > middle:
                self.BASIC += 1
                A[k] = B[j]
                j += 1

            elif j > end:
                self.BASIC += 2
                A[k] = B[i]
                i += 1

            elif B[j] < B[i]:
                self.BASIC += 3
                A[k] = B[j]
                j += 1

            else:
                A[k] = B[i]
                i += 1
        end  = time.perf_counter()
        self.SORTHELPERRTIME += end - begin
        self.TOTALSPACE += len(B)

    def insertionsort(self, list):
        begin = time.perf_counter()
        #print("insertion")
        for i in range(1, len(list)):
            curr = list[i]
            position = i

            while (position > 0) and (list[position - 1] > curr):
                self.ALTSROTBASIC += 1
                list[position] = list[position - 1]
                position = position - 1

            list[position] = curr
        end  = time.perf_counter()
        self.ALTSORTRTIME += end - begin

    def setinfo(self):
        super().setinfo()

        self.info['alt sort run time'] = self.ALTSORTRTIME
        self.info['alt sort basic opeartions'] = self.ALTSROTBASIC
        self.info['alt sort splits'] = self.ALTSORTSPLITS

    def mergesort(self, A, B, start, end):
        self.SPLITS += 1
        if (end <= start):
            return
        if end <= start + self.cutoff - 1:
            self.insertionsort(A[start:end])
        middle = int(start + (end - start) / 2)
        self.mergesort(A, B, start, middle)
        self.mergesort(A, B, middle + 1, end)
        self.merge(A, B, start, middle, end)


def run():
    srt = misort(size=size, ceiling=ceiling, asInt=isInt, rtype=rtype, cutOff = cutoff)


run()


#cProfile.run('mergesort(list, B, start, end - 1)')