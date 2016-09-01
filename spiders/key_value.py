# coding:utf-8
from sqlalchemy import Column, Integer, String,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# base class config
Base = declarative_base()


class Frency(Base):
    __tablename__ = 'frency'
    id = Column(Integer, primary_key=True)
    times = Column(Integer)
    date = Column(String(100))
    word = Column(String(300))
    
    def __repr__(self):
        return self.word + ":" + self.times


#  create table
engine = create_engine('mysql+mysqldb://root:8354210@127.0.0.1/edmodo',connect_args={'charset':'utf8mb4'})
Base.metadata.create_all(engine)


