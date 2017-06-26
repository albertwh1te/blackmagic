# -*- coding: utf-8 -*-


import time


for i in range(100000):
    a = time.time()
    if str(a)[:10] != str(int(a)):
        print(str(a)[:10],str(int(a)),a)
