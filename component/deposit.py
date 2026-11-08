from datetime import date
def Deposit():
    with open("data.dat","r") as current_cash:
        current_status = current_cash.read()
    Deposit_ammount = int(input("Enter Deposit ammount: "))
    pourpous = input("for what: ")
    if Deposit_ammount != 0:
        with open("data.dat","w") as write_data:
            write_data.write(current_status - Deposit_ammount)
        with open("history.dat","a") as history:
            history.write(f"{date.today()} : Deposit : {pourpous} \n")
    elif Deposit_ammount == 0:
        print("please enter Ammount and try again :!:")
    else:
        print("Invalid input")