import requests
from bs4 import BeautifulSoup
from models import Stock
from utils import headers,BASE_URL,engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


cookies_jar  = requests.get('https://xueqiu.com',headers=headers).cookies
stocks_list = []
Session = sessionmaker(bind=engine)
session = Session()

for stock in session.query(Stock.code):
    stocks_list.append(BASE_URL+stock.code+"/follows")

raw = requests.get(stocks_list[0], headers=headers, cookies=cookies_jar)
print(raw)
# raw = requests.get('https://cn.bing.com',headers=headers)
soup = BeautifulSoup(str(raw.content),"html.parser")
# number = soup.find(id="followsCount")
# number = soup.find("h2", class_="widget-title"a
number = soup.find("div", class_ = "stockInfo").span.string.split("(")[1].split(")")[0]
print(stocks_list[0])
# print(raw.content)
print(type(int(number)))
