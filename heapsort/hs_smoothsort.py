from base import *

def isAscending(v1, v2):
    """Comparator function"""
    return v1 <= v2


def up(vb, vc):
    temp = vb
    vb += vc + 1
    vc = temp
    return vb, vc


def down(vb, vc):
    temp = vc
    vc = vb - vc - 1
    vb = temp
    return vb, vc


def smoothSort(A):
    """The main SmoothSort function
        Variables: q,r,p,b,c,r1,b1,c1,N
    """

    def sift():
        nonlocal r1, b1, c1
        r0 = r1
        T = A[r0]
        while b1 >= 3:
            testbase.BASIC +=1
            r2 = r1 - b1 + c1

            if not isAscending(A[r1 - 1], A[r2]):
                r2 = r1 - 1
                b1, c1 = down(b1, c1)
            if isAscending(A[r2], T):
                b1 = 1
            else:
                A[r1] = A[r2]
                r1 = r2
                b1, c1 = down(b1, c1)
        if r1 != r0:
            A[r1] = T

    def trinkle():
        nonlocal p, b1, c1, b, c, r1
        p1 = p
        b1 = b
        c1 = c
        r0 = r1
        T = A[r0]
        while p1 > 0:
            while (p1 & 1) == 0:
                testbase.BASIC += 1
                p1 >>= 1
                b1, c1 = up(b1, c1)
            r3 = r1 - b1
            if p1 == 1 or isAscending(A[r3], T):
                p1 = 0
            else:
                p1 -= 1
                if b1 == 1:
                    A[r1] = A[r3]
                    r1 = r3
                elif b1 >= 3:
                    r2 = r1 - b1 + c1
                    if not isAscending(A[r1 - 1], A[r2]):
                        r2 = r1 - 1
                        b1, c1 = down(b1, c1)
                        p1 <<= 1
                    if isAscending(A[r2], A[r3]):
                        A[r1] = A[r3]
                        r1 = r3
                    else:
                        A[r1] = A[r2]
                        r1 = r2
                        b1, c1 = down(b1, c1)
                        p1 = 0
        if r0 != r1:
            A[r1] = T
        sift()

    def semitrinkle():
        nonlocal r1, r, c
        r1 = r - c
        if not isAscending(A[r1], A[r]):
            A[r], A[r1] = A[r1], A[r]
            trinkle()

    # Start of main function
    N = len(A)
    q = 1
    r = 0
    p = 1
    b = 1
    c = 1
    #building the tree
    while q < N:
        testbase.BASIC += 1
        r1 = r

        if (p & 7) == 3:
            b1 = b
            c1 = c
            sift()
            p = (p + 1) >> 2
            b, c = up(b, c)
            b, c = up(b, c)
        elif (p & 3) == 1:
            if (q + c) < N:
                b1 = b
                c1 = c
                sift()
            else:
                trinkle()
            b, c = down(b, c)
            p <<= 1
            while b > 1:
                b, c = down(b, c)
                p <<= 1
            p += 1
        q += 1
        r += 1

    r1 = r
    trinkle()

    #build the sorted array
    while q > 1:
        testbase.BASIC += 1
        q -= 1
        if b == 1:
            r -= 1
            p -= 1
            while (p & 1) == 0:
                p >>= 1
                b, c = up(b, c)
        elif b >= 3:
            p -= 1
            r = r - b + c
            if p > 0:
                semitrinkle()
            b, c = down(b, c)
            p = (p << 1) + 1
            r += c
            semitrinkle()
            b, c = down(b, c)
            p = (p << 1) + 1
            # element q is done
            # element 0 is done

class sortRun(testbase):
    name="mergesort"
    #Declare test type just to stay consistent
    mergesort = 0
    mergesort1 = 1

    def __init__(self, size, ceiling, asInt, rtype):
        self.size = size
        self.gen  = randomizer.generator(maximum=ceiling,asInt=asInt)
        self.toSort = self.gen.gen(rtype,size)
        self.CEILING = ceiling
        self.INT = asInt
        self.PARTITIONTYPE = self.ptypes[rtype]
        end = len(self.toSort)
        B = [None] * end
        start = time.perf_counter()
        self.begin= time.perf_counter()
        smoothSort(self.toSort)
        # self.toSort = self.mergesort1(self.toSort)
        end = time.perf_counter()
        self.TOTALRTIME = end - start
        self.SPLITRTIME += self.TOTALRTIME - self.SORTHELPERRTIME
        # pprint(self.toSort)
        self.setinfo()
        self.dump()

def run():
    # alist = [54,26,93,17,77,31,44,55,20]
    # smoothSort(alist)
    # print(alist)
    srt = sortRun(size=size, ceiling=ceiling, asInt=isInt, rtype=partType)


run()

