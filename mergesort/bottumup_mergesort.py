import random, cProfile, time, scipy
from numpy import copy

def bottomupmerge(A, B, lo, mid, hi):
    B = copy(A)

    i = lo
    j = mid + 1

    for k in range(lo, hi)

    i0 = left
    i1 = right

    # While there are elements in the left or right runs
    for j in range(left, end, 1):
        if (i0 < right and (i1 >= end or A[i0] <= A[i1])):
            B[j] = A[i0]
            i0 += 1
        else:
            B[j] = A[i1]
            i0 += 1



def copy_array(B, A, n):
    for i in range(0, n):
        A[i] = B[i]



def bottomupsort(A):
    N = len(A)
    B = [None] * N
    for n in range(1, N, n):
        for i in range(0, (N-n), n):
            lo = i
            m = i + n - 1
            hi = min(i + n + n - 1, N - 1)
            bottomupmerge(A, B, lo, m, hi)


    width = 1
    while width < n:
        i = 0
        while i < n:
            bottomupmerge(A, i, min(i + width, n), min(i + (2 * width), n), B)
            i += 2 * width
        width *= 2
    #A = copy(B)
    return B
    #copy_array(B, A, n)


list = random.sample(range(100), 100)
#cProfile.run('bottomupsort(list, B, 100)')
B = [None] * 100
bottomupsort(list, B, 100)
print (list)
#print "Goodbye"