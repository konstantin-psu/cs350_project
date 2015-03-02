__author__ = 'konstantin'

import sys
import os
from numpy import copy
from numpy import sort
import time
import argparse
sys.setrecursionlimit(50000)
parser = argparse.ArgumentParser(description='Get input size')
parser.add_argument('-t', dest = 'type', type=int)
parser.add_argument('-s', dest = 'inputSize', type=int)
parser.add_argument('-pt', dest = 'partType', type=int)
parser.add_argument('-c', dest = 'ceiling', type=int)
parser.add_argument('-i', dest = 'asInt')
#srt = qsort(type=0, partType = 0, size = size, ceiling = 2000000, asInt = isInt)

args = parser.parse_args()
"""
function ty
two global variables:
1. Test type
2. Distribution type
"""

sys.path.insert(0, '/u/konstan2/cs350_project')

import randomizer
testType = 0
partitionType = 0

#from profiler import do_cprofile
#from randomizer import do_cprofile

import profile
import cProfile


#def do_cprofile(func):
#    def profiled_func(*args, **kwargs):
#        profile = cProfile.Profile()
#        try:
#            profile.enable()
#            result = func(*args, **kwargs)
#            profile.disable()
#            return result
#        finally:
#            profile.print_stats()
#    return profiled_func
#
#
#@do_cprofile
class qsort:
    """
        Global variables used to output information:
  1 # steps - partition, split
  3 # times - partition, split, total
  4 # space - total pace
  5 #!/bin/bash
  6 # Three arguments: 1.

    """
    """ GENERATED """
    PART = 0 # number of splits
    BASIC = 0 # number of partition basic operations
    SPLITRTIME = 0
    TOTALRTIME = 0
    PARTITIONRTIME = 0
    TOTALSPACE = 0
    NAME = ""
    toSort = None
    REPETITIONS = 5
    #Partition types
    gauss = 0
    uniform = 1
    sorted = 2
    reverse = 3
    identical = 4
    s25 = 5
    s85 = 6

    #Test types
    basic = 0
    threeWay = 1
    dualPivot = 2
    basicH = 3
    threeWayH = 4
    dualPivotH = 5
    suf='qsort'
    name = ""
    dpl = 0

    names = {
        0: suf+'Basic',
        1: suf+'ThreeWay',
        2: suf+'DualPivot',
        3: suf+'BasicH',
        4: suf+'ThreeWayH',
        5: suf+'DualPivotH'
    }
    ptypes = {
        0: 'gauss',
        1: 'uniform',
        2: 'sorted',
        3: 'reverse',
        4: 'identical',
        5: 's25',
        6: 's85',
        }

    """ REQUIRED """
    TYPE = None
    size = 1
    duplicates = 0
    seed = 10

    def __init__(self, rtype, partType, size, ceiling, asInt, pivotType = 0):
        self.size = size
        self.TYPE = rtype
        self.partType = partType
        self.generator = randomizer.generator(self.seed, ceiling, median = 0, asInt = asInt)
        self.toSort = self.generator.gen(self.partType, self.size)
        self.name = self.names[rtype]+self.ptypes[self.partType]+str(size)
        #self.dupl(self.toSort)
        self.sort()
        self.SPLITRTIME = self.TOTALRTIME - self.PARTITIONRTIME
        self.dump()
        self.reset()

    def sort(self):
        start = time.perf_counter()
        if self.TYPE == self.basic:
            self.toSort = self.quickSortBasic(self.toSort)
        elif self.TYPE == self.threeWay:
            self.toSort = self.quickSortThreeWay(self.toSort)
        elif self.TYPE == self.dualPivot:
            self.toSort = self.quickSortDualPivot(self.toSort)
        if self.TYPE == self.basicH:
            self.toSort = self.quickSortBasicH(self.toSort)
        elif self.TYPE == self.threeWayH:
            self.toSort = self.quickSortThreeWayH(self.toSort)
        elif self.TYPE == self.dualPivotH:
            self.toSort = self.quickSortDualPivotH(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start

    def reset(self):
        self.BASIC = 0
        self.PART = 0
        self.SPLITRTIME = 0
        self.TOTALRTIME = 0
        self.NAME = ""
        self.PARTITIONRTIME = 0
        self.TOTALSPACE = 0
        self.toSort = []

    def dump(self):
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
        print("elapsed time = {:.12f} seconds".format(self.TOTALRTIME))

    def quickSortThreeWay(self, arr):
        self.PART += 1
        less = []
        pivotList = []
        more = []
        if len(arr) <= 1:
            return arr
        else:
            start = time.perf_counter()
            pivot = arr[0]
            for i in arr:
                self.BASIC += 1
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    more.append(i)
                else:
                    pivotList.append(i)

            end = time.perf_counter()
            self.PARTITIONRTIME += end -start
            self.TOTALSPACE += len(pivotList)
            self.TOTALSPACE += len(less)
            less = self.quickSortThreeWay(less)
            self.PART += 1
            self.TOTALSPACE += len(more)
            more = self.quickSortThreeWay(more)
            self.PART += 1
            return less + pivotList + more
    def quickSortDualPivot(self, arr):
        self.PART += 1
        less = []
        pivotList1 = []
        middle = []
        pivotList2 = []
        more = []
        if len(arr) <= 1:
            self.BASIC += 1
            return arr
        else:
            start = time.perf_counter()
            pivot1 = arr[0]
            pivot2 = arr[len(arr)-1]
            if pivot1 > pivot2:
                 self.BASIC += 1
                 pivot1, pivot2 = pivot2, pivot1
            for i in arr:
                if i == pivot1:
                    self.BASIC += 1
                    pivotList1.append(i)
                elif i == pivot2:
                    self.BASIC += 1
                    pivotList2.append(i)
                elif i < pivot1:
                    self.BASIC += 1
                    less.append(i)
                elif i > pivot2:
                    self.BASIC += 1
                    more.append(i)
                else:
                    self.BASIC += 1
                    middle.append(i)
            end = time.perf_counter()
            self.PARTITIONRTIME += end -start
            self.TOTALSPACE += len(pivotList1)
            self.TOTALSPACE += len(pivotList2)
            self.TOTALSPACE += len(less)
            self.TOTALSPACE += len(middle)
            self.TOTALSPACE += len(more)
            less = self.quickSortDualPivot(less)
            middle = self.quickSortDualPivot(middle)
            more = self.quickSortDualPivot(more)
            return less + pivotList1 + middle + pivotList2 + more

    def quickSortBasic(self, arr):
        self.PART += 1
        less = []
        pivotList = []
        more = []
        if len(arr) <= 1:
            self.BASIC += 1
            return arr
        else:
            start = time.perf_counter()
            pivot = arr[0]
            for i in arr:
                if i < pivot:
                    self.BASIC += 1
                    less.append(i)
                elif i > pivot:
                    self.BASIC += 1
                    more.append(i)
            pivotList.append(pivot)
            end = time.perf_counter()
            self.PARTITIONRTIME += end -start
            self.TOTALSPACE += len(pivotList)
            self.TOTALSPACE += len(less)
            self.TOTALSPACE += len(more)
            less = self.quickSortBasic(less)
            more = self.quickSortBasic(more)
            return less + pivotList + more

    def quickSortBasicH(self, arr):
        self.PART += 1
        less = []
        pivotList = []
        more = []
        h = len(arr)
        if h <= 1:
            return arr
        else:
            start = time.perf_counter()
            l = 1
            h = h-1
            pivot = arr[0]
            while True:
                while l <= h and arr[l] < pivot:
                    self.BASIC += 1
                    less.append(arr[l])
                    l+=1
                while l <=h and arr[h] > pivot:
                    self.BASIC += 1
                    more.append(arr[h])
                    h-=1
                if l > h:
                    break
                less.append(arr[h])
                more.append(arr[l])
                self.BASIC += 1

                l+=1
                h-=1
            pivotList.append(pivot)
            end = time.perf_counter()
            self.PARTITIONRTIME += end -start
            self.TOTALSPACE += len(pivotList)
            self.TOTALSPACE += len(less)
            self.TOTALSPACE += len(more)
            less = self.quickSortBasicH(less)
            more = self.quickSortBasicH(more)
            return less + pivotList + more
    def dupl(self, arr):
        arr1 = []
        for i in arr:
            if i in arr1:
                self.dpl += 1
            arr1.append(i)

    def quickSortThreeWayH(self, arr):
        self.PART += 1
        less = []
        pivotList = []
        more = []
        h = len(arr)
        if h <= 1:
            return arr
        else:
            start = time.perf_counter()
            l = 1
            h = h-1
            pivot = arr[0]
            while True:
                while l <= h and arr[l] == pivot:
                    self.BASIC += 1
                    pivotList.append(arr[l])
                    l+=1
                while l <= h and arr[l] < pivot:
                    self.BASIC += 1
                    less.append(arr[l])
                    l+=1
                while l <=h and arr[h] == pivot:
                    self.BASIC += 1
                    pivotList.append(arr[h])
                    h-=1
                while l <=h and arr[h] > pivot:
                    self.BASIC += 1
                    more.append(arr[h])
                    h-=1
                if l > h:
                    break
                less.append(arr[h])
                more.append(arr[l])
                self.BASIC += 1
                l+=1
                h-=1
            pivotList.append(pivot)
            end = time.perf_counter()
            self.PARTITIONRTIME += end -start
            self.TOTALSPACE += len(pivotList)
            self.TOTALSPACE += len(less)
            self.TOTALSPACE += len(more)
            less = self.quickSortThreeWayH(less)
            more = self.quickSortThreeWayH(more)
            return less + pivotList + more

    def quickSortDualPivotH(self, arr):
        self.PART += 1
        less = []
        pivotList1 = []
        middle = []
        pivotList2 = []
        more = []
        h = len(arr)
        if h <= 1:
            return arr
        else:
            start = time.perf_counter()
            l = 1
            h = h-1
            pivot1 = arr[0]
            pivot2 = arr[len(arr)-1]
            if pivot1 > pivot2:
                pivot1, pivot2 = pivot2, pivot1
            while True:
                while l <= h and arr[l] == pivot1:
                    pivotList1.append(arr[l])
                    l+=1
                while l <= h and arr[l] == pivot2:
                    pivotList2.append(arr[l])
                    l+=1
                while l <= h and arr[h] == pivot1:
                    pivotList1.append(arr[h])
                    h-=1
                while l <= h and arr[h] == pivot2:
                    pivotList2.append(arr[h])
                    h-=1
                while l <= h and arr[l] < pivot1:
                    self.BASIC += 1
                    less.append(arr[l])
                    l+=1
                while l <=h and arr[h] > pivot2:
                    self.BASIC += 1
                    more.append(arr[h])
                    h-=1
                while l <= h and arr[l] > pivot1 and arr[l] < pivot2:
                    self.BASIC += 1
                    middle.append(arr[l])
                    l+=1
                while l <= h and arr[h] > pivot1 and arr[h] < pivot2:
                    self.BASIC += 1
                    middle.append(arr[h])
                    h-=1
                if l > h:
                    break
                if (arr[h] < pivot1):
                  self.BASIC += 1
                  less.append(arr[h])
                if (arr[l] > pivot2):
                  self.BASIC += 1
                  more.append(arr[l])
                l+=1
                h-=1
            pivotList1.append(pivot1)
            pivotList2.append(pivot2)
            end = time.perf_counter()
            self.PARTITIONRTIME += end -start
            self.TOTALSPACE += len(pivotList1)
            self.TOTALSPACE += len(pivotList2)
            self.TOTALSPACE += len(middle)
            self.TOTALSPACE += len(less)
            self.TOTALSPACE += len(more)
            less = self.quickSortThreeWayH(less)
            middle = self.quickSortDualPivotH(middle)
            more = self.quickSortThreeWayH(more)
            return less + pivotList1 + middle + pivotList2 + more

    def compare(self, a,b):
        if len(a) != len(b):
            return False
        l = len(a)
        i =0
        while i < l:
            if a[i] != b[i]:
                # print a[i]
                # print b[i]
                # print i
                return False
            i+=1
        return True

    # def quickSortBasic(self, arr, left, right):
    #     pass

    # def qsortRange(self, a, start, end):
    #      if (start > end):
    #          return a
    #      pivotIndex = self.partition(a, start, end)
    #
    #      self.qsortRange(a, start, pivotIndex - 1)
    #      self.qsortRange(a, pivotIndex + 1, end)
    #      return a

    #Hoare's
    # def partition(self, a, start, end):
    #     i = start+1
    #     pivotIndex = start
    #     j = end
    #     while True:
    #         while a[i] < a[pivotIndex]:
    #             i+=1
    #             if (i == end):
    #                 break
    #         while a[pivotIndex] < a[j]:
    #             j-=1
    #             if (j == start):
    #                 break
    #         if (i>=j):
    #             break
    #         a[i], a[j] = a[j], a[i]
    #     a[pivotIndex], a[j] = a[j], a[pivotIndex]
    #     return j

    # def insertionSort(self, a, start, end):
    #     for i in xrange(start, end + 1):
    #         # Insert a[i] into the sorted sublist
    #         v = a[i]
    #         for j in reversed(xrange(0, i)):
    #             if a[j] <= v:
    #                 a[j + 1] = v
    #                 break
    #             a[j + 1] = a[j]
    #         else:
    #             a[0] = v
    #     return a
    # def quckSortThreeWay(self, arr):
    #     less = []
    #     pivotList = []
    #     more = []
    #     if len(arr) <= 1:
    #         return arr
    #     else:
    #         pivot = arr[0]
    #         for i in arr:
    #             if i < pivot:
    #                 less.append(i)
    #             elif i > pivot:
    #                 more.append(i)
    #             else:
    #                 pivotList.append(i)
    #         less = self.quickSort(less)
    #         more = self.quickSort(more)
    #         return less + pivotList + more
    #     pass
    # def quckSortDualPivot(self, a, start, end):
    #     pivot1 = start
    #     pivot2 = end
    #     pivot1, pivot2 = self.partitionDual(a, start, end, pivot1, pivot2)
    #     self.qsortDualPivot(a, start, pivot1 - 1)
    #     self.qsortDualPivot(a, pivot1+1, pivot2 - 1)
    #     self.qsortDualPivot(a, pivot2 + 1, end)
    #     return a
    # def partitionDual(self, a, start, end, pivotIndex1, pivotIndex2):
    #     low = start
    #     high = end - 1  # After we remove pivot it will be one smaller
    #     pivotValue1 = a[pivotIndex1]
    #     pivotValue2 = a[pivotIndex2]
    #     if pivotValue1 > pivotValue2:
    #         a[pivotIndex1], a[pivotIndex2] = a[pivotIndex2], a[pivotIndex1]
    #         pivotValue1 = a[pivotIndex1]
    #         pivotValue2 = a[pivotIndex2]
    #     elif pivotValue1 == pivotValue2:
    #         while (pivotValue1 == pivotValue2) and (low < high):
    #             low+=1
    #             pivotValue1 = a[low]
    #
    #     lt = low + 1
    #     gt = high
    #     while True:
    #         while low <= high and a[low] < pivotValue1:
    #             a[pivotValue1], a[lt] = a[lt], a[pivotValue1]
    #             low = low + 1
    #         while low <= high and a[high] >= pivotValue2:
    #             a[pivotValue2], a[gt] = a[gt], a[pivotValue2]
    #             high = high - 1
    #         if low > high:
    #             break
    #         a[low], a[high] = a[high], a[low]
    #     return lt, gt

#parser.add_argument('-t', dest = 'type')
#parser.add_argument('-s', dest = 'inputSize')
#parser.add_argument('-pt', dest = 'partType')
#parser.add_argument('-c', dest = 'ceiling')
#parser.add_argument('-i', dest = 'asInt')
def run():
    rtype = 5
    partType = 2
    size = 100
    ceiling = 10000
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
        isInt = args.asInt
    # size = 10000000

    srt = qsort(rtype=rtype, partType = partType, size = size, ceiling = ceiling, asInt = isInt)
    # print("elapsed time = {:.12f} seconds".format(elapsed))
    # print compare(arr1, done)
    # arr1 = sort(arr1)
    # print compare(arr1, done)
    # print arr1
    # print done

#cProfile.run('run()')
#profile.run('run()')
run()
