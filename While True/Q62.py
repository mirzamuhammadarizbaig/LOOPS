monster_health=100
player_health=100

while True:
    choice=input("Press a to attack or r to run : ")

    if choice=="a":
        monster_health=monster_health-15
        player_health=player_health-10
        print("Monster health :",monster_health,"Your health :",player_health)

        if monster_health<=0:
            print("You defeated the monster!")
            break

        if player_health<=0:
            print("You were defeated, game over")
            break

    elif choice=="r":
        print("You ran away safely")
        break

    else:
        print("Invalid choice")
