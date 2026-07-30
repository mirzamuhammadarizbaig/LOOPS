number=88
run=True

while run:
    guess=int(input("Guess the number\n"))
    if guess==number:
        print("Correct")
        run=False
    else:
        print("Try Again")
