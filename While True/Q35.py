correct_username="ariz"
correct_password="pass123"

while True:
    username=input("Enter username (or type exit) : ")

    if username=="exit":
        print("Thank you for using this program")
        break

    password=input("Enter password : ")

    if username==correct_username and password==correct_password:
        print("Login successful")
    else:
        print("Invalid username or password")
