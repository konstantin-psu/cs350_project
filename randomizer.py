__author__ = 'konstantin'
"""
sorted
reverse sorted
randomized (Uniform distribution)
randomized (Gaussian/Normal distribution)
25% sorted
85% sorted
list of the identical items (Zero distribution)
"""

from scipy import random
from numpy import sort
from numpy import append
from numpy import concatenate
from numpy import around
#import cProfile


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
#@do_cprofile
SEED = 10
class item:
    #place holders:
    def __init__(self, value, id):
        self.value = value
        self.id = id
    def __eq__(self, other):
        return self.value == other.value
    def __ne__(self, other):
        return self.value != other.value
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value
    def __le__(self, other):
        return self.value <= other.value
    def __ge__(self, other):
        return self.value >= other.value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)+":"+str(self.id)

class generator:
    Gauss = 0
    Uniform = 1
    Sorted = 2
    Reverse = 3
    Identical = 4
    S25 = 5
    S85 = 6
    def __init__(self, seed=10, maximum = 50000, median = 0, asInt = False):
       self.maximum = maximum
       self.median = median
       self.seed = seed
       self.asInt = asInt
       SEED = seed
       random.seed(seed)

    def gen(self, t, size):
        if t == self.Gauss:
            return self.gauss(size=size)
        elif t == self.Uniform:
            return self.uniform(size=size)
        elif t == self.Sorted:
            return self.sorted(size=size)
        elif t == self.Reverse:
            return self.reverseSorted(size=size)
        elif t == self.Identical:
            return self.identical(size=size)
        elif t == self.S25:
            return self.s25(size=size)
        elif t == self.S85:
            return self.s85(size=size)

    def gauss(self, size):
        s = random.normal(self.median, self.maximum, size)
        if (self.asInt):
            s = s.astype(int)
        return self.convert(s)
    def uniform(self, size):
        s = random.uniform(high = self.maximum, size=size)
        if (self.asInt):
            s = s.astype(int)
        return self.convert(s)
    def sorted(self, size):
        s = random.uniform(high = self.maximum, size=size)
        s = sort(s)
        if (self.asInt):
            s = s.astype(int)
        return self.convert(s)
    def reverseSorted(self, size):
        s = random.uniform(high = self.maximum, size=size)
        s = s[::-1]
        if (self.asInt):
            s = s.astype(int)
        return self.convert(s)
    def identical(self, size):
        s = random.uniform(low=self.maximum, high = self.maximum, size=size)
        if (self.asInt):
            s = s.astype(int)
        return self.convert(s)
    def s25(self, size):
        if (size < 4):
            first = 1
        else:
            first = int(around(size * 0.25))
        last = size - first
        s = concatenate([sort(random.uniform(high = self.maximum, size=first)) , random.uniform(high = self.maximum, size=last)])
        if (self.asInt):
            s = s.astype(int)
        return self.convert(s)
    def s85(self, size):
        if (size < 4):
            last = 1
        else:
            last = int(around(size * 0.25))
        first = size - last
        s = concatenate([sort(random.uniform(high = self.maximum, size=first)) , random.uniform(high = self.maximum, size=last)])
        if (self.asInt):
            s = s.astype(int)
        return self.convert(s)
    def randomPivot(self, min = 0,  max=0):
        p = random.randint(low= min, high = max)
        return p

    def convert(self, a):
        # will be array of items
        arr = []
        id = 0
        for i in a:
            x = item(i,id)
            arr.append(x)
            id += 1
        return arr
