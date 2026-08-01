secretNumber=32
running=True

while running:
    num=int(input("Guess the secret number: "))

    if num>secretNumber:
        print("Too high, try again")
    elif num<secretNumber:
        print("Too low, try again")
    elif num==secretNumber:
        print("You Guess the right number")
        running=False
    