from sqlalchemy.orm import declarative_base,sessionmaker
#create_engine helps to do different database task
from sqlalchemy import Column,String,DateTime,Integer,create_engine
from datetime import datetime
import os


BASE_DIR=os.path.dirname(os.path.realpath(__file__))
#site.db is created database name
connection_string="sqlite:///"+os.path.join(BASE_DIR,'site.db')

Base=declarative_base()

#using sql database
#echo gives the stepwise function carrying out in the database
engine=create_engine(connection_string,echo=True)

Session=sessionmaker()

"""

class User
    id int
    username str
    email str
    date_created datetime

"""

class User(Base):
    #table name
    __tablename__='users'
    id=Column(Integer(),primary_key=True)
    username=Column(String(25),nullable=False,unique=True)
    email=Column(String(80),unique=True,nullable=False)
    #date time to created time
    date_created=Column(DateTime(),default=datetime.utcnow())

    #to print the values in attributes
    def __repr__(self):
        return f"<User username={self.username} email={self.email} datecreated {self.date_created}"

new_user=User(id=1,username="john",email="john@gmail.com")

print(new_user)


#commit