health=100
round=1
while health>0:
    damage=int(input(f"Round {round}, enter damage taken: "))
    health-=damage
    if health<0:
        health=0
    print(f"Health is now {health}")
    round+=1
print("You have died. Game over")
