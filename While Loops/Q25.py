pin="1234"
entered=input("Enter your PIN (or 'forgot' to exit): ")
while entered!=pin:
    if entered=="forgot":
        print("Exiting PIN verification")
        break
    entered=input("Wrong PIN, try again (or 'forgot' to exit): ")
else:
    print("PIN Correct, Access Granted")
