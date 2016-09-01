# coding:utf-8
# this scripts should run under python3 environments

from sqlalchemy import Column, Integer, String,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import itertools
import collections
from key_value import Frency
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



engine = create_engine('mysql+mysqldb://root:8354210@127.0.0.1/edmodo',connect_args={'charset':'utf8mb4'})

#  yeas = [i for i in range(2008,2017)]
#  yeas = [2016]
#  for year in yeas:
    # session
Session = sessionmaker(bind=engine)
query_session = Session()
    # make query
    #  all_post = query_session.query(Posts).filter(Posts.post_time.like('%'+str(year)+'%')).all()
all_posts = query_session.query(Posts).all()
query_session.close()
for post in all_posts:
    words_list = []
    #  for i in all_post:
    content = post.content
    words = content.replace(',',' ').replace('.',' ').replace(':',' ').\
        replace('?',' ').replace('!',' ').replace('\n',' ').replace('%',' ').\
        replace('(',' ').replace(')',' ').replace('"',' ').replace('@',' ').replace(';',' ').replace('”',' ').replace('“ ',' ').lower()
    words_list = words.split(' ')
        #  print(words_list)
        #  words_totall_list += words_list
        #  print(len(words_totall_list))
    words_set = set(words_list)
    print(len(words_set))
    for i in words_set:
        if not i.strip() == '':
            Session = sessionmaker(bind=engine)
            write_session = Session()
            words_f = Frency(
                times=words_list.count(i),
                word=i,
                date=post.post_time,
            )
            write_session.add(words_f)
            write_session.commit()
            write_session.close()
            print(i,words_list.count(i),post.post_time)
    
#  od = collections.OrderedDict(sorted(words_frency.items()))
#  print(od)
#  for k,value in od:
    #  print(k,value)

    
    
    
