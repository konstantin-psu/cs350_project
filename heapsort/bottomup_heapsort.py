"""
function leafSearch(a, end, i) is
    j ← i
    while 2×j ≤ end do
        (Determine which of j's children is the greater)
        if 2×j+1 < end and a[2×j+1] > a[2×j] then
            j ← 2×j+1
        else
            j ← 2×j
    return j

function siftDown(a, end, i) is
    j ← leafSearch(a, end, i)
    while a[i] > a[j] do
        j ← parent(j)
    x ← a[j]
    a[j] ← a[i]
    while j > i do
        swap x, a[parent(j)]
        j ← parent(j)
"""

