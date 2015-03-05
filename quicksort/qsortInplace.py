__author__ = 'konstantin'

from base import *
import argparse
#sys.setrecursionlimit(50000)
parser = argparse.ArgumentParser(description='Get input size')
parser.add_argument('-t', dest = 'type', type=int)
parser.add_argument('-s', dest = 'inputSize', type=int)
parser.add_argument('-pt', dest = 'partType', type=int)
parser.add_argument('-c', dest = 'ceiling', type=int)
parser.add_argument('-i', dest = 'asInt', type=int)
parser.add_argument('-piv', dest = 'Pivot', type=int)

args = parser.parse_args()

sys.path.insert(0, '/u/konstan2/cs350_project')

testType = 0
partitionType = 0

basic = 0
dualPivot = 1
basicH = 2

class qsortInPlace(testbase):
    #Test types
    basic = 0
    dualPivot = 1
    basicH = 2
    suf='qsortInPlace'
    name = ""
    dpl = 0

    names = {
        0: suf+'Basic',
        1: suf+'DualPivot',
        2: suf+'BasicH',
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
    pivotType = False


    def __init__(self, rtype, partType, size, ceiling, asInt, pivotType = False):
        self.pivotType = pivotType
        self.size = size
        self.TYPE = rtype
        self.partType = partType
        self.generator = randomizer.generator(self.seed, ceiling, median = 0, asInt = asInt)
        self.toSort = self.generator.gen(self.partType, self.size)
        self.name = self.names[rtype]+self.ptypes[self.partType]
        self.TOTALSPACE += size
        #self.dupl(self.toSort)
        self.sort()
        self.SPLITRTIME = self.TOTALRTIME - self.SORTHELPERRTIME
        # pprint(self.toSort)
        self.dump()
        self.reset()

    def sort(self):
        lr = len(self.toSort)
        start = time.perf_counter()
        if self.TYPE == self.basic:
            self.quickSortLomuto(self.toSort, 0, lr-1)
        elif self.TYPE == self.dualPivot:
            self.quickSortDualPivot(self.toSort, 0, lr-1)
        if self.TYPE == self.basicH:
            self.quickSortHoare(self.toSort, 0, lr-1)
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
        pstr = "first/last"
        if (self.pivotType):
            pstr = "random"

        super().dump()
        print("pivot type   :        " + pstr)

    #IMPLEMENTATION #######################################################


    def quickSortLomuto(self, alist, first,last):
        self.SPLITS += 1
        if first<last:
            startp = time.perf_counter()
            splitpoint = self.Lomuto(alist, first, last)
            endp = time.perf_counter()
            self.SORTHELPERRTIME += endp - startp
            self.quickSortLomuto(alist,first,splitpoint-1)
            self.quickSortLomuto(alist,splitpoint+1,last)

    def quickSortHoare(self, alist, first,last):
        self.SPLITS += 1
        if first<last:
            startp = time.perf_counter()
            splitpoint = self.Hoare(alist,first,last)
            endp = time.perf_counter()
            self.SORTHELPERRTIME += endp - startp
            self.quickSortHoare(alist,first,splitpoint-1)
            self.quickSortHoare(alist,splitpoint+1,last)

    def quickSortDualPivot(self, alist, first,last):
        self.SPLITS += 1
        if first<=last:
            startp = time.perf_counter()
            splitpoint1, splitpoint2 = self.dual(alist,first,last)
            a1 = alist[first: splitpoint1]
            a2 = alist[splitpoint1+1:splitpoint2]
            a3 = alist[splitpoint2+1:last+1]
            endp = time.perf_counter()
            self.SORTHELPERRTIME += endp - startp
            self.quickSortDualPivot(alist,first,splitpoint1-1)
            self.quickSortDualPivot(alist, splitpoint1+1, splitpoint2-1)
            self.quickSortDualPivot(alist,splitpoint2+1,last)

    def dual(self, arr, first, last):
        a1 = arr[first: last+1]
        # p1, loc1 = self.pivot(arr,True, l = first, r = last)
        # p2, loc2 = self.pivot(arr,False, l = first, r = last)
        p1 = arr[first]
        p2 = arr[last]
        # if self.pivotType:
        #     arr[first], arr[loc1] = arr[loc1] , arr[first]
        #     arr[last], arr[loc2] = arr[loc2] , arr[last]

        if p1 > p2:
            arr[first], arr[last] = arr[last], arr[first]
            p1 = arr[first]
            p2 = arr[last]
        elif p1 == p2:
            while p1 == p2 and first < last:
                first += 1
                p1=arr[first]

        # if p1 > p2 and first < last:
        #     arr[first], arr[last] = arr[last], arr[first]



        i = first + 1
        s = first + 1
        p = last - 1


        while i <= p:
            if arr[i] <= p1:
                arr[s], arr[i] = arr[i], arr[s]
                s +=1
                i+=1
            elif arr[i] >= p2:
                arr[p], arr[i] = arr[i], arr[p]
                p -= 1
            else:
                i+=1

        if (last - first > 1):
            arr[first], arr[s-1] = arr[s-1], arr[first]
            arr[last], arr[p+1] = arr[p+1], arr[last]
        return s-1, p+1

    def Hoare(self, arr, first, last):
        pivotvalue, loc = self.pivot(arr,True, l = first, r = last)
        if self.pivotType:
            arr[first], arr[loc] = arr[loc] , arr[first]

        leftmark = first+1
        rightmark = last

        done = False
        while not done:
            while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
                self.BASIC += 1
                leftmark = leftmark + 1

            while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
                self.BASIC += 1
                rightmark = rightmark -1

            if rightmark < leftmark:
                self.BASIC += 1
                done = True
            else:
                temp = arr[leftmark]
                arr[leftmark] = arr[rightmark]
                arr[rightmark] = temp

        temp = arr[first]
        arr[first] = arr[rightmark]
        arr[rightmark] = temp
        return rightmark

    def Lomuto(self, arr, first, last):
        pivotvalue, loc = self.pivot(arr,True, l = first, r = last)
        if self.pivotType:
            arr[first], arr[loc] = arr[loc] , arr[first]

        i = first + 1
        s = first

        while i <= last:
            if arr[i] < pivotvalue:
                s +=1
                arr[s], arr[i] = arr[i], arr[s]
            i+=1

        arr[first], arr[s] = arr[s], arr[first]
        return s


def run():
    # rtype = basic
    rtype = dualPivot
    partType = Uniform
    size = 150
    ceiling = 500
    # pivotType = True
    pivotType = False
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
        isInt = bool(args.asInt)
    if args.Pivot is not None:
        pivotType = bool(args.Pivot)

    srt = qsortInPlace(rtype=rtype, partType = partType, size = size, ceiling = ceiling, asInt = isInt, pivotType= pivotType)

run()

# /usr/bin/python3.4 /home/konstantin/cs350_project/quicksort/qsortInplace.py
# name:                 qsortInPlaceBasicuniform
# size:                 10000000
# basic operations:     0
# partition operations: 19980001
# total split time:     10.54379344057088019326329231262207031250000000000000
# total time:           964.10956462100148200988769531250000000000000000000000
# total partition:      953.56577118043060181662440299987792968750000000000000
# total space used:     10000000
# number of duplicates: 0
# correctness:          True
# pivot type   :        random
#
# Process finished with exit code 0
