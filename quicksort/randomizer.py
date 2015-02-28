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
class generator:
    def __init__(self, seed=10, maximum = 50000, median = 0):
       self.maximum = maximum
       self.median = median
       self.seed = seed
       SEED = seed
       random.seed(seed)

    def sorted(self, size):
        pass
    def gauss(self, size):
        s = random.normal(self.median, self.maximum, size)
        return s
    def uniform(self, size):
        s = random.uniform(high = self.maximum, size=size)
        return s
    def sorted(self, size):
        s = self.uniform(size=size)
        s = sort(s)
        return s
    def reverseSorted(self, size):
        s = self.sorted(size)
        s = s[::-1]
        return s
    def identical(self, size):
        s = random.uniform(low=self.maximum, high = self.maximum, size=size)
        return s
    def s25(self, size):
        if (size < 4):
            first = 1
        else:
            first = int(around(size * 0.25))
        last = size - first
        s = concatenate([sort(random.uniform(high = self.maximum, size=first)) , random.uniform(high = self.maximum, size=last)])
        return s
    def s85(self, size):
        if (size < 4):
            last = 1
        else:
            last = int(around(size * 0.25))
        first = size - last
        s = concatenate([sort(random.uniform(high = self.maximum, size=first)) , random.uniform(high = self.maximum, size=last)])
        return s

class rnd:
    def normal(self, max):
        s = random.binomial(self.median, max)
        return int(around(s))
    def uniform(self, size):
        s = random.uniform(high = self.maximum)
        return s
    def sorted(self, size):
        s = self.uniform(size=size)
        s = sort(s)
        return s
    def reverseSorted(self, size):
        s = self.sorted(size)
        s = s[::-1]
        return s
    def identical(self, size):
        s = random.uniform(low=self.maximum, high = self.maximum, size=size)
        return s
    def s25(self, size):
        if (size < 4):
            first = 1
        else:
            first = int(around(size * 0.25))
        last = size - first
        s = concatenate([sort(random.uniform(high = self.maximum, size=first)) , random.uniform(high = self.maximum, size=last)])
        return s
    def s85(self, size):
        if (size < 4):
            last = 1
        else:
            last = int(around(size * 0.25))
        first = size - last
        s = concatenate([sort(random.uniform(high = self.maximum, size=first)) , random.uniform(high = self.maximum, size=last)])
        return s
