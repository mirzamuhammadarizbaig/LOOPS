player_health=100
enemy_health=100

while True:
    choice=input(
        "1.Punch\n"
        "2.Kick\n"
        "3.Block\n"
    )

    if choice=="1":
        enemy_health=enemy_health-10
        print("Enemy health :",enemy_health)

    elif choice=="2":
        enemy_health=enemy_health-15
        print("Enemy health :",enemy_health)

    elif choice=="3":
        print("You blocked the attack")

    else:
        print("Invalid choice")
        continue

    if enemy_health<=0:
        print("You win!")
        break

    player_health=player_health-10
    print("Your health :",player_health)

    if player_health<=0:
        print("You lose!")
        break
