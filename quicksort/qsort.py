__author__ = 'konstantin'

import randomizer
from numpy import sort
def quickSort(arr):
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
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

a = randomizer.generator(seed=10, maximum = 20)
# arr =a.uniform(10)
# s = sort(arr)
# print arr
# # if arr.any() == s.any():
# #     print True
# arr = quickSort(arr)
# print s
# print arr == s
print a.uniform(10)
print a.gauss(10)
print a.identical(10)
print a.reverseSorted(10)
print a.s25(10)
print a.s85(10)
print a.sorted(10)
