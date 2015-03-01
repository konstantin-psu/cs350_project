import random, cProfile

def heapsort( list ):
    length = len( list ) - 1
    for i in range ( (length / 2), -1, -1 ):
        siftDown( list, i, length )

    # a[0] is the root and largest value.
    # The swap moves it in front of the sorted elements
    # the heap size is reduced by 1
    # the swap ruined the heap property, so restore it
    for i in range ( length, 0, -1 ):
        if list[0] > list[i]:
            swap( list, 0, i )
            siftDown( list, 0, i - 1 )


def siftDown( list, first, last ):
    largest = 2 * first + 1
    while largest <= last:
        if ( largest < last ) and ( list[largest] < list[largest + 1] ):
            largest += 1


        if list[largest] > list[first]:
            swap( list, largest, first )
            first = largest;
            largest = 2 * first + 1
        else:
            return


def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


list = random.sample(xrange(10000000), 10000000)
cProfile.run('heapsort(list)')
#heapsort(list)
#print list