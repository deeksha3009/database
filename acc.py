from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bank import Account,Base

engine= create_engine("sqlite:///bank.db")
Base.metadata.bind= engine

Session=sessionmaker(bind=engine)
session=Session()

def create_account(name,balance,pin):
	account=Account(name=name,balance=balance,pin=pin)

	session.add(account)
	session.commit()

def deposit(pin,amount):
	acc=session.query(Account).filter(Account.pin==pin).one()
	acc_1=acc.balance
	acc_1+=amount
	session.commit()
	
def show_balance(pin):
	acc=session.query(Account).filter(Account.pin==pin).one()
	print(acc.name,acc.balance)


def withdrawal(pin,amount):
	acc=session.query(Account).filter(Account.pin==pin).one()
	acc_1=acc.balance
	acc_1-=amount
	session.commit()
		
	
		

