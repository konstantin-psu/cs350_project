__author__ = 'konstantin'

from base import *
# sys.path.insert(0, '/u/konstan2/cs350_project') change to project path

testType = 0
partitionType = 0

threeWay = 0
dualPivot = 1

class qsort(testbase):
    """
      Global variables used to output information:
      1 # steps - partition, split
      3 # times - partition, split, total
      4 # space - total pace
      5 #!/bin/bash
      6 # Three arguments: 1.

    """
    """ GENERATED """

    #Test types
    threeWay = 0
    dualPivot = 1
    suf='qsort'
    name = ""

    names = {
        0: suf+'ThreeWay',
        1: suf+'DualPivot',
    }
    """ REQUIRED """
    TYPE = None
    size = 1
    duplicates = 0
    seed = 10
    pivotType = False


    def __init__(self, rtype, partType, size, ceiling, asInt, pivotType = False):
        super().__init__()
        self.pivotType = pivotType
        self.size = size
        self.filename = str(rtype) + self.filename
        self.TYPE = rtype
        self.INT = asInt
        self.partType = partType
        self.generator = randomizer.generator(self.seed, ceiling, median = 0, asInt = asInt)
        self.toSort = self.generator.gen(self.partType, self.size)
        self.PARTITIONTYPE = self.ptypes[self.partType]
        self.name = self.names[rtype]
        self.filename = self.name+"_test_results.json"
        self.CEILING = ceiling
        #self.dupl(self.toSort)
        self.sort()
        self.SPLITRTIME = self.TOTALRTIME - self.SORTHELPERRTIME
        self.setinfo()
        # self.print()
        # print(self.toSort)
        self.dump()
        self.reset()

    def sort(self):
        start = time.perf_counter()
        if self.TYPE == self.threeWay:
            self.toSort = self.quickSortThreeWay(self.toSort)
        elif self.TYPE == self.dualPivot:
            self.toSort = self.quickSortDualPivot(self.toSort)
        else:
           return
        end = time.perf_counter()
        self.TOTALRTIME = end - start

    def setinfo(self):
        super().setinfo()
        pstr = "first/last"
        if (self.pivotType):
            pstr = "random"
        self.info['pivot type']=pstr


    #IMPLEMENTATION #######################################################
    def quickSortThreeWay(self, arr):
        self.SPLITS += 1
        less = []
        pivotList = []
        more = []
        lr = len(arr)
        if lr <= 1:
            return arr
        else:
            start = time.perf_counter()
            pivot, loc = self.pivot(arr, True, l = 0 , r = lr-1)
            for i in arr:
                if i < pivot:
                    self.BASIC += 1
                    less.append(i)
                elif i > pivot:
                    self.BASIC += 2
                    more.append(i)
                else:
                    self.BASIC += 2
                    pivotList.append(i)

            end = time.perf_counter()
            self.SORTHELPERRTIME += end - start
            self.TOTALSPACE += len(pivotList)
            self.TOTALSPACE += len(less)
            less = self.quickSortThreeWay(less)
            self.TOTALSPACE += len(more)
            more = self.quickSortThreeWay(more)
            return less + pivotList + more


    def quickSortDualPivot(self, arr):
        self.SPLITS += 1
        less = []
        pivotList1 = []
        middle = []
        pivotList2 = []
        more = []
        lr = len(arr)
        if lr <= 1:
            self.BASIC += 1
            return arr
        else:
            start = time.perf_counter()
            pivot1, loc1 = self.pivot(arr, True, l = 0, r = lr -1)
            pivot2, loc2 = self.pivot(arr, False, l = 0, r = lr-1)
            if pivot1 > pivot2:
                 pivot1, pivot2 = pivot2, pivot1
            for i in arr:
                if i == pivot1:
                    self.BASIC += 1
                    pivotList1.append(i)
                elif i == pivot2:
                    self.BASIC += 2
                    pivotList2.append(i)
                elif i < pivot1:
                    self.BASIC += 3
                    less.append(i)
                elif i > pivot2:
                    self.BASIC += 4
                    more.append(i)
                else:
                    self.BASIC += 4
                    middle.append(i)
            end = time.perf_counter()
            self.SORTHELPERRTIME += end - start
            self.TOTALSPACE += len(pivotList1)
            self.TOTALSPACE += len(pivotList2)
            self.TOTALSPACE += len(less)
            self.TOTALSPACE += len(middle)
            self.TOTALSPACE += len(more)
            less = self.quickSortDualPivot(less)
            middle = self.quickSortDualPivot(middle)
            more = self.quickSortDualPivot(more)
            return less + pivotList1 + middle + pivotList2 + more

def run():
    srt = qsort(rtype=rtype, partType = partType, size = size, ceiling = ceiling, asInt = isInt, pivotType= pivotType)

run()
