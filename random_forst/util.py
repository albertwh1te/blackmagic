# -*- coding: utf-8 -*-

import time
import datetime

# 字符串转时间戳
def str2timestamp(d, f = "%Y-%m-%d %H:%M:%S"):
    t = time.strptime(d, f)
    return time.mktime(t)

# 时间戳转字符串
def timestamp2str(d, f = "%Y-%m-%d %H:%M:%S"):
    x = time.localtime(d)
    return time.strftime(f, x)

def getDay(days = 0, f = "%Y-%m-%d"):
    currTime = datetime.datetime.now()
    day = currTime + datetime.timedelta(days)
    return datetime.datetime.strftime(day, f)

def safe_int(p):
    try:
        return int(p)
    except Exception as ex:
        return None

def safe_index(array, index):
    try:
        a = array[index]
        return True, a
    except Exception as ex:
        return False, None

def requestParam(request, key, default = None):
    return request.args.get(key, default) if key in request.args.keys() else request.form.get(key, default)

class DATA:
    @staticmethod
    def make(a,s,q):
        return {"answer":a,"score":s,"question":q}

class RetCode:

    CODE = "code"
    MSG = "msg"
    DATA = "data"

    SUCCESS = (0, "请求成功")
    UNKNOWN_ERROR = (1, "未知错误")
    FAIL = (9, "失败")
    PARAMETER_NOT_ENOUGH = (1001, "参数不足")
    REDIS_ERROR = (1002, "redis出错")
    MONGO_ERROR = (1003, "mongo连接出错")
    STOP_UPDATE = (1004, "暂停更新")
    SERVER_ERROR = (1005, "服务器错误")
    BOTKEY_ERROR = (1006, "botkey错误")
    RUNOUT = (1007, "调用次数用尽")


    @staticmethod
    def sucess(f,d):
        """
            f a function current represent as jsonify
            d data that pass in,current is a dict
         """
        result = {
            RetCode.CODE: RetCode.SUCCESS[0],
            RetCode.MSG : RetCode.SUCCESS[1],
            RetCode.DATA: {}
        }
        return f(result)

class ConstantVal:
    authkey = "authkey"
    botkey = "botkey"
    _id = "_id"
    username = "username"
    phone = "phone"
    question = "question"
    answer_list_eng = 'answer_list_eng'
    answer_list_num = 'answer_list_num'
    answer_list_default = 'answer_list_default'
