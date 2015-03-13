__author__ = 'konstantin'
from numpy import log2

size = 1
while size < 20000000:
    if size < 1000000:
        size *= 10
    else:
        size += 1000000
    m = size*log2(size)
    print(str(size)+" & "+ str(m))
