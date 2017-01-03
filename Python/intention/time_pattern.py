# -*- coding:utf-8 -*-
import os
import datetime
import special_pattern as specp
import tradition_pattern as tradp
import ltpwebservice as ltp
from dict_file import DictFile as dictf
from dateutil.relativedelta import relativedelta

class TimePattern(object):
    '''处理时间模块'''

    def __init__(self, ROOTDIR):
        '''初始化,包括输入语句,进行分词以及获取本地时间'''
        self.ROOTDIR = ROOTDIR
        # self.init_file_paths()
        self.init_time()
        # self.load_multi_dicts()

#     def init_file_paths(self):
#         '''初始化基本路径'''
#         self.order_path = '%s/data/order_time_dict.pkl'%self.ROOTDIR
#         self.date_path = '%s/data/date_time_dict.pkl'%self.ROOTDIR
#         self.number_path = '%s/data/number_dict.pkl'%self.ROOTDIR
#         self.holiday_path = '%s/data/holiday_dict.pkl'%self.ROOTDIR
#         self.tradition_path = '%s/data/tradition_dict.pkl'%self.ROOTDIR

    def init_time(self):
        '''初始化基本时间,包括服务器时间以及远古时间
        参数:
            today : 服务器上今天的时间,数据类型为datetime,格式为"年-月-日"
            start : 最早日期开始的时间,数据类型以及格式同上,年月日为1900-01-01
            trad_today: 今天时间的农历版
        '''
        self.today = datetime.date.today()
        self.start = datetime.datetime.strptime('1900-01-01','%Y-%m-%d').date()
        self.converter = tradp.TraditionConverter()
        self.special = specp.SpecialPattern()
        self.trad_today = self.convert_tradition_time('normal', self.today)

    def convert_tradition_time(self, convert_from, convert_date):
        '''阳阴日历转换
        convert_from 代表了从需要被转换的时间形式
        normal为阳历, tradition为阴历'''
        try:
            convert_result = {
                              'normal': self.converter.normal_to_tradition(convert_date),
                              'tradition': self.converter.tradition_to_normal(convert_date)
                              }[convert_from]
            return convert_result
        except:
            return None

