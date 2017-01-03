# -*- coding: utf-8 -*-

import re
from random import choice
from service.tbldef import ConstVariableName
from service.rediskeydef import get_config_redis

class MeaningfulSentence:
    """
        检查语句是不是有意义的语句
    """
    def __init__(self, ltpserver):
        self.splitchar = ";"
        self.pattern = re.compile("(\[1f[0-2]\d\]|\[1f3[0-6]\])")
        self.ltpserver = ltpserver

    # def useful_word_filter(self, sen, redisClient, segment, postag):
    def useful_word_filter(self, sen, redisClient):
        """
            检测这一句是不是有意义的语句
        """
        if len(unicode(sen.strip(),"utf-8")) == 1:
            return True, -1
        word = re.sub(self.pattern, self.splitchar, sen.strip())
        # word_list = segment(word)
        # word_dict = postag(word_list)
        raw  = self.ltpserver.postagger(word)
        word_list = []
        word_dict = {}
        word_list = [str(meat['cont']) for meat in raw]
        # word_dict = [meat['pos'] for meat in raw]
 #       print word_list,[meat['pos'] for meat in raw]
        map(lambda x,y:word_dict.update({x:y}),word_list,[meat['pos'] for meat in raw])

        result = self.__word_classify(word_dict, redisClient)
        if result.get("useful") != 0:
            return False, 0
        if self.__english_only(result):
            return True, 1
        if self.__nums_only(result):
            return True, 2
        if self.__face_only(result):
            return True, 3
        return True, -1

    def __english_only(self, ret):
        """ 只有英文 """
        return ret["ws"] != 0 and ret["wp"] == 0 and ret["poe"] == 0 and ret["stopword"] == 0 and ret["face"] == 0 and ret["num"] == 0
    def __nums_only(self, ret):
        """ 只有数字 """
        return ret["num"] != 0 and ret["wp"] == 0 and ret["poe"] == 0 and ret["stopword"] == 0 and ret["face"] == 0 and ret["face"] == 0
    def __face_only(self, ret):
        """ 只有表情 """
        return ret["face"] != 0 and ret["wp"] == 0 and ret["poe"] == 0 and ret["stopword"] == 0 and ret["ws"] == 0 and ret["num"] == 0

    def __word_classify(self, word_dict, redisClient):
        result = {
            "wp": 0,
            "poe": 0,
            "face": 0,
            "num": 0,
            "stopword": 0,
            "useful": 0,
            "ws": 0
        }
        for k,v in word_dict.items():
            if v == 'p' or v == 'o' or v == 'e':
                result["poe"] += 1
            elif k == self.splitchar:
                result["face"] += 1
            elif v == 'wp':
                result["wp"] += 1
            elif v == 'm':
                result["num"] += 1
            elif k.isalpha():
                result["ws"] += 1
            else:
                result2 = redisClient.hget("stopword", k)
                if result2 != None:
                    result["stopword"] += 1
                else:
                    result["useful"] += 1
        return result

    def answer_static(self, mongoClient, redisClient, w = 0):
        configs = get_config_redis(mongoClient, redisClient)
        eng = configs.get(ConstVariableName.answer_list_eng)
        num = configs.get(ConstVariableName.answer_list_num)
        default = configs.get(ConstVariableName.answer_list_default)
        if w == 1:# 只有英文和符号
            answer_list = eng or ["给我找个英文老师先!","看到英文就头疼","麻烦翻译一下先!"]
        elif w == 2: # 只有数字和符号
            answer_list = num or ["看到数字就晕","不要发暗语好不好？"]
        else:
            answer_list = default or ["呵呵","什么意思呀？","火星文？"]
        return choice(answer_list)
