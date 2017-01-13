# -*- coding: utf-8 -*-

from datetime import timedelta,datetime

a = datetime.now()
for i in xrange(-10,10):
    difference = timedelta(days=i)
    perturbation = a + difference
    always_sunday = perturbation + timedelta(days=(6-perturbation.weekday()))
    print always_sunday.weekday(),"\n",always_sunday.date()
