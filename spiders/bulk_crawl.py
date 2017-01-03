# coding:utf-8
# this scripts should run under python3 environments
import csv
import requests
from bs4 import BeautifulSoup

#  with open('edmodo.csv', 'wb') as csvfile:
    #  fieldnames = ['title', 'posttime']
    #  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #  writer.writeheader()

for i in range(84):
    raw_page = requests.get("https://blog.edmodo.com/page/"+str(i+1)+"/")
    soup = BeautifulSoup(raw_page.content,'html.parser')
    title = soup.find_all('h3',attrs={'style':'font-size: 1.5em;'})
    time = soup.find_all('span',attrs={'class':'cfdate'})
    with open('edmodo.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        print(len(title),len(time))
        for w in range(10):
            writer.writerow([title[w].string,time[w].string])
            print(w,title[w].string,time[w].string)

#  print(soup)
#  #  print(len(cc))
#  a = title[0]
#  b = time[0]
#  print(a)
#  print(a.string)
#  print(b.string)

#print(title[0].a.content)
#print(soup[0].content)






