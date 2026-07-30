total_score = 0
highest_score = 0
highest_round = 0

for r in range(1, 26):
    points = int(input(f"Enter points earned in round {r}: "))
    total_score += points

    if points > highest_score:
        highest_score = points
        highest_round = r

print("Total Score:", total_score)
print("Best Round:", highest_round, "with", highest_score, "points")
