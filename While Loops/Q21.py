password="admin123"
attempts=0
while attempts<5:
    entered=input("Enter password: ")
    if entered==password:
        print("Access Granted")
        break
    else:
        attempts+=1
        print(f"Wrong password, attempts left: {5-attempts}")
else:
    print("Account locked, too many wrong attempts")
