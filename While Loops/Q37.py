import random
playerhealth=100
enemyhealth=100
while playerhealth>0 and enemyhealth>0:
    playerdamage=random.randint(5,15)
    enemydamage=random.randint(5,15)
    enemyhealth-=playerdamage
    playerhealth-=enemydamage
    print(f"You dealt {playerdamage} damage, enemy dealt {enemydamage} damage")
    print(f"Player health: {playerhealth}, Enemy health: {enemyhealth}")
if playerhealth<=0:
    print("You lost the fight!")
else:
    print("You won the fight!")
