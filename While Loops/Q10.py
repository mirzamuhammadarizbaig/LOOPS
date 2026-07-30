correctPassword = "miti123"

password = input("Enter Password: ")

while password != correctPassword:

    print("Wrong Password!")

    password = input("Enter Password: ")

print("Access Granted!")