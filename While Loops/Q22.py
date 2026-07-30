pin="4321"
attempts=0
locked=False
while attempts<3 and not locked:
    entered=input("Enter your PIN: ")
    if entered==pin:
        print("PIN Correct, Access Granted")
        break
    else:
        attempts+=1
        print("Wrong PIN")
        if attempts==3:
            locked=True
            print("Account Locked")
