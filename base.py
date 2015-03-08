__author__ = 'konstantin'

import sys
import time
import randomizer
import json
from pprint import pprint
import argparse

parser = argparse.ArgumentParser(description='Test harness arguments parser')
parser.add_argument('-t', dest = 'type', type=int, help= 'Test type, can be empty')
parser.add_argument('-s', dest = 'inputSize', type=int, help='Array size')
parser.add_argument('-pt', dest = 'partType', type=int, help = 'Partition Type')
parser.add_argument('-c', dest = 'ceiling', type=int, help='Ceiling of values to be created for our array, if ceiling is less than input size, and type is set as integer, then by pigeon principle array will have duplicates')
parser.add_argument('-i', dest = 'asInt', type=int, help='Array content type, if 1 then content is integers, 0 for floats')
parser.add_argument('-piv', dest = 'Pivot', type=int, help='This is valuable only for quick sort, if 1 - random, else if 0 - first/last')
parser.add_argument('-cut', dest = 'CutOff', type=int, help='cutof value')
parser.add_argument('-f', dest = 'filename', type=str, help='filename')

args = parser.parse_args()

sys.setrecursionlimit(2500)


#Available distributions
Gauss = 0
Uniform = 1
Sorted = 2
Reverse = 3
Identical = 4
S25 = 5
S85 = 6

#For stability check

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
    RECURSIONDEPTH= 0
    SPLITRTIME = 0
    TOTALRTIME = 0
    SORTHELPERRTIME = 0
    TOTALSPACE = 0
    RECLIM = sys.getrecursionlimit()
    STABILITY=True
    ALTSORTRTIME=0
    ALTSROTBASIC=0
    ALTSORTSPLITS=0
    cutoff=None
    name = ""
    CEILING = 0
    INT = None
    PARTITIONTYPE = None
    toSort = None  #placeholder for array that will be sorted
    REPETITIONS = 5
    size = 0
    #Partition types
    gauss = 0
    uniform = 1
    sorted = 2
    reverse = 3
    identical = 4
    filename = args.filename + "_results.json"
    # filename = "_results.json"
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
            "correctness" : self.correctness(self.toSort),
            "cutoff":self.cutoff,
            "stability":self.STABILITY

        }


    def print(self):
        pprint(self.info)

    def dupl(self, arr):
        self.duplicates = {}
        for i in arr:
            try:
                self.duplicates[i.value] += 1
            except KeyError:
                self.duplicates[i.value] = 0


        self.totDupl = 0
        for i in self.duplicates:
            self.totDupl += self.duplicates[i]


    def dump(self):
        with open(self.filename, 'a') as out:
            out.write(json.dumps(self.info, sort_keys = True, indent=4, separators=(',', ':')))
            out.write("\n")



    def pivot(self, arr, first, l, r):
        if (self.pivotType):
            p =self.generator.randomPivot(min = l, max = r)
            return arr[p], p
        if (first):
            return arr[l], l
        return arr[r], r

    def correctness(self, a):
        #check stability along the way
        if len(a) != self.size:
            return False
        l = len(a)
        i =1
        p = 0
        while i < l:
            if a[i].id < a[p].id and a[i] == a[p]:
                self.STABILITY = False
            if a[i] < a[p]:
                # print(str(i-1)+" Previous "+a[p].astype('str')+" current "+ a[i].astype('str'))
                # err +=1
                # if err > 1:
                return False
            p +=1
            i +=1
        return True

# parser.add_argument('-t', dest = 'type', type=int, help= 'Test type, can be empty')
# parser.add_argument('-s', dest = 'inputSize', type=int, help='Array size')
# parser.add_argument('-pt', dest = 'partType', type=int, help = 'Partition Type')
# parser.add_argument('-c', dest = 'ceiling', type=int, help='Ceiling of values to be created for our array, if ceiling is less than input size, and type is set as integer, then by pigeon principle array will have duplicates')
# parser.add_argument('-i', dest = 'asInt', type=int, help='Array content type, if 1 then content is integers, 0 for floats')
# parser.add_argument('-piv', dest = 'Pivot', type=int, help='This is valuable only for quick sort, if 1 - random, else if 0 - first/last')
# parser.add_argument('-cut', dest = 'CutOff', type=int, help='This is valuable only for quick sort, if 1 - random, else if 0 - first/last')

partType = Uniform
size = 100
ceiling = 10
rtype = Uniform
# pivotType = True
pivotType = False
isInt = True
cutoff=10
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
if args.CutOff is not None:
    cutoff = args.CutOff
