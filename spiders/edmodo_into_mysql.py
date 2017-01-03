# coding:utf-8
# this scripts should run under python3 environments

import requests
from bs4 import BeautifulSoup
from sqlalchemy import Column, Integer, String,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# base class config
Base = declarative_base()

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(300),nullable=True)
    url = Column(String(500),nullable=True)
    key_words = Column(String(300),nullable=True)
    post_time = Column(String(300),nullable=True)
    content = Column(Text(),nullable=True)
    

    def __repr__(self):
        return self.title + ":" + self.post_time


#  create table
#  engine = create_engine('sqlite:///edmodo.db')
engine = create_engine('mysql+mysqldb://root:8354210@127.0.0.1/edmodo', connect_args={'charset':'utf8mb4'})
Base.metadata.create_all(engine)


for page_number in range(84):
    # crawl basic info
    raw_page = requests.get("https://blog.edmodo.com/page/"+str(page_number+1)+"/")
    soup = BeautifulSoup(raw_page.content,'html.parser')
    titles = soup.find_all('h3',attrs={'style':'font-size: 1.5em;'})
    times = soup.find_all('span',attrs={'class':'cfdate'})
    
    for i in range(10):
        Session = sessionmaker(bind=engine)
        session = Session()
        title = titles[i].string
        time = times[i].string
        # crawl post content and key words
        url = titles[i].find_all('a')[0].attrs['href']
        raw_content = requests.get(url)
        content_soup = BeautifulSoup(raw_content.content)
        content = content_soup.find_all('div',attrs={'class':'flocontent'})[0].get_text()
        keywords = content_soup.find_all('div',attrs={'class':'flocontent'})[0].find_all('span',attrs={'class':'tags'})
        key_words =[]
        for word in keywords:
            key_words.append(word.get_text())

        new_posts = Posts(
                title = title,
                url = url,
                post_time = time,
                content = content,
                key_words = str(key_words),
        )
        session.add(new_posts)
        session.commit()
        print(page_number,i)

