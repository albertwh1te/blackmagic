# coding:utf-8
# this scripts should run with python3
import math

def merge(Arr_1,Arr_2):
    merge_arr = []
    i = 0
    j = 0
    #  print merge_arr
    while i < len(Arr_1) and j < len(Arr_2):
        if Arr_1[i] < Arr_2[j]:
            print i,j
            print Arr_1[i]
            merge_arr.append(Arr_1[i])
            i += 1
            print "i",i
            #  print merge_arr
        if Arr_1[i] > Arr_2[j]: 
            print Arr_2[j]
            merge_arr.append(Arr_2[j])
            #  print merge_arr
            j += 1
            print "j",j
            
    
    if i == len(Arr_1) and j < len(Arr_2):
        merge_arr += Arr_2[j:]
        print Arr_2[j:]

    if j == len(Arr_2) and i < len(Arr_1):
        merge_arr += Arr_1[i:]
        print Arr_1[i:]
    return merge_arr
    

test_A = [2,5,8,11]
test_B = [1,3,6,7]
print merge(test_A,test_B)
       
    
    

   
    

