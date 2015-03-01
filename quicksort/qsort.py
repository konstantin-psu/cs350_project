__author__ = 'konstantin'

import sys
import os
from numpy import copy
from numpy import sort

sys.path.insert(0, '/u/konstan2/cs350_project')

import randomizer
PRANDOM = 0
PFIRST = 1
PNORMAL = 3

CURRENT = PFIRST
#from profiler import do_cprofile
from numpy import sort
#from randomizer import do_cprofile

import profile


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
    def __init__(self, pivotType = PFIRST):
       CURRENT = pivotType

    def quickSortThreeWay(self, arr):
        less = []
        pivotList = []
        more = []
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            for i in arr:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    more.append(i)
                else:
                    pivotList.append(i)
            less = self.quickSortThreeWay(less)
            more = self.quickSortThreeWay(more)
            return less + pivotList + more
    def quickSortLomuto(self, arr):
        less = []
        pivotList = []
        more = []
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            for i in arr:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    more.append(i)
                else:
                    pivotList.append(i)
            less = self.quickSortThreeWay(less)
            more = self.quickSortThreeWay(more)
            return less + pivotList + more
    def quickSortDualPivot(self, arr):
        less = []
        pivotList1 = []
        middle = []
        pivotList2 = []
        more = []
        if len(arr) <= 1:
            return arr
        else:
            pivot1 = arr[0]
            pivot2 = arr[len(arr)-1]
            if pivot1 > pivot2:
                 pivot1, pivot2 = pivot2, pivot1
            for i in arr:
                if i == pivot1:
                    pivotList1.append(i)
                elif i == pivot2:
                    pivotList2.append(i)
                elif i < pivot1:
                    less.append(i)
                elif i > pivot2:
                    more.append(i)
                else:
                    middle.append(i)
            less = self.quickSortDualPivot(less)
            middle = self.quickSortDualPivot(middle)
            more = self.quickSortDualPivot(more)
            return less + pivotList1 + middle + pivotList2 + more
    def quickSortBasic(self, arr):
        less = []
        pivotList = []
        more = []
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            for i in arr:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    more.append(i)
            pivotList.append(pivot)
            less = self.quickSortBasic(less)
            more = self.quickSortBasic(more)
            return less + pivotList + more

    def quickSortBasicH(self, arr):
        less = []
        pivotList = []
        more = []
        h = len(arr)
        if h <= 1:
            return arr
        else:
            l = 1
            h = h-1
            pivot = arr[0]
            while True:
                while l <= h and arr[l] < pivot:
                    less.append(arr[l])
                    l+=1
                while l <=h and arr[h] > pivot:
                    more.append(arr[h])
                    h-=1
                if l > h:
                    break
                less.append(arr[h])
                more.append(arr[l])
                l+=1
                h-=1
            pivotList.append(pivot)
            less = self.quickSortBasicH(less)
            more = self.quickSortBasicH(more)
            return less + pivotList + more

    def quickSortThreeWayH(self, arr):
        less = []
        pivotList = []
        more = []
        h = len(arr)
        if h <= 1:
            return arr
        else:
            l = 1
            h = h-1
            pivot = arr[0]
            while True:
                while l <= h and arr[l] == pivot:
                    pivot.append(arr[l])
                    l+=1
                while l <= h and arr[l] < pivot:
                    less.append(arr[l])
                    l+=1
                while l <=h and arr[h] > pivot:
                    more.append(arr[h])
                    h-=1
                if l > h:
                    break
                less.append(arr[h])
                more.append(arr[l])
                l+=1
                h-=1
            pivotList.append(pivot)
            less = self.quickSortThreeWayH(less)
            more = self.quickSortThreeWayH(more)
            return less + pivotList + more

    def quickSortDualPivotH(self, arr):
        less = []
        pivotList1 = []
        middle = []
        pivotList2 = []
        more = []
        h = len(arr)
        if h <= 1:
            return arr
        else:
            l = 1
            h = h-1
            pivot1 = arr[0]
            pivot2 = arr[len(arr)-1]
            if pivot1 > pivot2:
                pivot1, pivot2 = pivot2, pivot1
            while True:
                # while l <= h and arr[l] == pivot:
                #     pivot.append(arr[l])
                #     l+=1
                while l <= h and arr[l] < pivot1:
                    less.append(arr[l])
                    l+=1
                while l <=h and arr[h] > pivot2:
                    more.append(arr[h])
                    h-=1
                while l <= h and arr[l] > pivot1 and arr[l] < pivot2:
                    middle.append(arr[l])
                    l+=1
                while l <= h and arr[h] > pivot1 and arr[h] < pivot2:
                    middle.append(arr[h])
                    h-=1
                if l > h:
                    break
                if (arr[h] < pivot1):
                  less.append(arr[h])
                if (arr[l] > pivot2):
                  more.append(arr[l])
                l+=1
                h-=1
            pivotList1.append(pivot1)
            pivotList2.append(pivot2)
            less = self.quickSortThreeWayH(less)
            middle = self.quickSortDualPivotH(middle)
            more = self.quickSortThreeWayH(more)
            return less + pivotList1 + middle + pivotList2 + more
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

def compare(a,b):
    l = len(a)
    i =0
    while i < l:
        if a[i] != b[i]:
            print a[i]
            print b[i]
            print i
            return False
        i+=1
    return True

def run():
    size = 50
    a = randomizer.generator(seed=10, maximum = 35)
    srt = qsort()
    arr =a.uniform(size)
    arr1 = copy(arr)
    # print arr1
    done = srt.quickSortDualPivotH(arr)
    # done = srt.quickSortBasic(arr)
    print len(done)
    print compare(arr1, done)
    arr1 = sort(arr1)
    print compare(arr1, done)
    # print arr1
    # print done

#cProfile.run('run()')
#profile.run('run()')
run()
