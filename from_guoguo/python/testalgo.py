from random import randrange
from collections import Counter, defaultdict


def max_prematation(M, A=None):
    if A is None:
        A = set(range(len(M)))
    if len(A) == 1:
        return A
    B = set([M[i] for i in A])
    C = A - B
    if len(C):
        A.remove(C.pop())
        return max_prematation(M, A)
    return A


def max_perm(M):
    n = len(M)
    A = set(range(n))
    counter = Counter(M)
    lossers = [i for i in A if counter[i] == 0]
    while lossers:
        losser = lossers.pop()
        A.remove(losser)
        pointto = M[losser]
        counter[pointto] -= 1
        if counter[pointto] == 0:
            lossers.append(pointto)
    return A


def findNestest(seq):
    dd = float('inf')
    for x in seq:
        for y in seq:
            d = abs(x - y)
            if x == y:
                continue
            if d < dd:
                xx, yy, dd = x, y, d
    print(xx, yy, dd)


def findNestest_Fast(seq):
    dd = float("inf")
    seq.sort()
    for i in range(len(seq) - 1):
        if seq[i] == seq[i + 1]:
            continue
        d = abs(seq[i] - seq[i + 1])
        if d < dd:
            xx, yy, dd = seq[i], seq[i + 1], d
    print(xx, yy, dd)


def selectionSortRecursion(alist, length):
    if length == 0:
        return
    max_index = length
    for i in range(length):
        if alist[i] > alist[max_index]:
            max_index = i
    alist[length], alist[max_index] = alist[max_index], alist[length]
    selectionSortRecursion(alist, length - 1)
    return alist


def selectionSortIteration(alist):
    for j in range(len(alist) - 1, 0, -1):
        max_index = j
        for i in range(j):
            if alist[i] > alist[max_index]:
                max_index = i
        alist[j], alist[max_index] = alist[max_index], alist[j]
    return alist


def counting_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    for key in range(min(C), max(C) + 1):
        B.extend(C[key])
    return B


def main():
    seq = [randrange(10 * 10) for i in range(10)]
    findNestest(seq)
    findNestest_Fast(seq)
    alist = [3, 20, 1441, 25, 6]
    print(selectionSortRecursion(alist, len(alist) - 1))
    print(selectionSortIteration(alist))
    print(counting_sort(alist))
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    print(M)
    print(max_prematation(M))
    print(max_perm(M))


if __name__ == '__main__':
    main()
