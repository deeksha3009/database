from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
class Account(Base):
	__tablename__ ='account'

	pin=Column(Integer,primary_key=True )
	balance=Column(Integer)
	name=Column(String(100),nullable=False)



engine= create_engine("sqlite:///bank.db")

Base.metadata.create_all(engine)