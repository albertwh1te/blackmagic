# -*- coding=utf-8 -*-
import time
def time_cost(func):
    def wrapper(**kwargs):
        print(kwargs)
        start = time.clock()
        func()
        cost = time.clock() - start
        print('the cost time is ', cost)
    return wrapper

@time_cost
def test_func(time=None):
    sum = 0
    for i in range(100000):
        sum *= i
    print(sum)

if __name__ == "__main__":
    test_func(time=3)