correct_pin="1234"

while True:
    pin=input("Enter your PIN : ")

    if pin==correct_pin:
        print("PIN accepted")
        break
    else:
        print("Wrong PIN, try again")
