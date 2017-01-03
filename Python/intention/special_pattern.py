# -*- coding: utf-8 -*-
import re
import datetime

class SpecialPattern():

    def __init__(self):
        self.today = datetime.date.today()

    def get_special_time(self, sentence):
        # 孙定远
        content = sentence.decode('utf-8').replace(' ','')
        day_re = re.compile(u"(?<!\.)(?<!-)(?<!\d)"
                            u"(?P<day>[0-3]?[0-9])([\u65e5, \u53f7]?)"
                            u"(?![\u6708])(?![\u5e74])(?!\d)")
        month_re = re.compile(u"(?P<month>[0-1]?[0-9])([\u6708])")
        year_re = re.compile(u"([2]?[0]?)(?P<year>[1][6,7])([\u5e74])")
        day, month, year = re.search(day_re, content), re.search(month_re, content), re.search(year_re, content)
        if day:
            day_time = int(day.group("day"))
        else:
            day_time = self.today.day
        if month:
            month_time = int(month.group("month"))
        else:
            month_time = self.today.month
        if year:
            year_time = int(year.group("year"))
            if 16 <= year_time <= 17:
                year_time += 2000
        else:
            year_time = self.today.year
        if not (day or month or year):
            return None
        return self.confirm_date(year_time,month_time,day_time)

    def confirm_date(self, year,month,day):
        # 孙定远
        validate = 0
        daysinmonth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day >= 1 and day <= 29:
                validdate = 1
        elif month >= 1 and month <= 12:
            if day >= 1 and day <= daysinmonth[month - 1]:
                validate = 1
        if year > 2017 or year < 2016:
            validate = 0
        else:
            if day <= 9:
                day = "0" + str(day)
            if month <= 9:
                month = "0" + str(month)
            ret_date = str(year) + "-" + str(month) + "-" + str(day)
            return datetime.datetime.strptime(ret_date, '%Y-%m-%d').date()
