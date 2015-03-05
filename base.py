__author__ = 'konstantin'

import sys
import time
import randomizer
import json
from pprint import pprint

sys.setrecursionlimit(2500)


#Available distributions
Gauss = 0
Uniform = 1
Sorted = 2
Reverse = 3
Identical = 4
S25 = 5
S85 = 6
class testbase(object):
    """
      Global variables used to output information:
      1 # steps - partition, split
      3 # times - partition, split, total
      4 # space - total pace
      5 #!/bin/bash
      6 # Three arguments: 1.

    """
    """ GENERATED """
    SPLITS = 0 # number of splits
    BASIC = 0 # number of partition basic operations
    SPLITRTIME = 0
    TOTALRTIME = 0
    SORTHELPERRTIME = 0
    TOTALSPACE = 0
    RECLIM = sys.getrecursionlimit()
    NAME = ""
    CEILING = 0
    INT = None
    PARTITIONTYPE = None
    toSort = None  #placeholder for array that will be sorted
    REPETITIONS = 5
    #Partition types
    gauss = 0
    uniform = 1
    sorted = 2
    reverse = 3
    identical = 4
    filename = ""
    s25 = 5
    s85 = 6

    suf=''
    name = ''
    dpl = 0

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
    totDupl = 0
    seed = 10
    pivotType = False


    def __init__(self):
        pass

    def reset(self):
        self.BASIC = 0
        self.PART = 0
        self.SPLITRTIME = 0
        self.TOTALRTIME = 0
        self.NAME = ""
        self.PARTITIONRTIME = 0
        self.TOTALSPACE = 0
        self.toSort = []

    def setinfo(self):
        self.dupl(self.toSort)
        self.info = {
            "name":self.name,
            "size":self.size,
            "basic operations" : self.BASIC,
            "partition operations" : self.SPLITS,
            "total split time":self.SPLITRTIME,
            "total time":self.TOTALRTIME,
            "total partition":self.SORTHELPERRTIME,
            "total space used":self.TOTALSPACE,
            "number of duplicates" : self.totDupl,
            "ceiling":self.CEILING,
            "partition type":self.PARTITIONTYPE,
            "is integer":self.INT,
            "correctness" : self.correctness(self.toSort)

        }


    def print(self):
        pprint(self.info)

    def dupl(self, arr):
        self.duplicates = {}
        for i in arr:
            try:
                self.duplicates[i] += 1
            except KeyError:
                self.duplicates[i] = 0


        self.totDupl = 0
        for i in self.duplicates:
            self.totDupl += self.duplicates[i]





    def pivot(self, arr, first, l, r):
        if (self.pivotType):
            p =self.generator.randomPivot(min = l, max = r)
            return arr[p], p
        if (first):
            return arr[l], l
        return arr[r], r

    def correctness(self, a):
        if len(a) != self.size:
            return False
        l = len(a)
        i =1
        p = 0
        while i < l:
            if a[i] < a[p]:
                print(str(i-1)+" Previous "+a[p].astype('str')+" current "+ a[i].astype('str'))
                # err +=1
                # if err > 1:
                return False
            p +=1
            i +=1
        return True
