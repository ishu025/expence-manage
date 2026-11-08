from datetime import date
import os
def withdraw():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "..", "data.dat")
    history_path = os.path.join(current_dir, "..", "history.dat")
    with open(data_path, "r") as current_cash:
        content = current_cash.read()
        print(f"DEBUG - Read from file: '{content}'")
        current_status = int(content.strip()) if content.strip() else 0
    withdraw_ammount = int(input("Enter withdraw amount: "))
    pourpous = input("for what: ")
    if 0 < withdraw_ammount <= current_status:
        new_balance = current_status - withdraw_ammount
        with open(data_path, "w") as write_data:
            write_data.write(str(new_balance))
        with open(history_path, "a") as history:
            history.write(f"{date.today()} : WithDraw : {pourpous} : ammount   {withdraw_ammount} \n")
        print(f"Withdrawal successful! Remaining balance: {new_balance}")
    elif withdraw_ammount > current_status:
        print("Not enough money to withdraw! Try Again")
    else:
        print("Invalid input")
