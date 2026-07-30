import random
playerhealth=100
enemies=0
while playerhealth>0:
    enemies+=1
    damage=random.randint(5,25)
    playerhealth-=damage
    print(f"Enemy {enemies} attacked! Took {damage} damage, health is now {playerhealth}")
print(f"You destroyed {enemies-1} enemies before dying")
