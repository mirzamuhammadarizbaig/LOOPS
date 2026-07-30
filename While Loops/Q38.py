playerhealth=100
enemies=0
while playerhealth>0:
    enemies+=1
    damage=int(input(f"Enemy {enemies} attacked, enter damage taken: "))
    playerhealth-=damage
    print(f"Health is now {playerhealth}")
print(f"You destroyed {enemies-1} enemies before dying")
