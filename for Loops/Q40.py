n = int(input("How many voters?: "))
candidates = ["a", "b", "c"]
votes = [0, 0, 0]

for i in range(1, n+1):
    choice = input("Vote for A/B/C: ").lower()
    for j in range(0, len(candidates)):
        if choice == candidates[j]:
            votes[j] += 1

for j in range(0, len(candidates)):
    print(candidates[j], votes[j])

maxVotes = votes[0]
winnerIndex = 0
for j in range(0, len(votes)):
    if votes[j] > maxVotes:
        maxVotes = votes[j]
        winnerIndex = j

print("Winner is:", candidates[winnerIndex], "with", maxVotes, "votes")