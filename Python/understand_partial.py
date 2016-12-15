# coding:utf-8

from functools import  partial

def power(n,x):
    return n ** x

square = partial(power,x=2)
cube = partial(power,x=3)

def test_partial():
    assert square(2) == 4
    assert cube(2) == 8

test_partial()
