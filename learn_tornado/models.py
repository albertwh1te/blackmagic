# coding:utf-8
from sqlalchemy import Column, Integer, String,Text,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime



Base = declarative_base()
class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True)
    post_date = Column(DateTime,default=datetime.now())
    

    def __repr__(self):
        return self.name + ":" + self.post_date
   
engine = create_engine('mysql+mysqldb://root:8354210@127.0.0.1/todo',connect_args={'charset':'utf8mb4'})
Base.metadata.create_all(engine)

#  Session = sessionmaker(bind=engine)
#  session = Session()

#  new_one = Todo(
    #  name="test1"
#  )
#  session.add(new_one)
#  session.commit()





    
    

   

