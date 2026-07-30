number=8

while True:
    num=int(input("Guess the number: "))
    if num==number:
        print("Correct")
        break
    else:
        print("Try Again")