# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.relativedelta import relativedelta

def genMonthlist(starttime,endtime):
    results = []
    cursor = starttime
    while cursor <= endtime:
        results.append(cursor)
        cursor += relativedelta(months=1)
    return results


if __name__ == '__main__':
    starttime = datetime(2015,1,1)
    endtime = datetime(2017,6,1)
    print(genMonthlist(starttime,endtime))
