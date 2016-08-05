# coding:utf-8
import time


def time_func(func):
    def _wrapper():
        start = time.clock()
        print start
        func()
        end = time.clock()
        print end
    return _wrapper

@time_func
def test_it():
    print "see"

test_it()
#  #  test_it = time_func(test_it)
#  test_it()
#  print test_it
#  print test_it()
