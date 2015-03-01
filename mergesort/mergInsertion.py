import random, cProfile
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




def insertionsort(list):
    print("insertion")
    for i in range(1, len(list)):
        curr = list[i]
        position = i

        while (position > 0) and (list[position - 1] > curr):
            list[position] = list[position - 1]
            position = position - 1

        list[position] = curr



def mergesort(A, B, start, end):
    cutoff = 10
    if (end <= start):
        return
    if end <= start + cutoff - 1:
        insertionsort(A[start:end])
    middle = int(start + (end - start) / 2)
    mergesort(A, B, start, middle)
    mergesort(A, B, middle + 1, end)
    merge(A, B, start, middle, end)



list = random.sample(range(100), 12)
start = 0
end = len(list)
B = [None] * end

mergesort(list, B, start, end - 1)
print(list)

#cProfile.run('mergeSort(list)')