#     def load_multi_dicts(self):
#         '''读取多个字典
#         参数:
#             order_time_dict : 时间权重字典,例如"明"代表了+1
#             date_time_dict  : 时间颗粒度字典,例如"天"代表了day
#             number_dict     : 阿拉伯数字的中文表示形式,例如"一"代表了1
#             tradition_dict  : 传统农历节假日字典,例如"元宵节"代表了"正月十五"
#             *_terms         : 代表了字典的keys
#         '''
#         self.order_time_dict, self.order_terms = self.load_single_dict(self.order_path)
#         self.date_time_dict, self.date_terms = self.load_single_dict(self.date_path)
#         self.number_dict, self.number_terms = self.load_single_dict(self.number_path)
#         self.holiday_dict, self.holiday_terms = self.load_single_dict(self.holiday_path)
#         self.tradition_dict, self.tradition_terms = self.load_single_dict(self.tradition_path)
#
#     def load_single_dict(self,path):
#         '''利用pickle读取pkl文件'''
#         with open(path, 'r') as fr:
#             single_dict = pickle.load(fr)
#         return single_dict, single_dict.keys()

    @staticmethod
    def modify_date(original_date, change_dates):
        '''根据需要更改的年月日数字,对original_date进行时间的增删
        参数:
            change_dates : 涵盖年月日的turple
        '''
        change_day, change_month, change_year = change_dates
        original_date += datetime.timedelta(days=change_day)
        original_date += relativedelta(months=change_month)
        original_date += relativedelta(years=change_year)
        return original_date

    def timediff(self, end_time, diff_type):
        '''计算时间间隔'''
        diff_result = {
                    'tradition': end_time - self.trad_today,
                    'normal': end_time - self.today
                    }[diff_type]
        return diff_result.days

    @staticmethod
    def datetime_to_string(date):
        '''将datetime类型转换成str类型'''
        return date.strftime('%Y-%m-%d')

    def chinese_to_number(self, word):
        '''把文中的中文数字表现方式替换成阿拉伯数字
        例如"二"变成2'''
        # 由于nubmer_dict中的key都是unicode形式,所以这里确保word的类型与key一样
        if type(word) is str: word = word.decode('utf-8')
        # 替换时间代词的中文代表的数字
        for chinese_number, digit_number in dictf.number_dict.items():
            word = word.replace(chinese_number, digit_number)
        return word.encode('utf-8')

    def split_dates(self, time_terms):
        '''将文中的时间类型分成数字类型时间以及文字类型时间'''
        digit_dates, chart_dates = [], []
        holiday_dates, tradition_dates = [], []
        for time_word in time_terms:
            # 农历节假日
            if time_word in dictf.tradition_dict:
                tradition_dates.append(time_word)
                continue
            # 公历节假日
            if time_word in dictf.holiday_dict:
                holiday_dates.append(time_word)
                continue
            # 替换中文代表的数字
            word = self.chinese_to_number(time_word)
            # 分开数字类型时间以及文字类型时间
            if word[0].isdigit():
                digit_dates.append(word)
            else:
                chart_dates.append(word)
        return digit_dates, chart_dates, holiday_dates, tradition_dates

    def deal_holiday_dates(self, holiday_dates):
        '''处理阳历节假日'''
        holiday_result = None
        if len(holiday_dates) == 0:
            pass
        else:
            # 仅处理第一个节假日
            date = dictf.holiday_dict[holiday_dates[0]]
            holiday = datetime.datetime.strptime(date, '%m%d').date().replace(year=self.today.year)
            # 判断是否超过了今天的时间
            if self.timediff(holiday, 'normal') >= 0:
                holiday_result = holiday
            # 超过则年份加一
            else:
                holiday_result = holiday.replace(self.today.year+1)
        return holiday_result

    def deal_tradition_dates(self, tradition_dates):
        '''处理农历节假日'''
        tradition_result = None
        if len(tradition_dates) == 0:
            pass
        else:
            # 仅处理第一个节假日
            date = dictf.tradition_dict[tradition_dates[0]]
            # 获取输入日期的农历
            if len(date) is 2:
                tradition = datetime.datetime.strptime(date, '%d')\
                    .replace(year=self.trad_today.year, month=self.trad_today.month).date()
            else:
                tradition = datetime.datetime.strptime(date, '%m%d')\
                    .replace(year=self.today.year).date()
            # 判断是否超过了今天的农历时间
            time_slot = self.timediff(tradition, 'tradition')
            if time_slot >= 0:
                pass
            # 超过则年份加一
            elif time_slot >= -31:
                tradition = tradition.replace(month=self.trad_today.month + 1)
            else:
                tradition = tradition.replace(year=self.trad_today.year + 1)
            tradition_result = self.convert_tradition_time('tradition', tradition)
        return tradition_result

    def deal_digit_dates(self, digit_dates):
        '''处理数字类型时间
        将文中pos为nt的单词进行时间模式匹配'''
        # 时间不同的表现形式
        time_formats = ['%Y.%m.%d','%Y-%m-%d','%Y%m%d','%d日','%m月','%Y年','%y年']
        input_time, output_time = None, None
        output_year, output_month, output_day = None, None, None
        # 判断时间是否满足规定的时间表现形式
        for tf in time_formats:
            for time in digit_dates:
                try:
                    # 转换时间格式为datetime
                    input_time = datetime.datetime.strptime(time,tf).date()
                    # 补全年月日判断,仅保留不为远古时间的年月日
                    if input_time.year != self.start.year:
                        output_year = input_time.year
                    if input_time.month != self.start.month:
                        output_month = input_time.month
                    # 解决用户输入日期与1号重叠
                    if input_time.day != self.start.day or tf == '%d日':
                        output_day = input_time.day
                    break
                except:
                    continue
        # 缺失年和月的时间信息,补全为当前时间的年月
        if output_year  is None: output_year  = self.today.year
        if output_month is None: output_month = self.today.month
        # 时间模式匹配的时候,可以缺失年和月,但是具体天数不能缺失
        if output_day   is None: return None
        # 根据记录的年月日更改时间
        output_time = self.start.replace(year  = output_year,
                                         month = output_month,
                                         day   = output_day)
        return output_time

    def deal_chart_dates(self, chart_dates):
        '''处理文字类型时间
        将文中pos为nt的单词进行拆解
        分别拆解为时间颗粒度,例如"年月周日",还有时间权重'''
        chart_length = len(chart_dates)
        output_day, output_month, output_year = 0, 0, 0
        date_type, time_score = None, None
        # 判断文字类型的时间数列是否为空
        if chart_length > 0:
            # 仅考虑第一个时间代词
            time_word = chart_dates[0]
            # 判断具体时间颗粒度
            for dt in dictf.date_time_dict:
                if dt in time_word:
                    date_type = dictf.date_time_dict[dt]
                    break
            # 判断具体时间权重
            for ot in dictf.order_time_dict:
                if ot in time_word:
                    time_score = dictf.order_time_dict[ot]
                    break
            if date_type is None or time_score is None:
                return output_day, output_month, output_year
            else:
                # 根据时间颗粒度以及权重,得出需要更改的年月日
                if date_type == 'day':
                    output_day = time_score
                if date_type == 'week':
                    output_day = time_score * 7
                if date_type == 'month':
                    output_month = time_score
                if date_type == 'year':
                    output_year = time_score
                return output_day, output_month, output_year
        else:
            return output_day, output_month, output_year


    def deal_dates(self, time_terms, sentence):
        '''根据处理过的文字以及数字类型时间,进行结合计算时间
        原理是基础时间和更改时间相结合
        change_digit_dates: 基础时间, 由deal_digit_dates得出
        change_chart_dates: 更改时间, 由deal_chart_dates得出
        如果仅有文字类型时间,那么基础时间则为当天
        如果仅有数字类型时间,那么更改时间则为0'''
        digit_dates, chart_dates, holiday_dates, tradition_dates = self.split_dates(time_terms)
        change_digit_dates = self.deal_digit_dates(digit_dates)
        change_chart_dates = self.deal_chart_dates(chart_dates)
        change_holiday_dates = self.deal_holiday_dates(holiday_dates)
        change_tradition_dates = self.deal_tradition_dates(tradition_dates)
        # 农历优先级最高
        if change_tradition_dates:
            return change_tradition_dates
        # 节假日优先级第二
        if change_holiday_dates:
            return change_holiday_dates
        # 处理基础时间不为空的情况
        if change_digit_dates:
            return self.modify_date(change_digit_dates, change_chart_dates)
        elif change_chart_dates == (0,0,0):
            # 无法获取任何时间类型处理情况
            special_result = self.special.get_special_time(sentence)
            if special_result:
                return special_result
            else:
                return self.modify_date(self.today, change_chart_dates)
        # 缺失数字类型时间,但是拥有文字类型时间的情况
        else:
            return self.modify_date(self.today, change_chart_dates)
