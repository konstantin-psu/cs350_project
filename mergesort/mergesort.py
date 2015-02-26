import random

def mergeSort(list):
    #print("Splitting ", list)
    if len(list) > 1:
        mid = len(list)/2
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



list = random.sample(xrange(100000000), 100000000)
mergeSort(list)
#print list
print "Goodbye"