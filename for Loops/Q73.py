total_points = 0
highest_score = 0
highest_match = 0

for m in range(1, 16):
    score = int(input(f"Enter score for match {m}: "))
    total_points += score

    if score > highest_score:
        highest_score = score
        highest_match = m

average = total_points / 15

print("Total Points:", total_points)
print("Highest Scoring Match:", highest_match, "with", highest_score, "points")
print("Average Score:", round(average, 2))
