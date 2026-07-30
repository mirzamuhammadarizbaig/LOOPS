player1score=0
player2score=0
while player1score<5 and player2score<5:
    player1=input("Player 1, choose rock, paper or scissors: ")
    player2=input("Player 2, choose rock, paper or scissors: ")
    if player1==player2:
        print("It's a tie")
    elif (player1=="rock" and player2=="scissors") or (player1=="paper" and player2=="rock") or (player1=="scissors" and player2=="paper"):
        player1score+=1
        print(f"Player 1 wins this round! Score: {player1score}-{player2score}")
    else:
        player2score+=1
        print(f"Player 2 wins this round! Score: {player1score}-{player2score}")
if player1score==5:
    print("Player 1 won the match!")
else:
    print("Player 2 won the match!")
