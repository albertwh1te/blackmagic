# -*- coding: utf-8 -*-
import requests
from functools import wraps
import time

def time_it(func):
    # @wraps
    def _wrapper(*args,**kwargs):
        start_time = time.clock()
        result = func(*args,**kwargs)
        cost_time = start_time - time.clock()
        return result,cost_time
    return _wrapper

@time_it
def calc_post(url,info):
    return requests.post(url,data=info)

@time_it
def calc_get(url,info):
    return requests.get(url)



