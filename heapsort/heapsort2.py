
"""
procedure heapsort(a, count) is
    input: an unordered array a of length count

    (Build the heap in array a so that largest value is at the root)
    heapify(a, count)

    (The following loop maintains the invariants that a[0:end] is a heap and every element
     beyond end is greater than everything before it (so a[end:count] is in sorted order))
    end ← count - 1
    while end > 0 do
        (a[0] is the root and largest value. The swap moves it in front of the sorted elements.)
        swap(a[end], a[0])
        (the heap size is reduced by one)
        end ← end - 1
        (the swap ruined the heap property, so restore it)
        siftDown(a, 0, end)

 procedure heapify(a,count) is
     (end is assigned the index of the first (left) child of the root)
     end := 1

     while end < count
         (sift up the node at index end to the proper place such that all nodes above
          the end index are in heap order)
         siftUp(a, 0, end)
         end := end + 1
     (after sifting up the last node all nodes are in heap order)

 procedure siftUp(a, start, end) is
     input:  start represents the limit of how far up the heap to sift.
                   end is the node to sift up.
     child := end
     while child > start
         parent := floor((child-1) / 2)
         if a[parent] < a[child] then (out of max-heap order)
             swap(a[parent], a[child])
             child := parent (repeat to continue sifting up the parent now)
         else
             return

"""