player_mana=100
enemy_health=100

while True:
    choice=input(
        "1.Fireball (30 mana)\n"
        "2.Lightning (50 mana)\n"
        "3.Exit\n"
    )

    if choice=="1":
        if player_mana<30:
            print("Not enough mana")
        else:
            player_mana=player_mana-30
            enemy_health=enemy_health-20
            print("Enemy health :",enemy_health,"Your mana :",player_mana)

    elif choice=="2":
        if player_mana<50:
            print("Not enough mana")
        else:
            player_mana=player_mana-50
            enemy_health=enemy_health-40
            print("Enemy health :",enemy_health,"Your mana :",player_mana)

    elif choice=="3":
        print("Thank you for playing")
        break

    else:
        print("Invalid choice")
        continue

    if enemy_health<=0:
        print("You defeated the enemy, you win!")
        break
