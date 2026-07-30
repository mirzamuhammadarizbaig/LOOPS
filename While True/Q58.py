treasure_spot=3

while True:
    choice=input("Guess a spot from 1 to 5 (or type exit) : ")

    if choice=="exit":
        print("Thank you for playing")
        break

    choice=int(choice)

    if choice==treasure_spot:
        print("Congratulations, you found the treasure!")
        break
    else:
        print("No treasure here, try again")
