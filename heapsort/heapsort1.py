
"""
procedure heapsort(a, count) is
    input: an unordered array a of length count

    (Build the heap in array a so that largest value is at the root)
    heapify(a, count)

    (The following loop maintains the invariants that a[0:end] is a heap and every element
     beyond end is greater than everything before it (so a[end:count] is in sorted order))
    end = count - 1
    while end > 0 do
        (a[0] is the root and largest value. The swap moves it in front of the sorted elements.)
        swap(a[end], a[0])
        (the heap size is reduced by one)
        end = end - 1
        (the swap ruined the heap property, so restore it)
        siftDown(a, 0, end)


(Put elements of 'a' in heap order, in-place)
procedure heapify(a, count) is
    (start is assigned the index in 'a' of the last parent node)
    (the last element in a 0-based array is at index count-1; find the parent of that element)
    start = floor ((count - 2) / 2)

    while start >= 0 do
        (sift down the node at index 'start' to the proper place such that all nodes below
         the start index are in heap order)
        siftDown(a, start, count - 1)
        (go to the next parent node)
        start = start - 1
    (after sifting down the root all nodes/elements are in heap order)

(Repair the heap whose root element is at index 'start', assuming the heaps rooted at its children are valid)
procedure siftDown(a, start, end) is
    root = start

    while root * 2 + 1 <= end do    (While the root has at least one child)
        child = root * 2 + 1       (Left child)
        swap = root                (Keeps track of child to swap with)

        if a[swap] < a[child]
            swap = child
        (If there is a right child and that child is greater)
        if child+1 <= end and a[swap] < a[child+1]
            swap = child + 1
        if swap = root
            (The root holds the largest element. Since we assume the heaps rooted at the
             children are valid, this means that we are done.)
            return
        else
            swap(a[root], a[swap])
            root = swap            (repeat to continue sifting down the child now)

"""

import math, random, cProfile

def heapsort(a, count):

    #an unordered array of a of length count
    #(Build the heap in array a so that largest value is at the root)
    heapify(a, count)

    #(The following loop maintains the invariants that a[0:end] is a heap and every element
    # beyond end is greater than everything before it (so a[end:count] is in sorted order))
    end = count - 1
    while (end > 0):
        #(a[0] is the root and largest value. The swap moves it in front of the sorted elements.)
        swap(a[end], a[0])
        #(the heap size is reduced by one)
        end = end - 1
        #(the swap ruined the heap property, so restore it)
        siftDown(a, 0, end)
    return a

#(Put elements of 'a' in heap order, in-place)
def heapify(a, count):
    #(start is assigned the index in 'a' of the last parent node)
    #(the last element in a 0-based array is at index count-1; find the parent of that element)
    start = int(math.floor((count - 2) / 2))

    while start >= 0:
        #(sift down the node at index 'start' to the proper place such that all nodes below
        # the start index are in heap order)
        siftDown(a, start, count - 1)
        #(go to the next parent node)
        start = start - 1
    #(after sifting down the root all nodes/elements are in heap order)

#(Repair the heap whose root element is at index 'start', assuming the heaps rooted at its children are valid)
def siftDown(a, start, end):
    root = 0  # start

    while (root * 2 + 1 <= end):    #(While the root has at least one child)
        child = root * 2 + 1       #(Left child)
        swapv = root                #(Keeps track of child to swap with)

        if a[swapv] < a[child]:
            swapv = child
        #(If there is a right child and that child is greater)
        if child+1 <= end and a[swapv] < a[child+1]:
            swapv = child + 1
        if swapv == root:
            #(The root holds the largest element. Since we assume the heaps rooted at the
             #children are valid, this means that we are done.)
            return
        else:
            swap(a[root], a[swapv])
            root = swapv            #(repeat to continue sifting down the child now)

def swap(a, b):
    tmp = a
    a = b
    b = a

list = random.sample(xrange(10), 10)
print list
#cProfile.run('print heapsort(list, 10)')
print heapsort(list, 10)

