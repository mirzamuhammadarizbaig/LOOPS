import random
health=100
round=1
while health>0:
    damage=random.randint(5,20)
    health-=damage
    if health<0:
        health=0
    print(f"Round {round}: Took {damage} damage, health is now {health}")
    round+=1
print("You have died. Game over")
