import random
options=["rock","paper","scissors"]
playerscore=0
computerscore=0
while playerscore<5 and computerscore<5:
    player=input("Choose rock, paper or scissors: ")
    computer=random.choice(options)
    print(f"Computer chose {computer}")
    if player==computer:
        print("It's a tie")
    elif (player=="rock" and computer=="scissors") or (player=="paper" and computer=="rock") or (player=="scissors" and computer=="paper"):
        playerscore+=1
        print(f"You win this round! Score: {playerscore}-{computerscore}")
    else:
        computerscore+=1
        print(f"Computer wins this round! Score: {playerscore}-{computerscore}")
if playerscore==5:
    print("You won the match!")
else:
    print("Computer won the match!")
