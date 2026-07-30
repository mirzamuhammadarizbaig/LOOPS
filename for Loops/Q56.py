wins = 0
losses = 0
draws = 0
points = 0
goals_scored = 0
goals_conceded = 0

for m in range(1, 11):
    gf = int(input(f"Match {m} - Goals scored by your team: "))
    ga = int(input(f"Match {m} - Goals conceded: "))

    goals_scored += gf
    goals_conceded += ga

    if gf > ga:
        wins += 1
        points += 3
        print(f"Match {m}: WIN")
    elif gf == ga:
        draws += 1
        points += 1
        print(f"Match {m}: DRAW")
    else:
        losses += 1
        print(f"Match {m}: LOSS")

print("Wins:", wins)
print("Losses:", losses)
print("Draws:", draws)
print("Total Points:", points)
print("Goals Scored:", goals_scored)
print("Goals Conceded:", goals_conceded)

if points >= 20:
    print("Champion! 🏆")
else:
    print("Not champion this season")
