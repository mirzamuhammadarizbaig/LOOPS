total=0
while total<100:
    roll=int(input("Enter your dice roll (1-6): "))
    total+=roll
    print(f"Total score: {total}")
print("You reached 100! Game over")
