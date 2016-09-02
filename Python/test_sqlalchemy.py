# coding:utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# base class config
Base = declarative_base()
# create databse scheme 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    fullname = Column(String(40))
    password = Column(String(40))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

# create table
#  engine = create_engine('sqlite:///sqlalchemy_example.db')
engine = create_engine('mysql+mysqldb://root:8354210@127.0.0.1/testdb')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

test_user = User(name="test_user",fullname="test_user_no1",password="123456")
session.add(test_user)
session.commit()

session = Session()
xx = session.query(User).all()
for aa in xx:
    print(aa.fullname,aa.password,aa.id,aa)

