__author__ = 'konstantin'
"""
Fast and dirty solution for random numbers generation:
This function requires SciPy package http://scipy.org/install.html
Should be able to save, inputs in following format
Line 1: Size of the input
Line 2: Sorted version of the input
Line 3: Unsorted version

Generator distribution requirements:
sorted
reverse sorted
randomized (Uniform distribution)
randomized (Gaussian/Normal distribution)
25% sorted
85% sorted
list of the identical items (Zero distribution)
test stability using customized sorting denition for list of inputs
more tests if time allows
"""
from scipy import random
from numpy import sort
import os

#rng = pow(2,32)
rng = 50
median = 0
seed = 1
home = os.path.expanduser("~")
separator = ","



class generator:
    def __init__(self, lengths):
        pass
    def generate(self, type, length):
        pass

def save(name, sorted, unsorted, size):
    if os.path.isfile(name):
        pass
    with open(name, "w") as out:
        out.write(size+'\n')
        for i in range(0,size):
            out.write(sorted[i]+separator)
        out.write('\n')
        for i in range(0,size):
            out.write(unsorted[i]+separator)

