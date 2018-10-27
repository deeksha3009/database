from acc import *
while True:
	options=print("1.create account\n\
	           2.deposit\n\
	           3.withdraw\n\
	           4.show balance\n")

	ch= input("-->")


	if ch=="1":
		print("welcome")
		name=input("enter name:")
		balance=input("enter starting amount to open:")
		pin=int(input("enter a 4 digit pin:"))	  
		create_account(name,balance,pin) 

	elif ch=="2":
		amount=int(input("enter amount to deposit:"))
		a_pin=int(input("enter pin:"))
		deposit(a_pin,amount)

	elif ch=="3":
		amount=int(input("enter amount:"))
		a_pin=input("enter pin:")
		withdraw(a_pin,amount)

	elif ch=="4":
		pin=int(input("enter pin:"))
		show_balance(pin)
