def login():
    user_name = input("UserName: ")
    password = input("Password: ")
    if user_name == "ishu" and password == "ishu":
        return True
    else:
        return False