import random, cProfile, time, scipy, argparse
from numpy import copy

def bottomupmerge(A, B, start, middle, end):
    B = copy(A)

    i = start
    j = middle + 1

    for k in range(start, end + 1):
        if i > middle:
            A[k] = B[j]
            j += 1

        elif j > end:
            A[k] = B[i]
            i += 1

        elif B[j] < B[i]:
            A[k] = B[j]
            j += 1

        else:
            A[k] = B[i]
            i += 1




def bottomupsort(A):
    # do ln N passes of pairwise merges

    length = len(A)
    B = [None] * length

    size = 1
    while size < length:
        start = 0
        while start < (length - size):
            bottomupmerge(A, B, start, start + size - 1, min(start + size + size - 1, length - 1))
            start += size + size
        size = size + size


parser = argparse.ArgumentParser(description='Get input size')
parser.add_argument('-s', dest='inputSize')

args = parser.parse_args()
size = int(args.inputSize)

list = random.sample(range(size), size)
cProfile.run('bottomupsort(list)')
#bottomupsort(list)
#print (list)