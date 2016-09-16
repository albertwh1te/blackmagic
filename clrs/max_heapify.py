# coding:utf-8
from heap_test import hearp_obj


def max_heapify(A,i):
    l = A.get_left(i)
    r = A.get_right(i)
#      print(A.get_node(i),A.get_node(l))
    #  print(A.get_node(r),A.get_node(r))
    if l < A.get_length() and A.get_node(l) > A.get_node(i):
        largest = l
    else:
        largest = i
    if r < A.get_length() and A.get_node(r) > A.get_node(largest):
        largest = r
    if largest != i:
        A.arr[i-1],A.arr[largest-1] = A.arr[largest-1],A.arr[i-1]
        max_heapify(A,largest)
   

before = hearp_obj([16,4,10,14,7,9,3,2,8,1])
print(before.arr)
max_heapify(before,2)
print(before.arr)
