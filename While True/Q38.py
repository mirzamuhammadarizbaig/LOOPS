votes_a=0
votes_b=0

while True:
    choice=input(
        "1.Vote for Candidate A\n"
        "2.Vote for Candidate B\n"
        "3.Show Result\n"
        "4.Exit\n"
    )

    if choice=="1":
        votes_a=votes_a+1
        print("Vote counted for Candidate A")

    elif choice=="2":
        votes_b=votes_b+1
        print("Vote counted for Candidate B")

    elif choice=="3":
        print("Candidate A :",votes_a)
        print("Candidate B :",votes_b)

    elif choice=="4":
        print("Thank you for voting")
        break

    else:
        print("Invalid choice")
