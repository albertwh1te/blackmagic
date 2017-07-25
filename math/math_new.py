# -*- coding: utf-8 -*-
import math

def split_numbers(x,y):
    if x == 0 or y < x:
        return []
    new_res = []
    results = [y/x] * x
    results[x-1] += y % x
    counter = 0
    for i in results:
        counter += i
        new_res.append(counter)
    return new_res

print(split_numbers(0,100))
print(split_numbers(3,2))
print(split_numbers(5,100))
print(split_numbers(3,100))
