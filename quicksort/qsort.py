__author__ = 'konstantin'

import sys
import os

sys.path.insert(0, '/u/konstan2/cs350_project')

import randomizer
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

def run():
    size = 100000000
    a = randomizer.generator(seed=10, maximum = 200000)
    arr =a.uniform(size)
    #print arr
    arr = quickSort(arr)
    print len(arr)

#cProfile.run('run()')
#profile.run('run()')
run()
