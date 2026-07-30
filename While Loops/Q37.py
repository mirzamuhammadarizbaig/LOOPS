playerhealth=100
enemyhealth=100
while playerhealth>0 and enemyhealth>0:
    playerdamage=int(input("Enter damage dealt to enemy: "))
    enemydamage=int(input("Enter damage dealt to player: "))
    enemyhealth-=playerdamage
    playerhealth-=enemydamage
    print(f"Player health: {playerhealth}, Enemy health: {enemyhealth}")
if playerhealth<=0:
    print("You lost the fight!")
else:
    print("You won the fight!")
