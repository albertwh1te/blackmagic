# -*- coding: utf-8 -*-

import pymongo
from simhash import Simhash

HOST = "ubuntu"
PORT = 27017
DB = "crazybot"
USER = "crazybot"
PASSWD = "MongoDBHhly2016"
import random

mongoClient = pymongo.MongoClient(HOST, PORT)
c = mongoClient[DB]
# c.authenticate(USER, PASSWD)
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == "__main__":
    # 增加测试的用户
    # c["USERS"].remove({})
    userids = []
    for x in xrange(1, 1000):
        user = {
            "username": "happy_%s" % (x),
            "phone": random.randint(10000000000, 99999999999),
            "phone_valid_time": "2016-09-01 00:01:01",
            "email": "lisper.inmove.%s@gmail.com" % (random.randint(1, 10000000000)),
            "email_valid_time": "2016-10-11 00:00:00",
            "valid": 1,
            "lost_login_time": "2016-12-01 00:00:00",
            "level": 1,
            "totalnum": 10000,
            "accountpe": 1,
            "cardnum": "%s%s%s%s" % (510902, random.randint(1000, 9999), random.randint(1000, 9999), random.randint(1000, 9999)),
            "frontimg": "http://www.baidu.com",
            "backimg": "http://www.baidu.com",
            "passwd": "allen12345"
        }
        _id = c["USERS"].insert(user)
        if len(userids) < 50:
            userids.append(_id)

    # 生成机器人
    # c["BOT"].remove({})
    user_bots = {}
    bots = []
    for x in xrange(1, 100):
        ruser = str(random.choice(userids))
        if user_bots.get(ruser) >= 3:
            continue
        elif not user_bots.get(ruser):
            user_bots.update({ruser: 1})
        else:
            user_bots.update({ruser: user_bots.get(ruser) + 1})
        bot = {
            "authkey": ruser,
            "name": "luishen",
            "age": 0,
            "sex": 1,
            "hobby": "打篮球",
            "birthday": "2016-12-13",
            "region": "深圳",
            "removed": 0,
            "isclosed":0
        }
        botid = c["BOT"].insert(bot)
        if len(bots) < 5:
            bots.append(botid)

    questions = [
        {"question": ["你好吗?"], "answer": "还好拉"},
        {"question": ["你在哪?", "你现在在哪工作?", "你位置是哪?"], "answer": "深圳"},
        {"question": ["今天天气怎么样", "今天天气好好呀!"], "answer": "走去打球"},
        {"question": ["今晚吃什么?", "今天的东西好好吃啊!"], "answer": "吃火锅"},
        {"question": ["走打dota!", "走开黑去!", "来来来,我打中单"], "answer": "走起"},
        {"question": ["考试怎么样了?", "今天考的什么?"], "answer": "考得不好呀"}
    ]
    masters_dict = {}
    masters_list = []
    # c["KD"].remove({})
    # 添加问题答案到知识库
    for i in xrange(20,50):
        for x in xrange(1, 1000000/i):
            bot = str(random.choice(bots))
            master = "5864ebc01d41c848e2374b88"
            question = random.choice(random.choice(questions).get("question"))+str(x)
            data = {
                "botkey": str(i),
                "answer": random.choice(questions).get("answer"),
                "question": question,
                "related": [],
                "create_time": "2016-12-13 00:00:00",
                "update_time": "2016-12-13 00:00:00",
                "removed": 0,
                "belong_to": master,
                "simhash": str(Simhash(unicode(question.decode().encode('utf-8')),f=32))
            }
            _id = str(c["KD"].insert(data))
            print x

        # print _id # if x < 100:
        #     masters_list.append(_id)
        # else:
        #     if not masters_dict.get(master):
        #         masters_dict.update({master: 1})
        #     else:
        #         masters_dict.update({master: masters_dict.get(master) + 1})

    unknown_question = [
        "打lol", "春节去哪?", "国庆怎么玩", "抢到火车票了吗?", "有没有问题"
    ]
    # 添加未知问题到未知知识表
    # c["UNKNOWN_KD"].remove({})
    for x in xrange(1, 200):
        bot = str(random.choice(bots))
        data = {
            "botkey": bot,
            "question": "%s %s" % (random.choice(unknown_question), random.randint(1, 100)),
            "create_time": "2016-11-03 00:01:02",
            "score": random.randint(1, 50)
        }
        c["UNKNOWN_KD"].insert(data)

    vague_question = [
        "来不来", "去不去", "去不去看电脑", "去不去hk", "去打球么?"
    ]
    # 添加模糊问题
    # c["VAGUE_KD"].remove({})
    # ks = []
    # kds = c["KD"].find({}).limit(10)
    # for kd in kds:
    #     ks.append(kd)
    # for x in xrange(1, 300):
    #     kd = random.choice(ks)
    #     data = {
    #         "botkey": kd.get("botkey"),
    #         "question": "%s %s" % (random.choice(vague_question), random.randint(1, 100)),
    #         "answer": kd.get("answer"),
    #         "vquestion": kd.get("question"),
    #         "create_time": "2016-11-29 00:00:00",
    #         "score": random.randint(60, 80),
    #         "linked": 0,
    #         "removed": 0
    #     }
    #     c["VAGUE_KD"].insert(data)



