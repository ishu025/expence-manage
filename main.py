from component.login import login
from component.Balance_check import balance_check
from component.welcome import home
from component.withdraw import withdraw
from component.deposit import Deposit
while True:
    login_value = login()
    if login_value == True:
        print("sucessfull")
        break
    elif login_value == False:
        print("incorrect username or password ! Try Again")
home()
while True:
    choice = int(input(">>>"))
    if choice == 1:
        print(f"₹ {balance_check()}")
    elif choice == 2:
        withdraw()
    elif choice == 3:
        Deposit()