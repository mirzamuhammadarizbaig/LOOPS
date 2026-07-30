registered_username=""
registered_password=""

while True:
    choice=input(
        "1.Signup\n"
        "2.Login\n"
        "3.Exit\n"
    )

    if choice=="1":
        registered_username=input("Choose a username : ")
        registered_password=input("Choose a password : ")
        print("Signup successful")

    elif choice=="2":
        username=input("Enter username : ")
        password=input("Enter password : ")

        if username==registered_username and password==registered_password:
            print("Login successful")
        else:
            print("Invalid username or password")

    elif choice=="3":
        print("Thank you for using this program")
        break

    else:
        print("Invalid choice")
