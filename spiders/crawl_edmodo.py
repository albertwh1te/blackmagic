# coding:utf-8
# this scripts should run under python3 environments

import requests
from bs4 import BeautifulSoup


raw_page = requests.get("https://blog.edmodo.com/page/2/")
soup = BeautifulSoup(raw_page.content)
title = soup.find_all('h3',attrs={'style':'font-size: 1.5em;'})
#  time = soup.find_all('span',attrs={'class':'cfdate'})

#  print(soup)
#  print(len(cc))
#  a = title[0]
#  b = time[0]
#  print(a)
#  print(a.string)
#  print(b.string)
url = title[0].find_all('a')[0]
url = url.attrs['href']
raw_content = requests.get(url)
content_soup = BeautifulSoup(raw_content.content)
#  content = content_soup.find_all('div',attrs={'class':'flocontent'})
content = content_soup.find_all('div',attrs={'class':'flocontent'})[0].get_text()
print(content)
#  keywords = content_soup.find_all('div',attrs={'class':'flocontent'})[0].find_all('span',attrs={'class':'tags'})
#  key_words =[]

#  for word in keywords:
    #  #  print(word,word.string,word.get_text())
    #  key_words.append(word.get_text())


#  print(str(key_words))
#  print(title[0])
#  print(title[0].find_all('a'))
#  print(title[0].find_all('a')[0].attrs['href'])
#print(soup[0].content)
#  print(content)
#  print(content[0].string)
#  print(len(content))
#  print(content)
#  with open('test.txt','a') as cc:
    #  cc.write(content)
    #  cc.close()





