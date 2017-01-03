# -*- coding: utf-8 -*-

from fake_user import MongoFaker
from ltpwebservice import LtpWebService
from simhash import Simhash
import time
from util import timestamp2str

def Simhash_ltp(question,ltp):
    return Simhash(ltps.segment_list(question),f=32).value


if __name__ == "__main__":
    botkey_list = ['5861db271d41c8eeb5ad81f8','586218e51d41c8772ca1c1d4']
    question = u'我是测试问题'
    answer = u'我是测试答案'
    best_score=70
    faker = MongoFaker('192.168.10.219', 49019)
    ltps = LtpWebService("http://192.168.50.46",9527)
    for botkey in botkey_list:
        for i in xrange(1,300):
            create_time =timestamp2str( int(time.time()) )
            question = question+str(i)
            answer = answer+str(i)
            a = faker.insert('KD',{'botkey':botkey,'question':question,'answer':answer,'simhash':Simhash(unicode(question+str(i)),f=32).value,'removed':0,'belong_to':0,'create_time':create_time,'update_time':create_time})
            faker.update('KD',{'question':question},{'$set':{'belong_to':str(a)}})
            faker.insert('VAGUE_KD',{"vquestion":"地我的哦的哦","botkey":botkey,'question':question,'answer':answer,"removed":0,"score":best_score,"question_id":str(a),"create_time":create_time,'linked':0})
