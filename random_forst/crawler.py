# -*- coding: utf-8 -*-

import requests
import json
from utils import headers
from bs4 import BeautifulSoup
from datetime import date,timedelta
import time


cookies_jar = requests.get('http://www.haodf.com/', headers=headers).cookies

# print cookies_jar


def parserQandA(url):
    raw = requests.get(url,headers=headers).content
    soup = BeautifulSoup(raw,'html.parser')
    question = soup.find(class_='h_s_cons_info_title')
    # answer = soup.find_all(class_='h_s_cons_title')
    # print soup,raw,question,answer
    answer = soup.find_all(class_='h_s_cons_title')[0]
    return question.string[5:],answer.string


def getDaymap(date):
    date = str(date).replace('-','')
    url = 'http://www.haodf.com/sitemap-zx/'+date+'_1/'
    raw = requests.get(url,headers=headers).content
    soup = BeautifulSoup(raw,'html.parser')
    urls = soup.find(class_='hh').find_all('a')
    return map(lambda x:str(x.get('href')), urls)
# except Exception as e:
    # print e

# print getDaymap(str(date(2016,12,1)).replace('-',''))[:-1]
start_date = date(2016,1,1)
end_date = date(2016,12,1)
dates_2016 = [ start_date + timedelta(n) for n in range(int ((end_date - start_date).days))]

start_date = date(2014,1,1)
end_date = date(2014,12,1)
dates_2015 = [ start_date + timedelta(n) for n in range(int ((end_date - start_date).days))]

# print map(lambda x:getDaymap(str(x).replace('-','')),[dates_2016])

# result = []
# for i in dates_2016:
#     urls = getDaymap(i)
#     for url in urls:
#         a,b = parserQandA(url+'l')
#         print a,b,unicode(a)
