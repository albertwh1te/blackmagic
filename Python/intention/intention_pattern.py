# -*-coding: utf-8 -*-
import os
import ltpwebservice as ltp
import time_pattern as timep
import loc_pattern as locp
from list_file import ListFile as listf
from dict_file import DictFile as dictf
# from module import ltpwebservice as ltp
# from module import time_pattern as timep
# from module import loc_pattern as locp
# from module.list_file import ListFile as listf

# ROOTDIR = os.path.dirname(os.path.realpath(__file__))

class Intention(object):
    '''意图识别模块'''

    def __init__(self, ROOTDIR, sentence):
        self.sentence = sentence
        #self.sentence = raw_input('INPUT\n')
        self.ROOTDIR = ROOTDIR
        # self.init_file_paths()
        # self.load_multi_dicts()
        self.load_ltp_server()
        self.timepattern = timep.TimePattern(ROOTDIR)

#     def init_file_paths(self):
#         '''初始化路径'''
#         self.train_intention_path = '%s/data/train_intention.pkl'%self.ROOTDIR
#         self.weather_intention_path = '%s/data/weather_type.pkl'%self.ROOTDIR
#
#     def load_multi_dicts(self):
#         '''读取多个字典
#         参数:
#             weather_intent : 天气关键词字典,{'温度':'WD'}
#             train_intent   : 火车关键词字典,{'动车':'train'}
#         '''
#         self.weather_intent, self.weather_terms = self.load_single_dict(self.weather_intention_path)
#         self.train_intent, self.train_terms = self.load_single_dict(self.train_intention_path)
#
#     def load_single_dict(self,path):
#         '''利用pickle读取pkl文件'''
#         with open(path, 'r') as fr:
#             single_dict = pickle.load(fr)
#         return single_dict, single_dict.keys()

    def load_ltp_server(self):
        '''初始化ltp,并进行词性分析'''
        ltps = ltp.LtpWebService("http://192.168.50.46",9527)
        self.ltp_result = ltps.parser(self.sentence)

    @staticmethod
    def judge_quest_mark(word,pos):
        '''判断是否为疑问代词'''
        # 标点符号识别
        wp_fun = lambda word,pos: pos == 'wp' and word is '?' or word is '？'
        # 疑问代词识别,例如'怎么样'
        quest_fun = lambda word,pos: pos is 'r' and word not in listf.person_list
        # 语气助词识别,例如'吗'
        mood_fun = lambda word,pos: pos is 'u' and word not in listf.mood_list
        # 量词识别,例如"几度",排除阿拉伯数字以及文字类型的量词
        quant_fun = lambda word,pos: pos is 'm' \
                    and not word[0].isdigit() and word not in dictf.number_dict
        judge_quest = wp_fun(word,pos) or quest_fun(word,pos) or \
                      mood_fun(word,pos) or quant_fun(word,pos)
        return judge_quest

    @staticmethod
    def judge_time_mark(pos):
        '''判断是否为时间代词'''
        return pos == 'nt'

    @staticmethod
    def judge_loc_mark(pos):
        '''判断是否为地点代词'''
        return pos == 'ns'

    @staticmethod
    def judge_ask_mark(word, pos):
        '''判断是否为询问代词'''
        return pos == 'v' and word in listf.ask_list

    def judge_marks(self, word, pos):
        '''判断代词类型'''
        if self.judge_quest_mark(word, pos):
            return 'quest'
        if self.judge_time_mark(pos):
            return 'time'
        if self.judge_loc_mark(pos):
            return 'loc'
        if self.judge_ask_mark(word, pos):
            return 'ask'

    def judge_weather_intention(self, word):
        '''判断是否有天气关键词'''
        return word in dictf.weather_intent

    def judge_train_intention(self, word, pos):
        '''判断是否有火车关键词'''
        # 判断单词中是否包含关键词,例如"火车票"中含有"火车"这个关键词
        contain_chinese_fun = lambda word: [i in word for i in dictf.train_intent].count(True) > 0
        # 判断中文关键词, 例如"火车票"
        chinese_fun = lambda word,pos: pos in ['n','b','v'] and \
                                      (word in dictf.train_intent  or contain_chinese_fun(word))
        # 判断列车号关键词
        digit_fun = lambda word,pos: pos == 'ws' and word[0] in ['D','G','T','C','K','Z','L','Y']
        return chinese_fun(word,pos) or digit_fun(word,pos)

    def judge_intention(self, word, pos):
        '''意图识别,并返回意图类型'''
        if self.judge_weather_intention(word):
            return 'weather'
        if self.judge_train_intention(word, pos):
            return 'train'

    @staticmethod
    def deep_weather_intention(intention_result):
        '''确定天气意图'''
        weather_again_sentence = '请重新输入 "城市 + 天气", 例如"深圳 天气"'
        # 判断时间是否在范围之内
        range_time = lambda result: result['timediff'] in [0,1]
        # 是否为询问语气判断
        has_quest = lambda result: int(len(result['quest']) != 0 or len(result['ask']) != 0)
        # 是否含有地点代词判断
        has_loc = lambda result: int(len(result['loc']) != 0)
        # 综合判断
        deep_judge = (has_quest(intention_result), has_loc(intention_result))
        # 有疑问代词, 有地点名词
        if deep_judge == (1,1):
            return 'continue'
