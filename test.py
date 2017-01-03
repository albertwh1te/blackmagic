# -*- coding: utf-8 -*-

def distance(cur, another):
    x = (cur ^ another) & ((1 << 32) - 1)
    ans = 0
    while x:
        ans += 1
        x &= x - 1
    return ans

import time

stop_number  = (1 << 32) - 1
fuck_number = 4198850447

start_time = time.time()
i = 0
for x in xrange(stop_number-10**6,stop_number):
    distance(fuck_number,x)
    print i
    i += 1

print time.time()-start_time
