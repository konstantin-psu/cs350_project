import random, cProfile
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
        pprint(self.toSort)
        self.heapsort(self.toSort)
        # self.toSort = self.mergesort1(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.SORTHELPERRTIME
        pprint(self.toSort)
        self.setinfo()
        self.dump()

    def heapsort(self, list):
        self.SPLITS += 1
        length = len(list) - 1
        for i in range(int((length / 2)), -1, -1):
            self.siftDown(list, i, length)

        # a[0] is the root and largest value.
        # The swap moves it in front of the sorted elements
        # the heap size is reduced by 1
        # the swap ruined the heap property, so restore it
        for i in range(length, 0, -1):
            if list[0] > list[i]:
                self.swap( list, 0, i )
                self.siftDown( list, 0, i - 1 )


    def siftDown(self,  list, first, last ):
        s = time.perf_counter()
        largest = 2 * first + 1
        while largest <= last:
            if (largest < last) and (list[largest] < list[largest + 1]):
                self.BASIC += 1
                largest += 1


            if list[largest] > list[first]:
                self.BASIC += 1
                self.swap(list, largest, first)
                first = largest
                largest = 2 * first + 1
            else:
                self.BASIC += 1
                e = time.perf_counter()
                self.SORTHELPERRTIME += e - s
                return


    def swap(self, A, x, y ):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp


def run():
    srt = sort(size=size, ceiling=ceiling, asInt=isInt, rtype=partType)

run()