#             if range_time(intention_result):
#                 return 'continue'
#             # 如果时间超出范围, 天气的时间范围是1天内
#             else:
#                 print '时间超出范围, ' + weather_again_sentence
#                 return 'again'
        # 无疑问代词, 有地点名词, 且仅有地点和领域两词, 或者地点领域时间三个词
        elif deep_judge == (0,1) and intention_result['length'] is 1:
            return 'continue'
#             if range_time(intention_result):
#                 return 'continue'
#             else:
#                 print '时间超出范围, ' + weather_again_sentence
#                 return 'again'
        # 无疑问代词, 无地点名词, 且仅有领域一个词
        elif deep_judge == (0,0) and intention_result['length'] is 1:
            print weather_again_sentence
            return 'again'
        # 有疑问代词, 缺失地点名词
        elif deep_judge == (1,0):
            print weather_again_sentence
            return 'again'
        # 其他情况
        else:
            # print '无意图,进入匹配'
            return None

    @staticmethod
    def deep_train_intention(intention_result):
        '''确定火车意图'''
        train_again_sentence = '请重新输入 "路线 + 火车", 例如"从深圳到北京 火车票"'
        # 判断时间是否在范围内
        range_time = lambda result: result['timediff'] in xrange(0,30)
        # 是否为询问语气判断
        has_quest = lambda result: int(len(result['quest']) != 0 or len(result['ask']) != 0)
        # 是否含有地点代词判断
        has_loc = lambda result: int(len(result['loc']) != 0)
        # 是否还有两个相邻的地点代词判断, 因为定火车票需要出发地以及目的地
        enough_loc = lambda result: int(len(result['loc']) is 2)
        # 综合判断
        deep_judge = (has_quest(intention_result), has_loc(intention_result))
        # 有地点名词, 且有足够的地点名词
        if deep_judge in [(1,1),(0,1)] and enough_loc(intention_result):
            return 'continue'
