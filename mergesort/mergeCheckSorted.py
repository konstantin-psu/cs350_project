import random, cProfile
from numpy import copy

"""
def mergeSort(list):
    #print("Splitting ", list)
    if len(list) > 1:
        mid = int(len(list)/2)
        left = list[:mid]
        right = list[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1

            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
        #print ("Merging ", list)
"""



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




list = random.sample(range(20), 10)
start = 0
end = len(list)
B = [None] * end

mergesort(list, B, start, end - 1)
print(list)

#cProfile.run('mergeSort(list)')
#print list
#print "Goodbye"