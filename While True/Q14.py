correct_username="ariz"

while True:
    username=input("Enter your username : ")

    if username==correct_username:
        print("Welcome",username)
        break
    else:
        print("Wrong username, try again")
