password=1234
attempts=3

while attempts>0:
    userPassword=int(input("Enter the password: "))
    if userPassword==password:
        print("Login Succesful")
        break

    else:
        attempts-=1
        print("Wrong Password")

        if attempts>0:
            print(f"Attempts Left = {attempts}")

if attempts==0:
    print("Account locked")
       