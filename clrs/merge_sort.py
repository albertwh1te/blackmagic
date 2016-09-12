# coding:utf-8
# this scripts should run with python3

def merge(Arr_1,Arr_2):
    merge_arr = []
    i = 0
    j = 0
    #  print merge_arr
    while i < len(Arr_1) and j < len(Arr_2):
        if Arr_1[i] < Arr_2[j]:
            merge_arr.append(Arr_1[i])
            i += 1
        #  if Arr_1[i] > Arr_2[j]: 
        else:
            merge_arr.append(Arr_2[j])
            j += 1
            
    
    if i == len(Arr_1) and j < len(Arr_2):
        merge_arr += Arr_2[j:]

    if j == len(Arr_2) and i < len(Arr_1):
        merge_arr += Arr_1[i:]
    return merge_arr
    

test_A = [2,5,8,11]
test_B = [1,3,6,7]
print(merge(test_A,test_B))


def merge_sort(arr):
    arr_len = len(arr)
    if arr_len > 1:
        import math
        left_half = merge_sort(arr[math.ceil(len(arr)/2):])
        right_half = merge_sort(arr[:math.ceil(len(arr)/2)])
        return merge(left_half,right_half)
    else:
        return arr


print(merge_sort([10,11,115,4,2,8,3,1]))
