import random, cProfile, argparse
from numpy import copy


import random, cProfile, time, scipy
from numpy import copy

def merge(A, B, start, middle, end):
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



def mergesort(A, B, start, end):
    if (end <= start):
        return
    middle = int(start + (end - start) / 2)
    mergesort(A, B, start, middle)
    mergesort(A, B, middle + 1, end)
    if(A[middle + 1] >= A[middle]):
        #print("sorted")
        return
    merge(A, B, start, middle, end)



parser = argparse.ArgumentParser(description='Get input size')
parser.add_argument('-s', dest='inputSize')

args = parser.parse_args()
size = int(args.inputSize)

list = random.sample(range(size*10), size)
start = 0
end = len(list)
B = [None] * end

mergesort(list, B, start, end - 1)
print(list)

#cProfile.run('mergesort(list, B, start, end - 1)')