#             if range_time(intention_result):
#                 return 'continue'
#             # 时间超出范围, 火车的时间范围是30天内
#             else:
#                 print '时间超出范围, ' + train_again_sentence
#                 return 'again'
        # 有疑问代词, 有地点名词, 没有足够的地点名词
        elif deep_judge == (1,1) and not enough_loc(intention_result):
            print train_again_sentence
            return 'again'
        elif deep_judge == (0,0) and intention_result['length'] is 1:
            return 'again'
        # 有疑问代词, 没有地点名词
        elif deep_judge == (1,0):
            print train_again_sentence
            return 'again'
        # 其他情况
        else:
            # print '无意图,进入匹配'
            return None

    def get_low_intention(self):
        '''初步意图识别'''
        low_intention_result = {'quest':[],       #疑问代词(list)
                                'ask':[],         #询问代词(list)
                                'loc':{},         #地点信息(dict)
                                'time':[],        #时间信息(datetime)
                                'intention':None, #意图类型(string)
                                'details':{},     #意图详情(dict)
                                'length':0,       #语句长度(int)
                                'timediff':0}     #时间间隔(int)
        # low_intention_result['length'] = len([1 for lr in self.ltp_result if lr['pos'] not in ['a', 'u']])
        for lr in self.ltp_result:
            word = lr['cont'].encode('utf-8')
            pos = lr['pos'].encode('utf-8')
            index = int(lr['id'].encode('utf-8'))
            # 获取意图类型
            intention = self.judge_intention(word, pos)
            if intention:
                low_intention_result['intention'] = intention
            # 获取代词类型
            judge_tag = self.judge_marks(word, pos)
            # 单独处理地点信息,因为其数据类型为dict
            if judge_tag == 'loc':
                low_intention_result[judge_tag][index] = word
            # 处理其他意图信息, 例如时间
            elif judge_tag:
                low_intention_result[judge_tag].append(word)
        low_intention_result['length'] = len(self.ltp_result) - \
                                         len(low_intention_result['time']) - \
                                         len(low_intention_result['loc'])
        return low_intention_result

    def get_deep_intention(self, intention_result):
        '''进一步意图识别'''
        train_again_sentence = '请重新输入 "路线 + 火车", 例如"从深圳到北京 火车票"'
        weather_again_sentence = '请重新输入 "城市 + 天气", 例如"深圳 天气"'
        if intention_result['intention']:
            # 转换时间以及地点为规定格式
            format_time = self.timepattern.deal_dates(intention_result['time'],self.sentence)
            format_loc = locp.LocPattern.deal_locations(intention_result['loc'])
            # 替换时间以及地点, 且时间数据类型转换成string
            intention_result['time'] = self.timepattern.datetime_to_string(format_time)
            intention_result['loc'] = format_loc
            intention_result['timediff'] = self.timepattern.timediff(format_time, 'normal')
            if intention_result['intention']:
                # 根据意图类型,确认是否为真意图
                deep_result = {
                               'weather': lambda result: self.deep_weather_intention(result),
                               'train'  : lambda result: self.deep_train_intention(result)
                               }[intention_result['intention']](intention_result)
                return {
                        'continue': intention_result,
                        'again'   : {
                                    'weather':weather_again_sentence,
                                    'train':train_again_sentence
                                    }[intention_result['intention']],
                        None      : self.ltp_result
                       }[deep_result]
        else:
            # print '无意图,进入匹配'
            return self.ltp_result

    def get_intention(self):
        '''获取全部意图
        这里只要判断是否为字典类型,就决定是否有意图
        NoneType : 重新输入,因为缺少某些意图成分
        dict     : 意图抓取,意图完整
        list     : 无意图,进入匹配系统'''
        low_intention_result = self.get_low_intention()
        high_intention_result = self.get_deep_intention(low_intention_result)
        return high_intention_result

# '''
# 记得加上意图中的具体信息,例如天气中的子类-温度,火车中的车等级以及座位等级
# '''
# if __name__ == '__main__':
#     while True:
#         intent = Intention(ROOTDIR)
#         intention_result = intent.get_intention()
#         result_type = type(intention_result)
#         print {
#                 list: '\n没有意图,进入匹配',
#                 dict: '\n意图完整,数据抓取',
#                 type(None): '\n重新输入,缺失意图'
#                 }[result_type]
#         if type(intention_result) is dict:
#             print '\n结果是:#########'
#             for i,j in intention_result.items():
#                 if i == 'loc':
#                     try:
#                         print '出发地点:%s\t目的地点:%s'%(j['start'],j['end'])
#                     except:
#                         print '出发地点:%s'%(j['start'])
#                 if i == 'time':
#                     print '具体时间:\t%s'%j
#                 if i == 'intention':
#                     print '意图类型:\t%s'%j
