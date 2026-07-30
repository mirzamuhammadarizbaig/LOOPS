c1 = 0
c2 = 0
c3 = 0

for i in range(1, 101):
    vote = input(f"Voter {i} - Vote for candidate (1/2/3): ")
    if vote == "1":
        c1 += 1
    elif vote == "2":
        c2 += 1
    elif vote == "3":
        c3 += 1
    else:
        print("Invalid vote")

print("Candidate 1 votes:", c1)
print("Candidate 2 votes:", c2)
print("Candidate 3 votes:", c3)

if c1 > c2 and c1 > c3:
    print("Winner: Candidate 1")
elif c2 > c1 and c2 > c3:
    print("Winner: Candidate 2")
elif c3 > c1 and c3 > c2:
    print("Winner: Candidate 3")
else:
    print("It's a tie")
