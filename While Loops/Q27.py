correctuser="admin"
correctpass="pass123"
attempts=0
while attempts<3:
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username==correctuser and password==correctpass:
        print("Login Successful")
        break
    else:
        attempts+=1
        print(f"Invalid credentials, attempts left: {3-attempts}")
else:
    print("Too many failed attempts, account locked")
