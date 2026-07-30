correct_pin="1234"
attempts=0

while True:
    if attempts>=3:
        print("Card blocked due to too many wrong attempts")
        break

    pin=input("Enter your PIN : ")

    if pin==correct_pin:
        print("PIN accepted, welcome")
        break
    else:
        attempts=attempts+1
        print("Wrong PIN, attempts left :",3-attempts)
