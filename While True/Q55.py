team_a_score=0
team_b_score=0
counter=0

while True:
    choice=input("Press p to play next minute or e to end match : ")

    if choice=="p":
        index=counter%3
        counter=counter+1

        if index==0:
            team_a_score=team_a_score+1
            print("Goal for Team A!")
        elif index==1:
            team_b_score=team_b_score+1
            print("Goal for Team B!")
        else:
            print("No goal this minute")

        print("Team A :",team_a_score,"Team B :",team_b_score)

    elif choice=="e":
        print("Final score, Team A :",team_a_score,"Team B :",team_b_score)
        break

    else:
        print("Invalid choice")
