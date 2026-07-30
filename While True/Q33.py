counter=0

while True:
    choice=input("Press r to roll the dice or e to exit : ")

    if choice=="e":
        print("Thank you for playing")
        break

    elif choice=="r":
        index=counter%6
        result=index+1
        counter=counter+1
        print("You rolled a",result)

    else:
        print("Invalid choice")
