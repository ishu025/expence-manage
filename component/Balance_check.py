def balance_check():
    with open("data.dat","r") as balance:
        current_balance = balance.read()
    return current_balance
