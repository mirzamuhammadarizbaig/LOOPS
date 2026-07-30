counter=0

while True:
    choice=input("Enter rock, paper or scissors (or type exit) : ")

    if choice=="exit":
        print("Thank you for playing")
        break

    index=counter%3

    if index==0:
        computer="rock"
    elif index==1:
        computer="paper"
    else:
        computer="scissors"

    counter=counter+1
    print("Computer chose",computer)

    if choice==computer:
        print("It is a tie")
    elif choice=="rock" and computer=="scissors":
        print("You win")
    elif choice=="paper" and computer=="rock":
        print("You win")
    elif choice=="scissors" and computer=="paper":
        print("You win")
    else:
        print("You lose")
