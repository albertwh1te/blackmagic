# coding:utf-8
# time complexity O(n)
# sapce complexity O(n)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

test_arr = [33, 4, 55, 999, 10, 88]
print test_arr
result_arr = insertion_sort(test_arr)
print result_arr
