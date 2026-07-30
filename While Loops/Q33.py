import random
total=0
while total<100:
    roll=random.randint(1,6)
    total+=roll
    print(f"You rolled a {roll}, total score: {total}")
print("You reached 100! Game over")
