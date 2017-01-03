# coding:utf-8
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
from simhash import Simhash
from ltpwebservice import LtpWebService
from tbldef import TblUser
from copy import deepcopy
from functools import partial

class MongoFaker(object):

    def __init__(self, host, port):
        self.__client = MongoClient(host,port).crazybot


    def insert(self,db,data):
        return self.__client[db].insert(data)
    # todo
    # def update(self,)

    def randomAq(self,url):
        try:
            return requests.get(url)
        except Exception as e:
            print e
            return None

def generate_user(n,user_dict):
    map(lambda x:user_dict.update({x:str(n)}),[i for i in user_dict])
    user_dict.update({'phone':str(1231514)+str(n)})
    user_dict.update({'username':'iam'+str(n)})
    user_dict.update({'totalnumber':5000})
    user_dict.update({'botkey':[str(n)]})
    return user_dict

if  __name__ == "__main__":
    faker = MongoFaker('192.168.10.219', 49019)
    # raw = faker.randomAq('http://www.mcmarry.com/cn/faq.html')
    # soup = BeautifulSoup(raw.content,"html.parser")
    # all_soup = soup.find(class_='custom')
    # question = [i.string for i in all_soup.find_all('strong')]
    # for i in all_soup:
        # if i.string:
            # print i.string
    # answer = filter(lambda x : x and len(x) > 8,[i.string for i in all_soup])[:-4]
    # print answer
    # or i in answer:
        # print i
    # print len(answer)
    # print len(question)

    # fuck ltp server to have token
    ltps = LtpWebService("http://192.168.50.46",9527)
    # token = ltps.segment(question)
    # print token

    # fuck simhash to have simhash value of question
    # print map(lambda x:,ltps.segment(i) for i in question])
    # print simhash_guy.simhash(ltps.segment('你好啊你好发发发'))
    # map(lambda x,y:faker.insert



    # faker.insert('KD',{'botkey':'8888','question':'自强不息厚德载物','answer':'我的强奸他么' ,'simhash':12432341,'removed':0})
    # faker.insert('KD',{'botkey':'9527','question':'强大','answer':'我的强奸他么' ,'simhash':12432341,'removed':0})
    # map(lambda x,y:faker.insert('KD',{'botkey':'9527','question':x,'answer':y ,'simhash':Simhash(unicode(x),f=32).value,'belong_to':0,'removed':0}),question,answer)
    # from functools import partial
    # print map(partial(generate_user,a=TblUser),[j for j in xrange(9520,9530)])
    result = []
    w = TblUser()
    user_dict = w.__class__.__dict__
    user_dict.pop('__module__')
    user_dict.pop('__doc__')
    user_dict.pop('tbl_name')
    # for i in xrange(9520,9530):
        # user_dict = generate_user(i,user_dict)
        # result.append(deepcopy(user_dict))
    # print result
    # map(lambda x:faker.insert('USERS',x),map(lambda x:deepcopy(partial(generate_user,user_dict=user_dict)(x)),[j for j in xrange(9520,9530)]))
    # ugly part todo beautify it
    import crawler
    for i in crawler.dates_2015:
        urls = crawler.getDaymap(i)
        for url in urls:
            try:
                question,answer = crawler.parserQandA(url+'l')
                a = faker.insert('KD',{'botkey':'9524','question':question,'answer':answer,'simhash':Simhash(unicode(question),f=32).value,'removed':0,'belong_to':0})
                # print a,type(a)
                print question,answer,a
            except Exception as e:
                print e
                continue
